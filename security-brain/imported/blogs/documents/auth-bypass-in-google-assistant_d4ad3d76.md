---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-10_auth-bypass-in-google-assistant.md
original_filename: 2021-10-10_auth-bypass-in-google-assistant.md
title: Auth Bypass in Google Assistant
category: documents
detected_topics:
- automation-abuse
- command-injection
- mobile-security
tags:
- imported
- documents
- automation-abuse
- command-injection
- mobile-security
language: en
raw_sha256: d4ad3d760830e09ccf7336c42fbf15a67f084c1eab068e7b007075b8108a2e7b
text_sha256: c61fe24e28c2768f6bda194a65df4262bd22e87e8d74a373cc7c50dd33b173bb
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Auth Bypass in Google Assistant

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-10_auth-bypass-in-google-assistant.md
- Source Type: markdown
- Detected Topics: automation-abuse, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `d4ad3d760830e09ccf7336c42fbf15a67f084c1eab068e7b007075b8108a2e7b`
- Text SHA256: `c61fe24e28c2768f6bda194a65df4262bd22e87e8d74a373cc7c50dd33b173bb`


## Content

---
title: "Auth Bypass in Google Assistant"
page_title: "[#0011] Malicious webpage can execute Google Assistant commands without any permissions | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0011"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0011"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Insecure deeplink"]
bounty: "8,133.70"
publication_date: "2021-10-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3253
---

#0011  
Vendor: Google  
Status: fixed  
Reported: Nov 25, 2019  
Disclosed: Oct 10, 2021 (685 days) 

# Malicious webpage can execute Google Assistant commands without any permissions

Summary: Webpage can execute Google Assistant commands without any permissions

Steps to reproduce:

  1. Generate the TTS audio files using the Google Cloud TTS API, using the text commands in the JavaScript comments
  2. Make sure the device is not muted, or have headphones connected
  3. Open the POC HTML on an Android device with Google Assistant
  4. Click one of the POC attacks
  5. See the Google Assistant commands execute automatically, without any permissions

This attack works by first triggering Google Assistant using a deeplink (acquired from the mobile “google.com” page, where there is a button to trigger the Assistant) and after a bit of delay, playing TTS generated commands as plain audio.

This attack can be exploited the same way (or sending a “VOICE_COMMAND” intent) by Android applications (without any permissions required), actually that was my first idea, but I figured that the impact is way higher if a victim only has to visit a webpage to get the same results.

One weird thing I noticed while testing using the Chrome browser on Android, is that an audio file is played differently depending on the length. This forced me to split the attacking commands into different audio files (for example the “share location” and the phone number are different commands), since when I tried to play the longer audio file, Chrome interpreted it as a “media”, and displayed the media control notification as well. And triggering Assistant while a longer audio “media” was playing, caused Assistant to pause the audio. When using shorter audio files, the media control notification did not appear, and Assistant didn’t pause the media, allowing it to execute the malicious commands.

I used the Cloud Text-to-Speech API to generate the audio files. I used language_code=’en-US’ and name=”en-US-Wavenet-A” to generate the audio files. All of the text input used to generate the audio files can be found in the JavaScript comments.

I attached 2 POC videos to make it easier to see the attack running:

Single command POC Video: https://youtu.be/T3CgECvV-qM

Multiple command / Confirmation POC Video: [redacted]

