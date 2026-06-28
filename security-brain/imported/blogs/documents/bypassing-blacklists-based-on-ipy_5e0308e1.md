---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-10-15_bypassing-blacklists-based-on-ipy.md
original_filename: 2014-10-15_bypassing-blacklists-based-on-ipy.md
title: Bypassing blacklists based on IPy
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 5e0308e102c64777916aa067de62b4ca603d653e848c709f12b6b6e8bf1f88c5
text_sha256: e493416c5abd4e6a7f4031c1e379c4e5e8ace88359f5c2587999788182c0dd3c
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing blacklists based on IPy

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-10-15_bypassing-blacklists-based-on-ipy.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `5e0308e102c64777916aa067de62b4ca603d653e848c709f12b6b6e8bf1f88c5`
- Text SHA256: `e493416c5abd4e6a7f4031c1e379c4e5e8ace88359f5c2587999788182c0dd3c`


## Content

---
title: "Bypassing blacklists based on IPy"
page_title: "Bypassing blacklists based on IPy | Agarri : Sécurité informatique offensive"
url: "https://www.agarri.fr/blog/archives/2014/10/15/bypassing_blacklists_based_on_ipy/index.html"
final_url: "https://www.agarri.fr/blog/archives/2014/10/15/bypassing_blacklists_based_on_ipy/index.html"
authors: ["Nicolas Grégoire (@Agarri_FR)"]
programs: ["Prezi", "autocracy (python-ipy)"]
bugs: ["IP address validation bypass"]
bounty: "500"
publication_date: "2014-10-15"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 6364
---

* [Home](/en/index.html "Home page")
  * [Company](/en/company.html "Company details")
  * [Publications](/en/publications.html "Public interventions and published vulnerabilities")
  * [Trainings](/en/trainings.html "Burp Suite Pro training")
  * [Blog](/blog/ "Technical analysis and personnal opinions")
  * [ ![fr](/images/fr.png)](/fr/ "French version")

