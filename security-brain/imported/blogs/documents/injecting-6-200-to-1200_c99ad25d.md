---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-02_injecting-6200-to-1200.md
original_filename: 2019-07-02_injecting-6200-to-1200.md
title: Injecting {{6*200}} to $1200
category: documents
detected_topics:
- command-injection
- password-reset
- xss
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- xss
- automation-abuse
- api-security
language: en
raw_sha256: c99ad25da12bae0d7b345074ba6f23855f61ae2900a0e1d859c9c1f51545b46c
text_sha256: b9f9ce29c3f86a8b2a128d1a1c61781d91f25bd2c8c52e9e51c928b659cad663
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Injecting {{6*200}} to $1200

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-02_injecting-6200-to-1200.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, xss, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c99ad25da12bae0d7b345074ba6f23855f61ae2900a0e1d859c9c1f51545b46c`
- Text SHA256: `b9f9ce29c3f86a8b2a128d1a1c61781d91f25bd2c8c52e9e51c928b659cad663`


## Content

---
title: "Injecting {{6*200}} to $1200"
page_title: "Injecting {{6*200}} to $1200 | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/injecting-6200-to-1200/"
final_url: "https://gauravnarwani.com/injecting-6200-to-1200/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["SSTI"]
bounty: "1,200"
publication_date: "2019-07-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5171
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/07/Server-Side-Template-Injection-Zafiyeti-social.png?fit=1000%2C525&ssl=1) ](https://gauravnarwani.com/injecting-6200-to-1200/)

# Injecting {{6*200}} to $1200

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [July 2, 2019](https://gauravnarwani.com/injecting-6200-to-1200/)

Server-Side Template Injection or SSTI, in short, is considered one of the most critical vulnerabilities nowadays. Mistaken with Cross-Site Scripting, Template Injection can directly attack web servers and obtain Remote Code Execution. Template engines are widely used nowadays in many of the Web Applications to present dynamic data in web pages and emails and handling user input in an unsafe manner could lead to such vulnerability. A case has been discussed below where my Friend could use user input to get Remote Code Execution via SSTI. Let’s first jump into what is SSTI and how to find it and later on discuss the case study. Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the Blog.

### Server-Side Template Injection

Template injection allows an attacker to include template code into an existent (or not) template. A template engine makes designing HTML pages easier by using static template files which at runtime replaces variables/placeholders with actual values in the HTML pages.

To know why Server Side Templates can be dangerous read the following post: <https://www.netsparker.com/blog/web-security/server-side-template-injection/>

or read the following lines below:

Server-Side Template provides an easier method of managing the dynamic generation of HTML code rather than big code snippets which get the username of the person dynamically from a cookie. However, the real struggle begins when you try to change anything in the big code snippets– like adding CSS classes or changing the order of the HTML tags. SST makes it easier for you. Let’s see the following code below: 

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/07/SSTI_2.jpg?fit=531%2C200&ssl=1)

In the backend the code **$template- >assign(‘username’, getUsernameFromCookie());** does the job automatically for us. Using the function **$template- >show();** it replaces the value accordingly and prints the HTML code. 

### Why Server-Side Templates Can Be Dangerous?

It looks harmless and it actually is. But if you study it closely, you will see that you can execute native functions from the template. This code shows that we have user-controlled input inside a template string, which in turn means that users can execute template expressions. An example of a malicious expression could be as simple as _{{system(‘whoami’)}}_ , which would execute the _whoami_ system command.

Template Injection Methodology

Includes 3 Stage:

  1. Detect: A simple code {{7*7}} if turns 49 would prove the existence of SSTI
  2. Identify: The second step to Identify what template engine is used in the backend. Some examples include submitting {{7*’7′}} which would result in 49 in Twig Engine and 7777777 in Jinja2. The following image illustrates how to find the backend engine.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/07/SSTI_1.png?fit=640%2C386&ssl=1)

  3. Exploit: For all the template engines mentioned above, each of them has an exploit in the following URL:

[https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection)

## Case Study: SSTI to RCE ($1200 Bounty)

The application under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data Tier (Databases). As this was a private program all illustrations of vulnerabilities will be represented with the host as example.com.

The application had a **register** page where a user could register a new username and password which allowed him to login to the application via the **login** page.

While testing the application, a username **{{7*7}}** was entered in the **username field** of the form. The application took the payload as a string everywhere in the application and prevented the execution of the payload. Browsing throughout the application the username was displayed as **“{{7*7}}”**.

The application has a**forgot password** option in the login page where a user could change his password via his email id and username. Once a user enters his email id or username, a mail was sent to the user with a link to reset his password.

Here’s where the magic happens. When the user enters **either** his email id or username, a mail was sent to the email as:

Hello,

You requested a new password for the username {{7*7}}

Click here to create your new password

But, when the **user enters his email id in both username and email id fields** , an email was sent as:

Hey there,

Click your username below to reset your password

**49**

This was completely strange as the payload entered initially had then been fired leading to SSTI.

This was the detection process as mentioned above.

The next step in the process is to detect where the backend template was detected.

The payload **{{7*’7′}}** was passed in the username parameter. The mail received was as such

Hey there,

Click your username below to reset your password

**7777777**

This confirms the backend engine was **Jinja2**

The bug was exploited for RCE and sent to the program over the weekend. The bug is now in unresolved stage with a bounty awarded of $1200.

Takeaways –

  1. Always try to check SSTI on username parameters in password reset pages or any email triggering endpoints. A case study of RCE is in the link below:

[https://hackerone.com/reports/125980](https://hackerone.com/reports/125980)

The researcher could execute SSTI in almost the same way in the blog above.

  2. Always try to fuzz parameters with the same input. As you saw above just entering values in one of the fields didn’t execute our payload but in when inserted in both fields made it execute
  3. Never give up. The program was a 5-year-old program and still,l a critical bug was found on the website.

That’s all for this blog. Hope you liked it.

**#BugBountyTip** : While playing with API endpoints always try to send ‘INVALID CONTENT TYPE’ in the request and end-up by getting hidden endpoints in the response

The entire credits of the bug found above go to **[Verneet Singh](https://twitter.com/err0rrrrr)**  

That’s all for today. Please subscribe to my [**blog**](https://gauravnarwani.com/blog). Connect with me on [**LinkedIn**](https://linkedin.com/in/gauravnarwani97).  

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/injecting-6200-to-1200/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/injecting-6200-to-1200/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/injecting-6200-to-1200/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/injecting-6200-to-1200/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/injecting-6200-to-1200/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/injecting-6200-to-1200/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)