— POC HTML —
  
  
  <html>
  
  <body>
  
  <h1>
  <a onclick="share()" href="googleapp://deeplink/?data=CkwBDb3mGzBFAiEAic8-0un3nRrMa_hkMUV9fj_zD09xhu9D6xTXEsFSRPICIEJlWlJRSqv3afrbX9J8BZa_h3sAfF8NSDFAlLSj10MUEjkKAggAEgIIbxoQEg4IBBIK6oqo9AQECAFAACIdChtodHRwOi8vYXNzaXN0YW50Lmdvb2dsZS5jb20">
  share location</a>
  </h1>
  
  <h1>
  <a onclick="opendoor()" href="googleapp://deeplink/?data=CkwBDb3mGzBFAiEAic8-0un3nRrMa_hkMUV9fj_zD09xhu9D6xTXEsFSRPICIEJlWlJRSqv3afrbX9J8BZa_h3sAfF8NSDFAlLSj10MUEjkKAggAEgIIbxoQEg4IBBIK6oqo9AQECAFAACIdChtodHRwOi8vYXNzaXN0YW50Lmdvb2dsZS5jb20">open
  front door</a>
  </h1>
  
  <script>
  // language_code='en-US'
  // name="en-US-Wavenet-A"
  
  function share() {
  setTimeout(function() {
  
  var audio = new Audio('share1.mp3'); // "share my location with"
  audio.play();
  
  setTimeout(function() {
  
  var audio = new Audio('share2.mp3'); // "[redacted]" [PHONE NUMBER TO SEND SMS TO]
  audio.play();
  
  setTimeout(function() {
  var audio = new Audio('confirm.mp3'); // "send it"
  audio.play();
  }, 12000);
  
  }, 6000);
  
  }, 500);
  }
  
  function opendoor() {
  setTimeout(function() {
  
  var audio = new Audio('open.mp3'); // "open the front door"
  audio.play();
  
  }, 500);
  }
  </script>
  
  </body>
  
  </html>
  

— END POC HTML —

Attack scenario: This attack allows an attacker to execute malicious commands in Google Assistant, on behalf of the victim, just by making the victim visit a webpage. The Assistant has access to extremely sensitive information, and may be able to control the victim’s Google Account, Smart Home, and other IOT appliances. An attacker should never be able to execute commands in Google Assistant, without having sufficient permissions.

Limitation of this attack:

  * The phone must not be muted or have headphones connected, since Google Assistant wouldn’t hear the malicious audio
  * The malicious commands could be heard by the user, since they are playing out loud
  * The attack will fail if the user closes the Assistant mid-attack

Why I checked “Is this vulnerability public or known to third parties?”: I found out about this issue (only the idea of playing the commands as audio, using the phone) by browsing forums where people were talking about finding ways to execute Assistant commands to automate their different workflows. This method was posted publicly as an “Automate” (Android automating app) “flow” to execute an Assistant command. Their motivations wasn’t malicious, but I realized that this method could be abused by an attacker, and made it into a POC. Therefore, I mark this vulnerability as public, since anyone can find this information and use it for malicious purposes.

* * *

### Comments:

**Vendor - 2019-11-25 10:17**

** NOTE: This e-mail has been generated automatically. **

Thanks for your report.

This email confirms we’ve received your message. We’ll investigate and get back to you once we’ve got an update. In the meantime, you might want to take a look at the list of frequently asked questions about Google VRP at https://sites.google.com/site/bughunteruniversity/behind-the-scenes/faq.

If you are reporting a security vulnerability and wish to appear in Google Security Hall of Fame, please create a profile at https://bughunter.withgoogle.com/new_profile.

You appear automatically in our Honorable Mentions if we decide to file a security vulnerability based on your report, and you will also show up in our Hall of Fame if we issue a reward.

**Note that if you did not report a vulnerability, or a technical security problem in one of our products, we won’t be able to act on your report. This channel is not the right one if you wish to resolve a problem with your account, report non-security bugs, or suggest a new feature in our product.**

Cheers, Google Security Bot

Follow us on Twitter! https://twitter.com/googlevrp

* * *

**Me - 2019-11-25 10:26**

One possible fix for this could be to disable _any_ playing audio on the device when the Assistant is listening for commands.

* * *

**Vendor - 2019-11-25 13:29**

** NOTE: This e-mail has been generated automatically. **

Hey,

Just letting you know that your report was triaged and we’re currently looking into it.

You should receive a response in a couple of days, but it might take up to a week if we’re particularly busy. In the meantime, you might want to take a look at the list of frequently asked questions about Google VRP at https://sites.google.com/site/bughunteruniversity/behind-the-scenes/faq.

Thanks, Google Security Bot

* * *

**Me - 2019-11-26 16:52**

