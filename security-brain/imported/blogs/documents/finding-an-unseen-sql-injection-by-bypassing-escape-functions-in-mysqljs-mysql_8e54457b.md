---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-21_finding-an-unseen-sql-injection-by-bypassing-escape-functions-in-mysqljsmysql.md
original_filename: 2022-02-21_finding-an-unseen-sql-injection-by-bypassing-escape-functions-in-mysqljsmysql.md
title: Finding an unseen SQL Injection by bypassing escape functions in mysqljs/mysql
category: documents
detected_topics:
- supply-chain
- sqli
- command-injection
- automation-abuse
tags:
- imported
- documents
- supply-chain
- sqli
- command-injection
- automation-abuse
language: en
raw_sha256: 8e54457bbfee8a5123fda4b0c7de968921f96abf1e0c709d8c6db45c88e50ee5
text_sha256: 958cce5dbe5c917ec4da1e18b1f2a5adf36dfeb6b173c7d37e782f5777c67f5b
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: true
---

# Finding an unseen SQL Injection by bypassing escape functions in mysqljs/mysql

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-21_finding-an-unseen-sql-injection-by-bypassing-escape-functions-in-mysqljsmysql.md
- Source Type: markdown
- Detected Topics: supply-chain, sqli, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: True
- Raw SHA256: `8e54457bbfee8a5123fda4b0c7de968921f96abf1e0c709d8c6db45c88e50ee5`
- Text SHA256: `958cce5dbe5c917ec4da1e18b1f2a5adf36dfeb6b173c7d37e782f5777c67f5b`


## Content

---
title: "Finding an unseen SQL Injection by bypassing escape functions in mysqljs/mysql"
url: "https://flattsecurity.medium.com/finding-an-unseen-sql-injection-by-bypassing-escape-functions-in-mysqljs-mysql-90b27f6542b4"
authors: ["stypr (@stereotype32)"]
programs: ["Oracle (MySQL)"]
bugs: ["SQL injection"]
publication_date: "2022-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2880
scraped_via: "browseros"
---

# Finding an unseen SQL Injection by bypassing escape functions in mysqljs/mysql

Finding an unseen SQL Injection by bypassing escape functions in mysqljs/mysql
Flatt Security Inc.
Follow
9 min read
·
Feb 21, 2022

346

3

Press enter or click to view image in full size
TL;DR

