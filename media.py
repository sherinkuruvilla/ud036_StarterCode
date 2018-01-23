import webbrowser


class Movie:
    """Author: Sherin Kuruvilla
       This class Movie is stored in a module or file named media
       The Movie class defines an object that can store
       structured data and methods pertaining to movies.
       This class support 4 movie attributes and 2 methods."""

    def __init__(self, movie_title, movie_story_line,
                 movie_poster_image, movie_youtube_trailer):
        # This is the class initializing function for Movie class
        # which requires as input
        # title, description, image and trailer video urls values
        # which are assigned to each instance.
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_trailer

    def show_trailer(self):
        # Uses the web browser object to open the video of the attached url
        webbrowser.open(self.youtube_trailer)

    def show_poster(self):
        # uses the web brower's open method
        # to display the poster image
        webbrowser.open(self.poster_image)
