<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>20120812</sld:Name>
            <sld:Title/>
            <sld:FeatureTypeStyle>
                <sld:Name>name</sld:Name>
                <sld:FeatureTypeName>Feature</sld:FeatureTypeName>
                <sld:Rule>
                    <sld:RasterSymbolizer>
                        <sld:Geometry>
                            <ogc:PropertyName>geom</ogc:PropertyName>
                        </sld:Geometry>
                        <sld:ColorMap type="intervals">
                            <sld:ColorMapEntry color="#ffffff" opacity="0.00000000001" quantity="0.00000000001" label="Ha (Hectares)"/>
                            <sld:ColorMapEntry color="#ffffb2" opacity="1.0" quantity="100" label="Low (0-100)"/>                         
                            <sld:ColorMapEntry color="#fecc5c" opacity="1.0" quantity="500" label="Low-Average (100-500)"/>                          
                            <sld:ColorMapEntry color="#fd8d3c" opacity="1.0" quantity="5000" label="Average (500-1000)"/>                          
                            <sld:ColorMapEntry color="#f03b20" opacity="1.0" quantity="10000" label=" High-Average (5000-10000)"/>                          
                            <sld:ColorMapEntry color="#bd0026" opacity="1.0" quantity="500000" label="High (> 10000)"/>                          
                        </sld:ColorMap>
                    </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>