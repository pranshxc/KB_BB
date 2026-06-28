---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-14_from-django-debug-mode-to-pii-data-leak-of-more-than-500-employees-due-broken-ac.md
original_filename: 2023-04-14_from-django-debug-mode-to-pii-data-leak-of-more-than-500-employees-due-broken-ac.md
title: From Django Debug Mode to PII Data Leak of more than 500+ Employees due Broken
  Access Control and IDOR
category: documents
detected_topics:
- access-control
- idor
- api-security
- jwt
- command-injection
- otp
tags:
- imported
- documents
- access-control
- idor
- api-security
- jwt
- command-injection
- otp
language: en
raw_sha256: 3a34191ba7e5d265b060e05fd2b88403fddafb0fb5790188112f998e1dc2217f
text_sha256: 26a24e1bf558202dd728bf4d73bc3f57d46565530fb11a21107ae2644dc3c292
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# From Django Debug Mode to PII Data Leak of more than 500+ Employees due Broken Access Control and IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-14_from-django-debug-mode-to-pii-data-leak-of-more-than-500-employees-due-broken-ac.md
- Source Type: markdown
- Detected Topics: access-control, idor, api-security, jwt, command-injection, otp
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `3a34191ba7e5d265b060e05fd2b88403fddafb0fb5790188112f998e1dc2217f`
- Text SHA256: `26a24e1bf558202dd728bf4d73bc3f57d46565530fb11a21107ae2644dc3c292`


## Content

---
title: "From Django Debug Mode to PII Data Leak of more than 500+ Employees due Broken Access Control and IDOR"
url: "https://medium.com/@ar_hawk/from-django-debug-mode-to-pii-data-leak-of-more-than-500-employees-due-broken-access-control-and-a3eb602a4207"
authors: ["Aayush Vishnoi (@AayushVishnoi10)"]
bugs: ["Debug mode enabled", "IDOR", "Information disclosure", "JWT", "Broken Access Control", "Exposed registration page"]
publication_date: "2023-04-14"
added_date: "2023-05-08"
source: "pentester.land/writeups.json"
original_index: 1266
scraped_via: "browseros"
---

# From Django Debug Mode to PII Data Leak of more than 500+ Employees due Broken Access Control and IDOR

From Django Debug Mode to PII Data Leak of more than 500+ Employees due Broken Access Control and IDOR
Aayush Vishnoi
Follow
4 min read
·
Apr 15, 2023

276

4

TL;DR

While performing a pentest for a client, I found an interesting subdomain running on port 8443 with a Django Debug mode enabled , exposing the endpoints for Swagger UI Dashboard and Redoc API Documentation Dashboard. The same subdomain running on port 443 as well, hosting a Login/Sign-Up panel leads to accessing the Authorized Swagger API endpoints exposing the PII data of the organization employees.

Get Aayush Vishnoi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s start with the complete workflow of the misconfiguration.

Recon — Getting Started
Let’s take the target domain as redacted.com.
I started with basic subdomain enumeration using tools such as Subfinder, Amass, Assetfinder and Alterx[tried first time].
$ subfinder -d redacted.com -o subfinder.txt
$ amass enum -d --passive redacted.com -o amass.txt
$ echo redacted.com | assetfinder --subs-only | tee assetfinder.txt
$ cat subfinder.txt amass.txt assetfinder.txt | sort -u | anew subdomains.txt
$ cat subdomains.txt | alterx | anew subd.txt
After gathering all the subdomains, I saved them in a file say subd.txt.
Now, its time to resolve the subdomains and check how many of them are alive or having status code 200. I used httpx and then saved the output in a file say live.txt.
$ cat subd.txt | httpx -mc 200 | tee live.txt
Now, I have the live subdomains lists, I always perform port scanning on the subdomains I found, I have used naabu for port-scanning.
$ cat subd.txt | naabu -top-ports 1000 -o port-scan.txt
Now, I have data to work on . I started nuclei on the live subdomains at the backend and started manually looking each subdomain to find any interesting subdomain to start with and I found one interesting subdomain say 3ntern1l.redacted.com.
For the subdomain 3ntern1l.redacted.com, I found two open ports 8443 and 443.
Time to Hack — Working with the Subdomain
On the port 8443, I found Django Debug mode Enabled by just adding a random string at the end of the URL say, 3ntern1l.redacted.com/hacker.
From the debug mode, I found 5endpoints as displayed in the snapshot below.
Press enter or click to view image in full size
Django Debug Mode Enabled on PORT 8443
Using the Swagger endpoint, I was successfully able to access the Swagger UI Dashboard.
Press enter or click to view image in full size
Swagger UI Dashboard
I was not able to access the API endpoints as they require the authorization token to get authenticated and access the API endpoints successfully, but I don’t have any token or credentials at this moment.
I know that subdomain is also running on port 443. I navigated to port 443 and found a Login as well as Sign Up page. I immediately signed up and accessed the dashboard.
Press enter or click to view image in full size
Login Page
While navigating the dashboard, I found that subdomain is using the same API endpoints of which Swagger UI Dashboard was available to me. In the burp-request, I also found the JWT Token being used to authorize the API endpoints.
Press enter or click to view image in full size
Burp Intercepted Request of API Endpoint
I immediately copied the JWT token and pasted on the Swagger UI Dashboard. I was successfully able to access the API endpoints available on the dashboard.
I found 2–3 endpoints requires only an id input from the user. I start playing with those endpoints and found that with a change of id💥
Press enter or click to view image in full size
Press enter or click to view image in full size
IDORs

The data exposed includes the PII data such as first name, last name, professional email address, phone number, etc of more than 500+ employees registered on the subdomain.

Conclusion

From the analysis, I can say that the above subdomain have the following misconfiguration and vulnerabilities:

Web Server Misconfiguration [ Django Debug Mode and Sign-up Allowed on Internal Subdomain ]
Broken Access Control [ No Verification/Validation of the JWT Token ]
IDOR [ Accessing the PII Data of other registered users ]
PII Data Leak

Thanks for reading, hope you enjoyed and learned something from this blog.

Let me know, if you have any questions.
