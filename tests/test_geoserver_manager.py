import unittest
import os
from geobricks_geoserver_manager.config.config import config
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
from geobricks_common.core.log import logger

log = logger(__file__)

class GeobricksTest(unittest.TestCase):

    def setUp(self):
        self.workspace = "workspace_test"

    def test_publish_raster(self):
        path = getAbsPath("data/raster/MOD13A2_3857.tif")
        data = {
            "layerName": "MOD13A2_3857",
            "workspace": self.workspace,
        }
        geoserver_manager = GeoserverManager(config)
        result = geoserver_manager.publish_coveragestore(path, data, True)
        self.assertEqual(result, True)

    def test_publish_shapefile(self):
        path = {
            'shp': getAbsPath('data/shp/gaul0_malta_4326.shp'),
            'shx': getAbsPath('data/shp/gaul0_malta_4326.shx'),
            'dbf': getAbsPath('data/shp/gaul0_malta_4326.dbf'),
            'prj': getAbsPath('data/shp/gaul0_malta_4326.prj')
        }
        # an alternative could be the zip file, but gsconfig delete it afterwards
        # path = "data/shp/gaul0_malta_4326.zip"
        data = {
            "layerName": "gaul0_malta_4326",
            "workspace": self.workspace,
        }
        geoserver_manager = GeoserverManager(config)
        result = geoserver_manager.publish_shapefile(path, data, True)
        self.assertEqual(result, True)

    def test_publish_sld(self):
        path = getAbsPath('data/sld/test.sld')
        # TODO: use the same structure also for the SLD?
        # an alternative could be the zip file, but gsconfig delete it afterwards
        # path = "data/shp/gaul0_malta_4326.zip"
        # data = {
        #     "layerName": "gaul0_malta_4326",
        #     "workspace": self.workspace,
        # }
        geoserver_manager = GeoserverManager(config)
        result = geoserver_manager.publish_style(path, None, self.workspace, True)
        self.assertEqual(result, True)


def getAbsPath(path):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), path))


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_test()
