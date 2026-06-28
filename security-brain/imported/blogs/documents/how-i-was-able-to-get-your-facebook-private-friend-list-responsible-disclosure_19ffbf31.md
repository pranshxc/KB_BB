---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-01_how-i-was-able-to-get-your-facebook-private-friend-list-responsible-disclosure.md
original_filename: 2019-04-01_how-i-was-able-to-get-your-facebook-private-friend-list-responsible-disclosure.md
title: How I was able to get your facebook private friend list [Responsible Disclosure]
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 19ffbf3159312692094a5932f9ce93e950ec0fd7987c9ecd3ad74ac811e794bb
text_sha256: 2f007ff96da97989f22df28dd99051ded94d0c3ab075bb2c43bce4ab4d20305f
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to get your facebook private friend list [Responsible Disclosure]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-01_how-i-was-able-to-get-your-facebook-private-friend-list-responsible-disclosure.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `19ffbf3159312692094a5932f9ce93e950ec0fd7987c9ecd3ad74ac811e794bb`
- Text SHA256: `2f007ff96da97989f22df28dd99051ded94d0c3ab075bb2c43bce4ab4d20305f`


## Content

---
title: "How I was able to get your facebook private friend list [Responsible Disclosure]"
url: "https://medium.com/@rajsek/how-i-was-able-to-get-your-facebook-private-friend-list-responsible-disclosure-91984606e682"
authors: ["Raja Sekar Durairaj"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "10,000"
publication_date: "2019-04-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5335
scraped_via: "browseros"
---

# How I was able to get your facebook private friend list [Responsible Disclosure]

Press enter or click to view image in full size
How I was able to get your facebook private friend list [Responsible Disclosure]
Raja Sekar Durairaj
Follow
3 min read
·
Apr 1, 2019

453

3

A User Data Disclosure occurs when personal information held by an organisation is lost or subjected to unauthorised access or disclosure. in general it is a security incident in which sensitive, protected or confidential data is copied, transmitted, viewed, stolen or used by an individual unauthorized to do so.

As per facebook help page, “People You May Know” is a feature that can help people find friends on Facebook. People You May Know suggestions come from things like,

* Having friends in common, or mutual friends. This is the most common reason for suggestions.

* Being in the same Facebook group or being tagged in the same photo.

* Your networks (example: your school, university or work) and etc.

Facebook friends list Privacy

By default, the Friends section of your profile is public. Facebook has Privacy option to limit the sharing of those infomation to others ( Public, Friends, only me etc) Source: FB help link

About the Issue:

“This issue could have allowed a malicious user to infer a victim’s private social graph by entering victim’s confirmed phone number during user registration.”

Steps followed to break FB privacy restrictions
Create a new FB account with the victim’s mobile number. After completing sign up it will redirect to “SMS confirmation” page

2. Since the attacker doesn’t have the victim’s SMS, the attacker needs to click on the “Update Contact info” button and entered their own new email id “hack@rajsek.com”

Get Raja Sekar Durairaj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Complete the account verification by entering the code, which the attacker received via email.

4. Then navigate to this page https://www.facebook.com/friends/requests/?fcref=swpsa or curl below request will disclose the most of the victim’s private friends to attacker.

curl ‘https://www.facebook.com/gettingstarted/?step=friend_requests' -H ‘authority: www.facebook.com' -H ‘referer: https://www.facebook.com/gettingstarted/' -H ‘cookie: xxxx’ — compressed

5. There are also couple of other URLs that disclose the private friends list to the attacker.

Disclosed Victim’s Friend
Video POC:
Thanks Sameer Rao for allowing me to add this video
Conclusion:

This issue could have allowed a malicious user to infer a victim’s private social graph by entering victim’s confirmed phone number during user registration.”

The combination of two useful features (suggesting the friends, User registration) made this data leak possible.

Timeline
Oct 16, 2018: First disclosure to Facebook
Mar 20, 2019: Facebook awarded 10000 USD

Reference

https://rpadovani.com/facebook-responsible-disclosure
Thank you for reading this post

Before you go:

Be sure to clap and follow me on medium ️👏️️
Follow us: X | LinkedIn 🚀 🧑🏻‍💻
