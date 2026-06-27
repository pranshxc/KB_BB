---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '398400'
original_report_id: '398400'
title: 'AWS Credentials leaked: access to production database backups, SSL certs and
  more'
team_handle: redact
created_at: '2016-10-21T07:33:16.000Z'
disclosed_at: '2018-08-23T08:24:33.750Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 77
tags:
- hackerone
---

# AWS Credentials leaked: access to production database backups, SSL certs and more

## Metadata

- HackerOne Report ID: 398400
- Weakness: 
- Program: redact
- Disclosed At: 2018-08-23T08:24:33.750Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found a public accessible Jenkins instance: https://██████jenkins.██████.com

This instance requires login, however, it is possible to register an account using the signup page:
https://██████jenkins.██████.com/signup

### Arbitrary file reads

From there it is possible to use the Jenkins Script Console to read information on the system:
https://██████jenkins.██████.com/script

For example: /etc/passwd

`"cat /etc/passwd".execute().text`
```
root:x:0:0:root:/root:/bin/bash
[...]
██████:x:530:530:██████:/home/██████:/bin/bash
██████:x:558:558:██████:/home/██████:/bin/bash
[...]
```

## AWS Credentials

The jenkins user has AWS credentials set up in its home dir: `/mnt/ephemeral/var/lib/jenkins/.aws/credentials`

With these credentials it is possible to:

- list all EC2 instances (~480), including hostnames, state, security groups (internal) IP addresses et cetera. See attached `ec2_instances.txt`
- read all S3 buckets. List of bucket names attached `s3_buckets.txt`

## S3 buckets

The account has access to 168 S3 buckets. I scanned through these to see if there was anything interesting. The most interesting ones found:

- s3://s3.██████.com/backups/
- s3://s3.██████.com/backups/ssl/
- s3://s3.██████.com/backups/██████prodmysql/20161021/
- s3://atlassian-backups.██████ops.com/
- s3://backups.██████ops.com/██████svn/

### backups/ssl

This contains several SSL certificates:
```
✓ ls -l ssl/certs/
total 0
[...]
drwxr-xr-x 5 tom staff 170 May 18 02:08 m.██████.com
drwxr-xr-x 3 tom staff 102 Jan 13  2015 ██████.██████.com
drwxr-xr-x 4 tom staff 136 Feb 23  2015 ██████.██████.com
drwxr-xr-x 4 tom staff 136 May  8  2015 secure.██████.com
drwxr-xr-x 3 tom staff 102 Jan 13  2015 secure.██████.com
[...]
drwxr-xr-x 4 tom staff 136 May 18 02:10 wildcard.██████.com
drwxr-xr-x 3 tom staff 102 May 18 02:12 wildcard.██████.com
[...]
drwxr-xr-x 4 tom staff 136 May 18 02:09 wildcard.██████.com
drwxr-xr-x 6 tom staff 204 Jul 21 16:39 www.██████.cn
drwxr-xr-x 4 tom staff 136 Oct 21 18:45 www.██████.com
```

### backups/██████prodmysql/20161021/

Looking at the naming convention and content of this directory I'm pretty confident this is an actual backup of todays production data. The directory contains a ~40GB large bzipped file called: ██████prodmysql.20161021.tar.bz2

I don't want to go further and actually access that data, but based on what data you appear to store in your application this backup could contain:

- email addresses;
- (hashed) passwords;
- social security numbers;
- and/or credit card numbers;
- and/or bank account numbers;
- and/or address information.

Since ██████ is using the ██████ API I expect W9 tax form data to be stored here as well. Ref: https://www.██████.com/help/faq

Can you confirm my assumptions on the production database are correct?

### backups/*

Several other interesting folders found, but no need digging in to that as I think this report has already proved its point so far.

# Mitigation

- Take the Jenkins instance down!
- Cycle the AWS access tokens used by the Jenkins user

Please let me know if there is anything else I can do to help out or if anything is unclear.

Regards,
Tom

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
