from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager

config = {
    "settings" : {
        # geoserver settings
        "geoserver": {
            "geoserver_master": "http://168.202.28.214:10001/geoserver/rest",
            "geoserver_slaves": [],
            "username": "admin",
            "password": "geoserver",
            }
    }
}

geoserver_manager = GeoserverManager(config)
print geoserver_manager
cat = geoserver_manager.gs_master
styles = cat.get_styles()
for style in styles:
    if "ghg_" in style.name and "_EN" not in style.name:
        try:
            print style.name
            #cat.create_style(style.name + "_EN", style.sld_body)
            # a style can be deleted if is not used as default layer by any layey in the catalog
            cat.delete(style)
        except Exception, e:
            print e

