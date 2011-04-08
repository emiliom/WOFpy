
import soaplib
import logging

from werkzeug.wsgi import DispatcherMiddleware
from soaplib.core.server import wsgi

import wof
import OdmSqlAlchDao


from wofpy_soap.soap import WOFService
from wofpy_flask import config
from wofpy_flask import create_app

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    
    #TODO: How to run two flask apps simultaneously?
    # See Application Factories: http://flask.pocoo.org/docs/patterns/appfactories/
    # think I need to make a factory for wof as well? and set reference to it
    # in the created flask_app
    
    flask_app = create_app()
    flask_app.config.from_object(config.DevConfig)
    
    wof.config_from_file('config/lbr_config.cfg')
    wof.dao = OdmSqlAlchDao.OdmSqlAlchDao()
    
    soap_app = soaplib.core.Application(services=[WOFService],
        tns='http://www.cuahsi.org/his/1.0/ws/',
        name='WaterOneFlow')

    soap_wsgi_app = soaplib.core.server.wsgi.Application(soap_app)
    
    flask_app.wsgi_app = DispatcherMiddleware(flask_app.wsgi_app, {
        '/soap': soap_wsgi_app
    })
    
    flask_app.run(host='0.0.0.0', port=8080, threaded=True)