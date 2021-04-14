#8-6
def city_names(name,country):
	print(f"{name.title()}, {country.title()}")
city_names('pitori','mzansi')

#8-7
def make_album(album_name, artist_name):
	"""Return a dictionary of information about an album."""
	album = {'Album':album_name, 'Artist':artist_name}
	return album
albuminfo=make_album('Manando', 'Emtee')
print(albuminfo)

#8-8
def make_album(album_name, artist_name):
	"""Return a dictionary of information about an album."""
	album = {'Album':album_name, 'Artist':artist_name}
	return album
poll = True
while poll:
	albumname = input("Please enter album name: ")
	artistname = input("Please enter artists name: ")
	albuminfo = make_album(albumname,artistname)
	print(albuminfo)
	quite = input("Is there more albums?")
	if quite == 'no':
		poll = False

