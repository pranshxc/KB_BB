---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-06_blind-sql-injection-at-fasteditorhemacom.md
original_filename: 2020-08-06_blind-sql-injection-at-fasteditorhemacom.md
title: Blind SQL Injection at fasteditor.hema.com
category: documents
detected_topics:
- xss
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- api-security
language: en
raw_sha256: dc363ab0421756db0cc6325201e7da1360415a78def2ef995fe226d51b30c321
text_sha256: db3c6240078dd21accd482c7d1d83c7ae79f42ad34c422407e0c27e5ad19439f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Blind SQL Injection at fasteditor.hema.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-06_blind-sql-injection-at-fasteditorhemacom.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `dc363ab0421756db0cc6325201e7da1360415a78def2ef995fe226d51b30c321`
- Text SHA256: `db3c6240078dd21accd482c7d1d83c7ae79f42ad34c422407e0c27e5ad19439f`


## Content

---
title: "Blind SQL Injection at fasteditor.hema.com"
url: "https://medium.com/@jonathanbouman/blind-sql-injection-at-fasteditor-hema-com-6ac140c0d1a3"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Hema"]
bugs: ["SQL injection"]
publication_date: "2020-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4347
scraped_via: "browseros"
---

# Blind SQL Injection at fasteditor.hema.com

Blind SQL Injection at fasteditor.hema.com
Jonathan Bouman
Follow
10 min read
·
Aug 6, 2020

527

Press enter or click to view image in full size
Proof of concept. The username of the database user starts with ‘hema’.

Background
These days almost every website uses a database. A server application will formulate a query that is send to the database whenever a visitor requests data from the site. The programming language used in those queries is often SQL. When constructing the database query a server application needs to consider the access levels of the requesting user; only data should be returned that the user has access to.

But what if there is a flaw somewhere in this process that allows you to manipulate the query that is send to the database? You may end up with thousands of school records, private financial data or a hacked firewall. Serious stuff, data leaks are around the corner.

SQL Injections (SQLi) are therefore considered to be critical bugs, in bug bounty programs they often reward you the highest payouts.

HEMA
As described in my previous report; I like HEMA. As a customer I’m happy with their high quality products and as a security researcher I’m happy how they communicate (responsive & friendly). Furthermore they allow me to disclose the bug reports so you can learn from their mistakes and last but not least, if you find good bugs you might end up with truly amazing worst or apple pie.

Good reasons to help them again, getting their customer data more secure; including my own pictures.

Recon, photo projects
Today we start with clicking around in the Photo Project part of the website. It allows you to create photo projects (think of photo books) and a service that allows you to print a batch of photos. Photos you might pick up a few hours later in the physical store. The HEMA uses different sub domains for their services; each having its own API.

Press enter or click to view image in full size
Recon, finding endpoints that are interesting. Wait, is that an ‘orderby’ parameter?!

Vulnerable endpoint
Query string and POST parameters are the ones I keep a close eye on. Is there something that gives me a clue that it might be parsed directly into a SQL query?

I trigger on words that I recognize from SQL queries; from, where, order by, select, limit, offset, id are some of them. It helps if you understand a little bit about SQL; so if you’re new to this, head over to freeCodeCamp and take a quick course :-).

HEMA uses an external subdomain for certain photo projects: https://fasteditor.hema.com/

Whenever someone opens that URL, one of the first requests to be made by the web browser is one to the endpoint: https://fasteditor.hema.com/api/user/<userID>/products?offset=0&limit=8&orderby=id+DESC

This endpoint returns a list of the previous photo projects. Properly sorted sorted, in a descending order applied to the ID.

What happens if we insert a ' into the orderby value? Can we break the query?

Press enter or click to view image in full size
Gotcha! The server returns a SQL error, a first sign we might ran into a SQL injection bug.

We’ve got an error back that looks promising; it learns us that PDO (PHP Data Objects) is used and it even contains a piece of the SQL query. The fact that our ' is not escaped inside this error message is a big red flag.

It always helps when we try to reconstruct the server code while trying to exploit the bug. I google different parts of the error and try to combine my findings in pseudo code. For example I found this stackoverflow post that gives a clue about a possible mistake that’s being made on the server side.

