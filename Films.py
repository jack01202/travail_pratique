class Film :
    def __init__(self,name):
        self.name = name

    def watch (self):
        print("Bon visionnage !")
class FilmCassette(Film):
    def __init__(self, name):
        """Initailise le nom et la bande magnétique"""
        self.name = name
        self.magnerique_tape = True

    def rewind(self):
        """Rembobine le film"""
        print("c'est long a rembobiner !")
        self.magnerique_tape = True


film = Film ("2001: l'odyssee de l'espace")
film_cassette = FilmCassette ("Blader runner")

print(film_cassette.name)
print(film_cassette.magnerique_tape)
film_cassette.watch()
film_cassette.rewind()