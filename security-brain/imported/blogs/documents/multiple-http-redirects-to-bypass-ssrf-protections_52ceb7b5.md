---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-29_multiple-http-redirects-to-bypass-ssrf-protections.md
original_filename: 2022-01-29_multiple-http-redirects-to-bypass-ssrf-protections.md
title: Multiple HTTP Redirects to Bypass SSRF Protections
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 52ceb7b59cdf88ad8d4a2f8621c1accf9da1c89d3610be45e3a338d38777112c
text_sha256: a3bec6d6deb281cba3388ff0e461d42dbfb4c3c22b90f94f1bb448976b65eef2
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple HTTP Redirects to Bypass SSRF Protections

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-29_multiple-http-redirects-to-bypass-ssrf-protections.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `52ceb7b59cdf88ad8d4a2f8621c1accf9da1c89d3610be45e3a338d38777112c`
- Text SHA256: `a3bec6d6deb281cba3388ff0e461d42dbfb4c3c22b90f94f1bb448976b65eef2`


## Content

---
title: "Multiple HTTP Redirects to Bypass SSRF Protections"
url: "https://infosecwriteups.com/multiple-http-redirects-to-bypass-ssrf-protections-45c894e5d41c"
authors: ["ne555"]
bugs: ["SSRF"]
publication_date: "2022-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2969
scraped_via: "browseros"
---

# Multiple HTTP Redirects to Bypass SSRF Protections

Multiple HTTP Redirects to Bypass SSRF Protections
Koru AI
Follow
4 min read
·
Jan 29, 2022

178

1

Hello hackers,

I needed to utilize many known SSRF techniques at once to successfully exploit many endpoints in the same company. After discovering away, I applied it to all functionalities that use attacker-controlled URLs and found 2 blind and 1 full read SSRFs. This was a bug bounty program so the blind SSRFs closed as dups and another one was accepted.

Press enter or click to view image in full size
About the Target

This company provides marketing services to other businesses. Their application lets you create and manage marketing campaigns. There were many functionalities to test but the application itself was slow and I don’t like testing bloated apps. So, after learning to do some basic stuff in the app I decided to not spend much time and pass the program after finding some vulns.
The application had a lot to do with URLs. So, it captured my attention and I decided to look mainly for SSRFs.

The report itself isn’t disclosed. Hence, I’ll refer it as “company.com” and I won’t share any image from the application itself and alter the URL structure.

Exploitation Process
The API needs the user to be authenticated to the app and uses cookies to do so.

2. We have an API call such as

https://www.company.com/api/campaign/v3/check-snippet?url=http://example.com/

3. url parameter is our injection point. The first thing I tried was to make a request to my interactsh handler to get HTTP headers and IP address of the request. The request below was made.

Press enter or click to view image in full size

4. The request came from an AWS EC2 IP address and there weren’t any open ports. There is also no useful HTTP headers leaking.

5. The application makes any outgoing request. So, my goal is the hit internal hosts. This was a blind request because it didn’t leak me the response it got. However, this functionality returns the full URL as JSON if the the request to attacker controlled URL is successfully made.

6. Both domain and direct IP was allowed. I’ve run netcat HTTP server on my Linux VPS and tried to make a request to that and it worked. However when I tried to make a request to “127.0.0.1”, it didn’t work. Then, I tried “localhost” but that also didn’t work.

7. I’ve tried to abuse the URL parser by fuzzing 00 to FF in “http://127.0.0.1/$FUZZ”, “$FUZZhttp://127.0.0.1” and “http://local$FUZZhost” but nothing came out from that. Then, I tried this beautiful script that generates many payloads. Again, nothing worked. I have a tendency to FUZZ all UTF-8 everywhere. I’ve discovered many odd behaviors in web applications by that way.

8. I’ve payloads like “127.0000000.000000.000001” and “127.1”. Didn’t work

9. I tried to use a subdomain that returns “127.0.0.1” in DNS A record queries. Didn’t work.

Get Koru AI’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

10. There are two github repos I always use when trying to bypass SSRF protections.

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery
https://github.com/cujanovic/SSRF-Testing

11. I wanted to see if the API follows HTTP redirects. So, I’ve done what I always did before and used a site that automatically makes 302 redirects to the IP address set in the URL. It looked like this:

https://make302redirect.io/127.0.0.1

12. I’ve used this payload to get a request, but it didn’t work. Turns out the application basically searched for keywords like “localhost” and “127.0.0.1” and if that exists in the URL provided by the user, it is blocked.

13. So, I’ve tried to run a simple Netcat HTTP server on my VPS that makes 302 redirects to any request sent to it. The command looks like this:

echo -e "HTTP/1.1 302 Found\nContent-Type: application/json\nLocation: http://127.0.0.1\n" | sudo nc -l -s 64.227.116.98 -p 8080 -q 1

(I don’t use that IP address now. Please don’t abuse the current user)

14. I’ve made the API request below.

https://www.company.com/api/campaign/v3/check-snippet?url=http://myIP/

15. It didn’t work.

16. At this point, I was desperate. The application basically grepped keywords like “localhost, 127.0.0.1” and followed HTTP redirects. So, after trying some other payloads with 
pleorqy
, I’ve run two of those netcat servers in different ports and redirected the first one to the other to the localhost. It looked like this:

Vulnerable server ---> my server on port 8080 ---> my server on port 8081 ---> localhost

17. This time it worked.

Conclusion

If I were to use services like 127.0.0.1.nip.io , I’d never discovered this vulnerability because the application didn’t accept anything that has “127.0.0.1” in it.
The application checked the value of Location the header in the first HTTP 302 redirect. However, It didn’t check the second one. That leads to SSRF.

I’ve used these methods in different API endpoints and discovered 3 of these bugs in total. One of them was a full SSRF that let me discover internal assets.

🔈 🔈 Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.
IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live
