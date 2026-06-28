---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-15_120-days-of-high-frequency-hunting.md
original_filename: 2022-01-15_120-days-of-high-frequency-hunting.md
title: 120 Days of High Frequency Hunting
category: documents
detected_topics:
- path-traversal
- idor
- access-control
- ssrf
- xss
- sqli
tags:
- imported
- documents
- path-traversal
- idor
- access-control
- ssrf
- xss
- sqli
language: en
raw_sha256: f7e36a9f8f04dca980aa0112e5626f898da80ad62ed0ba5b6936e4190e2bd23b
text_sha256: 1c9110dca7f978b439c9f029310b4910fc72a0db6f12b1b9a75bcdaec7b15d7d
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# 120 Days of High Frequency Hunting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-15_120-days-of-high-frequency-hunting.md
- Source Type: markdown
- Detected Topics: path-traversal, idor, access-control, ssrf, xss, sqli
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `f7e36a9f8f04dca980aa0112e5626f898da80ad62ed0ba5b6936e4190e2bd23b`
- Text SHA256: `1c9110dca7f978b439c9f029310b4910fc72a0db6f12b1b9a75bcdaec7b15d7d`


## Content

---
title: "120 Days of High Frequency Hunting"
page_title: "120 Days of High Frequency Hunting :: kuldeepdotexe's blog"
url: "https://kuldeep.io/posts/120-days-of-high-frequency-hunting/"
final_url: "https://kuldeep.io/posts/120-days-of-high-frequency-hunting/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)", "Sam Paredes (@caffeinevulns)"]
bugs: ["SSRF", "LFI", "Information disclosure", "Broken Access Control", "Authentication bypass", "XSS", "SQL injection"]
publication_date: "2022-01-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3006
---

Hi, guys!

