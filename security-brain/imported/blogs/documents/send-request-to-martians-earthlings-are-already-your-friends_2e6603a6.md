---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-01_send-request-to-martians-earthlings-are-already-your-friends.md
original_filename: 2018-09-01_send-request-to-martians-earthlings-are-already-your-friends.md
title: Send request to Martians. Earthlings are already your friends.
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- cors
- csrf
- api-security
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- cors
- csrf
- api-security
language: en
raw_sha256: 2e6603a696cfe377de5c21ebae6e3d6185258988f617cffa9713d1c2163394ad
text_sha256: 67d7a5eff557b0fbdc173f91b1b5bc4dbe5557cd1944533b973b343d05358b69
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Send request to Martians. Earthlings are already your friends.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-01_send-request-to-martians-earthlings-are-already-your-friends.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, cors, csrf, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `2e6603a696cfe377de5c21ebae6e3d6185258988f617cffa9713d1c2163394ad`
- Text SHA256: `67d7a5eff557b0fbdc173f91b1b5bc4dbe5557cd1944533b973b343d05358b69`


## Content

---
title: "Send request to Martians. Earthlings are already your friends."
url: "https://blog.sagarvd.me/2018/09/youtube-csrf.html"
final_url: "https://blog.sagarvd.me/2018/09/youtube-csrf.html"
authors: ["Sagar VD"]
programs: ["Google"]
bugs: ["CSRF"]
publication_date: "2018-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5726
---

###  Send request to Martians. Earthlings are already your friends. 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ September 01, 2018  ](https://blog.sagarvd.me/2018/09/youtube-csrf.html "permanent link")

Hello everyone,  
  
I'm back with another write up. This time it's a Google bug. YouTube is Google's video sharing site and a great place to explore. As a bug hunter, you can spend hours or days or even weeks in YouTube without hesitation.I always used YouTube to play some music when I worked as a developer last year.  
  
When I started bug hunting, I tried YouTube multiple times and can't find any. Then I started hunting on another google services.  
  
After hunting for more than 2 hours, I found a bug on one of Google's acquisition. According to [Google](https://nullcon.net/website/archives/ppt/goa-16/Secrets-of-Google-VRP-by-Krzysztof-Kotow.pdf), a video PoC is required only if it is contributing something that the text can't. But I'm a great fan of videos and my first bug to google (duplicate) contained a 15min video 😎.  
  
I recorded a video of that bug I found and visited YouTube to upload it. when I clicked upload button, I noticed something strange aside it, something new. It looked like a message button.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzY-d71diZKEKS1DcQJtxrATuXDogOs7NJva-P3cW_O9eHrm90OIF6nH627OAJ_NuPNcf8GwKHKhL7OQ7TbxPrsZtp5OepRLK0yk0NBjiLoZn6uzMyT3qtTtko2Kbxh8SYOY8fiv5b9Qzc/s1600/youtube+writeup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzY-d71diZKEKS1DcQJtxrATuXDogOs7NJva-P3cW_O9eHrm90OIF6nH627OAJ_NuPNcf8GwKHKhL7OQ7TbxPrsZtp5OepRLK0yk0NBjiLoZn6uzMyT3qtTtko2Kbxh8SYOY8fiv5b9Qzc/s1600/youtube+writeup.png)

  
  
But then, the upload page has loaded suddenly and the button is not there. I confused. It looks like a new feature. And the bug I already have in my hand is from an old service. If I continue to report the bug I have in my hand, someone else may found and report bugs in the new service. Now, I don't want another duplicate (I already have 2).  
  
  
  
  
  
I decided to test this new feature and clicked back button. When clicked on the messenger icon, it's a new feature and I saw a message from YouTube 5 mins ago. I thanked god. I'm not late to the party.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9l2smOqSyKDguy2m97QeEz6iiMtz3M2mztDglDd0u4Y7esv1KESk70ymbhiTiW08b90UenG6k3AyoMmTVRoIHaAmFu_8Q0H2dernncxnQXTk6fbxOykDLH_N6plJ17PN2K1k9Y_QXGMwk/s320/youtube+writeup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg9l2smOqSyKDguy2m97QeEz6iiMtz3M2mztDglDd0u4Y7esv1KESk70ymbhiTiW08b90UenG6k3AyoMmTVRoIHaAmFu_8Q0H2dernncxnQXTk6fbxOykDLH_N6plJ17PN2K1k9Y_QXGMwk/s1600/youtube+writeup.png)

  
  
I clicked on the thread and a chat window, similar to hangouts' and Facebook's opened at the bottom. I saw a message there and a link to a video. Below that, there's a button "Send an Invitation link". Clicking on it, a link revealed. It was something like https://youtu.be/addme/{hash}.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB2XjKum-5lRqR298m5GK8vPIAU3gooyiyyswZ-SNfcfk6pO8GgYqCPQRIW198AmCT82IhSmUePNGG_gp4aGAe-NRtEP4HAM35MHWSy5zKOG1zW8b_-qjpdfqdFbui7aitmjOoqKRyDvg3/s320/youtube+writeup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhB2XjKum-5lRqR298m5GK8vPIAU3gooyiyyswZ-SNfcfk6pO8GgYqCPQRIW198AmCT82IhSmUePNGG_gp4aGAe-NRtEP4HAM35MHWSy5zKOG1zW8b_-qjpdfqdFbui7aitmjOoqKRyDvg3/s1600/youtube+writeup.png)

  
  
  
I opened it on another browser where one of my alternate google account logged in. It takes us to a page with a button to accept the request. I suddenly think about the possibility of csrf there. When inspected source code, there is no csrf token is present. Still I am not sure whether it is vulnerable to csrf. May be it is added by some dirty JavaScript code.  
  
  
  
  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiAzlfVLc1qiD9PQpKNM-Nx4waIzBUoKxhyXW_qzn_opq0xuNrG6rQsbsThu22lGa-67Aqqb3S1KnF0n0FN-vobh7Usv2zfC1uhQ7I8xWGABEtoI9RiB_pkdmI6f7zNQTPaZhEPDnpbSzC/s320/youtube+writeup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiAzlfVLc1qiD9PQpKNM-Nx4waIzBUoKxhyXW_qzn_opq0xuNrG6rQsbsThu22lGa-67Aqqb3S1KnF0n0FN-vobh7Usv2zfC1uhQ7I8xWGABEtoI9RiB_pkdmI6f7zNQTPaZhEPDnpbSzC/s1600/youtube+writeup.png)

  
  
