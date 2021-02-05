#!/usr/bin/env python
# coding: utf-8

# Web Scraping - Mission to Mars

# Dependencies

import pandas as pd
import time
import requests
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from splinter import Browser


def scrape():
    # Mars News
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Retrieve page with the requests module
    response = requests.get(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(response.text, "lxml")    # LXML Parser

# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and
#      collect the latest News Title and Paragraph Text.
# Assign the text to variables for reference later.
    news_title = soup.find("div", class_="content_title").text
    news_synopsis = soup.find("div", class_="rollover_description_inner").text

# Characteristics of Mars

    # Visit the Mars Facts webpage(https://space-facts.com/mars/) to scrape the table containing facts about the planet.
    facts_url = "https://space-facts.com/mars/"

    # Retrieve page with the requests module
    response1 = requests.get(facts_url)

    # Create BeautifulSoup object and parse
    soup = bs(response1.text, "lxml")    # LXML Parser

    # Read the website HTML and convert to a pandas datframe
    mars_df = pd.read_html(facts_url)
    mars_df = mars_df[0]
    mars_df.columns = ['Characteristic', 'Fact']
    # Remove numerical index value
    mars_df.set_index('Characteristic', inplace=True)

    # Save HTML file
    mars_html = mars_df.to_html(header=False, index=False)

# Mars Hemispheres Images

# Visit the USGS Astrogeology site:
    #  (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
    hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URLs
    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    home_url = 'https://astrogeology.usgs.gov'

    # Create BeautifulSoup object and parse
    browser.visit(hemis_url)
    html = browser.html
    soup = bs(html, "lxml")    # LXML Parser
    # soup = bs(html, 'html.parser')  #HTML parser

    # Finding the hemispheres data through their HTML divisions
    mars_hemispheres = soup.find('div', class_='collapsible results')
    hemispheres = mars_hemispheres.find_all('div', class_='item')

    # Empty list for hemispheres' Title and image_urls
    mars_images = []

    # Iterate through each hemisphere data
    for hemi in hemispheres:

        # Get Titles
        hemisphere = hemi.find('div', class_="description")
        title = hemisphere.h3.text
        title = title.strip('Enhanced')

        # Get Images
        end_link = hemisphere.a["href"]
        browser.visit(home_url + end_link)

        image_html = browser.html
        image_soup = bs(image_html, 'html.parser')

        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']

        # Storage Dictionary
        image_dict = {}
        image_dict['Title'] = title
        image_dict['Image URL'] = image_url

        # Add data to empty list "mars_images"
        mars_images.append(image_dict)

    # Close browser window
    browser.quit()

# Create a summary dictionary of all scraped data
    summary_data = {
        'News from the Red Planet': news_title,
        'News Summary': news_synopsis,
        'Characteristics': mars_html,
        'Images': mars_images
    }
    return (summary_data)

# Step 2 - MongoDB and Flask Application

# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

# * Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a
#   function called `scrape` that will execute all of your scraping code from above and return
#   one Python dictionary containing all of the scraped data.

# * Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call
#   your `scrape` function.

# * Store the return value in Mongo as a Python dictionary.

# * Create a root route `/` that will query your Mongo database and pass the mars data into an
#  HTML template to display the data.

# * Create a template HTML file called `index.html` that will take the mars data dictionary and
#   display all of the data in the appropriate HTML elements. Use the following as a guide for
#   what the final product should look like, but feel free to create your own design.

# Hints

# Use Pymongo for CRUD applications for your database. For this homework, you can simply
#   overwrite the existing document each time the `/scrape` url is visited and new data is obtained.


