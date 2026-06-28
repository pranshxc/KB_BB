---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-16_bypassing-the-2fa-mfa-an-easy-win.md
original_filename: 2023-04-16_bypassing-the-2fa-mfa-an-easy-win.md
title: Bypassing the 2FA /MFA — An Easy win
category: documents
detected_topics:
- mfa
- command-injection
- otp
tags:
- imported
- documents
- mfa
- command-injection
- otp
language: en
raw_sha256: d263da0b95d2365c0dcdd71667345af2928fb96950f7cd8390d5e7e8b759379a
text_sha256: 9b4ffd3829121a66f78db667e47da6713e6db70b647101a30ad471c530c12064
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing the 2FA /MFA — An Easy win

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-16_bypassing-the-2fa-mfa-an-easy-win.md
- Source Type: markdown
- Detected Topics: mfa, command-injection, otp
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `d263da0b95d2365c0dcdd71667345af2928fb96950f7cd8390d5e7e8b759379a`
- Text SHA256: `9b4ffd3829121a66f78db667e47da6713e6db70b647101a30ad471c530c12064`


## Content

---
title: "Bypassing the 2FA /MFA — An Easy win"
url: "https://medium.com/@mehtashobhit98/bypassing-the-2fa-mfa-an-easy-win-9b059bf0ac75"
authors: ["Shobhit Mehta"]
programs: ["MathWorks"]
bugs: ["2FA / MFA bypass"]
publication_date: "2023-04-16"
added_date: "2023-04-29"
source: "pentester.land/writeups.json"
original_index: 1262
scraped_via: "browseros"
---

# Bypassing the 2FA /MFA — An Easy win

Bypassing the 2FA /MFA — An Easy win
Shobhit Mehta
Follow
2 min read
·
Apr 16, 2023

73

Hello Readers, Today I am going to tell how was I was to bypass the 2FA protection for a product based company main login page. I hope this blog help you learn something new and apply to your bug hunting techniques.

Press enter or click to view image in full size

I was hunting on a VDP called : MathWorks , This is a company which makes Matlab software.

In the program there was nothing special mentioned about the in scope and out scope so started with the Login page of the main website.

After spending some time with the application I figured out that they have put new feature of 2FA/MFA for their users for better security. I started to dig more into that functionality as it was a new thing that they have rolled out.

I started playing with 2FA/MFA thing and figured out that you can setup the 2FA/MFA in three ways :-

Using Google Authenticator App
Receiving code via text message on mobile
Receiving code via email on your registered mail id.

I choose the email method and setup my 2FA/MFA with the code I got on email and logged out.

Get Shobhit Mehta’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now When I login again I was asked the code which I received on my email and instead of putting right code, I thought of why not to brute this with random codes and check the behaviour of application. I immediately put the request in intruder and generated random 6 digit codes (check below screenshot)

Press enter or click to view image in full size
Security Token
Random payloads

The response I got was completely eye-opener. After 200+ request the application log you in without the actual right 2FA/MFA token.

So I was logged into my account by just hitting the random 6 digit codes for more than 200 times.

I reported that to the team and they were also surprised of this beahaviour. I was not awarded any bounty for this but I got an acknowledgement letter from The MathWorks (check it here)

Press enter or click to view image in full size

Thank You Reading.
