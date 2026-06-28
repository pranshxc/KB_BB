---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-06_exposing-millions-of-voter-id-card-users-details.md
original_filename: 2022-07-06_exposing-millions-of-voter-id-card-users-details.md
title: Exposing Millions of Voter ID card users’ details.
category: documents
detected_topics:
- idor
- rate-limit
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- idor
- rate-limit
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: 7c021cc3fcadf6898511cc27813bcf14ca56a67c870546774a230da8a3ef3afc
text_sha256: 9b770b24493697dd7b227e0e782da3d02bad71b778f4aef2729ca35a33acaadf
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Exposing Millions of Voter ID card users’ details.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-06_exposing-millions-of-voter-id-card-users-details.md
- Source Type: markdown
- Detected Topics: idor, rate-limit, command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `7c021cc3fcadf6898511cc27813bcf14ca56a67c870546774a230da8a3ef3afc`
- Text SHA256: `9b770b24493697dd7b227e0e782da3d02bad71b778f4aef2729ca35a33acaadf`


## Content

---
title: "Exposing Millions of Voter ID card users’ details."
url: "https://infosecwriteups.com/exposing-millions-of-voter-id-card-users-details-8a993c9a5d35"
authors: ["Aziz Al Aman (@nxtexploit)"]
programs: ["CERT-In"]
bugs: ["IDOR", "OTP bypass", "Account takeover", "Logic flaw"]
publication_date: "2022-07-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2485
scraped_via: "browseros"
---

# Exposing Millions of Voter ID card users’ details.

Aziz Al Aman
 highlighted

Exposing Millions of Voter ID card users’ details.
Aziz Al Aman
Follow
4 min read
·
Jul 7, 2022

200

1

Press enter or click to view image in full size

Hi, Everyone. hope you’re well. I’m Aziz. Through this write-up, I will share some security issues I’ve found on the official Voter ID card maintaining platform http://nvsp.in. I was filling out a correction form for my mom’s card, I’m not really interested in finding bugs on gov websites :`) that moment burpsuite was running in the background and I thought let's have a try. After spending half an hour I found some critical issues that I’m going to share. All these issues are already fixed by the government.

Get Aziz Al Aman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In India, a Voter ID card is an identity document issued by the Election Commission of India to adult domiciles of India who have reached the age of 18, which primarily serves as an identity proof for Indian citizens while casting their ballot in the country’s municipal, state, and national elections. More than 780 million Voter IDs are active at present.

1st bug : Bruteforcing valid Voter IDs and extracting details (IDOR / BOLA)

While registering a new account it shows two options “I have EPIC number” and “I don’t have EPIC number”. EPIC stands for Electors Photo Identification Card and the EPIC number is nothing but Voter ID no. If we chose we don’t have a Voter ID number then they will give you an option to add after registering on the portal. After registration, I tried to add any random EPIC no. with my account but it show it's not valid. So I sent that HTTP request to burp intruder for brute-forcing.

Press enter or click to view image in full size
sending an HTTP request for an invalid ID

A Voter ID also known as EPIC number is an alphanumerical ID, it contains three Alphabets at starting and seven numbers i.e. WRI2345678, RDH2345678, DTN2345678, YCV2345678, NLN2345678, XMB2345678, etc. These three alphabets are Not random alphabets, you can find similar IDs with similar these three alphabets in beginning but the rest seven digits are different.

Press enter or click to view image in full size

I added the payload position on these seven-digit numbers on`Epic_no=` parameter i.e “ Epic_no=WRI$2345678$ ” (as you can see in the below screenshot.)

Press enter or click to view image in full size
Adding payload position

Surprisingly there is no limitation implemented in the backend and I was able to send unlimited requests without getting blocked by firewall. As a result backend server responding 302 redirections for every valid voter ID. (As shown in the screenshot below)

Press enter or click to view image in full size
responding 302 for every valid voter ID

Then I wrote a python script that will brute force the values and give output all valid voter_IDs for me.

Now I have valid Voter IDs of random persons then, I added these IDs with my profile under “/Account/MyProfile”. Then there is an option under the “/forms/”section which is form001 and this form is already filled with Name, father’s name, address, Date of birth, etc. according to that valid EPIC ID added to my profile.

Press enter or click to view image in full size
Extracted details of a random Person
2nd bug : Account takeover (OTP bypass)

On the profile details updating section I was trying to add another user's number. So I created another account for it. But there was an OTP implanted there, and I tried to brute-force it but it didn’t work :( I remember reading an article last year, you can read it here, where the author just added 0 after intercepting the request. And I did the same thing here on OTP parameter and it worked :)

Press enter or click to view image in full size
intercepting traffic while OTP is verifying
Press enter or click to view image in full size
Changed the OTP value to zero

After bypassing I thought it just can register the victim’s number then I’ll reset the password, But surprisingly on replacing the victim’s number my profile data automatically changed with the victim’s details, And I can own his account.

Press enter or click to view image in full size
3rd bug : Delete/remove any random user’s Voter ID card Permanently (Logic flaw)

From the 1st bug, we can get and add any random user’s Voter ID to our account, From that on the home page there is an option for “Deletion of Enrolment”. And nothing to be needed after an attacker added any random Voter ID on his profile section. then he can easily delete any random user’s Voter ID permanently.

Press enter or click to view image in full size
An attacker can delete any random user’s card permanently

I reported these three issues to vdisclose@cert-in.org.in and they fixed these issues.

I hope you liked this article, If you have any questions then you can dm me on Twitter: https://twitter.com/nxtexploit

Thanks for reading,
