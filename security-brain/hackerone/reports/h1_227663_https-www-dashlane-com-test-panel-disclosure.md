---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '227663'
original_report_id: '227663'
title: '[https://www.dashlane.com] Test Panel Disclosure'
team_handle: dashlane
created_at: '2017-05-11T09:30:00.142Z'
disclosed_at: '2017-07-21T18:45:05.191Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
---

# [https://www.dashlane.com] Test Panel Disclosure

## Metadata

- HackerOne Report ID: 227663
- Weakness: 
- Program: dashlane
- Disclosed At: 2017-07-21T18:45:05.191Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Greetings,

On https://www.dashlane.com/ , I observed that the server discloses test panel at :

https://www.dashlane.com/app/tests/

{F183690}

I found no relation between an account and the following page to do unauthorized tests.

The following tests are available with no credential :
==

- https://www.dashlane.com/app/tests/encrypt.html
- https://www.dashlane.com/app/tests/decrypt.html
- https://www.dashlane.com/app/tests/deflate.html
- https://www.dashlane.com/app/tests/inflate.html
- https://www.dashlane.com/app/tests/unittest.html

For example it was possible to extract a salt or obtain various information :
==

        Debug Start encodingReceived (length: 1)1Start compressingDeflating raw input: (length: 1)49:Hex: (length: 2)31Input Base64: (length: 4)MQ==Deflating with level 7Deflated value: (length: 3)3After deflating Base64: (length: 20)AAAAAXjaMwQAADIAMg==Done compressingIn byte array: (length: 13)0:0:0:1:120:218:51:4:0:0:50:0:50:Actual data: (length: 13)0:0:0:1:120:218:51:4:0:0:50:0:50:Preparing 5 salts.Start calculating PBKDF2Feeding PBKDF2 with:- salt: '»iõòC6g¤w-Ö~Edcn\\ }¶p8ûÑþ¡ò'- pass: '1'- iterations: 10204Done calculating BPKDF2, took 0.311 secondsPBKDF2: (length: 32)106:76:228:43:126:148:140:72:64:151:168:117:46:244:164:247:206:202:249:160:71:224:76:248:229:115:221:172:179:104:30:49:Calculating Bytes To Key:- iterations: 1- salt: bb69f512f2433667a4772dd67e4564636e5c5c8a201b7db67038fbd1fea19cf2Final key: (length: 32)106:76:228:43:126:148:140:72:64:151:168:117:46:244:164:247:206:202:249:160:71:224:76:248:229:115:221:172:179:104:30:49:Initial vector: (length: 16)173:220:214:98:209:30:141:67:138:196:13:63:4:202:26:199:Encrypting (length: 13)0:0:0:1:120:218:51:4:0:0:50:0:50:Encrypted data: (length: 16)Ç_£IS¤<_ÁT(ËwñEncoded & with salt: (length: 72)u2n1EvJDNmekdy3WfkVkY25cXIogG322cDj70f6hnPJLV0Mzx1...... And we are done here.

I produced a video :
==

{F183691}

Fix :
==

The panel should be protected with 403 or 401

Best regards
@Rbcafe

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
