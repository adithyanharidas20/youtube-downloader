import subprocess
import math
import os
import platform

def compress_video(input_file, output_file, target_size_mb):
    """
    Compress a video to a target size without significant quality loss.
    
    Args:
        input_file (str): Path to the input video file.
        output_file (str): Path to the output compressed video file.
        target_size_mb (float): Desired output file size in megabytes.
    """
    # Convert target size from MB to bits
    target_size_bits = target_size_mb * 8 * 1024 * 1024

    # Get video duration in seconds using FFmpeg
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "error", "-select_streams", "v:0",
                "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", input_file
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        duration = float(result.stdout.strip())
    except Exception as e:
        print("Error obtaining video duration:", e)
        return
    
    # Calculate the target bitrate in bits per second
    target_bitrate = target_size_bits / duration

    # Determine the null equivalent for the system
    null_output = "NUL" if platform.system() == "Windows" else "/dev/null"

    # Encode the video using the calculated bitrate
    try:
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", input_file, "-b:v", f"{math.floor(target_bitrate)}", 
                "-pass", "1", "-c:v", "libx264", "-preset", "slow", "-c:a", "aac", 
                "-b:a", "128k", "-f", "mp4", null_output
            ],
            check=True
        )
        subprocess.run(
            [
                "ffmpeg", "-y", "-i", input_file, "-b:v", f"{math.floor(target_bitrate)}", 
                "-pass", "2", "-c:v", "libx264", "-preset", "slow", "-c:a", "aac", 
                "-b:a", "128k", output_file
            ],
            check=True
        )
        print(f"Compression complete. Output saved to {output_file}.")
    except subprocess.CalledProcessError as e:
        print("Error during compression:", e)

# Main function to get user inputs and run compression
def main():
    input_file = input("Enter the path of the video file to be compressed: ").strip()
    if not os.path.isfile(input_file):
        print("Error: File not found. Please check the path and try again.")
        return
    
    output_file = input("Enter the path for the output compressed video: ").strip()
    target_size_mb = float(input("Enter the desired output file size in MB: ").strip())
    
    compress_video(input_file, output_file, target_size_mb)

if __name__ == "__main__":
    main()
