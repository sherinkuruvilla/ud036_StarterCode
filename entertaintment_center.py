import fresh_tomatoes
import media
import time

toy_story=media.Movie("Toy Story",
                      "This is a story of a kid and his toys coming to life",
                      "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
                                         "https://www.youtube.com/watch?v=KYz2wyBy3kc&start=16&end=55")
##                      "https://www.youtube-nocookie.com/embed/KYz2wyBy3kc?showinfo=0&start=16&end=55&autoplay=1&rel=0")
##print(toy_story.story_line)
##toy_story.show_poster()
##time.sleep(3)
##toy_story.show_trailer()

avatar=media.Movie("Avatar",
                      "Avatar is a distant planet with a native alien species colonized by humans",
                      "http://theideasbodega.com.au/wp-content/uploads/2015/01/neytiri_in_avatar_2-wide-do-we-really-need-avatar-2-1024x640.jpeg",
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8&start=84&end=127")
##                      "https://www.youtube-nocookie.com/embed/d1_JBMrrYw8?showinfo=0&start=84&end=127&autoplay=1&rel=0")
##avatar.show_trailer()

pulimurugan=media.Movie("Pulimurugan",
                      "Malayalam thriller starring Mohan Lal as the catcher of Tiger, PuliMurugan",
                      "http://pressks.com/wp-content/uploads/2016/10/puli-murugan-first-day-collection.jpg",
                                           "https://www.youtube.com/watch?v=blQUlD8g4Pk&start=54&end=94")
##                      "https://www.youtube-nocookie.com/embed/blQUlD8g4Pk?showinfo=0&start=54&end=94&autoplay=1&rel=0")
##pulimurugan.show_trailer()

dhangal=media.Movie("Dhangal",
                      "Award winning Amir Khan hindi action cinema about Indian Wrestler Sisters rise to fame",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcQIXnFlBKGWT1ByyIu3qfxX6opQX6BmeeU_qsiE3X8rX9ZRr63r",
                                       "https://www.youtube.com/watch?v=x_7YlGv9u1g&start=0&end=141")
##                      "https://www.youtube-nocookie.com/embed/x_7YlGv9u1g?showinfo=0&start=141&end=183&autoplay=1&rel=0")
##dhangal.show_trailer()
movies=[dhangal, avatar, pulimurugan, toy_story]
fresh_tomatoes.open_movies_page(movies)

