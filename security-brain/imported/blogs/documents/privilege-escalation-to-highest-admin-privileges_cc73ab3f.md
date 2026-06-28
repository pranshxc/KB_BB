---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-23_privilege-escalation-to-highest-admin-privileges.md
original_filename: 2019-01-23_privilege-escalation-to-highest-admin-privileges.md
title: Privilege Escalation to Highest Admin Privileges
category: documents
detected_topics:
- access-control
- idor
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- api-security
language: en
raw_sha256: cc73ab3f8f034fca95fb93e438d2088979c0659d9694c11eb530ab1aa35805cb
text_sha256: 31004c45fa0a8d7b2bc3a66b80f11d99924c999538504fde352be724068174e5
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation to Highest Admin Privileges

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-23_privilege-escalation-to-highest-admin-privileges.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `cc73ab3f8f034fca95fb93e438d2088979c0659d9694c11eb530ab1aa35805cb`
- Text SHA256: `31004c45fa0a8d7b2bc3a66b80f11d99924c999538504fde352be724068174e5`


## Content

---
title: "Privilege Escalation to Highest Admin Privileges"
page_title: "Privilege Escalation to Highest Admin Privileges | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/priv-esc-highest-admin/"
final_url: "https://gauravnarwani.com/priv-esc-highest-admin/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["IDOR", "Privilege escalation"]
publication_date: "2019-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5455
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/01/WhatsApp-Image-2019-01-24-at-2.43.24-AM.jpeg?fit=1000%2C742&ssl=1) ](https://gauravnarwani.com/priv-esc-highest-admin/)

# Privilege Escalation to Highest Admin Privileges

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [January 23, 2019](https://gauravnarwani.com/priv-esc-highest-admin/)

Hello Guys, today we are going to talk about a very interesting vulnerability I found in a private program. The vulnerability allowed an attacker to perform the highest admin privileged task being just a normal user. The attack is discussed as a case study later after a brief passage about Privilege Escalations and IDOR. Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the Blog.

## Privilege Escalation

Privilege escalation occurs when a user gets access to more resources or functionality than they are normally allowed, and such elevation or changes should have been prevented by the application. This is usually caused by a flaw in the application. The result is that the application performs actions with more privileges than those intended by the developer or system administrator.

The degree of escalation depends on what privileges the attacker is authorized to possess, and what privileges can be obtained in a successful exploit. For example, a programming error that allows a user to gain extra privilege after successful authentication limits the degree of escalation, because the user is already authorized to hold some privilege. Likewise, a remote attacker gaining superuser privilege without any authentication presents a greater degree of escalation.

Usually, people refer to vertical escalation when it is possible to access resources granted to more privileged accounts (e.g., acquiring administrative privileges for the application), and to horizontal escalation when it is possible to access resources granted to a similarly configured account (e.g., in an online banking application, accessing information related to a different user).

## Insecure Direct Object References 

Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability, attackers can bypass authorization and access resources in the system directly, for example, database records or files.

Insecure Direct Object References allow attackers to bypass authorization and access resources directly by modifying the value of a parameter used to directly point to an object. Such resources can be database entries belonging to other users, files in the system, and more. This is caused by the fact that the application takes user-supplied input and uses it to retrieve an object without performing sufficient authorization checks.

For Example, The value of a parameter is used directly to retrieve a database record  
Sample request: **http://foo.bar/somepage?invoice=12345**

In this case, the value of the **invoice** parameter is used as an index in an invoices table in the database. The application takes the value of this parameter and uses it in a query to the database. The application then returns the invoice information to the user.

Since the value of the invoice goes directly into the query, by modifying the value of the parameter it is possible to retrieve any invoice object, regardless of the user to whom the invoice belongs. To test for this case the tester should obtain the identifier of an invoice belonging to a different test user, and then check whether it is possible to access objects without authorization.

## Case Study: Remote attacker gaining superuser privileges

The application under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data Tier (Databases) having 4 different types of roles – **_Admin, Student, Moderator and Vendor_**. Credentials to test each of the roles were provided beforehand by the program manager. The student had access to the _student dashboard_ , the moderator had access _to moderator dashboard_ , the vendor had access to _the vendor dashboard_ and the admin had access to _student dashboard_ as well had options to _set up new users_ for the application.

## Privilege Escalation

While testing for issues on the admin dashboard, an endpoint was found where an admin could create a user based on roles. The admin only had privileges to create users which have less privileged roles (Admin could only create users with the roles moderator and vendor). A POST request was sent to the server with the necessary details like username, password, phone number, role id etc. Once the request was sent to the server, a new user was created.

A POST request was sent to the server with the role moderator(roleId-3) and then with the role vendor(roleId-4) and users were created with the assigned roles.

The POST request was then modified by sending the roleId-1. As there were no checks on the parameter, the user created had superuser privileges i.e. Privileges above the admin role

To check whether the user had necessary privileges, the admin panel was logged in with the credentials while creating the new user. The application now opened with superuser privileges and now the user had access to the entire application. The user could now add or delete a role as well as monitor all the users in the application.

## Exploiting Further - IDOR

To test whether the entire application had broken access, all endpoints which the superuser had access to had been captured in the Repeater of Burp Suite and the application was now logged in as a non-privileged user i.e. Moderator and Vendor. The endpoints such as adding or deleting a role were sent as a POST request with the session id of the less privileged user and the necessary parameters to complete the request. Turned out each and every endpoint was vulnerable for IDOR, where any user could change the values in the parameters sent by the POST request and perform actions which he is unauthorized to do.

A few cases were:

Change role permissions  
**PUT /admin/role-permissions**  
**Host: example.com**  
**..**  
**..**  
******{“roleId”:4,”permissionId”:1}**

Where roleId:4 (Vendor) would be given permissionId:1(Permission to access student dashboard)

Getting other users data  
**GET /users/239**  
**Host: example.com**  
**..**  
**..**  
**..**

Would give the user details in response. By changing the value from 239 to any other user id, all the sensitive information about that user would be leaked as there were no checks placed on this value.

The bug was reported under its disclosure platform and is still in the state of Triaged with the bounty undecided.

**#BugBountyTip** – Google Dorks for Content Discovery

Extensions

site:http://example.com filetype:php

site:http://example.com filetype:aspx

site:http://example.com filetype:swf

site:http://example.com filetype:wsdl

Directory structure

site:http://example.com intext:”index of /”

Juicy Stuff

site:http://example.com filetype:txt

site:http://example.com inurl:.php.txt

site:http://example.com ext:txt

That is all for today. Please Subscribe to my **[Blog](https://gauravnarwani.com/blog/)**. Connect with me on [**LinkedIn**](https://linkedin.com/in/gauravnarwani97/).

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/priv-esc-highest-admin/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/priv-esc-highest-admin/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/priv-esc-highest-admin/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/priv-esc-highest-admin/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/priv-esc-highest-admin/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/priv-esc-highest-admin/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)

Tags:[admin](https://gauravnarwani.com/tag/admin/) [bugbounty](https://gauravnarwani.com/tag/bugbounty/) [bugbountytip](https://gauravnarwani.com/tag/bugbountytip/) [bugbountytips](https://gauravnarwani.com/tag/bugbountytips/) [privilege](https://gauravnarwani.com/tag/privilege/) [privilege escalation](https://gauravnarwani.com/tag/privilege-escalation/) [securities](https://gauravnarwani.com/tag/securities/) [security](https://gauravnarwani.com/tag/security/) [webapp](https://gauravnarwani.com/tag/webapp/)
