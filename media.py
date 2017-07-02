class Movie():
# Defining the constructor, which
# instantiates the objects of this class. It takes in
# parameters passed while creating the objects.
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
