---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-10_31k-ssrf-in-google-cloud-monitoring-led-to-metadata-exposure.md
original_filename: 2020-11-10_31k-ssrf-in-google-cloud-monitoring-led-to-metadata-exposure.md
title: 31k$ SSRF in Google Cloud Monitoring led to metadata exposure
category: documents
detected_topics:
- ssrf
- rate-limit
- sso
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- ssrf
- rate-limit
- sso
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: ef74de4ad95445970926e09e368407de37a704c7cd77360a482ca1cddecfe365
text_sha256: 654d2b8989d397cf3139d102726e2a91d5c5cbf9eb5348ea846d042af47aaba3
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# 31k$ SSRF in Google Cloud Monitoring led to metadata exposure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-10_31k-ssrf-in-google-cloud-monitoring-led-to-metadata-exposure.md
- Source Type: markdown
- Detected Topics: ssrf, rate-limit, sso, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `ef74de4ad95445970926e09e368407de37a704c7cd77360a482ca1cddecfe365`
- Text SHA256: `654d2b8989d397cf3139d102726e2a91d5c5cbf9eb5348ea846d042af47aaba3`


## Content

---
title: "31k$ SSRF in Google Cloud Monitoring led to metadata exposure"
url: "https://nechudav.blogspot.com/2020/11/31k-ssrf-in-google-cloud-monitoring.html"
final_url: "https://nechudav.blogspot.com/2020/11/31k-ssrf-in-google-cloud-monitoring.html"
authors: ["David Nechuta (@david_nechuta)"]
programs: ["Google"]
bugs: ["SSRF"]
bounty: "31,337"
publication_date: "2020-11-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4146
---

###  31k$ SSRF in Google Cloud Monitoring led to metadata exposure 

