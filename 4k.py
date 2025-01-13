import yt_dlp

def download_video_4k():
    try:
        # Input YouTube video URL
        url = input("Enter the YouTube video URL: ")
        
        # Input custom output filename (without extension)
        custom_filename = input("Enter the desired output filename (without extension): ")
        
        # Options for yt-dlp
        ydl_opts = {
            'format': 'bestvideo[height=2160]+bestaudio/best[height=2160]',  # 4K video + best audio
            'outtmpl': f'{custom_filename}.%(ext)s',  # User-defined output filename
            'merge_output_format': 'mp4',  # Merge output format
        }
        
        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading in 4K...")
            ydl.download([url])
            print("Download completed successfully!")
    
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    download_video_4k()
