# youtube_playlist_tracker

Do you hate it when a video has been deleted from your music playlist in Youtube?
And you can't seem to find the title of the video? 

With this python script you can constantly monitor your playlist and keep track of videos added and removed.

Steps:
* Create an Api key
* Save the key as env variable
* Find your music playlist_id
* Run the script (better as a cron job)

The scripts works with 3 txt files:
1. `Video_Titles.txt` will keep the current video-titles that are on youtube-playlist
2. `Video_Titles_Removed.txt` will keep the video-titles that are removed from the playlist
3. `Video_Titles_Added.txt` will keep the video-titles that are added to the playlist
