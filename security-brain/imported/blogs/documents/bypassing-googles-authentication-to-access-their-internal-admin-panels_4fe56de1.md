---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-24_bypassing-googles-authentication-to-access-their-internal-admin-panels.md
original_filename: 2018-02-24_bypassing-googles-authentication-to-access-their-internal-admin-panels.md
title: Bypassing Google’s authentication to access their Internal Admin panels
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 4fe56de19685e3a9129957d8a04b812ee0a13f3c29b379d3590a71955a9b14d1
text_sha256: 3adde061b4c4f3be3d5b664050d6cef60754b6789ba6aae3253b3aa7b8e00a04
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Google’s authentication to access their Internal Admin panels

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-24_bypassing-googles-authentication-to-access-their-internal-admin-panels.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `4fe56de19685e3a9129957d8a04b812ee0a13f3c29b379d3590a71955a9b14d1`
- Text SHA256: `3adde061b4c4f3be3d5b664050d6cef60754b6789ba6aae3253b3aa7b8e00a04`


## Content

---
title: "Bypassing Google’s authentication to access their Internal Admin panels"
url: "https://medium.com/bugbountywriteup/bypassing-googles-fix-to-access-their-internal-admin-panels-12acd3d821e3"
authors: ["Vishnu Prasad P G (@vishnuprasadnta)"]
programs: ["Google"]
bugs: ["Authentication bypass"]
bounty: "13,337"
publication_date: "2018-02-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5965
scraped_via: "browseros"
---

# Bypassing Google’s authentication to access their Internal Admin panels

Vishnu Prasad P G
 highlighted

Bypassing Google’s authentication to access their Internal Admin panels — Vishnu Prasad P G
Vishnu Prasad P G
Follow
5 min read
·
Feb 24, 2018

3.4K

14

Hi all,

I’m Vishnu prasad, a third-year engineering student, a passionate developer, and a noob in bug hunting ( Please forgive my mistakes in this writeup, if any ).

I recently found a bug in Google that enables anyone to access the internal admin panel of YouTube’s Broadcasting Satellite & YouTube TV. I reported it as part of the Google VRP which earned me $13337.

And this article explains my story to the Google hall of fame.

With that being said, let’s start 😃

One day, while searching for new bugs in Google, I got some of Google’s IP addresses from some domain.

I checked the IP addresses and could understand that the list contained some internal devices IP too(Recon). Recently, a similar bug was reported by my friend KL SREERAM regarding their internal device IP and also another one by my good friend Vishnu who had found a subdomain with access to the admin panels. However, these issues had already been fixed. And Google had also blocked the public access to these entire IP ranges.

But now, I had some similar IP addresses with me and I somehow had to find a way to bypass this restriction. 😺

I started searching extensively in Google for a way to access the blocked IP addresses [of Google]. Every article/blog/forum/comments I read told me that we need their proxy/VPN to access the IP addresses.

I kept searching and searching for new ways

And then all of a sudden it happened!

My power supply went off!

And I have no battery backup devices 😕 (KSEB sucks! )

I was like …..

I had already decided that I would somehow find a way to bypass this and that I was not ready to quit 👽

I just couldn’t stop and so, I took out my mobile phone and started searching in Google again. As I searched, just out of curiosity, I tried to open one of those IP addresses in my Google Chrome mobile browser (I love browsing in Chrome)

WTF — A page with HTTP login appeared in front of me.

Whoa! I never expected to see that!

So there was login in front of me, possibly the door to the inside of one of the most powerful companies in the world. However, I needed a username and password to get into it.

So what do I do?

I tried clicking the log in button without entering any credentials at all.

To my surprise, a page with many buttons and options appeared in front of me. It took me a minute to realize that I am inside a Google product’s Admin Panel.

BINGO !! I am in!

(I got the idea of using null credentials for Google login from SREERAM’s blog post while I read about his finding. Thanks for that Bro..! )

At that time, however, I really didn’t know how it happened. The only thing I knew was that I had got access to an admin panel of a Google product.

Get Vishnu Prasad P G’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After a few minutes, the power was back and I tried to open the same IP on my computer. But it wouldn’t open. The login page never showed up! How unfortunate!

Now, I got totally confused. 😕

Why was it working in my mobile phone browser and not in my laptop browser? This question kept bothering me…

Anyway, in one hour, I made a POC on my phone and submitted the report to Google.

In about 5 hours I got their reply that they had triaged my report. I also got a “Nice Catch!” response to my report. I was jumping with joy. The mighty Google at Silicon Valley had responded to me at Trivandrum!

They asked me — “ Can you tell us which IP addresses did you use for this access?”. They basically wanted to know which proxy did I connect to. But I didn’t know that. So I decided to dig deep into it.

In about 2 hours I found the loop that helped me enter into their admin panels.

The grand mystery had been decoded!

It was Google’s Data saver that helped me to access their internal IP’s. It was turned on in my Chrome mobile browser. I have included an image to help you understand its working.

Press enter or click to view image in full size

This proxy acts as their access proxy and gave me access to their internal pages. So, after adding this proxy to my computer I was able to access the admin panel from my laptop browser as well.

There you go. Now with that, anyone can access the Google admin panels from anywhere in the world!

Scary !!

I replied to them with a very detailed write-up. And I got a reply within 30 minutes.

Press enter or click to view image in full size

I have included some screenshots as well as the admin panel that I got access to.

Press enter or click to view image in full size
Their Satelite reciever admin panel
Press enter or click to view image in full size
YouTube TV Admin panel (Screen Control)

In addition to this, I got access to their broadcasting panel, internal PCSC configuration, and many such locations using this particular technique.

Finally, they rewarded me with $13337 😲

Google Hall Of Fame — https://bughunter.withgoogle.com/rank/hof/1

Profile Link — https://bughunter.withgoogle.com/profile/76289848-1b71-44c7-b11f-6475ffbc4d7f

Now, Also they selected me as one of their Top Bughunter in year 2k17 😃.

And featured in Times Of India(TOI). 😃

The reason behind my achievements and the one who inspired me to always dream and aim higher is my mentor Mr. Sreenath Sasikumar, Founder and CEO of MashupStack — a fullstack web development training company. They rightly say, well begun is half done :-)

For More details contact me — https://www.vishnuprasadpg.com

Thank you,

Vishnu Prasad P G
