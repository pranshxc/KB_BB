---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-02-22_github-rce-writeup.md
original_filename: 2014-02-22_github-rce-writeup.md
title: GitHub RCE Writeup
category: blogs
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- blogs
- command-injection
- automation-abuse
language: en
raw_sha256: dc8242180f355936fa3c4ae31d5bb1c17e78753883c8f8a68eb372a9535515cf
text_sha256: 0b96b71fbbf08959ae42461e6483a609596dbe648888e3946aa5de4280f71366
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# GitHub RCE Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-02-22_github-rce-writeup.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `dc8242180f355936fa3c4ae31d5bb1c17e78753883c8f8a68eb372a9535515cf`
- Text SHA256: `0b96b71fbbf08959ae42461e6483a609596dbe648888e3946aa5de4280f71366`


## Content

---
title: "GitHub RCE Writeup"
page_title: "GitHub RCE Writeup :: 0day.click"
url: "https://0day.click/recipe/2014-02-22-github/"
final_url: "https://0day.click/recipe/2014-02-22-github/"
authors: ["joernchen (@joernchen)"]
programs: ["GitHub"]
bugs: ["RCE"]
publication_date: "2014-02-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6378
---

#  [GitHub RCE Writeup](https://0day.click/recipe/2014-02-22-github/)

2014-02-22

[Original gist](https://gist.github.com/joernchen/a7c031b6b8df5d5d0b61)
  
  
  GitHub RCE by Environment variable injection Bug Bounty writeup
  
  Disclaimer: I'll keep this really short but  I hope you'll get the key points.
  
  GitHub blogged a while ago about some internal tool called gerve:
  https://github.com/blog/530-how-we-made-github-fast
  
  Upon git+sshing to github.com gerve basically looks up your permission
  on the repo you want to interact with. Then it bounces you further in
  another forced SSH session to the back end where the repo actually is.
  
  At some point I figured that it is possible to inject some environment
  variables into gerve/the forked SSH process by setting my username to
  something like "joerchen\n\nLD_ASSUME_KERNEL=1\n\n".
  
  LD_ASSUME_KERNEL=1 will prevent the actual command from being run, just
  like this:
  
  ---
  joernchen ~ $ LD_ASSUME_KERNEL=1 uname -a
  uname: error while loading shared libraries: libc.so.6: cannot open shared object file: No such file or directory
  ---
  
  For the details on this, check man 8 ld.so.
  
  So far so good, how can we use this fact to make SSH execute arbitrary
  commands?
  
  The technique I came up with used both features of ld.so and SSH itself:
  
  LD_PRELOAD=/path/to/libfakeroot.so
  SSH_ASKPASS=/usr/bin/ex
  DISPLAY=:1
  
  How and why did this work?
  
  1.) libfakeroot makes SSH think it's root (we can inject this via
  LD_PRELOAD because the ssh binary is not setuid)
  2.) ssh tries to read /root/.ssh/known_hosts
  3.) ssh fails reading 'cause it's actually running as the git user
  4.) ssh connects to $backend and wants to ask the user if
  $backend_hostkey is OK.
  5.) ssh has no terminal and DISPLAY is set
  6.) ssh invokes the command specified in SSH_ASKPASS
  
  From being dropped in /usr/bin/ex we could just say:
  !/bin/sh
  and be happy with having a shell as git@github.com
  

* * *

[ < [CVE-2012-0809 Exploit] ](https://0day.click/recipe/2014-04-28-sudo-expoit/) :: [ [XXE to RCE] > ](https://0day.click/recipe/2012-09-04-xxe-to-rce/)
