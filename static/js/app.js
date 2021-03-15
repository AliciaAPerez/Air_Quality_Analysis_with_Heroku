function buildPlot() {
    // Seting Up Initial Map Center and Zoom Level
    const map = L.map('map', {
        center: [36.7378, -119.7871],
        zoom: 7, 
        scrollWheelZoom: false,
        tap: false
    });

    // Control panel to display map layers
    const controlLayers = L.control.layers( null, null, {
    position: "topright",
    collapsed: false
    }).addTo(map);

    // Display Carto Basemap Tiles with Light Features and Labels
    // This will be the Default Map
    const light = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>'
    }).addTo(map); 

    controlLayers.addBaseLayer(light, 'Carto Light basemap');

    // Stamen Colored Terrain Basemap Tiles with Labels //
    const terrain = L.tileLayer('https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.'
    }); 

    controlLayers.addBaseLayer(terrain, 'Stamen Terrain basemap');

    function markerColor(aqi) {
        if (aqi <= 50) {
            return "green"
        } else if (aqi <= 51 &&  aqi <= 100) {
            return "yellow"
        } else if (aqi <= 101 && aqi <= 150) {
            return "orange"
        } else if (aqi <= 151 && aqi <= 200) {
            return "red"
        } else if (aqi <= 201 && aqi <= 300) {
            return "purple"
        } else {
            return "maroon"
        }
    }
    // Read markers data from data.csv
    d3.json("currentAQIData").then(function(AQIData) {
        console.log(AQIData)
        
        const data = AQIData.data;

        console.log(data)
        
        // var CurrentAQIValue = data.CurrentAQIValue.map(data => data.CurrentAQIValue);

        // for (let [key, value] of Object.entries(data)) {
        // var dataJSON = JSON.parse(data);
        
        var CurrentAQIValue = []
        var Latitude = []
        var Longitude = []
        var CurrentPollutant = []
        
        for (var index = 0; index < data.length; index++) {
            var aqiData = data[index];
            // console.log(aqiData)
            // console.log(aqiData.CurrentAQIValue)};

            CurrentAQIValue = aqiData.CurrentAQIValue.toString()
                let marker = L.circle([aqiData.Latitude, aqiData.Longitude], {
                radius: 7500,
                fillOpacity: 0.50,
                stroke: false,
                fillColor: markerColor(aqiData.CurrentAQIValue)
                }).bindPopup("<strong>" + aqiData.CurrentPollutant + "</strong><br>" + 
                    "<h3>"+ CurrentAQIValue + "</h3>");
                console.log(marker);
                marker.addTo(map);
            }

    
    map.attributionControl.setPrefix(
        'View <a href="https://github.com/HandsOnDataViz/leaflet-map-csv" target="_blank">code on GitHub</a>'
    )
}
)};



buildPlot();