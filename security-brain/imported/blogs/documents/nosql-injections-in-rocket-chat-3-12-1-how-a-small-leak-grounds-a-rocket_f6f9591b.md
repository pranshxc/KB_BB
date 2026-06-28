---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-18_nosql-injections-in-rocketchat-3121-how-a-small-leak-grounds-a-rocket.md
original_filename: 2021-05-18_nosql-injections-in-rocketchat-3121-how-a-small-leak-grounds-a-rocket.md
title: 'NoSQL Injections in Rocket.Chat 3.12.1: How A Small Leak Grounds A Rocket'
category: documents
detected_topics:
- command-injection
- password-reset
- mfa
- api-security
- sso
- sqli
tags:
- imported
- documents
- command-injection
- password-reset
- mfa
- api-security
- sso
- sqli
language: en
raw_sha256: f6f9591b690324cbf54470c5c7f23e24f8784c18a52165b3763a1354e0f5f493
text_sha256: 21491f5cbb258eb59bd5dfacfaf6416bb57480d6d55c6a49332542990695a3c2
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# NoSQL Injections in Rocket.Chat 3.12.1: How A Small Leak Grounds A Rocket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-18_nosql-injections-in-rocketchat-3121-how-a-small-leak-grounds-a-rocket.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, mfa, api-security, sso, sqli
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `f6f9591b690324cbf54470c5c7f23e24f8784c18a52165b3763a1354e0f5f493`
- Text SHA256: `21491f5cbb258eb59bd5dfacfaf6416bb57480d6d55c6a49332542990695a3c2`


## Content

---
title: "NoSQL Injections in Rocket.Chat 3.12.1: How A Small Leak Grounds A Rocket"
page_title: "NoSQL Injections in Rocket.Chat 3.12.1: How A Small Leak Grounds A Rocket | Sonar"
url: "https://www.sonarsource.com/blog/nosql-injections-in-rocket-chat/"
final_url: "https://www.sonarsource.com/blog/nosql-injections-in-rocket-chat/"
authors: ["Paul Gerste"]
programs: ["Rocket.Chat"]
bugs: ["NoSQL injection", "RCE"]
publication_date: "2021-05-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3642
---

## TL;DR overview

  * Sonar's research uncovered NoSQL injection vulnerabilities in Rocket.Chat that allow attackers to bypass authentication or extract data by injecting MongoDB query operators into user-controlled input fields.
  * Unlike SQL injection, NoSQL injection exploits JSON-based query structures—passing objects like {"$gt": ""} instead of strings bypasses equality checks entirely, a pattern that standard input sanitization often misses.
  * The findings affect versions of Rocket.Chat that directly pass user input into MongoDB queries without schema validation, emphasizing the need for strict input typing in Node.js/MongoDB stacks.
  * Developers using MongoDB should enforce schema validation at the application layer and avoid passing raw request body objects directly into query methods.

Rocket.Chat is one of the most popular open source solutions for team communication, written in JavaScript and TypeScript. It has more than 12 million users worldwide and there are over 800,000 server instances deployed that are being used to exchange confidential information and files. We discovered critical vulnerabilities in its source code that could have been used by an attacker to take complete control over a server, starting with as little as any user’s email address. 

In this blog post we investigate these vulnerabilities by first taking a quick look at NoSQL databases, then explaining how injections look like in that context. We then analyze the found vulnerabilities and how they can be chained for an exploit. Finally we give advice on how to prevent such bugs in your applications.  

## Impact

During the analysis of Rocket.Chat 3.12.1 we found two NoSQL Injection vulnerabilities. These can allow attackers to escalate their privileges, to execute arbitrary system commands on the host server, and to steal confidential user data and chat messages. Both vulnerabilities are fixed in version 3.13.2 and backported to older branches in versions 3.12.4 and 3.11.4.

To attack a Rocket.Chat instance, an attacker either needs an account or has to know the email address of any user that has 2-factor authentication (2FA) disabled. Some open source communities use public Rocket.Chat instances with open registration, which would be vulnerable. In other scenarios it can be easy to guess or find email addresses of users.

## Technical Details

We found two NoSQL Injection vulnerabilities in two separate components. Each one can be used on its own to take over an admin account but they use different injection approaches, making it interesting to see both. Combining them into a chain makes an attack less likely to be detected.  

### MongoDB Injection Primer

[MongoDB](https://www.mongodb.com/) is a popular document-oriented database and falls into the category of NoSQL databases. It consists of collections and documents, which are the respective equivalents of tables and rows in a relational database. Each document has a JSON-like structure with keys and values on multiple hierarchical levels. A document that represents a user could look like this:

**Example document**

Copy to clipboard
  
  
  {
  _id: "507f1f77bcf86cd799439011",
  name: "admin",
  age: 42,
  secrets: {
  token: "s3cr3t"
  },
  role: "admin"
  }

Queries also have such a JSON-like structure and describe which fields of a document have to have certain values in order to be contained in the result set. The query supports literal values but also operators. There are field-level operators that can be used to e.g. specify a numeric range, and there are top-level operators that can be used to build more complex queries. A query that returns all users that are over 18 years old and have the  _admin_ role would look like this:

**Example query**

Copy to clipboard
  
  
  {
  age: {
  $gt: 18
  },
  role: "admin"
  }

A classic injection in this scenario occurs when a program expects a certain user-provided value to be a string, but it can also be an object. This happens often when user input comes in JSON format. In such a case, an attacker can for example bypass a login by specifying an object as the password parameter which contains an operator expression that is always true, like `{"$ne":1}`.

When exploiting SQL Injections, joins and subqueries are often used to leak data from different tables. There are equivalents of this in MongoDB, but they cannot be used in every scenario. Attackers have to get creative when they find a NoSQL Injection, because it usually does not give them the same capabilities that an SQL Injection would.  

### NoSQL Injection #1: Taking Over a Regular User 

During our research we managed to execute arbitrary code on the server, but we had to take small steps to get there. The first step for an attacker is to take over an unprivileged user account. One of the NoSQL Injections can be used without authentication, but it requires us to know the email address of a user that does not have two-factor authentication (2FA) enabled.

The first vulnerability is CVE-2021-22911: a Blind NoSQL Injection that allows to leak a user’s password reset token. The vulnerable part of the code is located in the `getPasswordPolicy()` method. This method can be called without being authenticated, which makes sense because the frontend needs to know the password policy when users are registering. Its parameter `params` is coming from a user-controlled JSON value but is not validated in any way:

[**server/methods/getPasswordPolicy.js**](https://github.com/RocketChat/Rocket.Chat/blob/f2817c056f9c063dd5f596446ef2e6c61634233b/server/methods/getPasswordPolicy.js#L7-L15)

Copy to clipboard
  
  
  7  getPasswordPolicy(params) {
  8  const user = Users.findOne({ 'services.password.reset.token': params.token });
  9  if (!user && !Meteor.userId()) {
  10  throw new Meteor.Error('error-invalid-user', 'Invalid user', {
  11  method: 'getPasswordPolicy',
  12  });
  13  }
  14  return passwordPolicy.getPasswordPolicy();
  15  }

  
The `Users.findOne()` method in line 8 queries the users collection with the provided query object and returns the first match. Since an attacker can provide `params.token` as an object, they can use MongoDB’s `$regex` operator to check if a token begins with a certain character. To check if a token begins with an uppercase `A`, the query would look like this:

Copy to clipboard
  
  
  Users.findOne({
  'services.password.reset.token': {
  $regex: '^A'
  }
  });

  
This can be used to create an oracle that can tell whether a token begins with a certain sequence of characters or not. When the query matches a user, the server’s password policy is returned, but when it does not return any result the method returns an error. An attacker can repeatedly make guesses and observe the oracle’s response to see if our guess was correct, until the whole token is known.

Exploitation of this vulnerability works like this: an attacker requests a password reset for a user using their email address, uses the oracle to leak the newly created token, and finally uses that token to change the user’s password. This enables access to more attack surface because authenticated users, while having no special privileges, can use a lot more of Rocket.Chat’s features.  

### NoSQL Injection #2: Elevating Privileges

Taking over a user account with the previously described NoSQL injection was noisy: the user got a password reset email, was logged out, and cannot log in because the password was changed. If that happens to an admin they would likely investigate and detect the attack. Also, admin accounts are probably more likely to be protected by two-factor authentication (2FA).

So in order to elevate privileges, an attacker can use a second vulnerability: Rocket.Chat Security Issue 0025. It requires authentication, but has more impact: it can not only be used to leak a user’s password reset token, but any field of any user in the database. Here is how it works:

The `users.list` API endpoint takes a query parameter from the URL which is then used to query the users collection. Documents in that collection contain fields that should not be accessible by everyone, which is why the query is filtered by using a blocklist that removes certain fields from the query and the result.  
  
[**app/api/server/v1/users.js**](https://github.com/RocketChat/Rocket.Chat/blob/f2817c056f9c063dd5f596446ef2e6c61634233b/app/api/server/v1/users.js#L223-L246)

Copy to clipboard
  
  
  223  API.v1.addRoute('users.list', { authRequired: true }, {
  224  get() {
  ...  // …
  230  const { sort, fields, query } = this.parseJsonQuery();
  232  const users = Users.find(query, { /* … */}).fetch();
  239  return API.v1.success({
  240  users,
  ...  // …
  244  });
  245  },
  246  });

The filtering only considers actual fields that could be queried, but not top level MongoDB operators. The general drawback of using a blocklist approach for validation is that it is easy to miss something. Using an allowlist to explicitly permit known values is more effective at preventing such issues.

To bypass the filter, the `$where` top-level operator can be used which takes a JavaScript expression and executes it for each document in a collection to decide if the document should be contained in the result set or not. 

This sounds like Remote Code Execution (RCE) but the code is executed inside the MongoDB process and is very restricted, it can only access the fields of the current document and there are no APIs that allow interaction with the outside world. But it still allows for more flexibility when exploiting this injection.

At first we thought this would be another case of a Blind NoSQL Injection where we would make incremental guesses to observe responses, because the result set is always stripped of any sensitive fields. But then we realized that we could leak values by throwing an error inside the `$where` operator’s JavaScript expression! The error is then passed back to the user in the API response with the full error message. An example of this is the following query that leaks an admin user’s secret:

Copy to clipboard
  
  
  {"$where":"this.username==='admin' && (()=>{ throw this.secret })()"}

  
The API response would then include the secret:

Copy to clipboard
  
  
  {
  "success": false,
  "error": "uncaught exception: aHR0cHM6Ly9iaXQubHkvM3VQclgwUA=="
  }

  
With this technique, an attacker can find an admin account and leak their email, password hash, and 2FA secret. They then request a password reset, leak the reset token, and perform the reset just like before. After that, the attacker can log in with the new password and the 2FA codes that can be generated with the secret. After achieving RCE (which we will cover in the next section) the attacker can restore the admin’s original password hash so that the admin can still log in and is less likely to notice the attack.  

### From Admin to Remote Code Execution 

At this point, the attacker has access to an admin user, which already has a huge impact. To determine the severity of this we wanted to know if it is possible to gain Remote Code Execution capabilities, so we spent a little more time researching.

Rocket.Chat has a feature called  _Integrations_ that allows creating incoming and outgoing web hooks. These web hooks can have scripts associated with them that are executed when the web hook is triggered. They are run using the [ _vm_ module](https://nodejs.org/api/vm.html#vm_vm_executing_javascript) of Node.js which might sound safe to use but is explicitly declared to not be a security mechanism. A script that runs inside a VM context has no access to system resources per default, but there are easy ways to break out.

To escape a VM context, the attacker has to get access to objects from the parent context. In this case there are multiple objects and functions passed to the script as arguments which can be used to access the parent context’s function constructor to create a new function. Any functions created with that constructor will inherit its context, regardless of the context they are executed in.

In order to execute system commands on the server the attacker creates a script that will get the `require()` function of the parent context and uses it to load the `child_process`module which contains an `exec()` function:  
  
**payload.js** :

Copy to clipboard
  
  
  1  const require = console.log.constructor('return process.mainModule.require')();
  2  const { exec } = require('child_process');
  3  exec('echo pwned > /tmp/proof.txt');

  
This concludes the exploit chain, starting with just the email address of a regular user, ending with the capabilities to execute arbitrary commands on the server. It shows the dangers of NoSQL Injection vulnerabilities and how important it is to validate all user inputs. SonarQube Server and SonarQube Cloud can help you to identify different types of injection vulnerabilities in your code automatically.  

## Mitigation

Vulnerabilities like the first one are easy to fix. The input should only be a string, so adding a type check is the way to go. This form of validation should be applied in each location that handles JSON user input.

The second vulnerability is more complex, because users should be able to provide a query object, where some fields and operators should work while others are forbidden. To get this right, it is important to validate the user input as strictly as possible.

Restrict the usage of operators. If there is no need for operators at all, then deny user inputs that contain any. If some operators are required, make sure that they cannot be used to leak any data, e.g. with `$regex`. Especially top-level operators like `$where` are dangerous, because they can be used to bypass other restrictions, like seen in the exploitation of the second vulnerability we presented. It can be [disabled entirely in your database configuration](https://docs.mongodb.com/manual/reference/operator/query/where/#javascript-enablement) if it is not needed.

Prefer allowlists over blocklists because it is easy to miss something. Even if your blocklist is correct at the moment it can become insufficient when new operators are added in a future version of the database or when the data structures of the application change. Only allow fields and operators that are known to be safe, deny all others.

Finally, keep in mind that it is not enough to simply restrict the projection, i.e. the data that is returned from the query. Blind or error-based NoSQL Injections can still be used to leak that data, as we have demonstrated with our exploits. It is important to also restrict the fields that can be used in a query.  

## Timeline

**Date**| **Action**  
---|---  
2021-03-19| We report detailed advisories for the NoSQL Injection issues via HackerOne  
2021-03-22| Vendor confirms the vulnerabilities  
2021-04-14| Vendor fixes the NoSQL Injection issues and releases new versions (3.13.2, 3.12.4, 3.11.4)  
  
## Summary

In this blog post we analyzed two code vulnerabilities found in **Rocket.Chat (3.12.1)** , a widely used open source solution for team communications written in JavaScript. We outlined how NoSQL Injections can be exploited, and how they can lead to a complete takeover of a Rocket.Chat instance. We also explained how to prevent these kinds of vulnerabilities.

We reported these vulnerabilities to the vendor in March 2021. They confirmed and fixed the vulnerabilities quickly and the communication with them went smoothly, so kudos to Rocket.Chat security team! If you are running Rocket.Chat, we highly recommend updating to the latest version.
