---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-11_hacking-hackerone-how-computer-vision-helped-uncover-hidden-vulnerabilities.md
original_filename: 2023-05-11_hacking-hackerone-how-computer-vision-helped-uncover-hidden-vulnerabilities.md
title: 'Hacking HackerOne: How computer vision helped uncover hidden vulnerabilities?'
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 15bc8b43260dcc35aba58ce57b63bfb621746959c69628128f3d2fa1baaf7792
text_sha256: 45366948ce1d01fe7fc47c7c14616c395a961ba0bb38acc9e6652ef4d1de0429
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking HackerOne: How computer vision helped uncover hidden vulnerabilities?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-11_hacking-hackerone-how-computer-vision-helped-uncover-hidden-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `15bc8b43260dcc35aba58ce57b63bfb621746959c69628128f3d2fa1baaf7792`
- Text SHA256: `45366948ce1d01fe7fc47c7c14616c395a961ba0bb38acc9e6652ef4d1de0429`


## Content

---
title: "Hacking HackerOne: How computer vision helped uncover hidden vulnerabilities?"
url: "https://3bodymo.medium.com/hacking-hackerone-how-computer-vision-helped-uncover-hidden-vulnerabilities-858d03a6a67"
authors: ["Abdullah Mohamed (@3bodymo_)"]
programs: ["HackerOne"]
bugs: ["Information disclosure", "AI"]
publication_date: "2023-05-11"
added_date: "2023-06-25"
source: "pentester.land/writeups.json"
original_index: 1164
scraped_via: "browseros"
---

# Hacking HackerOne: How computer vision helped uncover hidden vulnerabilities?

Hacking HackerOne: How computer vision helped uncover hidden vulnerabilities?
Abdullah Abdelrazek
Follow
9 min read
·
May 11, 2023

220

2

Press enter or click to view image in full size

Hello everyone! Today, I would like to share my experience using artificial intelligence to scan all the disclosed videos on HackerOne. I will discuss how I successfully developed an AI model that enabled me to report multiple reports based on the model’s results.

The Main Problem

HackerOne was accepting any report about reporting undisclosed reports in the disclosed reports video.
It seems a little confusing, so I will give an example until I can explain it more clearly.

Let’s take this disclosed report as an example, #1294767:

Press enter or click to view image in full size

The report contains a recorded video that the bug hunter recorded as a PoC for his report; the problem is that there are undisclosed reports shown in that video (at the left side).

Press enter or click to view image in full size
An idea

We need a way to scan every video in disclosed reports on the platform; if you do it in a convention way and discover every video manually, it could take weeks, so we have to find an optimal way to do it.

We could find a way to do that with the help of AI and computer vision, so the first thing to do is to know how we will train our AI model.

AI Model Approach

The first solution that came to my mind was to use the image classification approach, but I thought it would not be a better choice for this problem, so I thought to solve it with object detection.
I will give you an example for those types of models until you know the difference.

Image classification model: The image classification model will be designed to take a video frame as input and classify it as either containing undisclosed reports or not. However, a challenge arises during dataset collection, as acquiring a sufficient amount of the “NOT” class (frames without disclosed reports) can be difficult. This scarcity of negative examples might hinder the model’s training process and affect its overall performance.

Object detection model: On the other hand, the object detection model operates by analyzing a video frame and identifying specific objects that it has been trained on. Rather than focusing on classifying the frame as a whole, the model localizes and recognizes individual objects within the frame based on its training data.

For the dataset part, I decided to collect 250 screenshots, so I opened my HackerOne account and my friend’s account and started taking screenshots.

Press enter or click to view image in full size

I chose this part as an object (the red rectangle), so later, when the model sees this part in videos, it will detect it.

Since the screenshots are taken in the same way and the screen doesn’t change, the annotation boxes coordinates will not change in all images.
I opened labelImg (a Python tool that allows you to annotate your objects) and I labelled only one image, then I made a small script to copy this annotation information to all images.

import os

image_folder_path = './images'
text_folder_path = './train/labels'
image_file_list = os.listdir(image_folder_path)

coordinates = "0 0.170047 0.550314 0.254717 0.798742"

