---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-26_chains-on-chains-chaining-multiple-low-level-vulns-into-a-critical.md
original_filename: 2020-09-26_chains-on-chains-chaining-multiple-low-level-vulns-into-a-critical.md
title: 'Chains on Chains: Chaining multiple low-level vulns into a Critical.'
category: documents
detected_topics:
- xss
- jwt
- rate-limit
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- xss
- jwt
- rate-limit
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 16ea476a05ae696033ad3f36b5dafbf3cf3b54bea5733040abffb7e2fc538c3f
text_sha256: f74ce68d0e7387dd24602fb31dbfff6e8e88f989ca50b04ace63dd66c097f0d8
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Chains on Chains: Chaining multiple low-level vulns into a Critical.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-26_chains-on-chains-chaining-multiple-low-level-vulns-into-a-critical.md
- Source Type: markdown
- Detected Topics: xss, jwt, rate-limit, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `16ea476a05ae696033ad3f36b5dafbf3cf3b54bea5733040abffb7e2fc538c3f`
- Text SHA256: `f74ce68d0e7387dd24602fb31dbfff6e8e88f989ca50b04ace63dd66c097f0d8`


## Content

---
title: "Chains on Chains: Chaining multiple low-level vulns into a Critical."
url: "https://medium.com/@masonhck357/chains-on-chains-chaining-multiple-low-level-vulns-into-a-critical-8b88db29738e"
authors: ["Daniel Marte (@Masonhck3571)"]
bugs: ["Blind XSS", "CSP bypass", "Lack of rate limiting", "Exposed JWT generation endpoint", "JWT"]
publication_date: "2020-09-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4235
scraped_via: "browseros"
---

# Chains on Chains: Chaining multiple low-level vulns into a Critical.

Chains on Chains: Chaining multiple low-level vulns into a Critical.
Daniel Marte
Follow
4 min read
·
Sep 26, 2020

210

2

Hello! Hope all is well. I know it has been a while since my last writeup! Just a quick little introduction for those who do not know me. My name is Daniel but the hacking community knows me as Masonhck357. I have been hacking for a little over a year, mainly with Bugcrowd. I am currently Top 300 and continuing the grind! I want to share a vulnerability in which I leveraged several misconfigurations and low-medium vulns for a Critical bug!

Background on the program.

The program is an app that provides an online service directory that connects consumers to local businesses in the home improvement trade industry. They also have a separate new feature for Government entities. For the sake of the article, we will call the app. https://www.work.com :D

The Recon:

The first thing I do when performing recon on an app is to fingerprint. I typically use Wappalyzer’s chrome extension which will do the trick. I was happy to see that this was an app written in PHP. I then proceeded to spend a couple of hours using the webapp as intended. I first created a “consumer” account and used the app as that role, then switched to a “worker” account and did the same. I wrote down everything that I thought was interesting to avoid getting stuck in the rabbit hole. Towards the end of my day, I was reviewing my Burp Proxy history and I noticed that the session cookie did not have the Httponly or Secure flag. I COULD report this immediately and make a quick $100 but I decided to exploit it further.

Sidenote: I also ended up locating an AJAX directory that contained PHP files like https://work.com/api/ajax/dir/file.php. I decided to FUZZ that PHP endpoint for more PHP files and came across a hidden file called JWT.php When making this call, I would just receive a JWT token, similar to the same token I would use for certain API calls. I also noticed that this JWT token does NOT expire. Definitely seems interesting but not worth reporting just yet.

The XSS:

Get Daniel Marte’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I want to exploit the session cookie. The first thing I do is look for XSS. If I can locate an XSS, I can call document.cookie and retrieve the victim’s session token. I already reported an XSS on the program the day before so I didn’t want to use the same XSS on this report. I start going through every endpoint I came across that contained a parameter.NO LUCK! I did some content discovery to find some new assets but no luck. I decided to use GAU(https://github.com/lc/gau) and see if there were any other endpoints that I haven’t come across from that have been cached. I came across an endpoint: https://work.com/dir/app-detection.php. The page was still live but pretty useless. I decided to parameter Bruteforce the endpoint and I found a parameter that that was vulnerable to XSS. Immediately throw in a payload to see that I get stopped by the Content Security Policy.

The CSP Bypass:

To bypass this I ended up injecting an iframe and using the “srcdoc” attribute to bypass CSP and execute the HTML that’s inputted as the value of srcdoc(which would be a script making a call to BXSS URL) So now I have the victim’s session token! SUCCESS! I am still not finished though. I want to confirm that I can maximize the severity of this.

The Final exploitation

I immediately head to Burp and start searching for endpoints that expose sensitive information in the response body AND used the session token. I found some interesting sensitive information but nothing that would warrant max severity. I then thought….”What about that JWT.php file I found earlier?” I immediately throw that endpoint into Burp, replace the session cookie, and voila, a JSON web token on behalf of my victim that does not expire! I immediately take that token and start exploring with it. As expected, I was able to access much more sensitive data from my victim. If my victim was a government asset, I would be able to see highly sensitive documents that were uploaded to the app. I am also able to generate a payment JSON web token and make payments on behalf of the victim!

Conclusion:

Lets recap! Here are the following misconfigurations/vulnerabilities that were chained:

1. Lack of proper security flags on cookies
2. Blind XSS with CSP bypass
3. Hidden PHP file generating JWT token
4. Lack of rate-limiting allowing me to content discover with ease.
5. Sensitive information disclosure

Fun right? Always continue to push for the highest severity you can and always ask yourself if you can do more. Don’t sell yourself short and always aim for the top. I hope you all enjoyed the writeup! If you have any questions feel free to reach out on here or on my Twitter @masonhck3571.
