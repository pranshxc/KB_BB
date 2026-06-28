---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-19_unleashing-the-cloud-a-journey-into-hacking-college-servers-and-uncovering-secur.md
original_filename: 2023-06-19_unleashing-the-cloud-a-journey-into-hacking-college-servers-and-uncovering-secur.md
title: 'Unleashing the Cloud: A Journey into Hacking College Servers and Uncovering
  Security Vulnerabilities'
category: documents
detected_topics:
- sso
- access-control
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- sso
- access-control
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 47e6663e881f41cbc9fcb11b5b64bb97bc4d385b6a0f54c994e153cd79da23a9
text_sha256: 627ab1ff8b530d4c6e1e4d0eed776d7ff03a00a9339ad9db2ddd27f790c1d365
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: true
---

# Unleashing the Cloud: A Journey into Hacking College Servers and Uncovering Security Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-19_unleashing-the-cloud-a-journey-into-hacking-college-servers-and-uncovering-secur.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: True
- Raw SHA256: `47e6663e881f41cbc9fcb11b5b64bb97bc4d385b6a0f54c994e153cd79da23a9`
- Text SHA256: `627ab1ff8b530d4c6e1e4d0eed776d7ff03a00a9339ad9db2ddd27f790c1d365`


## Content

---
title: "Unleashing the Cloud: A Journey into Hacking College Servers and Uncovering Security Vulnerabilities"
page_title: "My Fist Hacking Blog : A Journey into Hacking College Servers and Uncovering Security Vulnerabilities | by Smukx | Medium"
url: "https://medium.com/@smukx/how-i-hacked-my-college-cloud-servers-and-find-dos-ato-google-authentication-priv-esc-676b2db98938"
authors: ["Smukx (@Smukx07)"]
bugs: ["Authentication bypass", "Account takeover", "DoS", "Privilege escalation"]
publication_date: "2023-06-19"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1032
scraped_via: "browseros"
---

# Unleashing the Cloud: A Journey into Hacking College Servers and Uncovering Security Vulnerabilities

My Fist Hacking Blog : A Journey into Hacking College Servers and Uncovering Security Vulnerabilities
Smukx
Follow
8 min read
·
Jun 19, 2023

87

3

1

Press enter or click to view image in full size
source from pandasecurity

Hello Guys . My name is Smukx , this is my first blog write up , so in this article we are going to see how i hacked my college cloud server , and Found interesting vulnerabilities… Trust me its going to be more Fun while you read and gain some unknown knowledge ! . Lets get into the series .

Found Vulnerabilities : Bypassing Google Authentication + DOS Attack + Account Take Over + Privilege Escalation !!
Current Scenario ; )

My College has assigned Some training sessions to learn Advance Linux , and C Programming for 1st Year Students . For that they have assigned clouds for each and every student to learn . As i am one of them ! but with a different mindset , you know We are hackers/pentesters , we think a different perspective…

Press enter or click to view image in full size
Source From Times of israel
Information Gathering …
Press enter or click to view image in full size

This is my default cloud , you can see that they are using ubuntu 20.04 LTS (Focal Fossa) Version . No Browser ,No additional software’s were installed and don’t know the password for superuser . thats a disadvantage ;(

To Access cloud, we have to sign in through google accounts ;)

Press enter or click to view image in full size

So i started Enumerating things , found ip address , kernel version, network config settings . but that doesn’t contain any interesting information so far . on ifconfig i can see it addr as 172.20.1.53 . If you guys have experience with docker then you know it’s a default bridge config for docker containers . So they use docker ?!, but for GUI ? i thought that they use some opensource services like VNC .

so i listed out the process that are running as user and root !Look what i got ?

Press enter or click to view image in full size

using my roll no as token .. hmm that’s sus ..

My Guess was right , On the ps 1 , we can see that it is running vnc_startup.sh through kasm_startup.sh with the filepath dockerstartup . we found it guys , they uses kasm workspace . so i written a small bash script to re-run the vnc_startup.sh for 60 Sec. when i run it , My VNC display has gone . Giving me an error ! . Actually they are using javascript to disable the settings function , but when i crash my system for a minute , the js got disable and i got the popup on the left side .

Press enter or click to view image in full size

One Good thing is that we have found the version for kasm_workspace . ;) . After a minute, i got my machine back . So when i searched for the version , i got goosebumps . i took a list of released versions for your

concern

Press enter or click to view image in full size
Image 4

OMG WTF ..! They use the oldest and beta version of this application . We know that older versions always has an Vulnerable piece of code . So, I started some web recon cause it’s a web server , as I am currently learning web security , yes . It’s time to learn new things .

before that when i try to Read source in dockerstartup file ,i find this help function on bash script !

Press enter or click to view image in full size

