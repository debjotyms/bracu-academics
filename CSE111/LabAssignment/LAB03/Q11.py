from sympy import numer


class Spotify:
    def __init__(self,song):
        print("Welcome to Spotify!")
        self.song = song
    
    def playing_number(self,number):
        if len(self.song)<number:
            return f"""{number} number song not found. Your playlist has {len(self.song)} songs only."""
        else:
            print("##########################")
            return f"""Playing {number} number song for you
Song name: {self.song[number-1]}"""
    def add_to_playlist(self,songName):
        self.song.append(songName)


user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))