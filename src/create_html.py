import os





def html(top_10_tracks,top_10_artists,top_related,album,img_url):
    with open('C:/Users/romi3/OneDrive/Documents/spotifyApi.html', "w", encoding="utf-8") as file:
        file.write('''<!DOCTYPE html> 
                        <html>    
                          <head>
                            <title>Spotify API</title>
                            <link href="style.css" rel="stylesheet">
                            <script src="script.js" type="text/javascript"></script>
                              <style>
        h1 {
            font-size: 35px;
        }

        h2 {
            font-size: 20px;
            align-items: center;
        }

        h3 {
            font-size: 30px;
        }

        h4 {
            font-size: 20px;
        }

        h6 {
            font-size: 25px;
        }

        body {
            background-color: #F9F8F1;
            color: #2C232A;
            font-family: sans-serif;
            font-size: 2.0em;
            margin: 0 auto;
            width: 2000px;
        }

        .pie-chart {
            width: 950px; 
            height: 750px; 
            display: block;
            margin: auto;
        }

        .album-cover {
            width: 750px; 
            height: 650px; 
            display: block;
            margin: auto;
            position: relative;
        }

        .text {
            font-size: 16px;
            width: 600px;
        }

        .center {
            margin: auto;
            width: 100%;
            text-align: center;
        }

        .header {
            margin: auto;
            width: 100%;
            text-align: center;
            background-color: #2C232A;
            color: #F9F8F1;
        }

        .top-10 {
            display: flex;
            align-items: flex-start;
        }

        .tracks {
            width: 50%;
            text-align: left;
            padding: 20px;
        }

        .artists {
            width: 50%;
            text-align: left;
            padding: 20px;
        }

        .top-album {
            display: flex;
            align-items: flex-start;
           
        }

        .rec,
        .cover {
            display: inline-block;
            vertical-align: top; 
            text-align: left;
        }

        .rec {
            width: 50%;
            text-align: left;
            padding: 10px;
        }

        .cover {
            width: 50%;
            text-align: right;
            padding: 10px;
            
        }



        .album-text {
            text-align: center;
            top: 0;
            left: 0;
        }

        .text-artist {
            text-align: left;
            top: 0;
            left: 0;
            margin-left: 375px;
        }

        .text-tracks {
            text-align: left;
            top: 0;
            left: 0;
            margin-left: 250px;
        }

    </style>
                          </head>
                          <body>
                             <div class="body">
                                <div class="header">
                                    <h1><u>Spotify API</u></h1>
                                    <h4>Data extracted from Spotify</h4>
                                </div>
                                <div class="top-10">
                                    <div class="tracks">
                                        <h3 class="album-text"><u>Top 10 tracks</u></h3>
                                        <p class="text-tracks">''' + top_10_tracks + '''</p>
                                                        
                                    </div> 
                                    <div class="artists">
                                        <h3 class="album-text"><u>Top 10 artists:</u></h3>
                                        <p  class="text-artist">'''+top_10_artists+'''</p>
                                    </div>
                                </div>
                                <br>
                                <div class="center"> 
                                    <h5><u>Top genre:</u></h5>
                                </div> 

                                <div class="image">
                                    <img class="pie-chart" src="'''+ os.getcwd() +'''\pie_chart.png" >
                                  <br><br><br>
                                </div>
                              
                                 <div class="top-album">
                                    <div class="rec">
                                        <h3><u>5 Recommended songs based on your top artists:</u></h3>
                                        <p>'''+top_related+'''</p>
                                        </div>
                                    <div class="cover">
                                        <h3 class="album-text"><u>Top album</u></h3>
                                        <p class="album-text">'''+str(album)+'''</p>
                                        <img class="album-cover" src="'''+img_url+'''" >
                                    </div>
                                </div>
                            </div>
                          </body>
                        </html>''')
        file.close()
