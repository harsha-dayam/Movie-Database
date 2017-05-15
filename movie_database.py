import fresh_tomatoes
import media #module containing the class Movies

#movie database
toy_story = media.Movies("Toy Story", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
kungfu_panda = media.Movies("Kung Fu Panda", "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg", "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
monsters_university = media.Movies("Monsters University", "https://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg", "https://www.youtube.com/watch?v=QxrQ6BaijAY")
the_prestige = media.Movies("The Prestige", "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg", "https://www.youtube.com/watch?v=o4gHCmTQDVI")
fight_club = media.Movies("Fight Club", "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg", "https://www.youtube.com/watch?v=BdJKm16Co6M")
the_others = media.Movies("The Others", "https://upload.wikimedia.org/wikipedia/en/4/4c/TheOthers.jpg", "https://www.youtube.com/watch?v=ISch6Fi-q0A")
pirates = media.Movies("Pirates of the Caribbean: The Curse of the Black Pearl", "https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png", "https://www.youtube.com/watch?v=naQr0uTrH_s")
planet_apes = media.Movies("War for the Planet of the Apes", "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg", "https://www.youtube.com/watch?v=UEP1Mk6Un98")
spiderman = media.Movies("Spider-Man 3", "https://upload.wikimedia.org/wikipedia/en/7/7a/Spider-Man_3%2C_International_Poster.jpg", "https://www.youtube.com/watch?v=1bzqHbTD64w")

#storing all the movies in a list to be called by fres_tomatoes function: open_movies_page
movies = [toy_story, monsters_university, kungfu_panda, the_prestige, fight_club, the_others, planet_apes, pirates, spiderman]
#calling the fresh_tomatoes module function to create the html document for the movie database website
fresh_tomatoes.open_movies_page(movies)
