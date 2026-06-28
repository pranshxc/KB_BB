---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-27_regular-expression-injection-a-code-review-low-hanging-fruit.md
original_filename: 2020-12-27_regular-expression-injection-a-code-review-low-hanging-fruit.md
title: Regular expression injection, a code review low hanging fruit
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 517acd9d902f022d533594dd6bd74a038a53073f5fda3165872f379b95d2d2c4
text_sha256: d293eecd68db71a9881ac50bd43313f02c3b1b3f32a4c785e6378b66d5a2af51
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Regular expression injection, a code review low hanging fruit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-27_regular-expression-injection-a-code-review-low-hanging-fruit.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `517acd9d902f022d533594dd6bd74a038a53073f5fda3165872f379b95d2d2c4`
- Text SHA256: `d293eecd68db71a9881ac50bd43313f02c3b1b3f32a4c785e6378b66d5a2af51`


## Content

---
title: "Regular expression injection, a code review low hanging fruit"
page_title: "Regular expression injection, a code review low hanging fruit | $BLOG_TITLE"
url: "https://blog.deesee.xyz/regex/security/2020/12/27/regular-expression-injection.html"
final_url: "https://blog.deesee.xyz/regex/security/2020/12/27/regular-expression-injection.html"
authors: ["Dominic (@dee__see)"]
bugs: ["ReDoS"]
publication_date: "2020-12-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4046
---

REGEX, SECURITY

# [Regular expression injection, a code review low hanging fruit](https://blog.deesee.xyz/regex/security/2020/12/27/regular-expression-injection.html)

December 27, 2020

Regular expression injection is a common bug that doesn’t get talked about a lot. This blog post covers how to find that bug and has 3 examples of vulnerabilities found in real applications.

