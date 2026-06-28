---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-02_bragging-rights-lets-head-back-to-bug-bucket.md
original_filename: 2021-04-02_bragging-rights-lets-head-back-to-bug-bucket.md
title: 'Bragging Rights: Let’s head back to bug bucket'
category: documents
detected_topics:
- mfa
- idor
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- mfa
- idor
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 7f3c68d2fbb5be4f8ecd7a5a4d2133c897d43b00907d8ba5b8f5f2b4e5f8c129
text_sha256: c9de5aa5fd1a638fc31d86dc5c34b47a9d5a30b0fbe05f5bdd744614fca12925
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Bragging Rights: Let’s head back to bug bucket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-02_bragging-rights-lets-head-back-to-bug-bucket.md
- Source Type: markdown
- Detected Topics: mfa, idor, xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `7f3c68d2fbb5be4f8ecd7a5a4d2133c897d43b00907d8ba5b8f5f2b4e5f8c129`
- Text SHA256: `c9de5aa5fd1a638fc31d86dc5c34b47a9d5a30b0fbe05f5bdd744614fca12925`


## Content

---
title: "Bragging Rights: Let’s head back to bug bucket"
url: "https://infosecwriteups.com/bragging-rights-lets-head-back-to-bug-bucket-88c94730b6fa"
authors: ["Manas Harsh (@ManasH4rsh)"]
bugs: ["XSS", "IDOR", "2FA / MFA bypass"]
bounty: "951"
publication_date: "2021-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3770
scraped_via: "browseros"
---

# Bragging Rights: Let’s head back to bug bucket

Bragging Rights: Let’s head back to bug bucket
Manas Harsh
Follow
4 min read
·
Apr 2, 2021

242

1

Press enter or click to view image in full size

Welcome back my hacker homies! I hope you all are doing great, like me! So many things to learn daily and new resources keep coming. Keep upgrading yourself:) I’m here with another read of Bragging rights series and here I will be discussing a bunch of bugs which I found recently. It includes some XSS with bypasses, IDORs and a 2FA bypass. What are we waiting for? Let’s start!

Synack has been awesome for me till now and there are no mixed emotions. Only happiness and learning. Recently I was hunting on a program and it had multiple functionalities. I was not finding a good program since a couple of weeks before this and many of my bugs got rejected(probably 12?) for silly reasons. We don’t discuss it here, I got this program and it had two user roles, an admin and a normal user with less privilage. We got a long weekend and I put 3 days into it. It DID take time but output was awesome since I got 2 XSS, 2 IDORs and 1 2FA bypass.

Let’s discuss the XSS bypass first. Program had a funtionality where we can add the review for a doctor service and if someone goes there, he can read the posted review. Scenario is quite simple? Yes, but exploitation part was not that easy. I tried to put some payload and even tried the normal bypasses like “>, />, %00 and others but it didn’t work. My payloads were getting accepted as normal reviews. I went back to 
Brute Logic
 methods on his site i.e this. Finally, I was able to bypass this with this payload:

‘`”><><div/onmouseover=’alert(document.cookie)’> style=”x:”>

So, now whoever visits on this review, you know what happeens :p

Press enter or click to view image in full size

Takeaway: Put time to bypass the filters from codes. Try developer tools to understand the code and put your mind into it :)

Second XSS was quite simple and it was a reflected one. Once I knew what it’s filtering, I just applied the correct payload in URL and got a pop-up. Payload was simple, just added some bypasses before that:

‘`”><\x00script>javascript:alert(1)</script>

IDORs were quite generic so we won’t diuscuss that here. Simple number changers from URL encoded data and we could see the details of a particular patient. One IDOR was on reciept page and another was for how many times a a user has made appointments. Last one had a lower severity. If it was not enough, I got a dupe for this one :(

However, well, I got a 2FA bypass as well and I think I can discuss it here. Application had a 2FA functionality where you can login to the application with a 6-digit code recieved on your contact number. I was reading about 2FA bypasses recently and one of the methods helped me here. During authentication, if you put a wrong code, it gives you a JSON error in response like this:

{

“status”: “false”,

Get Manas Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“error”: “Incorrect code provided”

}

Now, if we capture the request with an incorrect 2FA code and change the response like this, you can successfully login to application:

{

“status”: “true”,

}

We need to change the response status code from 401 UNAUTHORISED to 200 OK as well. It was a cool bypass isn’t it? Not hard, just mindgames with application.

Takeaway: Check every possible way to break the application. Intrude everything you can. Application is all yours!

XSS: $441

IDOR: $300

2FA bypass: $410

Note: Not putting much screenshots because recently I have seen my screenshots on someone else’s LinkedIn post xD

For finding good bugs, I would say main apps are likely to be more vulnerable in my opinion. We just don’t put enough time on it. Good old applications with large scopes are still buggy. All it takes is time, sometimes people find the bugs in few mins, but those are some rare cases. A few times we lack in skills as well, I have felt that many times. I couldn’t find bug on a fresh target, someone else did within an hour. Not our fault, all we can do is keep learning!

I hope this read helps you in some way. If you find it helpful, show some love and clap icon is down below:) If you learn something from it, help someone else who needs it :) Keep helping, keep moving. We’ve got an awesome community :) Also, you can follow me on twitter with this username: @manasH4rsh.

See you all sooner:) take care, happy hacking!

Adios❤
