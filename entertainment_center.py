import fresh_tomatoes
import media



Toy_story = media.Movie("Toy story",
                        "A story of a boy and his toys who come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

#print(Toy_story.storyline)

Avatar = media.Movie("Avatar",
	                 "A marine on an alien planet",
	                 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	                 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print(Avatar.storyline)
#Avatar.show_trailer()

notebook = media.Movie("The Notebook",
	                   "A story of true love that never dies",
	                   "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
	                   "https://www.youtube.com/watch?v=S3G3fILPQAU")



Prestige = media.Movie("The Prestige",
	                   "Two stage magicians engage in competitive one-upmanship in an attempt to create the ultimate stage illusion.",
	                   "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
	                   "https://www.youtube.com/watch?v=6VaCFcNGTHo")



Inception = media.Movie("Inception",
	                   "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO. ",
	                   "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
	                   "https://www.youtube.com/watch?v=8hP9D6kZseM")




Deja = media.Movie("Deja Vu",
	                "After a ferry is bombed in New Orleans, an A.T.F. agent joins a unique investigation using experimental surveillance technology to find the bomber, but soon finds himself becoming obsessed with one of the victims. ",
	                "https://upload.wikimedia.org/wikipedia/en/c/cf/DejaVuBigPoster.jpg",
	                "https://www.youtube.com/watch?v=oz1hv1u0DXc")



Shawshank = media.Movie("The Shawshank Redemption",
	                   "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency. ",
	                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
	                   "https://www.youtube.com/watch?v=6hB3S9bIaco")



Vendetta = media.Movie("V for Vendetta",
	                   "In a future British tyranny, a shadowy freedom fighter, known only by the alias of V, plots to overthrow it with the help of a young woman. ",
	                   "https://upload.wikimedia.org/wikipedia/en/9/9f/Vforvendettamov.jpg",
	                   "https://www.youtube.com/watch?v=k_13fFIrhPk")

	                   
Matrix = media.Movie("The Matrix",
	                 "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.  ",
	                 "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
	                 "https://www.youtube.com/watch?v=vKQi3bBA1y8")

Conjuring = media.Movie("The Conjuring",
	                 "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
	                 "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
	                 "https://www.youtube.com/watch?v=Vjk2So3KvSQ")




#notebook.show_trailer()
movies = [Toy_story, Avatar, notebook, Prestige, Inception, Deja, Shawshank, Vendetta, Matrix, Conjuring]
fresh_tomatoes.open_movies_page(movies)
