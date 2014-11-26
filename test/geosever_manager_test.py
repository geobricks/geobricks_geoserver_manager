from geoserver_settings_test import config
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
from geobricks_processing.utils.log import logger

log = logger("geoserver_manager_test")

geoserver_manager = GeoserverManager(config)

data_coverage = {
    "layerName": "MOD13A2_3857",
    "path": "../test_data/MODIS/MOD13A2/MOD13A2_3857.tif",
    "workspace": "workspace_test",
}

# deleting
try:
    geoserver_manager.delete_store(data_coverage["layerName"])
    #geoserver_manager.delete_layer(data_coverage["name"])
except Exception, e:
    log.error(e)

# publishing
try:
    geoserver_manager.publish_coveragestore(data_coverage)
except Exception, e:
    log.error(e)


# publishing

data_postgis_table = {
    "layerName": "gaul0_3857_test",
    "store": "daje-fenix",
    "workspace": "daje",
    "defaultStyle": "gaul0_highlight_polygon"
}

try:
    geoserver_manager.delete_layer(data_postgis_table["layerName"])
except Exception, e:
    log.error(e)


try:
    store = geoserver_manager.gs_master.get_store(data_postgis_table["store"])
    geoserver_manager.publish_postgis_table(data_postgis_table)
except Exception, (response, status):
    log.error(response)
    log.error(status)

