---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-18_how-i-hacked-facebook-part-two.md
original_filename: 2021-03-18_how-i-hacked-facebook-part-two.md
title: 'How I hacked Facebook: Part Two'
category: documents
detected_topics:
- ssrf
- command-injection
- path-traversal
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- ssrf
- command-injection
- path-traversal
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: 9b6b3ef2f09c9ae5be0471da3d4aa239308bdd1c5f50561b706071404b0120a5
text_sha256: 7e9491929292206d9687f890d5f730fcf7fbf6cead273913d90b0907e50451e8
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked Facebook: Part Two

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-18_how-i-hacked-facebook-part-two.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, path-traversal, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `9b6b3ef2f09c9ae5be0471da3d4aa239308bdd1c5f50561b706071404b0120a5`
- Text SHA256: `7e9491929292206d9687f890d5f730fcf7fbf6cead273913d90b0907e50451e8`


## Content

---
title: "How I hacked Facebook: Part Two"
url: "https://infosecwriteups.com/how-i-hacked-facebook-part-two-ffab96d57b19"
authors: ["Alaa Abdulridha (@alaa0x2)"]
programs: ["Meta / Facebook"]
bugs: ["SSRF", "Account takeover", "Cookie manipulation"]
bounty: "54,580"
publication_date: "2021-03-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3807
scraped_via: "browseros"
---

# How I hacked Facebook: Part Two

How I hacked Facebook: Part Two
Alaa Abdulridha
Follow
8 min read
·
Mar 18, 2021

669

9

Press enter or click to view image in full size

Description: This is the second and final part of How I hacked Facebook you can find part one here [ How I hacked Facebook: part one ].

I highly recommend reading part one to understand the storyline.

In part one I have found Account takeover by an unsecured API which allowed me to change the password of any admin account with no user interaction, and I got rewarded 7500$ by the Facebook security team, In part two I have found account takeover using cookies manipulation and chained it with Internal SSRF I got rewarded a bounty of $xxxxx Yes 5 figures number .. let’s start.

This article was previously revised by multiple parties before releasing it, and I had to get written permission to release it as well so that some names and information might be changed as a request from Facebook and its partners.

So when I found the first vulnerability in part one Facebook mitigated it after a day of reporting it.. then I had to get back to read the burp suite history and just to see how things worked.

Press enter or click to view image in full size

As you can observe in the screenshot, Number 1 in blue, the cookies its ASPXAUTH, Absolutely yes!.

Have you got what I imply? — ASPXAUTH indicates 80% it’s vulnerable but first, you need several things:

validationKey (string): hex-encoded key to use for signature validation.
decryptionMethod (string): (default “AES”).
decryptionIV (string): hex-encoded initialization vector (defaults to a vector of zeros).
decryptionKey (string): hex-encoded key to use for decryption.

You can read more about that here: MachineKey Class

well, I don’t have these 4 things, so how did I assume it’s vulnerable? — Okay. Actually, I didn’t but most of the application that uses the ASPXAUTH they use only email or user in the encrypted cookies with the encryption keys, and expiration time. I exploited it in other bounty programs websites using the same method many times before, and it worked.

So here I have to find a way to go around this, and I believe there’s nothing to lose by trying, after that, I proceeded to google and searched for other websites that utilized the same application — I assumed here that I will be lucky and find a website that utilizes the same application and same encryption keys and I just have to use the correct admin username.

I did that and I found another website using the same application and the registration is active and I registered using a username that is used by the Facebook admin, I intercepted the request and took the ASPXAUTH and replaced it with the Facebook expired ASPXAUTH, and guess what?

Press enter or click to view image in full size

I missed this Panel for a while :) .. but yeah! I’m back into it again, now let’s have a little talk about ASP.net mistake that most developers must be careful while building their applications to secure it according to these several points::

The ASPXAUTH must be stored in the database and the application must check if it’s valid.
The ASPXAUTH sometimes must contains more than the username as further validation.
The Encryption and decryption keys must be different from site to site (must change the default keys).

Conclusion 1: I was able to login using any admin account just by knowing the username, the complexity of this vulnerability I consider it very low and the impact is high, If I report only this vulnerability I will get $7500 as the first part but I wanted more.

So I just noticed something in the panel which’s the option of making forms, and there was another option which’s API trigger. So, I suspected something, mostly there’s an SSRF here with no limits at all, according to that I wrote a message to the Facebook Security Team explaining to them my suspicion there’s almost certain critical SSRF in the application, and if I can get permission to test it, and they answered me :

