from geoserver.catalog import Catalog
from geoserver.resource import FeatureType
from geobricks_common.core.log import logger
from geobricks_common.core.filesystem import sanitize_name

log = logger(__file__)

class GeoserverManager():

    gs_master = None
    gs_slaves = []

    def __init__(self, config, disable_ssl_certificate_validation=False):
        # settings
        config = config["settings"]["geoserver"]
        # log.info(config["geoserver_master"])
        # log.info(config["password"])
        # log.info(config["username"])
        self.config = config
        if "geoserver_master" in config:
            print config["geoserver_master"]
            self.gs_master = Catalog(config["geoserver_master"], self.config["username"], self.config["password"])
        else:
            raise Exception('config["geoserver_master"] has to be mapped to a running Geoserver')
        if "geoserver_slaves" in config:
            for gs_slave in config["geoserver_slaves"]:
                self.gs_slaves.append(Catalog(gs_slave, self.config["username"], self.config["password"]))

    def _initialize_geoserver(self, geoserver):
        geoserver.username = self.config["username"]
        geoserver.password = self.config["password"]

    def publish_coveragestore(self, path, data, overwrite=False, reload_gs_slaves=True):
        log.info(data)
        workspace = self.gs_master.get_default_workspace() if "workspace" not in data else self.check_workspace(data["workspace"], False)
        if "layerName" not in data:
            raise Exception("No layerName found in the metadata")

        name = data["layerName"]

        # publish
        self.gs_master.create_coveragestore(name, path, workspace, overwrite)

        # setting default style
        if "defaultStyle" in data:
            self.set_style(name, workspace.name, data["defaultStyle"], False)

        # reload geoserver slaves
        if reload_gs_slaves:
            self.reload_gs_slaves()
        return True

    def publish_postgis_table(self, data, reload_gs_slaves=True, native_crs=None, srs=None, overwrite=False):
        try:
            '''Publish a featuretype from data in an existing store'''
            # @todo native_srs doesn't seem to get detected, even when in the DB
            # metadata (at least for postgis in geometry_columns) and then there
            # will be a misconfigured layer
            name = data["layerName"]
            title = data["title"] if "title" in data else name
            store = self.gs_master.get_store(data["store"])
            # #if native_crs is None: raise ValueError("must specify native_crs")
            #srs = srs or native_crs
            feature_type = FeatureType(self, store.workspace, store, name)
            # because name is the in FeatureType base class, work around that
            # and hack in these others that don't have xml properties
            feature_type.dirty['name'] = name
            # feature_type.dirty['srs'] = srs
            # feature_type.dirty['nativeCRS'] = native_crs
            feature_type.enabled = True
            feature_type.title = title
            headers = {
                "Content-type": "application/xml",
                "Accept": "application/xml"
            }
            headers, response = self.gs_master.http.request(store.resource_url, "POST", feature_type.message(), headers)
            if headers.status != 201:
                raise Exception(response, headers.status)

            # defaultStyle
            if "defaultStyle" in data:
                # TODO: test it
                self.set_style(name, store.workspace.name, data["defaultStyle"], False)

            # reload geoservers
            if reload_gs_slaves:
                self.reload_gs_slaves()

            return feature_type
        except Exception, (response, status):
            raise Exception(response, status)

    def set_style(self, layer_name, workspace, style_name, reload_gs_slaves=True):
        log.info(layer_name)
        log.info(style_name)
        log.info(workspace)
        layer = self.gs_master.get_layer(workspace + ":" +layer_name)
        log.info(layer)
        layer._set_default_style(style_name)
        self.gs_master.save(layer)
        if reload_gs_slaves:
            self.reload_gs_slaves()

    def publish_style(self, name, data, overwrite=True, reload_gs_slaves=True):
        # TODO: there is no return in the function (add it to gsconfig library)
        self.gs_master.create_style(name, data, overwrite)
        print self.gs_master.username, self.gs_master.password
        if reload_gs_slaves:
            self.reload_gs_slaves()

    def delete_style(self, name, workspace=None, reload_gs_slaves=True):
        # TODO: there is no return in the function (add it to gsconfig library)
        style = self.gs_master.get_style(name, workspace)
        self.gs_master.delete(style)
        print self.gs_master.username, self.gs_master.password
        if reload_gs_slaves:
            self.reload_gs_slaves()

    def delete_store(self, name, workspace=None, purge=True, recurse=True, reload_gs_slaves=True):
        store = self.gs_master.get_store(name, workspace)
        self.gs_master.delete(store, purge, recurse)
        # reload slaves
        if reload_gs_slaves:
            self.reload_gs_slaves()
        return True

    #def delete_layer(self, name, purge=True, recurse=True, reload_gs_slaves=True):
    def delete_layer(self, name,  workspace=None, purge=True, recurse=True, reload_gs_slaves=True):
        layer = self.gs_master.get_layer(name, workspace)
        self.gs_master.delete(layer, purge, False)
        # reload slaves
        if reload_gs_slaves:
            self.reload_gs_slaves()

    def check_workspace(self, name, reload_gs_slaves=True, uri=None):
        uri = self.gs_master.service_url + "/" + name
        print uri
        if self.gs_master.get_workspace(name) is None:
            self.gs_master.create_workspace(name, uri)
        if reload_gs_slaves:
            self.reload_gs_slaves()
        return self.gs_master.get_workspace(name)

    def get_default_workspace_name(self):
        return self.gs_master.get_default_workspace().name

    def reload_gs_slaves(self, reload_gs_master=False):
        if reload_gs_master: self.gs_master.reload()
        for gs_slave in  self.gs_slaves:
            self.gs_slave.reload()


def check_name(name, sanitize=True):
    """
    This method check the names, should be avoided to use dots as names and white spaces
    :param name: name of the layer
    :return: True False and in case a sanitized name
    """
    if "." in name or " " in name or name.islower() is False:
        if sanitize:
            return False, sanitize_name(name)
        else:
            False
    return True