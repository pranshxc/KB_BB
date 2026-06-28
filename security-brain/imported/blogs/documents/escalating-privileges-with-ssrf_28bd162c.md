---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-20_escalating-privileges-with-ssrf.md
original_filename: 2023-07-20_escalating-privileges-with-ssrf.md
title: Escalating Privileges With SSRF
category: documents
detected_topics:
- access-control
- api-security
- jwt
- ssrf
- command-injection
- otp
tags:
- imported
- documents
- access-control
- api-security
- jwt
- ssrf
- command-injection
- otp
language: en
raw_sha256: 28bd162cc99c928ac5e16360082828ebf52ce75d322efc4a0ebbe481b7ad871f
text_sha256: aebd4c7ec34e7c4a9465661f3c07c4cc64761cc9aed63401969a8981359d3fa4
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating Privileges With SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-20_escalating-privileges-with-ssrf.md
- Source Type: markdown
- Detected Topics: access-control, api-security, jwt, ssrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `28bd162cc99c928ac5e16360082828ebf52ce75d322efc4a0ebbe481b7ad871f`
- Text SHA256: `aebd4c7ec34e7c4a9465661f3c07c4cc64761cc9aed63401969a8981359d3fa4`


## Content

---
title: "Escalating Privileges With SSRF"
page_title: "Escalating Privileges With SSRF :: kuldeepdotexe's blog"
url: "https://kuldeep.io/posts/escalating-privileges-with-ssrf/"
final_url: "https://kuldeep.io/posts/escalating-privileges-with-ssrf/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)"]
bugs: ["SSRF", "JWT"]
publication_date: "2023-07-20"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 910
---

Hello again, folks!

This post is regarding my recent findings on Synack Red Team which consisted of a total of 4 SSRF vulnerabilities. Three of them were authenticated SSRFs and the last was a fully unauthenticated SSRF.

If you follow me on Twitter, you must have seen my post regarding this.

The finding is pretty straightforward. I can explain it in fewer lines but I want to explain my stepwise thought process to finding this specific vulnerability. I want to do this because the target was live for a total of 11 hours and 47 minutes before I reported the vulnerability, and surprisingly no one else reported it despite the relatively small attack surface.

To the blog now,

I was onboarded to the target at 01:31 AM at night. I was obviously sleeping. After waking up, I realized there was a new API target. So I hopped onto my machine.

I prepared the testing environment by loading the Postman collection and Postman environment files into Postman. I then started Burp Suite in order to view and manipulate the requests.

![Postman Collection](/Postman-collection.png)

### Application Overview⌗

There were different services running on each sub-collection. By manually checking each request, I found out that there were a total of 5 services that were actually performing some sort of operation. The other collections are for authentication and other purposes.

The 5 services that were running included:

  * XXXIntegration
  * AssetManagement
  * Billing
  * CustomerManagement
  * OLS

To access any of these services, you require a service-specific access token. For example, if you want to access the `Billing` service, you must have a `Billing` access token. If you have an `AssetManagement` access token, it will not work for the `Billing` service and vice versa.

I obtained an access token for the `AssetManagement` service. I set the access token in the Postman environment in order to for the testing process to work properly. And I started exploring various requests.

### Initial Discovery⌗

By manually testing each request on a one-by-one basis, I came across the `XXXService - /xxxevent` request.

The request looked like this:
  
  
  POST /api/xxx/xxxevent HTTP/1.1
  Content-Type: application/json
  Authorization: Bearer redacted
  Host: AssetManagement-service-host
  Content-Length: 507
  {
  "event_id": "redacted",
  "event_type": "redacted",
  "event_time": "2022-07-06T14:55:00.00Z",
  "correlation_id" : "redacted",
  "payload": {
  "urls": [
  {
  "url_type": "XXXIntegration",
  "url": "https://XXXIntegration-service-host/api/xxxhistory/xxx/1234"
  }  
  ]
  }
  }
  

Here is the explanation for each parameter:

Parameter | Explanation  
---|---  
`event_id` | This is a UUID for a particular event.  
`event_type` | Set to “ _public_ ” by default in the collection. Most probably, this identifies if the event is public or private.  
`event_time` | Describes the time of the event.  
`url_type` | This is set to `XXXIntegration` showing that the `XXXIntegration` service is being requested.  
`url` | This is the parameter of utmost interest, as this specifies an `XXXIntegration` service URL to fetch data. A user can modify this parameter to hold any arbitrary URL and the API will send requests to that URL  
  
The response to this request showed no interesting behavior as it was just a `500 Internal Server Error` page without any verbose errors.

I started testing this request by providing it with a Synack Burp Collaborator URL. And, to my surprise, it actually sent me an HTTP request.

![Request In Collaborator](/request-to-collaborator.png)

### Initial Assumption and Its Limitations⌗

Just like you, I also noticed the authorization token in the request. But at the time of testing, I assumed this was my own authorization token. I believed the server forwarded parts of my request to the URL provided as the `url` parameter.

This kind of behavior has almost no impact on its own because stealing our own bearer token yields nothing. It must be chained with some other attack like CSRF in order to exploit other users. For example, it can be exploited when you make the victim send a request to an attacker-controlled domain.

### Bypassing The Blacklist To Achieve A Partial SSRF⌗

I ignored this behavior and started checking if I can do a local port scan for it to be eligible for a partial SSRF. I tried to make the API send a request to `localhost` but the API had a blacklist in place for such payloads. I tried a handful of payloads like:

  * `localhost`
  * `127.0.0.1`
  * `0.0.0.0`
  * `127.1`

But as expected, all were being filtered by the API.

