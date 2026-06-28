---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-24_two-factor-authentication-bypass-50-.md
original_filename: 2020-04-24_two-factor-authentication-bypass-50-.md
title: Two Factor Authentication Bypass [ $50 ]
category: documents
detected_topics:
- mfa
- otp
- command-injection
tags:
- imported
- documents
- mfa
- otp
- command-injection
language: en
raw_sha256: 36e09c510c56be17e711d6063bc3ab4a850fcf88176679aeca675a4b4d1bc668
text_sha256: 3d43db38844dc9b22d484d4e4b1a52c8be8b6836b3ce2eec1d1cb85aef7de4ae
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Two Factor Authentication Bypass [ $50 ]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-24_two-factor-authentication-bypass-50-.md
- Source Type: markdown
- Detected Topics: mfa, otp, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `36e09c510c56be17e711d6063bc3ab4a850fcf88176679aeca675a4b4d1bc668`
- Text SHA256: `3d43db38844dc9b22d484d4e4b1a52c8be8b6836b3ce2eec1d1cb85aef7de4ae`


## Content

---
title: "Two Factor Authentication Bypass [ $50 ]"
url: "https://medium.com/@aungpyaehackeronetester/two-factor-authentication-bypass-50-5b397e68cfed"
authors: ["Aung Pyae Ko Ko (@BlcKVRtuL1)"]
bugs: ["2FA / MFA bypass"]
bounty: "50"
publication_date: "2020-04-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4635
scraped_via: "browseros"
---

# Two Factor Authentication Bypass [ $50 ]

Aung Pyae Ko Ko
Follow
2 min read
·
Apr 25, 2020

81

1

Two Factor Authentication Bypass [ $50 ]

Hi everyone.Today i want to share bug bounty experience from my private program .

I was checking for some vulnerability.

» NOTHING FOUND »

I think let’s try to next time.I noticed Two Factor Authentication — ON/OFF in some strange json endpoint.I decided this can be vulnerable and then that I try to bypass.

Two Factor Authentication is a need 5 digit OTP.I enter the 5 digit OTP are not real value.(I try to ON the Two Factor Authentication)

PUT /api/sts/v2/settings?client_request_id=b8e69342–2e33–4f53-b323-e9186c97e995 HTTP/1.1
Host: www.target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: application/json, text/plain, /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.target.com/settings/account
Content-Type: application/json;charset=utf-8
Content-Length: 105
Connection: close

Get Aung Pyae Ko Ko’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

{“Settings”:{“DataType”:”Integer”,”DomainName”:”services”,”ResourceName”:”TwoFactor”,”SelectedValue”:1},”VerificationDetails”:{“VerificationId”:”f2315d56-a523–42ea-9999–4de187ec5d07",”VerificationCode”:”12345"}}

Press enter or click to view image in full size

Now i found that in this request.Simply forward this request and went to get response.I only get message Invalid verification code in the response.I Check it out.

Press enter or click to view image in full size

Wait!!.I know that this.Two Factor Authentication is based SelectedValue(ON is 1 and OFF is 2).Why you to need in other json endpoint(VerificationDetails).Because SelectedValue is include in Settings.Therefore i remove VerificationDetails to the json endpoint and then send the request.

Hola !! I was able to Two Factor Authentication ON/OFF without verifying the OTP.

I report to private program and i got Informative.

Now reopen and i got $50

Press enter or click to view image in full size

Sorry for my poor English.

I am noob. See you next bug.