Found a github site , Readed whole repo

GitHub — ConSol/docker-headless-vnc-container: Collection of Docker images with headless VNC environments

Press enter or click to view image in full size
Github page

So they are using headless vnc sessions to create 500+ docker containers 😮, I think it’s a huge process . Using these scripts they have made the process easier.

So I shut my laptop and booted my PC at HOME , opened Burpsuite and started intercepting each Request . Opened nmap and scanned All the Ports , intercepted each and every file that kasm has . Found public ip address through `curl ifconfig.me` , pinged it through my local pc . It works ! . so the machine is connected to the same network ,good .Okk now what .. It’s Time to get into main work

Bypassing Google Authentication

So when I inspect some parameters , requests on browser . I saw a weird but interesting request through its public Ip .

Press enter or click to view image in full size

when I open that URL in new tab ! , I got access to my Cloud.

Press enter or click to view image in full size

the default credentials //username : cloud //password=***REDACTED*** ROLL NO

So we can bypass Google authentication ! . infact that's not cookie 😑, its an Token that assigned to Each containers . I think it has to ATO ? Hmm… Let’s See . For now :

Successfully Bypassed Google Authentication ✅

DOS ( Denial-of-Service )

As Far We have Gathered some Basic Information About the target , after all if you analyse it well , You got an idea !, the container was configured by default , so to dos the system , we can increase the memory and CPU Process to test !

Get Smukx’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Target Specs :

CPU : Intel(R) Xeon(R) CPU E7–8870 v3 @ 2.10GHz , RAM : 503 GB

For that i have coded some C and Python codes . First time coding for an server processor . i was so Happy while coding ! when i executed the C Program ( RABBIT VIRUS ALGORITHM ) Link , my cloud was started lagging and crashed !

Press enter or click to view image in full size

and After few minues later ! ….WAIT WHAT !! WTF IS GOING ON HERE !?!?

Press enter or click to view image in full size

The Whole Server including login portal was Crashed Permanently ;( .

source from tenor.com

wait wait ? if my guess was correct @! did they host the web page on the same Container ?? Ouch My God . At-least they can set a limit to each containers . By Default configuring on that script , it leads to load Every process on PC . The only solution for that is to restart the server . I have done 2 to 3 times after that , same results :)

Successfully Found DOS Vulnerability ✅

(ATO) Account Takeover

This was not what I Expected , but when i was looking on a request , i saw a POST request from /api/signin ..hmm thats look sus .. when i saw the content , it uses json format to fetch the API using my Email . hmm ;)

Press enter or click to view image in full size

I tried a different email of one of my classmates..

Press enter or click to view image in full size

Gotcha .. we did it boys , So when we modify the URL with the ID , we got in Guys !

Note : I can legally see all Students name,Email and Roll no though student portal .

Press enter or click to view image in full size

For a easy process i did write an simple python script ; )

Press enter or click to view image in full size

So the API was fetched from the database(MongoDB) using our Email from flask . So It fetches the data from the database to authenticate , if we gave the wrong input through Json it leads to flask error . can we pentest the mongo db ; ))

Successfully Found Account Takeover ✅

Privilege Escalation .

So we have reached the main part , the most awaited twisted movement. so getting started into recon again

Press enter or click to view image in full size
source from imdb.com

Used linpeas to find if any leaked file exists , used my shell script to discover the active containers in the specific domain. In that I found an silly but interesting thing . with that we can do ? the pic given below Explains you well . which i might cover in the part 2 ;)

Press enter or click to view image in full size
By looking at the Pic , you can understand what i mean ;)

So Lets get into the Topic …

No CVE’S on containers , that’s for sure . so when I’m searching the internet for Critical CVEs , Nothing Found ;( . But I didn’t lose Hope . So when i was surfing college stuffs , i got recommended an interesting video.

DEF CON 30 CONFERENCE . In that Samuel Erb and Justin Gardner Both covered a video about Exploring kasm vulnerability CSRF and RCE . what a luck !. So I took a bowl of popcorn 🍿 and started watching that , it was fun and the most roughest path ever .

Press enter or click to view image in full size
IMAGE FROM DEF CON CONFERENCE

Since the KASM version is too old , I executed it , guess what … it works . since the privilege escalation is not my credit , that’s why i didn't speak much on this topic

Successfully Executed Privilege Escalation Technique ✅

Did i Report ?! , Not yet

As i said earlier , there is 1 thing remaining that i need to Find , but it can take quite a time . But if i succeed it , i will write that topic in second part.

If you Like my Article . Give me a Clap for appreciation so that it could help me to publish more content like this . Do Follow my media Accounts Guys .

GitHub | : | Twitter

Happy Hacking :(){ :|:& };:

Bye Bye Guys , see you around …

Source From tenor.com
