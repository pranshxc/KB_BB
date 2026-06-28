---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-12_add-description-to-instagram-posts-on-behalf-of-other-users-6500.md
original_filename: 2018-10-12_add-description-to-instagram-posts-on-behalf-of-other-users-6500.md
title: Add description to Instagram Posts on behalf of other users - 6500$
category: blogs
detected_topics:
- mfa
- idor
- command-injection
- api-security
tags:
- imported
- blogs
- mfa
- idor
- command-injection
- api-security
language: en
raw_sha256: 6ecea43c539665216d4107b09d26b71df592b163bbf74ef5bc25b5ff9aef89c1
text_sha256: 835e293eeb96011a22c217f391875f316a9a6fbfa40eeca6a4926e5b512d3ef3
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Add description to Instagram Posts on behalf of other users - 6500$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-12_add-description-to-instagram-posts-on-behalf-of-other-users-6500.md
- Source Type: markdown
- Detected Topics: mfa, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `6ecea43c539665216d4107b09d26b71df592b163bbf74ef5bc25b5ff9aef89c1`
- Text SHA256: `835e293eeb96011a22c217f391875f316a9a6fbfa40eeca6a4926e5b512d3ef3`


## Content

---
title: "Add description to Instagram Posts on behalf of other users - 6500$"
url: "https://medium.com/bugbountywriteup/add-description-to-instagram-posts-on-behalf-of-other-users-6500-7d55b4a24c5a"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "6,500"
publication_date: "2018-10-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5647
scraped_via: "browseros"
---

# Add description to Instagram Posts on behalf of other users - 6500$

Add description to Instagram Posts on behalf of other users - 6500$
Sarmad Hassan (Juba Baghdad)
Follow
5 min read
·
Oct 12, 2018

775

4

Press enter or click to view image in full size

Hello folks, it’s JubaBaghdad again, today I would like to share with you an interesting bug that I found in Instagram that make me able to add description to other users Posts, are you ready !! :)

The Story of finding

In 6-August-2018 an idea came to my mind, I wanted to bypass two-factor authentication (2fa) of Instagram from Facebook page, because there is an option on Facebook page that allowed you to Manage Instagram, for more details see this link.

I switched to my Facebook Test Page and clicked on Instagram tab and tried to login using my old Instagram account, but I couldn’t log in because I forgot my password as usual :)

Press enter or click to view image in full size
You can Manage your Instagram account from your Facebook page

After that I opened Instagram from my web browser to see if my account is still exist or not and I saw this :

Press enter or click to view image in full size
This is how Instagram looks like when you open it from web browser

If you look at the above image maybe you will not notice any interesting thing, but for me it was really interesting !! Why !! Because I already Tested Instagram web app. before and I have that habit which is memorizing options and features so I can quickly notice any new feature, Look again at the image above and you will see there is an interesting option called IGTV.

What is IGTV:

IGTV, is a new feature for watching long-form, vertical video from your favorite Instagram creators, for more details see this link.

I read a lot about this feature from Instagram Info Center, and decided to test it :)

So I created an IGTV video, once I created it I clicked on the edit option and Intercepted the request with burpsuite to see what kind of parameters inside this feature and I saw this :

POST /media/1887820989027383407/edit/

caption=test&publish_mode=igtv&title=test

OK let’s analyze the above request and see what we have in our hands:

1- media id = 1887820989027383407 ===> is the ID of my IGTV video, I searched about media ID and noticed that Instagram refers to any post (photo, video and IGTV video) with media ID and I can get any media ID for other users posts by just visiting their posts and viewing the source code:

Press enter or click to view image in full size
You can get any post’s media ID from the source code

2- Another way to get media ID, by just visiting the user post, hit like and intercepting the request with burpsuite ( I used it in my PoC video).

3- The parameters (caption & title)

when you create any photo or video in Instagram the web app ask you to put description to that photo or video (it’s optional you can leave it blank like millions of users do :) ), In IGTV, caption refers to Description too.

Cool, we got all the information that we want, what next!!

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you noticed the above request we have media ID, so as a bug hunters of course we will try to trick Instagram server and change that media ID to another User media ID and see, Can we trick the system and add description to other Users posts on behalf of them !!??

Testing stage

while testing this on my another test account, I noticed below things:

I can add description to other users posts (By replacing my media ID with their post’s media ID), if they didn’t put any description to their posts.
It works in all kind of Posts like photos, videos and IGTV videos.
It works only on public accounts.
The most weird thing, the response gave me an Internal Server error with an error message “Oops an error occurred” , but instead the bug works like a charm, you will see that in my PoC video below.
Why this bug is so Dangerous
A lot of users (Millions of accounts) on Instagram set their profile to public .
If we search on any public account, we can find at least one post that have no description which make the bug works in almost millions of accounts.
If this bug was in a bad hands (Black hat), he can target the most-followed_Instagram_accounts see this link.
Most Instagram Users including Celebrities are vulnerable to this bug, because they used to make posts without adding description, for example:

Mark zuckerberg ===> 4.6 Millions Followers ==> see his post

Selena Gomez ===> 140 Millions Followers ===> see her post

Ariana Grande ====> 125 Millions Followers ==> see her post

Beyoncé =====> 117 Millions Followers ====> see her post

Kim Kardashian ===> 115 Millions Followers ==> see her post

Lionel Messi :)====> 97 Millions Followers ===> see his post

The list is so long :), so Imagine High bug like this in a bad hands, it could be leading to a big media hype by targeting celebrities as an example, or create big problems between giant companies like apple and its competitor Samsung :) and so on.

I reported this bug directly to Facebook Security Team and they fixed it within one day only, the fix was so fast because of bug severity, they also rewarded me an awesome bounty 6500$

I would like to thanks Facebook Security Team for this awesome Bounty.

Also I would like to Thanks My friend Kassem Bazzoun for his huge support and helping me with this bug. Thanks a million bro. :)

Timeline:
August. 06, 2018 — Initial Report
August. 14, 2018 — Report Triaged
August. 15, 2018 — Bug Fixed
August. 15, 2018 — Fix Confirmed
October. 10, 2018–6500$ Bounty awarded

PoC Video:

Takeways:

Don’t depends on the response only, sometimes it gives you an error, but instead your bug will work, I learned that when I saw a video couple months ago of my friend Abdellah Yaala see his video at the minute 1:22, so you have to check what you’re testing from the web app. too.
Try to check your target from time to time and to check if there is any new option or feature (when there is a new feature there is a new bug).
Try to memorize your target options, it will make you identify any new option quickly just like I did :).

Thank you

Sarmad Hassan (JubaBaghdad)
