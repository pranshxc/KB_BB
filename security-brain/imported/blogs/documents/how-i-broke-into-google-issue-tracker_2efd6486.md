---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-10_how-i-broke-into-google-issue-tracker.md
original_filename: 2018-04-10_how-i-broke-into-google-issue-tracker.md
title: How I broke into Google Issue Tracker
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: 2efd6486ce750bfa837d073fcc46d77fcc0077297f4cce3f2fd2d2f973bce357
text_sha256: 4b5f926a36aa790dbb8200e51cfafb06767937db07e85eb50615f77bb74d503c
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I broke into Google Issue Tracker

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-10_how-i-broke-into-google-issue-tracker.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `2efd6486ce750bfa837d073fcc46d77fcc0077297f4cce3f2fd2d2f973bce357`
- Text SHA256: `4b5f926a36aa790dbb8200e51cfafb06767937db07e85eb50615f77bb74d503c`


## Content

---
title: "How I broke into Google Issue Tracker"
url: "https://medium.com/bugbountywriteup/how-i-broke-into-google-issue-tracker-667b9e33e931"
authors: ["Abhishek Bundela (@abhibundela)"]
programs: ["Google"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2018-04-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5924
scraped_via: "browseros"
---

# How I broke into Google Issue Tracker

How I broke into Google Issue Tracker
Abhishek Bundela
Follow
3 min read
·
Apr 10, 2018

486

1

Hi friends,

Recently, I published an article where I explained a flaw in google groups functionality. When I submitted that vulnerability to Google I noticed that researchers can comment on the issue in issue tracker by replying to the email from buganizer system.

Press enter or click to view image in full size

After submitting three N/A (won’t fix) report to Google, finally I managed to submit one valid report but unfortunately that was marked as duplicate. Thanks to Google security team, they are very responsive and allowed me to write about the vulnerability.

For learning about Google Issue Tracker’s functionalities, I went through issue tracker’s documentation.

Issue Tracker is a tool used internally at Google to track bugs and feature requests during product development. It is available outside of Google for use by external public and partner users who need to collaborate with Google teams on specific projects.

Users can also create issues by sending an email to buganizer system. You can learn more about it here.

Users are required to send an email to buganizer-system+componentID@google.com for creating an issue.

componentID:It is an integer value of component where you want to report the issue.

If they want to comment on an issue then they have to send an email to buganizer-system+componentID+threadID@google.com.

Get Abhishek Bundela’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

threadID:It is also an integer value for a particular issue.

Press enter or click to view image in full size

You can clearly view in the above image, if you want to create an issue using email then your domain should support SPF & DKIM. I had talked about SPF & DKIM in my previous post. Now, a simple question arises “How does Issue Tracker handle unverified emails ( emails that failed SPF & DKIM verification )”. What if the content from unverified emails directly got posted in Issue tracker ? This means that if an attacker knows the victim’s email address, he can create/comment on an issue on behalf of the victim. So for testing this functionality, I sent an email via smtp2go service and I was astonished by the result. Yes, I can create an issues on behalf of any user in the public issue tracker ! I can also comment on issues just by sending an email to buganizer-system+componentID+threadID@google.com.

I was successful in creating/commenting on issues in public issue tracker, so I thought it might be possible that I can also comment on any issue in the private issue tracker. I sent an email (random email) to one of my issues (via smtp2gto) but the attempt was unsuccessful in creating a comment on that issue. Then, I tried to comment on the issue (via smtp2gto) using my email address ( the same email that is used while reporting the vulnerability ) and I got success.

Impact

An attacker can create/comment on issues using anyone’s email address in public issue tracker. Creating/Commenting issue does not disclose reporter’s email since email’s only first two characters and domain name are visible. You can check this in the attached image.

Press enter or click to view image in full size

Attacker can see those characters & domain name in public issue tracker and can comment on that particular issue using any email that starts with those characters and ends in that particular domain. Attacker can also comment on an issue using random email like abc@googledev.com to fool the public researchers and ask for more details.

While for commenting on private issue tracker, attacker has to know the componentID, threadID and email address located to that ID. Google’s security team consider this as p2 (priority) s2(severity) level.

POC

Thanks for your patience.

Learn, Build & Break!
