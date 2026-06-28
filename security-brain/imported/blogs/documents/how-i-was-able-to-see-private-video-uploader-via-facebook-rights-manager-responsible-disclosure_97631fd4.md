---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-28_how-i-was-able-to-see-private-video-uploader-via-facebook-rights-managerresponsi.md
original_filename: 2020-05-28_how-i-was-able-to-see-private-video-uploader-via-facebook-rights-managerresponsi.md
title: How I was able to see Private Video Uploader Via Facebook Rights Manager.[Responsible
  Disclosure]
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: 97631fd45cb168efd212caf69150c0f490a0d128abb1806d2e8718df9578e1ec
text_sha256: 5c69f9918f64cbb1c1eecaa1965383341b886c16061c3fd2a4026539be27ed4b
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to see Private Video Uploader Via Facebook Rights Manager.[Responsible Disclosure]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-28_how-i-was-able-to-see-private-video-uploader-via-facebook-rights-managerresponsi.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `97631fd45cb168efd212caf69150c0f490a0d128abb1806d2e8718df9578e1ec`
- Text SHA256: `5c69f9918f64cbb1c1eecaa1965383341b886c16061c3fd2a4026539be27ed4b`


## Content

---
title: "How I was able to see Private Video Uploader Via Facebook Rights Manager.[Responsible Disclosure]"
url: "https://medium.com/@kishoretk/how-i-was-able-to-see-identity-of-a-private-video-up-loader-via-rights-manager-responsible-39d996517b6e"
authors: ["Kishore TK (@kishoretk_off)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2020-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4554
scraped_via: "browseros"
---

# How I was able to see Private Video Uploader Via Facebook Rights Manager.[Responsible Disclosure]

How I was able to see Private Video Uploader Via Facebook Rights Manager.[Responsible Disclosure]
Kishore TK
Follow
3 min read
·
May 28, 2020

230

Hello Everyone! I hope you’re doing great. So, due to the pandemic in India, we all had to stay home and I couldn’t find a better way to kill my boredom. So I decided to write a blog about one of my recent findings.

“This bug is responsibly disclosed to Facebook WhiteHat Team and patched.”

Facebook runs a whitehat program, wherein security researchers across the globe would report their security vulnerabilities to them and according to the severity, they get paid. Sounds, interesting ain’t it? To know more about this click here.

Since I run a media company called The360Groups, I had access to this wonderful tool called Rights Manager by Facebook.

So you might be wondering what’s this rights manager tool all about, which I’ll be demystifying below.

Also, keep in mind this is a privacy issue.

Press enter or click to view image in full size
Source: Rights Manager.

W
hat is Rights Manager?

Rights Manager helps you to:

Easily upload and maintain a reference library of video content to monitor and protect, including live video streams.

Specify permitted uses of each video by setting match rules.

Identify and surface new matches against your protected content so you can review them and file a report if needed.

Whitelist specific Pages and profiles that have permission to use your copyrighted content.

Use the Rights Manager API to integrate existing content management workflows and to easily upload and manage large libraries.

Rights Manager is for publishers that publish content on Facebook and also, those that don’t publish on Facebook, but want to protect their content. If you want to get access to this, click here

Source : Facebook

D
escription

Rights Manager got this option through which you can find matching videos of yours automatically. This is basically to stop copyright infringement, content being pirated, etc.
It works as follows, if your video gets uploaded somewhere you’ll get an alert in your rights manager dashboard. Further, if you want to, you can either add it under whitelist or report it to take it off.

Get Kishore TK’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Interestingly, while I was randomly exploring this option I got to know that it was exposing the uploader’s private account. (Profile ID)

Impact

“Give Permission” option in Rights Manager could expose the identity of a private video uploader.

Reproduction Steps
Upload the video to rights manager that needs to be protected.
Upload the same video from a user’s profile
Now, Rights Manager would detect your video and notify you via matching tab as someone posted your video(whoever uploads your video), Now the give permission tab would appear.
When you give permission, the account gets whitelisted. Now, go to settings of rights manager find the whitelisted person (The profile of the user who uploaded your video will be disclosed)
Right-click on whitelisted name of the profile and copy the link. Now, the link would be something like business.facebook.com/username Remove the “business” alone from the link and paste the link on a new tab (facebook.com/username).
Now we’d be having the uploader’s profile.
Press enter or click to view image in full size

That’s all for today folks! :D

Responsibly Disclosed to Facebook

Reported on 30 April 2020 at 13:10

Not Valid on 2 May 2020 at 03:52

(Found my report open on 16th May 2020)

Impact and more details were given on 16 May 2020 at 12:23

Triaged on 20 May 2020 at 22:11

Fixed on 21 May 2020 at 17:45

Bounty on 28 May 2020 at 16:17

Thanks to:

Rahul Raj, Sriram , Guhan Raja, Hemanth Joseph , Adithyan AK, Vijith Vellora

Special Thanks to:

Madurai360 and Team