However I’m not sure what was the real cause; so feel free to share your thoughts about the possible root cause, drop it in the comments!

Pseudo code

$dbh = new PDO("photos");

$orderToUse = $_GET['orderby'];

$stmt = $dbh->prepare('SELECT * FROM photos where userId = :username ORDER BY '.$orderToUse.' LIMIT :limit');
$stmt->execute( array(':username' => $_REQUEST['username'], ':limit' => $_REQUEST['limit']) );

SQLMap
A great tool that helps you discover and exploit SQL injection bugs is SQLMap. It can return you proof of concepts payloads and it’s even possible to make full dumps of the victim database.

Lets save the suspected vulnerable request in a text file and run SQLMap: use -r to load your file, use -p to specify the parameter you want to test and use -f extensive database version fingerprinting.

Press enter or click to view image in full size
SQLMap discovers that the orderby parameter is vulnerable to 3 different types of SQL injection attacks

So we have 3 different types of SQL injection attacks that might work for this parameter:

Boolean-based blind, we can manipulate the behavior of the sort depending on internal data. For example: if the admin username starts with an ‘a’ we sort the IDs in the query ASC (ascending) if not we sort them DESC (descending). This allows one to enumerate every single character of the username by just looking at the sort direction of the output.

Stacked queries, we might add our own queries to the query. This one is tricky and quite dangerous. We are allowed to extend the query with new queries. This might allow one to delete database content, start reverse shells or easily create time based SQL attacks (more about that below) in order to retrieve data.

Time-based blind, most databases support the SLEEP() function. A function that pauses the execution of the query for a certain amount of seconds. We can use this to ex filtrate data by measuring the time it takes for the server to send a reply back. For example if the current database username of the server starts with a X we trigger a sleep for 2 seconds, if it starts with a Z a sleep for 4 seconds, etc. Repeat this for every position in the string and you can easily reconstruct the full username by looking at the response times of the request.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Creating a working payload
Most of the times SQLmap allows you to easily ex filtrate the data, it has pre-defined payloads that work in most cases. However today we have bad-luck. SQLmap is having a hard time because of some firewalls and other limitations. I might miss a trick, so please leave a comment if I should have tried another command :-)

Press enter or click to view image in full size
Trying to fetch the current logged in database user by using the SQLmap --user option. Sadly, no data is returned.

Lets grab some good SQL injection cheat-sheets and start the Burp Suite Repeater, we’re going to handcraft our own payload!

I would like to start with the final payload and dissect it piece by piece:
orderby=width+DESC;SELECT+(CASE+WHEN+(SUBSTRING((user())FROM(1)FOR(1))='§h§')+THEN+SLEEP(8)+ELSE+SLEEP(1)+END)

Today we want to retrieve the current logged in database username, we want to run the function USER() and retrieve its output.

The first piece is width+DESC; I changed the ID to width (not sure why, it has no use in the payload, so ignore that). I now end the original query by injecting a ; into the string.
We want to retrieve the output of the USER() function, a function that returns a string (for example waldo@127.0.0.1). What if we can compare every position in the string against all the possible characters. If we have a match we let the server sleep for 8 seconds, if not we let it sleep for 1 second. To be able to do that we need to select the first character of the string that is returned by the USER() function. We can use the SUBSTRING() function in order to fetch only 1 character of a string: the first argument of this function is the input string, the second argument the position we want to retrieve and the third how many characters to return.
Time for a little trick. Somehow , characters are not allowed in this payload. Whatever payload I tried that contained a , returned a response without any sleep functions trigger (all response times < 500ms). So we have to think of a workaround for that. Today I learned that you can use FROM and FOR as a replacement. How? Google is your friend, I searched forsubstring without comma sql injection which led me to a blog somewhere hidden on the internet. One of the comments gave me a clue how to bypass this limitation, use FOR and FROM! So now we are able to convert SUBSTRING(user(),1,1) to SUBSTRING((user())FROM(1)FOR(1)). We just bypassed a firewall (or something else that broke our payload).
The §h§ part is used by Burp Suite Intruder as an injection spot of our character list.
Last but not least, the CASE WHEN (<above substring check>) THEN SLEEP (8) ELSE SLEEP(1) END statement. This allows us to let the server sleep for 8 seconds if we have a hit (the character in the USER() output is the same as our character that Burp Suite Intruder injected), and sleep for 1 second if it’s the substring check is not a hit. We encapsulate the query inside a SELECT () just to be sure that the database will execute the query.