One more thing to add is that if a Android application is using the same method to issue malicious Assistant commands, it could bypass one or more of the above mentioned limitations that a website is unable to:

  * The muted phone, by playing the audio as an alarm so it plays even when the phone is set to silent
  * The need for not having any headphones plugged in / connected, by playing the audio as an alarm, because in my limited research that seems to play on both the headphones and on the speaker, or by routing the audio using the setSpeakerphoneOn(true) method.

These should not require any/dangerous permissions.

Thanks, David

* * *

**Vendor - 2019-12-02 16:28**

Hi,

Nice catch! I’ve filed a bug based on your report.

All you need to do now is wait. If you don’t hear back from us in 2-3 weeks or have additional information about the vulnerability, let us know!

Regards,

Google Trust and Safety

* * *

**Me - 2019-12-18 00:20**

** NOTE: This is an automatically generated email **

Hello,

Thank you for reporting this bug. As part of Google’s Vulnerability Reward Program, the panel has decided to issue a reward of $500.00.

Important: if you aren’t registered with Google as a supplier, p2p-vrp@google.com will reach out to you. If you have registered in the past, no need to do it again - sit back and relax, and we will process the payment soon.

If you have any payment related requests, please direct them to p2p-vrp@google.com. Please remember to include the subject of this email and the email address that the report was sent from. Regards,

Google Security Bot

If you’d like your name added to our Hall of Fame:
  
  
  https://bughunter.withgoogle.com/
  

Just create a profile here: https://bughunter.withgoogle.com/new_profile

In addition, we encourage you to signup for our Vulnerability Research Grants program, where we issue monetary payments to VRP researchers, even when no vulnerabilities are found. To read more about the program visit: https://www.google.com/about/appsecurity/research-grants/

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Vendor - 2020-01-07 16:41**

Hey David,

We were reviewing past VRP reports for our end of the year review and it came to our attention that your report was not correctly assessed, when it was previously reviewed in our reward panel.

I have sent your report back for a second review and you should be receiving an updated reward decision next week.

Regards, [redacted], Google Trust & Safety

* * *

**Vendor - 2020-01-17 00:20**

** NOTE: This is an automatically generated email **

Hello,

Thank you for reporting this bug. As part of Google’s Vulnerability Reward Program, the panel has decided to issue a reward of $4500.00.

Important: if you aren’t registered with Google as a supplier, p2p-vrp@google.com will reach out to you. If you have registered in the past, no need to do it again - sit back and relax, and we will process the payment soon.

If you have any payment related requests, please direct them to p2p-vrp@google.com. Please remember to include the subject of this email and the email address that the report was sent from. Regards,

Google Security Bot

If you’d like your name added to our Hall of Fame:
  
  
  https://bughunter.withgoogle.com/
  

Just create a profile here: https://bughunter.withgoogle.com/new_profile

In addition, we encourage you to signup for our Vulnerability Research Grants program, where we issue monetary payments to VRP researchers, even when no vulnerabilities are found. To read more about the program visit: https://www.google.com/about/appsecurity/research-grants/

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Me - 2020-04-19 20:40**

Hi!

I have plans around potentially disclosing this issue in a talk at a security conference in October 2020. I am writing this to ask about the status of this issue and to request permission to disclose this issue when it will become fully fixed.

Would the disclosure time of October 2020 be possible?

Thank you, David

* * *

**Vendor - 2020-04-30 16:07**

Hi David,

Disclosure around October 2020 should be fine.

Best of luck with preparing with your talk and if you would like us to review any of your presentation for feedback, please let us know!

Regards, [redacted], Google Trust & Safety

* * *

**Vendor - 2020-12-11 11:09**

Hi David,

Per our email discussion, sending you a note just as an FYI: We classified this report as an abuse risk.

Best of luck in your future research,

[redacted]

* * *

**Me - 2021-02-25 09:04**

Hi,

Can I ask what the fix was here? My POC broke, looks like that link which triggered Assistant is now disabled. But, I can still play malicious audio to Assistant, if it was triggered manually.

Is only the “programatic triggering” that was removed? If so, if I find any other way to auto-trigger Assistant, is that considered a new bug?

Thank you, David

* * *

**Me - 2021-03-03 10:17**

Hi David,

I’m not sure if I fully understand your question - so please let me know if I missed anything.

