---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-22_bugbounty-how-i-was-able-to-see-other-users-payments-in-a-travel-application-ido.md
original_filename: 2020-09-22_bugbounty-how-i-was-able-to-see-other-users-payments-in-a-travel-application-ido.md
title: '#Bugbounty- “How I was able to see other users Payments in a travel application”
  — IDOR #800$'
category: documents
detected_topics:
- idor
- command-injection
- information-disclosure
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- information-disclosure
- mobile-security
language: en
raw_sha256: ffbbcf63df45d0959ea6e1abf362a23ebc906aab86bca053e4bd3baf34ac2c3f
text_sha256: a41c9b449a8c77958012a666725a2f552575bcaf073d6fb9afb5e36c4abb372d
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# #Bugbounty- “How I was able to see other users Payments in a travel application” — IDOR #800$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-22_bugbounty-how-i-was-able-to-see-other-users-payments-in-a-travel-application-ido.md
- Source Type: markdown
- Detected Topics: idor, command-injection, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `ffbbcf63df45d0959ea6e1abf362a23ebc906aab86bca053e4bd3baf34ac2c3f`
- Text SHA256: `a41c9b449a8c77958012a666725a2f552575bcaf073d6fb9afb5e36c4abb372d`


## Content

---
title: "#Bugbounty- “How I was able to see other users Payments in a travel application” — IDOR #800$"
url: "https://medium.com/@haxor8595/bugbounty-how-i-was-able-to-see-other-users-payments-in-a-travel-application-idor-800-2060db62cbbe"
authors: ["ganiganesh (@ganiganeshss79)"]
bugs: ["IDOR", "Information disclosure"]
bounty: "800"
publication_date: "2020-09-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4243
scraped_via: "browseros"
---

# #Bugbounty- “How I was able to see other users Payments in a travel application” — IDOR #800$

#Bugbounty- “How I was able to see other users Payments in a travel application” — IDOR #800$
ganiganeshss79
Follow
2 min read
·
Sep 22, 2020

186

1

Let me thank all the bug bounty hunters over there who are creating great content and inspiring a lot of people like me.

Thank You, community folks, @akhilreni_hs @stokfredik @hakluke @farah_hawa01 @dhakal_ananda @adityashende17 @bugcrowd @rakesh_3895

Hi Guys,

Myself Ganesh, I am a security analyst at WesecureApp and a part-time bug bounty hunter. I recently got an invite for a Travel application.

The application allows users to make a booking at hotels /Flights so upon users filling up necessary information they will be redirected to the Payment Gateway there are couple options for the user to complete payment. I have selected the Credit card option and captured the request using a burp proxy.

Press enter or click to view image in full size
Request

And I have observed the application is making redirection to “*redacted.com”. I tried changing all values in the request body parameters out of curiosity I tried brute-forcing at “req_reference_number” and was able to list out other users payments.

Get ganiganeshss79’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Lucky me :)

Press enter or click to view image in full size

I was able to view other user’s sensitive information such as social security number, Passport Number, Name, Valid Ticket ID’s.

Though, it’s a P1 issue team has listed it out as P2 :)

Thanks for reading my blog :)

Twitter : 
ganiganeshss79
