Movie Database
-----------------------------------------------------------------------------------------------------
Movie database is a web application that displays a list of movie tiles.  
User can click on each movie tile to see a short trailer video.

Usage
------------------------------------------------------------------------------------------------------
1. Download the python source code for the movie database application.

    a. Browse to the following github location, https://github.com/sherinkuruvilla/ud036_StarterCode
    b. Select the "clone or download" open and choose "Download Zip".
    c. Extract the file to your local directory, for example, C:\Movies.
    d. Verify that you can see 3 source files - media.py, entertaintment_center.py, and fresh_tomatoes.py.


2. Install Python 2.7 on your machine.
    a. Download python installation files from https://www.python.org/downloads/
    b. Select python 2.7.* version and download. (Do not install the python 3.* version)
    c. Install python using defaults.

3. Open the movies database
    a. Browse to your local directory, C:\Movies and locate the file named entertaintment_center.py.
    b. To run the program, simply double click the file.
    c. You may also the open the file entertaintment_center.py using IDLE GUI and run it using F5.
    d. You will see a web page open up with the movies displayed. 
    e. Click on each movie to see the trailer video.

4. Editing movies in Movie Database. (optional)
    a. Browse to your local directory, C:\Movies and locate the file named entertaintment_center.py.
    b. Open the entertaintment_center.py program file using Python IDLE GUI. 
    c. You will see that there are already 4 movies to the entertaintment_center.py.
    d. You can add more movies to this file and update Movies array (see file for more details)

Enjoy the movies and trailers!


Solution Summary
-----------------------------------------------------------------------------------------------------------------------
All the movies that are instantiated and displayed in the browser are defined using a Movie class defined in the media module media.py.
This class stores the movie name, a short description, a poster image URL and the youtube video URL.
The movies objects are instantiated in the entertainment_center, stored in an object array named movies and passed to the python program that generates an HTML output.  This function is called as fresh_tomatoes.open_movies_page(movies).
This call generates an html file names fresh_tomatoes.html, which is then called using the webbrowser.open() method.

About
-------------------------------------------------------------------------------------------------------------------------
# ud036_StarterCode
Source code for a Movie Trailer website.
1/20/2018 Sherin Kuruvilla
Project #1
Movie Database

