import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import pandas as pd
from collections import Counter
import seaborn as sns


def get_sp(cid,cs,username,redirect_uri,time):
    #from spotify for developers app:
    oauth_scopes = 'user-read-recently-played playlist-read-private user-top-read'
    t_range = time
    cid = cid
    cs = cs
    username = username
    redirect_uri = redirect_uri

    #getting oauth throgh spotipy:
    auth_manager = SpotifyOAuth(username=username,client_id=cid,
                                    client_secret=cs,
                                    redirect_uri=redirect_uri,
                                    scope=oauth_scopes)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp,t_range
def get_top_tracks (sp,t_range):

    user_top_tracks = sp.current_user_top_tracks(limit=20,time_range=t_range,offset=1)
    top_tracks={"track":[],"album":[],"artist":[]}
    for i in user_top_tracks["items"]:
        top_tracks["track"].append(i['name'])
        top_tracks["album"].append(i['album']['name'])
        top_tracks["artist"].append(i['artists'][0]['name'])

    df_top_tracks=pd.DataFrame(top_tracks)
    return df_top_tracks

def get_top_artist(sp,t_range):
    user_top_artists=sp.current_user_top_artists(limit=20,time_range=t_range,offset=1)
    top_id=[]
    top_artists={'Name':[],'Genre':[],'Popularity':[]}
    for i in user_top_artists['items']:
        top_artists['Name'].append(i['name'])
        top_artists['Genre'].append(i['genres'])
        top_artists['Popularity'].append(i['popularity'])
        top_id.append(i['id'])
    df_top_artist=pd.DataFrame(top_artists)
    top_id=top_id[0:4]

    return df_top_artist,top_id


def top_genres_grapsh (df):
    genres=[]
    music_genres = ["Blues", "Classical", "Country", "Electronic", "Folk", "Hip Hop", "Indie", "Jazz", "Metal", "Pop",
                    "R&B", "Rock", "Reggae", "Soul", "Funk", "Gospel", "Punk", "World", "Alternative", "EDM", "Rap",
                    "Techno", "Dubstep",  "Trance", "Latin", "Disco",
                    "Instrumental", "Acoustic", "Korean-Pop", "Salsa"]
    for genre in df['Genre']:
       for i in music_genres:
           if (i.lower() in genre[0].lower()):
               genres.append(i)
    genre_counts = Counter(genres)
    genre_label=list(genre_counts.keys())
    counts=list(genre_counts.values())

    plt.clf()
    plt.figure(facecolor='#F9F8F1')
    plot=plt.pie(counts,labels=genre_label,autopct=lambda p: '{:.1f}%'.format(round(p,2)) if p > 0 else "",
                 colors=sns.color_palette('Paired'))
    plt.ylabel("")
    plt.savefig('pie_chart.png')
    return plot

def top_albums(df_tracks):
    album_count=Counter(df_tracks['album'])
    i,j=1,0
    sorted_dict=sorted([(value,key) for (key,value) in album_count.items()],reverse=True)
    length=len(sorted_dict)
    top=sorted_dict[j][1]
    while (sorted_dict[i][0]==sorted_dict[j][0] and i<length-1):
        index_1=df_tracks.index[df_tracks['album'] == sorted_dict[i][1]].tolist()
        index_2=df_tracks.index[df_tracks['album'] == sorted_dict[j][1]].tolist()
        if (index_2<index_1):
            top=sorted_dict[j][1]
        i+=1
        j+=1
    return top

def get_cover(album,sp,t_range):
    user_top_tracks = sp.current_user_top_tracks(limit=20,time_range=t_range,offset=1)
    for item in user_top_tracks['items']:
        if item['album']['name'] == album:
            img = item['album']['images'][0]
            break
    return img['url']



def get_feature(tracks_id,sp,tracks,artist_name):
        features_info = sp.audio_features(tracks=tracks_id)
        df_features = pd.DataFrame(features_info)
        df_features = df_features.drop(['key','mode','type','id','uri','track_href','analysis_url','duration_ms','time_signature'],axis=1)
        avg=df_features.mean(axis=1)
        df=pd.DataFrame()
        df['tracks']=tracks
        df['artists']=artist_name
        df['tracks_id']=tracks_id
        df['average']=avg

        return df


def similar_artist(artist_id,sp):
    data=pd.DataFrame( {'tracks': [], 'artists': [], 'tracks_id': [], "average_score": []})
    for id in artist_id:
        similar=sp.artist_related_artists(id)
        ids=[]
        tracks =[]
        tracks_id=[]
        artist_name=[]
        for item in similar['artists']:
            ids.append(item['id'])
        ids=ids[0:4]
        for id in ids :
            top_tracks=sp.artist_top_tracks(id)
            for i in top_tracks['tracks']:
                tracks.append(i['name'])
                tracks_id.append(i['id'])
                artist_name.append(i['artists'][0]['name'])
        df_similar=get_feature(tracks_id,sp,tracks,artist_name)
        data=pd.concat([data, df_similar], axis=0)
    return data

def compare_similar(sp,t_range):
    top_tracks = sp.current_user_top_tracks(limit=5, time_range=t_range, offset=1)
    tracks = []
    tracks_id = []
    artist_name = []
    for item in top_tracks['items']:
        tracks_id.append(item['id'])
        tracks.append('name')
        artist_name.append('artist')
    df_top_tracks=get_feature(tracks_id,sp,tracks,artist_name)
    avg=df_top_tracks['average'].mean()
    df,top=get_top_artist(sp,t_range)
    similar_df=similar_artist(top,sp)
    similar_df=similar_df.rename(columns={"tracks":"track","artists":"artist"})
    similar_df['top_average']=avg
    similar_df['distance']=(similar_df['average']-similar_df['top_average']).abs()
    similar_df=similar_df.sort_values('distance')
    similar_df=similar_df.drop_duplicates()
    top5=similar_df.head(5)
    return top5