[ November 12, 2020  ](https://nechudav.blogspot.com/2020/11/31k-ssrf-in-google-cloud-monitoring.html "permanent link")

## 

**Update 25.01.2021:** Added Google engineers exploit method for getting access token.  

[Google Cloud Monitoring ](https://cloud.google.com/monitoring)(formerly called Stackdriver) is a service, which provides monitoring for cloud resources (VM instances, App Engine, Cloud functions...). It is available from Google Cloud Console. This service offers monitoring, alerting, uptime checks of cloud resources and much more. It is important to note that the Google Cloud Monitoring service itself is running on Google Cloud virtual machines.  

Every virtual machine in Google Cloud stores its metadata on the [metadata server](https://cloud.google.com/compute/docs/storing-retrieving-metadata). Those metadata include project ID, service account information, information about the virtual machine, or public ssh keys. The metadata might be queried from within the instance (from the IP address 169.254.169.254) or from the Compute Engine API. 

One of the services that Google Cloud Monitoring offers are [Uptime checks](https://cloud.google.com/monitoring/uptime-checks). An Uptime check is a service, that sends periodically requests to a resource to see if it responds. A check can be used to determine the availability of App Engine, VM instance, URL, etc.

I started to test this feature for SSRF by creating an uptime check, which sends a request to an URL/IP address. Most of the URLs and IP addresses, that are usual SSRF targets were blocked. But since the Cloud Monitoring itself is running on Google Cloud VM instances, there was a possibility that I could try to call metadata endpoints, because the request to the metadata endpoint itself would be sent from within the instance. 

When the metadata are queried from within the virtual machine, it is required to include header "Metadata-Flavor: Google" for metadata API version "v1" (older versions of metadata API did not require this header). Luckily there was an option to add custom headers to the request, so that was not an issue.  

I created the uptime check with the following parameters:

``

`Protocol: HTTP  
Hostname: 169.254.169.254  
Path: /computeMetadata/v1/project/project-id  
Custom Headers: Metadata-Flavor: Google (required for /v1/ metadata endpoints) `

``

`

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWjc-sXLkoYR1ssOiLNcTu2caPsTE18ssE2OpUjXsieOeZ0IbL_Gne2L5HrFDUdM4qr0YflFG3AayZM1Cj7_KUgqoJ5LTGdVvXu5cFvt_L7CXdf1y7MhVhWBx4HNRauDh4esglym_TJYU6/s320/settings_uptimecheck.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWjc-sXLkoYR1ssOiLNcTu2caPsTE18ssE2OpUjXsieOeZ0IbL_Gne2L5HrFDUdM4qr0YflFG3AayZM1Cj7_KUgqoJ5LTGdVvXu5cFvt_L7CXdf1y7MhVhWBx4HNRauDh4esglym_TJYU6/s541/settings_uptimecheck.png)

  

  

`

Then I pressed the Test button on the bottom of the Uptime check creation form, which sent a request to the metadata server and then displayed that the check was successful.

The response I saw was:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSZlFDdPELw4igVNzXfPY2zBErzmZdIzIwlLwkV2-fH9HSdcMXxKrJ33sy-LbUo4kXRqlAWTU4tLgZa8xXGgdF1K5Ke-RLUcxAgnJYxY_uXWl3taTcdZTitbroklzDkFh81BYYk_jXrYwp/s320/responseok.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSZlFDdPELw4igVNzXfPY2zBErzmZdIzIwlLwkV2-fH9HSdcMXxKrJ33sy-LbUo4kXRqlAWTU4tLgZa8xXGgdF1K5Ke-RLUcxAgnJYxY_uXWl3taTcdZTitbroklzDkFh81BYYk_jXrYwp/s520/responseok.png)

Because the response code was 200 and the response time was 2 ms, I was sure that the metadata endpoint is reachable via uptime check (request to external URL would take much longer). The problem was that the response body to this request was not visible. Only two things that were returned were the response code and response time. At this point, this was only blind SSRF.  

To get the response body, I used another Uptime check feature - Response validation. Response validation is a feature that checks if the response body contains a specific string. The example configuration could be seen in the image below.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR-UKIC-NqjtlXICUfMQ2EdyUhDRpxItk6fkWW1BphqZoSbMYy6TECQcnrY2HOBlNXGTihFg-ncpbC6uCsclUUJNYqNNPrsj56mTXqa84EO4h0TkkAc2ORQE0fwHOeN4GqEG1qqZ8gqh4j/w400-h313/responsevalid.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjR-UKIC-NqjtlXICUfMQ2EdyUhDRpxItk6fkWW1BphqZoSbMYy6TECQcnrY2HOBlNXGTihFg-ncpbC6uCsclUUJNYqNNPrsj56mTXqa84EO4h0TkkAc2ORQE0fwHOeN4GqEG1qqZ8gqh4j/s552/responsevalid.png)

The method I used was following - I started by looking for one character that is included in the response. I did this by gradually testing whether the response contained one of all possible characters. Then after one character was found, I tried to find second character by appending or prepending characters to the already found character and trying again if it was contained in the response. This process would be repeated until the full response was parsed from the metadata server.

For example, I would try whether the response contains characters 'a', 'b', 'c'... Let's say I found that 'c' is contained in the response. Then I would continue and try to prepend or append another character and tried to find if the response includes characters 'ca', 'cb', 'cc'... Then if I found that 'ca' is returned in the response, I would try another combinations - 'caa', 'cab', 'cac'... and repeat the process until I got the response.  

To do the response body validation I used the endpoint which is called, when the Test button in the Uptime check form is pressed.

The request looked like this:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhsrDM5Nul925suiK30s6MuTziq77dH4qg5b1_etj8lktgT7XcNMsSHpqmZAleKlJS4hRtukt2LOdXam34SWf3yYKr0qWH5-t2wS4HaVUrd7gh62BWMmBc1IbU_2FJ6RdAdtsnmQ8hJen2/w580-h561/request.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhsrDM5Nul925suiK30s6MuTziq77dH4qg5b1_etj8lktgT7XcNMsSHpqmZAleKlJS4hRtukt2LOdXam34SWf3yYKr0qWH5-t2wS4HaVUrd7gh62BWMmBc1IbU_2FJ6RdAdtsnmQ8hJen2/s1324/request.png)

  
  

I created a simple Python script, which parses the response using the described method automatically. The script is available here - <https://gist.github.com/nechudav/0b2e0217ffe31a3cd1c1743c590595e6>  

With this script, I obtained project-level metadata - public SSH key, project name and other information about the Google Cloud Monitoring project. It was also possible to get instance-level metadata which are same for all instances (machine type, CPU platform...). But I struggled with getting instance-level metadata that are unique for each instance or data that are periodically refreshed (for example service account tokens, IP addresses of the instances). It was because Uptime check service is running on multiple instances across the world (there were about 54 running instances) and the requests made to the service are load-balanced. So there was no assurance that multiple requests would be sent to the same instance. Getting unique instance-level metadata would require sending large amount of requests, which was problematic, because the API was rate-limited and it would be very time-consuming. At this point I did not continue in the research. 

I reported the issue, it got accepted, and Google VRP rewarded me $31,337 for this bug. I'd like to thank Google VRP team for the reward and quick response.  

Time of report: June 2020

**Update:** Google engineers found a really nice and clever way to obtain access tokens by reducing number of requests using binary search and regex. Below is the comment describing their solution.

**Comment:**  

We actually ended up writing an exploit to get an access token, after struggling with the same limitation. The two main tricks were binary search for each character (to send fewer requests) and probing both positive and negative matches (to get reliably results). For example:

  * `foo[a-n]`
  * `foo[^a-n]`

One of those requests must eventually return a success response when we hit the correct backend. We'd repeat queries (up to some limit) until we get any OK response and then adjust the search space based on that. Thanks to regexps you can probe multiple characters in parallel (`foo[a-n]`, `foo.[a-n]`, `foo..[a-n]`). In the beginning tokens will overlap, but after ~10 characters or so we usually had a unique prefix. Access tokens are valid for 60 minutes, so on average you have 30 minutes. In the end the exploit took ~15 minutes to get a full access token, including rate limiting. Fun bug. :)

  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[bug bounty](https://nechudav.blogspot.com/search/label/bug%20bounty) [google vrp](https://nechudav.blogspot.com/search/label/google%20vrp) [ssrf](https://nechudav.blogspot.com/search/label/ssrf) [writeup](https://nechudav.blogspot.com/search/label/writeup)

Labels: [bug bounty](https://nechudav.blogspot.com/search/label/bug%20bounty) [google vrp](https://nechudav.blogspot.com/search/label/google%20vrp) [ssrf](https://nechudav.blogspot.com/search/label/ssrf) [writeup](https://nechudav.blogspot.com/search/label/writeup)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps
