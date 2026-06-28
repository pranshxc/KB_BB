---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-16_thisclosed_2-postgresql-database-exfiltration-through-the-abuse-of-postgrest-req.md
original_filename: 2023-01-16_thisclosed_2-postgresql-database-exfiltration-through-the-abuse-of-postgrest-req.md
title: thisclosed_#2 - PostgreSQL Database Exfiltration through the abuse of PostgREST
  requests
category: blogs
detected_topics:
- access-control
- api-security
- sqli
- command-injection
tags:
- imported
- blogs
- access-control
- api-security
- sqli
- command-injection
language: en
raw_sha256: ab06dfbda098378c5c6971b5cbb2dc27a28e215b5d9865cf17df90fbc12bd884
text_sha256: f1c5c819fad44df2e590e5b0edb9c84e82ab5cf8addb6e3d061b1a200cdfbdde
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# thisclosed_#2 - PostgreSQL Database Exfiltration through the abuse of PostgREST requests

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-16_thisclosed_2-postgresql-database-exfiltration-through-the-abuse-of-postgrest-req.md
- Source Type: markdown
- Detected Topics: access-control, api-security, sqli, command-injection
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `ab06dfbda098378c5c6971b5cbb2dc27a28e215b5d9865cf17df90fbc12bd884`
- Text SHA256: `f1c5c819fad44df2e590e5b0edb9c84e82ab5cf8addb6e3d061b1a200cdfbdde`


## Content

---
title: "thisclosed_#2 - PostgreSQL Database Exfiltration through the abuse of PostgREST requests"
page_title: "thisclosed_#2 | Hackrate Blog"
url: "https://blog.hckrt.com/blog/thisclosed_2/"
final_url: "https://blog.hckrt.com/blog/thisclosed_2/"
authors: ["Samuele Gugliotta (@indevi0us)"]
bugs: ["SQL injection"]
publication_date: "2023-01-16"
added_date: "2023-01-18"
source: "pentester.land/writeups.json"
original_index: 1670
---

