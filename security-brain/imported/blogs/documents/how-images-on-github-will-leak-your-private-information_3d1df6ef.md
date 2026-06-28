---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-24_how-images-on-github-will-leak-your-private-information.md
original_filename: 2020-11-24_how-images-on-github-will-leak-your-private-information.md
title: How images on Github will leak your private information
category: documents
detected_topics:
- sso
- command-injection
- information-disclosure
tags:
- imported
- documents
- sso
- command-injection
- information-disclosure
language: en
raw_sha256: 3d1df6efcbb55422c1e681c8783492f5a0e523df9096e23375e87729f6cfd5fd
text_sha256: ded3614d77695a57bf7f803ab973d75fce941210fa1646c50866a6a847294b1e
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How images on Github will leak your private information

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-24_how-images-on-github-will-leak-your-private-information.md
- Source Type: markdown
- Detected Topics: sso, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `3d1df6efcbb55422c1e681c8783492f5a0e523df9096e23375e87729f6cfd5fd`
- Text SHA256: `ded3614d77695a57bf7f803ab973d75fce941210fa1646c50866a6a847294b1e`


## Content

---
title: "How images on Github will leak your private information"
url: "https://fuomag9.medium.com/how-images-on-github-will-leak-your-private-information-88f3b563e7d9"
authors: ["fuomag9 (@fuomag9)"]
programs: ["GitHub"]
bugs: ["Information disclosure"]
publication_date: "2020-11-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4108
scraped_via: "browseros"
---

# How images on Github will leak your private information

How images on Github will leak your private information
fuomag9
Follow
2 min read
·
Nov 24, 2020

31

I was browsing a github repository where a guy posted its food travel pictures and while the pics were very appetizing, my mind wondered if there was information associated with the pictures he posted.

Press enter or click to view image in full size
And there was data, A LOT OF DATA

By putting the URLs on exif viewer, there was information about device, GPS data, time, software used, etc. I started searching on github for every place that would allow me to upload images that were vulnerable and the two locations I found were the Leave a comment functionality and the Social preview feature in the github repositories.

By doing futher tests I even discovered that images were not immediately deleted from the servers if uploaded from the comments interface but never sent. (Is this the new google photos?)

Get fuomag9’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The following are the POCs I made in the hackerone report to show this behaviour:

Social preview:
Create a repository
Go to the repository settings page (i.g. https://github.com/fuomag9/POC/settings)
Upload a social preview image via the GUI that contains EXIF data
Obtain the image URL by page inspection or other methods (i.g. https://repository-images.githubusercontent.com/305512860/cf5bea80-1260-11eb-9c8c-b3654d358e62)
Use an EXIF viewer tool, such as http://exif-viewer.com/ and put the image URL on it
Metadata will be shown
Github issues:
Create a repository
Create an issue
Drop an image in the Leave a comment that contains EXIF data in textbox from your device
Wait for the upload to be completed
Copy the image URL (i.g. https://user-images.githubusercontent.com/1580624/96513784-f74c4d80-1262-11eb-94b9-3715dc68e388.jpg)
Use an EXIF viewer tool, such as http://exif-viewer.com/ and put the image URL on it
Metadata will be shown
How did github respond to the issue? Well…

Thanks for the submission! We have reviewed your report and validated your findings. After internally assessing the finding we have determined it is a known low risk issue. We may make this functionality more strict in the future, but don’t have anything to announce right now. As a result, this is not eligible for reward under the Bug Bounty program.

Even though it’s a confirmed issue with other platform such as gitlab, github does NOT consider it to be an issue. Furthermore, it got closed as informative seconds after being reported (Such fast triaging!) but I had to wait a month to get a response about disclosure. (But they don’t disclose reports on hackerone 🤷)
