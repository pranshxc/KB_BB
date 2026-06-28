---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-06_let-me-unmask-my-next.md
original_filename: 2023-04-06_let-me-unmask-my-next.md
title: Let me Unmask my next 👻
category: documents
detected_topics:
- idor
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 8f985b32ce4e33f67fa109e671f5ad35cba838507d406a8cdfa395af20faef8c
text_sha256: f84843d49b2809402ee3327adeafdcf83472f9ba27b0a76ab128a7c04e1c6ab5
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Let me Unmask my next 👻

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-06_let-me-unmask-my-next.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `8f985b32ce4e33f67fa109e671f5ad35cba838507d406a8cdfa395af20faef8c`
- Text SHA256: `f84843d49b2809402ee3327adeafdcf83472f9ba27b0a76ab128a7c04e1c6ab5`


## Content

---
title: "Let me Unmask my next 👻"
page_title: "Let me Unmask my next 👻 | crypt0g30rgy.github.io"
url: "https://crypt0g30rgy.github.io/post/TinderBug"
final_url: "https://crypt0g30rgy.github.io/post/TinderBug"
authors: ["g30rgy th3 d4rk (@Crypt0g30rgy)"]
programs: ["Tinder"]
bugs: ["IDOR", "Payment bypass"]
publication_date: "2023-04-06"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1293
---

# [crypt0g30rgy.github.io](https://crypt0g30rgy.github.io/)

# Let me Unmask my next 👻

## Ain’t we all humans 😂

This is a story about a bug i found on the popular dating app tinder, it involved a paywall bypass and idor that could enable me to see who had matched and liked my profile without waiting or paying.

i reported this bug on february of 2022, i was in my house bored and lonely one day in the month of `"love"` february, i hadn’t had much luck with `"love"` since am an indoor 24/7 person and i thought well if i get everything else i need from the internet why not also try to get `"love"` from there, made a tinder account. And after several swipes and like backs (a few days) i would always hit the paywall when i wanted to see who like me back. So on the 21 of that month i said to myself `"hey, am a hacker and no one applicatin should dictate to me what to do"` So i grabbed my laptop, fired burp suite and firefox, proxy working i logged into my tinder account and within a few hours i figured the application flow between seeing who likes you and their info.

The flow was as below;

> When a normal user registers to tinder the are not allowed to view who has liked them until they purchase a subscription, you only get blurred data back. ![blurred](/images/poc/blured.jpg)

> When the try to view data of a user who have liked them by visiting <https://tinder.com/app/likes-you> they are hit by a paywall and can not proceed. ![paywall](/images/poc/paywall.jpg)

At this point all the liker’s data is blurred including pictures . However i realized that this security measure is only applied in the frontend and the underlying api brings back all the user data including user_id which can then be user to query each individual users data where we can even view the full unblurred /Original images. The api gives users this information really quick and easy and its just not shown in the frontend due to the paywall

After finding this information disclosure i started poking around for a way to retrive a specific (single) user data. this is where i ended up finding an idor at `"/user/'your likers id'?locale=en-GB"`

With all the data in place i could query the data of users who had liked me back and also get their unblurred versions of pictures and any other information that they had on their profile.

## Reproduction Steps

  1. Connect a http logging and editing tool to your browser like burp and visit <https://tinder.com/app/likes-you> (Should have someone liking your profile first) and you should see the blurred profile
  2. Look at your burp history and find a request to the api `GET /v2/my-likes?locale=en-GB`
  3. Find the likers’ user_id under ‘{“type”:”user”,”user”:{“_id”:”","badges":[],'
  4. Now hit the below api endpoint;

  
  
  GET /user/`your likers id`?locale=en-GB HTTP/2
  Host: api.gotinder.com
  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0
  Accept: application/json
  App-Session-Id: <>
  User-Session-Id: <>
  X-Supported-Image-Formats: webp,jpeg
  Platform: web
  X-Auth-Token: <>
  Origin: https://tinder.com
  Referer: https://tinder.com/
  Te: trailers
  

  1. Replace all with their respective data like user tokens or in proxy find the `GET /v2/my-likes?locale=en-GB` api request and send to repeater then delete the “/v2/my-likes?locale=en-GB” and replace with `"/user/'your likers id'?locale=en-GB"` Observe the api response and you can find all the likers info which was blurred including original images, distance from you etc. Images with the string ‘original’ in url will result in being able to view the unblurred image.

## Report

After i found this bug i was so excited, given the target and the bounty, 4000$ at the time. So i quickly headed to the report section of tinder and submitted my bug and waited to get rich 😂😂.

The api model returning the data of who liked you was fixed and the following day was returning no data.

well my dreams of getting rich quickly were extinguished early the next day when it turned out the idor was a duplicate 😂😂😂, ofcourse it had to be, i mean what are the chances, more than 75% i tell you.

![dupped](/images/poc/duplicate.png)

## Contacts

### @[github](https://github.com/crypt0g30rgy) @[twitter](https://twitter.com/crypt0g30rgy) @[LinkedIn](https://www.linkedin.com/in/george-maina-waithaka-95a465214/) @[Intigriti](https://app.intigriti.com/profile/g30rgyth3d4rk) @[hackerone_old](https://hackerone.com/crypt0p3n3tr4t0r?type=user)
