import webbrowser


class Movie():

	 def show_trailer(self):
	 	webbrowser.open(self.youtube_url)

	 def __init__(self, title,storyline,poster_image,url):
		self.title = title
		self.storyline = storyline
		self.poster_image = poster_image
		self.youtube_url = url
