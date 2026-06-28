---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-25_stored-xss-with-two-different-parameters_2.md
original_filename: 2021-05-25_stored-xss-with-two-different-parameters_2.md
title: Stored XSS with two different parameters
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: 87b14b97e6ab056162abfd993fbcacfc924d7cb09ffd02bf44b8dd81e5c86b6a
text_sha256: 0a7cd907385273675c9ed7528957b0f2a189749e77fcbab2b952219d15247421
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS with two different parameters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-25_stored-xss-with-two-different-parameters_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `87b14b97e6ab056162abfd993fbcacfc924d7cb09ffd02bf44b8dd81e5c86b6a`
- Text SHA256: `0a7cd907385273675c9ed7528957b0f2a189749e77fcbab2b952219d15247421`


## Content

---
title: "Stored XSS with two different parameters"
url: "https://joelmcg1993.medium.com/stored-xss-with-two-different-parameters-d9243cae3e6a"
authors: ["Joel Cantu (@InfosecRintox)"]
bugs: ["Reflected XSS"]
publication_date: "2021-05-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3623
scraped_via: "browseros"
---

# Stored XSS with two different parameters

Stored XSS with two different parameters
Joel Cantu
Follow
4 min read
·
May 25, 2021

442

2

Press enter or click to view image in full size

Hello Readers,

Today I will share a story of how to exploit an XSS vulnerability using two different parameters.

If you are new to hacking, here's a brief explanation from OWASP:

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

The 3 more common ways to exploit this kind of vulnerability are:

Reflected XSS: where the malicious script comes from the current HTTP request.
Stored XSS: where the malicious script comes from the website’s database.
DOM-based XSS: where the vulnerability exists in client-side code rather than server-side code.

In this case, it’s a Stored XSS. So, let’s begin…

I can’t disclose much information about the target or endpoint since it was a private client, but I will try to explain it as much as I can.

Understanding the behavior

The application had this functionality that a user can comment on uploaded pictures and everyone else can see those comments. It had one input field: “comment”

One caveat though, the comment field had a mechanism to HTML encode “dangerous” characters such as “<” and “>” (which is the right way to protect against XSS attacks; or is it?)

Another thing to consider is that once you submitted a comment, your first name and the value of the “comment” parameter were stored in the database and reflected back in between tags, meaning that we must try to insert <script> <img> <svg>… tags to properly pop our XSS. It was reflected back on the source code like this:

<p>
<h3> YourFirstName</h3>
<br>
CommentValue
</p>

As I mentioned, the comment parameter was HTML encoding dangerous characters, meaning “<” was turned into “&lt;” and “>” into “&gt;”. This means that we cannot insert new tags to execute XSS. So, the next logical step is to poke the second parameter we control, which is the value of the first name.

This parameter can only be changed in the settings options and it had one more caveat, it only allowed 12 characters as your first name.

So, I changed the value of my first name into “<>Joel” to see how the application works. As it turns out, the “<” and “>” characters were HTML encoded on my profile page, but what about the comment endpoint?

To my surprise, once I made a comment, the endpoint reflected this:

<p>
<h3><>Joel</h3>
<br>
whatever
</p>

Now, the fun begins…

Exploiting the vulnerability

We now know that the first name parameter from the settings page was not HTML encoding dangerous characters on the comment endpoint, but the problem is that it’s limited to only 12 characters.

Get Joel Cantu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to insert short payloads from my arsenal such as <svg/onload=alert(1)>, but still too long. I made my research and stumble upon brutelogic’s (who is an XSS GOD) blog about the shortest XSS payload. Still, no luck since his payload was 15 characters long.

So, I needed to change the approach of exploiting this vulnerability. If I was going to exploit it, I needed to use both of these parameters to properly exploit the vulnerability.

Here’s some background you must know. In Javascript, comments can be placed like:

//This is a comment per line

Or

/*
Multiple comments
on multiple lines
*/

So, I tried both. I changed my first name value to <script>/* and for the comment, I placed */alert(document.domain)//

When I visited the page, the XSS popped! The source code looked like this:

<p>
<h3><script>/*</h3><br>*/alert(document.domain)//</p></script></h3>
</p>

Why it worked????

We need to understand the very first thing a browser does before displaying the contents of a web page to a user. It reads the code and validates that the HTML tags are correctly closed. If they aren’t, the browser inserts the correct closing tags so that the code can run without errors.

For this reason, we can execute the malicious JS code without needing to insert the closing </script> tag on the comment field, the browser itself inserts it.

Now, we can see that the </h3><br> tags are comments interpreted by JS because they are in between /**/. Then, the </p> tag is being commented by the normal // characters in JS.

Since the HTML tags are not closed properly, the browser then adds the </script></h3></p> tags

Takeaways

XSS is one of the most common vulnerabilities out there because any user-supplied input can be used for malicious purposes. Programmers must validate that every user-supplied parameter on every endpoint is being properly filtered/encoded. Stored XSS is more critical than Reflected XSS since any user, including admins, who visits the page will trigger the malicious JS code.

As we saw, just because the first name parameter was being limited to only 12 characters and the comment parameter was properly being encoded, it doesn't mean that the endpoint was protected against an XSS attack. As a hacker, you must follow your instinct and don’t give up once you stumble upon a brick wall, try to use every parameter at your disposal and get creative.

Thank you for reading this blog as it is my first one. I hope you learn something new.

Feel free to leave a comment.

Best regards,

Joel (Rintox)
