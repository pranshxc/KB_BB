---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-10_cors-misconfiguration-pii-leak.md
original_filename: 2023-12-10_cors-misconfiguration-pii-leak.md
title: CORS Misconfiguration -> PII Leak
category: documents
detected_topics:
- cors
- command-injection
- automation-abuse
tags:
- imported
- documents
- cors
- command-injection
- automation-abuse
language: en
raw_sha256: 064e8a403a6b2d9229342a70b3836d64ce41ecf2f7adcfd2184c40a969cebf3b
text_sha256: 96078eccfb8d50fc31e26ade53c7fe8e821b9c7ddd2737ab2afd3c6f90a8a65d
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# CORS Misconfiguration -> PII Leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-10_cors-misconfiguration-pii-leak.md
- Source Type: markdown
- Detected Topics: cors, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `064e8a403a6b2d9229342a70b3836d64ce41ecf2f7adcfd2184c40a969cebf3b`
- Text SHA256: `96078eccfb8d50fc31e26ade53c7fe8e821b9c7ddd2737ab2afd3c6f90a8a65d`


## Content

---
title: "CORS Misconfiguration -> PII Leak"
url: "https://medium.com/@boogsta/cors-misconfiguration-pii-leak-2765ff5b7115"
authors: ["Boogsta"]
bugs: ["CORS misconfiguration"]
publication_date: "2023-12-10"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 641
scraped_via: "browseros"
---

# CORS Misconfiguration -> PII Leak

CORS Misconfiguration -> PII Leak
Boogsta
Follow
4 min read
·
Dec 11, 2023

186

Twitter

https://twitter.com/Warlok_x00 — Follow me to keep up to date

Hello again!

Where have I been the last 3 months? Well firstly trying to not get a duplicate report on bug bounties for a start. But also I’ve been studying for my CySA+ certificate as well as partaking in the TryHackMe AoC 2023 side quests. More on that on the 28th December so stick around ;)

Alrighty onto the bug! So as the title states this was a CORS (Cross-Origin Resource Sharing) misconfiguration on a program that doesn’t want to be named so I’ll try and keep their identity as close to my chest as possible while also providing you with the information. If you want to read up more about CORS misconfigurations please see here

What is CORS (cross-origin resource sharing)? Tutorial & Examples | Web Security Academy
In this section, we will explain what cross-origin resource sharing (CORS) is, describe some common examples of…

portswigger.net

Now navigating to the website, I first did my basic recon on the main page and didn’t really find much but seen we had a login and sign up portal. Nice, can note this for later testing. But first up, lets make an account on the website. After doing the sign-up to the website. I intercepted the traffic nothing really stood out. So I tried to edit my user information and and found a nice request like below

Press enter or click to view image in full size
Request and response

As you can see, this is making a PATCH request and inside of the response we have the header access-control-allow-origin and it was showing a value of https://devportal.redacted.com. This is useful information as if you read the article above we are sometimes able to leak PII from this.

Get Boogsta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

We now face two questions:

It’s a PATCH request does it accept GET?
Are we able to put our own domain inside of the header?

We can do and test this by just editing the request we send over to the web server. Here I used Firefox developer tools but it can also work in Burpsuite too if you wanted to try this kind of bug out yourself. Lets have a look at the request and the response and break it down

Press enter or click to view image in full size

In the top section you can see my test account details (don’t worry it is a temporary email address) and in the bottom half we have our developer tools. Underlined in red on our left we have added the header Origin and supplied it with the value of https://test.com as this is the website we want to try and reflect in our response. In the middle of the developer tools, we have the word GET underlined. This is our request type and I changed the request method from PATCH to get to see if we get a valid response. On the right you can see we have https://test.com reflected in the access-control-allow-origin header. Perfect! Now we need to make a valid and working PoC. This can be foud on Github however I’ll also supply the PoC I used below too.

<html>
  <body>
  <div id="demo">
  <h1>CORS PoC by Boogsta</h1>
  <h2>Please press below the button below to connect your accont to our service!</h2>
  <button type="button" onclick="cors()">Exploit</button>
  </div>
  <script>
  function cors() {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
  document.getElementById("demo").innerHTML = alert(this.responseText);
  }
  };
  xhr.open("GET",
  "https://devportal.redacted.com/", true);
  xhr.withCredentials = true;
  xhr.send();
  }
  </script>
  </body>
 </html>

Where it says https://devportal.redacted.com this is where we of course put our websites domain. Now we have everything set up let’s host it locally!

Press enter or click to view image in full size
Beautiful!

Now once we press “Exploit” we get the following request

Press enter or click to view image in full size

Now we have successfully exploited the CORS bug and from here I reported it, and got a duplicate :( However! It’s the experience that counts and knowing it’s a valid find always should spur you onto the next program or bug.

The impact of this would be that attacker is able to leak the PII (Personal Identifiable Information) from the website. This would not look exactly like my PoC it would be more realistic and believable and also no pop-up too. The attacker would most likely send this data to some sort of server for later use.

This is classed as a P3 find and should always be taken serious especially when it poses threats and risks like what we seen in this write up.

Thanks for reading! Like I said before, I have some more write ups coming for the TryHackMe Side Quests challenges so stay around for that!