I and [@caffeinevulns](https://twitter.com/caffeinevulns) took inspiration from [@infosec_au](https://twitter.com/infosec_au)’s [blog](https://shubs.io/high-frequency-security-bug-hunting-120-days-120-bugs/) about high-frequency bug hunting and how he found 120 bugs in 120 days. After going through the blog, we decided to try to find 120 bugs in 120 days. Although we did not exactly succeed in finding 120 bugs in 120 days, we still found pretty nice bugs. This blog will be a transparent disclosure of all the bugs I found on Synack Red Team during these 120 days and a small write-up about the techniques I used to find/exploit them.

This particular write-up is limited to my bugs only due to length concerns. However, you can find [@caffeinevulns](https://twitter.com/caffeinevulns)’ bugs on his blog at <https://coffeejunkie.me/>.

For summarising, I found a total of 36 valid vulnerabilities and performed 29 missions and 29 patch verifications. Please note that I have not included duplicate and low-impact findings that were rejected. I originally decided to include them as well but then I felt lazy because I had to go through all the submissions once again and it was not worth the effort for rejected submissions.

### Submissions⌗

Transaction | Date  
---|---  
[AC in /reports/posts.php Leaking PII](/posts/120-days-of-high-frequency-hunting/#ac-in-reportspostsphp-leaking-pii) | Aug 05, 2021  
[Misconfigured Web Server Leaks Admin Functionalities In 302 Response Body](/posts/120-days-of-high-frequency-hunting/#misconfigured-web-server-leaks-admin-functionalities-in-302-response-body) | Aug 05, 2021  
Unauthenticated SQL Injection in [REDACTED] on owner and scheme parameters | Aug 05, 2021  
Debug Flag Allows for viewing of Database Credentials | Aug 19, 2021  
Debug Flag Allows To See Database Credentials | Aug 19, 2021  
Debug Flag Allows To See Database Credentials | Aug 23, 2021  
Root Detection Bypass Using Frida | Sep 15, 2021  
Wordpress Login Panel | Sep 15, 2021  
Exposed Drupal Login Panel | Sep 16, 2021  
[Multiple Time Based SQL Injections](/posts/120-days-of-high-frequency-hunting/#multiple-time-based-sql-injections) | Sep 17, 2021  
Spring Boot Path Traversal - CVE-2020-5410 | Sep 21, 2021  
[Reflected XSS via E-Mail parameter with ASP.NET WAF Bypass](/posts/120-days-of-high-frequency-hunting/#reflected-xss-via-e-mail-parameter-with-aspnet-waf-bypass) | Sep 23, 2021  
Outdated Jira instance leaking PII information | Sep 24, 2021  
[Login Authentication Bypass In Client Side UI](/posts/120-days-of-high-frequency-hunting/#login-authentication-bypass-in-client-side-ui) | Sep 28, 2021  
[Access Control Issue Allows To Execute SQL Statements](/posts/120-days-of-high-frequency-hunting/#access-control-issue-allows-to-execute-sql-statements) | Sep 28, 2021  
Reflected XSS Via URL on [REDACTED] | Sep 30, 2021  
Reflected XSS Via key Parameter on [REDACTED]/admin/core/html/google_api_lang.php | Sep 30, 2021  
Reflected XSS Via POST Body | Sep 30, 2021  
Config Backup Disclosing Cpanel Passwords | Sep 30, 2021  
Folder Backup Exposing CVs | Oct 01, 2021  
[/connectors endpoints leaking Database Connection Information](/posts/120-days-of-high-frequency-hunting/#connectors-endpoints-leaking-database-connection-information) | Oct 01, 2021  
IDOR Exposing CVs and PII | Oct 01, 2021  
WordPress Login Panel | Oct 05, 2021  
Exposed Drupal Login Panel | Oct 06, 2021  
Admin Panel Disclosure | Oct 13, 2021  
Multiple Time Based SQL Injections | Oct 13, 2021  
[Local File Inclusion In download.php](/posts/120-days-of-high-frequency-hunting/#local-file-inclusion-in-downloadphp) | Oct 14, 2021  
Default Admin Credentials On Nagios Server | Oct 28, 2021  
Multiple Exposed Files Disclosing Confidential Information | Oct 28, 2021  
[SSRF Allowing To Access Internal Service](/posts/120-days-of-high-frequency-hunting/#ssrf-allowing-to-access-internal-service) | Nov 02, 2021  
[SSRF Allowing To Access Internal Service](/posts/120-days-of-high-frequency-hunting/#ssrf-allowing-to-access-internal-service) | Nov 02, 2021  
IDOR Allows To Read Order Details | Nov 04, 2021  
IDOR Allows To Read Order Details | Nov 04, 2021  
Reflected XSS With WAF Bypass | Nov 10, 2021  
Multiple IDORs Allowing To Modify Endpoint Details | Nov 11, 2021  
[Pre-auth Server Side Request Forgery](/posts/120-days-of-high-frequency-hunting/#pre-auth-server-side-request-forgery) | Nov 24, 2021  
Patch Verifications(29) |  
Missions(29) |  
  
### Analysis⌗

Category | Vuln Count  
---|---  
Information Disclosure | 13  
Cross Site Scripting | 5  
Access/Privacy Control Violation | 4  
Insecure Direct Object Reference | 4  
SQL Injection | 3  
Server Side Request Forgery | 3  
Path Traversal/Local File Inclusion | 2  
Default Credentials | 1  
Root/Jailbreak Detection Bypass | 1  
  
## Brief Descriptions⌗

#### AC in /reports/posts.php Leaking PII⌗

The PHP script **/reports/posts.php** accepted a numeric POST parameter named `scheme` which returned the residential address of users. I used the following command to enumerate different IDs and return addresses associated with the ID:
  
  
  for id in $(seq 1 50); do curl https://[REDACTED]/reports/posts.php -X POST -d "scheme%5B%5D=$id&custom=&create=Posts" --silent | sed '1,2d'; done
  

The above command will return addresses of users having IDs ranging from 1 to 50.

#### Misconfigured Web Server Leaks Admin Functionalities In 302 Response Body⌗

This was the famous execute after redirect issue in PHP. The server had many PHP scripts that when visited, redirected to the login page. However, the 302 redirects also had the body contents of the same PHP script. Due to this, an attacker could access protected pages that leaked the admin functionality.

I got around the redirect issue by adding the following match and replace rule in Burp:

Field | Value  
---|---  
Type | Response header  
Match | Location: https://[REDACTED].com  
Replace |  
Comment |  
  
Note: `Replace` and `Comment` fields are empty.

#### Multiple Time Based SQL Injections⌗

This particular finding was very interesting because although it was pretty straightforward, `sqlmap` was still not able to exploit it. For this vulnerability, I had to manually enumerate the database and dump information. It was a time-based SQL injection so it required a lot of patience to get something meaningful out of the database.

I first confirmed the SQL injection using the same special character fuzzing. However, this time, the application did not throw an SQL error when we sent a single quote. Instead, the response content was changed. Normally, the page would respond with 400 bad request. But if you send a single quote in the parameter, the response code changed from 400 to 500 hinting at an SQL injection. Now, if we do `'-- -`, the WAF blocked us from using that payload. I tried to bypass the WAF by using different forms of comments like `#` and `/*` but none of them worked and the WAF still blocked us.

The host where I confirmed SQLi was `api-gateway-c.[REDACTED].com`. However, there was another host in scope which was very similar to our host. The other host was `api-gateway.[REDACTED].com`. I checked if the auth token obtained from `api-gateway-c.[REDACTED].com` worked on `api-gateway.[REDACTED].com` and to my surprise, it actually did!

I checked if the endpoints where I confirmed SQL injection was present on `api-gateway.[REDACTED].com` or not. The endpoints were actually present! I sent the SQL injection payload `'-- -` to the new host and the server sent 400 again. This successfully confirmed that the new server was also vulnerable to SQL injection and was not protected with WAF. This allowed me to enumerate the database freely without any issues.

The issues are still not resolved. For some reason, `sqlmap` did not detect the injection point so I decided to manually enumerate the database.

I could get the server to delay response using a payload like `'; WAITFOR DELAY '00:00:10'-- -`.

Now, I needed to find a way to dump data using the delay. For that, I used MSSQL’s `IF` statement. I constructed a payload that delayed the webserver for 10 seconds if the database username started with the character that I supplied. For example, the server would sleep for 10 seconds if the first letter of the database username was ‘A’.

The payload that I constructed was as follows:
  
  
  IF((SELECT SYSEM_USER) LIKE '%') WAITFOR DELAY '00:00:10'
  

I enumerated the whole database username this way. One character at a time. To enumerate one single character, it required me to send 64 requests. However, thanks to Burp Suite’s Intruder, I did not have to manually change the character and send 64 times. I just created a wordlist of lowercase and uppercase characters along with `-` and `_` as special characters and gave it to Intruder. Then, I sorted the results by the **Response received** column.

After running the Intruder 10 times, we get the 10 characters long database username.

Normally, Synack Red Team requires actual table dumps to accept an SQL injection vulnerability. But in this case, they still accepted without me showing the database dumps because of the ridiculously slow data retrieval.

#### Reflected XSS via E-Mail parameter with ASP.NET WAF Bypass⌗

I detect XSS vulnerabilities using a fairly simple payload like `d0mxss'"><`. This payload allows me to find out the context in which the input is reflected. I used the same payload to detect this XSS. The payload was reflected in an input tag like:
  
  
  <input name="E-mail" value="d0mxss'"><">
  

The ASP.NET WAF blocked common payloads like `" onclick="alert(1)`. To bypass the WAF, I used the following payload:
  
  
  " onmouseenter="alert(document.domain)
  

The above payload will make the reflected HTML look like:
  
  
  <input name="E-mail" value="" onmouseenter="alert(document.domain)">
  

When the user moves the pointer above the `E-mail` input, the XSS gets triggered.

#### Login Authentication Bypass In Client Side UI⌗

This was a really lame vulnerability that should not exist at all. All the authentication mechanism was implemented in the frontend using JavaScript and no checking was done on the backend whatsoever. Even a simple login request was not sent to the backend.

When we visited the web application, the application asked for a password in a JavaScript prompt. However, if we just click “**cancel** ” in the JavaScript prompt, we get access to the user interface.

In fact, the UI had the functionality to execute SQL statements and all of this was possible by just clicking “**cancel** ”.

#### Access Control Issue Allows To Execute SQL Statements⌗

This was the same UI that we talked about in the previous vulnerability. I felt like a normal user should not be able to access the UI to execute SQL statements. This was because the interface was at the `/admin` endpoint and this endpoint was discovered from JavaScript files and there were not any links/references to this endpoint in the UI.

I found this concerning so I reported this issue and they actually accepted it considering it valid.

#### /connectors endpoints leaking Database Connection Information⌗

When doing directory brute force with the `raft-small-words.txt` wordlist provided in the [SecLists](https://github.com/danielmiessler/SecLists), I came across an endpoint called `/connectors`. When visited, this endpoint listed the following connectors:

  * jdbc_sink_auroradb
  * local-file-sink
  * mdb_sink_new
  * s3_sink_sf_case_cdc1
  * test-vk

I then felt like these connectors should be accessible via URL. So, I visited the following URL: `http://[REDACTED]/connectors/jdbc_sink_auroradb`. And the endpoint listed the PostgreSQL credentials. I checked for PostgreSQL instances on the network if there were any.

To find PostgreSQL servers, I ran the following `masscan` command:
  
  
  sudo masscan -iL scope.txt -p 5432
  

In the `masscan` result, there were a couple of IPs. I used the credentials obtained from the `/connectors` endpoint to log into these servers. And, the credentials actually worked!

For logging in, I used the following command:
  
  
  psql -h [REDACTED] -p 5432 -U root postgres
  

#### Local File Inclusion In download.php⌗

I found the `download.php` file being reported as an SSRF in the analytics. However, it was rejected. I then investigated a bit more and found out that the `download.php` takes a GET parameter named `f` and the value of `f` is a file that will be retrieved by the PHP script. Upon investigating the LFI, I found out that the script had the following line in the source code:
  
  
  file_get_contents($_GET['f']);
  

So, I just put `f=download.php` to show the PoC.

#### SSRF Allowing To Access Internal Service⌗

This was a vulnerability in Oracle Application Server 10g Mapviewer.

For proof of concept, I performed a full port scan of the server to confirm that the `8002` port was not exposed to the internet. I then put the URL `http://127.0.0.1:8002/mapviewer/omserver` as the Mapviewer URL and submitted the request. The request succeeded and a response was received from the `8002` port confirming the SSRF vulnerability.

If we provided a port that was not open or did not serve HTTP, the response timed out.

#### Pre-auth Server Side Request Forgery⌗

This was a `nuclei` finding.

This was however interesting because the same day, I was onboarded on two different programs from the same organization. One was an internal test meaning we had to test their internal network that is not reachable by the public. And the other was an external test that had public-facing IPs.

One of such public-facing IPs was vulnerable to Microsoft Exchange’s CVE-2021-26855. This was a pre-auth SSRF and you can find the PoC on the internet.

I could have reported this right away but I felt like I should fully exploit the impact of an SSRF. So, I took the list of IPs from the internal test and put them into the SSRF exploit to find out the HTTP servers.

Synack’s VPN was not correctly configured and the internal IPs were not accessible by us. However, by exploiting this SSRF, I could reach those IPs as well.

From this point, I did not go ahead to enumerate these IPs as post-exploitation is not allowed on Synack Red Team.

Reported the issue and won the quality round.

Thanks for the read. :)

You can reach out to me at [@kuldeepdotexe](https://twitter.com/kuldeepdotexe).
