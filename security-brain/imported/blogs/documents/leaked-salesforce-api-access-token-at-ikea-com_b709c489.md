---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-04_leaked-salesforce-api-access-token-at-ikeacom.md
original_filename: 2019-04-04_leaked-salesforce-api-access-token-at-ikeacom.md
title: Leaked Salesforce API access token at IKEA.com
category: documents
detected_topics:
- xss
- api-security
- idor
- access-control
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- api-security
- idor
- access-control
- command-injection
- file-upload
language: en
raw_sha256: b709c4890695da4f5fc22b92afe6de7c8a2d5425c46a114a165833dfae052e03
text_sha256: 25f74021b3dba9aff0e89ea4ef536d3013779118bfc8f061f553d30e313e6b5f
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Leaked Salesforce API access token at IKEA.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-04_leaked-salesforce-api-access-token-at-ikeacom.md
- Source Type: markdown
- Detected Topics: xss, api-security, idor, access-control, command-injection, file-upload
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b709c4890695da4f5fc22b92afe6de7c8a2d5425c46a114a165833dfae052e03`
- Text SHA256: `25f74021b3dba9aff0e89ea4ef536d3013779118bfc8f061f553d30e313e6b5f`


## Content

---
title: "Leaked Salesforce API access token at IKEA.com"
url: "https://medium.com/@jonathanbouman/leaked-salesforce-api-access-token-at-ikea-com-132eea3844e0"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Ikea"]
bugs: ["Information disclosure", "Salesforce"]
bounty: "250"
publication_date: "2019-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5330
scraped_via: "browseros"
---

# Leaked Salesforce API access token at IKEA.com

Leaked Salesforce API access token at IKEA.com
Jonathan Bouman
Follow
6 min read
·
Apr 4, 2019

310

4

Press enter or click to view image in full size
Proof of concept

Background
Previously we discussed a Local File Inclusion bug at IKEA.com, the bug was quite complicated and showed us that you have to think out of the box in order to exploit it.

This time we will learn how a relative simple and easy to spot bug can have a high impact; a potential data leak of customer data.

Plenty of high profile brands use Salesforce for their Customer Relationship Management (CRM); it’s perfect for customer care support. Furthermore it’s real easy to implement their software on your own website by using their API.

IKEA.com
As mentioned in our previous bug report, IKEA is a nice brand with a proper responsible disclosure statement. So we’re safe to help them find bugs, maybe even in exchange for a reward. Time to search for bugs!

Finding targets
As always we start with a search for interesting sub domains. A good start is to use Amass, it will query different public available data sets and gives you a nice list of sub domains back.

However searching manually in different data sets is never a bad idea; search the social media accounts of the brand for interesting sub domains and URLs. Open Facebook.com, Twitter.com and LinkedIn.com; search the brand name, search for domain names and see what you end up with.

IKEA Spain Tweet

IKEA Customer care
The Tweet deeplinks to https://social.ikea.es/KAirva which resolves to https://ww9.ikea.com/es/es/contacto/formulario.php?cid=a1:of%7Ca2:es%7Ca3:csc_social%7Ccc:915 a simple page with a web form.

Press enter or click to view image in full size

Forms always deserve a closer look; are there any query parameters reflected in the source (reflected XSS), are you able to upload arbitrary files (stored XSS) or are you able to inject HTML code in one of the fields, code that is being executed in the web interface of the administrator (blind XSS)?

Query parameters
A good start is to search with the Param Miner (Burp Suite plugin) for query parameters that are being reflected in the page source. Found a parameter? Put the request in the Burp Suite Repeater and check if you can create a reflected XSS bug.

Long story short: no luck today, no XSS vulnerable reflected parameters are being found on this page.

The file upload
The next thing we check is the file upload; where do upload files end up and are we able to upload our own how HTML files to a public IKEA url?

Lets open the Chrome DevTools, select a file, press the upload button and watch the network requests being made. Of course you can also use the Burp Suite Proxy History to see the requests.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This time we discover something special. Our browser actually makes quite a few requests in order to upload a simple file. Let’s have a closer look at these requests, what is happening?

Press enter or click to view image in full size
Three requests are needed for a simple file upload
The first request https://ww9.ikea.com/es/en/contact/sendFormS4G.php creates a Salesforce Object ID for the ticket and returns us the ID.
The second request https://ww9.ikea.com/es/en/contact/loginS4G.php gives returns a Salesforce API access token
The third request https://ww9.ikea.com/es/en/contact/sendAttachmentS4G.php uploads the file to the Object ID returned by the first request, using the Salesforce API access token from the second request.

That looks quite cumbersome, making three requests for a simple upload, but if it works it works.

What about the API access token that is being shared with our browser? Does it only has access to our Salesforce object ID or can we use it to access other objects as well? We may use this access token to make requests directly to the Salesforce REST API.

Salesforce documentation
Let’s open the Salesforce REST API documentation:
- How to use the access token in our requests
- How to check which objects we can access
- How to create a list output of a specific object type.

Salesforce REST API
We are able to list the different type of objects and our access permissions by requesting the following URL:
curl https://yourInstance.salesforce.com/services/data/v37.0/sobjects/ -H "Authorization: Bearer token"

Press enter or click to view image in full size
We can access,search, create and delete all the account objects. This means we may have a potential customer data leak.

The output from above is a small snippet of the 389kb JSON file being returned. It contains 465 different object types; from AuthConfigs till Emailmessages, for most we are allowed to query and retrieve them. Mmm.

What about customer data? During bug bounties you want to show the impact of a bug, but at the same time you need to be responsible. That means that you need to limit the amount of data you request, don’t dump the full database, just a few records is enough to show the impact.

Lets create a small list of 25 customers with their names and phone numbers. We do this by requesting a list of users from an account.
curl https://eu15.salesforce.com/services/data/v43.0/sobjects/Account/listviews/00B24000003oGRNEA2/results -H “Authorization: Bearer 00D24XXXXXXXXXXXXXX” -o poc1.json

Press enter or click to view image in full size
Output of poc1.json: definitions of the columns
A snippet of the output, name and phone is censored from the screenshot

We just proved that this bug may lead to a customer data leak, so it’s time to write the report and inform IKEA.

Conclusion
IKEA uses Salesforce for some of their customer care support forms on IKEA.com. In one of those web forms we were able to upload files to their Salesforce instance. IKEA shared their Salesforce API access token with our browser in order to do this. This shared access token was not restricted to only our own support ticket, but it gave access to other customer data as well; a potential customer data leak is the result.

This learns us that whenever we run into Salesforce access tokens we should check their access permissions by making requests to the external REST API of Salesforce.

Solutions
- Restrict access permissions of the shared access token
- Don’t share any access tokens with a visitor, handle the file upload server side.

Reward
€ 250

Timeline
18–09–18 Discovered bug, reported to IKEA through Zerocopter
20–09–18 Bug confirmed by Zerocopter
20–09–18 Bug confirmed by IKEA
21–09–18 IKEA fixed the bug and revoked the API key
21–09–18 Fix confirmed
24–09–18 Requested to coordinate the disclosure of the bug
25–09–18 IKEA informed me I can’t disclose the bug because it affects customer data and investigation of the impact is not finished yet
25–09–18 Requested to update me when the investigation is finished
25–09–18 IKEA requested me to contact my contact person at IKEA for further updates
13–10–18 Requested my contact person at IKEA for coordination and updates
15–10–18 IKEA contact person informed me that investigation is still going on
27–11–18 Requested update
28–11–18 IKEA contact person informed me that investigation is still going on
13–02–19 Requested update
14–02–19 IKEA requested to read the draft of this blog before I publish it
14–02–19 Informed IKEA that I scheduled to write this blog on 21–2–19
28–02–19 Wrote this blog and shared draft with IKEA
01–03–19 IKEA requested me to wait for a few weeks before I publish the report
02–04–19 IKEA informed me I’m allowed to disclose this report
04–04–19 Published this report
