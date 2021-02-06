# Mission to Mars
<!-- Add Jumbotron to Header -->
        <div class="jumbotron text-center"
            style="background-image: url('https://wallpapercave.com/wp/wp2461878.jpg'); background-position: center; background-size: cover;height: 250px;">
            <h1 style="color:white">Mission to Mars</h1></div>
Project begins with initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.<br>
<br>
1. The Jupyter Notebook contains the scraping code and the dictionary of information is saved as a Mongo database. <br>
2. The Jupyter Notebook is then converted to a python file for use in a Flask app.  
3. The Flask app has two routes- one for scraping new data from NASA and the other to redirect to the HTML home page code.

