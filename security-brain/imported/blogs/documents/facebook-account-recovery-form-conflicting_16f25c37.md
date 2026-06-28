---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-13_facebook-account-recovery-form-conflicting_2.md
original_filename: 2017-02-13_facebook-account-recovery-form-conflicting_2.md
title: Facebook Account Recovery Form (CONFLICTING)
category: documents
detected_topics:
- password-reset
- xss
- command-injection
- business-logic
tags:
- imported
- documents
- password-reset
- xss
- command-injection
- business-logic
language: en
raw_sha256: 16f25c370a1987b49039c5de7665876f986cf2cd410de549815fe205d30e8c69
text_sha256: 1fd72db2b4136d5177be7826ea7eed32ef7b6e1ba4d70507a2c695542bb9ed7d
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Account Recovery Form (CONFLICTING)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-13_facebook-account-recovery-form-conflicting_2.md
- Source Type: markdown
- Detected Topics: password-reset, xss, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `16f25c370a1987b49039c5de7665876f986cf2cd410de549815fe205d30e8c69`
- Text SHA256: `1fd72db2b4136d5177be7826ea7eed32ef7b6e1ba4d70507a2c695542bb9ed7d`


## Content

---
title: "Facebook Account Recovery Form (CONFLICTING)"
url: "https://medium.com/@zahidali_93675/conflict-account-recovery-form-in-facebook-2b6e7d203cfd"
authors: ["Zahid Ali"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "1,000"
publication_date: "2017-02-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6226
scraped_via: "browseros"
---

# Facebook Account Recovery Form (CONFLICTING)

Zahid Ali
Follow
4 min read
·
Feb 13, 2017

15

1

F
acebook Account Recovery Form (CONFLICTING)

I started my bug hunting journey in may 2015. I already published my
writeups before about bugs i found in Facebook. This is my first bug i
found in Facebook in may 2015.
I heard about bug bounty Programs that how these companies inviting
hackers to see bugs inside their system and they are paying them
bounties for that.
So i decided to test social media giant “FACEBOOK” first to see whats
happening inside facebook. I watched couple of videos uploaded by bug
hunters and their writeups. But frankly it is very hard to understand
how and where to start first.
Before hunting bugs i always check password recovery area’s for
different account :D so i decided to check these area’s and searching
account recovery forms. I got one so i tested for “XSS” but failed. I
tried to ask google and got so many links where people discussed that
it is very difficult to find “xSS” in Facebook. So i just forgot about
the “XSS” and tried to find something else.
After a few tests i figured it out that form is conflicting.

Description and Impact:
If “Attacker” submit a form for specific id and if “Victim” do the
same then first form submitted by “Attacker” will remove from Facebook
Dashboard and “Victim’s” Submitted Form will appear in the dashboard.
But in the email attacker will get a link of victim’s form and with
the help of that link “Attacker” was able to see the conversation
between “Victim” and Facebook Admin.

Reproduction steps:

Go to https://m.facebook.com
Click on “Forgot Password”
Enter Phone number or Facebook Username of Victim
Click — ->>> (No longer have access to these?)
Enter Recovery email twice
Fill up the form with fake info and submit.

Screen shots of Reproduction steps of form submitting by (Attacker):

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

“Also Getting reply in Email”

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Now form was successfuly submitted by attacker.

Get Zahid Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

=======================================

Screen Shots of victim submitting Form:

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Victim successfuly submitted form

=======================================

Attacker’s form deleted from support dashboard:

Press enter or click to view image in full size

Now Attacker is getting reply in the email of victim’s form (Conversation between Admin and Victim):

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

That’s it :)

Facebook award me 1000USD for that bug and that was my first bounty i got from facebook in june 2015.

Press enter or click to view image in full size

:)
