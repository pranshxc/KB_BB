---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-24_how-i-was-able-to-delete-any-image-in-facebook-community-question-forum.md
original_filename: 2018-02-24_how-i-was-able-to-delete-any-image-in-facebook-community-question-forum.md
title: How I was able to delete any image in Facebook community question forum
category: documents
detected_topics:
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: 153c027bc647e63545837b11e651536d8854ae00ac43e43a3939bb2175bd22a5
text_sha256: 9d88f5bf43e8c5c8ca763d23acc194b08a1fe3e14dda73353b9e0bd0d7ad3e2e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to delete any image in Facebook community question forum

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-24_how-i-was-able-to-delete-any-image-in-facebook-community-question-forum.md
- Source Type: markdown
- Detected Topics: idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `153c027bc647e63545837b11e651536d8854ae00ac43e43a3939bb2175bd22a5`
- Text SHA256: `9d88f5bf43e8c5c8ca763d23acc194b08a1fe3e14dda73353b9e0bd0d7ad3e2e`


## Content

---
title: "How I was able to delete any image in Facebook community question forum"
url: "https://medium.com/@JubaBaghdad/how-i-was-able-to-delete-any-image-in-facebook-community-question-forum-a03ea516e327"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "1,500"
publication_date: "2018-02-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5964
scraped_via: "browseros"
---

# How I was able to delete any image in Facebook community question forum

How I was able to delete any image in Facebook community question forum
Sarmad Hassan (Juba Baghdad)
Follow
5 min read
·
Feb 24, 2018

805

10

Press enter or click to view image in full size

Hello guys, my name is Sarmad Hassan known as (Juba Baghdad), I’m a bug hunter from Iraq, it’s my first write up about bug bounty programs. Today, I want to share with you my last bug that I found in Facebook community question forum.

After I got some HOF’s in many programs like Google, Apple, Mozilla, Sony ...etc, I decided to participate in Facebook bug bounty program and give it a try :)

I submitted about 10 reports to Facebook Sec. team since April 2017 and all of them closed as N/A (Not Applicable) which made me frustrated, so I said to my self I’ll never submit any report till I find a serious valid one, so I started digging deeper, and while checking facebook domains I came across community question forum so I clicked on the below link :

https://www.facebook.com/help/community/question/?id=10155342339873049&rdrhc

I posted an answer with attached photo and intercepted it with Burpsuite, to see what is going on, the request was as below:

POST /help/community/async/post_answer/?view=top&question_id=10155342339873049&helpCommunityPath=%2Fbusiness%2Fhelp%2Fcommunity%2F&dpr=1 HTTP/1.1
Host: www.facebook.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://www.facebook.com/business/help/community/question/?id=10155342339873049
Content-Type: application/x-www-form-urlencoded
Content-Length: 404
Cookie: fr=xxx; datr=xxx; sb=xxx; wd=1366x625; c_user=100015771374169; xs=xxx; pl=n; act=xxx; presence=xxx
Connection: close

fb_dtsg=xxx&answer=test&attachment=%7B%22fbid%22%3A275252333010477%7D&view=top&__user=100015771374169&__a=1&__dyn=xxx&__req=h&__be=1&__pc=PHASED%3ADEFAULT&__rev=3671169&jazoest=xxx&__spin_r=3671169&__spin_b=trunk&__spin_t=1519420965

So what brought my attention in the above request is the (attachment=) parameter which is responsible for the photo that uploaded by the user from his machine :

attachment={“fbid”:275252333010477}

fbid = is the id of any uploaded photo in facebook

I said what if I change my “fbid” number with other user’s “fbid” attached photo :), so I directly opened my test account (Sadiq Hamed_as an attacker) and post an answer and intercept with burpsuite and replaced the “fbid” number of the test account (Sadiq Hamed_as an attacker) with the fbid of my real account (Sarmad Hassan_as a victim) and boo000oooom, the answer posted successfully with the same attached photo :)

Press enter or click to view image in full size
Victim account posted an answer with attached photo
Attacker account posted an answer with the same “fbid” of victim’s attached photo

and I was like oh!! I smell IDOR here:

after that I said if I delete the posted answer in (Sadiq Hamed_as an attacker) account, I think the attached photo of (Sarmad Hassan_as a victim) will be deleted too, because both of them (Attacker and Victim ) have the same “fbid” number, so I deleted posted answer from attacker account and refreshed the victim account page but nothing happened, the photo was still there :(

Press enter or click to view image in full size
photo of victim still there after refreshing the page

and I was like

so I said maybe it will take some time to be deleted in Victim account, so I refreshed multiple times in both accounts (Attacker and Victim) for more than one minute and checked the Victim account again whether the photo deleted or not and the result was as below:

Press enter or click to view image in full size
photo of victim’s account deleted by the attacker

booooooom :)

I didn’t stop there, I said let’s dig deeper and deeper to see what I could do with this bug and I found out that it’s also works on any photo uploaded by Facebook help team itself and also it works on Facebook workplace as well.

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But I faced a little problem regarding the “fbid” number for other users account that don’t belong to me, I asked my friend Max Pasqua for help, and he told me that when he was trying to find some bugs in facebook in the past, he noticed that there is a relationship in the image URL link between “second number” in the image URL link and a constant number equal to {3333333}

below is the explanation of getting “fbid” through Image URL only :

1- First You need to get the image link
for example the below link image

https://scontent.febl3-1.fna.fbcdn.net/v/t39.2229-6/20406039_500237376979766_6048207520713932800_n.jpg?oh=247e74133ad7cdde4cb9da0996ca345b&oe=5B05ACC9

2- then you get this part of the URL

20406039_500237376979766_6048207520713932800_n.jpg?oh=247e74133ad7cdde4cb9da0996ca345b&oe=5B05ACC9

3- then you get the second number set between the underscore so it would be this (500237376979766)

4- you need to go into a calculator and subtract (263936780808699) from (3333333) which the last number (3333333) is a constant number

5- the final formula will be as below

fbid = 500237376979766–3333333 ==> 500237373646433

so the fbid for the above image link will be ==> 500237373646433

Special thanks for Max Pasqua for his awesome method

Conclusion Impact of the bug:

A) In https://www.facebook.com/help/community, the attacker is able to :

1- Delete any attached Photo that uploaded by facebook help team.

2- Delete any attached Photo in any user question.

3- Delete any attached Photo in any user answer.

B) In work place domain https://workplace.facebook.com/help/work/community, the attacker is able to :

1- Delete any attached Photo that uploaded by facebook help team.

2- Delete any attached Photo in any user question.

3- Delete any attached Photo in any user answer.

Timeline:
Jan. 27, 2018 — Initial Report
Feb. 07, 2018 — Report Triaged
Feb. 13, 2018 — Fixed By Facebook
Feb. 19, 2018 —Fixed Confirmed
Feb. 23, 2018 —Bounty of $1,500 awarded

PoC Video: in facebook workplace

Takeways:

1- Never give up.

2- Try to understand the web app. and it’s parameters, and put it in your notes.

3- When there is images in the web app. always focus on image’s id parameters cause there is a chance to get IDOR out there.

4- Manipulate, Manipulate and Manipulate with parameters.

5- Burpsuite is your best friend and try to intercept everything, don’t be lazy :)

6- If you didn’t find any bug, try another day and keep digging till you find valid one, trust me it is only a matter of time.

Thank you

Sarmad Hassan (JubaBaghdad)