In your initial report, you were able to execute Google Assistant commands automatically, without any user permissions. The root cause that led to this particular issue has been fixed now. Of course, if you are able to identify a different way to auto-trigger Assistant we would be really curious to hear about.

Let me know if you have any other questions!

Best, [redacted]

* * *

**Vendor - 2021-04-28 10:42**

The status of this report is being changed so that our automation will notify you when the underlying bug is fixed. There isn’t any action needed on your part here, just a book-keeping change. Apologies for the extra noise/email.

* * *

**Me - 2021-03-14 18:25**

Hi,

Good news (for me, at least), the deeplink is back! It looks to have some extra protection, and sometimes it’s glitching all over the place, but I was able to bypass it if the user has some music playing:

https://youtu.be/phIgnbaGDHo

Thank you, David

* * *

**Me - 2021-03-14 18:35**

Some extra info, if teams would be confused about the origin of this deeplink:

This link is used on google.com, when visited with an (android?) User Agent. \

When the bug got fixed initially, this button also became unusable (but it was still there), but few days ago I pressed it, and it was working again, hence I tried the POC. And now it works again, with the same exact deeplink the original POC had in 2019.

I attached a picture of what it looks like.

* * *

**Vendor - 2021-03-18 13:17**

Hi David,

Great job (as always) - thank you for pointing that out! I’ve reached out to the product team with all the info you’ve shared to make them aware of this.

We will keep you posted as we learn more!

Thanks! [redacted]

* * *

**Vendor - 2021-06-08 14:49**

Hi David,

Was your latest test on an actual phone or an emulation? Can you provide us the phone model you used to test this?

* * *

**Me - 2021-06-08 19:05**

Hi,

I used a real device, a Pixel 5 with the latest Google app.

Thank you, David

* * *

**Vendor - 2021-06-08 19:58**

Thanks David.

* * *

**Me - 2021-07-11 07:47**

Hi,

Is there any update on this issue? When is the fix expected?

Thank you, David

* * *

**Vendor - 2021-07-13 08:59**

Hi David,

I don’t have any updates on the timeline of the fix yet. Having said that, I can confirm that the team is working on the fix and that your report was sent to the VRP Panel. We had some difficulties to reproduce this issue but you should get an update on your reward later today.

Best, [redacted]

* * *

**Vendor - 2021-07-13 15:20**

** NOTE: This is an automatically generated email **

Hello,

Regarding our Vulnerability Reward Program: The VRP panel has decided to issue a reward of $3133.70 for your report. Congratulations!

Important: If you aren’t already registered with Google as a supplier, p2p-vrp@google.com will reach out to you. If you have registered in the past, no need to repeat the process – you can sit back and relax, and we will process the payment soon.

Note: This month, we are changing our payment processing backend. There might be small delays (a few weeks) with how the payments are processed. Thanks for understanding, and sorry for the trouble!

If you have any payment related requests, please direct them to p2p-vrp@google.com. Please remember to include the subject of this email and the email address that the report was sent from.

Regards,

Google Security Bot

P.S. Two other things we’d like to mention:

  * If you’d like us to add your name to our Hall of Fame at https://bughunter.withgoogle.com/rank/hof, please create a profile at https://bughunter.withgoogle.com/new_profile if you haven’t already done so.
  * We encourage you to sign up for our Vulnerability Research Grants program at https://www.google.com/about/appsecurity/research-grants/, where we issue monetary payments to VRP researchers, even when no vulnerabilities are found.

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Me - 2021-08-11 13:07**

Hi,

It looks like to me that if the Assistant is opened with deeplink, it requires a manual press on the mic icon to start listening. This seems to fix the issue.

Can you please confirm this? Did the product team implement this as a fix?

**[Disclosure Warning!]**  
I plan to disclose this bug at a security conference in October, and in an internal company-wide talk **on Friday**.

Please let me know if I should delay disclosure.

Thank you,  
David

* * *

**Me - 2021-08-13 07:36**

[redacted] confirmed that the product team has indeed pushed a fix. I’ll disclose the issue today.

* * *

**Vendor - 2021-08-08 16:19**

Thanks for letting us know David :)
