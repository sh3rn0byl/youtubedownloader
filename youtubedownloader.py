#!/usr/bin/python

import os
from pytube import YouTube as yt
from pytube import Playlist
import time

print("\n\nWelcome to Youtube Downloader\n\n")

loop = True
while loop :

    print("###############################################\n")

    print("Choose 1 for audio and 2 for video or quit to exit the program :")
    av = str(input("-1- Audio \n-2- Video\n====> "))

    while av != "1" and av != "2" and av != "quit":
        print("\nError_occured : Invalid choice\n")
        av = input("Choose 1 for audio or 2 for video or quit to exit the program :\n====>")
    if av == "quit":
        exit()

    print("\n##############################################\n")

    print("Choose 1 for Playlist and 2 for single video")
    playlist_svideo = input("-1- Playlist \n-2- Single Video \n====> ")

    while playlist_svideo != "1" and playlist_svideo != "2" and playlist_svideo != "quit":
        print("\nError_occured : Invalid choice")
        playlist_svideo = input("Choose 1 for Playlist or 2 for single video or quit to exit the program :\n====> ")
    if playlist_svideo == "quit":
        exit()

    print("\n##############################################\n")

    HOME_DIR = os.path.expanduser("~")
    print("Where you wanna output this file ?\nby default the audio go to the [music] folder and the video go to the [video] folder")
    path_choice = input(">>>$HOME/")

    if path_choice == "":
        if av == "1":
            full_path = os.path.join(HOME_DIR , "Music/")
        elif av == "2":
            full_path = os.path.join(HOME_DIR , "Videos/")


    elif path_choice != None:

        full_path = os.path.join(HOME_DIR , path_choice)

    def downloader(aud_vid , plist_svideo , path):
        print("\n##############################################\n")

        url = input("Enter the url of the video or playlist\n====> ")

        print("\n##############################################\n")

        try :
            # First if statement for downloading the audio
            if aud_vid == "1" :

                if plist_svideo == "1" : # This one is for audio playlist
                    aud_playlist = Playlist(url)
                    print(f"[+] Downloading {aud_playlist.title}...")
                    for music in aud_playlist.videos :
                        music.streams.filter(only_audio=True,abr="128kbps").first().download(path)
                        print("[+] Download completed")

                elif plist_svideo == "2" : # This one is for single audio
                    aud_single = yt(url)
                    print(f"[+] Downloading {aud_single.title}...")
                    out_file = aud_single.streams.get_by_itag(140).download(path)
                    print("[+] Download completed\n")
                    print("[+] Converting to mp3 format...")
                    base, ext = os.path.splitext(out_file)
                    new_file = base + ".mp3"
                    os.rename(out_file, new_file)
                    time.sleep(3)
                    print("[+] Successfully converted")

            elif aud_vid == "2" : # This elif is for Videos

                if plist_svideo == "1" : # For playlists
                    vid_playlist = Playlist(url)
                    print(f"[+] Downloading {vid_playlist.title}...")
                    for video in vid_playlist.videos:
                        video.streams.get_highest_resolution().download(path)
                    print("[+] Download completed")

                elif plist_svideo == "2" : # For single video
                    vid_single = yt(url)
                    print(f"[+] Downloading {vid_single.title}...")
                    vid_single.streams.get_highest_resolution().download(path)
                    print("[+] Download completed")


        except Exception as e:

            print(e)

    downloader(av , playlist_svideo , full_path)
