---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-04_nosql-injection-in-plain-sight.md
original_filename: 2022-04-04_nosql-injection-in-plain-sight.md
title: NoSQL Injection in Plain Sight
category: documents
detected_topics:
- oauth
- jwt
- idor
- sqli
- command-injection
- otp
tags:
- imported
- documents
- oauth
- jwt
- idor
- sqli
- command-injection
- otp
language: en
raw_sha256: 3244f92390ef77374513b9806e56b9650d2f5adc92f1f745c8ccc778012768e3
text_sha256: 379c6ca9401ca08cd5c9045f20f31b9c6f4fd520b37e881100c7bd19b44673b5
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# NoSQL Injection in Plain Sight

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-04_nosql-injection-in-plain-sight.md
- Source Type: markdown
- Detected Topics: oauth, jwt, idor, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `3244f92390ef77374513b9806e56b9650d2f5adc92f1f745c8ccc778012768e3`
- Text SHA256: `379c6ca9401ca08cd5c9045f20f31b9c6f4fd520b37e881100c7bd19b44673b5`


## Content

---
title: "NoSQL Injection in Plain Sight"
page_title: "NoSQL Injection in Plain Sight :: kuldeepdotexe's blog"
url: "https://kuldeep.io/posts/nosql-injection-in-plain-sight/"
final_url: "https://kuldeep.io/posts/nosql-injection-in-plain-sight/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)"]
bugs: ["NoSQL injection"]
publication_date: "2022-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2750
---

Hello, folks!

This article is going to be about my recent discovery on Synack Red Team which was a NoSQL injection.

I asked if I should do a write-up or not in my [Twitter](https://twitter.com/kuldeepdotexe/status/1507023576888934406?s=20&t=nWRb1rUsGdZzuTHbcgSotA) and a lot of you responded with a writeup. Therefore, I am writing this article to showcase the finding.

Please note that this will not be a technical guide on why NoSQL injections exist and their breakdown. I will just share the thought process and approach that I had when testing this particular application.

So, when I got onboarded to this program, it had one application in scope. It was an authenticated test and credentials were provided by the client. Synack’s quality period was also going on and it had approximately 8 hours.

As always, I fired up Burp Suite, opened Burp’s in-built browser, went to the login page, and started intercepting.

I was closely monitoring every request after clicking “Login”.

First, there was a login request to the `/oauth2/token` endpoint. This endpoint returned the JWT token that allowed us to access the application APIs. However, no fun here.

After the login request, there was another request to a metadata endpoint. This also was not very interesting as the endpoint returned data that was going to be used to render the frontend.

But after the first two requests, a request to the `/api/[CLIENT_NAME]/Customers` was sent. This request in particular was very interesting as it had a parameter named `$filter`. And the parameter had a long NoSQL string inside it.

The request looked like this:
  
  
  GET /api/[CLIENT_NAME]/Customers?$filter=(id%20eq%202)%20and%20((is_active%20eq%20%27Y%27)%20and%20(is_deleted%20eq%20%27N%27))&$orderby=name HTTP/1.1
  Host: [TARGET_APPLICATION]
  ...
  [SNIPPED_BECAUSE_IRRELEVANT]
  

If you look at the value of the `$filter` parameter, the URL encoded string decodes to the following filter:
  
  
  (id eq 2) and ((is_active eq 'Y') and (is_deleted eq 'N'))
  

This endpoint returned basic customer information like customer name, last login date, etc.

You can see the full request-response pair below:

![Request - Response pair](/customers.png)

I had read a few blogs on NoSQL injection in past. Especially after the HackIM CTF. So, I figured this was something related to NoSQL.

The `eq` in the `$filter` is the same as SQL’s `=` or `LIKE`.

So, what the endpoint really did was that it read the value of `$filter` and then it evaluated the filter and retrieved the data specified in the filter.

To break down the parameters in the above filter,

  * `id` (This was the customer ID. Our current user had the customer ID of 2. If I had changed it to 1 instead of 2, this would have been an easy IDOR.)
  * `is_active` (This was an attribute our user had. The `is_active` attribute would be `Y` if our user was active and `N` if not.)
  * `id_deleted` (This was another attribute to specify if our user was deleted or not.)

So, the `/api/[CLIENT_NAME]/Customers` endpoint took the filter and returned our own user(user ID 2)’s data **if and only if** our user was active **and** not deleted.

For testing, I removed the later part which was `((is_active eq 'Y') and (is_deleted eq 'N'))` and just sent the following filter:
  
  
  $filter=(id eq 2)
  

The application happily returned my data without erroring out.

As I was aware that this was NoSQL, I googled “NoSQL wildcards” and tried to play around with wild cards. I came across the following documentation by MongoDB on wildcard indices: <https://www.mongodb.com/docs/manual/core/index-wildcard/>

I played around with wild cards doing things like `$filter=($** eq 2)` and some of it worked meanwhile some of it did not.

I also tried to forcefully put wild cards in the value and crafted this payload: `$filter=(id eq $**)`

But it did not have a valid syntax so it also failed.

I honestly did not put much effort into wildcards as I was not getting the syntax right.

Then a thought popped into my mind. There was one operator in the filter called `eq`. What if I use some other operator? Is it possible to do it?

I googled “MongoDB syntax” which led me to this awesome documentation again by MongoDB: <https://www.mongodb.com/docs/manual/tutorial/query-documents/>

![Query Documents](/querydocuments.png)

The above documentation very nicely explains MongoDB syntax with SQL alternative syntax to properly understand it.

However, after going a little further into the documentation, the documentation linked to another documentation page which was about “Query and Projection Operators”. You can find it here: <https://www.mongodb.com/docs/manual/reference/operator/query/>

![Reference](/reference.png)

And, this page was exactly what I needed to craft my exploit! The page listed down all the MongoDB operators and their use cases.

![Operators](/operators.png)

I decided to go with the `gt` operator because I wanted the endpoint to return user details of all the users whose user ID was greater than 0. I had made an assumption that user IDs will start from zero.

For that purpose, I crafted the following payload:
  
  
  $filter=(id gt 0)
  

And the application returned the customer information of the other user as well. Sadly there were only two users and this was a pre-production application. However, I still was happy because I got the info of the other user.

![Customers Pwned](/customers-pwned.png)

I was still not happy with the results because only basic login information was leaked. Any sort of PII or sensitive information was not leaked from this endpoint.

I went back to my Burp history and found all the endpoints that had this `$filter` parameter. I had gathered a total of 7 endpoints.

Closely inspecting the endpoints, I found one interesting endpoint called `/api/[CLIENT_NAME]/CustomerLogins`. This was interesting because it took the filter as well as returned PII in the response.

I used the same payload as above and sent the request. And the application leaked email address, username, password hash, and phone number! And that too of the administrator user. Not just any random user.

![Password Dump](/passworddump.png)

I reported all the endpoints and wrote a nice report. There were few other reports for the same vulnerability after the QR had ended but my report managed to win.

Thanks for the read. :)

You can reach out to me at [@kuldeepdotexe](https://twitter.com/kuldeepdotexe).
