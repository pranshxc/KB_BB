---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-16_alternative-link.md
original_filename: 2022-10-16_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: dab45e0b052f3b971464bd4c81a470db815a8774f262240ac01293dc6f6aa198
text_sha256: 0dc99649f9a79e41e46c8a620bf430ea48c2235fa0888f5460d5b555b1d3df7e
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-16_alternative-link.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `dab45e0b052f3b971464bd4c81a470db815a8774f262240ac01293dc6f6aa198`
- Text SHA256: `0dc99649f9a79e41e46c8a620bf430ea48c2235fa0888f5460d5b555b1d3df7e`


## Content

---
title: "Alternative link"
page_title: "How I Got $10,000 From GitHub For Bypassing Filtration oF HTML tags | by Saajan Bhujel | InfoSec Write-ups"
url: "https://infosecwriteups.com/how-i-got-10-000-from-github-for-bypassing-filtration-of-html-tags-db31173c8b37"
authors: ["Saajan Bhujel (@saajanbhujel)"]
programs: ["GitHub"]
bugs: ["XSS"]
bounty: "10,000"
publication_date: "2022-10-16"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2036
scraped_via: "browseros"
---

# Alternative link

How I Got $10,000 From GitHub For Bypassing Filtration oF HTML tags
Saajan Bhujel
Follow
8 min read
·
Oct 16, 2022

1.1K

11

Hey everyone👋

I hope you’re having an A+ week🚀!

In today’s blog, I am going to tell you that, “How I Got $10,000 From GitHub For Bypassing A Filtration oF HTML tags”

Press enter or click to view image in full size

A
few months back, One day I was just scrolling the Twitter feed. And, Suddenly a tweet from @github came into my focus. Basically, The Tweet was regarding GitHub’s new feature that gives the ability to render or display Mathematical expressions(TeX and LaTeX style syntax) in Markdown through the MathJax library.

What is MathJax?

MathJax is an open-source JavaScript display engine for LaTeX, MathML, and AsciiMath notation that works in all modern browsers, with built-in support for assistive technology like screen readers.

After reading the tweet, I got to know that, “GitHub is now using MathJax library to display Mathematical expressions in Markdown files”. So, The first thing I tried was to find any previous or known bugs in the MathJax library. And mainly, I was looking to find any previous XSS or HTML injection CVEs.

Luckily, I found the known XSS issue in the MathJax library which affects versions <2.7.4 . And, The Payload should be in a Unicode form to work.

\unicode{}

Press enter or click to view image in full size
Known CVE in a MathJax library which affects versions <2.7.4

Then, I created a markdown file in my test repository. And, I started my testing. So, I entered 👇 this payload in a file:

Payload:- $$\\u003cu\u003eHello\u003c/u\u003e{}$$ or $$\\u003cu\u003eWhy\u003c\uffofu\u003e{}$$ , etc.

*Note: $$...$$ are math delimiters.

But, Nothing worked for me. And, I knew the reason is that “The CVE was only vulnerable for version <2.7.4 meanwhile the GitHub is using a newer version”.

Thus, I thought that “I had to find a bypass by myself to successfully exploit the attack and If somehow I am able to render basic HTML tags like: <b>,<i>,<u>.” And, You may be wondering why I said only basic HTML tags? Coz, Most of the time websites use WAFs, different kinds of filters, and restrictions to prevent the use of advanced tags but they don’t do the same thing for basic and common tags. That’s why I said!.

And once I found a bypass or way to render basic tags using math expressions. Then only in this situation, “I will try to escalate the impact by trying advanced tags”.

The First way or method of exploiting:

So, The first thing I did “was to find any interesting behavior which can be very useful for me to render basic tags using math expressions”. For this, I tried different-different types of methods(like Unicode, URL encoding, and etc). And again, This also does not work for me.

But, Somehow I was able to find a way that is very helpful for rendering the basic tags using math expressions. I noticed that “when I used basic tags after the \ then only that time the tag gets render without any error or without being filtered”.And, The payload is $$\<u>HELLO</u>{}$$

