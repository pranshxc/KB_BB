---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-19_bugbounty-journey-from-lfi-to-rce-how-i-was-able-to-get-the-same-in-one-of-the-i.md
original_filename: 2018-04-19_bugbounty-journey-from-lfi-to-rce-how-i-was-able-to-get-the-same-in-one-of-the-i.md
title: '#BugBounty — ''Journey from LFI to RCE!!!''-How I was able to get the same
  in one of the India’s popular property buy/sell company.'
category: documents
detected_topics:
- command-injection
- path-traversal
tags:
- imported
- documents
- command-injection
- path-traversal
language: en
raw_sha256: dede6209156fcf3e508fca1f48888d1475aa2492985cd617139f16f8c6da8717
text_sha256: 86a2852f1d909d333d35dc4675aa6c6c56391cc51799e2e979eeec7e1fa96fa0
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — 'Journey from LFI to RCE!!!'-How I was able to get the same in one of the India’s popular property buy/sell company.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-19_bugbounty-journey-from-lfi-to-rce-how-i-was-able-to-get-the-same-in-one-of-the-i.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `dede6209156fcf3e508fca1f48888d1475aa2492985cd617139f16f8c6da8717`
- Text SHA256: `86a2852f1d909d333d35dc4675aa6c6c56391cc51799e2e979eeec7e1fa96fa0`


## Content

---
title: "#BugBounty — 'Journey from LFI to RCE!!!'-How I was able to get the same in one of the India’s popular property buy/sell company."
page_title: "#BugBounty — “Journey from LFI to RCE!!!”-How I was able to get the same in one of the India’s popular property buy/sell company. | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/@logicbomb_1/bugbounty-journey-from-lfi-to-rce-how-a69afe5a0899"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["LFI", "RCE"]
publication_date: "2018-04-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5906
scraped_via: "browseros"
---

# #BugBounty — "Journey from LFI to RCE!!!"-How I was able to get the same in one of the India’s popular property buy/sell company.

Top highlight

#BugBounty — “Journey from LFI to RCE!!!”-How I was able to get the same in one of the India’s popular property buy/sell company.
Avinash Jain (@logicbomb)
Follow
3 min read
·
Apr 20, 2018

1.1K

13

Hi Guys,

This blog is about how I was able to get Remote Code Execution (RCE) from Local file inclusion (LFI) in one of the India’s property buyers & sellers company. Let’s see what was the complete scenario-

As a bugbounty hunter the most important thing that I feel is the approach which we try or follow to exploit the vulnerability and which ultimately leads to have a much more impact from the vulnerability and the same I carried here.

While searching for the vulnerabilities, I found LFI in the target site- https://www.victimsite.com/forum/attachment-serve?name=../../../../../../../../../../etc/shadow&path=. As you can see parameter “name” was vulnerable to LFI.

Press enter or click to view image in full size
LFI (/etc/shadow)

I was confirmed that LFI was there and so now my target was to escalate it to get RCE. Before that, I have read many articles on how to get RCE from LFI and this one helped me a little here — https://medium.com/@p4c3n0g3/lfi-to-rce-via-access-log-injection-88684351e7c0 . Now the idea was to get access to some file may be log files which could provide some user controller input (in order to run some command) .

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I tried reading access logs ,error logs , different location to access them.

Press enter or click to view image in full size
Access Logs response

But it seems the user with which I got LFI didn’t have access to access logs files. Did a little reading,researching and I came to know that “/proc/self/fd” provides symbolic shortcut to access logs and various other system related file. So I tried reading those in search for access logs-

Press enter or click to view image in full size
/proc/self files

and I run intruder over /proc/self/fd/{number} and one of the fd files provided me access to access logs —

Press enter or click to view image in full size
Access log file

and what caught my attention here was “referer” header because I knew that it was something which is under user controlled input. Time to execute some command. I added ‘referer’ header in the HTTP request , set its value to system(id) and forwarded it-

Press enter or click to view image in full size
LFI to RCE

and a cheerful response :)

Press enter or click to view image in full size
RCE Response

So this is how I was able to get Remote code execution(RCE) from Local file inclusion(LFI)! :)

Report details-

13-April-2018 — Bug reported to the concerned company.

16-April-2018 — Bug was marked fixed.

16-April-2018 — Re-tested and confirmed the fix

Reward in progress.

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )
