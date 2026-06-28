---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-20_escalating-privileges-like-a-pro.md
original_filename: 2019-10-20_escalating-privileges-like-a-pro.md
title: Escalating Privileges like a Pro
category: documents
detected_topics:
- access-control
- command-injection
- rate-limit
tags:
- imported
- documents
- access-control
- command-injection
- rate-limit
language: en
raw_sha256: ff0822f4fa18420032f0ee1a2920fb81e42d989b069c1973393a2ef78fe07687
text_sha256: 5e2730871c99eee901c9badd9d240e5d695ff3a304985af5f6275da24937715d
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating Privileges like a Pro

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-20_escalating-privileges-like-a-pro.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `ff0822f4fa18420032f0ee1a2920fb81e42d989b069c1973393a2ef78fe07687`
- Text SHA256: `5e2730871c99eee901c9badd9d240e5d695ff3a304985af5f6275da24937715d`


## Content

---
title: "Escalating Privileges like a Pro"
page_title: "Escalating Privileges like a Pro | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/escalating-privileges-like-a-pro/"
final_url: "https://gauravnarwani.com/escalating-privileges-like-a-pro/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["Privilege escalation"]
publication_date: "2019-10-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4981
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/10/8619276-3x2-700x467.jpg?fit=700%2C467&ssl=1) ](https://gauravnarwani.com/escalating-privileges-like-a-pro/)

# Escalating Privileges like a Pro

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [October 20, 2019](https://gauravnarwani.com/escalating-privileges-like-a-pro/)

**Privilege Escalation** occurs when a user gets access to more resources or functionality than they are normally allowed and such elevation or changes should have been prevented by the application. This is usually caused by **a flaw in the application**. The result is that the application performs actions with more privileges than those intended by the developer or system administrator.

In this blog, we would learn about **different types of Privilege Escalations** as well as learn how to efficiently hunt for this vulnerability on various Bug Bounty Programs. The blog mentioned below is a demonstration of tool **“Autorize”** which automatically detects escalation/authorization related issues, giving much faster results than manually testing requests. Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the **Blog**.

## Privilege Escalation ( A5-Broken Access Control )

**Privilege escalation** is a common threat vector for adversaries, which allows them to enter organizations’ IT infrastructure and seek permissions to steal sensitive data, disrupt operations and create backdoors for future attacks.

The degree of escalation depends on what privileges the attacker is authorized to possess, and what privileges can be obtained in a successful exploit. For example, a programming error that allows a user to gain extra privilege after successful authentication limits the degree of escalation, because the user is already authorized to hold some privilege. Likewise, a remote attacker gaining superuser privilege without any authentication presents a greater degree of escalation.

Usually, people refer to **vertical escalation** when it is possible to access resources granted to more privileged accounts (e.g., acquiring administrative privileges for the application), and **to horizontal escalation** when it is possible to access resources granted to a similarly configured account (e.g., in an online banking application, accessing information related to a different user).

### Testing for Role/Privilege Manipulation

In every portion of the application where a user can create information in the database (e.g., making a payment, adding a contact, or sending a message), can receive information (statement of account, order details, etc.), or delete information (drop users, messages, etc.), it is necessary to record that functionality. The tester should try to access such functions as another user to verify if it is possible to access a function that should not be permitted by the user’s role/privilege (but might be permitted as another user).

#### **Manipulation of a User group**

For example:  
The following HTTP POST allows the user that belongs to grp001 to access order #0001:
  
  
  POST /user/viewOrder.jsp HTTP/1.1  
  Host: www.example.com  
  ...  
  
  groupID=grp001&orderID=0001

Verify if a user that does not belong to grp001 can modify the value of the parameters ‘groupID’ and ‘orderID’ to gain access to that privileged data.

Ideally for a tester to test for privilege escalation, a request first had to be made from the privileged user and then the same request had to be made for a lower privileged user. This was a very time-consuming process and thus a tool was released to automate the boring stuff. Here’s where **“Autorize”** comes into the picture

## Autorize – An Automatic Authorization Enforcement Detection Extension

As the description of the tool on [Github](https://github.com/Quitten/Autorize) says that – **Autorize** is an automatic authorization enforcement detection extension for Burp Suite. It was written in Python by Barak Tawily, an application security expert, and Federico Dotta, a security expert at Mediaservice.net. Autorize was designed to help security testers by performing automatic authorization tests. With the last release now Autorize also performs automatic authentication tests.

#### **Now, what exactly does Autorize do?**

The time-consuming process such as replacing cookies and adding various headers is automatically done by Autorize. All a tester needs to do is **copy the cookies and the appropriate headers** of the lower privileged user into the configuration panel of the tool and start the tool. It is now the job of Autorize to **replace these values** in every request which is sent via Burp Suite.

The plugin works without any configuration but can be easily customised according to the requirement of the user. It is also possible to save the state of the results in various formats to read and also reuse by the extension.

**How to Install:** The tool is publicly available on Burp’s BAPP Store. If you have any difficulties installing the tool, please refer to <https://github.com/Quitten/Autorize> to install it manually.

#### **How to Use Autorize?**

  1. Login into the Account of a Lower Privileged User.
  2. Either copy the cookies and headers of any request or Right-Click -> Send cookie to Autorize.
  3. In the Autorize Tab, paste these values inside the text box above “Fetch cookies from last request”
  4. Now login into the Account of the Higher Privileged User.
  5. For all the requests made to the application you can do either of the two things:

  * Manually send requests to Autorize to test via Right-Click -> Send request to Autorize
  * Click the Button “Autorize is off” to turn Autorize on with green colour button indicating it is on. This will intercept all the requests which are sent from the application to the server and would automatically perform auth checks.

#### **How to check for Enforcement?**

There are 3 enforcement statuses:

  * Bypassed! – Red colour
  * Enforced! – Green colour
  * Is enforced??? (please configure enforcement detector) – Yellow colour

### Practical Demo

For practical purposes, the demo is been shown on BWAPP. For this demonstration, we have created two user’s “bee” (admin) and “user” (normal user).

To start the account of “user” is first accessed. Any standard request is captured and the cookies are copied.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/10/bwapp_1.png?fit=1000%2C531&ssl=1)

The cookies are now copied inside the textbox under Autorize tab

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/10/bwapp_2.png?fit=1000%2C582&ssl=1)

Now we can set interception filters. In this case we only want to intercept all those requests which are in our scope. So, Select Scope Items Only in the Type box under Interception filters and click on Add Filter. 

This would prevent all the requests going through the browser to be intercepted and tested for Privilege Escalation Issues.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/10/bwapp_3.png?fit=1000%2C569&ssl=1)