for image_file_name in image_file_list:
  file_basename = os.path.splitext(image_file_name)[0]
  text_file_name = file_basename + '.txt'
  text_file_path = os.path.join(text_folder_path, text_file_name)
  with open(text_file_path, 'w') as text_file:
  text_file.write(coordinates)

The bounding box (coordinates) here is represented by five values [object-class, x_center, y_center, width, height]. The object-class refers to the class label of the object within the bounding box. It represents the category or type of object that the bounding box is representing. It is typically represented as an integer value corresponding to a specific class or category. The x_center and y_center are the normalized coordinates of the center of the bounding box. To make coordinates normalized, we take pixel values of x and y, which marks the center of the bounding box on the x-axis and y-axis. Then we divide the value of x by the width of the image and value of y by the height of the image. The width and height represent the width and the height of the bounding box. They are normalized as well.

The labelImg creates one text file for each image, and it saves the annotation boxes coordinates in that text file, so here I put the coordinates value in the coordinates variable and read the image name, then create a text file named as the image name containing the value of the coordinates.

I trained my model using an object detection algorithm based on YOLO principles.

YOLOv7 is a real-time object detection algorithm that was developed by the Academia Sinica AI Lab in Taiwan. It is the seventh version of the YOLO (You Only Look Once) object detection algorithm, and it is one of the most accurate and efficient object detection algorithms available today.
YOLOv7 is a single-stage object detector, which means that it can detect objects in a single pass through an image. This makes it much faster than two-stage object detectors, such as Faster R-CNN. YOLOv7 is also very accurate, and it has been shown to outperform other object detection algorithms on a variety of datasets.

The model performed well in training and testing, but I got a lot of false positives on other videos that don’t contain disclosed reports, and it also didn’t perform well in detecting vulnerable videos.

Press enter or click to view image in full size

This is an example of a false positive result; the model considers this part as an exposed report with high confidence.
So, I have to find another optimal way to improve the model and make it better at detection.

I changed the way of annotation, and I made it like this:

Press enter or click to view image in full size

Here I have to make the annotation process manually because every box has a different size and different location.

Get Abdullah Abdelrazek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I thought it would perform better, and yes, after training the model, the false positive detection was less and the model was detecting better.

Press enter or click to view image in full size
Discover Videos

Now, we have to find a way to download all videos from all disclosed reports.
I searched to see if I can get the report information in JSON format until I can deal with it easily. I remembered there is an export feature in the report page, but when I clicked on it, I didn’t find JSON format, but I found pdf, zip, and raw text. I did choose pdf until I saw what the URL would look like. It just adds .pdf to end of report number:

https://hackerone.com/reports/1294767.pdf

I quickly changed .pdf to .json and yeah the report now shows in JSON format.

Now I have to make a Python script to download all videos from all disclosed reports.

But first we have to get all the numbers of disclosed reports, so I searched for a while to see if someone was collecting these reports, and I found this useful repo on GitHub. He also uploaded a Python script until you could get updated reports.

Let’s start the work..

Exploit Time!

At first, we have to extract report numbers from the csv file, so I made this useful script that will extract them and save them in a text file.

import csv

csv_file = 'data.csv' # The csv file in the repo
output_file = 'report_numbers.txt'

with open(csv_file, 'r') as file:
  reader = csv.reader(file)
  next(reader)
  numbers = [row[2].split('/')[-1] for row in reader if int(row[2].split('/')[-1])]

numbers.sort(reverse=True)

with open(output_file, 'w') as file:
  file.write('\n'.join(numbers))

After that, I made another script to download all videos from a report.

import requests
import json
import os

if not os.path.exists('videos'):
  os.makedirs('videos')

with open('report_numbers.txt', 'r') as file:
  report_numbers = file.readlines()