This API was allowing requests to arbitrary domains so I thought to try a domain name that resolved to `127.0.0.1`. So, I tried it again with the `localtest.me` domain and it successfully bypassed the blacklist. I confirmed that it bypassed the blacklist by the `500 Internal Server Error` response. Normally, if the API filtered the payload, it sent a `403 Forbidden` response.

API normally:

![API Throwing A 403 When Supplied with 0.0.0.0](/api-filtering-localhost.png)

API when I use localtest.me:

![API Blacklisting Bypass Using localtest.me](/api-filtering-localhost-bypassed.png)

Now, all I had to do was create a local port scan PoC and submit it as a partial SSRF. However, I decided to escalate this issue in order for a better payout. I kept this vulnerability aside and started checking other functionalities that could potentially be used to exploit the SSRF.

### Attempting To Understand JWT⌗

At random, a thought clicked in my brain. I wanted to confirm if the bearer token that I received in the collaborator indeed belonged to me. I later confirmed that the bearer token in the collaborator was different from the one that I had in my request.

I used [jwt.io](https://jwt.io/) to decode both the tokens and compared them side by side. And this comparison further confirmed my belief that both the tokens are different. I will not show a screenshot of this for obvious reasons.

Even after confirming that the token is from a different user/service, I still had no idea where this token was being used. I thought to fuzz all API endpoints of all services with this bearer token to see if any of them respond with a `200 OK` or even anything apart from `401 Unauthorized`.

### Finding Services To Use The JWT⌗

As usual, I got lazy and started looking for alternatives to fuzzing. Also, fuzzing must be the last resort in this situation because there were endpoints that performed different CRUD operations. Any wrong request can break the API.

After checking each request manually for a while, a thought randomly clicked in my brain, once again. Let’s revisit our vulnerable request:
  
  
  {
  "url_type": "XXXIntegration",
  "url": "https://XXXIntegration-service-host/api/xxxhistory/xxx/1234"
  }
  

Here, `XXXIntegration` specifies that we are requesting the `XXXIntegration` service. If you notice, the `XXXIntegration` service is there in the 5 services that I listed at the start of the blog. And the `XXXIntegration-service-host` is a host for the same service.

So, my hypothesis was that if the original request was being sent to the `XXXIntegration-service-host` host, then this access token must also belong to the same service.

To confirm this theory, I copied the authorization token received in the collaborator and pasted it into the health check endpoint of the `XXXIntegration-service-host` host. The health check endpoint was the perfect to test for this. The reason behind this is that it returned a `401 Unauthorized` response if the credentials are invalid and a `200 OK` response if the credentials are valid.

After setting the authorization token, I successfully received a `200 OK`. This confirmed that the token that was leaked in collaborator belonged to the `XXXIntegration` service.

Before setting the authorization token:

![API showing a 401 before setting the authorization token](/healthcheck-before-setting-token.png)

After setting the authorization token leaked in the collaborator:

![API showing a 200 OK after setting the authorization token](/healthcheck-after-setting-token.png)

This proved that the authorization token can be used to interact with the `XXXIntegration` service. However, just to make sure that it can not be accessed with any valid access token, I sent a request to the health check endpoint of the `XXXIntegration` service with an access token for the `AssetManagement` service. This failed because the application had proper access control checks in place.

Also, I later confirmed that we can exfiltrate an access token of ANY service by specifying the service name in the `url_type` parameter. If you replace `XXXIntegration` with `Billing` in the vulnerable request, the collaborator request will yield a Billing service access token.

Now we have everything we need to craft a full SSRF report.

  1. A request to an arbitrary URL
  2. API leaking access token of another service
  3. Privilege escalation using the access token

### Finding Even More (Scarier) SSRFs⌗

I started writing a report on this issue. But I accidentally closed all my tabs in Postman. I used the “filter” option in Postman to search for the “event” keyword hoping to find the vulnerable endpoint. But instead, I was greeted with 9 such endpoints that ended with “event”. I checked all of them and found out that all of them were vulnerable.

Now, instead of writing one report, I had to write 4 different reports. I wrote the first three reports. And then moved on to the next and final report. This is where I was so shocked that I could not believe what I was seeing.

The last endpoint was accessible without any sort of authentication. The request to it looked like this:
  
  
  POST /api/xxx/xxxevent HTTP/1.1
  Content-Type: application/json
  Host: CustomerManagement-service-host
  Content-Length: 622
  
  {
  "event_id": "redacted",
  "event_type": "redacted",
  "event_time": "2022-08-30T09:00:00.0000000Z",
  "correlation_id": "redacted",
  "payload": {
  "urls": [
  {
  "url_type": "CustomerManagement",
  "url": "https://CustomerManagement-service-host/api/xxx/customer/1234"
  },
  {
  "url_type": "XXXIntegration",
  "url": "https://XXXIntegration-service-host/api/xxxhistory/xxx/1234"
  }
  ]
  }
  }
  

Any form of authentication was not required to access this endpoint. So, it allowed a remote unauthenticated attacker to obtain valid authorization tokens for different services. All an attacker has to do is tell the server about the service he/she wants to interact with and a URL to send the authenticated access token. The server will send the credentials without asking for anything. It’s that simple. And it’s that scary.

Sent all four reports to Synack and they accepted them happily with a generous bounty amount.

### Conclusion/Takeaways⌗

  1. Manually check for small details/anomalies. This may or may not lead to vulnerabilities. But it can certainly help you escalate the severity of the issue.
  2. Always try to increase the severity of your finding. Never settle for a lower severity vulnerability. Take the help of your fellow hackers if you need to.

I work full-time as a bug bounty hunter mostly hacking in Synack Red Team (SRT). If you’re interested in becoming a part of the Synack Red Team, feel free to connect with me on Twitter, Instagram, or LinkedIn. I’m always happy to offer guidance to fellow cybersecurity enthusiasts.

EOF