Turn Autorize On to intercept all requests of items in scope

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/10/bwapp_4.png?fit=1000%2C521&ssl=1)

Capture request of a privileged user and send it to Autorize. Or if you have turned the intercept on, it will test the request automatically.

In this case I am sending a POST request to change secret.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/10/bwapp_6.png?fit=1000%2C426&ssl=1)

The POST request Original Length and Modified length is similar even are their responses, this indicates that the application is vulnerabile to Privilege Escalation. The is Enforced? in orange indicates the possibility of the vulnerability which the tester has to confirm, wheread Enforced! in the Unauthenticated testing indicates that the endpoint is not vulnerable to privilege escalation where unauthenticated testing was done.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/10/bwapp_8.png?fit=1000%2C522&ssl=1)

### Case Study: Invite Users on Locked Page

The application was a three-tier web application with two different kinds of users – Admin and Guest. In the application, there was a functionality where a page was shared between an Admin and the Guest. The page had a lock feature which locked certain features of the page such as inviting another user to that page.

Only an admin was allowed to add users to the page after lock. By using the method above, the cookies of Guest were copied to Autorize and the add to page request was sent from Admin.

Turns out that there was only client-side validation for Guest when the page was locked. Thus, by using Autorize I was successfully able to add other users to the page, escalating my privileges to that of Admin.

This bug was accepted by Synack and is currently in the triaged stage.

That’s all for this Blog. Hope you liked it.

#**BugBountyTip:** While testing for SSTI, if the Engine is running in a sandboxed environment and there is no way to escape it, try accessing global variables. Brute-force a list of common variables to check if any local variable is accessible. You can view the wordlist [here](https://github.com/err0rr/SSTI/blob/master/Wordlist). Thankyou [Verneet](https://twitter.com/err0rrrrr) for this tip.

That’s all for today. Please subscribe to my [blog](https://gauravnarwani.com/blog). Connect with me on [LinkedIn](https://www.linkedin.com/in/gauravnarwani97).

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/escalating-privileges-like-a-pro/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/escalating-privileges-like-a-pro/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/escalating-privileges-like-a-pro/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/escalating-privileges-like-a-pro/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/escalating-privileges-like-a-pro/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/escalating-privileges-like-a-pro/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)
