<p align="center"><img width="100%" height="144" src="images/readme.PNG"></p>
<br>            
Project begins with initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter from public websites:<br>
  - https://space-facts.com/mars/
  - https://mars.nasa.gov/news/
  - https://astrogeology.usgs.gov/
<br>
1. The Jupyter Notebook contains the scraping code and the dictionary of information is saved as a Mongo database. <br>
2. The Jupyter Notebook is then converted to a python file for use in a Flask app.<br>
3. The Flask app has two routes- one for scraping new data from NASA and the other to redirect to the HTML home page code.<br>
<br>
The code is run as a Python file. 
<p align="center"><img width="586" height="1109" src="images/page_screenshot.PNG"></p>
<br>
<p align="center"><img width="100%" height="128" src="images/footer.png"></p>
