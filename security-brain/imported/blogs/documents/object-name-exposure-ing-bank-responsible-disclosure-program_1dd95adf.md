---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-08_object-name-exposure-ing-bank-responsible-disclosure-program.md
original_filename: 2018-11-08_object-name-exposure-ing-bank-responsible-disclosure-program.md
title: Object name Exposure — ING Bank Responsible Disclosure Program
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 1dd95adfccb258c4faead8a3c9ab0725e85a6b7974cbf626496234e98ea73305
text_sha256: a55d13def2ddc15e8f4a5bbf3d1dff473a8a04a1da27728a60011113a7a58c1c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Object name Exposure — ING Bank Responsible Disclosure Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-08_object-name-exposure-ing-bank-responsible-disclosure-program.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1dd95adfccb258c4faead8a3c9ab0725e85a6b7974cbf626496234e98ea73305`
- Text SHA256: `a55d13def2ddc15e8f4a5bbf3d1dff473a8a04a1da27728a60011113a7a58c1c`


## Content

---
title: "Object name Exposure — ING Bank Responsible Disclosure Program"
page_title: "Object name Exposure — ING Bank Responsible Disclosure Program | by Rohit kumar | Medium"
url: "https://medium.com/@rohitcoder/object-name-exposure-ing-bank-responsible-disclosure-program-1f8f808cc789"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["ING Bank"]
bugs: ["Information disclosure"]
publication_date: "2018-11-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5601
scraped_via: "browseros"
---

# Object name Exposure — ING Bank Responsible Disclosure Program

Object name Exposure — ING Bank Responsible Disclosure Program
Rohit kumar
2 min read
·
Nov 8, 2018

--

1

--

Heading: Object name Or Internal Architecture Getting Exposed because Of Deserialisation Error

NOTE: Usually i only copy/paste my conversation in medium am not having enough time to write these blog posts properly i am sharing this only for learning purpose not for earning my followers. 😐 👊

Hi, I am Rohit Kumar a Security Researcher and Bug Hunter from India.

Vulnerability: Information Disclosure & Internal Architecture Disclosure

— — — — — — — — — — — — — — — -

Reproduction Steps

— — — — — — — — — — — — — — — -

1. Login into => https://developer.ing.com

2. Now go to your Profile for Updating it

3. Edit your name and save it (At this step intercept your request using burp suite)

4. Now, At this endpoint

PATCH /individuals/791345bc-9444–4edc-9955–1b78e86fddfd/individualNames/EifQPFiEYfMiU- 3FODj3sT736QkPuGe4nigpckH2fEqkaitoTfuLjGG3Lu9UDN84DDCkrGf0y8Lx89HLHcUrFfcb HTTP/1.1

Host: api.developer.ing.com

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You will notice a json text in request body like this

{“individualName”:{“lastUpdateUser”:”external-id-means”,”firstName”:”Geeky bbc”}}

5. Now, Change “firstName” key to anything like “test”. So, final request body will be like

{“individualName”:{“lastUpdateUser”:”external-id-means”,”test”:”Geeky bbc”}}

6. Now, forward or repeat this request. it will throw a error

Unrecognized field “test” (class com.ing.tpa.onepam.exchange.model.IndividualName), not marked as ignorable (11 known properties: “startDate”, “lastName”, “salutation”, “endDate”, “type”, “firstName”, “secondName”, “links”, “lastUpdateUser”, “initials”, “_links”])

at [Source: (org.glassfish.jersey.message.internal.ReaderInterceptorExecutor$UnCloseableInputStream); line: 1, column: 65] (through reference chain: com.ing.tpa.onepam.individual.json.model.IndividualNameInputMessage[“individualName”]->com.ing.tpa.onepam.exchange.model.IndividualName[“test”])

Press enter or click to view image in full size

7. Now, you can . see this is exposing field names, internal object names and architecture.

Few more information

Now, here in this report i would also like to mention that i reported one more vulnerability before this which was received by you on 30 August 2018.

I sent you snapshots of PoC and after receiving that report you guys Rejected it and mentioned that this is false positive and this bug not exist. Now, tell me if its false positive how i reproduced it? Lets say my snapshots are fake okay? Now, tell me how i am able to insert 7 lakh characters into your database and i am having strong proof you can check my developer.ing.com account you will get dozens of app created by me which is having around 6 lakh characters. I reported it ethically but i don’t believe you guys are doing it in ethical way.

We should do our own work ethically. If your community will behave ethically everyone will behave ethically.

Thanks,

Rohit Kumar