I navigated to network tab and then clicked on the accept button. It sends a POST request to `https://www.youtube.com/add_contact?action_connect` and the only parameter present is `c` with value {{hash from the url}}. Whoa I was really excited to see there is no csrf token present in it and The next window shows that the you're connected with person X and a button start sharing.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUaf83U_q_8reQ1bT1Vx-cn_rchsaeh7tBaqWGRzZiUiTDhpisLd68eYxBi_Rj5EQjawecLcrK7L-jsK1h2cpCa3MdcQt_RDcrwKCnsYM2B6BkcC-m-dVDBbm-Qk_wwHQqnpfQiqpxqWWv/s320/youtube+writeup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUaf83U_q_8reQ1bT1Vx-cn_rchsaeh7tBaqWGRzZiUiTDhpisLd68eYxBi_Rj5EQjawecLcrK7L-jsK1h2cpCa3MdcQt_RDcrwKCnsYM2B6BkcC-m-dVDBbm-Qk_wwHQqnpfQiqpxqWWv/s1600/youtube+writeup.png)

  
  
I made a PoC with an ajax request. I aware of Cors and I don't want the response. Even if the response is blocked by CORS, no issues. But, something weird happened. I noticed a new term CORB. Chrome, first send an option request to the target and if ACAO header is not present, the request will be cancelled. Since I've took a break for ~10 months from the field, I didn't knew such a thing was implemented in chrome.  
  
The only choice I've left with is, making a normal HTTP post. But it will directly take the victim to "you're now connected" page and they'll know what just happened. Still it is a vulnerability and I reported it ASAP. All of this happened in 30 minutes.  
  
The PoC code looked like this  
  
`<html>  
<head></head>  
<body>  
<form action="https://www.youtube.com/add_contact?action_connect" method="post">  
<input name="c" type="hidden" value="{{hash fr}}" />  
<input type="submit" value="Continue" />  
</form>`  
` </body>`  
`</html>`

  
  
I added the button there to record PoC video. After that, I changed it to `documents.forms[0].submit()` so that the form gets submitted automatically. The impact changes from user interaction needed to no user interaction needed.  
  
In next panel meeting, Google rewarded with $ ████ bounty  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXHAtpMHUiOR3vhNKxfPA-yH_vmaLDr2SM-W6uiE9zikzvcmn13ptV40ox-XOnVMGbYWXz_z5BnD9PqV99jVmbS3CVVp084DBXOWlLZY-K-mgRpfyxCMAQWcYG5ES9BaywCglUI6u8AiWW/s320/youtube+writeup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXHAtpMHUiOR3vhNKxfPA-yH_vmaLDr2SM-W6uiE9zikzvcmn13ptV40ox-XOnVMGbYWXz_z5BnD9PqV99jVmbS3CVVp084DBXOWlLZY-K-mgRpfyxCMAQWcYG5ES9BaywCglUI6u8AiWW/s1600/youtube+writeup.png)

  
And Google fixed it in 15 days.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSFkH8hhcpB-_PYnxoInxkW_cGsrpUPqV9vU-q8ZZXGnWRArZM2W7EdwGRtUzi1iXbLp4KywCmvWD78nUWHzTQDuLOaR2ocKnc81Eg89zY0OQmmthJXIuV3ZuRdzKRixkG98wansQ2NO5w/s320/youtube+writeup.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSFkH8hhcpB-_PYnxoInxkW_cGsrpUPqV9vU-q8ZZXGnWRArZM2W7EdwGRtUzi1iXbLp4KywCmvWD78nUWHzTQDuLOaR2ocKnc81Eg89zY0OQmmthJXIuV3ZuRdzKRixkG98wansQ2NO5w/s1600/youtube+writeup.png)

  
**Impact**  
  
1\. Connect with anyone  
2\. Add this code in an iframe in your website and you will get Google account details of everyone who visited your site.  
  
**Fix**  
  
The session token is added to the form, which will protect against csrf attack.  
  
  
  
  
  
PoC Video  

  
  
  
TimeLine (timezone is in IST)  
  
25 Jul 2018 06:51 PM - Issue Reported  
25 Jul 2018 10:37 PM - Initial Triage ( Priority from P4->P3)  
26 Jul 2018 07:10 PM - Send the updated PoC link  
27 Jul 2018 12:59 AM - Accepted, P3 -> P2 and the Nice catch.  
31 Jul 2018 08:50 PM - Bounty Rewarded $ ████  
10 Aug 2018 10:04 AM - Issue Fixed.  
  
Thank you google for the bounty.

[Bug Bounty](https://blog.sagarvd.me/search/label/Bug%20Bounty) [CSRF](https://blog.sagarvd.me/search/label/CSRF) [Google](https://blog.sagarvd.me/search/label/Google) [Youtube](https://blog.sagarvd.me/search/label/Youtube)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/8968959338756795373?po=452557503831336440&hl=en&saa=85391&origin=https://blog.sagarvd.me&skin=contempo)
