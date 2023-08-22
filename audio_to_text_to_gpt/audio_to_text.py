import openai
from docx import Document
from moviepy.editor import VideoFileClip

def trancribe_audio(audio_path):
    with open(audio_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    key_points = key_points_extraction(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
    }

def abstract_summary_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def key_points_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

def saves_to_docx(minutes, filename):
    doc = Document()
    for k, v in minutes.items():
        heading = ' '.join(word.capitalize() for word in k.split('_'))
        doc.add_heading(heading, level=1)
        doc.add_paragraph(v)
        # Add a line break between sections
        doc.add_paragraph()
    doc.save(filename)

def extract_audio_from_video(video_path):
    # Load the video file
    clip = VideoFileClip(video_path)

    # Extract the audio and save it as an MP3 file
    audio = clip.audio
    audio.write_audiofile("audio.mp3")

    # Close the video file
    clip.close()
    return "audio.mp3"
    
def main():
    # set up the api key
    openai.api_key_path = "api_key.key"
    # ask [1] for video or [2] for audio
    choice = input("Enter [1] for video or [2] for audio: ")
    if choice == '1':
        # ask the path to the user
        video_path = input("Enter the path to the video file: ")
        audio_path = extract_audio_from_video(video_path)
    elif choice == '2':
        # ask the path to the user
        audio_path = input("Enter the path to the audio file: ") 
    
    transcripton = trancribe_audio(audio_path)
    minutes = meeting_minutes(transcripton)
    print(minutes)
    # ask for the filename
    filename = input("Enter the filename: ")
    saves_to_docx(minutes, filename+'.docx')
    
if __name__ == '__main__':
    main()