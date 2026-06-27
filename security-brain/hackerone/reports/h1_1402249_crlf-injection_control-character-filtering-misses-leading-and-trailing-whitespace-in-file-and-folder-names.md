---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1402249'
original_report_id: '1402249'
title: Control character filtering misses leading and trailing whitespace in file
  and folder names
weakness: CRLF Injection
team_handle: nextcloud
created_at: '2021-11-17T02:30:13.121Z'
disclosed_at: '2022-05-27T07:23:54.354Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- crlf-injection
---

# Control character filtering misses leading and trailing whitespace in file and folder names

## Metadata

- HackerOne Report ID: 1402249
- Weakness: CRLF Injection
- Program: nextcloud
- Disclosed At: 2022-05-27T07:23:54.354Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
It is possible to create files and folders that have leading and trailing `\n`, `\r`, `\t`, and `\v` characters. The server rejects files and folders that have these characters in the middle of their names, so this might be an opportunity for injection.

In `lib/private/Files/Storage/Common.php`, the filename is trimmed before being checked for control characters:

```
        556         protected function verifyPosixPath($fileName) {
        557                 $fileName = trim($fileName);
        558                 $this->scanForInvalidCharacters($fileName, "\\/");
        ...
        570         private function scanForInvalidCharacters($fileName, $invalidChars) {
        571                 foreach (str_split($invalidChars) as $char) {
        572                         if (strpos($fileName, $char) !== false) {
        573                                 throw new InvalidCharacterInPathException();
        574                         }
        575                 }
        576
        577                 $sanitizedFileName = filter_var($fileName, FILTER_UNSAFE_RAW, FILTER_FLAG_STRIP_LOW);
        578                 if ($sanitizedFileName !== $fileName) {
        579                         throw new InvalidCharacterInPathException();
        580                 }
        581         }
```

## Steps To Reproduce:
  1. Create a file with an HTTP request of `PUT /remote.php/webdav/%09%0a%0b%0dfile%09%0a%0b%0d`...
  1. Browse to `http://NEXTCLOUD_HOST/index.php/apps/files/` and notice that the file has been created.
  1. Run `ls` in the data directory to see that the filename contains control characters.

or,

  1. Create a folder with an HTTP request of `MKCOL /remote.php/dav/files/user/%09%0a%0b%0ddir%09%0a%0b%0d`...
  1. Browse to `http://NEXTCLOUD_HOST/index.php/apps/files/` and notice that the folder has been created.
  1. Run `ls` in the data directory to see that the folder's name contains control characters.

## Supporting Material/References:

  * The result of `ls` in the data directory: F1516406.

## Impact

This may just be a hardening issue, but if the file or directory names are inserted into an HTTP response unfiltered, CRLF injection may occur.

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
