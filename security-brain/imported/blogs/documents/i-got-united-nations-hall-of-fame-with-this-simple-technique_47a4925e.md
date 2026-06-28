---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-15_i-got-united-nations-hall-of-fame-with-this-simple-technique.md
original_filename: 2023-02-15_i-got-united-nations-hall-of-fame-with-this-simple-technique.md
title: I Got United Nation’s Hall Of Fame With This Simple Technique!
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
raw_sha256: 47a4925ed4a83622c3b64c48179133fbbcf4f81527e11a5d1f8cb0976315dcdf
text_sha256: e076acc613dae38891904ffb4e782a9a24f87f855e3b6ef2cb4fe2e2caddb2a5
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# I Got United Nation’s Hall Of Fame With This Simple Technique!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-15_i-got-united-nations-hall-of-fame-with-this-simple-technique.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `47a4925ed4a83622c3b64c48179133fbbcf4f81527e11a5d1f8cb0976315dcdf`
- Text SHA256: `e076acc613dae38891904ffb4e782a9a24f87f855e3b6ef2cb4fe2e2caddb2a5`


## Content

---
title: "I Got United Nation’s Hall Of Fame With This Simple Technique!"
page_title: "I GOT UNITED NATION’S HALL OF FAME WITH THIS SIMPLE TECHNIQUE! | by Faiyaz Ahmad | Medium"
url: "https://faiyazhacks.medium.com/i-got-united-nations-hall-of-fame-with-this-simple-technique-3d9a021e4a5d"
authors: ["Faiyaz Ahmad"]
programs: ["United Nations"]
bugs: ["HTML injection"]
publication_date: "2023-02-15"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1527
scraped_via: "browseros"
---

# I Got United Nation’s Hall Of Fame With This Simple Technique!

I GOT UNITED NATION’S HALL OF FAME WITH THIS SIMPLE TECHNIQUE!
Faiyaz Ahmad
Follow
5 min read
·
Feb 15, 2023

256

4

Press enter or click to view image in full size

Hi everyone! I hope you all are good and having a wonderful day. I know its been a long time since i have written articles on Medium. The reason behind this is that i am currently working more on my YouTube channel and on BePractical. A small summary: Me with my friends are trying to create a platform that aims to provide cybersecurity as well as web development contents, articles, services etc. for free or for as low price as possible. We have lot more contents on Bug Bounty, Cybersecurity etc on our website so do check it out by clicking here.

Press enter or click to view image in full size
https://bepractical.tech

Now, let’s get back to the topic. In this article, I am going to tell you a simple yet effective technique to find vulnerability that i have used on United Nation. Let’s begin

Part1: The Method/Technique

Let’s try to understand what this technique is all about. The idea is quite simple, Look for one vulnerability at a time. That means, First identify the vulnerability that you want to look on the target and then start using various methods/tools to find that vulnerability. Which means, that you need to first have a vulnerability in your mind and then start looking that vulnerability. Until you’ve found that vulnerability or scanned the target manually for that vulnerability, don’t look for other stuffs!(Mostly works in target that with huge assets in scope) For example, Let’s assume that there is a target (*.example.com)

Step 1: The first thing we need to do is to analyze the target in depth. Like looking for the technology on which the web application is working, ports running on the server etc. Let’s assume that example.com is running behind a PHP and have a lot of input fields. So tell me, Which vulnerability should we look into the target?

The answer is: those vulnerabilities that uses some input field to be exploited. (Now, it’s your job to name out few vulnerabilities that requires input in the comment😉) For this example, let’s assume that we want to look for Cross Site Scripting.

Step 2: Now we have one vulnerability in mind i.e. Cross Site Scripting. In this step, our goal is to find the common places where xss usually occurs. I guess we all know that xss occurs mostly in GET parameters and POST forms. Therefore, we need to find all possible get parameters and forms.

Press enter or click to view image in full size
A common method to extract GET and POST parameters

Tip: You can use tools like arjun, katana, gau, waybackurl, dirsearch, google dork etc to find as many links as possible or you can automate this process by writing a bash script(or use ChatGPT for it😉)

Step 3: The final step is to start looking for cross site scripting with the data we’ve filtered out. Hopefully, we may eventually able to find XSS on the target.

Get Faiyaz Ahmad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I hope you have understood this simple technique. Now, let’s jump to the second part of this article.

Part 2: The Story

So, I was hunting on the United Nation’s bug bounty program and this time i thought “hmm..i’ll look for only HTML Injection vulnerability in email” because i know that this type of misconfiguration is often ignored by the developers. Therefore, The first thing that i did was to look for all the endpoints that have registration functionality using the google dork below

site:<un_owned_domains> inurl:register

Now, this simple query will return a lot of results in which have the registration functionality

Press enter or click to view image in full size

Now after this, I have manually checked few subdomains for the HTML Injection vulnerability and after few minutes I got one!!

Press enter or click to view image in full size

It turns out that they were not filtering the dangerous < and > characters in the First Name and Last Name field. As a result, I was able to execute a simple HTML tag in the email i.e <h1>Test</h1>.

After that, I quickly reported this vulnerability to their security team and got my name listed in their Hall of Fame after a week.🥳

😁
CONCLUSION

I hope you have learned something new in this article. The key point is to understand your target in depth as the more you understand your target, the more you will get vulnerabilities. And always try to look for a single vulnerability and a time. Doing this will eventually help to not only find vulnerabilities but also your understanding of that vulnerability will also increase.

If you have any doubts then feel free to let know. Join our telegram channel over here if you want to stay updated with the latest trends going in cybersecurity.

Also, If you like my articles then do check out this video on “Finding Hidden Links from JavaScript files”

Let’s meet again in some other article. Till then
