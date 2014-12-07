Geobricks Manager for Geoserver Clusters
=====================

The main purpose of this project is to provide a configurable entry point to handle a cluster of Geoservers.
It uses as dependency [gscofing](https://github.com/boundlessgeo/gsconfig) as base REST engine to publish the data.

Example to configure a cluster of Geoservers
```python
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager

config = {
    "geoserver_master": "http://localhost:9090/geoserver/rest",
    "geoserver_slaves": [],
    "username": "admin",
    "password": "geoserver"
}
geoserver_manager = GeoserverManager(config)
```

Example of how to publish a coveragestore

```python

data_coverage = {
    "layerName": "raster_name",
    "path": "../test_data/MODIS/MOD13A2_3857.tif",
    # optional workspace (otherwise it uses the default Geoserver master one)
    "workspace": "test_workspace",
    # optional style to be applied to the layer
    "defaultStyle": "mask"
}
geoserver_manager.publish_coveragestore(data_coverage)
```
