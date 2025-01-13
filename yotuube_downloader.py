import yt_dlp

def download_video_1080p():
    try:
        # Input YouTube video URL
        url = input("Enter the YouTube video URL: ")
        
        # Options for yt-dlp
        ydl_opts = {
            'format': 'bestvideo[height=1080]+bestaudio/best[height=1080]',  # 1080p video + best audio
            'outtmpl': 'valiban1080p.%(ext)s',  # Output file name
            'merge_output_format': 'mp4',  # Merge output format
        }
        
        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading in 1080p...")
            ydl.download([url])
            print("Download completed successfully!")
    
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    download_video_1080p()
