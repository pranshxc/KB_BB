---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-28_just-another-tale-of-severe-bugs-on-a-private-program.md
original_filename: 2018-09-28_just-another-tale-of-severe-bugs-on-a-private-program.md
title: Just another tale of severe bugs on a private program.
category: documents
detected_topics:
- ssrf
- idor
- xss
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- ssrf
- idor
- xss
- command-injection
- otp
- business-logic
language: en
raw_sha256: 9527d849bf9522fa4356d1b6c839ce3831d255c290cf339b831e94bdae231ce8
text_sha256: 6a64f22e4a60b2652022fb3aeb15aef4e331f9b50dd6592d84e8d0fa1f20eba4
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Just another tale of severe bugs on a private program.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-28_just-another-tale-of-severe-bugs-on-a-private-program.md
- Source Type: markdown
- Detected Topics: ssrf, idor, xss, command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `9527d849bf9522fa4356d1b6c839ce3831d255c290cf339b831e94bdae231ce8`
- Text SHA256: `6a64f22e4a60b2652022fb3aeb15aef4e331f9b50dd6592d84e8d0fa1f20eba4`


## Content

---
title: "Just another tale of severe bugs on a private program."
url: "https://medium.com/@sivakrishnasamireddi/just-another-tale-of-severe-bugs-on-a-private-program-405870b03532"
authors: ["Siva Krishna Samireddi (@le4rner)"]
bugs: ["Open redirect", "SSRF", "IDOR", "Logic flaw"]
bounty: "1,623"
publication_date: "2018-09-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5676
scraped_via: "browseros"
---

# Just another tale of severe bugs on a private program.

Just another tale of severe bugs on a private program.
Siva Krishna Samireddi
Follow
4 min read
·
Sep 28, 2018

356

2

Hello again,

It would be cool if you read my previous write up before you read this because it’s the same program and the only program that feeds me.

So after I earned 80k INR on the bugs that I found previously, I had to pay my hostel expenses which were around 75k INR. I had a situation like whether I should buy a laptop (my current laptop is dying) or pay my hostel expenses. However, finally, I bought myself a laptop and a brand new mobile. My bank balance again came to its initial state and I began facing downtime in finding bugs ( Came to know it’s quite common in a bug hunter’s timeline ). My father paid my fees from his pocket.

And then one night,

I began testing, my favorite program again. I was looking around just browsing through the application and looking for suitable endpoints to attack. I came across a POST request that looks like below:

URL:

https://redacted.com/v1/api/action?channel=12

POST Data:

{“URL”:”https://subdomain.redacted.com","method":"GET"}

It is obvious that server makes GET request to the provided URL from the POST data. I replaced the URL to my python simple HTTP server. And BOOM!

Nothing happened, no sign of request on my terminal. There is regex check on URL like *.redacted.com. It makes a request only if the URL is one of the subdomains of redacted.com.

Ah! Then I remembered about the open redirect ( which they don't accept without major risks like a token leak ) which I found earlier

https://partner.redacted.com/v1/api?example=blabla&redirectUrl=https://google.com

Inserting this 302 redirect to https://google.com in URL param resulted in fetching google.com content. What to with this SSRF?

I quickly reminded myself that the company uses Amazon cloud services.

Then I used the payload

https://partner.redacted.com/v1/api?example=blabla&redirectUrl=http://169.254.169.254/latest/meta-data

{“URL”:”https://partner.redacted.com/v1/api?example=blabla&redirectUrl=http://169.254.169.254/latest/meta-data","method":"GET"}

Meta-data access through SSRF

I was on cloud9 looking at this response.

Got the Metadata of the aws cloud of the company. I successfully chained an open redirect, SSRF and metadata endpoint to obtain aws metadata.

I now had access to the entire cloud. With no delay, I reported it the company and they fixed it in like 4 hours. I was awarded a bounty amount of 40k INR ( 551 approx ). So that was the highest they can pay.

Fine, I enjoyed the bounty very much, since it is the highest I ever got. Thank you private company. Also, then I decided that I should find the bugs like them. They are really satisfying.

Wait it’s not over. Another night I was again checking for XSS bugs I usually find on the application commonly. Then something struck me.

They fixed the bug in four hours and asked me to verify. Did they had a fix on their staging servers?

I quickly navigated one to virustotal.com and found the staging subdomains. I just replaced the actual domains in the request with the staging domains and BOOM.

Get Siva Krishna Samireddi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Pwned them again!!

Sent the report to them again and I got another 40k INR. (550 approx ).

And again in the same month:

I signed up as a partner and I was asked to upload scanned signature. I quickly uploaded a fake image. Images are being sent to their S3 pointing to cdn.redacted.com. I tried bypassing the upload policies. I got no way in exploiting it. But when I looked into the path of the image it was like

http://cdn.redacted.com/partner/821111/signature/signature.png

I quickly wrote a python script to check if I can download other users’ signature and result was like :

Downloading signature.png of other users.

Reporting this to the company they gave me 15k INR ( 206$ approx ).

I was like is this too much in a month? Hehe :p

Going on…

I found another bug that allowed me to make a refund of any payment made to the merchant.

They basically implemented QR payment system to allow offline stores to use their wallet services. A shopkeeper gets a QR code and he sticks it to the wall of his store. I got the idea of testing after facing a trouble for paying money using cash in a shop ( I was lacking money in cash ). I was forced to use the QR payment systemto pay the shop.

Upon scanning QR code, it made a request

{“request”:{“qrCodeId”:”QR_DATA_ASHDGVA”,”scanCompletedTime”:”1530007755497"}}

In response code:

{…..“MERCAHNT_ID”:”SECRET_CODE",…}

I signed up myself as a merchant and paid some bucks using QR to my merchant account. I tried refunding myself genuinely and then I used merchant id of another merchant. I was successful in refunding from other merchant’s account. It lacked the verification of merhcant_id and the requesting account session. So it affected all the offline merchant stores using the QR system across India including IRCTC ( India’s e-ticketing website).

And I was paid 23k INR for this bug ( 317$ approx ).

Isn’t it cool?

End of the month I transferred 100K to my father’s bank account which is the most satisfying moment among all these.

Total bounty paid: 550$+550$+206$+317$ = 1623$

Thanks for reading.

PS: Any pro bug hunter reading this? Please ignore my innocence and respond if I ever DM you on twitter and share on your handle if possible. :p

More SSRF bypass techniques: https://github.com/cujanovic/SSRF-Testing

Follow me on Twitter: https://twitter.com/le4rner

I am BTech final year student. Please feel free to hire me or invite me to test your company privately.

Ping me on my email: Redacted. -_-

Thanks again for spending some time reading this.
