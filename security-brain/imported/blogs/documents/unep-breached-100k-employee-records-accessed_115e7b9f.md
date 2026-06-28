---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-11_unep-breached-100k-employee-records-accessed.md
original_filename: 2021-01-11_unep-breached-100k-employee-records-accessed.md
title: UNEP Breached, 100K+ Employee Records Accessed
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: 115e7b9f052ca60beb03db3b794ea07940ff467a7f9bc395b59633e1b7149c2b
text_sha256: e51341befcc6dafeffd2045200eb3148917e7f4017f892475439df17aaed9a5e
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# UNEP Breached, 100K+ Employee Records Accessed

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-11_unep-breached-100k-employee-records-accessed.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `115e7b9f052ca60beb03db3b794ea07940ff467a7f9bc395b59633e1b7149c2b`
- Text SHA256: `e51341befcc6dafeffd2045200eb3148917e7f4017f892475439df17aaed9a5e`


## Content

---
title: "UNEP Breached, 100K+ Employee Records Accessed"
page_title: "Hack the Galaxy"
url: "https://johnjhacking.com/blog/unep-breach/"
final_url: "https://johnjhacking.com/blog/unep-breach/"
authors: ["Jackson Henry (@JacksonHHax)", "John Jackson (@johnjhacking)", "Nick Sahler (@nicksahler)", "Aubrey Cottle"]
programs: ["United Nations"]
bugs: ["Information disclosure"]
publication_date: "2021-01-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4009
---

* [ Home ](/)
  * [Blog](/blog)
  * [Research](/research)

  * [ Home ](https://johnjhacking.com)
  * [Blog](/blog)
  * [Research](/research)

# UNEP Breached, 100K+ Employee Records Accessed

A writeup detailing the exposed employee records that Sakura Samurai managed to access during our security research through their vulnerability disclosure program.

Published on Jan 11, 2021

Reading time: 3 minutes.

* * *

# United Nations Environment Programme Breached, 100K+ Employee Records Accessed

# Executive Summary

We noticed that The United Nations had a Vulnerability Disclosure Program and a Hall of Fame, therefore Sakura Samurai 桜の侍 our security research group, set out to look for vulnerabilities to report to the United Nations. During the research process Jackson Henry @JacksonHHax , Nick Sahler, John @johnjhacking and Aubrey Cottle @Kirtaner identified an endpoint that exposed Git Credentials. The credentials gave us the ability to download the Git Repositories, identifying a ton of user credentials and PII. In total, we identified over 100K+ private employee records. We also discovered multiple exposed .git directories on UN owned web servers [ilo.org], the .git contents could then be exfiltrated with various tools such as “git-dumper”.

# Exposed PII

**Travel Records [Two Documents: 102,000+ Records]**

![](/uploads/travel-records.png)  
Travel Records Included Employee ID Numbers, Names, Employee Groups, Travel Justification, Start and End Dates, Length of Stay, Approval Status, Destination and the Length of the stay.

**HR Nationality Demographics [Two Documents: 7,000+ Records]**

![](/uploads/nationality-records.png)  
Included Employee Name, Employee Group, Employee ID Numbers, Person’s Nationality, Person’s Gender, Employee Pay Grade, Organization Work Unit Identification Number and Organization Unit Text Tags.

**Generalized Employee Records [One document: 1,000+ Records]**

![](/uploads/hr-records.png)  
Index Numbers, Employee Names, Employee Emails, Employee Work Subareas and Employee Org Units. Note: The column with the “Red number 1” represent the Employee’s specific work department and was blurred as some of the sub-units are smaller.

**Project and Funding Source Records [One Document: 4,000+ Records]**

![](/uploads/project-funding.png)  
Included Project Identification Number, Affected Areas, Grant and Co-financing amounts, Implementing Agencies, Countries, Funding Sources, Period of the Project and if the Project/Concept was approved.

**Evaluation Reports [One Document: 283 Projects]**

![](/uploads/eval-reports.png)  
Overall descriptions of the Evaluations and Reports, Periods Conducted and a link to the report on the project.

# Technical Assessment

In addition, on the lesser side of severity, we managed to takeover a SQL Database and a Survey Management Platform belonging to the International Labour Organization - also in the UN’s VDP program scope. However, it was of note that the ILO vulnerabilities were of little prominence as the Database and Survey Management platform were fairly abandoned in nature and contained hardly anything of use. Nonetheless, a Database takeover and admin account takeover on a platform are still Critical vulnerabilities.

We had performed subdomain enumeration of all of the domains in scope for the VDP offered by the UN. During our research, we began to fuzz multiple endpoints with tooling and initially discovered that an ilo.org subdomain had an exposed .git contents. Utilizing git-dumper [[**https://github.com/arthaud/git-dumper**](https://github.com/arthaud/git-dumper "https://github.com/arthaud/git-dumper")] we were able to dump the project folders hosted on the web application, resulting in the takeover of a MySQL database and of survey management platform due to exposed credentials within the code.

**MySQL Credentials**

**![](/uploads/sql.png)  
Note:** _We will not provide a picture of the survey platform due to the specific nature of the application._

* * *

After we had taken over one of the International Labour Organization’s MySQL Databases and performed account takeover on the survey management platform, we began to enumerate other domains/subdomains.

Eventually, we found a subdomain on the United Nations Environment Programme that allowed us to discover github credentials after a bit of fuzzing.

![](/uploads/git.png)  
Ultimately, once we discovered the GitHub credentials, we were able to download a lot of private password-protected GitHub projects and within the projects we found multiple sets of database and application credentials for the UNEP production environment. In total, we found **7 additional credential-pairs** which could have resulted in unauthorized access of multiple databases. We decided to stop and report this vulnerability once we were able to access PII that was exposed via Database backups that were in the private projects.

* * *

**Check out our website**  
<https://sakurasamurai.org>

**_Twitter Links:_**  
Main Page  
<https://twitter.com/SakuraSamuraii>  
Founders  
[https://github.com/johnjhacking](https://github.com/johnjhackingg "https://github.com/johnjhacking")  
Members  
<https://twitter.com/nicksahler>  
<https://twitter.com/JacksonHHax>  
<https://twitter.com/Kirtaner>  
<https://twitter.com/rej_ex>  
<https://twitter.com/endingwithali>

![Creative Commons](https://mirrors.creativecommons.org/presskit/icons/cc.svg) ![CC-BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) 2020 John
