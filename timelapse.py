# Imports for heatmap
import csv
import pandas as pd
import folium
from folium.plugins import HeatMapWithTime
from flask import Markup

def get_timelapse():
    file = "Data/all_data.csv"
    param = "Ozone"
    # get the data
    histData = pd.read_csv(file, parse_dates=['Date'])

    histData['year'] = (histData['Date'].dt.year)
    histData['month'] = (histData['Date'].dt.month)
    histData['day'] = 1
    histData['newDate'] = pd.to_datetime(histData[['year', 'month', 'day']])

    #Reorder columns
    columns = ['newDate', 'Latitude', 'Longitude', 'AQI', 'Defining_Parameter','county_name']
    reorderData = histData[columns]
    
    # Get only the data for the parameter
    paramData = reorderData.loc[reorderData['Defining_Parameter'] == param]

    sortedhistData = paramData.sort_values(by=['newDate'])

    newhistData = sortedhistData.reset_index()
    newhistData.drop(columns=['index'], inplace=True)

    mapData=newhistData[["newDate", "Latitude", "Longitude", "AQI", 'Defining_Parameter']]
    # Create list of lists, with the "key" of the list being the date, and the "value" being all measurements for that date.
    # 1. Need list of date
    mapTime = []
    mapTime = mapData["newDate"].sort_values().unique()


    # 2. create the lists
    mapData_list = []
    
    # Weight must be between 0 and 1.  Divide AQI by max value to get correct data
    minAQI = mapData["AQI"].min()
    maxAQI = mapData['AQI'].max()

    mapData["AQI_adj"] = mapData["AQI"]/maxAQI
    
    for date in mapTime:
        mapData_list.append(mapData.loc[mapData['newDate'] == date, ["Latitude", "Longitude", "AQI_adj"]].groupby(["Latitude", "Longitude"]).mean().reset_index().values.tolist())

    # create the base map
    start_coords = (36.7378, -119.7871)
    folium_map = folium.Map(location=start_coords, zoom_start=6, tiles='Stamen Terrain')

    #add the Heat Map from the data
    HeatMapWithTime(data=mapData_list, radius=20, auto_play=True, overlay=False, max_opacity=0.3,
                       gradient = {0.2: '#FBD973', 
                            0.4: '#fa782f', 
                            0.75: '#F16578', 
                            .9: '#782890'}).add_to(folium_map)

    # display base map with HeatMap 
    _ = folium_map._repr_html_()

    map_id = Markup(folium_map.get_root().html.render())
    hdr_txt = Markup(folium_map.get_root().header.render())
    script_txt = Markup(folium_map.get_root().script.render())

    return([map_id, hdr_txt, script_txt])

get_timelapse()