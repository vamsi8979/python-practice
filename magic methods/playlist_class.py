class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __len__(self):
        return len(self.songs)
    
    def __getitem__(self, index):
        return self.songs[index]

my_playlist = Playlist(["Song 1", "Song 2", "Song 3"])
print("Length: ",len(my_playlist))
print("First Song: ",my_playlist[0]) 
print("Third Song: ",my_playlist[2])