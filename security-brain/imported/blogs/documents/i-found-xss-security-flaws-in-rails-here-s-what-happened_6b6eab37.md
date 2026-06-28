---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-07_i-found-xss-security-flaws-in-rails-heres-what-happened.md
original_filename: 2020-05-07_i-found-xss-security-flaws-in-rails-heres-what-happened.md
title: I Found XSS Security Flaws in Rails – Here's What Happened.
category: documents
detected_topics:
- access-control
- xss
- idor
- command-injection
- cloud-security
tags:
- imported
- documents
- access-control
- xss
- idor
- command-injection
- cloud-security
language: en
raw_sha256: 6b6eab37f9cfd24f7ac227c21d7b644172226a666a699ea5e99602d295ae04d8
text_sha256: 36a54273bc4a4965bfb089d738a7d5da0271f22f6faa5e4a9918e19cba1d8f7e
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# I Found XSS Security Flaws in Rails – Here's What Happened.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-07_i-found-xss-security-flaws-in-rails-heres-what-happened.md
- Source Type: markdown
- Detected Topics: access-control, xss, idor, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `6b6eab37f9cfd24f7ac227c21d7b644172226a666a699ea5e99602d295ae04d8`
- Text SHA256: `36a54273bc4a4965bfb089d738a7d5da0271f22f6faa5e4a9918e19cba1d8f7e`


## Content

---
title: "I Found XSS Security Flaws in Rails – Here's What Happened."
page_title: "I Found XSS Security Flaws in Rails – Here's What – Chef Secure"
url: "https://chefsecure.com/blog/i-found-xss-security-flaws-in-rails-heres-what-happened"
final_url: "https://chefsecure.com/blog/i-found-xss-security-flaws-in-rails-heres-what-happened"
authors: ["Jesse Campos"]
programs: ["Ruby on Rails"]
bugs: ["XSS"]
bounty: "500"
publication_date: "2020-05-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4600
---

#  [ ![Chef Secure](https://chefsecure.com/assets/logo-tr-733a12e308c32d3d2752829ddf90e91a6b2576bccd84c9e5b379690b7c841f59.png) ](/)

MENU

  * [Cross Site Scripting (XSS) Course __](/courses/xss)

Learn one of the most common security flaws on the web — allowing you to hijack accounts, steal data and take over entire webpages. 

  * [The No-Code Hacking Course __](/courses/no-code-hacking-course)

