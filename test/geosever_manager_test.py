from geoserver_settings_test import config
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
from geobricks_processing.utils.log import logger

log = logger("geoserver_manager_test")

geoserver_manager = GeoserverManager(config)

data_coverage = {
    "name": "test_gsconfig11",
    "path": "/home/vortex/Desktop/LAYERS/MOROCCO_MICHELA/to_publish/original/wheat_mask.tif",
    "workspace": "daje",
    "defaultStyle": "mask"
}


# publishing
# try:
#     #geoserver_manager.delete_store(data_coverage["name"])
#     #geoserver_manager.delete_layer(data_coverage["name"])
#     #geoserver_manager.publish_coveragestore(data_coverage)
# except Exception, e:
#     log.error(e)


# publishing

data_postgis_table = {
    "name": "gaul0_3857_test",
    "store": "daje-fenix",
    "workspace": "daje",
    "defaultStyle": "gaul0_highlight_polygon"
}

try:
    geoserver_manager.delete_layer(data_postgis_table["name"])
except Exception, e:
    log.error(e)


try:
    store = geoserver_manager.gs_master.get_store(data_postgis_table["store"])
    geoserver_manager.publish_postgis_table(data_postgis_table)
except Exception, (response, status):
    log.error(response)
    log.error(status)

