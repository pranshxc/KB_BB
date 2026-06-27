---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '229170'
original_report_id: '229170'
title: RTLO character allowed in shared files
weakness: UI Redressing (Clickjacking)
team_handle: nextcloud
created_at: '2017-05-17T12:40:08.108Z'
disclosed_at: '2020-08-17T08:34:47.122Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- ui-redressing-clickjacking
---

# RTLO character allowed in shared files

## Metadata

- HackerOne Report ID: 229170
- Weakness: UI Redressing (Clickjacking)
- Program: nextcloud
- Disclosed At: 2020-08-17T08:34:47.122Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

SUMMARY
-------------
Hello, I have notices that you do not properly strip the RTLO (right to left override) character __in the sharing page of the file__, thus allowing someone to mask the real extension of a file and if the user downloads, then opens the file something may be executed on his machine.

Very important : This char is handles correctly in file lists, but incorrectly if you get the share link of that file.

POC
------------
First of all, create a file with a fake extension by utilizing the RTLO character. I usually do it like this (my example is to fake a .html as a .txt) :
1. Create a file called : testtxt.lmth
2. Go to Chrome, open the JS console and write copy("\u202e");
3. Go to your file, try to rename it, place the cursor between the . and the l from the extension and CTRL+V to paste the copied RTLO char. The name should be now `testtxt.html`

Now, back to nextcloud. I used https://demo.nextcloud.com for my test

1. Upload the file
2. You will notice that the name is correctly written in file file manager (you see the .html extension, not .txt)
3. Share the file (I also added a password, but it shouldn't matter)
4. With another account / user go to that file
5. The name you will see is `testtxt.html`. But, if you download this file and open it the html will be executed in your browser

__Video POC attached__ (I cannot attach the RTLO file because h1 strips the char out, as it should)

ADVICE
-----------
Normally you should strip this char out along with more unicode chars. I have reported this / seen this behaviour and stripping the unicodes out fixes it, __and I recommend it__. Also in some other programs, the user cannot even download the file (after he downloads the file, it cannot be opened as it is not found on the disk anymore - the name is replaced again by the system).

But, the behaviour from nextcloud should be patched.

Also, the txt <-> html faking is trivial, but faking .exe / .bat / .cmd etc can have other consequences as the user knows he should have downloaded a .txt file from nextcloud.

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
