---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-01_how-i-managed-to-get-an-googlecom-email-address-bypassing-their-previous-patch.md
original_filename: 2018-12-01_how-i-managed-to-get-an-googlecom-email-address-bypassing-their-previous-patch.md
title: How I managed to get an @Google.com email address, bypassing their previous
  patch!
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- mobile-security
language: en
raw_sha256: e0fa939d601adc620bff0ea0c9664b6d33cff9f6ff480507aac905587542ffb4
text_sha256: 3219082110fc23123bf0b87132ac1ce73822d4e7ea30c6fc3f2099316a4d7dac
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I managed to get an @Google.com email address, bypassing their previous patch!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-01_how-i-managed-to-get-an-googlecom-email-address-bypassing-their-previous-patch.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `e0fa939d601adc620bff0ea0c9664b6d33cff9f6ff480507aac905587542ffb4`
- Text SHA256: `3219082110fc23123bf0b87132ac1ce73822d4e7ea30c6fc3f2099316a4d7dac`


## Content

---
title: "How I managed to get an @Google.com email address, bypassing their previous patch!"
page_title: "How I managed to get an @Google.com email address, bypassing their previous patch! - Andmp | A blog about infosec, bug hunting and more!"
url: "https://www.andmp.com/2018/12/how-i-managed-to-get-google.html"
final_url: "https://www.andmp.com/2018/12/how-i-managed-to-get-google.html"
authors: ["Gopal Singh (@gopalsinghcse)"]
programs: ["Google"]
bugs: ["Logic flaw"]
bounty: "3,133.70"
publication_date: "2018-12-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5552
---

_The Google Bug Tracker helps them(Google) in tracking through different bugs and security issues, but Gopal, a highly skilled security researcher managed to leverage and pilferage Google through its own issue tracker, isn't it quite creative? A defensive mechanism, since the same tool is used to track and patch security issues was implemented to pervade through Google's protection._

  

Every organisation have bug trackers, in fact, for example most companies use external ones like Jira bug tracker to track and resolve bugs, so what makes Google's case unique in particular is their custom tailored Issue Tracker and it's features. Security researcher [Gopal ](https://twitter.com/gopalsinghcse)discovered that although Google had in the past attempted to fix several security issues in their Bug Tracker, yet, it was unsafe and indeed his firm conviction led to him finding a different issue, that can be called a regression but nevertheless, he bypassed Google's previous fix proving the fact - No system can be made "secure" (completely), no matter what amount of patches you make, this again shows the need for bug bounties to motivate and attract highly talented talented individuals as Gopal, and also motivates security researchers to use offensive methods as the one mentioned in this case, and keep trying harder to circumvent all security measures kept in place, even previous patches.

  

\------------------------------------------------------

  

##  How I managed to get a Google organisation email, bypassing their previous patch!

I came across this [writeup](https://medium.freecodecamp.org/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5) by [Alex](https://medium.com/@alex.birsan). I started testing the issue tracker, and I wanted to see if I could somehow manage to get an @google.com Account. In the issue tracker, I found the  _browse components feature._ There were two public issue trackers, I clicked on Android Public Tracker

Bugs reported to _Android_ showed up here. To report a Bug in Android public issue tracker you may simply send an email to-

buganizer-system+_componentID_ @google.com

In this case, android’s component id is **190923**.

The issue I made, got listed in the public issue tracker. I got a confirmation email from buganizersystem+my_email@google.com and hence, replies to the email would be directed to-

buganizer-system+_componentID_ _+__issueID_ @google.com

I replied to that email and comment was posted in the conversation. I can add google email to see if I can get a confirmation code, to test this I clicked on [Forwarding and POP/IMAP](https://mail.google.com/mail/u/0/#settings/fwdandpop) in Gmail settings and added the google email to the forwarding email address. I was surprised to see I got a confirmation code in the Android public issue tracker.

There are two parts here, to get a google account. Signup and verification. I can verify a google account, but I could not signup for a @google.com account so my report got closed as _Won’t Fix. Bummer!_

  
  
  
  
  
  

![](https://cdn-images-1.medium.com/max/958/1*VPKKHkJihwBU5EGmiCO87Q.jpeg)

  

  

Then I started visiting every subdomain of Google to see if I could use google.com email to signup and this new signup page appeared.

  
  
  
  
  
  

![](https://cdn-images-1.medium.com/max/958/1*FnYAmegCjYie3tJD31dW7A.jpeg)

  

I could feel my heartbeats racing, after coming across this new signup page. I signed up using the bug…@google.com email and then it asked me to verify by entering the code.

###  Verifying The email address

I was waiting for the verification code in the conversation and then received the verification code in the mail.

  
  
  
  
  
  

![](https://cdn-images-1.medium.com/max/958/1*2V5EtNmYL9dLuWzzE5Pahg.jpeg)

![](https://cdn-images-1.medium.com/max/958/1*i3SoADa-WPpR624Nr9BPyA.jpeg)

  

After successfully signing up for the Google Account, I reopened the issue.

Nice catch!

  
  
  
  
  
  

![](https://cdn-images-1.medium.com/max/958/1*OM8Cx-NTdPsFxkGJgMcqxQ.jpeg)

  

Finally, at 9:50 PM that day, the most awaited email arrived $3133.70. I could not sleep the whole night.

  
  
  
  
  
  

![](https://cdn-images-1.medium.com/max/958/1*cp_Noolq5VnWPNf3NqgNGg.jpeg)

  

  

###  Video PoC

  
  
  
  
  
  

  

Thanks to [Alex Birsan](https://medium.com/@alex.birsan) this would not be possible without his write-up. I learned a lot from reading write-ups
