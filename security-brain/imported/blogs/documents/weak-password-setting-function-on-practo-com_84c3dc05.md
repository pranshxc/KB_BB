---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-09_weak-password-setting-function-on-practocom.md
original_filename: 2020-10-09_weak-password-setting-function-on-practocom.md
title: Weak Password Setting function on practo.com
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 84c3dc05ddf4e8af5177d549603b278823160f5149d5c67799a57bb6ca043e76
text_sha256: cd9d9fe8ecd5177a99f9f06bd3bab7060757111c9231964c3a7f6cffae7611d5
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# Weak Password Setting function on practo.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-09_weak-password-setting-function-on-practocom.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `84c3dc05ddf4e8af5177d549603b278823160f5149d5c67799a57bb6ca043e76`
- Text SHA256: `cd9d9fe8ecd5177a99f9f06bd3bab7060757111c9231964c3a7f6cffae7611d5`


## Content

---
title: "Weak Password Setting function on practo.com"
url: "https://medium.com/@aakashadhikari786/weak-password-setting-function-on-practo-com-79df78245b81"
authors: ["dark-haxor"]
programs: ["Practo"]
bugs: ["Broken authorization"]
publication_date: "2020-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4206
scraped_via: "browseros"
---

# Weak Password Setting function on practo.com

Weak Password Setting function on practo.com
dark-haxor
Follow
2 min read
·
Oct 9, 2020

5

This is my bug bounty story……so lets get started with the bug without further talking.

The target was Practo.com

So I haven’t set my password when i came up with this issue (I logged in with OTP) . When Itried to login via browser i was prompted for setting password and this request was in play.

Press enter or click to view image in full size
Request
Press enter or click to view image in full size
Popup asking us to set password

Enter some value of both the fields and set password …we now have a password for our account.

Now let exploit.

If we try to change the password we need the old password.

Press enter or click to view image in full size
we need old pass to change

Lets bypass this…..

Get dark-haxor’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

From the above request we can see that the link for asking us setting new password is

https://accounts.practo.com/fill_password?create_password=***REDACTED***>https://accounts.practo.com/fill_password?create_password=***REDACTED***

If we go back to this link we can see this

Press enter or click to view image in full size

I was surprised !! This link should have expired but its still active. I put new password and the password was changed without the old password.

Just change [my_mobile_no] to your registered mobile no. Thats it!!!

Reported on : Oct 1, 2020, 12:12 AM

Response : Oct 9, 2020, 12:36 AM

Press enter or click to view image in full size
Response from the developer

Wont be fixed but they will change the feature :)

No hall of fame will be provided.
