
album={}
i=0

def make_album(artist_name, song_name):
    """Return a full name, neatly formatted."""
    full_name = f"{artist_name} {song_name}"
    album[artist_name]=song_name
    return full_name.title()
    
   # This is an infinite loop!
while True:
    i=0
    print("\nPlease tell me of an artist and song to add to the album:")
    print("\nPress 'q' to quit at any time.")
    artist_name = input("Artist name: ")
    if artist_name=='q':
        break
    song_name = input("Song name: ")
    if song_name=='q':
        break
    formatted_name = make_album(artist_name, song_name)
    print(f"\n{formatted_name}!")
    for k,v in album.items():
        i+=1
        print(f"\n\t{i}. {k.title()} | {v.title()}")