So, I quickly replaced the <u> tag with other advance tags(like <script>,<iframe>, <style>) in order to know “Is the website using more filters to prevent the use of the advance tags?”. The answer is Yessss, The GitHub markdown files are using some more filters in which “they simply filtered any advance tags except <style> tags”.

Then after testing this mathjax integration, I found that it’s possible to add <style> tags on using a backslash(\) before it (like: \<style>{property:value}</style>). So for customizing the CSS, I used these below payloads in my test.md files:

$$\<style>*{display:none}</style>{}$$
$$\<style>div{background-color:#66f3e6}</style>{}$$
$$\<style>*{font-size:23px;}</style>{}$$
$$\<style>body{padding: 50px;background-color: #4b6bb7;}</style>{}$$

Hence, I noticed that now I am able to change the CSS of the whole page.

Press enter or click to view image in full size
Able to change the CSS of the page using this method

And, I created and submitted my first report to GitHub’s HackerOne program. But, You know what happens with my report “Report closed within 5 mins by bot saying that it is a previously identified issue and is being tracked internally”. For the minutes, I was so confused and thought that “The bot is really a bot or a human is behind the bot”.

So, I asked the program, “Is this quick response coming from the BOT or from a real person?”. Then, GitHub’s traiger confirmed and replied, “Yes, please rest assured that your report was reviewed by a real person. Thanks for checking in on my humanity!”

All I can say is that “My first ever bug report to GitHub closed as Duplicate”.

The second way or method of exploiting:

GitHub fixed the issue within 24 hours.

So, I thought to retest the issue with my previous method and payloads. And, I found that “I was no more able to use advance tags with previous method and payloads”.

And somehow, I managed to find a new way to render tags. But this time, I was only able to use normal tags(like: <div>,<span>,<section>,<input>,<label>,<button>) not “<style> and <script>” in the math expressions.

$$<div>Test</div>{}$$
$$<input type=text>{}$$
$$<button>Click Here</button>{}$$

Although, We can also use a few tags like “<div>,<span>, and <section>” without math expressions in markdown files. But usually, It’s not possible for us to render tags like “<input> and <button>”. So, This is a big win situation for me because I already found a way where “I was able to use tags like <input> and <button> using math expressions in markdown files”.

Get Saajan Bhujel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Still, I didn’t reported this to GitHub because “I did not see any impact here except using restricted tags”. So, I tried to find something similar to the above first way where maybe I can modify the CSS of the page. But as I already said that “After the fix, I was no more able to use <style> tag”. So, The only option left was to use the style attribute to modify CSS but again one more problem comes was that “GitHub restricts the use of attributes”.

* NOTE *

As we know that we can use “class”, “id” and a few more attributes in markdown(.md) files but not the “style” attribute because it may lead to a change in the CSS of the page.

But do you know one thing? surprisingly, I was able to use the “style” attribute only with math expressions. And at the same time, It’s kinda impossible to use the “style” attribute in the markdown files without using math expressions.

Payload:- $$<tag style="property:value" acceptedAttribute="True"></tag>{}$$

So, I simply created a payload that makes my markdown file page like a login page.

$$<div style="position:fixed;padding:10%;padding-right:100%;left:-9%;top:-20%;background:white;padding-bottom:100%;"><section style="margin-left:500px;padding:30px;"><h2 style="text-align:center;">Sign in to GitHub</h2><div><label>Username: </label><input type=text style="border-radius:5px;border:1px solid;">
<label>Password=***REDACTED*** type=password style="border-radius:5px;border:1px solid;"><div style="text-align:center;"><button style="background:#2da44e;color:white;margin:10px;border-radius:9px;border:none;font-weight:500;padding:4px;padding-right:20px;padding-left:20px;" type=submit>Sign in</button></div></section></div></div><!--{}$$
Press enter or click to view image in full size
Bypass the fixed and this time I was able to use tags and change CSS

But this time, I did not created a new report because “I found the bypass on the next day, and also in the last report the team also stated that they are internally working on this”. Cause, I thought “If the team is still working on this feature, then they might again close the report as Duplicate”.

So, I only commented that “I just found a bypass that can again change the CSS of the whole page. So please let me know, whether the internal team fixed the issue or not? Cause I am not able to reproduce it more with the last method! If yes(the issue is fixed) then, I am happy to create a new report as a bypass…..” on the last report.

And, The GitHub staff replied with the below statement that you can see in the below image😁.

Press enter or click to view image in full size

On the next day when I woke up, I noticed that the GitHub team again fixed the issue because the new payload was not working anymore😶. So, This shows that “they were right and they literally working internally on the MathJax”.

The third way or method of exploiting:

Still, I didn’t stop myself to find something unusual in the MathJax feature.

I noticed that after the second fix, I wasn’t able to render any of the advance tags using the previous payloads.

If you saw my two above payloads for two different methods then you can clearly see that “I used a backslash(\) before using any tags in math expressions like: \<tagName>{} ”

Same, I also noted this thing and changed my payload position from $$\<tagName>{}$$ to $$\{<tagName>}$$ in math expressions. Yet, the tags were filtered. But after spending more time, I finally found a method to render a few tags like <input>,<svg>,<button>,<textarea> using MathJax.

Payload: $$\<script>{&lt;renderTag&gt;}$$

How this payload work: (Read in detail)

At the first position after the backslash(\), the tags should be a malicious tag that gets filtered out from the payload like \<script> or \<style>
And, The main tag that we want to render, should be in between the curly bracket {&lt;renderTag&gt;} . The Greater and Less than signs should be in the form of HTML entities.

So our, Final payload will look like: $$\<script>{&lt;renderTag&gt;}$$. From this, the <script> or any tag that is written before the curly bracket will be filtered out. And, The Mathjax will then only render tags that are in the curly brackets.

I used these below payloads in my test.md files for POC.

$$\<script>{&lt;div&gt;&lt;section&gt;&lt;h2&gt;Sign in to GitHub&lt;/h2&gt;&lt;label&gt;Username: &lt;/label&gt;&lt;input&gt;&lt;br&gt;&lt;label&gt;Password=***REDACTED*** in&lt;/button&gt;&lt;/section&gt;&lt;/div&gt;<!--}$$
## Input tag:
$$\<script>{&lt;input&gt;<!--}$$
## Button tag:
$$\<script>{&lt;button&gt;Test Button&lt;/button&gt;<!--}$$
## Textarea tag:
$$\<script>{&lt;textarea&gt;Write something...&lt;/textarea&gt;<!--}$$
Press enter or click to view image in full size
Able to use a few advanced tags in math expressions

Although, I tried to increase the impact of this issue but failed.

So, I reported this issue to GitHub as Low severity. And this time, GitHub accepted the issue as Medium severity and paid the bounty of $10,000 with SWAG and GitHub Pro free of charge.

Press enter or click to view image in full size
GitHub accepted the issue as Medium severity and paid the bounty of $10,000

All I can say is that “this new MathJax feature brings some misconfiguration”.

Summary of payload:

(I) Payload that I used in the first method or way
$$\<style>{property:value}</style>{}$$
(II) Payload that I used in the second method or way
$$<tag style="property:value" acceptedAttribute="True"></tag>{}$$
(III) Payload that I used in the third method or way
$$\<script>{&lt;renderTag&gt;}$$

Timeline of the reports:
May 21st - Reported the first report to GitHub
May 21st - Report closed as Duplicate
May 24th - Again Reported the issue with a new bypass to GitHub
May 25th - Report triaged by the GitHub
Aug 20th - GitHub resolved the issue
Aug 20th - GitHub rewarded me with the $10,000 bounty, a SWAG, and GitHub Pro as well.

If you liked this blog, then give me a follow✨

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
