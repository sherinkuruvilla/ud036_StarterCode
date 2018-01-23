import webbrowser


class Movie:
    """Author: Sherin Kuruvilla
       This class Movie is stored in a module or file named media
       The Movie class defines an object that can store details about movies"""

    def __init__(self, movie_title, movie_story_line, movie_poster_image, movie_youtube_trailer):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)

    def show_poster(self):
        webbrowser.open(self.poster_image)
