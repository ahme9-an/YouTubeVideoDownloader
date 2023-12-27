import threading
from tkinter import *
from pytube import YouTube
import os
def downloadytv():
    resolution = resolution_var.get()
    url = link.get()
    download_path = download_dir.get()
    def show_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        progress_label.config(text=f"Downloading... {percentage_of_completion:.2f}%")
    def download_video():
        try:
            yt = YouTube(url)
            yt.register_on_progress_callback(show_progress)
            video = yt.streams.filter(res=resolution, file_extension='mp4').first()
            if video:
                video.download(output_path=download_path)
                progress_label.config(text=f"Downloaded: {yt.title}")
            else:
                progress_label.config(text="Video at specified resolution not found.")
        except Exception as e:
            progress_label.config(text=f"Error: {str(e)}")
    threading.Thread(target=download_video).start()
root = Tk()
root.geometry('500x300')
f1 = Frame(root)
f1.grid()
Label(f1, text='=====Youtube Video Downloader=====', font=15, padx=6).grid(row=0, columnspan=2)
Label(f1, text='Enter link here', font=5).grid(row=1)
link = StringVar()
Entry(f1, font=5, textvariable=link).grid(row=1, column=1, pady=5, padx=10)
Label(f1, text='Select resolution', font=5).grid(row=2)
resolution_var = StringVar()
resolution_choices = ['1080p', '720p', '480p', '360p', '240p', '144p']
resolution_var.set('720p')  # default resolution
OptionMenu(f1, resolution_var, *resolution_choices).grid(row=2, column=1)
download_dir = StringVar()
download_dir.set(os.getcwd())  # default download directory
Entry(f1, font=5, textvariable=download_dir).grid(row=3, column=1, pady=5, padx=10)
Label(f1, text='Download Directory', font=5).grid(row=3)
Button(f1, text='Download', padx=50, relief=RAISED, font=10, borderwidth=5, command=downloadytv).grid(row=4, column=1, pady=5)
progress_label = Label(root, text="Download Progress", font=5)
progress_label.grid(row=5, columnspan=2, pady=10)
root.mainloop()
