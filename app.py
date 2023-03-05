import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips ,CompositeAudioClip


# PICK RANDOM NUMBER FROM LENGTH OF VIDEO FILE THERE ARE IN VIDEOS FOLDER 

lenVideos = len(os.listdir('./videos'))

# RESIVE INPUT FROM USER HOW MUCH VIDEO HE WANT TO COMBILE 

combileLen = int(input(f'How Many Videos You Want To MIX (avalable videos {lenVideos}) ? :'))

# validating user input if avalable videos equals with require mix 

while combileLen > lenVideos:
    combileLen = int(input(f'There is only {lenVideos} videos plase insert correct mix value ? :'))



# CREATE RANDOM NUMBERS BASED ON USERINPUT(combileLen) = videoIDs
# use random number to select random video from videos folder (readyToMIX)

videoIDs = []
readyToMIX = []

for i in range(combileLen):
    id = random.randint(1,lenVideos)
    # if id don't exist in list add the id
    while id in videoIDs:
        id = random.randint(1,lenVideos)
    videoIDs.append(id)
    readyToMIX.append(VideoFileClip(f"./videos/{id}.mp4"))




# COMBILE TEH VIDEOS

print(f'mixing videos, IDs:{videoIDs}')

final_clip = concatenate_videoclips(readyToMIX)


# Adding the background music 

mixed_audio = final_clip.audio # background audio of our mixed videos

bg_music = AudioFileClip("./audios/1.mp3") # background music that we want to add

bg_music = CompositeAudioClip([bg_music] * (int(mixed_audio.duration / bg_music.duration) + 1)) # ajusting the background music to fit our mix video length

bg_music = bg_music.set_duration(mixed_audio.duration) 

final_audio = CompositeAudioClip([mixed_audio, bg_music]) # mixing the audios (mixed video background + the new backgound music)

final_clip = final_clip.set_audio(final_audio) # finaliy seting the audio 

# Save(Export) the Video

final_clip.write_videofile("./output/finjkjal.mp4")

