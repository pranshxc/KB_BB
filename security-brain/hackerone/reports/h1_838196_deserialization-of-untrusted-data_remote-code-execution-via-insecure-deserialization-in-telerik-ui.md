---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '838196'
original_report_id: '838196'
title: Remote Code Execution via Insecure Deserialization in Telerik UI
weakness: Deserialization of Untrusted Data
team_handle: deptofdefense
created_at: '2020-04-03T14:48:45.089Z'
disclosed_at: '2020-05-07T16:54:15.813Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 42
tags:
- hackerone
- deserialization-of-untrusted-data
---

# Remote Code Execution via Insecure Deserialization in Telerik UI

## Metadata

- HackerOne Report ID: 838196
- Weakness: Deserialization of Untrusted Data
- Program: deptofdefense
- Disclosed At: 2020-05-07T16:54:15.813Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,
I found an outdated version of Telerik Web UI (v2016.2.607.40) at the following URL: https://███/Telerik.Web.UI.WebResource.axd?type=rau.
This means that we can achieve full RCE by chaining two different CVEs: CVE-2017-11317, which allows us to upload arbitrary files on the server, and CVE-2019-18935, which is a deserialization vulnerability.

First of all, the only thing that I tried to prove that I had successfully achieved code execution was making the server sleep for 10 seconds.
No data was compromised.

Steps to reproduce
---------------------
The steps that I followed are thoroughly described in this blog post: <https://know.bishopfox.com/research/cve-2019-18935-remote-code-execution-in-telerik-ui>.
Here's a quick summary:
- Download the files in the attachments
- Make sure you have pycryptodome installed (pip3 install pycryptodome)
- Run the following command: `python3 CVE-2019-18935.py -u https://█████/Telerik.Web.UI.WebResource.axd?type=rau -v 2016.2.607.40 -f 'C:\Windows\Temp' -p sleep_042020163752,45_amd64.dll`
- The `sleep_042020160430,40_amd64.dll` is supposed to Sleep(10). This will make the server hang for roughly ten seconds, and after that you will get a response like this one: `[*] Response time: 12.88 seconds`
- The exploit worked.

Things to note
---------------------
I had to edit the original exploit code provided in the aforementioned blog post (https://github.com/noperator/CVE-2019-18935) because I noticed that when uploading the .dll file the server added a .tmp at the end of the file name.
That's why the original code was failing to exploit the deserialization part.
I added `+ '.tmp'` at the end of line 95 and after that it worked just fine.

A DLL file can only work once. This means that to test the vulnerability again a new DLL has to be compiled.
For this reason I provided several DLLs in the attachments so you don't have to compile them (especially because a windows machine with Visual Studio installed is required).

I didn't upload a reverse shell because I thought it was not a great idea, but if needed I could do it.

How to fix
---------------------
Just upgrade Telerik for ASP.NET AJAX to R3 2019 SP1 (v2019.3.1023) or later.

## Impact

Full **Remote Code Execution** on the vulnerable server.

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
