
<p align="center">
<img alt="spotify logo" src="assets/rythminsights.png" width="350">
</p>
</p>

 This project utilizes the Spotify API to extract data such as track information, user playlists, and user listening habits. It then processes this data to generate an [HTML file](http://htmlpreview.github.io/?https://github.com/romisadeh/rhythminsights/blob/main/assets/spotifyApi.html) for visualizing trends, favorite tracks, and personalized recommendations. Perfect for exploring your Spotify data in a user-friendly format! <br />

 **Features:**

- Classifies user's reviews with an RNN model.
- Trained on 40,000 movie reviews that were scraped from [imdb.com](https://www.imdb.com).
- Exports an HTML file with statistics about recently published movies.
- Generates a review for the top movie of the week.
- Updates weekly according to [Imdb: movies in theaters](https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth).
- Can be applied on custom movie lists 


## Requierments:
- tensorflow 2.0+
- nltk

## Quick start:
Run this command to get the summary in an HTML file:

```shell
python src/moviescoreai.py --name <name for the HTML file>  --output <output path> --start <Optional, if you want to file to open by defult>
--movies-url <url for your movies list >
```

