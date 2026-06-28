---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-10_bypassed-facebook-phone-number-security.md
original_filename: 2017-02-10_bypassed-facebook-phone-number-security.md
title: Bypassed Facebook Phone Number Security
category: documents
detected_topics:
- idor
- access-control
- command-injection
- password-reset
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- access-control
- command-injection
- password-reset
- rate-limit
- automation-abuse
language: en
raw_sha256: ac1c98c14dad6d826c137001800a28472a7bbf0adafba54c6bb9cde790b729de
text_sha256: d0c5c18a55fe39fb1f6bf943c1487c3bf873b6a3f4c9d81fa14a48b26706682a
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassed Facebook Phone Number Security

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-10_bypassed-facebook-phone-number-security.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, password-reset, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `ac1c98c14dad6d826c137001800a28472a7bbf0adafba54c6bb9cde790b729de`
- Text SHA256: `d0c5c18a55fe39fb1f6bf943c1487c3bf873b6a3f4c9d81fa14a48b26706682a`


## Content

---
title: "Bypassed Facebook Phone Number Security"
url: "https://medium.com/@zahidali_93675/bypassed-facebook-phone-number-security-9e2d34dc063b"
authors: ["Zahid Ali"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw", "Information disclosure"]
bounty: "3,000"
publication_date: "2017-02-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6227
scraped_via: "browseros"
---

# Bypassed Facebook Phone Number Security

Zahid Ali
Follow
5 min read
·
Feb 11, 2017

18

B
ypassed Facebook Phone Number Security

=======================================

Enumeration vulnerabilities which demonstrate that a given e-mail address or mobile phone number is tied to “a Facebook account” are not eligible under the bug bounty program. This is true whether the endpoint returns only confirmed items, or both confirmed and unconfirmed. In absence of the user ID that the e-mail/mobile number is linked to, this behavior is considered extremely low risk.

Vulnerabilities which allow an attacker to determine which specific user ID that an e-mail address or mobile phone number is linked to MAY be rewarded under the bug bounty program, but ONLY if they do this in violation of appropriate privacy settings on the specific user account regarding who can look-up the user via the e-mail/mobile number.

=======================================

I discovered this vulnerability when i was testing “FACEBOOK” account recovery form. (However, that form was only available for the users who registered their Facebook ID with phone numbers.)

Description and Impact:

If a user sets privacy to “Who can look you up using the phone number you provided?” (Friends Only). Attacker was able to see which specific user ID that a phone number is linked with the help of that account recovery form.

Reproduction Steps:

Go to Forgotten password?
Type a phone number where facebook id is linked.
Now click “No longer have access to these”
type your new email twice
fill up form with fake information and “Submit”
Support Dashboard will open where self-identified uid is visible for the attacker.

Screen shots :

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Facebook accepted my bug and awarded me 1500USD for that bug.

After successfuly patched and got a bounty i disclosed this bug with my friends.

But i was curious about that form so again i tried to test that form and i see that vulnerability is patched only in support dashboard and still i am able to exploit this bug with changed behaviour.

“Getting user id in the email in the first attempt they patched the bug but server still sending user id of that specific phone number if we do 2nd attempt with the same email”

Steps to reproduce same bug with change behaviour:

Go to Forgotten password?
Type a phone number where facebook id is linked.
Now click “No longer have access to these”
type your new email twice
fill up form with fake information and “Submit”
Support Dashboard will open but this time self-identified UID is not visible in the support dashboard. (Because bug has been patched)

7. Check the email but user id is not there also.

8. Go to Forgotten password? (Again)

9. Type same phone number.

10. repeat same steps with same email we did it in first bug.

Get Zahid Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Screen shots:

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

“I got reply from Facebook but in this reply i am not getting user id of that number. Now Lets do 2nd attempt.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

This time i am getting self identified uid: in the email (Highlighting)

:)

I reported to Facebook and got a reply from admin Reginaldo:

========================================

Hi Zahid,

Ah, I see what’s happening here. Can you still reproduce this? It has the same root cause as your other report #314709118, so the fix for #314709118 should have fixed this one too. As we get a lot of submissions, we’ll close this ticket while we wait for more info from you. If you do find that the issue still reproduces, please reply to this email and the ticket will re-open and we can take another look.

Thanks for your submission.

Reginaldo
Security
Facebook

========================================

I replied yes i am still able to reproduce this bug. And then i got a reply from admin Neal

========================================

Hi Zahid,

We have looked into this issue and believe that the vulnerability has been patched. New tickets going forward should not contain the information. Please follow up with us if you believe that the patch does not resolve this issue.

Neal
Security
Facebook

========================================

I replied “Yes bug has been patched now”

I wasn’t expect a bounty for that report i thought they will merge the reports.

But then i got a reply from admin Neal

========================================

Hi Zahid,

Awesome, thanks for confirming! We will be in touch about bounty information in the next few days.

Thanks,

Neal
Security
Facebook

========================================

And then got awarded again for the same bug with changed behaviour.

Press enter or click to view image in full size

That was a surprise bounty for me :)
