import media
import fresh_tomatoes

# list containing movies that is fed to open_movies_page()
movie_list = []
# text file having movies data
movie_DB = "DB/moviesList"
file = open(movie_DB, "r")
# each line is in the following format:
#           movie_title, poster_image_url, youtube_trailer_url
for line in file:
    title, poster, trailer = line.split(", ")
    movie = media.Movie(title, poster, trailer)
    movie_list.append(movie)
file.close()
fresh_tomatoes.open_movies_page(movie_list)