at this point, I was still in contact with them in the report of the first part (The account takeover), because these vulnerabilities were reported a week after the first one. As you can see Facebook Security Team still thinks that I’m claiming that I have another auth bypass and SSRF even after I explained the vulnerabilities to them with proofs. According to that, it means they gave me the green light to test the SSRF.

After a while, I wrote a small script and uploaded it to their editor, the script allowed me to send any request I want with any data (GET, POST, PUT, PATCH, HEAD, OPTIONS) to any URL — internal or/and external.

Press enter or click to view image in full size

From the script backend, I was able to change the request method and the sent data, etc

at this point, I was able to escalate this vulnerability to RCE, LFI if I go a little further maybe (I’m not really 100% sure about this point, I asked Facebook later to grant me the permission to reverse engineer the app but they did not accept, and they believe I won’t be able to escalate it).

And I tried to hit the Facebook canary script :), again guess what?

Press enter or click to view image in full size

I got my lucky Canary token, Now what’s next? — I have to make a new report with the full details including the scripts and PoC as they mentioned before.

Get Alaa Abdulridha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Conclusion 2: By writing a script to send custom-crafted requests I was able to gain an Internal SSRF and gain access to the Facebook internal network, The complexity here I consider it low and the Impact is Critical.

The Full Impact of this SSRF :

A successful SSRF attack can often result in unauthorized actions or access to data within the Facebook internal network, either in the vulnerable application itself or on other back-end systems that the application can communicate with. In some situations, the SSRF vulnerability might allow an attacker to perform arbitrary command execution.

An SSRF exploit that causes connections to external third-party systems might result in malicious onward attacks that appear to originate from the organization hosting the vulnerable application, leading to potential legal liabilities and reputational damage.

.For more info about SSRF vulnerabilities check this article from portswigger.

Final Conclusion: I chained both vulnerabilities to get to one point which’s accessing the Facebook internal network (SSRF), By using the Account takeover to reach into my uploaded script inside the application which will send custom-crafted requests as I want.

Let’s talk about what I’m able to achieve by using the chain of vulnerabilities I found until now:

I’m able to access any Facebook employee account in the legal department panel.
I don’t need to explain the kind of juicy information the attacker could find after signing in.
I was able to use the SSRF to access the Facebook internal network (intern.our.facebook.com).
With a little more effort I believe I was able to escalate this vulnerability and use it to scan the internal network/servers.

we all know how critical the SSRF is especially it’s not rate limited and I can easily edit the content type and the request methods and as the Facebook payout guidelines say this vulnerability should be rewarded with a bounty of $40,000 with $5000 bonus if I’m able to edit the request content type and the request method.

After a long time of waiting, I just got this message from Facebook :

Got rewarded by Facebook $40,000 plus a $2,000 bonus (which should be $7,000 lol)

so I asked them why I did not get the full control bonus ($5000), and the answer was:

The total with the first vulnerability is $54,800

I reported this vulnerability days after the vulnerability in part one.

Report time Line:

Wednesday, September 9, 2020 — Vulnerabilities reported.
Monday, October 26, 2020 — Facebook asked me to open a new report. ~Mitigation applied.
Monday, October 26, 2020 — Report Triaged.
Thursday, February 25, 2021 — Fixed and rewarded. ~ 6 months I know lol.
Friday, March 5, 2021 — Bonus $5300 rewarded.

I would like to give a Golden tip for the bug hunters, Always when you see ASPXAUTH try to get the cookies from another website that using the same application and test the same method that I did:

Create new ASPXAUTH cookies from the other website.
Test if the cookies will work on your target website.

I enjoyed this but waiting 6 months and closing reports for irrational reasons I’m very grateful but all this hard-working, and this is not the only SSRF I found, actually, I found more interesting ones but Facebook closed them as informative because Facebook signed an agreement with the vendor which it was signed weeks after the reports got Triaged which this is not my problem actually, so anyways I just won’t call it the best experience.

This is the final part and I’m sorry if anything is not clear and for the delay in providing part two, as mentioned before, I waited some time for written permission, and the report got revised, so a lot of things got removed or blurred to keep the privacy of the other parties.

you can follow me on Twitter For more write-ups and tips: https://twitter.com/alaa0x2

and you can check the write-up on my personal blog:

https://alaa.blog/2021/02/how-i-hacked-facebook-part-two/

Cheers.
