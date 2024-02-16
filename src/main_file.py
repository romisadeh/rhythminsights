import create_html
import spotify_API

cid=input("Enter your spotify client_Id: ")
cs=input("Enter your Client_secret: ")
username=input("Enter username: ")
redirect_uri=input("Enter redirect uri")

sp,t_range=spotify_API.get_sp(cid,cs,username,redirect_uri)
df_top_tracks=spotify_API.get_top_tracks(sp,t_range)
df_top_artist,top=spotify_API.get_top_artist(sp,t_range)

def top_10_artist():
    string =""
    for i in range(0,10):
        string+=str(i+1)+". "+df_top_artist.iloc[i]['Name']+'<br>'
    return string

def top_tracks(x,df):
    string =""
    for i in range(0, x):
       string +=str(i+1)+". "+ str(df.iloc[i]['track']) + " - " + str(df.iloc[i]['artist'])+'<br>'
    return string

top_10_tracks = top_tracks(10,df_top_tracks)
top_10_artists=top_10_artist()
album=spotify_API.top_albums(df_top_tracks)
img_url=str(spotify_API.get_cover(album,sp,t_range))
similar=spotify_API.compare_similar(sp,t_range)
top_related=top_tracks(5,similar)
pi_chart=spotify_API.top_genres_grapsh(df_top_artist)
create_html.html(top_10_tracks,top_10_artists,top_related,album,img_url)

