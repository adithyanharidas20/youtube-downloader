import yt_dlp
import subprocess
import os

def download_compressed_video():
    try:
        # Input YouTube video URL
        url = input("Enter the YouTube video URL: ")

        # Input custom output filename (without extension)
        custom_filename = input("Enter the desired output filename (without extension): ")

        # Temporary download file name
        temp_file = f"{custom_filename}_temp.mp4"

        # Compressed file name
        compressed_file = f"{custom_filename}_compressed.mp4"

        # Options for yt-dlp
        ydl_opts = {
            'format': 'bestvideo[height=2160]+bestaudio/best[height=2160]',  # 4K video + best audio
            'outtmpl': temp_file,  # Temporary file for initial download
            'merge_output_format': 'mp4',  # Merge output format
        }

        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading video in 4K...")
            ydl.download([url])
            print("Download completed successfully!")

        # Compress the video using ffmpeg
        print("Compressing video to maintain 4K quality...")
        ffmpeg_command = [
            "ffmpeg", "-i", temp_file, "-vf", "scale=3840:2160", "-vcodec", "libx265", "-crf", "18", compressed_file
        ]
        subprocess.run(ffmpeg_command, check=True)

        # Remove the temporary file
        os.remove(temp_file)

        print(f"Compressed file saved as: {compressed_file}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    download_compressed_video()
