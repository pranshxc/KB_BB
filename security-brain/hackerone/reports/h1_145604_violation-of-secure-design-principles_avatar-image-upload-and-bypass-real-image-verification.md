---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145604'
original_report_id: '145604'
title: Avatar image upload and bypass  real image verification
weakness: Violation of Secure Design Principles
team_handle: nextcloud
created_at: '2016-06-18T01:50:10.608Z'
disclosed_at: '2017-01-15T22:07:23.197Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
tags:
- hackerone
- violation-of-secure-design-principles
---

# Avatar image upload and bypass  real image verification

## Metadata

- HackerOne Report ID: 145604
- Weakness: Violation of Secure Design Principles
- Program: nextcloud
- Disclosed At: 2017-01-15T22:07:23.197Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi

We can bypass Avatar Upload image verification and extension  uploading a php file or any other extension binding a valide  jpeg image  , there is no risk for the moment because the avatar is renamed to avatar_upload on the remote server , but it ll be nice to secure this part of code .

Example  
---------------
here is the same file with two different extension : 

http://91.121.108.101/image1.jpg
http://91.121.108.101/image1.php      <== execute php code inside the image 

1) download image1.jpg

2) as you can see  if you open the file image1.jpg  file on notepad it hide php code ( phpinfo(); function in this case .

3) rename image1.jpg to image1.php  , and try to upload it on the avatar upload form , it pass the verification  .

This verification is not enought in this  file :  /core/controller/avatarcontroller.php  


	if ($image->valid()) {
				$mimeType = $image->mimeType();
				if ($mimeType !== 'image/jpeg' && $mimeType !== 'image/png') {
					return new DataResponse(
						['data' => ['message' => $this->l->t('Unknown filetype')]],
						Http::STATUS_OK,
						$headers
					);
				}

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
