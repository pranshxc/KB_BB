---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-10_account-take-over-via-an-api.md
original_filename: 2023-04-10_account-take-over-via-an-api.md
title: Account Take Over (Via an API)
category: documents
detected_topics:
- access-control
- rate-limit
- idor
- command-injection
- password-reset
- information-disclosure
tags:
- imported
- documents
- access-control
- rate-limit
- idor
- command-injection
- password-reset
- information-disclosure
language: en
raw_sha256: 90221cc2828b6b5e680b932fc64ae160a82ec7d84ed2d15fc6dfe34fe833a654
text_sha256: d9786b9c41a26081769fb47cbc5543364e8040ade0d593214cb0680aa9f9cc0e
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Account Take Over (Via an API)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-10_account-take-over-via-an-api.md
- Source Type: markdown
- Detected Topics: access-control, rate-limit, idor, command-injection, password-reset, information-disclosure
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `90221cc2828b6b5e680b932fc64ae160a82ec7d84ed2d15fc6dfe34fe833a654`
- Text SHA256: `d9786b9c41a26081769fb47cbc5543364e8040ade0d593214cb0680aa9f9cc0e`


## Content

---
title: "Account Take Over (Via an API)"
url: "https://medium.com/@thabisomokoena/account-take-over-via-an-api-2eea4fe49532"
authors: ["Thabiso Mokoena"]
bugs: ["Account takeover", "Information disclosure", "Broken Access Control", "Cryptographic issues"]
publication_date: "2023-04-10"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1283
scraped_via: "browseros"
---

# Account Take Over (Via an API)

Jacky Baloyi
Follow
6 min read
·
Apr 10, 2023

16

Account Take Over (Via an API)

Hi. This is my first story. Please bear with me. Now that we have that out of the way, Let's dig in. This is a write-up about an ATO on a subdomain of a reputable site in my country.

Tools used: python 3,hashes.com, burp community, https://10015.io/, subfinder, httpx

Account Takeover On redacted.domain.xxx:

# Subdomain enumeration: subfinder -d redacted.co.za | httpx -sc -title -tech-detect

# Went over the results from the command above: I saw redacted(subdomain)

Fired burp: Paste the subdomain URL. login attempt while intercepting the request. I saw that the subdomain has an exposed API, or at least exposes the API without proper authentication. api/Auth?.., api/Users?email=… I had the idea of removing routes. I came up with api/users. Viola, it worked. listed all users.

This returned a comprehensive list of responses from users. It has a whole lot of key-value objects. I skimmed through it. I saw that the password value is always null. So I tried api/Users/userID (e.g., api/Users/1). This returned the same key-value json object, only this time it had the value password.

Press enter or click to view image in full size
req & res
# Password Hashes:

Looking at the password value, hashed. I assumed it was a NTLM hash since the JSON object was also exposing the AD Login user name. I did my research. I tried hashcat and online tools to decrypt the hash(es). I could not win. Actually, these tools could not identify the hash.

Went down a rabbit hole. I retrieved several password hashes from the same subdomain. Still no luck identifying the hash type. I immediately thought they must have added some kind of extra layer to make it harder for guys like us to crack the hashes.

I did more digging; please bear with me. I have been doing this actively since the COVID-19 pandemic (10 years on and off). I am still learning. Okay, back to the thingy. After some time researching, a thought crossed my mind. I decided to compare all the password hashes collected from the site via the API bug or flaw. When comparing those hashes, I realized that the length of the hashes varies. Some are 123 characters long, some are 127, and some are 125. You get the flow.

Get Jacky Baloyi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I immediately went into some more research on how possible it is to recover the omitted characters. There was no useful material I could find. I tried it on forums too. No luck. I went back to the subdomain and fiddled with the API once more. I then decided to get the details of the first user on the system(this usually means the sysadmin). Lights on, the JSON object is returned, and it's not the system administrator. Shattered.

Press enter or click to view image in full size

I look through the object. I copy the password hash and count the characters. I found them to be 127. Okay, that is not far from the SHA 512 character limit. Okay, I tried hash ID and hash identifier. No luck, invalid.

I look for Sha 512 examples online. I find them, cont them. They are 128 characters long. What I noticed is that the examples were all starting with the letter e. So, I decide to also add the letter "e" at the beginning of the hash retrieved. Then I head to hashes.com to verify and identify the hash, and viola: the hash has been successfully identified as sha-512. not only identified but also decrypted. The plain text was 11 characters long. OMG! how exciting. I tried it on the login form, and it worked.

Upper hand: now I know the original password string. I decided to encrypt the original string using https://10015.io/. It gave me a perfect 128-bit Sha 512 hash. Then I compared the hash that was missing to the hash that was newly generated. With this, I was hoping to see if I could detect how the web app was omitting characters (hashes). I could not figure it out. It looked random.

F
inding a way to get full sha-512 hashes

since the hashes have omitted characters. I had a way to find them. So an idea came to me. I was curious about how the site's "forget password" function worked. I had to find out. Before resetting the password, I changed the email address of the user I managed to login as. Okay, done. Now it hit forget password, and I entered my email (my registered user email). Password reset was successfully sent. I checked my email. Viola, the much-needed email is there.

I looked at it. Their reset mechanism sends you a temporary, digit-only password when you request the reset. The temporary password in the email was only four digits. I was like, "This can be brute-forced, depending on whether the password does not expire." Yes, it can be brute-forced. Brute-forcing is not fun (at least to me). I needed a faster way. I kept requesting the "forget password" option. I kept on studying the temporary passwords; they were four digits and random, also ranging from 1000 to 2000.

So I wrote a for-loop Node.js function that counts from 1–2000. The nodejs function was saving the for-loop output to a file. after saving to a file. I had to make a way of encrypting the output to Sha-512 so I could quickly compare hashes.

So I started to write a bash script to do so; it worked, but it was not accurate; I could not make it accurate. I ran to Python. I wrote a quick script that encrypts the contents of a text file, line by line. Make sure to encode each line before encryption; otherwise, it won’t work as expected. The hash will be different. Okay, the script worked as expected. Remember the omitted hashes I had earlier? This script helped me identify the missing characters by comparing the first 5–6 characters of the SHA-512 hash.

A
TO

To take over an account, all I had to do was request a password reset on behalf of the user (since I knew all their details except for the clear text password). Headed to the forget password end-point, I requested the password reset. Then I headed back to the API route: GET api/Users/theUserIdOfTheUserWhoRequestedThePasswordReset.

I did this through Burp Suite’s proxy. The GET request returned JSON objects of the user with the same details but a different password hash (since I requested the reset). I copied the first six characters of the new hash and passed it to my Python script that hashes the for-loop output and then searches for the first six characters, comparing it to the hashes of the for-loop contents. The script writes to a file like this:
6734: sha512-hash
6735: sha512-hash
6736: sha512-hash
6737: sha512-hash
etc : etc

If a line has the passed six characters at the beginning of the line, the program returns that line, which has the hashes, and assumes the omitted hash is the same as the hash matched on file, which turned out to be the case 100% of the time.

I am not claiming to have found a way to get omitted characters from the sha512 hash, but I found a way for this particular web app since I had enough info to understand how it works. After a hash was matched, I copied the digits before the semi-colon; this was indeed the temporary password the web app sends to the user’s email when they reset the password. I used the users’ email as the username and the copied digits from the file (generated by the Python script) as a password, and viola! I was successfully logged in.