The [OWASP top 10](https://owasp.org/www-project-top-ten/) lists injection vulnerabilities as the #1 web application security risk and describes them as such:

> Injection flaws, such as SQL, NoSQL, OS, and LDAP injection, occur when untrusted data is sent to an interpreter as part of a command or query. The attacker’s hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.

Regular expression (regex) injection doesn’t get a callout, but it’s part of that category and looking for it can be fairly simple.

Before we go further, I’d note that I’m going to assume the reader is familiar with regular expressions in this blog. If it’s not the case [regular-expression.info](https://www.regular-expressions.info/) and [regex101.com](https://regex101.com/) are great resources, but in my opinion this is really something you learn by doing so go ahead and `grep` all the things to get better! :)

## What’s the risk

Why even look for that type of vulnerability? It’s true that regex injection is generally a lot less severe than the other injection bugs. The danger of this vulnerability is [regular expression denial of service](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS). Follow that link if you’re not familiar with ReDoS, but the general idea is that regex injection allows the attacker to create a regex that performs _extremely_ poorly on purpose, causing the process to hang. While this will not allow an attacker to leak customer data or shell a server, it can slow down or even take down a service and if the vulnerability happens in something like an AWS Lambda it can create a very large bill.

## How to find it

Similar to all injection vulnerabilities, a regex injection happens when user input is used, unsanitized, to create a regular expression. What makes it a bit easier to spot than many other injection vulnerabilities however is that there are usually very few sinks.

> ❓ If you’re not familiar with the concept of sources and sinks, watch [this video by LiveOverflow](https://www.youtube.com/watch?v=ZaOtY4i5w_U) for a quick intro.

In general, regular expressions are defined either with a regex literal if the language supports it (Ruby, PHP, JavaScript, Perl and more)
  
  
  # ruby
  regex = /regex/
  

with an inline string
  
  
  // C#
  var regex = new System.Text.RegularExpressions.Regex("regex");
  

or with a reference to a constant
  
  
  // TypeScript
  const REGULAR_EXPRESSION = "regex";
  let regex = new RegExp(REGULAR_EXPRESSION)
  

While those can be vulnerable to ReDoS (that’s a blog post in itself), they’re definitely not vulnerable to regular expression injection and you can ignore all those declaration “patterns” when looking at the code for this type of vulnerability.

The interesting declaration patterns you want to look for are those with a variable (as opposed to a constant)
  
  
  // JavaScript
  function apiAction(arg1) {
  let regex = new RegExp(arg1 + 'some-suffix$');
  // ... regex is used later
  }
  

or languages that support interpolation inside a regex literal
  
  
  # ruby
  def api_action(arg1)
  regex = /#{arg1}some-suffix$/
  # ... regex is used later
  end
  

## How to exploit it

To demonstrate exploitation, here are a few examples I found and reported

> ❗ Testing for denial of service issues can have bad consequences on a live system. Given that you’re doing code review here, run the application locally and test only on your local version.

### GitLab

Public issue on GitLab.com: [Regular Expression Denial of Service in Elastic search results](https://gitlab.com/gitlab-org/gitlab/-/issues/257497)

When processing results from a code search, GitLab would use [this code](https://gitlab.com/gitlab-org/gitlab/-/blob/26962cded7d44900f7aab0d93b7095e3d518e1bb/ee/lib/gitlab/elastic/search_results.rb#L121):
  
  
  def self.parse_search_result(result, project)
  ref = result["_source"]["blob"]["commit_sha"]
  path = result["_source"]["blob"]["path"]
  extname = File.extname(path)
  basename = path.sub(/#{extname}$/, '')
  

The code here is creating a regular expression with a file’s extension to strip the extension from the file name. If a file is named `file.txt`, the regular expression `/.txt$/` is created. The file here however is a file pushed to a repository by a user, so it’s user input.

To exploit this, an attacker can create a file named `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab.(a+)+` with content `SEARCH_ME_REGEX_DOS_ISSUE` and then search for `SEARCH_ME_REGEX_DOS_ISSUE` which triggers the code above. The regex `/.(a+)+$/` will be created and when executed against the filename `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab.(a+)+` it will cause a regular expression denial of service.

The fix was simply to not use regular expressions when stripping the extension from the path.

### Public bug bounty program that doesn’t disclose bugs

This application stored data in a JSON file with a format like this
  
  
  {
  "property:name1": "value1",
  "property:name2": "value1",
  "otherKey": "other value"
  }
  

During a specific operation, it would iterate through the keys and run the following (slightly modified) code
  
  
  if key.match( /^property:#{get_prefix( input )}\/(.*)$/ )
  props.merge!( $1 => value )
  elsif key.match( /^property:#{get_prefix( input )}(\0.*)$/ )
  props.merge!( $1 => value )
  else
  props
  end
  

It was possible to name a certain object in that application with the name `a{1}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab|(a{0,}){0,}$|` which created this in the JSON file:
  
  
  {
  "property:a{1}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab|(a{0,}){0,}$|": "value1"
  }
  

and cause the code above to run the regex `/^property:a{1}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab|(a{0,}){0,}$|\/(.*)$/`

Why the `a{1}`? Because without it `/^property:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab|(a{0,}){0,}$|\/(.*)$/` would have actually matched the string `"property:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab|(a{0,}){0,}$|"` without problem.

Shoutout to [P4nda](https://twitter.com/InfoSecP4nda/) who collaborated with me on this, we found several instances of this vulnerable pattern in that application.

The fix here was to use [`Regexp.escape`](https://ruby-doc.org/core-2.7.1/Regexp.html#method-c-escape).

### Private bug bounty program

I like this last one because it’s a fairly common pattern. Many applications implement a feature where you can use `*` as a wildcard to search for things. For example if you want to build an API where searching for `dee*` should return both `dee-see` and `deesee`, you could create a regex from user input and change the `*` to `.*`. By now you might understand where this is going.

This API allowed the user to search if a job with a certain ID exists (ID here is any string, not limited to numbers). The code (mostly) looked like this:
  
  
  async function jobsExist(jobIds: string[] = []) {
  const { body } = await internalApi.getJobs<JobsResponse>({
  job_id: jobIds.join(),
  });
  
  const results: { [id: string]: boolean } = {};
  if (body.count > 0) {
  const allJobIds = body.jobs.map((job) => job.job_id);
  
  jobIds.forEach((jobId) => {
  const regexp = new RegExp(`^${jobId.replace(/\*+/g, '.*')}$`);
  const exists = allJobIds.some((existsJobId) => regexp.test(existsJobId));
  results[jobId] = exists;
  });
  } else {
  jobIds.forEach((jobId) => {
  results[jobId] = false;
  });
  }
  
  return results;
  }
  

Here an attacker could create a job named `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab` and then search for job IDs `["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", "(a+)+"]`. The `internalApi` call would return the existing `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab` job and then execute the regex `^(a+)+$` on it, causing the ReDoS.

Fun fact: this was actually redundant code, the internal API called at the beginning handled wildcards correctly and no regex filtering needed to be applied at all. The fix was basically to remove this code!

### Note on exploitability

Some languages are not vulnerable to ReDoS! Without going too deep into the technical details in this blog post, ReDoS is caused by regex backtracking and some regex engines don’t support that at all. Rust and golang’s default regex engines aren’t vulnerable and other languages might use a non-default engine like [`re2`](https://github.com/google/re2) (through a 3rd party dependency) that’s not vulnerable. Make sure the code base you are reviewing can actually be exploited!

## Regex injection RCE?

PHP had an `e` flag in regular expressions (deprecated in PHP 5.5.0, removed in 7.0.0) that evaluated the replacement in `preg_replace` as PHP code. See [this blogpost](https://medium.com/@roshancp/command-execution-preg-replace-php-function-exploit-62d6f746bda4) for more details.

## Avoiding this bug

If there’s an easy way to do the job without regex then you should consider using it (for example use a “starts with” function rather than building a regex with user input to check if a string begins with a given prefix). Otherwise, most programming languages will have a built-in function to escape special characters in a string before using it as a regex. See for example [`Regex.Escape` in C#](https://docs.microsoft.com/en-us/dotnet/api/system.text.regularexpressions.regex.escape?view=net-5.0) or [`Regexp.escape` in Ruby](https://ruby-doc.org/core-2.7.1/Regexp.html#method-c-escape). Unfortunately, the [proposal for a similar function in JavaScript](https://github.com/benjamingr/RegExp.escape/issues/43) wasn’t accepted…

## Conclusion

Regular expression injection is a fairly widespread bug that many people don’t pay attention to. It’s not the most critical finding, but it’s a fun one to look for, it’s fairly “greppable”, and if you’re getting into source code review for fun or bounties (or both!) you might want to add that to your arsenal.
