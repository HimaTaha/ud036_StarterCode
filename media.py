class Movie:
    """ this is the data structure for a movie
    Attributes:
        title(str): the name of the movie
        poster_image_url(str): url to  the movie poster image to be displayed
        trailer_youtube_url(str): the url to the movie trailer on youtube
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
            self.title = title
            self.poster_image_url = poster_image_url
            self.trailer_youtube_url = trailer_youtube_url
