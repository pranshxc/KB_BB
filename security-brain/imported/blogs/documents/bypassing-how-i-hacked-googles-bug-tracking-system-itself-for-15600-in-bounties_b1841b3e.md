---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-17_bypassing-how-i-hacked-googles-bug-tracking-system-itself-for-15600-in-bounties.md
original_filename: 2018-11-17_bypassing-how-i-hacked-googles-bug-tracking-system-itself-for-15600-in-bounties.md
title: Bypassing “How I hacked Google’s bug tracking system itself for $15,600 in
  bounties.”
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- mobile-security
language: en
raw_sha256: b1841b3e439ca06de0136efc2d6c663acba85d690d9237ff7822b132d78c50a8
text_sha256: 2c803be87c8529cc6e7e4d25c8b0d521d09f81c3d654427f03595507b5d8a819
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing “How I hacked Google’s bug tracking system itself for $15,600 in bounties.”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-17_bypassing-how-i-hacked-googles-bug-tracking-system-itself-for-15600-in-bounties.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `b1841b3e439ca06de0136efc2d6c663acba85d690d9237ff7822b132d78c50a8`
- Text SHA256: `2c803be87c8529cc6e7e4d25c8b0d521d09f81c3d654427f03595507b5d8a819`


## Content

---
title: "Bypassing “How I hacked Google’s bug tracking system itself for $15,600 in bounties.”"
page_title: "I bypassed “How I hacked Google’s bug tracking system itself for $15,600 in bounties.” Here’s how. | by Gopal Singh | Medium"
url: "https://medium.com/@gopalsingh/bypassing-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-16134466ab15"
authors: ["Gopal Singh (@gopalsinghcse)"]
programs: ["Google"]
bugs: ["Logic flaw"]
bounty: "3,133.70"
publication_date: "2018-11-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5578
scraped_via: "browseros"
---

# Bypassing “How I hacked Google’s bug tracking system itself for $15,600 in bounties.”

Gopal Singh
 highlighted

I bypassed “How I hacked Google’s bug tracking system itself for $15,600 in bounties.” Here’s how.
Gopal Singh
Follow
4 min read
·
Nov 17, 2018

468

Hello Everyone!

I was reading some write-ups, and I came across this bug which I liked: “Getting a Google employee account.” It was a nice find by 
Alex Birsan
. I started testing the issue tracker, and I was trying to see if I could get a Google account. Then looking around in issue tracker, I noticed in the browse components there were two public issue trackers. So I clicked on Android Public Tracker.

I could see bugs reported to Android there. To report a Bug in the Android public issue tracker, you can send an email to:

buganizer-system+componentID@google.com

where android’s component id is 190923.

I could see that my issue got listed in the public issue tracker. I got a confirmation email from buganizersystem+my_email@google.com. A reply to this email would be directed to:

buganizer-system+componentID+issueID@google.com

I responded to that email, and a comment was posted in the conversation. I could add a Google email to see if I could get a confirmation code. To test this I clicked on Forwarding and POP/IMAP in Gmail settings and added the Google email to the forwarding email address. I was surprised to see I got a confirmation code in the Android public issue tracker.

Get Gopal Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There are two parts here to get a Google account Signup and verification. I could verify a Google account, but I could not signup for an @google.com account, so my report was closed as Won’t Fix. I almost gave up, because after the initial fix I could not use my google.com email. But I decided to give it one last try.

Press enter or click to view image in full size

Then I started visiting every sub-domain of Google to see if I could use a google.com email to signup. This new signup page appeared (see below). Initially, I could not find “Use my current email address instead” to get it to go to https://partnerissuetracker.corp.google.com/. Then you would click on Create an account, and you could see there was an option to use your current email address.

Press enter or click to view image in full size

My heart rate increased after seeing the new signup page. I began to sign up using the buganizer-system+componentID+issueID@google.com email and then it asked me to verify by entering the code.

Verify your email address

I was waiting for the verification code in the conversation, and then I received the verification code in the email and the conversation in the issue tracker.

Press enter or click to view image in full size
Press enter or click to view image in full size

After successfully signing up for the Google Account, I reopened the issue. The impact here was that you can access https://google.ridecell.com which requires a Google account. Besides this, I tried to upgrade my account to Gmail now as I had a Google account. I added it to my Gmail, and I was able to send an email using from buganizer-system+componentID+issueID@google.com

If you try to spoof google.com email, your mail will land in spam. But my email appeared in the inbox, and it was from @google.com so an attacker could pretend that they were a Google employee.

Nice catch!
Press enter or click to view image in full size

It was 9:50 PM when I was looking for bugs, and finally, the most awaited email arrived: I was getting $3133.70. I could not sleep the whole night.

Press enter or click to view image in full size

Check out this video to see more:

Thanks to 
Alex Birsan
 — this would not have been possible without his write-up. I learned a lot from reading his write-up. Also, thanks to 
Avinash Jain
 and 
Alex Birsan
 for taking the time to review the draft.

Thanks for reading!

Gopal Singh
 (https://twitter.com/gopalsinghcse)
