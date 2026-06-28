---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-29_how-i-got-a-bug-at-apple-that-leads-to-takeover-accounts-of-any-user-who-view-my.md
original_filename: 2022-12-29_how-i-got-a-bug-at-apple-that-leads-to-takeover-accounts-of-any-user-who-view-my.md
title: How I got a Bug At Apple that lead’s to takeover accounts of any user who view
  my profile
category: documents
detected_topics:
- idor
- xss
- command-injection
- rate-limit
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- rate-limit
- api-security
- cloud-security
language: en
raw_sha256: bfb6236b265bd73d827e630425ace2c63b37815aed36fac83663ac1bbb285c67
text_sha256: 32af3631ed9a98dbd9b1c28fd65b98703841814e20f67f08bd0965e78a861b22
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How I got a Bug At Apple that lead’s to takeover accounts of any user who view my profile

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-29_how-i-got-a-bug-at-apple-that-leads-to-takeover-accounts-of-any-user-who-view-my.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, rate-limit, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `bfb6236b265bd73d827e630425ace2c63b37815aed36fac83663ac1bbb285c67`
- Text SHA256: `32af3631ed9a98dbd9b1c28fd65b98703841814e20f67f08bd0965e78a861b22`


## Content

---
title: "How I got a Bug At Apple that lead’s to takeover accounts of any user who view my profile"
url: "https://hamzadzworm.medium.com/how-i-got-a-bug-that-leads-to-takeover-accounts-of-any-user-who-view-my-profile-913c8704f6cd"
authors: ["Abdelkader Mouaz (@hamzadzworm)"]
programs: ["Apple"]
bugs: ["XSS", "Account takeover"]
publication_date: "2022-12-29"
added_date: "2022-12-30"
source: "pentester.land/writeups.json"
original_index: 1720
scraped_via: "browseros"
---

# How I got a Bug At Apple that lead’s to takeover accounts of any user who view my profile

Top highlight

How I got a Bug At Apple that lead’s to takeover accounts of any user who view my profile
Hamzadzworm
Follow
3 min read
·
Dec 29, 2022

205

3

Hi Team Iam Abdelkader Mouaz my pseudo is Hamzadzworm today i will share with you a Bug That Lead To Takeover account of any user just if he view my profile

I Was Hunting On Apple For Few Days, I Try to Do Subdomain Enumeration Using Multipe Tools To Get All possible Subdomains I Was Able To get About 20K Live Subdomain it Was A Big list but I had A lot Of time I keeped Testing Them One By One

I found an interesting One It Was A community Subdomain That You Can Log in into It With Your I Cloud Account so i was thinking That If I get An Account Takeover There I Will Be Able To Takeover Icloud Accounts

i keep searching For Few Days Untile I got An Interesting Endpoint It Was Location One where Iam Able To put Location On My Profile But I Couldn’t Do That Manually

Location Adresss eWere Added Automatically By Putting Adresse And it was picking this Automatique Locations From Apple Maps thats an exemple For It

maps.apple.com/?&q=Test&address=Test

it was redirecting me to google maps with an input Test/Test

Press enter or click to view image in full size

it was an interesting thing so i go to add a new map thats non listed in google map then share it using the endpoint i found:

Get Hamzadzworm’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

maps.apple.com/?&q=Test&address=Test

Press enter or click to view image in full size

after i was able to add the map i put a blind xss payload in google place name then sent it and it was accepted it wasnt executed in google for sure

but after i link it with maps.apple.com becasue apple maps taking map from google map i was able to make a finall payload and add it in my profile location and

it Was At (Lieu) which mean Location As You See in the Screen Bellow

Press enter or click to view image in full size

And Yey Its Executed

Press enter or click to view image in full size

Then I Added A Blind Xss Payload At Map And Opened New Account And Try To View My Profile That Contain Blind Xss And Its Fired And I got cookies Of Account At My Xss Hunter Account Which Allowed Me To Takeover The Account

I Hope You Enjoyed The Write Up Let A Comment For Me If you Liked it -.- :)
