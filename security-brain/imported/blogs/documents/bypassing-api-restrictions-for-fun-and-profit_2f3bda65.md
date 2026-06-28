---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-07_bypassing-api-restrictions-for-fun-and-profit.md
original_filename: 2023-02-07_bypassing-api-restrictions-for-fun-and-profit.md
title: Bypassing API Restrictions for Fun and Profit
category: documents
detected_topics:
- api-security
- command-injection
- otp
- automation-abuse
- cors
- clickjacking
tags:
- imported
- documents
- api-security
- command-injection
- otp
- automation-abuse
- cors
- clickjacking
language: en
raw_sha256: 2f3bda6568639411edbe49cfe3ee79cd017841fefb21387516c70b5e2c425f7c
text_sha256: e2986c6d3afd7cfcc0f96fc096f17337fd583da6ca4ba92d8f384c6d3f55eede
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# Bypassing API Restrictions for Fun and Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-07_bypassing-api-restrictions-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, otp, automation-abuse, cors, clickjacking
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `2f3bda6568639411edbe49cfe3ee79cd017841fefb21387516c70b5e2c425f7c`
- Text SHA256: `e2986c6d3afd7cfcc0f96fc096f17337fd583da6ca4ba92d8f384c6d3f55eede`


## Content

---
title: "Bypassing API Restrictions for Fun and Profit"
url: "https://arnavtripathy98.medium.com/bypassing-api-restrictions-for-fun-and-profit-c9ab746b67be"
authors: ["Arnav Tripathy"]
bugs: ["Payment bypass", "Logic flaw"]
publication_date: "2023-02-07"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1563
scraped_via: "browseros"
---

# Bypassing API Restrictions for Fun and Profit

Bypassing API Restrictions for Fun and Profit
Arnav Tripathy
Follow
4 min read
·
Feb 7, 2023

30

1

Press enter or click to view image in full size
Image credits: https://blog.open-xchange.com/ox-bug-bounty-programs-two-years-in/

Recently, I downloaded and started testing an application locally which provided dashboard access along with rest API endpoints for it’s users to easily interact with it’s functionality. However, while playing with it’s API’s using the available documentation, I realized that some of the API’s were not accessible. As per the error message, I realized that in order to use the unavailable API’s, I would have to buy the premium version of the app. In this blog, I talk how I was able to bypass the restrictions. For simplicity sake, let us tag all our app components used in the blog:

App is redacted.com
API available is GET /start/transaction
API unavailable in free tier(currently used locally but available in premium version ) is POST /stop/transaction

The app allowed me to generate a token to use as an API and I was checking out it’s endpoints using Postman. While I was getting proper results for the start endpoint, I was getting the below error for the unavailable API endpoint:

{ 
"API is accessible only from dashboard. Please upgrade to premium for programmatic access."
}

While the error was sufficiently easy to understand, I still went ahead and googled about the app to see what exactly was the case. As it turns out, the application had retired certain API’s in the latest versions of free tier, though I was still able to do the action of the API through the dashboard. In our case, we can assume that we can start a transaction through the given API, but in order to stop a transaction, we would either need to go to the dashboard or upgrade to premium version.

I started to proxy all dashboard traffic through Burp Suite. To my surprise, the exact endpoints were being reused in the dashboard, which confirmed the existence of the endpoints. Now the question remains, how is the application blocking my Postman requests but seems to work from the dashboard?

I started analyzing the request headers. Below is the request sent to the stop transaction endpoint through Burp:

POST /stop/transaction
Host: redacted.com
Content-Length: 3144
Sec-Ch-Ua: “Chromium”;v=”109", “Not_A Brand”;v=”99"
Sec-Ch-Ua-Platform: “macOS”
X-Api-Token: "$api_token"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
X-Cookie: token="$token"
Content-Type: application/json
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://redacted.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

{
"Json data"
}

While most of headers are what is expected in a browser made request, two additional fields caught my eye:

The X-Api-Token field which had a token different from the API key generated.
The X-Cookie field which was probably the session token.

In my Postman , I added the two additional fields and removed the field with the API key. It threw an error which seemed like a content length issue. After adding the Content-Length header, I was able to use the endpoint like a regular API!

Get Arnav Tripathy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now the objective was clear, in order to use the endpoint as an API, I would need to craft a request which would:

Have the X-Api-Token header value.
Have the session token calculated and appended.
Have the correct content-length calculated and appended.

On analyzing the application for a few days, I discovered that the X-Api-Token value did not change. Maybe it was unique to each application setup. So the first part of the request headers was easy.

For the session token, I analyzed the login workflow through Burp. The login request was something like this:

POST /session HTTP/1.1
Host: redacted.com
Content-Length: 55
Sec-Ch-Ua: "Chromium";v="109", "Not_A Brand";v="99"
Sec-Ch-Ua-Platform: "macOS"
X-Api-Token: "$api_token"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: https://redacted.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://redacted.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

{"username":"admin","password":"admin"}

The response to this request was:

HTTP/1.1 200 OK
Cache-Control: no-cache, no-store, must-revalidate
X-Frame-Options: DENY
Content-Type: application/json
Connection: close
Content-Length: 179
Expires: 0
Expect-CT: max-age=0
Pragma: no-cache

{"token":"$token"}

Problem solved! All I had to do was just craft a post request to login and fetch the token from response. As for the content length , all I had to do was calculate length dynamically from the script.

My final script which bypassed the API restrictions is as below:

import requests
import json

#Credentials needed to automate session
username= "admin"
password=***REDACTED***
x_api_token="1AB-345-678"

#Function to generate headers for Login
def headers_data(request_data,if_login,token=0):
  data_len= str(len(request_data))
  headers_request = {
  'Content-Length': data_len,
  'Content-Type': 'application/json',
  'X-API-Token': x_api_token
  }  
  if if_login:
  return headers_request
  else:
  headers_request['X-Cookie']= 'token='+token
  return headers_request 

#Login to application and store token
login_data= '{"username":' + '"' + username + '"'+',"password":' + '"' + password + '"'+'}'
login_headers = headers_data(login_data,True)
try:
  login_tokens = requests.post('https://redacted.com/session', headers=login_headers, data=login_data, verify=False)
  token= login_tokens.json().get('token')
  print("Login Successful !")
except:
  raise Exception("Login Automation failed") 

#Post request to stop endpoint.
payload_data= { "Some json data to be posted to stop transaction"}
update_ip_headers = headers_data(payload_data,False,token)
stop_transaction_response= requests.put('https://redacted.com/stop/transaction', headers=update_ip_headers, data=payload_data, verify=False)
print("Transaction stopped via API")

Using this script, I was able to stop a transaction programmatically without the need to upgrade to a premium plan!

While the impact was not high for this application, you never know what you might come across :p . Hope this blog is useful for bug bounty hunters!