Beginner-friendly hacking without any coding experience required — get hands-on experience hacking with high-severity vulnerabilities like IDOR, Sensitive Data Exposure, Broken Authentication and Broken Access Control. 

  * [XSS Probes Dashboard __](https://chefsecure.com/xss-probes)

Use XSS Probes to find hidden vulnerabilities in websites. 

  * [Contact us __](/contact)

Stuck on a challenge, have questions or need help? We'd love to hear from you. 

Share this page:

[__](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fchefsecure.com%2Fblog%2Fi-found-xss-security-flaws-in-rails-heres-what-happened) [__](https://twitter.com/share?hashtags=chefsecure&url=https%3A%2F%2Fchefsecure.com%2Fblog%2Fi-found-xss-security-flaws-in-rails-heres-what-happened) [__](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fchefsecure.com%2Fblog%2Fi-found-xss-security-flaws-in-rails-heres-what-happened) [__](mailto:?Subject=Check this out!Body=Look what I found on Chef Secure! https://chefsecure.com/blog/i-found-xss-security-flaws-in-rails-heres-what-happened)

[LOGIN](/login) [SIGN UP](/join)

# I Found XSS Security Flaws in Rails – Here's What Happened.

  1. [Home](/)
  2. [Blog](/blog)
  3. I Found XSS Security Flaws in Rails – Here's What Happened 

![I Found XSS Security Flaws in Rails – Here's What Happened](https://chefsecure.com/assets/tw-i-found-xss-security-flaws-in-rails-heres-what-happened-c755bfa9c939557ee16ec48770ba15729170db06eb32edddb6591504ef46594a.png)

Take a look at this code: 
  
  
  JS_ESCAPE_MAP = {
  "'"  => "\\'",
  '"'  => '\\"',
  '\\'  => '\\\\',
  "\r\n" => '\n',
  "\n"  => '\n',
  "\r"  => '\n',
  }
  
  def escape_javascript(javascript)
  # replace every unsafe character with safe version
  return javascript.gsub(/(\\|\r\n|[\n\r"'])/u, JS_ESCAPE_MAP)
  end

This is a simplified version of what protects JavaScript strings in the Ruby on Rails framework from attacks. 

Except for the past 5 years, there've been 2 things missing that could still allow attackers a way in. 

So what's wrong with it? 

Ruby on Rails is a web framework used for quickly building web applications with minimal setup and configuration. 

Although it's isn't so trendy anymore, it's stable and reliable in most cases so it's still used by a lot of companies like Github, Shopify, Airbnb, Soundcloud and even here at Chef Secure. 

##  Here's the problem 

The code I showed you earlier is a function used by developers to escape untrusted data for safe use in JavaScript strings. 

You can use it like this: 
  
  
  string = '<%= j untrusted_data %>'

or like this 
  
  
  string = '<%= escape_javascript untrusted_data %>'

And it'll stop untrusted data from running malicious code in XSS attacks. 

As you know, JavaScript strings can be created with single or double quotes. However when ES6 was introduced in 2015, it added a new way to create strings using what's called template literals. 
  
  
  'string1'
  "string2"
  `string3`

The difference: template literals allow you to build strings while including variables and expressions inside. 

## Walking through the vulnerability

Here's an example. Let's say you want to show a user's online status using their name and a `getStatus` function that takes in their id so the end result looks like this: 

Jesse is Online 

The old way would be to add the different pieces of the string together. 
  
  
  '<%= j user.name %> is ' + getStatus(<%= user.id %>)

The new way with template literals allows you to combine these pieces together inside a single string: 
  
  
  `<%= j user.name %> is #{getStatus(<%= user.id %>)}`

So how do we exploit this? 

As I go over in the Attacks inside JavaScript recipe [in my XSS course](/courses/xss), the most common way attackers achieve XSS in JavaScript is by breaking out of strings in order to get into the execution context - the place where your code gets run. 

Now, in contrast to HTML where you can have invalid syntax without much consequence, JavaScript is very picky and will stop working with even the smallest error, so you need to make sure you end up with valid JavaScript after your injection. 

The pattern I present in the recipe is simple: 

  * start with your payload (`alert()`)
  * surround it with matching string characters
  * and finally add a plus in between each part

stringChar+alert()+stringChar 

This allows you to break out of JS strings without errors – just like adding in a new variable. 

Do you see what's missing now? 

## The first attack

The escaping doesn't account for backticks being used to create strings via template literals. In this case, this means we can run our exploit using the exact same pattern with backticks for the string characters. 
  
  
  `+alert()+`

Okay, so let's add protection from backticks. 
  
  
  JS_ESCAPE_MAP = {
  "'"  => "\\'",
  '"'  => '\\"',
  '`'  => '\\`',
  ...
  
  def escape_javascript(javascript)
  # replace every unsafe character with safe version
  return javascript.gsub(/(\\|\r\n|[\n\r"'`])/u, JS_ESCAPE_MAP)
  end

##  There's still another problem 

It turns out that the same benefit offered by template literals to combine expressions inside strings, also allows attackers to execute malicious code without even having to break out of the string! 

So to launch an attack this time, we'd just surround our payload with the `${}` interpolation piece and we don't have to worry about any extra parts. 
  
  
  ${alert()}

And now the second fix is to escape the `$` character to stop this. 
  
  
  JS_ESCAPE_MAP = {
  "'"  => "\\'",
  '"'  => '\\"',
  '`'  => '\\`',
  '$'  => '\\$',
  ...
  
  def escape_javascript(javascript)
  # replace every unsafe character with safe version
  return javascript.gsub(/(\\|\r\n|[\n\r"'`$])/u, JS_ESCAPE_MAP)
  end

## We were warned

It turns out this scenario was already discussed 8 years ago. 

After the Rails patch was released, [James Kettle](https://twitter.com/albinowax), Director of Research at [PortSwigger](https://portswigger.net/), sent me a message on Twitter linking to a discussion on adding template literals to JavaScript where [Gareth Heyes](https://twitter.com/garethheyes) warns about the holes that will open up as a result. 

Gareth warns: 

... this will introduce a new class of DOM based XSS attacks since developers in their infinite wisdom will use this feature to place user input inside ... 

_[Read the full discussion here](https://esdiscuss.org/topic/implicitly-escaped-or-not-in-quasis). _

## What else is vulnerable?

Considering that I appear to be the first to report this type of vulnerability and how long it's remained unpatched, it makes me wonder how often it's been exploited in the wild and what other frameworks and modules share this same problem. 

### Timeline

This issue has taken over a year to fix since originally reporting to the Rails team. 

![Awkward Silence Rails Logo](https://chefsecure.com/assets/blog/rails-awkward-silence-d4ba20aa1cbeaff8339254cec9ebc9f9669f3274144e1aa094097bf71d87691d.png) _At least HackerOne has a badge for Patience_

  * January 3, 2019: Submitted issue with solution to fix on HackerOne 
  * January 3, 2019: Received response on addressing issue
  * February 6, 2019: Follow up for status and offered dev assistance
  * May 21, 2019: Follow up for status
  * January 21, 2020: Follow up for status and verified issue on most recent release 
  * February 5, 2020: Received assistance from HackerOne staff to contact Rails team 
  * March 5, 2020: Follow up for status
  * March 6, 2020: HackerOne staff escalated issue internally
  * March 12, 2020: Patch created by [Tenderlove](https://twitter.com/tenderlove) and fix was verified 
  * March 19, 2020: Official patch released
  * March 24, 2020: Request made to close issue
  * April 8, 2020: Follow up for status
  * April 9, 2020: Received assistance from HackerOne staff
  * May 4, 2020: Follow up for status
  * May 5, 2020: Issue closed and $500 bounty awarded

_P.S. Despite the long timeframe for getting this fixed, the hard work of the Rails team and HackerOne staff is still appreciated ✌️_

-[Jesse](https://www.linkedin.com/in/jesse-campos)

Share: [__](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fchefsecure.com%2Fblog%2Fi-found-xss-security-flaws-in-rails-heres-what-happened) [__](https://twitter.com/share?hashtags=chefsecure&url=https%3A%2F%2Fchefsecure.com%2Fblog%2Fi-found-xss-security-flaws-in-rails-heres-what-happened) [__](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fchefsecure.com%2Fblog%2Fi-found-xss-security-flaws-in-rails-heres-what-happened) [__](mailto:?Subject=Check this out!Body=Look what I found on Chef Secure! https://chefsecure.com/blog/i-found-xss-security-flaws-in-rails-heres-what-happened)

### Start learning

Hacking Websites With Cross-Site Scripting

[WATCH NOW](/courses/xss/recipes/hacking-websites-with-cross-site-scripting)

### Like | Subscribe | Follow

  * [__](https://www.youtube.com/channel/UCqx-vnWwxXQEJ0TC5a6vuNw)
  * [__](https://www.facebook.com/chefsecure)
  * [__](https://twitter.com/chefsecure)
  * [__](https://www.linkedin.com/company/chefsecure)

## Ready to master XSS?

The Ultimate XSS Training Course gives you the full, uncensored picture of Cross-Site Scripting from the perspectives of criminal hackers and the engineers whose job it is to stop them. 

![Cross-Site Scripting icon](https://chefsecure.com/assets/xss-icon-5bce1ff993d3a5ad3d7b9c9cf4777e5e8796c4b9e18d08686ec5359cd2720079.png)

## Cross-Site Scripting

Cross-Site Scripting (XSS) is the **#1 most common** appsec vulnerability that allows attackers to steal private data, hijack accounts and spread ransomware on your sites. This course teaches students to: 

__

Discover critical XSS vulnerabilities in web applications. 

__

Create, analyze and stop malicious exploits used by criminal hackers. 

__

Fix XSS vulnerabilities in routine and emergency situations. 

__

Stop costly vulnerabilities before they reach production using the latest best practices and techniques. 

[SEE THE COURSE](/courses/xss) [START LEARNING](/courses/xss/recipes/hacking-websites-with-cross-site-scripting)

**Courses**

[Cross Site Scripting (XSS)](/courses/xss)

[The No-Code Hacking Course](/courses/no-code-hacking-course)

**Learn More**

[About Chef Secure](/about)

[Chef Secure Blog](/blog)

**Support**

[Contact](/contact)

[Security](/security)

[Terms of use](/terms)

[Privacy policy](/privacy)

[Success disclaimer](/success-disclaimer)

Chef Secure, LLC © 2026 - All rights reserved.
