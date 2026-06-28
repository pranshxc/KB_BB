---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-19_access-control-violation-sensitive-data-exposure.md
original_filename: 2022-02-19_access-control-violation-sensitive-data-exposure.md
title: Access Control Violation - Sensitive Data Exposure
category: documents
detected_topics:
- command-injection
- information-disclosure
- access-control
- file-upload
tags:
- imported
- documents
- command-injection
- information-disclosure
- access-control
- file-upload
language: en
raw_sha256: 2b071dc35320ff315c47de9adbe7d01a965e704f2e056b3c893360fa056df126
text_sha256: a851ce2629d85302e94f6cdbe90921b3fdcb28aad3d2e40d84c78c9ee9b76f3b
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Access Control Violation - Sensitive Data Exposure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-19_access-control-violation-sensitive-data-exposure.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, access-control, file-upload
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `2b071dc35320ff315c47de9adbe7d01a965e704f2e056b3c893360fa056df126`
- Text SHA256: `a851ce2629d85302e94f6cdbe90921b3fdcb28aad3d2e40d84c78c9ee9b76f3b`


## Content

---
title: "Access Control Violation - Sensitive Data Exposure"
page_title: "Access Control Violation - Sensitive Data Exposure — Machevalia"
url: "https://machevalia.blog/blog/access-control-violation-sensitive-data-exposure"
final_url: "https://machevalia.blog/blog/access-control-violation-sensitive-data-exposure"
authors: ["Nick Berrie (@machevalia)"]
bugs: ["Directory listing"]
bounty: "444.50"
publication_date: "2022-02-19"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 2885
---

# Access Control Violation - Sensitive Data Exposure

[Bug Bounty](/blog/category/Bug+Bounty)[Write Ups](/blog/category/Write+Ups)

Feb 19

Written By [](/blog?author=63a1076f081fe62c6e3ae37b)

## Private Job Data Exposed via Directory Listing

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae468/1671497590680/directory_listing.png?format=original) Directory Listing Example

### Overview

Directory listing is a common thing to run across in pentesting or bug bounty hunting. Despite allowing directory listings not being a good practice, there is generally no security consequence by allowing it. In this write-up, I'll detail how I discovered sensitive information disclosure in a directory listing that wasn't straightforward on looking at the directory initially. 

### Vulnerability Discovery

I explained in my [Remote Code Execution in .tgz File Upload](/machevalias-blog/remote-code-execution-in-tgz-file-upload) article, that I was able to access a PHP web shell that I uploaded via a jobs directory that was exposed to the public. On another area of this web application, I found that users could upload files to execute jobs on scientific data. Each user who uploaded files had the option of logging in to save the job to their profile as well as mark the job as private to prevent leaking their private scientific data to the public. Through the application interface, the controls to prevent me from accessing private jobs worked just fine. However, the job files were uploaded to the same jobs directory where my PHP web shell went after I submitted it from another area of the web application. So now I knew that pretty much anywhere I submitted files from, regardless of format, the files would ultimately land in the jobs directory. 

I uploaded a few files to shoot for remote code execution in this portion of the web application and was unsuccessful because the application reformatted any file that I provided without executing any of it. One thing I did notice while working in this area of the web application is that another user had uploaded a job that they had marked private. The private job landed right between two of the jobs that I had submitted which were public. 
  
  
  /Jobs./Job_156498793245 - 1/1/2022 01:22:56 <-- My public job./Job_158754653125 - 1/1/2022 01:21:43 <-- Their private job./Job_158343450454 - 1/1/2022 01:20:21 <-- My other public job

Via the web interface, I could see the job had been submitted and completed but I couldn't see the results or input data. By sorting the jobs directory by data modified, I could see that my jobs sandwiched another job #. I opened the data in that job sandwiched between my jobs and found that I could see all of their job information including contact information, the fact that the job was supposed to be private and protected, and much more. 

### Vulnerability Remediation and Payout

I advised the program of this issue and recommended that they prevent directory listing on the jobs directory. To do this, in Apache web server, the organization needed to create a .htaccess file in the related application directory. They needed to add the following lines to the httpd.conf (sometimes apache2.conf) file or replace the existing lines with the following:
  
  
  <Directory /{YOUR DIRECTORY}>Options FollowSymLinks</Directory>

As you can see from the example code above, you should remove the _Indexes_ and _MultiViews_ statements for the directory listing feature will be disabled safely on an Apache webserver.

For example:

My httpd.conf file before disallowing directory listing:

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae46b/1671497590692/apache2.conf_before.png?format=original)

With the above configuration I can list my jobs directory:

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae46e/1671497590704/directory_listing-1.png?format=original)

Here is the file after I made the configuration changes:

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae471/1671497590714/apache2.conf_after-1.png?format=original)

And, here is the result:

![](http://static1.squarespace.com/static/639bcf9ae1aabb6394c4c281/63a1076f081fe62c6e3ae375/63a10776081fe62c6e3ae474/1671497590724/directory_listing_forbidden.png?format=original)

The program quickly fixed the issue. Overall, I was awarded $444.50 for this submission. 

[Bug Bounty](/blog/tag/Bug+Bounty)[Write-up](/blog/tag/Write-up)

[ ](/blog?author=63a1076f081fe62c6e3ae37b)
