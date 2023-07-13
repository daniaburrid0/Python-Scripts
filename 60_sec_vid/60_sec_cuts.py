# Importing necessary libraries
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os
from tqdm import tqdm

# This function takes a video file path as an input, cuts it into clips of the specified duration,
# and saves them in a new directory with the same name as the video file.
def cut_video(path, clip_duration=60):
    # Load the video file from the path
    clip = VideoFileClip(path)
    
    # Get the duration of the video in seconds
    duration = clip.duration
    
    # Extract the filename and the directory from the path
    filename = os.path.basename(path)
    filename_without_ext = os.path.splitext(filename)[0]
    dir_name = os.path.dirname(path)
    
    # Define the output folder and create it if it doesn't exist
    output_folder = os.path.join(dir_name, filename_without_ext)
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except OSError as e:
            print(f"Error creating output folder: {e}")
            return
    
    # If the video is shorter than the clip duration, copy it to the output folder
    if duration <= clip_duration:
        output = os.path.join(output_folder, f"{filename_without_ext}_1.mp4")
        clip.write_videofile(output)
        return
    
    # Cut the video into clips of the specified duration
    num_clips = int(duration / clip_duration) + 1
    for i in tqdm(range(num_clips)):
        start_time = i * clip_duration
        end_time = min((i + 1) * clip_duration, duration)
        output = os.path.join(output_folder, f"{filename_without_ext}_{i+1}.mp4")
        ffmpeg_extract_subclip(path, start_time, end_time, targetname=output)

# This function prompts the user for a video file path and performs basic error checking.
def get_user_input():
    while True:
        path = input("Please enter the path to the video file: ")
        if not os.path.isfile(path):
            print("The path you entered does not exist. Please try again.")
        elif not path.lower().endswith(('.mp4', '.flv', '.avi', '.mov', '.wmv', '.mkv')):
            print("The file you entered is not a recognized video format (.mp4, .flv, .avi, .mov, .wmv, .mkv). Please try again.")
        else:
            return path

# This is the main function that coordinates the user input and the video cutting.
def main():
    video_path = get_user_input()
    clip_duration = int(input("Please enter the clip duration in seconds (default is 60): ") or "60")
    cut_video(video_path, clip_duration)

# This is the entry point of the script. When the script is run, it calls the main function.
if __name__ == "__main__":
    main()
