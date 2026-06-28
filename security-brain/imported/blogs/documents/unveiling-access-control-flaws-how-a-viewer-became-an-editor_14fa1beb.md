---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-10_unveiling-access-control-flaws-how-a-viewer-became-an-editor.md
original_filename: 2023-07-10_unveiling-access-control-flaws-how-a-viewer-became-an-editor.md
title: 'Unveiling Access Control Flaws: How a Viewer Became an Editor'
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
- cloud-security
language: en
raw_sha256: 14fa1beb99482a096c032b0dd98e1a34c682cbcb67039056f6772c89c8bbf391
text_sha256: 3df9efd7de00c07f458b635769174ee9fb2226e58df22e5c01086bc8b5260796
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Unveiling Access Control Flaws: How a Viewer Became an Editor

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-10_unveiling-access-control-flaws-how-a-viewer-became-an-editor.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `14fa1beb99482a096c032b0dd98e1a34c682cbcb67039056f6772c89c8bbf391`
- Text SHA256: `3df9efd7de00c07f458b635769174ee9fb2226e58df22e5c01086bc8b5260796`


## Content

---
title: "Unveiling Access Control Flaws: How a Viewer Became an Editor"
url: "https://amjadali110.medium.com/unveiling-access-control-flaws-how-a-viewer-became-an-editor-b4aa83a5a0ec"
authors: ["Amjad Ali"]
bugs: ["Broken Access Control"]
publication_date: "2023-07-10"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 948
scraped_via: "browseros"
---

# Unveiling Access Control Flaws: How a Viewer Became an Editor

Unveiling Access Control Flaws: How a Viewer Became an Editor
Amjad Ali
Follow
3 min read
·
Jul 10, 2023

261

1

Hey everyone 👋,

Hope all are good and fine. I’m back with another write-up. If you missing the previous write-up stories you can check it out from here: https://amjadali110.medium.com/hyperlink-injection-726d8151b216. In this write-up i want to share with you the story of a recent finding I discovered during a Gray Box testing of a web application.

Press enter or click to view image in full size

During my assessment, I came across a web application called test.com, which served as a data management portal. The website had three different user roles: Viewer, Editor, and Admin. As part of my testing, I logged in using an Editor account to explore the functionalities of the web app. Editors had complete access to modify the data within the portal.

While making modifications to an entry, I captured the corresponding HTTP request and analyzed its structure. The request was sent as a POST method to the endpoint “/dir/mis/update?queryid=9361” and contained the data in JSON format. Here’s an example of the request:

POST /dir/mis/update?queryid=9361 HTTP/2
Host: test.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Bearer <token>
Content-Type: application/json
Content-Length: 392
Origin: http://test.com
Connection: close
Referer: http://test.com/dir/
Cookie: JSESSIONID=<value>

{
  "STATE CODE":"ALL",
  "STATE GST CODE":"0",
  "FILING DATE":"2017-12-01 00:00:00.0",
  "LAST DATE":"2018-02-10 00:00:00.0",
  "RETURN YEAR":"2017-18",
  "TARGET DATE":"2018-01-10",
  "GSTNOT":"72/2017  Central Tax#2017-12-29",
  "NOTIFICATION DATE":"2017-12-29",
  "PERIOD":"122017",
  "GST NOTIFICATION":"72/2017  Central Tax",
  "STATE NAME":"ALL",
  "TYPE":"GSTR1",
  "PREFERENCE":"N",
  "REMARK":"Test Data",
  "dataKeyEdit":6
}

Upon further analysis, I discovered several vulnerabilities within the application’s access control mechanisms. Notably, the website relied heavily on weak cookie implementation for user authentication, and the only check performed was on the presence of the “Authorization: Bearer <token>” header in the request. Strikingly, the “Authorization: Bearer <token>” contained minimal information, such as the username, expiration time, and issuance time.

Get Amjad Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Exploiting these vulnerabilities, I devised a plan to bypass the access controls. After logging out from the Editor account, I logged in as a Viewer. Although Viewers had restricted permissions and couldn’t modify data, they could still view it. Armed with the knowledge of the HTTP request structure, I crafted a new request identical to the one I observed earlier. However, this time, I used the Viewer’s “Authorization: Bearer <token>” and corresponding cookies.

In the crafted request, I replaced the “REMARK” parameter with a malicious payload, “Hello.” To my surprise, when I sent the request, I received a 200 OK response, indicating that the modifications were successful.

Press enter or click to view image in full size

It became apparent that the website only checked the presence of the “Authorization: Bearer <token>” header in the request. Regardless of whether it belonged to a privileged user or a non-privileged user, the server processed the request without proper authorization. This vulnerability existed on all the endpoints, meaning the entire web app was vulnerable to unauthorized data modification.

This vulnerability allowed a lower-level user, such as a Viewer, to modify data even though they lacked the necessary permissions. It exposed a significant flaw in the application’s access control mechanism and could potentially lead to unauthorized modifications or data tampering.

Thank you for taking the time to read about my experience. If you have any thoughts or questions, please feel free to share them in the comments section. You can also connect with me on LinkedIn: https://www.linkedin.com/in/amjadali110/

Happy Bug Hunting!
