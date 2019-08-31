import wget
import termcolor as t

url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
filename = wget.download(url)
print(t.colored("Hello SWDV660, music file was downloaded and saved in the project folder",'cyan','on_blue'))