It was found that unexpected behaviors in the query’s escape function could cause a SQL injection in mysqljs/mysql (https://github.com/mysqljs/mysql), which is one of the most popular MySQL packages in the Node.js ecosystem.

Typically, query escape functions or placeholders are known to prevent SQL injections. However, mysqljs/mysql is known to have different escape methods over different value types, and it could eventually cause unexpected behaviors when the attacker passes the parameter with a different value type. Unexpected behaviors include buggy behaviors and SQL injections.

Nearly all online development tutorials and security guidelines are misleading, and this has potentially affected many Node.js projects which are depending on this library.

The word “unseen” has been added in the title as most automated SQL injection scanners and payloads do not look for such cases at the time of writing.

Please note that connection.escape(), mysql.escape() and pool.escape() are also affected with the same approach.

The following code is an example of a vulnerable snippet you could find on the top-most result of Node.js express development tutorials on Google search.

The code above seems secure at first sight. However, due to the specifications from the express package, it is possible to pass in username or password with a different value type such as Object, Boolean, Array.

The following code is an example exploit script that passes inpassword as Object and bypasses the authentication.

As seen in the code above, the SQL query will be changed unexpectedly when the passwordparameter is passed as an Object .

To remediate such behaviors, please do at least one of two workarounds listed below:

Adding stringifyObjects: true on mysql.createConnection to prevent unexpected escaping output with the Object type. (MUST)

2. Adding type checks before executing the query (SHOULD)

It is recommended to add type checks before executing the query when you are facing any problems with the former workaround or willing to enforce more security on your project.

However, adding type checks on every case may add more cost on your development and maintenance. It may also introduce another unexpected problems when you’re not really aware of what is going on in the code.

Introduction

Hi, I’m stypr (@stereotype32, https://harold.kim/) from Flatt Security Inc. It’s been a long time since I posted about 0day-related posts. I have another upcoming technical blog post; however, the vendor has not released its advisory for months. so I decided to share something else that could be informational for both developers and security researchers. I will share another one as soon as the vendor releases the advisory.

This time, I decided to write and share some knowledge about the unseen SQL injection as it is found to be affected in many Node.js web applications. Yet, not many are aware of this vulnerability.

This SQL injection trick was first introduced to the public as an online CTF(cybersecurity competition) challenge. However, this vulnerability has already been known to many web security researchers for a very long time, and a lot of researchers were just silently using this trick for private penetration tests and attacking web services.

I decided to write the vulnerability as “unseen” as it is hard to catch such bugs from the developer and the security engineer’s perspective. After all, the escape method is considered a best practice in preventing SQL injections in most SQL-related packages across many languages. This assumption made this vulnerability almost tricky to find without digging down the affected dependency.

Here is the list of tutorials and security guidelines that are found to be misleading at the point of writing.

Security Guidelines

https://blog.sqreen.com/preventing-sql-injection-in-node-js-and-other-vulnerabilities/
https://www.veracode.com/blog/secure-development/how-prevent-sql-injection-nodejs
https://www.stackhawk.com/blog/node-js-sql-injection-guide-examples-and-prevention/

Tutorials

https://codeshack.io/basic-login-system-nodejs-express-mysql/
https://www.tutsmake.com/node-js-express-login-example-with-mysql/
https://www.nicesnippets.com/blog/nodejs-express-login-with-mysql-example
Exploit Demonstration

The vulnerable sample project we will use throughout this article is referenced from the top-most tutorial on a Google Search. (https://codeshack.io/basic-login-system-nodejs-express-mysql/)

Press enter or click to view image in full size

For your convenience, I wrote a docker-compose.yml, and you may be able to run this code quickly on your machine. https://github.com/stypr/vulnerable-nodejs-express-mysql

I also created a sample live instance so you can also access https://sqli.blog-demo.flatt.training/ for testing purposes.

Press enter or click to view image in full size
The domain name on the URL address bar was changed to the new domain.
Please note that the demo service may shut down or become inaccessible.

This example web service has three endpoints as the following.

Note that there is no registration feature available within the source code.

Press enter or click to view image in full size

The accounts table has the following row.

Press enter or click to view image in full size

The authentication flow is as follows. As seen, the code seems to be secure at first sight.

Now, let’s open Chrome’s Developer Tools from the browser.

You can capture the HTTP request and response with the developer tools by clicking the [Network] tab. You may also use your preferred browser and utilize its features.

By entering username and password on the website, the auth endpoint will be shown on the Developer Tools.

We will then copy the authentication request as fetch() code to execute it as JavaScript code. You can do this by right-clicking on the endpoint and clicking [Copy] -> [Copy as fetch]

Press enter or click to view image in full size

Now let’s move to the [Console] tab and copy-paste the code. The code should look like the following.

Let’s remove the verbose information from the code for convenient testing and execute the code.

As seen below, the Incorrect Username and/or Password error has returned as we passed an invalid credential.

Now, let’s change the code a bit to bypass the authentication. We will now change the password parameter to password[password] to make the parameter as Object and not String.

By running the code above, we get access to an administrator account.

To confirm, We can access the /home endpoint and see if we are logged in as admin.

Alternatively, you can also pass the data as JSON and bypass the authentication.

Press enter or click to view image in full size

So, what has caused the authentication bypass?

Root Cause

First of all, let’s check the official documentation to find out how the escape function works.

Get Flatt Security Inc.’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://github.com/mysqljs/mysql/blob/master/Readme.md#escaping-query-values

As explained in the official documentation, the value types will escape differently depending on the value type we pass as into the parameter.

In order to avoid SQL Injection attacks, you should always escape any user provided data before using it inside a SQL query. You can do so using the mysql.escape(), connection.escape() or pool.escape() methods:

… (snipped) …

Different value types are escaped differently, here is how:

- Numbers are left untouched

- Booleans are converted to true / false

- Date objects are converted to 'YYYY-mm-dd HH:ii:ss' strings

… (snipped) …

- Strings are safely escaped

… (snipped) …

- Objects are turned into key = 'val' pairs for each enumerable property on the object. If the property's value is a function, it is skipped; if the property's value is an object, toString() is called on it and the returned value is used.

- undefined / null are converted to NULL

… (snipped) …

The functionescape is loaded from mysqljs/sqlstring(https://github.com/mysqljs/sqlstring), and from here we see that escaping is done differently based on the type of the value.

lib/SqlString.js

Based on the official guideline, let’s now create an example code to see what happens if we pass different value types into the placeholder.

By running the code, we see that queries are differently escaped depending on the parameter’s value type.

As we see, some types (notably, Object types) include quoted identifiers when being escaped by the escape function. Quoted identifiers are used to indicate databases, tables, columns or such. With this, we can reference other tables or columns within the query.

Now let’s change obj_key_1 and obj_val_1 one by one.

What if password=***REDACTED*** is changed to password=***REDACTED*** ? Since the quoted identifier password is considered as a column, it will eventually become password=***REDACTED*** which will always return 1 (true) at the end. This behavior is similar to the behavior of evaluating 1=1 on the query.

Now, if we change the obj_val_1 to numeric 1 on top of the query, it will eventually become (1=1)=1, and eventually return 1 at the end.

Since 1 is considered as true, the password check is always returned as valid and could bypass the authentication.

Therefore, when the password parameter is passed as {'password': 1}, it will eventually convert to `password`=1, and finally bypasses the authentication logic.

Remediation

There are mainly two workarounds available to remediate this problem.

Workaround 1: Adding stringifyObjects option when createConnection is called

Adding "stringifyObjects":true option when calling mysql.createConnection will eventually block all unexpected behaviors when Object is passed in the parameter.

However, this may affect all existing queries in the project, and could introduce another problem when some queries actually pass Object parameter. You might also want to check out Workaround 2 as an alternative.

Before
After
Workaround 2: Adding type checks

The Workaround 1 may be the most efficient and effective way to fix this problem.

However, the former workaround only blocks any unexpected behaviors from Object exclusively. Other types such as Array, array of Array, Boolean could still cause unexpected problems since it is still escaped differently based on the value type. The former workaround would still introduce other unexpected behaviors in many rare cases.

So it would be better off to add type check codes to make your code much more strict. The downside of this workaround is that it may take a lot of time and cost to add type check codes and do maintenance on your projects. Also, there are chances that you may miss out type checks while writing your code.

Before
After
Conclusion

As seen in such cases, there are still unseen vulnerabilities coming up even if most trusted packages are used with the best security practices.

Make sure to read the official guideline carefully and catch out things that could potentially cause a security impact. It is recommended to add type checks as a lot of packages in Node.js ecosystem allow the non-primitive data to be processed internally. Checking types of user-passed values is always very important across many languages, so such unexpected behavior is not limited to Node.js packages.

From a security engineer’s perspective, I personally recommend to do white-box tests with Node.js web services as there are too many dependencies and unseen vulnerabilities with value type changes. Such attacks with value type change are generally harder to detect and find by black-box tests with automatic vulnerability scanners.

About us

Flatt Security Inc. provides security assessment services. We are willing to have offers from overseas. If you have any question, please contact us by https://flatt.tech/en/.

Thank you for reading this article.

Thanks

I would like to thank @SANGWOO and @sangwhanmoon for sharing good advice and feedback on this blog post. Thanks to my co-workers for reviewing and reading my post!
