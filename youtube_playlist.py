import datetime
import os
from typing import ItemsView
from googleapiclient.discovery import build

youtube_api_key = os.environ.get("youtube_api_key")
playlist_id     = "your_playlist_id"
# channel_id      = "your_channel_id"

youtube = build('youtube', 'v3', developerKey=youtube_api_key)

#------------------------------------------------------------------------#
# pl_request = youtube.playlists().list(
#     part= 'contentDetails, snippet',
#     channelId = channel_id,
#     maxResults= 10
#         )

# pl_response = pl_request.execute()

# for item in pl_response['items']:
#     print(item)

#     print( item['snippet']['title'] )
#------------------------------------------------------------------------#

video_title_list = [ ]   #List that holds all the titles of the videos of a playlist
nextPageToken    = None

while True:           #Loop through multiple pages of 50-values

    pl_request = youtube.playlistItems().list(
            part       ='contentDetails',
            playlistId = playlist_id,
            maxResults = 50,
            pageToken  = nextPageToken
        )

    pl_response = pl_request.execute()

    vid_ids = [ ]      #Save Video IDs from that page into a list

    for item in pl_response['items']:
        vid_ids.append ( item["contentDetails"]["videoId"] )

    # print(','.join(vid_ids))   #separate all values in a list with commas
    #------------------------------------------------------------------------#
    vid_request = youtube.videos().list(
            part       = "contentDetails, snippet",
            id         = ','.join(vid_ids),
            maxResults = 50
        )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        # print(item['snippet']['title'])
        video_title_list.append(item['snippet']['title'])

    nextPageToken = pl_response.get("nextPageToken")
    if not nextPageToken:
        break
#---------------------------------------------------------------------------#
with open('Video_Titles.txt', encoding='utf8') as file:
    saved_list   = file.read().splitlines()                   #Current local-save list of video titles
    current_list = [ song for song in video_title_list ]      #Current youtube-bases list of video titles

with open("Video_Titles.txt", "w", encoding="utf-8") as text_file:
    for song in video_title_list:
         text_file.write(str(song) + "\n")                    

songs_added   = [ song for song in current_list if song not in saved_list]
songs_removed = [ song for song in saved_list if song not in current_list]

current_time  = datetime.datetime.now()

if songs_removed:
    with open("Video_Titles_Removed.txt", "a+", encoding="utf-8") as text_file:
        text_file.write( f"Songs Removed on: {current_time} " + "\n\n")
        for song in songs_removed:
            text_file.write(str(song) + "\n")
        text_file.write( "#-----------------------------------------------#\n\n")

if songs_added:
    with open("Video_Titles_Added.txt", "a+", encoding="utf-8") as text_file:
        text_file.write( f"Songs Added on: {current_time} " + "\n\n")
        for song in songs_added:
            text_file.write(str(song) + "\n")
        text_file.write( "#-----------------------------------------------#\n\n")

# print("Done")
