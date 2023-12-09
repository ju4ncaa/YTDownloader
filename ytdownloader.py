# Author: 0xJuaNc4

# Modules
from os import system, name, getcwd
from pytube import YouTube
from time import sleep

# Colors palette
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

# Banner
def banner():
    system("cls" if name == "nt" else "clear")
    print(f"""{Colors.RED}
    __  ___________                  __             __       
    \ \/ /_  __/ _ \___ _    _____  / /__  ___ ____/ /__ ____
     \  / / / / // / _ \ |/|/ / _ \/ / _ \/ _ `/ _  / -_) __/   {Colors.YELLOW}(Made by 0xJuaNc4){Colors.RED}
     /_/ /_/ /____/\___/__,__/_//_/_/\___/\_,_/\_,_/\__/_/   
    {Colors.RESET}""")
    sleep(1)

# Download YouTube video
def download_video():
    video_url = input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Enter the url of the video you want to download: ")
    try:
        yt = YouTube(video_url)
        print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Loading video...")
        sleep(2)
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Video {Colors.YELLOW}{yt.title}{Colors.RESET} loaded!")
        print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Available download formats\n\n{Colors.YELLOW}1){Colors.RESET} mp3\n{Colors.YELLOW}2){Colors.RESET} mp4")
        user_choice = input(f"\n{Colors.YELLOW}[*]{Colors.RESET} Choose the video format: ")
        if user_choice.lower() == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
            extension = "mp3"
            print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Obtaining the highest audio quality...")
        elif user_choice.lower() == "mp4":
            stream = yt.streams.get_highest_resolution()
            extension = "mp4"
            print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Obtaining the highest video resolution...")
        else:
            print(f"\n{Colors.RED}[!]{Colors.RESET} The format you have entered is not valid, it must be mp3 or mp4.")
        sleep(2)
        print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Downloading {Colors.YELLOW}{yt.title}{Colors.RESET}...")
        stream.download(output_path=f"{getcwd()}/Downloads", filename=f"{yt.title}.{extension}")
        sleep(2)
        print(f"\n{Colors.GREEN}[*]{Colors.RESET} Download completed!")
        sleep(1)
        print(f"\n{Colors.YELLOW}[*]{Colors.RESET} Video saved in {Colors.YELLOW}{getcwd()}/Downloads{Colors.RESET}\n")
    except Exception as e:
        print(f"\n{Colors.RED}[!]{Colors.RESET} Error: {str(e)}\n")

# Main program
if __name__ == "__main__":
    try:
        banner()
        download_video()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!]{Colors.RESET} Exiting...\n")
