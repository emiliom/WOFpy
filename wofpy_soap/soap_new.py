import StringIO
import logging
import soaplib #soaplib 2.0.0-beta

import wof.code

from soaplib.core.model.base import Base
from soaplib.core.service import rpc, soap, DefinitionBase
from soaplib.core.model.primitive import String, Any, Integer, Float, DateTime
from soaplib.core.model.clazz import Array, ClassModel


logger = logging.getLogger(__name__)

NSDEF = 'xmlns:gml="http://www.opengis.net/gml" \
    xmlns:xlink="http://www.w3.org/1999/xlink" \
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" \
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \
    xmlns:wtr="http://www.cuahsi.org/waterML/" \
    xmlns="http://www.cuahsi.org/waterML/1.0/"'


class SiteInfoResponseType(ClassModel):
    queryInfo = QueryInfoType
    #site = 

class QueryInfoType(ClassModel):
    creationTime = DateTime
    queryURL = String
    querySQL = String
    #criteria
    #note
    #extension

class SiteInfoType(SourceInfoType):
    pass

class SourceInfoType(ClassModel):
    pass

class DataSetInfoType(ClassModel):
    pass

class GeogLocationType(ClassModel):
    pass

class LatLonBoxType(ClassModel):
    pass

class LatLonPointType(ClassModel):
    pass

class seriesCatalogType(ClassModel):
    pass

class VariableInfoType(ClassModel):
    pass

class ArrayOfOption(ClassModel):
    pass

class UnitsType(ClassModel):
    pass

class TimePeriodType(ClassModel):
    pass

class TimeIntervalType(ClassModel):
    pass

class TimeSingleType(ClassModel):
    pass

class TimePeriodRealTimeType(ClassModel):
    pass

class MethodType(ClassModel):
    pass

class SourceType(ClassModel):
    pass

class MetaDataType(ClassModel):
    pass

class ContactInformationType(ClassModel):
    pass

class QualityControlLevelType(ClassModel):
    pass

class VariablesResponseType(ClassModel):
    pass

class ArrayOfVariableInfoType(ClassModel):
    pass

class TimeSeriesResponseType(ClassModel):
    pass

class TimeSeriesType(ClassModel):
    pass

class TsValuesSingleVariableType(ClassModel):
    pass

class ValueSingleVariable(ClassModel):
    pass

class OffsetType(ClassModel):
    pass


class WOFService(DefinitionBase):
        
    @soap(Array(String), String, _returns=Any)
    def GetSites(self, site, authToken):
        
        siteArg = ','.join(str(s) for s in site)
        
        logging.debug(site)
        logging.debug(siteArg)
        
        
        siteResponse = wof.code.create_get_site_response(siteArg)
        outStream = StringIO.StringIO()
        siteResponse.export(outStream, 0, name_="sitesResponse",
                            namespacedef_= NSDEF)
        
        return outStream.getvalue()
    
    @soap(Array(String), String, _returns=String)
    def GetSitesXml(self, site, authToken): #This is the one that returns WITH <![CDATA[...]]>
        
        siteArg = ','.join(str(s) for s in site)
        
        siteResponse = wof.code.create_get_site_response(siteArg)
   
        outStream = StringIO.StringIO()
        siteResponse.export(outStream, 0, name_="sitesResponse",
                            namespacedef_= NSDEF)
        
        return str(outStream.getvalue()).replace('\n','')
    
    ###########################################################################
    
    @soap(String, String, _returns=String)
    def GetSiteInfo(self,site,authToken):
        
        siteInfoResponse = wof.code.create_get_site_info_response(site)
        
        outStream = StringIO.StringIO()
        siteInfoResponse.export(outStream, 0, name_="siteInfoResponse",
                                namespacedef_= NSDEF)
     
        return str(outStream.getvalue()).replace('\n','')
    
    @soap(String, String, _returns=Any)
    def GetSiteInfoObject(self,site,authToken):
        
        siteInfoResponse = wof.code.create_get_site_info_response(site)
        
        outStream = StringIO.StringIO()
        siteInfoResponse.export(outStream, 0, name_="siteInfoResponse",
                                namespacedef_= NSDEF)
     
        return outStream.getvalue()
    
    ###########################################################################
    
    @soap(String, String, _returns=String)
    def GetVariableInfo(self, variable, authToken):
        
        variableInfoResponse = wof.code.create_variable_info_response(variable)
        
        outStream = StringIO.StringIO()
        variableInfoResponse.export(outStream, 0, name_="variablesResponse",
                                    namespacedef_= NSDEF)
        
        return str(outStream.getvalue()).replace('\n','')
    
    @soap(String, String, _returns=Any)
    def GetVariableInfoObject(self, variable, authToken):
        
        variableInfoResponse = wof.code.create_variable_info_response(variable)
        
        outStream = StringIO.StringIO()
        variableInfoResponse.export(outStream, 0, name_="variablesResponse",
                                    namespacedef_= NSDEF)
        
        return outStream.getvalue()
    
    ###########################################################################

    @soap(String, String, String, String, _returns=String)
    def GetValues(self, location, variable, startDate, endDate):
        
        timeSeriesResponse = wof.code.create_get_values_response(
            location,variable,startDate,endDate)
           
        outStream = StringIO.StringIO()
        timeSeriesResponse.export(outStream, 0, name_="timeSeriesResponse",
                                  namespacedef_= NSDEF)
        
        return str(outStream.getvalue()).replace('\n','')
    
    @soap(String, String, String, String, _returns=Any)
    def GetValuesObject(self, location, variable, startDate, endDate):
        
        timeSeriesResponse = wof.code.create_get_values_response(
            location,variable,startDate,endDate)
           
        outStream = StringIO.StringIO()
        timeSeriesResponse.export(outStream, 0, name_="timeSeriesResponse",
                                  namespacedef_= NSDEF)
        
        return outStream.getvalue()
    
