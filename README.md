# ud036_StarterCode
Source code for a Movie Trailer website.
1/20/2018 Sherin Kuruvilla
Project #1
Movie Database

Steps for Running Movie Database
===========================================
Download the code from this git to your local repository
Lets say the folder is C:\Movies.  Make sure you have Python 2.7 installed on your machine.
Browse to your repository, C:\Movies and locate the file named entertaintment_center.py.
I have added 4 movies to the entertaintment_center.py.
We can add more movies to this file, if we like.  Make sure any additional movie names are added to the movies
array.  Now, to view the movies database, doubleclick the file.
You will see a web page open up with the movies displayed. Click on each movie to see the trailer video.


All the movies that are instantiated and displayed in the browser are defined using a Movie class defined in the media module media.py.
This class stores the movie name, a short description, a poster image URL and the youtube video URL.
The movies objects are instantiated in the entertainment_center, stored in an object array named movies and passed to the python program that generates an HTML output.  This function is called as fresh_tomatoes.open_movies_page(movies).
This call generates an html file names fresh_tomatoes.html, which is then called using the webbrowser.open() method.


Thanks,
Sherin Kuruvilla