i = 0
for report_number in report_numbers:
  i = i + 1
  report_number = report_number.strip()
  endpoint = f"https://hackerone.com/reports/{report_number}.json"
  response = requests.get(endpoint)
  
  print(f"{i}/{len(report_numbers)}")

  if response.status_code == 404:
  continue

  if response.status_code == 200:
  data = response.json()
  
  if 'attachments' in data:
  attachments = data['attachments']
  
  for attachment in attachments:
  if 'video‏‎' in attachment['type']:
  file_name_temp = attachment['file_name']
  file_name = file_name_temp.split('.')[0]
  file_ext = file_name_temp.split('.')[-1]
  new_file_name = f"{report_number}__{file_name}.{file_ext}"
  video_url = attachment['expiring_url']
  video_response = requests.get(video_url)
  if video_response.status_code == 200:
  print("Video has been downloaded!")
  video_path = os.path.join('videos', new_file_name)
  with open(video_path, 'wb') as video_file:
  video_file.write(video_response.content)
  
  if 'activities' in data:
  activities = data['activities']

  for activity in activities:
  if 'attachments' in activity:
  attachments = activity['attachments']
  for attachment in attachments:
  if 'video' in attachment['type']:
  file_name_temp = attachment['filename']
  file_name = file_name_temp.split('.')[0]
  file_ext = file_name_temp.split('.')[-1]
  new_file_name = f"{report_number}__{file_name}.{file_ext}"
  video_url = attachment['url']
  video_response = requests.get(video_url)
  if video_response.status_code == 200:
  print("Video has been downloaded!")
  video_path = os.path.join('videos', new_file_name)
  with open(video_path, 'wb') as video_file:
  video_file.write(video_response.content)

Let’s explain how this script works. At first, we have two types of videos: the first is the video that has been uploaded when you write the report, this will be in data['attachments']['expiring_url'], and the second type will be uploaded in comments, this will be in data['activities']['attachments']['url'].

Notice that the data is the whole JSON response.

One important thing is to link the downloaded video with the report number, so when I download the video, I rename it to {report number}__{original video name}.{video extension}

The second part is to pass those videos to my model, but the problem is that there are so many videos, and the model will take a long time to detect vulnerable videos because it scans every frame in the video.
An idea came to my mind. What if I reduce video frames to three frames per second only? That is a good enough number to detect if there is an undisclosed report in the video.

Reducing the number of frames will save us 10 times the time that the model would have taken if we did not reduce the frame rates, assuming that the average frame rate for one video is 30 frames per second.

There is another problem: YOLOv7 cannot deal with webm videos, so I have to convert this type of video to mp4 using ffmpeg. I made a small Python script to automate these tasks (converting webm videos to mp4 and reducing the number of frames).

import os
import subprocess

folder_path = "./videos"

def reduce_frames(input_file, output_file):
  subprocess.call(['ffmpeg', '-i', input_file, '-r', '3', output_file])

def convert_folder_videos(folder_path):
  i = 0
  total = len(os.listdir(folder_path))
  for filename in os.listdir(folder_path):
  i = i + 1
  print(f"{i}/{total}")
  if filename.endswith(".webm"):
  try:
  input_file = os.path.join(folder_path, filename)
  output_file = os.path.join(folder_path, os.path.splitext(filename)[0] + ".mp4")
  reduce_frames(input_file, output_file)
  print(f"Converted {input_file} to {output_file}")
  os.remove(input_file)
  except:
  continue
  else:
  try:
  input_file = os.path.join(folder_path, filename)
  output_file = os.path.join(folder_path, os.path.splitext(filename)[0] + "__reduced" + os.path.splitext(filename)[-1])
  reduce_frames(input_file, output_file)
  print(f"Converted {input_file} to {output_file}")
  os.remove(input_file)
  except:
  continue

convert_folder_videos(folder_path)

Now we are ready to pass the videos to our model.

python detect.py --weights best.pt --conf 0.50 --img-size 640 --source ./video-scan/videos/ --name new-scan

After running this command, the model will save the videos in which it has detected objects (undisclosed reports).

Since there are false positive results, we have to watch those videos manually until we can determine if they actually contain undisclosed reports or not.

At the end, the model detected tens of videos, but some of these videos did not contain undisclosed reports (the only report that was shown in the video was the disclosed report, from which we downloaded the current video), this is one of those examples:

Press enter or click to view image in full size

I submitted nearly 15 reports to HackerOne, but unfortunately, they decided not to pay for them. After my reporting, they declared these type of reports will be out of scope and closed all my reports as informative. Additionally, they informed me that they had mistakenly paid for previous reports with a similar concept.

Press enter or click to view image in full size

Update: we escalated the case to Jobert Abma (Co-founder of HackerOne), and they have decided to pay for all the reports. I’m extremely grateful to him.

Press enter or click to view image in full size

Thanks for your reading, I hope my story was useful.
