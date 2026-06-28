---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-29_httpsleigh-annegallowaycomtumblr.md
original_filename: 2018-06-29_httpsleigh-annegallowaycomtumblr.md
title: https://leigh-annegalloway.com/tumblr/
category: documents
detected_topics:
- rate-limit
- automation-abuse
- sso
- idor
- command-injection
- information-disclosure
tags:
- imported
- documents
- rate-limit
- automation-abuse
- sso
- idor
- command-injection
- information-disclosure
language: en
raw_sha256: 170efbf3f0547624d86ce8ca9720be69b3483c2862335f77ae0cdc4bf6b3d529
text_sha256: 4edc257070c9e6b1f517e268743da2f9b417d6ce9aa3528df8f836565c7eb022
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# https://leigh-annegalloway.com/tumblr/

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-29_httpsleigh-annegallowaycomtumblr.md
- Source Type: markdown
- Detected Topics: rate-limit, automation-abuse, sso, idor, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `170efbf3f0547624d86ce8ca9720be69b3483c2862335f77ae0cdc4bf6b3d529`
- Text SHA256: `4edc257070c9e6b1f517e268743da2f9b417d6ce9aa3528df8f836565c7eb022`


## Content

---
title: "https://leigh-annegalloway.com/tumblr/"
page_title: "Bug Bounty: Tumblr reCAPTCHA vulnerability write up"
url: "https://leigh-annegalloway.com/tumblr/"
final_url: "https://leigh-annegalloway.com/tumblr/"
authors: ["Leigh-Anne Galloway (@L_AGalloway)"]
programs: ["Automattic"]
bugs: ["Captcha bypass", "Username enumeration", "Information disclosure"]
publication_date: "2018-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5821
---

[Leigh-Anne Galloway](https://leigh-annegalloway.com)

  * [Twitter](https://x.com/L_AGalloway "Twitter")
  * [RSS](https://feedly.com/i/subscription/feed/https://leigh-annegalloway.com/rss/)

June 29, 2018

# Bug Bounty: Tumblr reCAPTCHA vulnerability write up

On the 16th of June, HackerOne paid out over $80,000 in rewards during their first London meetup. Bug bounties are big business, and for good reason. Bug bounty programs incentivise security researchers to report security issues in an organised manner.

![Bug Bounty: Tumblr reCAPTCHA vulnerability write up](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/tumblr-article-icon.jpg)

On the 16th of June, HackerOne paid out over $80,000 in rewards during their first London meetup. Bug bounties are big business, and for good reason. Bug bounty programs incentivise security researchers to report security issues in an organised manner. Not only do they compensate researchers, they also drive up the quality of reporting so that an organisation has the full details required to quickly fix the issue that has been identified. Security is hard, and even big companies can make trivial mistakes. Bug bounty fills a gap between internal resources and external adversaries. It’s also impossible to internally recruit the quality and diversity of security testers that you can gain access to through external programs such as Bugcrowd and Hacker One, or consultancy services.

I’ve personally had experience of both good and bad handling of security issue reporting. Last year I reported an issue to Myspace, a critical vulnerability which allowed access to any user account. Yes, any user account. After many attempts to make contact with Myspace, I decided to publicly disclose this issue. Why did I choose to publicly disclose? This particular issue affected over 360 million user accounts. Times Warner, the owners of MySpace have a duty of care to protect user accounts on this website. You can read the original article [here](https://leigh-annegalloway.com/myspace/). Public pressure was sufficient for them to implement a solution to close the vulnerability. This is not a favourable course of action, but in some cases, the only option is to publicly disclose the security issue.

**TUMBLR RECAPTCHA VULNERABILITY**

In contrast, I had an excellent experience reporting a security issue to Tumblr this year. I contacted Tumblr in October last year, using their security and reports [form](https://www.tumblr.com/security?ref=leigh-annegalloway.com). Unfortunately, my report was not received. In January I reached out to Tumblr on twitter. They were quick to respond to me through direct mail, and I was able to directly email my findings to one of their security engineers. Two days later, they confirmed that the vulnerability had been closed. The rest of this article covers the technical details of this vulnerability.  
I identified a misconfiguration in the implementation of google reCAPTCHA during the account registration process on www.tumblr.com. The Google reCAPTCHA value sent by the client and the application allows for the paramenter ‘g-recaptcha-response’ to be empty. This vulnerability affects all new account creation and it doesn’t require any special tools to exploit. This can be done manually by the user by clicking the buttons in the application, or by intercepting the HTTP request in a tool such as burp.

**IMPACT**

Captcha if implemented properly is rate limiting, it should prevent spammers from creating fake social media accounts and reduce the volume of requests to a given application. This misconfiguration allowed for fake accounts can be created. It also had the potential for email and username enumeration; because the application prohibits more than one username being associated with one email during the account sign up process.

**HOW IT WORKS**

In order to understand how this works, lets take a look at the normal page flow for account creation on www.tumblr.com. The first page you are presented with is the login page. You can navigate to the signup page by clicking on ‘Sign up’.

![001-2](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/001-2.jpg)

This takes us to the first page in the account creation process, the ‘register’ page.

![002-1](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/002-1.jpg)

Click on ‘Get Started’ and you are presented with a number of fields to complete; username, password and email.

![003-3](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/003-3.jpg)

Once we have completed this initial information we are asked to agree to the sites terms and agreements.

![004-1](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/004-1.jpg)

Finally, we are asked to complete a reCAPTCHA form to confirm that we are human.

![005-1](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/005-1.jpg)

![006-1](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/006-1.jpg)

The web application itself isn’t checking that the user has completed a reCAPTCHA check. So instead of clicking on “I’m not a robot”. Instead I can click on “Almost Done!”

![007-1](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/007-1.jpg)

This will will take me to the dashboard of my newly created account, therefore bypassing the reCAPTCHA check entirely!

![008](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/008.jpg)

If that wasn’t clear, check out this video which demonstrates how this works

So what is actually going on here? Let’s take a closer look at the request and response for a user who has successfully completed the reCAPTCHA challenge.

![009](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/009.jpg)

If you look at the POST parameters for this request you can see that the captcha challenge has a value in the argument ‘g-recaptcha-response’. But when we choose not to complete the captcha challenge our request looks like this:

![010](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/010.jpg)

In this case the request does not contain a value for the parameter ‘g-recaptcha-response’. But both requests provide the same valid response from the server:

![11](https://storage.ghost.io/c/1e/a5/1ea5e30e-732a-4b6d-b2c3-44a9c9e3f681/content/images/2018/06/11.jpg)

So what is actually going on here? The server isn’t checking for the parameter ‘g-recaptcha-response’ to have a value.

This is actually a more common issue than you might expect. Authentication vulnerabilities exist in many applications, even those that demand a high level of confidence from their user base. In May, Google had to fix a vulnerability that allowed for complete bypass of [Google reCAPTCHA](http://https//threatpost.com/google-patches-recaptcha-bypass/132335/?ref=leigh-annegalloway.com)

[ Author LA Galloway Read more posts by this author. ](/author/la/)
