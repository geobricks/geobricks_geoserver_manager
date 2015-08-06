import unittest
import os
from geobricks_geoserver_manager.config.config import config
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
from geobricks_common.core.log import logger

log = logger(__file__)



class GeobricksTest(unittest.TestCase):

    def test_publish_raster(self):
        path = os.path.abspath("data/raster/MOD13A2_3857.tif")
        data = {
            "layerName": "MOD13A2_3857",
            "workspace": "workspace_test",
        }
        geoserver_manager = GeoserverManager(config)
        result = geoserver_manager.publish_coveragestore(path, data, True)
        self.assertEqual(result, True)

    def test_publish_shapefile(self):
        path = {
            'shp': os.path.abspath('data/shp/gaul0_malta_4326.shp'),
            'shx': os.path.abspath('data/shp/gaul0_malta_4326.shp'),
            'dbf': os.path.abspath('data/shp/gaul0_malta_4326.dbf'),
            'prj': os.path.abspath('data/shp/gaul0_malta_4326.prj')
        }
        # an alternative could be the zip file, but gsconfig delete it afterwards
        # path = "data/shp/gaul0_malta_4326.zip"
        data = {
            "layerName": "gaul0_malta_4326",
            "workspace": "workspace_test",
        }
        geoserver_manager = GeoserverManager(config)
        result = geoserver_manager.publish_shapefile(path, data, True)
        self.assertEqual(result, True)


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_test()
