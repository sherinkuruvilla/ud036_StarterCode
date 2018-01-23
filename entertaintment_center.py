import fresh_tomatoes
import media
import time

# This python module is used to define
# the movies we want to show in the web site.
# I have instantiated 4 movie classes and
# gave them each a name, description, image URL and youtube trailer's URL
toy_story = media.Movie("Toy Story",
                        "This is a story of a kid and his toys coming to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&start=16&end=55")

avatar = media.Movie("Avatar",
                     "Avatar is a distant planet with a native alien species colonized by humans",
                     "http://theideasbodega.com.au/wp-content/uploads/2015/01/neytiri_in_avatar_2-wide-do-we-really-need-avatar-2-1024x640.jpeg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8&start=84&end=127")

pulimurugan = media.Movie("Pulimurugan",
                          "Malayalam thriller starring Mohan Lal as the catcher of Tiger, PuliMurugan",
                          "http://pressks.com/wp-content/uploads/2016/10/puli-murugan-first-day-collection.jpg",
                          "https://www.youtube.com/watch?v=blQUlD8g4Pk&start=54&end=94")

dhangal = media.Movie("Dhangal",
                      "Award winning Amir Khan hindi cinema about Sisters rise to fame",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcQIXnFlBKGWT1ByyIu3qfxX6opQX6BmeeU_qsiE3X8rX9ZRr63r",
                      "https://www.youtube.com/watch?v=x_7YlGv9u1g&start=0&end=141")

# The movies array is an array of movie objects
# which are defined above.
movies = [dhangal, avatar, pulimurugan, toy_story]

# pass the movies array to the fresh_tomatoes.py module's
# open_movies_page function, which will do a variable
# substitution to generate the web page templates
# for these 4 movies.
fresh_tomatoes.open_movies_page(movies)
