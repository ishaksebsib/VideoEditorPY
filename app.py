import os
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips


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


# Save(Export) the Video

final_clip.write_videofile("./output/final.mp4")

