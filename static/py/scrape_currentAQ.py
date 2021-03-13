# Importing Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import time as tm
import pandas as pd

# Function for Excel File
def city_data():
    # Creating File Path for Excel File
    filePath = "../Data/CA_Pop_Census_2010_2019_by_city.xlsx"
    excel_df = pd.DataFrame(pd.read_excel(filePath))
    
    # Converting Excel to CSV for Ease
    excel_df.to_csv ("CA_Pop_Census_2010_2019_by_city.csv",  
                    index=None,
                    header=None)
    
    # Creating DataFrame
    df = pd.DataFrame(pd.read_csv("CA_Pop_Census_2010_2019_by_city.csv"))
    
    # Cleaning CSV
    # Dropping UnWanted Columns and Indices
    df = df.drop(columns=["Unnamed: 1", "Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7",
                         "Unnamed: 8", "Unnamed: 9", "Unnamed: 10", "Unnamed: 11", "Unnamed: 12"],
                index=[0,1,484,485,486,487,488])
    # Renaming Column 0
    df = df.rename(columns={"Annual Estimates of the Resident Population for Incorporated Places in California: April 1, 2010 to July 1, 2019": "City"})
    # Parsing City Column
    df["City"] = df["City"].str.split(",", n=1, expand=True)
    # Dropping City and Town
    df["City"] = df["City"].str.split("city", n=1, expand=True)
    df["City"] = df["City"].str.split("town", n=1, expand=True)
    
    # Converting df to List
    return df['City'].tolist()

# Function for Browser
def init_browser():
    # Setting Up Splinter
    executable_path = {'executable_path': "C:/Windows/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)

# Function for Scrape
def scrape_info():
    
    # Calling init_browser Function
    browser = init_browser()
    
    # Calling city_list Function
    city_list = city_data()
    
    # Creating List of Current AQI Data
    currentAQI = []
    
    baseUrl = 'https://www.airnow.gov/?'
    state = 'CA'
    country = 'USA'
    
    for city in city_list:
        # Building URL Query
        url_air_now = baseUrl + 'city=' + city + '&state=' + state + '&country=' + country

        # Visiting URL 
        browser.visit(url_air_now)
        # Visiting the URL Takes Some Time, Using the Time Module to Slow Down the Run
        tm.sleep(1)

        # Scrape page into Soup
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        
        
        try:
            # Scraping Date & Time
            aqUpdateTime = soup.find('span', class_='aq-updated-time')
            currentDateTime = aqUpdateTime.text
            currentTime = currentDateTime.rsplit('PST')[0] + 'PST'
            currentDate = currentDateTime.rsplit('PST')[1]

            # Scraping Current Pollutant
            aqiItem = soup.find('div', class_='aqi')
            aqi = aqiItem.find('b').text
            pollutantItem = soup.find('div', class_='pollutant')
            pollutant = pollutantItem.find('b').text

            # Appending Dictionary to List
            currentAQI.append({"City": city, "Time": currentTime, "Date": currentDate,
                              "Current AQI Value": aqi, "Current Pollutant": pollutant})
        except IndexError:
            next
            
    # Closing Browser
    browser.quit()
  
    return currentAQI
        
scrape_info()
