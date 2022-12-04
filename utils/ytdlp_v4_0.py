import json
import yt_dlp
import os
from time import *
import requests




class AudioFile:

    def __init__(self, link):
        self.url = link
        self.home_dir = "/data/data/com.termux/files/home"
        self.bot_home_dir = "/data/data/com.termux/files/home/ub"
        self.json_filepath = "/data/data/com.termux/files/home/ub/json"
        self.module_dir = "/data/data/com.termux/files/home/ub/ytdl_down"

    def download_file(self):
        ydl_opts = {
            'outtmpl': '/data/data/com.termux/files/home/ub/ytdl_down/%(title)s.%(ext)s',
            'writethumbnail': True,
            'format': 'bestaudio/best',
            'postprocessors':[
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'},
                {'key': 'FFmpegMetadata', 'add_metadata': 'True'},
                {'key': 'EmbedThumbnail','already_have_thumbnail': False}
            ]
        }
        self.audioformat = ydl_opts['postprocessors'][0]['preferredcodec']

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url, download=True)
            var1 = json.dumps(ydl.sanitize_info(info))
            data = json.loads(var1)
            self.json_name = data['id']+'.json'
            self.filename = data['title']+"."+self.audioformat
            self.thumm_link = data['thumbnail']
            self.thumm = str(self.thumm_link.split("/")[-1])
            os.chdir(self.json_filepath)

            with open(self.json_filepath+'/'+self.json_name, 'w', encoding='utf8') as file:
                json.dump(data, file, ensure_ascii=False,  sort_keys=True, indent=4)

        os.chdir(self.module_dir)
        r = requests.get(self.thumm_link)
        with open(self.thumm, "wb") as code:
            code.write(r.content)

    def show_json(self):
        with open(self.json_filepath+'/'+self.json_name, encoding='utf-8') as file:
            info = file.read()
            print(info)
        os.chdir(self.bot_home_dir)

    def info(self):
        with open(self.json_filepath+'/'+self.json_name, encoding='utf-8') as file:
            info = json.load(file)
            json_name = info['title']+"-"+info['id']+'.json'
            filename = info['title']+"."+self.audioformat
            thumm_link = info['thumbnail']
            thumm = str(self.thumm_link.split("/")[-1])
        print(
        f"""
        {json_name}\n
        {filename}\n
        {thumm_link}\n
        {thumm}\n
        """)

    def show_thumm(self):
        return self.thumm

    def show_path(self):
        return self.filepath

    def show_file_name(self):
        return self.filename

    def delete_json(self):
        os.remove(self.json_filepath+'/'+self.json_name)

    def remove_thumb(self):
        os.chdir(self.module_dir)
        mas = []
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if(file.endswith('.jpg')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)

                elif(file.endswith('.png')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)

                elif(file.endswith('.webp')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)

    def remove_audio_files(self):
        os.chdir(self.module_dir)
        mas = []
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if(file.endswith('.mp3')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)
                elif(file.endswith('.m4a')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)




class VideoFile:

    def __init__(self, link):
        self.url = link
        self.home_dir = "/data/data/com.termux/files/home"
        self.bot_home_dir = "/data/data/com.termux/files/home/ub"
        self.json_filepath = "/data/data/com.termux/files/home/ub/json"
        self.module_dir = "/data/data/com.termux/files/home/ub/ytdl_down"

    def download_file(self):
        ydl_opts = {
            'outtmpl': '/data/data/com.termux/files/home/ub/ytdl_down/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.url, download=True)
            var1 = json.dumps(ydl.sanitize_info(info))
            data = json.loads(var1)

            self.json_name = data['id']+"-"+data['title']+'.json'
            self.filename = data['title']+"."+"mp4"
            self.thumm_link = data['thumbnail']
            self.thumm = str(self.thumm_link.split("/")[-1])

        with open(self.json_filepath+'/'+self.json_name, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False,  sort_keys=True, indent=4)

        os.chdir(self.module_dir)
        r = requests.get(self.thumm_link)
        with open(self.thumm, "wb") as code:
            code.write(r.content)

    def show_json(self):
        with open(self.json_filepath+'/'+self.json_name, encoding='utf-8') as file:
            info = file.read()
            print(info)

    def info(self):
        with open(self.json_filepath+'/'+self.json_name, encoding='utf-8') as file:
            info = json.load(file)
            json_name = info['id']+"-"+info['tile']+'.json'
            filename = info['title']+"."+info["formats"][-2]["ext"]
            thumm_link = info['thumbnail']
            thumm = str(self.thumm_link.split("/")[-1])
        print(
        f"""
        {json_name}\n
        {filename}\n
        {thumm_link}\n
        {thumm}\n
        """)

    def show_thumm(self):
        return self.thumm

    def show_path(self):
        return self.filepath

    def show_file_name(self):
        return self.filename

    def delete_json(self):
        os.remove(self.json_filepath+'/'+self.json_name)

    def remove_thumb(self):
        os.chdir(self.module_dir)
        mas = []
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if(file.endswith('.jpg')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)

                elif(file.endswith('.png')):
                   mas.append(os.path.join(file))
                   for x in mas:
                       os.remove(x)

                elif(file.endswith('.webp')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)

    def remove_video_files(self):
        os.chdir(self.module_dir)
        mas = []
        for root, dirs, files in os.walk(os.getcwd()):
            for file in files:
                if(file.endswith('.mp4')):
                    mas.append(os.path.join(file))
                    for x in mas:
                        os.remove(x)



if __name__ == "__main__":

    linka = 'https://youtu.be/ZdLymG0Mb2Q'

    x=AudioFile(linka)
    x.download_file()
    x.info()

#    y=VideoFile(linka)
#    y.download_file()
#    y.info()
