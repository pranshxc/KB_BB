---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-27_getting-access-to-disabledhidden-features-with-the-help-of-burpsuite-match-and-r.md
original_filename: 2019-11-27_getting-access-to-disabledhidden-features-with-the-help-of-burpsuite-match-and-r.md
title: Getting access to disabled/hidden features with the help of Burpsuite Match
  and Replace settings
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: 51cee4079e5bfe2520eb2c20eb2d777c39e511d8f0fd18773dfd1215e248836a
text_sha256: d7ce77b7ac1d395f0613abe0d01d8e45261922feb05316cc07c7ce9dec6a4b52
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Getting access to disabled/hidden features with the help of Burpsuite Match and Replace settings

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-27_getting-access-to-disabledhidden-features-with-the-help-of-burpsuite-match-and-r.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `51cee4079e5bfe2520eb2c20eb2d777c39e511d8f0fd18773dfd1215e248836a`
- Text SHA256: `d7ce77b7ac1d395f0613abe0d01d8e45261922feb05316cc07c7ce9dec6a4b52`


## Content

---
title: "Getting access to disabled/hidden features with the help of Burpsuite Match and Replace settings"
url: "https://medium.com/@johnssimon_6607/getting-access-to-disabled-hidden-features-with-the-help-of-burp-match-and-replace-e1d7b70d131e"
authors: ["Johns Simon (@Johnssimon22)"]
bugs: ["Broken authorization"]
publication_date: "2019-11-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4916
scraped_via: "browseros"
---

# Getting access to disabled/hidden features with the help of Burpsuite Match and Replace settings

Getting access to disabled/hidden features with the help of Burpsuite Match and Replace settings
Johns Simon
Follow
2 min read
·
Nov 27, 2019

351

1

A few months ago, During my bug bounty hunting, I came across a Company that lets other developers create API documentation similar to what swagger does and the company provides a 12 day free trial for the developers using their services. Apart from creating documentation they also allow it to be published on their domain.

As I told they restrict users from accessing project management features after a 12 days free trial period. Only users who pay are able to access the project they have created and even publish it publicly.

Now the issue came when I am able to access the project even after the 12 day trial period. The restriction they impose was by client-side rather than server-side. I came to know about this by examining how the web page contents get loaded each time when the web page was refreshed. When the web page was refreshed the page showed the project management at first in a millisecond and redirected to a home page.

Now that I know it is some client-side code doing the thing.I now need to check which API response does the client side code uses for displaying the data on the web page

I came across this API

Request

GET /api/v2/projects/{projectname}/listings HTTP/1.1
Host: [redacted .com]

Get Johns Simon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

XSRF-TOKEN: xxxxxxx

Response

{“dash”:false,”log”:false,”apikey”:false,”stage”:false,”appearance”:true,”documentation”:true}

So if you notice the response body some of them were set to false, while some were set to true.

Now burp to the rescue!!!. Burp has match and replace settings which is a nice little feature that lets you replace the request or response body headers automatically. This comes in handy in numerous attacks and has helped me over the past years in bug bounty. Especially when looking for blind XSS

Press enter or click to view image in full size

Now that burp replaces all response body having the keyword “false” to “true”
i can access project management page and continue to use it for lifetime.
The vulnerability was fixed by the company and rewarded me with a bounty

You could generate your own match and replace script and exported it on the burp suite.Here is a python script to generate your own match and replace the script.
https://github.com/Leoid/MatchandReplace

Thanks @Hamid Mohammad for making it easy to generate custom scripts
