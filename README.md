Steps for Running Movie Database
===========================================
1. Download the code from my git, https://github.com/sherinkuruvilla/ud036_StarterCode, to your local repository. 
Lets say the folder is C:\Movies.  
2. Make sure you have Python 2.7 installed on your machine.
3. Browse to your repository, C:\Movies and locate the file named entertaintment_center.py.
4. Open the entertaintment_center.py program file using Python IDLE GUI. Verify that I have added 4 movies to the entertaintment_center.py.
5. You can add more movies to this file, if you like.  Make sure any additional movie names are added to the movies
array.  
6. Now, to view the movies database, save the file, and run using F5.
7. You will see a web page open up with the movies displayed. Click on each movie to see the trailer video.
8. Enjoy my movies and trailers!

Thanks,
Sherin Kuruvilla


Solution Summary
-------------------------------
All the movies that are instantiated and displayed in the browser are defined using a Movie class defined in the media module media.py.
This class stores the movie name, a short description, a poster image URL and the youtube video URL.
The movies objects are instantiated in the entertainment_center, stored in an object array named movies and passed to the python program that generates an HTML output.  This function is called as fresh_tomatoes.open_movies_page(movies).
This call generates an html file names fresh_tomatoes.html, which is then called using the webbrowser.open() method.

# ud036_StarterCode
Source code for a Movie Trailer website.
1/20/2018 Sherin Kuruvilla
Project #1
Movie Database

