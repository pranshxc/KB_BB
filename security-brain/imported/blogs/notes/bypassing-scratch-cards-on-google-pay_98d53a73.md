---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-22_bypassing-scratch-cards-on-google-pay.md
original_filename: 2018-11-22_bypassing-scratch-cards-on-google-pay.md
title: Bypassing Scratch Cards On Google Pay
category: notes
detected_topics:
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- notes
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: 98d53a73250036e8f91fe40364ea6bbda2e6e7559892ef670680f29844fd830d
text_sha256: 814ba609c9f58eb9c503ac2b235217e6b71d91c9ca2f25545cceee18ec7f5b1c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Scratch Cards On Google Pay

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-22_bypassing-scratch-cards-on-google-pay.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `98d53a73250036e8f91fe40364ea6bbda2e6e7559892ef670680f29844fd830d`
- Text SHA256: `814ba609c9f58eb9c503ac2b235217e6b71d91c9ca2f25545cceee18ec7f5b1c`


## Content

---
title: "Bypassing Scratch Cards On Google Pay"
url: "https://medium.com/@pratheesh.p.narayanan/bypassing-scratch-cards-on-google-pay-8915d5423385"
authors: ["Pratheesh P Narayanan"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2018-11-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5568
scraped_via: "browseros"
---

# Bypassing Scratch Cards On Google Pay

Bypassing Scratch Cards On Google Pay
Pratheesh P Narayanan
Follow
3 min read
·
Nov 22, 2018

14

Hi There,

So,this story is all about how I was able to Bypass Scratch Cards On Google Pay .

Press enter or click to view image in full size

Intro…

As you all know Google offers scratch cards as a reward for using their payment system Google Pay. Recently,they had rolled out scratch cards for inviting friends for joining Google Duo.Once a person sign-up for the service,you get a scratch card on your Google Pay.You can get upto 30 cards during the offer period.

About the bug..

I don’t consider myself as an expert in security field.Nonetheless,I hope this report might help you at some point of time.

As said,you could earn rewards for inviting friends to try out Google Duo.As per the T&C of the offer,this is supposed to work with only Indian Users who signs-up with a +91 mobile number and have a valid email address linked to the Google Pay application.Both you and the person joining via your link must have Google Pay account for this offer to work.

Interestingly,I found that the offer can be bypassed by a user by using Virtual Numbers which can be generated easily by using applications like Text Now,2nd Line etc…

So,How Did I earn 30 scratch cards without referring anyone?

Get Pratheesh P Narayanan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1… Create a Valid Google Duo Account and generate an invite link.

2.. Delete Data of the google duo application.

3… Use the previously generated link to sign-up for the Duo application using the virtual number.Note that using virtual numbers should have been made the offer unavailable,But this seemed to work.

4… Sign up using the virtual number and link your own Google Pay account to this account. Note that you are not allowed to link multiple Duo accounts to the same Google Pay account,but in this scenerio,this too seemed to work.

5… You can repeat this process upto 30 times to earn 30 scratch cards.All this by using virtual numbers and your own Google Pay account.

Generating Duo account
Rewards Earned

Few days after sending the report,I was surprised to see many tutorials on Youtube by random creators exploiting the same vulnerability.So I knew I was not the only person who was aware of this issue.As expected my report to VRP team was a duplicate.

Press enter or click to view image in full size
As Expected :(

That’s all for this report.Thanks for your time here :)
