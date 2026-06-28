---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-03-13_airbnb-ruby-on-rails-string-interpolation-led-to-remote-code-execution.md
original_filename: 2017-03-13_airbnb-ruby-on-rails-string-interpolation-led-to-remote-code-execution.md
title: Airbnb – Ruby on Rails String Interpolation led to Remote Code Execution
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: f48916d6962adebee4be709355f444823f441d25d394678c14849ee9cadddcf2
text_sha256: 40ea77acd7775420de7fd557fd73c26895b1b68864c92684fc30ffdb7821f3c0
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Airbnb – Ruby on Rails String Interpolation led to Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-03-13_airbnb-ruby-on-rails-string-interpolation-led-to-remote-code-execution.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `f48916d6962adebee4be709355f444823f441d25d394678c14849ee9cadddcf2`
- Text SHA256: `40ea77acd7775420de7fd557fd73c26895b1b68864c92684fc30ffdb7821f3c0`


## Content

---
title: "Airbnb – Ruby on Rails String Interpolation led to Remote Code Execution"
page_title: "Airbnb – Ruby on Rails String Interpolation led to Remote Code Execution | ziot"
url: "https://buer.haus/2017/03/13/airbnb-ruby-on-rails-string-interpolation-led-to-remote-code-execution/"
final_url: "https://buer.haus/2017/03/13/airbnb-ruby-on-rails-string-interpolation-led-to-remote-code-execution/"
authors: ["Brett Buerhaus (@bbuerhaus)", "Ben Sadeghipour (@nahamsec)"]
programs: ["Airbnb"]
bugs: ["RCE"]
publication_date: "2017-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6209
---

# Airbnb – Ruby on Rails String Interpolation led to Remote Code Execution

March 13, 2017February 25, 2024

![airbnb_horizontal_lockup_print](https://buer.haus/wp-content/uploads/2016/05/airbnb_horizontal_lockup_print.jpg)

Authors:

  * [![image](https://abs.twimg.com/errors/logo23x19.png) Ben Sadeghipour](https://twitter.com/nahamsec)
  * [![image](https://abs.twimg.com/errors/logo23x19.png) Brett Buerhaus](https://twitter.com/bbuerhaus)

[@nahamsec](https://twitter.com/nahamsec) and I discovered a Cross-Site Scripting vulnerability a few months ago related to Rails typecasting request variables into JSON. This caused the output to be JSON formatted and the JSON indexes would avoid XSS encoding. We decided to run with this concept and explore the rest of the website to see if we could identify other vulnerabilities using the same method. Along the way we discovered an interesting output from the /api/v1/listings/[id]/update API request. This led us to finding a Remote Code Execution vulnerability on Airbnb due to Ruby on Rails string interpolation.

This is what the API request typically looks like:

>  * https://www.airbnb.com/api/v1/listings/[id]/update
>  * POST: {"listing":{"directions":"test"}}
> 

This is what it looks like to turn the listing directions string into an array:

>  * https://www.airbnb.com/api/v1/listings/[id]/update
>  * POST: {"listing":{"directions":[{"test":"test1"}]}}
> 

After turning it into an array, this is the output it was giving:
  
  
  "directions":"---\n- !ruby/hash:ActionDispatch::Http::ParamsHashWithIndifferentAccess\n  test: test1\n"

It wasn't the first time we had seen this, as there were other POST requests that resulted in a similar output:
  
  
  --- !

We were unfamiliar with the YAML format and it wasn't until we discovered the **!ruby** output and talked to [Jobert](https://twitter.com/jobertabma/) that we realized this was input inside of a YAML parser. Any attempt at exploiting this as a downstream Rails YAML deserialization attack failed. Any YAML formatted string in the input would be placed inside of quotes or escaped.

During our fuzzing, we were messing with different types of Rails features. We eventually landed on [string interpolation](http://ruby-for-beginners.rubymonstas.org/bonus/string_interpolation.html) and noticed it evaluated.
  
  
  {"listing":{"directions":[{"test":[{"abc":"#{1+1}"}]}] }}

Result: abc: ! '2'\n

This discovery made us realize that even though we were inside quotes we were able to use #{} to evaluate code. Using the **%x** arg we were able to execute shell commands.

>  * https://www.airbnb.com/api/v1/listings/[id]/update
>  * POST: {"listing":{"directions":[{"test":[{"abc":"#{%x['ls']}+foo"}]}] }}
> 

Result:

[![ls](https://buer.haus/wp-content/uploads/2017/02/ls.png)](https://buer.haus/wp-content/uploads/2017/02/ls.png)

**Thanks:**

  * [Jobert Abma](https://twitter.com/jobertabma/)

**Timeline:**

  * 2/11/2017: Initial discovery of potential flaw (did not report)
  * 2/20/2017: Verified and reported (Holiday)
  * 2/21/2017: Fixed
