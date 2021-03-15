# Air_Quality_Analysis
Tell your story web visualization Project 2

## Table of Contents 
* [Inspiration](#Inspiration)  
* [Team Members](#Team-members) 
* [General Info](#General-info) 
* [Technologies](#technologies)  
* [Setup](#setup)  
* [Data Sources](#data-sources)
* [Visuals](#visuals) 
* [Overview](#overview)  



## **Inspiration:**
>- Analyze Air Quality in California by county & compare to demographic information from the Census data. Information can be useful for businesses to make saftey decisions on outdoor working employee's health.

## **Team members:**
>- **Julia Headlee**  [Git Hub: julieheadlee](https://github.com/julieheadlee)
>- **Melanie Nolker** [Git Hub: mnolker](https://github.com/mnolker)
>- **Alicia Perez** [Git Hub: AliciaAPerez](https://github.com/AliciaAPerez)
>- **Kayla St. Germain** [Git Hub: KStG1992](https://github.com/KStG1992)

## **General Info:**
This project scrapes the current pollutants from the airnow website for California and displays the historical data of the state from 1/1/2010 to 10/31/2020.

## **Technologies:**
Project is created with:  
* HTML5
* Flask 1.1.2
* JavaScript 1.5
* Bootstrap 5.0.0
* Heroku 
* Flask-SQLAlchemy 2.4.4
* Pandas 1.1.5
* Python 3.6
* Jupyter Notebook 6.0.3
* SQLAlchemy 1.3.23
* pgAdmin 4

## **Setup:**
To launch the project, please use the following link:  
https://aperez-air-quality-analysis.herokuapp.com


## **Data sets:**
>- Air Quality current: https://docs.airnowapi.org/HistoricalObservationsByLatLon/docs
>>- scrape current data for visualization of current air quality
>- Air Quality historical data: https://aqs.epa.gov/aqsweb/airdata/download_files.html
>>- csv to database (cleanse using pandas); Use Python flask route to pass data from PostgressSQL database
>- US Census:  
    >>- by county: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html   
    >>- by city: https://www.census.gov/data/datasets/time-series/demo/popest/2010s-total-cities-and-towns.html  
>>- Use Python flask route to pass data from PostgressSQL database

## **Visuals:**
>- Topical graph with heatmap of Air Quality
>- Add layer to map to include demographic data
>- make interactive graph by picking date / county
>- Interactive map of air quality over time D3 folium JS library ? https://python-visualization.github.io/folium/

## **Overview:**
Database Map
![image](static/Images/Database_Model.png)  

Project ERD
![image](static/Images/Project_ERD.png)  

