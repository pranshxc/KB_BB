---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-22_interesting-stored-xss-via-meta-data.md
original_filename: 2022-11-22_interesting-stored-xss-via-meta-data.md
title: Interesting Stored XSS via meta data
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- api-security
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- api-security
language: en
raw_sha256: 494719d184a5438d9f73fd6a269f34938f42569015b9080de477491e05b7c859
text_sha256: e2e960f1b8fc9987e7f5b868f0e542100beb0a38127320261c6eb2ea5b7bed22
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Interesting Stored XSS via meta data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-22_interesting-stored-xss-via-meta-data.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `494719d184a5438d9f73fd6a269f34938f42569015b9080de477491e05b7c859`
- Text SHA256: `e2e960f1b8fc9987e7f5b868f0e542100beb0a38127320261c6eb2ea5b7bed22`


## Content

---
title: "Interesting Stored XSS via meta data"
url: "https://medium.com/pentesternepal/interesting-stored-xss-via-meta-data-eb8fe1de8b33"
authors: ["Veshraj Ghimire (@GhimireVeshraj)", "Bibek Neupane (@nb1b3k)"]
bugs: ["Stored XSS"]
publication_date: "2022-11-22"
added_date: "2022-11-23"
source: "pentester.land/writeups.json"
original_index: 1878
scraped_via: "browseros"
---

# Interesting Stored XSS via meta data

Interesting Stored XSS via meta data
Veshraj Ghimire
Follow
3 min read
·
Nov 22, 2022

125

3

Back in February of this year 
Bibek Neupane
 and I had hacked on a private bug bounty program on Hackerone, we had chosen one of the social platform as our target. This post will detail how we discovered Stored Cross-Site Scripting via meta data on one of the CDN of target. The teamwork was awesome and I can’t wait to do another soon.

Initial ‘Recon’

The web application was all about posting medias/texts and interacting with people (somehow similar to twitter). We stumbled upon one interesting feature, where you could fetch media with your custom url.

Press enter or click to view image in full size

We obviously thought of SSRF here, entering the burp collaborator url resulted on the request from server where various headers were disclosed, we tried to exploit this but failed, later on found something on Acunetix categorized low:
https://www.acunetix.com/vulnerabilities/web/envoy-metadata-disclosure/

We reported it as it is, but got duplicated:

Press enter or click to view image in full size

We didn't loosed hope and thought of digging more into it.

‘The vulnerability’

After giving it some time, Bibek came up with really interesting thing:

Press enter or click to view image in full size

The XSS was executed with jpeg extension but we had no idea how.

Confused us

After spending some more time on the feature, we finally figured it out.

Get Veshraj Ghimire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When you keep any html page link, it will search for image in it and tries to fetch the image to keep thumbnail. What he did was, kept his html page link where <meta> tag was present with SVG file containing javascript which made the page fetch the image and store as image/svg+xml mime-type but with .jpeg extension.

Press enter or click to view image in full size

“Crafting the Exploit”

This is how the final exploit looked like.

Press enter or click to view image in full size

Where evil.svg is hosted with following SVG payload.

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
  alert("n1b3bk");
  </script>
</svg>

We reported it immediately, and their reaction was very prompt. They rectified it within three days of receiving the report. Internal team initially increased the severity from medium to high, but then reduced it to medium and granted the bounty correspondingly because the attack was on CDN, making it less severe.

Press enter or click to view image in full size

This was something i was unaware about and i guess i would never find these type of vulnerabilities, this is why collaboration is very important. I think this type of issue is very less discussed so we thought of making a public writeup on this for the community. All thanks to 
Bibek Neupane
 for thinking Outside the Box ❤ ️

Reach out us at twitter:
Veshraj Ghimire
Bibek Neupane
