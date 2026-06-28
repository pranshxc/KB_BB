---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-24_bypass-apples-redirection-process-with-the-dot-character.md
original_filename: 2022-12-24_bypass-apples-redirection-process-with-the-dot-character.md
title: Bypass Apple’s redirection process with the dot (“.”) character
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 77a415bc9a7554e46d534dd7d961eeab88ca66cf01771376850f70c6f4e27bdd
text_sha256: 257e421e7262642e2148913e0324f9a2170cf193cb5c62a7c0c507e4512b1005
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Apple’s redirection process with the dot (“.”) character

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-24_bypass-apples-redirection-process-with-the-dot-character.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `77a415bc9a7554e46d534dd7d961eeab88ca66cf01771376850f70c6f4e27bdd`
- Text SHA256: `257e421e7262642e2148913e0324f9a2170cf193cb5c62a7c0c507e4512b1005`


## Content

---
title: "Bypass Apple’s redirection process with the dot (“.”) character"
url: "https://infosecwriteups.com/bypass-apples-redirection-process-with-the-dot-character-c47d40537202"
authors: ["can1337 (@canmustdie)"]
programs: ["Apple"]
bugs: ["Open redirect"]
publication_date: "2022-12-24"
added_date: "2022-12-27"
source: "pentester.land/writeups.json"
original_index: 1738
scraped_via: "browseros"
---

# Bypass Apple’s redirection process with the dot (“.”) character

Bypass Apple’s redirection process with the dot (“.”) character
can1337
Follow
3 min read
·
Dec 24, 2022

422

2

Hi guys, I have been gone for a while but now I’m back and here is a new write-up post. Today, I’m gonna show you the Open Redirection vulnerability I found at Apple’s subdomain using the dot character.

I don’t have a permission to publish this subdomain so I won’t publish it but you can think it as a forum area where users are active. So I’ll call it as “redacted” and let’s get started!

First of all, when we visit to the redacted.apple.com subdomain, there is a login screen here and logging in is quite simple.

Press enter or click to view image in full size

As you can see in the picture, the ?path= parameter is set to redirect to another page in the same subdomain in the section for choosing a nickname for users who log in for the first time.

This process will probably be redirected to “/welcome?login=true” for first time users after all prerequisites have been completed correctly.

As I guessed, the redirect was redirecting to the specified page after choosing the username and uploading the avatar. Of course I tried some payloads here primarily like https://evil.com & //evil.com etc.

Press enter or click to view image in full size

Actually, what was interesting to me here was that after using the //evil.com payload, the response was /evil.com with a single ‘/’ character.
If you are using a payload like ?path=//evil.com then the following is expected: redacted.apple.com//evil.com
However, the response I got is as follows: redacted.apple.com/evil.com

Press enter or click to view image in full size

In this case, I thought the only ‘/’ appended to the end was due to my payload, and I thought of just typing evil.com

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The behavior I actually expected was to be redirected to a non-existent redacted.apple.comevil.com domain, but instead I returned to “/welcome?login=true”. For most parameters it would be okay to simply navigate to evil.com in the subdomain. (?path=evil.com > x.apple.com/evil.com)

Finally an idea came to my mind and I hadn’t seen it anywhere before. I was thinking purely theoretically and was surprised to see that it was possible at Apple.

Press enter or click to view image in full size

If we set the payload to .evil.com (ie ?path=.evil.com), “.” character will be appended to the end of redacted.apple.com and this making it a subdomain of evil.com.

Press enter or click to view image in full size

And here is the result we expect. Adding a dot character in front of the payload means that the “/” character is missing in some cases. This makes redacted.apple.com a subdomain of evil.com

Press enter or click to view image in full size
https://support.apple.com/en-us/HT201536

This vulnerability was fixed by team and I was added the Apple Hall of Fame.

That’s all for now. Thanks for reading this far and I hope you liked it!

You can follow me on twitter: https://twitter.com/canmustdie

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