Howdy y’all, readers and fellow hunters! Here is Samuele ‘venomnis’ Gugliotta again, this time to present a web application vulnerability found within a private bug bounty program on [Hackrate](https://www.hckrt.com/), during the middle of the last year, 2022. Let’s cut the pleasantries short and get right into the action.

## **PostgreSQL Database Exfiltration through the abuse of PostgREST requests!**

### Summary

The vulnerability described in the report referenced within the current article would have allowed the database exfiltration, through abuse and malforming of application requests directly related to the usage of the external component PostgREST, used as a standalone web server, as well as an alternative to manual CRUD programming.

### Description

As a target in-scope of the above-mentioned private Bug Bounty Program (BBP), there was a web application, accessible following authorization through [HTTP Basic Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication), in which financial data inherent to registered organizations was imaged, processed and finally modified. Thus, the user provided for testing activities could access such data through certain dashboards, including tables which were being loaded on the front-end through a couple of GET requests in a fairly common pattern. Specifically, the uri `/pg/<table_name>` was passed, followed by the addition of the GET parameter `select` always turned out to contain the `*` value.

Looking at those requests in their entirety, they inevitably seemed somewhat suspicious and definitely deserved a little more attention:
  
  
  Copy 
  
  1/pg/vw_contract_with_orgs?select=*
  
  2/pg/vw_funding_with_orgs?select=*

So, I fired-up my preferred web application proxy, [Burp Suite](https://portswigger.net/burp), to intercept those requests before the tables within the dashboard, as well as their content, were fetched. There was not much to expect in a GET request, right? Wrong. In many contexts, bug bounty especially, the attention to detail is a key. Checking the contents of cookies or HTTP headers passed within certain requests can result in opening up several routes, which followed in the right way, with the right approach and a good dose of creativity, lead to some of the most interesting bugs.

In this specific case, the HTTP `X-Client-Info` header turned out to contain crucial information, as it allowed me to fully understand the logic behind the application and the reason why these requests were being passed in precisely this way, confirming previous suspicions.

It was found to contain the following string:
  
  
  Copy 
  
  1X-Client-Info: postgrest-js/0.35.0

What is that really?

Let me confess that before that moment I had never seen applications using it before, and it was quite new to me, so I armed myself with patience and driven by a natural interest I went to read, and study, the [official documentation of PostgREST](https://postgrest.org/en/stable/).

![](https://i.gifer.com/IHe.gif)

I’m not going to quote every part of it, so I suggest you go and read it directly should you be interested, otherwise expect a _tl;dr_ below.

As it states, _‟PostgREST is a standalone web server that turns your PostgreSQL database directly into a RESTful API. The structural constraints and permissions in the database determine the API endpoints and operations”_.

I couldn’t have asked for a better revelation! Suddenly, the GET requests that were being passed initially had a clear logic. Let’s disassemble them:

  * `/pg` ➔ resource with reference to the use of PostgREST, hence consequent confirmation that there was a database of type PostgreSQL behind the web application;
  * `vw_contract_with_orgs` and `vw_funding_with_orgs` ➔ nothing but two database tables, certainly sanitized and stripped of information that should not be visible, but that doesn’t change their nature;
  * `select=*` ➔ quite guessable, a simple select of all (`*`) contents, including columns, within the database PostgreSQL table.

Having clearly understood, at this point, how the application worked, all that remained was to abuse it.

To show the absolute impact of such a vulnerability, generally an attacker is interested in database tables that may contain sensitive content. For example, the `users` table is often targeted for obvious reasons, as it contains the information including name, id, e-mail and (_hashed_ , hopefully) password of all existing users in the system.

I think it’s fair, at this point, to specify that the use of PostgREST in general is by no means a security vulnerability, but it’s essential to apply the right authorization and access control side checks to make sure that a user, so in the worst case an attacker, cannot access content that they shouldn’t access by-design. Restricting certain specific database tables and just accepting queries from the application to sanitized ones that don’t contain content outside of what an average user should be accessing is what should have been done at best, but actually failed this time.

Having clarified this, let’s talk about the exploitation.

![](https://i.gifer.com/8fCE.gif)

Intercepting again the GET requests that are sent by the application whenever the content of the dashboard is refreshed, let us dwell on the first of the requests that fetch the content from the PostgreSQL database tables. The first one was `/pg/vw_contract_with_orgs?select=*`. After intercepting it, I forwarded the request to the web application proxy _repeater_ to allow me to quickly edit and test it while doing so. Then, I modified the query to point to the `users` table instead of `vw_contract_with_orgs`, so that the final request resulted exactly like `/pg/users?select=*`. Sending that request, I was confronted with a first resounding epic fail. Indeed, the application response was:
  
  
  Copy 
  
  1{"hint":null,"details":null,"code":"42501","message":"permission denied for table users"}

Apparently, the access to the `users` PostgreSQL database table had been properly secured by restricting users by inherent permissions. However, I didn’t put myself down. Rather, think about the logic of that `select` and how it should look on the back-end side. Having all the elements in view, it had to be something like:
  
  
  Copy 
  
  1SELECT * FROM users;

What if we don’t really care to see literally everything? What would you do if you were only interested in seeing something specific within a database table?

I think you would make a query only to the columns you are interested in.

So, I modified again that GET request, until it resulted in something like:
  
  
  Copy 
  
  1/pg/users?select=id

And consequently on the back-end side:
  
  
  Copy 
  
  1SELECT id FROM users;

The application returned the contents of the `id` column in the `users` database table, referring to the identifiers of all existing users.

![](https://i.gifer.com/C6b.gif)

I continued by chaining other columns, such as `email`, `updated_at`, `created_at`, dividing them by comma in the request, so like:
  
  
  Copy 
  
  1/pg/users?select=id,email,updated_at,created_at

And I kept going on as long as the application allowed me to do so from an authorization standpoint, returning each time the requested content through that `select`, which taking shape resulted in something like:
  
  
  Copy 
  
  1SELECT id,email,updated_at,created_at FROM users;

![](https://www.hckrt.com/blog/files/188-DBEXFIL-221227-3.gif) Considering the failed checks at the access control level, I wouldn’t have ruled out that there were other interesting tables to exfiltrate.

### Impact

Possibility to abuse the usage that the application makes of PostgREST to make queries on PostgreSQL database tables that normally should not be accessible to a user, exfiltrating sensitive information.

### Acknowledgements

Thanks as always to the HACKRATE team for giving me the opportunity to mess around in another very interesting private bug bounty program and for triaging my report. Heartfelt thanks also to the Customer team for taking my report seriously, resolving the issue, and deploying a fix in an absolutely respectable time.

That’s all for now.

_venomnis_
