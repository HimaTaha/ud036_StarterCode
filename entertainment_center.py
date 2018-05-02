import media
import fresh_tomatoes

movie_list = []
avatar_movie = media.Movie("Avatar 2009",
                           "http://dvdmedia.ign.com/dvd/image/object/060/060436/avatar-dvd.jpg",
                           "https://www.youtube.com/watch?v=5PSNL1qE6VY" )
movie_list.append(avatar_movie)
titanic_movie = media.Movie("Titanic 1997",
                            "data:image/jpeg;base64,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",
                            "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
movie_list.append(titanic_movie)




fresh_tomatoes.open_movies_page(movie_list)