# import unittest
# from geobricks_geoserver_manager.config.config import config
# from geobricks_common.core.log import logger
# from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
# from geobricks_common.core.filesystem import get_filename
# import glob
#
# log = logger(__file__)
#
#
# data_coverage = {
#     "layerName": "MOD13A2_3857",
#     "workspace": "workspace_test",
# }
# path = "../test_data/MODIS/MOD13A2/MOD13A2_3857.tif"
#
#
#
# # Example of publish postgis tables
# # data_postgis_table = {
# #     "layerName": "gaul0_3857_test",
# #     "store": "daje-fenix",
# #     "workspace": "daje",
# #     "defaultStyle": "gaul0_highlight_polygon"
# # }
# #
# # try:
# #     geoserver_manager.delete_layer(data_postgis_table["layerName"])
# # except Exception, e:
# #     log.error(e)
# #
# #
# # try:
# #     store = geoserver_manager.gs_master.get_store(data_postgis_table["store"])
# #     geoserver_manager.publish_postgis_table(data_postgis_table)
# # except Exception, (response, status):
# #     log.error(response)
# #     log.error(status)
#
#
# class GeobricksTest(unittest.TestCase):
#
#     def test_publish_coveragestore(self):
#         geoserver_manager = GeoserverManager(config)
#         result = geoserver_manager.publish_coveragestore(path, data_coverage)
#         self.assertEqual(result, True)
#
#     def test_delete_coveragestore(self):
#         geoserver_manager = GeoserverManager(config)
#         result = geoserver_manager.delete_store(data_coverage["layerName"])
#         self.assertEqual(result, True)
#
#     # def test_import_slds(self):
#     #     geoserver_manager = GeoserverManager(config)
#     #     for path in glob.glob("/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/*.sld"):
#     #         with open(path, 'r') as f:
#     #             data = f.read()
#     #             filename = get_filename(path)
#     #             print data
#     #             print filename
#     #
#     #
#     #             geoserver_manager.publish_style(filename, data)
