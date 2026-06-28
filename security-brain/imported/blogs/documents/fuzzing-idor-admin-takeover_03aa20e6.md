---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-09_fuzzing-idor-admin-takeover.md
original_filename: 2021-08-09_fuzzing-idor-admin-takeover.md
title: Fuzzing + IDOR = Admin TakeOver
category: documents
detected_topics:
- jwt
- idor
- access-control
- command-injection
- otp
tags:
- imported
- documents
- jwt
- idor
- access-control
- command-injection
- otp
language: en
raw_sha256: 03aa20e663242c0ea776550dcb07fbb937007676e268bb3ae497b65dee3692c7
text_sha256: ae3fbd2d920fc98c1b050ce6db166299224e78e098be4b4a87c6639de96668d8
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Fuzzing + IDOR = Admin TakeOver

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-09_fuzzing-idor-admin-takeover.md
- Source Type: markdown
- Detected Topics: jwt, idor, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `03aa20e663242c0ea776550dcb07fbb937007676e268bb3ae497b65dee3692c7`
- Text SHA256: `ae3fbd2d920fc98c1b050ce6db166299224e78e098be4b4a87c6639de96668d8`


## Content

---
title: "Fuzzing + IDOR = Admin TakeOver"
url: "https://medium.com/@gonzalocarrascosec/fuzzing-idor-admin-takeover-5343bb8f436e"
authors: ["Gonzalo Carrasco (@0xCGonzalo)"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2021-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3431
scraped_via: "browseros"
---

# Fuzzing + IDOR = Admin TakeOver

Top highlight

Fuzzing + IDOR = Admin TakeOver
Gonzalo Carrasco
Follow
4 min read
·
Aug 10, 2021

1K

8

Hello everyone, this is my first post. I’ve been thinking about writing about my findings for a while, so here we go.

Please let me know if you notice any spelling errors.

Press enter or click to view image in full size
https://pixabay.com/es/photos/m%c3%a1quina-de-escribir-mec%c3%a1nica-retro-407695/

We will call the victim web “example.com”. This objective has 6 well defined user roles. The user with low privileges I call it “Low Privilege” and the one with higher privileges I call it “Super Admin”.

Step 01

I love the fuzz, so first of all I started with fuzzing against the endpoint “/api/FUZZ” without login in the app, using the tool ffuf:

Press enter or click to view image in full size

I found 4 endpoints, 2 of them are important here:

user/users
user/updateuser
Step 02

I make a request against the found endpoint and I can see that the server only accepts the POST method:

Step 03

I change the method to POST:

And I can see that a message is displayed for lack of authorization to interact with the resource (endpoint):

Step 04

At this point, I need an authorization token. To obtain it, I log in to the application with my “Low Privilege” user account:

I click on any request and intercept the valid request on the backend, which attaches the “Authorization” header with the JWT:

Step 05

From the endpoint “/api/vehicle/getLoggedInUserBookings” I can see a header “Authorization: Bearer [token]”:

Press enter or click to view image in full size
Step 06

I copy and paste this header in my request from Step 03. I add the “Authorization” header with the token that I captured previously and make the request. At this point I noticed a new error message returned by the application:

Press enter or click to view image in full size
Step 07

Now, the first thing I think about is “balancing” the request to get a clean response from the server. This got me thinking about changing some headers like “Content Type” and “Accept”. Also, I always add a random parameter (JSON format) in the request with a random value to determine how the server reacts:

Press enter or click to view image in full size
Step 08

My first thought when faced with a new API is to save every single parameter I come across along the way. Continuing with this thought, I use the parameters I found in the request from Step 05 to debug the responses and try to get an accurate HTTP 200 OK response:

Press enter or click to view image in full size

The message “User details fetch successfully” tells me that everything is fine!

Step 09

It is an important point in the exploitation, since I must look for one or more parameters that allow me to obtain more information.

Get Gonzalo Carrasco’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Okay, using fuzzing techniques again, I find a valid parameter. This parameter was found with the name of ‘“role: 1”’:

The correct syntax to get the correct result with ffuf is as follows:

ffuf -w g0ld3n-api.txt -u https://vulnerable.com/api/endpoint -X POST --data '{"param1":value1,"param2":value2,"FUZZ":6}' -H 'Authorization: Bearer JWT'
Press enter or click to view image in full size
Step 10

Then I send the request with this new parameter (role) and the server returns me confidential information about all the users with the “role” equal to “6” corresponding to the Low Privilege role:

Press enter or click to view image in full size
Step 11

At this point I can detect that the API is vulnerable to IDOR in its functionality to view user information. Now, will it also be true for the “update user” endpoint found previously in Step 01?

I use the parameters found in Step 10 and start debugging to find a valid response from the server against the endpoint “/user/updateuser”. Once I achieve the “balance” to make the correct request, I change the value of the parameter ‘”role “: 6’ to ‘“role”: 1’:

Role 6 = Low Privilege
Role 1 = Super Admin
Press enter or click to view image in full size

I log in again with my user and I see that I am now Super Admin:

Press enter or click to view image in full size

Thank you very much for reading and please let me know if you notice any errors or inconsistencies.

I leave my git and twitter in case you want to take a look at it:

https://www.linkedin.com/in/gonzalo-carrasco-3a2727158/
https://github.com/0xCGonzalo/
https://twitter.com/0xCGonzalo

Take care!

Gifs Source: https://giphy.com/