[Main](https://www.agarri.fr/blog/index.html) > [Archives](https://www.agarri.fr/blog/archives/index.html) > [2014](https://www.agarri.fr/blog/archives/2014/index.html) > [10](https://www.agarri.fr/blog/archives/2014/10/index.html) >  
[<](https://www.agarri.fr/blog/archives/2014/09/11/trying_to_hack_redis_via_http_requests/index.html) 12:04:30 [>](https://www.agarri.fr/blog/archives/2015/12/17/amf_parsing_and_xxe/index.html)

##  mercredi 15 octobre 2014, 12:04:30 (UTC+0200) 

### Bypassing blacklists based on IPy

A few months ago, when working on my [slides](/docs/Easy_hacks_for_complex_apps-INS14.pdf) for [Insomni'hack](http://insomnihack.ch/), I had a few conversations with the Prezi security team. Among many defense-in-depth protections, they introduced some code forbidding access to private IP addresses. Their conversion backend (the one I exploited) was using Python [urllib2](https://docs.python.org/2/library/urllib2.html), and the blacklist was implemented via the [IPy](https://github.com/haypo/python-ipy) library.

  

Given that I enjoy bypassing blacklists, I asked Prezi for this specific piece of code. And they gave it to me ;-) Thanks guys! So, The code they used looks like that:

  

  
  
  import urllib2, IPy
  from socket import gethostbyname
  from urlparse import urlparse
  
  def has_private_ip(url, logger_func=None):
  
  [... more checks ...]
  
  # Confirm IP type is not private
  is_private = IPy.IP(ip_address).iptype() == 'PRIVATE'
  if is_private:
  log('Invalid IP for URL (private): %s' % url)
  return is_private
  

  

The first thing to notice is that the [... more checks ...] part is quite complex by itself. Converting an URL to an IP address is not a trivial task in a security-sensitive context. For example, you may want to take care of HTTP redirects and DNS-rebinding attacks. But let's focus on the code checking if the IP address is private or not. There's a simple call to iptype(), a function of the IPy library. Prezi's wrapper around this call could be more paranoid: if the function returns something else than 'PRIVATE' (for example 'RESERVED'), then it would be considered as OK. Explicitly checking for 'PUBLIC' would be better.

  

Now, IPy. It defines a few IPv4 and IPv6 ranges, based on the first bits of the IP addresses. For IPv4:

  

  
  
  IPv4ranges = {
  '0':  'PUBLIC',  # fall back
  '00000000':  'PRIVATE',  # 0/8
  '00001010':  'PRIVATE',  # 10/8
  '01111111':  'PRIVATE',  # 127.0/8
  '1':  'PUBLIC',  # fall back
  '1010100111111110': 'PRIVATE',  # 169.254/16
  '101011000001':  'PRIVATE',  # 172.16/12
  '1100000010101000': 'PRIVATE',  # 192.168/16
  '111':  'RESERVED', # 224/3
  }
  

  

This code too could be more paranoid: the fallbacks are 'PUBLIC', so subverting the parsing logic may bypass the blacklist. Under the hood, the iptype() function converts the IP address to a list of bits using strBin() and then tries to match this list against the previously shown IP ranges:

  

  
  
  def iptype(self):
  
  bits = self.strBin()
  for i in xrange(len(bits), 0, -1):
  if bits[:i] in IPv4ranges:
  return IPv4ranges[bits[:i]]
  return "unknown"
  

  

As you may have notice, a fourth state ('unknown') appears, but it can't be reached because of the fallbacks. Unless you can produce bits different of both '0' and '1' :-o

  

Now that the context is defined, let's do some hacking. Given that urllib2 supports tons of formats for IP addresses, maybe we could find a format misinterpreted by IPy and then wrongly considered as non 'PRIVATE'. Go go fuzzing!

  

  
  
  import IPy
  
  loopback = [
  '127.0.0.1',  # Normal
  '2130706433',  # Integer
  '0x7F000001',  # Hexa
  '0x7F.0x00.0x00.0X01', # Hexa - dotted
  '0177.0000.0000.0001', # Octal
  ]
  
  for ip in loopback:
  print ip + ':',
  try:
  print IPy.IP(ip).iptype()
  except:
  print 'Problem in IPy'
  

  

Simple setup: five ways to encode the loopback address, each of them supported by urllib2. The results?

  

  
  
  127.0.0.1: PRIVATE
  2130706433: PRIVATE
  0x7F000001: PRIVATE
  0x7F.0x00.0x00.0X01: Problem in IPy
  0177.0000.0000.0001: PUBLIC
  

  

Both the normal and integer formats are correctly considered as 'PRIVATE'. The hexadecimal format is OK too if not dotted. The dotted version will trigger a _'ValueError: invalid literal for int() with base 10'_ exception in parseAddress() when initializing the IPy object. Depending on how the code is structured, this could be enough for bypassing a filter. But the most interesting format is the octal one. '0177.0000.0000.0001' is considered as 'PUBLIC' by IPy and resolved to '127.0.0.1' by urllib2, that's a perfect fit! If we try to generalize the tests (using 10/8, 192.168/16, 169.254.169.254, ...), it appears that the hexadecimal dotted format will always raise the same exception. And that the octal format will confuse IPy a lot:

  

  
  
  [=] 0177.0000.0000.0001 (127.0.0.1)
  [+] PUBLIC - Fallback 1
  
  [=] 0251.0376.0251.0376 (169.254.169.254)
  [!] '0251.0376.0251.0376': single byte must be 0 <= byte < 256
  
  [=] 0300.0250.0001.0002 (192.168.1.2)
  [!] '0300.0250.0001.0002': single byte must be 0 <= byte < 256
  
  [=] 0254.0020.0003.0004 (172.16.3.4)
  [+] RESERVED
  
  [=] 0012.0013.0014.0015 (10.11.12.13)
  [+] PUBLIC - Fallback 0
  

  

The bug was reported to IPy's maintainer (Jeff Ferland aka autocracy) in March. No news since then :-( Prezi patched their own filter and awarded me $500. Not a big payout, but the real impact was near null in their setup. Thanks defense in depth mechanisms! Anyway, if you are using IPy, maybe you should take care of these bypasses...

  
Posted by Nicolas Grégoire | [Permanent link](https://www.agarri.fr/blog/archives/2014/10/15/bypassing_blacklists_based_on_ipy/index.html)

/\

###  webmaster@agarri.fr  
Copyright 2010-2021 Agarri
