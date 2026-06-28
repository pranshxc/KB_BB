---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-25_bugbounty-rewarded-by-securing-vulnerabilities-in-bookmyshow-indias-largest-onli.md
original_filename: 2018-03-25_bugbounty-rewarded-by-securing-vulnerabilities-in-bookmyshow-indias-largest-onli.md
title: '#BugBounty — Rewarded by securing vulnerabilities in Bookmyshow (India’s largest
  online movie & event booking portal)'
category: documents
detected_topics:
- sso
- idor
- command-injection
- api-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- api-security
language: en
raw_sha256: 354cbce7acbfe8f3e65eb70ef6de89828a583897b9028c241b242882047edbeb
text_sha256: fdff3e6da04f2ec6e0fc4f06a8a645baca19b37ce583da2ccfc2270503aae218
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — Rewarded by securing vulnerabilities in Bookmyshow (India’s largest online movie & event booking portal)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-25_bugbounty-rewarded-by-securing-vulnerabilities-in-bookmyshow-indias-largest-onli.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `354cbce7acbfe8f3e65eb70ef6de89828a583897b9028c241b242882047edbeb`
- Text SHA256: `fdff3e6da04f2ec6e0fc4f06a8a645baca19b37ce583da2ccfc2270503aae218`


## Content

---
title: "#BugBounty — Rewarded by securing vulnerabilities in Bookmyshow (India’s largest online movie & event booking portal)"
page_title: "#BugBounty — Rewarded by securing vulnerabilities in Bookmyshow (India’s largest online movie & event booking portal) | by Avinash Jain (@logicbomb) | Medium"
url: "https://medium.com/@logicbomb_1/bugbounty-rewarded-by-securing-vulnerabilities-in-bookmyshow-indias-largest-online-movie-bb81dba9b82"
authors: ["Avinash Jain (@logicbomb_1)"]
programs: ["BookMyShow"]
bugs: ["Host header injection", "IDOR"]
publication_date: "2018-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5944
scraped_via: "browseros"
---

# #BugBounty — Rewarded by securing vulnerabilities in Bookmyshow (India’s largest online movie & event booking portal)

#BugBounty — Rewarded by securing vulnerabilities in Bookmyshow (India’s largest online movie & event booking portal)
Avinash Jain (@logicbomb)
Follow
3 min read
·
Mar 25, 2018

426

5

Hi Guys,

Back with one more interesting blog explaining How I was able to find multiple vulnerabilities in India’s largest online movie booking portal — Bookmyshow. :)

Till now in my bugbounty hunting, I have realized one thing that companies which don’t have their bug bounty program are more reluctant to accept any kind of medium severity issues until and unless vulnerabilities are highly impactful and critical and the same happened here. Let’s see what was the complete thing —

So the first vulnerability that I managed to found was Host Header Attack, I was able to change the host header value to any malicious site and able to redirect. Further, I was also able to poisoned Web Cache. Now whenever user visit bookmyshow.com, he was getting redirected to the given malicious or phishing site. Below is the POC for it-

Press enter or click to view image in full size
Host Header Attack — Original Page

Above is the original request and it was vulnerable to Host Header attack. Here, I will change it it to goal.com and it can be observed in the below screenshot that in response there is 301 redirection and location to which application is redirecting depends upon the value of Host header in request-

Press enter or click to view image in full size
Host Header Attack — Changed host header value

And I was able to successfully got the redirection to the given input site goal.com —

Press enter or click to view image in full size
Host Header Attack — Successful redirection

And it was also leading to Web Cache Poisoning as this value was not getting validated on the server and so the user was getting redirected to the given malicious site whenever user tries to access bookmyshow.com . But there was a problem with this, the web cache was getting flushed very quickly and hence web cache poisoning was not persistent and effective and it also didn't get expected attention of bookmyshow security team. :) So, I resumed my hunt in search of some good bug and there comes this —

How I was able to get complete access to anyone’s owned “experience” !!

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Bookmyshow has the functionality by which a logged-in user can share their experiences.

Press enter or click to view image in full size
User Experience page

Every experience has an ID associated it. The URL looks like-

https://in.bookmyshow.com/national-capital-region-ncr/experiences/{Username}/test-hacked/5ab1284834e4ab0065ade267

and also every user can see any user’s experience ID by just seeing/reading their experiences so there was no bruteforcing or other techniques required to get the experience id of other users. The exploit was simple , I just modified the link a little and add a parameter “create” (which I got by creating my own experience ) —

https://in.bookmyshow.com/national-capital-region-ncr/experiences/create/{victim experience id}

and here you go,by accessing the above URL , I got the complete control/access over someone else experiences, I could edit the name, upload any image , write any description etc!!!

Report details-

27-Nov-2017 — Bug reported to the concerned company.

10-Jan-2018 — Bug was marked fixed.

10-Jan-2018 — Re-tested and confirmed the fix.

22-Jan-2018 — Rewarded by company.

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )
