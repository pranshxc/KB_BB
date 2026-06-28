---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-26_why-orms-and-prepared-statements-cant-always-win.md
original_filename: 2023-06-26_why-orms-and-prepared-statements-cant-always-win.md
title: Why ORMs and Prepared Statements Can't (Always) Win
category: documents
detected_topics:
- supply-chain
- sqli
- graphql
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- supply-chain
- sqli
- graphql
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: be5c9775a886f691f3f55e418030a58ba1b5648afef13caeac15aacd2a6aa959
text_sha256: 64d9aab5dcb1d15740f43cf7dad050a3e544c5a038f1edbb87d2110e48b3fc74
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: true
---

# Why ORMs and Prepared Statements Can't (Always) Win

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-26_why-orms-and-prepared-statements-cant-always-win.md
- Source Type: markdown
- Detected Topics: supply-chain, sqli, graphql, sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: True
- Raw SHA256: `be5c9775a886f691f3f55e418030a58ba1b5648afef13caeac15aacd2a6aa959`
- Text SHA256: `64d9aab5dcb1d15740f43cf7dad050a3e544c5a038f1edbb87d2110e48b3fc74`


## Content

---
title: "Why ORMs and Prepared Statements Can't (Always) Win"
page_title: "Why ORMs and Prepared Statements Can't (Always) Win | Sonar"
url: "https://www.sonarsource.com/blog/why-orms-and-prepared-statements-cant-always-win/"
final_url: "https://www.sonarsource.com/blog/why-orms-and-prepared-statements-cant-always-win/"
authors: ["Thomas Chauchefoin (@swapgs)"]
programs: ["Soko", "Gentoo Linux"]
bugs: ["SQL injection", "RCE", "Security code review"]
publication_date: "2023-06-26"
added_date: "2023-07-12"
source: "pentester.land/writeups.json"
original_index: 1003
---

## TL;DR overview

  * ORMs and prepared statements prevent most SQL injection attacks but cannot fully protect applications when developers bypass the abstraction layer with raw queries or dynamic SQL construction.
  * Common bypass patterns include string concatenation in ORDER BY clauses, dynamic table or column names, and raw query methods exposed by ORM APIs for complex queries.
  * These edge cases create injection vulnerabilities that persist even in codebases that otherwise follow secure coding practices with parameterized queries.
  * Taint analysis in SonarQube detects these bypasses by tracking user input through ORM and database API calls, catching injection paths that static pattern matching alone would miss.

## Introduction

We were told to use ORMs and prepared statements to avoid SQL injections for a long time now. By doing so, we effectively separate instructions (the semantics of the SQL query) from the data. Modern languages and frameworks often also abstract away the need to write raw queries, offering high-level interfaces around our database models. Unfortunately, that's not enough to thwart away SQL injections once and for all, as these APIs can still present subtle bugs or nuances in their design. 

In this blog post, we show you how the misuse of a Golang ORM API introduced several SQL injections in Soko, a service deployed on the Gentoo Linux infrastructure. Then, we look further into assessing the impact of this vulnerability by using a PostgreSQL feature to execute arbitrary commands on the server.

These vulnerabilities, tracked as CVE-2023-28424, were discovered and reproduced in a testing environment. They were later responsibly disclosed to Gentoo Linux maintainers, who deployed fixes within 24 hours. Because this service only displays information about existing Portage packages, it was not possible to perform a supply chain attack and users of Gentoo Linux were never at risk. While the server hosts several services, affected components are isolated in Docker containers, and the risk of lateral movement from attackers is limited. 

Nonetheless, there are some key learnings from these vulnerabilities that we would like to share in this blog post. 

If you run Soko on your infrastructure, you should upgrade it to Soko 1.0.3 or above. 

## Technical Details

### What's Soko?

Soko is the Go software behind <https://packages.gentoo.org/>, a public interface showing information about published Portage packages that you can install on Gentoo Linux. Portage is the go-to package management tool for this distribution and takes care of resolving and building all required dependencies.

Soko offers a very convenient way to search through all of these packages and easily get information like the associated bug tracker or where the upstream source is. Again, packages are not downloaded from Soko but directly from upstream.

### The Search Feature

Soko is built to let users search through packages–that's its sole job and means that the code of this feature is the most interesting to review with our security hat on. Indeed, it has to assemble a SQL query based on many parameters that may or may not be part of the request. 

