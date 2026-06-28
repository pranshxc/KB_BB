---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-09_how-to-confirm-a-google-users-specific-email-address-bug-bounty-submission.md
original_filename: 2017-08-09_how-to-confirm-a-google-users-specific-email-address-bug-bounty-submission.md
title: How to confirm a Google user’s specific email address (Bug Bounty Submission)
category: documents
detected_topics:
- rate-limit
- command-injection
- business-logic
tags:
- imported
- documents
- rate-limit
- command-injection
- business-logic
language: en
raw_sha256: b90812c1f66c2a550fd5344e06a9e1d356a4812454664e30606de5dc1c4fa854
text_sha256: 36a7a4f87452c8ffb147073485bc8227a4afbdb3c49ca1de2e984737d9540da0
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How to confirm a Google user’s specific email address (Bug Bounty Submission)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-09_how-to-confirm-a-google-users-specific-email-address-bug-bounty-submission.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `b90812c1f66c2a550fd5344e06a9e1d356a4812454664e30606de5dc1c4fa854`
- Text SHA256: `36a7a4f87452c8ffb147073485bc8227a4afbdb3c49ca1de2e984737d9540da0`


## Content

---
title: "How to confirm a Google user’s specific email address (Bug Bounty Submission)"
page_title: "How to confirm a Google user's specific email address (Bug Bounty Submission) - Tom Anthony"
url: "http://www.tomanthony.co.uk/blog/confirm-google-users-email/"
final_url: "https://www.tomanthony.co.uk/blog/confirm-google-users-email/"
authors: ["Tom Anthony (@TomAnthonySEO)"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2017-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6131
---

I recently reported an issue to Google, which allows an attacker to confirm whether a visitor to a web page is logged in to any one of a list of _specific_ Google accounts (including GSuite accounts). It is possible to check about 1000 email addresses every 25 seconds. Google have confirmed this as working as intended, and not considered a bug.

You can test it out yourself on this [demo page](https://www.tomanthony.co.uk/google_leak/).

Firstly, a video of a proof of concept, where I identify an account (myself) against a list of 20 accounts:

**Method**

Iâ€™ve previously written about identifying [whether a user is logged in to a certain social network](https://www.tomanthony.co.uk/blog/detect-visitor-social-networks/), and this attack is a variation of that method (albeit more serious, IMHO).

Google login pages often pass a `continue` parameter in the URL that is used to redirect a user to their intended destination after they complete login. However, if you are already logged in then you just get redirected immediately to the URL specified in the `continue` parameter.

This fact can be abused to craft a URL that will redirect users who are logged in to an image file, and challenge users who are not logged in with a login page. If you now use this URL as the `src` element in an `img` tag, you can use the Javascript `onload` and `onerror` functions to determine whether the image loaded correctly or not.

If the image loaded, then the user is logged in, and if it errored then the user is not logged in. This is an known issue but has limited capacity to cause any sort of problem.

However, Google succumbs to a far more dangerous variation where the attacker can also supply an additional parameter specifying an email address. The redirect then fires _if the email matches_ , but otherwise not.

At this point an attacker can just dynamically create loads of image tags (no need to even add them to the page, you can do it without attaching them to the DOM) with `onload` attributes and wait for a match. In my tests I could check about 1000 emails every 23-24 seconds or so. If a user is on your site for a couple of minutes then you could check many thousands of possible emails.

Combined with other ways to partially identify users â€” from using their geography via IP, targeting them with very-targeted (demographically or otherwise) social ads, identifying their corporate network or many other methods, you could dynamically load lists of targets. You can then match these people against requests and record their IP address, location, device, and all sorts of other information.

You may then use that knowledge to setup the attack above to then do some dynamic spear-phishing.

**Disclosure Timeline**

  * 14th July – I reported this to the security team via their form.
  * 17th July – I heard back it was triaged and awaiting attention.
  * 18th July – The team came back to me and asked me what my suggestions for handling this would be.
  * 18th July – I went back to them with my suggestion for some sort of nonce or salted hash of the email such that a the redirect only worked with that hash and email combo, to stop blind attacks.
  * 19th July – The security team confirms they are filing this as a bug.
  * 21st July – I sent over a copy of my blog post as additional explanation.
  * 9th August – Google team lets me know, after discussion, this is intended behaviour. They suggested there may be rate limiting at a higher rate (I’ve not tried to confirm), and don’t consider it a problem. No action to be taken.

This bug is quite specific, in that you need to have a target or list of target victims. However, I did think it could be quite bad if used.

If you missed it you can test this out here: [demo page](https://www.tomanthony.co.uk/google_leak/).

Lastly, a big thanks and shout out to the Google security team, they were responsive, friendly and communicative. 🙂

[Hacker News Discussion](https://news.ycombinator.com/item?id=14970472)
