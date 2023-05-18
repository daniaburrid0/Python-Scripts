# Importing necessary libraries
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import os

# This function takes a video file path as an input, cuts it into 60-second clips, 
# and saves them in a new directory with the same name as the video file.
def cut_video(path):
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
        os.makedirs(output_folder)
    
    # If the video is longer than 60 seconds, cut it into 60-second clips
    if duration > 60:
        start_time = 0
        end_time = 60
        i = 1

        while start_time < duration:
            output = os.path.join(output_folder, f"{filename_without_ext}_{i}.mp4")
            
            # Extract the clip from start_time to end_time and save it
            ffmpeg_extract_subclip(path, start_time, min(end_time, duration), targetname=output)
            
            # Update start_time and end_time for the next clip
            start_time += 60
            end_time += 60
            i += 1
    else:
        # If the video is 60 seconds or less, copy it to the output folder
        output = os.path.join(output_folder, f"{filename_without_ext}_1.mp4")
        clip.write_videofile(output)

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
    cut_video(video_path)

# This is the entry point of the script. When the script is run, it calls the main function.
if __name__ == "__main__":
    main()