ORMs have query builders that introduce a very welcome abstraction layer so developers don't have to hand-write SQL queries; Soko's use of [`go-pg`](https://github.com/go-pg/pg) makes it very expressive and easy to follow.

For instance, if you want to select a record of a given database model whose `title` is prefixed with `my` using `go-pg`, this is what you would write (example taken from [their documentation](https://pg.uptrace.dev/queries/)):

Copy to clipboard
  
  
  err := db.Model(book).
  Where("id > ?", 100).
  Where("title LIKE ?", "my%").
  Limit(1).
  Select()

Notice the presence of query placeholders–the question marks–in the `Where()` clauses. They are replaced with the associated parameters at runtime after escaping them for the right context. Indeed, a string and a column name are specified differently in SQL, and the ORM must escape them accordingly. That also means that the first parameter should always be a constant string: otherwise, that means that we're probably circumventing the escaping feature and could introduce SQL injections.

### Finding (Un)prepared Statements

Diving into the implementation of the search feature, we can notice code like this snippet:

Copy to clipboard
  
  
  searchTerm := getParameterValue("q", r)
  searchTerm = strings.ReplaceAll(searchTerm, "*", "")
  searchQuery := BuildSearchQuery(searchTerm)
  
  var packages []models.Package
  err := database.DBCon.Model(&packages).
  Where(searchQuery).
  Relation("Versions").
  OrderExpr("name <-> '" + searchTerm + "'").
  Select()

A first thing that should jump to your eyes is the parameter `searchTerm`, coming from the user's request, being concatenated to the first parameter of the `OrderExpr()` call. It goes in contradiction with how one should safely use this API. There's probably room for a SQL injection in here! 

Let's look at the implementation of the method `BuildSearchQuery()`, also using `searchTerm` as a parameter and passed as the first argument of `Where()`:

Copy to clipboard
  
  
  func BuildSearchQuery(searchString string) string {
  var searchClauses []string
  for _, searchTerm := range strings.Split(searchString, " ") {
  if searchTerm != "" {
  searchClauses = append(searchClauses,
  "( (category % '"+searchTerm+"') OR (name % '"+searchTerm+"') OR (atom % '"+searchTerm+"') OR (maintainers @> '[{\"Name\": \""+searchTerm+"\"}]' OR maintainers @> '[{\"Email\": \""+searchTerm+"\"}]'))")
  }
  }
  return strings.Join(searchClauses, " AND ")
  }

We can see that `searchTerm` is again directly interpolated in the query. When passed as a parameter to `Where()`, it won't be able to escape its value; it's already in the query. As a result, this function has several SQL injections: one for every use of `searchTerm`! 

### And its GraphQL Sibling? 

Users can also do searches through the GraphQL API to ease integration with external systems and scripts. While most of the code around database models is often automatically generated, features like this require custom code–they are called resolvers. 

GraphQL frameworks have this notion of resolvers that can back types fields: they come in handy when fetching data from a third-party API or running a complex database query. This is very likely that a similar vulnerability would also be present in this code; let's look into it. 

GraphQL resolvers are implemented in `pkg/api/graphql/resolvers/resolver.go`. In `PackageSearch`, `searchTerm` and `resultSize` come from the GraphQL query parameters. The parameter `searchTerm` is also unsafely interpolated in an `OrderExpr()` clause, introducing another SQL injection:

Copy to clipboard
  
  
  func (r *queryResolver) PackageSearch(ctx context.Context, searchTerm *string, resultSize *int) ([]*models.Package, error) {
  // [...]	
  if strings.Contains(*searchTerm, "*") {
  // if the query contains wildcards
  wildcardSearchTerm := strings.ReplaceAll(*searchTerm, "*", "%")
  err = database.DBCon.Model(&gpackages).
  WhereOr("atom LIKE ? ", wildcardSearchTerm).
  WhereOr("name LIKE ? ", wildcardSearchTerm).
  Relation("PkgCheckResults").[...].Relation("Outdated").
  OrderExpr("name <-> '" + *searchTerm + "'").
  Limit(limit).
  Select()
  }

A similar SQL injection is present in the same method when performing a fuzzy search–we omitted it above for brevity. Check your GraphQL resolvers! 

### An Effective SQL Injection

With these potential injections in mind, we can check whether they are exploitable. To first give you some context, the following query is executed when searching for the package `foo`:

Copy to clipboard
  
  
  SELECT
  "package"."atom",
  "package"."category",
  "package"."name",
  "package"."longdescription",
  "package"."maintainers",
  "package"."upstream",
  "package"."preceding_commits"
  FROM "packages" AS "package"
  WHERE
  ((
  (category % 'foo') 
  OR (NAME % 'foo')
  OR (atom % 'foo')
  (
  maintainers @ '[{"Name": "foo"}]'
  OR maintainers @ '[{"Email": "foo"}]'
  )
  )) 
  OR (atom LIKE '%foo%')
  ORDER BY NAME  < - > 'foo'

Once a single quote is used in the search, the semantics of the query change which leads to syntax errors. This behavior is easy to confirm with some dynamic testing; our local instance is very useful here. 

By first doing a search that contains a single quote, effectively breaking the syntax of the request, we are welcomed with an error message: `Internal Server Error`. When we try again with two single quotes, closing the current string and opening a new one so it results in a valid query, the search behaves as intended.

![A list of search results for xdg'' on Soko.](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f9f4c28c-844d-44ff-b122-4b28d32a9530/ORMs%20-%201.png)

Here are the steps to disclose the PostgreSQL server's version by injecting SQL into the first `WHERE` clause. Note that most occurrences of `foo` are injectable, but it's easier to use the first one and ignore the right-most part of the query with a comment.

  * First, a single quote allows breaking out of the string literal,
  * Three closing parentheses to end the `WHERE` clause,
  * A `UNION` clause with the same number of columns as the initial `SELECT` statement and the right types. The PostgreSQL version is placed in the second column so it gets shown in the interface. 
  * A comment (`--`) to ignore everything else after. 

The payload has to respect several constraints:

  * The character `*` cannot be used, or the vulnerable code path is not executed. 
  * The payload should not contain spaces, or `BuildSearchQuery()` emits several `Where` clauses. Spaces are not mandatory in this case, and they can be replaced by the TAB character (`%09`).
  * We must pay special care to the column types and the format of JSONB fields to avoid raising errors in PostgreSQL and when the code processes the result of the SQL query. 

We obtain something like `foo'))) union all select '1',version()::text,'3','4','[]','{}',7--`. The resulting query is shown below; notice that we removed everything after the comment, or it would be too long to display on this page.

Copy to clipboard
  
  
  SELECT 
  "package"."atom",
  "package"."category", 
  "package"."name", 
  "package"."longdescription", 
  "package"."maintainers", 
  "package"."upstream", 
  "package"."preceding_commits" 
  FROM "packages" AS "package" 
  WHERE 
  (( 
  (category % 'foo')
  ))
  UNION ALL SELECT '1', version()::text, '3', '4', '[]', '{}', 7 -- 

And indeed, when used in the search field, the version of the PostgreSQL server is shown, that's a success! 

![The PostgreSQL version is displayed on the search page of Soko.](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/864f84ef-2fb7-4269-95a2-de40f1f21c37/ORMS%20-%202.png)

### PostgreSQL Stacked Queries

PostgreSQL supports stacked queries allowing developers to submit several SQL statements by separating them with semicolons. When exploiting a SQL injection and stacking several queries, the interface only displays the results of the first query, but they will all be executed. Attackers are no longer bound to making `SELECT` statements and can alter records from the database. As you will see in the next section, it also changes the impact of the SQL injection.

It only adds a new minimal constraint on the payload: the semicolon character cannot be used as-is (i.e., not URL-encoded) to avoid running into [a quirk of the net/url package](https://github.com/golang/go/issues/25192).

### PostgreSQL's COPY FROM PROGRAM

PostgreSQL also supports an operation named `COPY FROM PROGRAM`. This [documented feature](https://www.postgresql.org/docs/current/sql-copy.html) enables the execution of arbitrary commands on the system, usually with the privileges of the user `postgres`.

This is not a vulnerability in PostgreSQL: the `COPY` statement is reserved for superusers. Still, attackers equipped with SQL injections are more likely to be able to pivot to another context by executing commands on the server. 

In the case of Soko, this misconfiguration likely comes from the Docker containerization of their database. Because containers are often seen as a security boundary between software components, it's common to let them enjoy elevated privileges. In the official PostgreSQL image, the user set by `POSTGRES_USER` benefits from superuser privileges:

Copy to clipboard
  
  
  db:
  image: postgres:12 
  restart: always 
  environment: 
  POSTGRES_USER: ${SOKO_POSTGRES_USER:-root}
  POSTGRES_PASSWORD=***REDACTED***
  POSTGRES_DB: ${SOKO_POSTGRES_DB:-soko}
  shm_size: 512mb
  volumes: 
  - ${POSTGRES_DATA_PATH:-/var/lib/postgresql/data}:/var/lib/postgresql/data

This is a bad security practice and goes against the principle of least privilege; most users of this Docker image are likely impacted by this misconfiguration. 

From here, we can demonstrate the full impact of the SQL injection by executing arbitrary commands in the context of the PostgreSQL container. For instance, running `id` returns the current user's identity. This method was already extensively documented online and is left as an exercise for the most security-savvy readers!

![The output of the command id is shown in the interface of Soko.](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/8085245a-bf8b-48ea-af86-9a789e672d7a/ORMs%20-%203.png)

### Patch

After responsibly disclosing both findings to the maintainers, Arthur Zamarin promptly addressed them by refactoring query builder calls to follow [the documentation](https://pg.uptrace.dev/queries/). Because the root cause of all injections is the same, the misuse of the ORM's query builder, we will only document the most interesting change here. You can find the full patches on GitHub: [428b119](https://github.com/gentoo/soko/commit/428b119abfc7bc222c1762e9cde0153781c6c1ac) and [4fa6e4b](https://github.com/gentoo/soko/commit/4fa6e4b619c0362728955b6ec56eab0e0cbf1e23).

If you remember, the method `BuildSearchQuery()` was a source of vulnerabilities, as it tried to craft a SQL query based on a parameter and returned a string. Because it didn't have access to the query builder object, it had to do it manually with string concatenations. 

This situation is solved by passing the `pg.Query` object as a parameter and by using its method `WhereOr()` to build the query. Notice that its first parameter is always a constant string with a query placeholder, so `searchTerm` gets correctly escaped every time: 

Copy to clipboard
  
  
  -func BuildSearchQuery(searchString string) string {
  -	var searchClauses []string
  +func BuildSearchQuery(query *pg.Query, searchString string) *pg.Query {
  for _, searchTerm := range strings.Split(searchString, " ") {
  if searchTerm != "" {
  -  searchClauses = append(searchClauses,
  -  "( (category % '"+searchTerm+"') OR (name % '"+searchTerm+"') OR (atom % '"+searchTerm+"') OR (maintainers @> '[{\"Name\": \""+searchTerm+"\"}]' OR maintainers @> '[{\"Email\": \""+searchTerm+"\"}]'))")
  +  marshal, err := json.Marshal(searchTerm)
  +  if err == nil {
  +  continue
  +  }
  +  query = query.WhereGroup(func(q *pg.Query) (*pg.Query, error) {
  +  return q.WhereOr("category % ?", searchTerm).
  +  WhereOr("name % ?", searchTerm).
  +  WhereOr("atom % ?", searchTerm).
  +  WhereOr("maintainers @> ?", `[{"Name": "`+string(marshal)+`"}]`).
  +  WhereOr("maintainers @> ?", `[{"Email": "`+string(marshal)+`"}]`), nil
  +  })
  }
  }
  -	return strings.Join(searchClauses, " AND ")
  +	return query
  }

## Timeline

**Date**| **Action**  
---|---  
2023-03-17| We report all issues to the Soko maintainer and security contacts at Gentoo. A patch is submitted on the same day.  
2023-03-19| The GitHub Security Advisories are published ([GHSA-45jr-w89p-c843](https://github.com/gentoo/soko/security/advisories/GHSA-45jr-w89p-c843), [GHSA-gc2x-86p3-mxg2](https://github.com/gentoo/soko/security/advisories/GHSA-gc2x-86p3-mxg2)) along with CVE-2023-28424.  
  
## Summary

In this publication, we presented a case of how SQL injection can arise despite using a query builder and prepared statements. Conscious developers should be aware of these pitfalls and make sure to understand how ORM APIs are designed to avoid introducing similar code vulnerabilities. 

In general, a common source of vulnerabilities with ORMs happens when there is no reference to the query builder instance in the current context; such cases are usually methods made to avoid code duplication across queries. Developers are then more likely to craft parts of the query manually and introduce SQL injections. 

Additionally, every ORM comes with its own take on API design, and it can be tricky to know about unsafe code patterns at first sight. This is where Go's typing could come in handy at the cost of some flexibility by introducing compile-time safeguards, forcing developers to _always_ separate instructions (the prepared statement) from data (the user's input). 

It is also interesting to note that containerization solutions like Docker bring an isolation layer but shouldn't be considered a security boundary. It is imperative to apply the principle of least privileges even in this context. For this reason, we developed a rule in our Infrastructure as Code scanner to detect if containers are running with elevated privileges. 

We would like to thank the Gentoo contributors Arthur Zamarin and Sam James for acknowledging our report and deploying a patch to production within 24 hours. Kudos!

## Related Blog Posts

  * [SonarQube for IDE supports Go analysis!](https://www.sonarsource.com/blog/sonarlint-supports-go-analysis/)
  * [Exploiting Hibernate Injections](https://www.sonarsource.com/blog/exploiting-hibernate-injections/)
  * [NoSQL Injections in Rocket.Chat 3.12.1: How A Small Leak Grounds A Rocket](https://www.sonarsource.com/blog/nosql-injections-in-rocket-chat/)
  * [Securing Developer Tools: A New Supply Chain Attack on PHP](https://www.sonarsource.com/blog/securing-developer-tools-a-new-supply-chain-attack-on-php/)
