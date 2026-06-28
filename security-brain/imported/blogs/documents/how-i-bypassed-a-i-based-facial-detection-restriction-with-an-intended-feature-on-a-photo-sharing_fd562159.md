---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-20_how-i-bypassed-ai-based-facial-detection-restriction-with-an-intended-feature-on.md
original_filename: 2024-01-20_how-i-bypassed-ai-based-facial-detection-restriction-with-an-intended-feature-on.md
title: How I Bypassed A.i. Based Facial Detection Restriction With An Intended Feature
  On A Photo Sharing App ?
category: documents
detected_topics:
- mobile-security
- command-injection
- path-traversal
- otp
- business-logic
- api-security
tags:
- imported
- documents
- mobile-security
- command-injection
- path-traversal
- otp
- business-logic
- api-security
language: en
raw_sha256: fd5621598a25bf3c81e03825c5cf5ce3aa8940bfea30919d157b8a47fda72143
text_sha256: ea624f128f539fece3e27393c44aa0a40e7e3bd3727ced31d3a5330618851b00
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# How I Bypassed A.i. Based Facial Detection Restriction With An Intended Feature On A Photo Sharing App ?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-20_how-i-bypassed-ai-based-facial-detection-restriction-with-an-intended-feature-on.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, path-traversal, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `fd5621598a25bf3c81e03825c5cf5ce3aa8940bfea30919d157b8a47fda72143`
- Text SHA256: `ea624f128f539fece3e27393c44aa0a40e7e3bd3727ced31d3a5330618851b00`


## Content

---
title: "How I Bypassed A.i. Based Facial Detection Restriction With An Intended Feature On A Photo Sharing App ?"
page_title: "HOW I BYPASSED A.I.. Introduction: | by Ishwar Kumar | Medium"
url: "https://medium.com/@Ishwar-Kumar/how-i-bypassed-a-i-6aa433370050"
authors: ["Ishwar Kumar"]
bugs: ["AI", "Logic flaw", "Facial recognition bypass"]
publication_date: "2024-01-20"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 514
scraped_via: "browseros"
---

# How I Bypassed A.i. Based Facial Detection Restriction With An Intended Feature On A Photo Sharing App ?

Ishwar Kumar
Follow
5 min read
·
Jan 21, 2024

12

2

HOW I BYPASSED A.I. BASED FACIAL DETECTION RESTRICTION WITH AN INTENDED FEATURE ON A PHOTO SHARING APP ?

Introduction:

Hello Readers,

I writing this article to share an Interesting bypass of A.I. based facial recognition system on a photo sharing application and its Implications I found if not managed or created securely. I will be keeping the application details confidential, for now we will call this application as “Test Application”.

Summary:

Before diving into explaining the vulnerability and why do I call it with Intended feature? Here’s an overview of how actually the Test Application works (functions):

In order to use the application:

The user has to signup with his/her email or phone number.

Now the user has to verify the OTP with their respective method of signup.

Once confirmed with all the verification of the user’s Identity successfully the Test Application now prompts the user’s to follow the procedure of facial recognition in order to use the application. (As a part of final step of successful registration). This is followed strictly and the user cannot skip this step as a part of the registration process.

Now you may ask where is the A.I. here being used ? :

Actually, This application uses A.I. in order to map the facial structure of its users so that it can map out your pictures from various group photos and place it under your profile section specifically. (So that you don’t have to take the pain as the user to go through each photo and find your pretty face, great feature isn’t it ?). This feature is extremely well working where in case there are lot of users and lot of pictures and A.I. can easily map out your face from all those pictures and list it under your profile section in the application.

Okay, so where is the vulnerability and why did I call it as an bypass with an Intended Feature? :

If followed all the steps successfully the user will be prompted to home section of the application. However on the facial recognition step, if the user taps out of the facial feature box intentionally, the application allows a feature of Importing of picture from the gallery (Intended Feature) rather than a live human face detection which helps in this bypass of facial recognition.

Now you may ask how ? :

Usually the A.I. based facial recognition system should map out the whole face, their textures, eyes (retina) , lips and enable proper check to be able to verify that the user or person is real rather than just a photograph which helps system to prevent bypassing of such crucial security measure. However in this case the A.I. detection pattern was flawed because it was only trained on detecting and verifying the user’s identity on 2 very crucial points, which are:

The face should be of a human.
The human face should be looking straight.

Something seems odd in here ?

Yes it is, since the A.I. fails to detect the difference between a real live detected human face and another deepfake or simply a normal human face, fulfilling the above 2 conditions anyone can simply import the picture and verify his/her identity and bypass this crucial step of security.

Press enter or click to view image in full size
Source: Internet
For testing reasons, I have tried:

I have tried to place an actual physical picture in front of the camera to see if the A.I. detects and verifies it, it didn’t since the more & more I came up close with the camera and the picture it actually it got blur and got detected.

What if the picture did not go blur ? Will it be accepted then ? :

Maybe yes, but it is not possible since it was detected at the first step as the picture goes blur. If the attacker finds a way to place the actual physical picture without making it blur, it can be bypassed. However it is extremely difficult to do that.

What if it was a deepfake picture ? Will it be able to bypass the security check ? :

Yes, 100% I am sure it would be able to bypass it only & only if it fulfilled the conditions above of the A.I. detection mechanism which is actually pretty easy to achieve.

Press enter or click to view image in full size
The picture I used to bypass the security check and got successfully verified as the user :)
Okay, so what’s the Impact ? :

Any attacker can simply Import the picture of anyone from the gallery and bypass the mandatory step and can watch all the group pictures of users without revealing his/her identity since the A.I. will not be able to find that picture in any group photos because it does not exists only on those group pictures.

Get Ishwar Kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now considering from the use of application point of view a user can import the picture for his or her convenience without actually going through live detection mechanism which is fine from developer’s point of view.

However, the catch seems to be missed by most of the folks out here is the broader attack surface is now enabled for the attackers, what if an attacker breaches the admin credentials and if this same feature of A.I. based detection is Implemented on admin privileges and the admin user itself and all the attacker has to do to is to verify and bypass this step by simply Importing the picture of admin and it will be bypassed without any issues. An attacker can also create a many accounts with same picture and plague the A.I. to map out pictures of certain person which will fill up the profiles and it will become hard to differentiate between the actual and the real user. Attackers can also use anyone’s picture without their permission which is seriously concerning.

Platforms the Test Application is available on ? :

It is available on Android (Play Store) and iOS (App Store). It even has a web version for it but I haven’t tested it. I tested it on Android and it worked. Similar would be followed on iOS too, since the functionality is same.

How did I confirmed it and have I reported it ? :

Yes I have reported it ethically and waiting for the response because it has been days. Upon further discussion of this vulnerability with my mentor Jayesh Sir (X:@Jayesh25_) and he also confirmed that it is actually a valid issue. (It’s always good to have mentors who can guide you to the right path where you feel the uncertainty, much grateful to him) :)

Conclusion:

I hope you liked my article on this interesting bypass of A.I. based facial recognition system. This was an interesting find for me too since it was satisfyingly good to fool the A.I. at its own game. No machines are fool proof.

Source: Internet

Feel free to reach out to me at my twitter: @Ravenzbb , if you got any more questions. I will be coming up time to time with my interesting bypasses and vulnerabilities in various domains, machines and services.

Thank you very much for reading and investing your precious time. :)
