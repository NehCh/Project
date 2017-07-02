import media
import fresh_tomatoes

# Storyline is broken down into multiple lines in order to comply with the
# Python style guidelines for maximum number of characters in a line.
# Poster Image URLs have not been tampered with to avoid confusion and kept
# at their orignal length. NOQA has been added as an inline comment.
Toy_Story = media.Movie("Toy Story (1995)",
                        "A story of a boy and his toys that come to life",
                        "https://vignette4.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
Despicable_Me = media.Movie("Despicable Me (2010)",
                        "The mischievous Minions hope that Gru will return to"
                        "a life of crime after the new boss of the Anti"
                        "-Villain League fires him.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3NjY0MTQ0Nl5BMl5BanBnXkFtZTcwMzQ2MTc0Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=sUkZFetWYY0")
Ratatouille = media.Movie("Ratatouille (2007)",
                        "Ratatouille is a 2007 American computer-animated "
                        "comedy film produced by Pixar and released by Buena"
                        "Vista Pictures Distribution.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=1tEC7OTQwGk")
Avatar = media.Movie("Avatar (2009)",
                        "A hybrid human-alien called an Avatar is created"
                        "to facilitate communication "
                        "with the indigenous Navis from the planet Pandora",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
Zootopia = media.Movie("Zootopia (2016)",
                        "In a city of anthropomorphic animals, a rookie "
                        "bunny cop and a cynical con artist fox must "
                        "work together to uncover a conspiracy.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BOTMyMjEyNzIzMV5BMl5BanBnXkFtZTgwNzIyNjU0NzE@._V1_QL50_SY1000_SX675_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=jWM0ct-OLsM")
Polar_Express = media.Movie("The Polar Express (2004)",
                        "A young boy embarks on a magical adventure to the "
                        "North Pole on the Polar Express.During his adventure"
                        " he learns about the spirit of Christmas.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM1NTU0NTE4MV5BMl5BanBnXkFtZTcwMTQ0MjEzMw@@._V1_QL50_SY1000_CR0,0,676,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=TQhRqtt-Fpo")

# Create an array of Objects instantiated
movies = [Toy_Story, Despicable_Me, Ratatouille,
          Avatar, Zootopia, Polar_Express]
fresh_tomatoes.open_movies_page(movies)
