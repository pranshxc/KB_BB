---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-06_full-company-building-takeover.md
original_filename: 2022-10-06_full-company-building-takeover.md
title: Full Company Building Takeover
category: documents
detected_topics:
- access-control
- xss
- sqli
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- access-control
- xss
- sqli
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: b028c9895d62922abee2d9f8019c7cb1d9b925befcfd2d99e64030bc3ee70eb2
text_sha256: 663b191e0be6a4900519f9470b9e094c7313032bc694ff46aa735de289c16800
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Full Company Building Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-06_full-company-building-takeover.md
- Source Type: markdown
- Detected Topics: access-control, xss, sqli, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `b028c9895d62922abee2d9f8019c7cb1d9b925befcfd2d99e64030bc3ee70eb2`
- Text SHA256: `663b191e0be6a4900519f9470b9e094c7313032bc694ff46aa735de289c16800`


## Content

---
title: "Full Company Building Takeover"
url: "https://omar0x01.medium.com/company-building-takeover-10a422385390"
authors: ["Omar Hashem (@OmarHashem666)"]
bugs: ["Information disclosure"]
publication_date: "2022-10-06"
added_date: "2022-10-08"
source: "pentester.land/writeups.json"
original_index: 2075
scraped_via: "browseros"
---

# Full Company Building Takeover

Full Company Building Takeover
Omar Hashem
Follow
4 min read
·
Oct 7, 2022

780

16

Hello everybody, Most of the time you read about account takeover or Infrastructure takeover but did you heard before about Company building takeover, Today I will share with you an interesting vulnerability that I found while hunting on one of the programs on Hackerone, so let’s refer to our target as Target-IP.com

Press enter or click to view image in full size

So i started by taking a look at shodan

ssl:<Company ssl name>

I found in the result some IPs that contain some login panels after spending some time on other IPs but I didn’t find anything that deserved to be reported until I found our Desired IP where our story Begins

After accessing the IP i found eMerge login panel

Press enter or click to view image in full size

After some information gathering, I found it’s a product that is commonly used between Company to manage Company building

I started to see if there is any public exploits

So let’s start by taking a look on searchsploit

┌──(omar㉿kali)-[~]
└─$ searchsploit “emerge”

Press enter or click to view image in full size

Nice there some juicy exploits here

But unfortunately none of them worked

So I completed my search on other websites for any public exploits on Google, packetstorm, GitHub, etc…

Found some other exploits but it looks like the product is patched

While analyzing headers i found that header

Press enter or click to view image in full size

PHP version is PHP/5 and we have login panel so what do you think is the best attack scenario for this version ?

it’s PHP Type Juggling

So let’s move to login request

Press enter or click to view image in full size

The parameters are sent in POST request as a string and to be able to test PHP Type Juggling we need to test it with content type that saves parameter data type if it is string or integer e.g. JSON

So i changed the content type and parameters to send the request in JSON

Press enter or click to view image in full size

But it seems that the back-end doesn’t accept JSON as it can’t recognize the login_id parameter which means our Type Juggling attacks failed before starting

After that, i started to test it for some attacks like SQLI on the login panel but it’s not vulnerable

Tried to get access to the registration endpoint maybe I can register a new user as an admin or less privileged user (e.g register,signup,sign-up,create-new-user)

┌──(omar㉿kali)-[~]
└─$ ffuf -w common-register-endpoints -u https://<Target-IP>/FUZZ

But i got nothing

Get Omar Hashem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So i started to doing some heavy fuzzing

┌──(omar㉿kali)-[~]
└─$ python3 dirsearch.py -w my-wordlist -u https://<Target-IP>/ -o dirsearch-output.txt

Left dirsearch working on background

Then started to do an analysis for the JS files hope to find some endpoints that will allow any type of broken access control vulnerabilities, Forced Browsing, exposed tokens, or hard-coded credentials, I tried to get DOM-Based-XSS by finding some sources following them to the sinks or finding any type of hidden parameters while doing all of this I found that dirsearch has finished her job

Press enter or click to view image in full size

At first glance, I expected that the “test.txt” file contains nothing except some popular messages that were echoed by the developers like “Hello World!”, “Hi” etc… but let’s check it

Try to enter the credentials on the login panel

Press enter or click to view image in full size
Note:data in the above image edited for sensitivity of data

The first thing I found in the dashboard were the logs containing the admin’s IP address and the time the employees accessed the building

Okay now i think there is no need to complete my JS analyses anymore 😁

After accessing the login panel as Admin Let’s see what we can do

Press enter or click to view image in full size

I found that I can watch live cameras of the Company Building

Press enter or click to view image in full size

I found that i can control the building elevators, doors

Press enter or click to view image in full size

I can collect employees data and adding new employees with authorization to access the Company building

Final Impact:

Take control of the entire building

Hope you guys enjoyed the write-up

Don’t forget to follow on Twitter

Twitter: @OmarHashem666

Keep in touch

Linkedin | Youtube | Twitter

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
