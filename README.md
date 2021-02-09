<p align="center"><img width="100%" height="144" src="images/readme.PNG"></p>
<br>            
Project begins with initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter from public websites:<br>
<ul>
    <li> https://space-facts.com/mars<li>
    <li> https://mars.nasa.gov/news<li>
    <li> https://astrogeology.usgs.gov<li>
</ul>
<br>
1. The Jupyter Notebook contains the scraping code and the dictionary of information is saved as a Mongo database. <br>
2. The Jupyter Notebook is then converted to a python file for use in a Flask app.<br>
3. The Flask app has two routes- one for scraping new data from NASA and the other to redirect to the HTML home page code.<br>
<br>
The code is run as a Python file with this result: 
<p align="center"><img style="border:5px double black;" src="images/page_screenshot.PNG" width="586" height="1109"></p>
<br>
<p align="center"><img width="100%" height="128" src="images/footer.png"></p>

