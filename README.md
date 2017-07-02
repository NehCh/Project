# Introduction
This a a website that allows the user to view movie trailers of some of the All Time Hits in Animated Movies.

# Prerequisites
In order to be able to view the website and run the code one needs to have Python installed on their machines. Use https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi for downloading Python on your machine.

# Steps to view the code
1. Clone a copy of the "media.py", "entertainment_centre.py" and "fresh_tomatoes.py" files on your system
2. To view the code one may use the Python IDLE or any other Editor

# Overview of the code:
1. The file "media.py" has defined a data structure, where Movie is a class and the contructor is initializing the instance variables for each object. These instance variables are common across different movies. So here we are creating the prototype of what data would be displayed for every movie on the webpage.
2. The file "entertainment_centre.py" has multiple instances of Class Movie that represent the different movies;  groups all the instances together in a list, and then passes this list to a function open_movies_page() which is defined in "fresh_tomatoes.py"
Each instance passes the Title, Storyline, Poster and Youtube URL of the movie to the constructor that gets called when the object gets instantiated.
This is where we are creating the actual objects, i.e. movies that we want to display along with the data.
3. The file "fresh_tomatoes.py" defines the function open_movies_page() and the various styling(CSS) and layout(HTML) aspects of the webpage.
When the function open_movies_page is called with the list of objects, that creates an HTML file which will display all of the favorite movies

# Steps to execute the code
1. Make sure that the three files are present under the same Folder in the Python directory in your system.
2. Launch the entertainment_centre.py file
3. Run using F5 key
4. This should launch the Python Shell
5. Also, it would lauch the Movie Trailer Website.

Alternatively, one can also launch the website directly from the fresh_tomatoes.html file that would be created in the Folder where fresh_movies.py is present, on successfully running the code once using the above steps.

# Expected result:
The website should list out a total of 6 movies, and on clicking on each, user should be able to view the trailer of that movie. 