Proof of concept
Whenever we can automate stuff, we should try to automate it. Burp Suite Intruder to the rescue. We instruct the Intruder to use our payload and replace the §h§ part with characters from a predefined list (consisting of all the letters of the alphabet, all the numbers and some common special signs like _-.@).

Press enter or click to view image in full size
We discover the first 4 letters of the logged in database username: hema

After we run the attack we sort on the Response completed column, this one shows us the time it took for every character to return a server response. Pay attention to the responses that take longer than 8 seconds, those are a hit!

We move on to the next position in the string when we discovered the correct character. We do this by changing the (SUBSTRING((user())FROM(1)FOR(1)) to (SUBSTRING((user())FROM(2)FOR(1)), re-run the attack and watch for the next +8 seconds hit. Don’t forget to keep an old fashioned notebook next to your PC so you can write down every single character.

After a while we end up with the string hema_live@10.0.102.192.

Congrats, we have just delivered our proof of concept that this server is vulnerable to blind SQL injections, we successfully exfiltrated the username that is logged in and the local IP address of the database server.

Limitation
It takes plenty of work to ex filtrate data manually. However it’s demonstrated in the past that SQLmap can automate these sort of attacks. I was not able to demonstrate that, however I would love to learn from my readers what they would do in this particular situation, leave me a comment below!

Impact
One should consider a database compromised whenever a SQL injection bug is found; most applications have access level checks on the application level and not in the database itself. This means we have unrestricted read / write access in a database whenever we can inject our SQL code.

It’s important to have database query logs in order to properly check if this bug was abused in the past. Relying on web server logs is often not enough (most web servers don’t log the POST parameters of a query). Please be aware that even query logs sometimes might be bypassed by including certain words in your payload.

Solution
Never trust client input. Whenever you use client input in your queries, apply proper checks and implement different techniques that protect your queries.

Discussion
While researching this bug I was surprised by the following error:

Press enter or click to view image in full size
Our SQL injection stopped working?! We are caught. Happy we already recorded the proof of concept videos! ;-)

The vendor of this specific app detected my attack and implemented a hot fix. Within hours of discovering the bug it was already fixed, amazing! I quickly reached out to them to identify myself as the person who triggered their alarms. Shout out to their developers for being so quick and for actually monitoring their apps.

A last point of discussion is the delivered proof of concept. One might be able to use this bug to perform remote code execution on the operating system; SQLMap even has special features that assist you with that. Some companies are fine if you try to escalate already critical bugs, some aren’t. For HEMA we don’t know that yet, so we stopped after proving this (already) critical bug.

Why hack a company that might be in heavy weather?
COVID-19 struck in the first quarter of 2020 and there were/are problems with their creditors. Some people might say: “Leave them alone!”

In my opinion it does not matter the situation of the company if there’s customer data at stake; the sooner bugs are discovered and resolved the better it is for everyone. It’s in the interest of everyone to protect the customer data. If a company handles the situation well it’s a win-win for all parties; the company avoided a potential breach, the customer data is protected, by publishing the report the public is informed that the company is taking bugs seriously. HEMA, keep up the good work!

Reward
€100 HEMA gift card + bonus (reward for reporting 5 reflected XSS bugs, a SQL injection bug and plenty of other bugs).

Timeline
11–05–20 Discovered the bug, hot fix deployed by vendor, written the report, informed HEMA
11–05–20 Telephone contact with vendor to disclose my finding, requests more time to check other endpoints
15–05–20 HEMA confirms the bug and informs me a fix is deployed, rewarded € 100 giftcard for this bug and six reflected XSS bugs
26–05–20 Requested update from vendor, confirms it is fixed and unit tests are now written to avoid future SQL injection bugs.
26–05–20 HEMA agrees with the publication of this report.
05–06–20 HEMA rewarded me a bonus for all the efforts made
06–08–20 Revised the report, published the report
