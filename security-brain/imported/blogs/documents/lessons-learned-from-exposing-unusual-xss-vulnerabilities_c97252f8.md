---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-09_lessons-learned-from-exposing-unusual-xss-vulnerabilities.md
original_filename: 2024-07-09_lessons-learned-from-exposing-unusual-xss-vulnerabilities.md
title: Lessons Learned From Exposing Unusual XSS Vulnerabilities
category: documents
detected_topics:
- xss
- api-security
- supply-chain
- sso
- access-control
- command-injection
tags:
- imported
- documents
- xss
- api-security
- supply-chain
- sso
- access-control
- command-injection
language: en
raw_sha256: c97252f8784ef451dc9304dc1b6ac76184aafeade52d684e5447d5bcfc293431
text_sha256: 8daf4422337f2ce3776f8ef8cbf23d34b395f0aa49a441773917d88459f95cc3
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Lessons Learned From Exposing Unusual XSS Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-09_lessons-learned-from-exposing-unusual-xss-vulnerabilities.md
- Source Type: markdown
- Detected Topics: xss, api-security, supply-chain, sso, access-control, command-injection
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `c97252f8784ef451dc9304dc1b6ac76184aafeade52d684e5447d5bcfc293431`
- Text SHA256: `8daf4422337f2ce3776f8ef8cbf23d34b395f0aa49a441773917d88459f95cc3`


## Content

---
title: "Lessons Learned From Exposing Unusual XSS Vulnerabilities"
page_title: "Lessons Learned From Exposing Unusual XSS Vulnerabilities | Imperva"
url: "https://www.imperva.com/blog/lessons-learned-from-exposing-unusual-xss-vulnerabilities/"
final_url: "https://www.imperva.com/blog/lessons-learned-from-exposing-unusual-xss-vulnerabilities/"
authors: ["Ron Masas (@RonMasas)"]
programs: ["Replicate", "ZoomInfo"]
bugs: ["DOM XSS", "postMessage", "Chatbot"]
publication_date: "2024-07-09"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 180
---

Misunderstood browser APIs are often at the core of many web security issues. With the rapid expansion of web APIs, keeping up with security best practices can be challenging. In this post, we’ll explore a few common mistakes developers make that lead to modern XSS (Cross-Site Scripting) vulnerabilities. These insights stem from specific vulnerabilities we identified and responsibly disclosed to Replicate and ZoomInfo, which are now patched.

## The PostMessage API

PostMessage is a web API that allows scripts from different origins to communicate with each other in a secure manner. However, this security relies heavily on developers implementing proper authorization checks. Unfortunately, it’s all too common for developers to either overlook these checks or implement them incorrectly, leading to vulnerabilities such as XSS.

## Introduction

ZoomInfo Chat (formerly InSent.AI) is a conversational marketing platform designed to enhance website engagement and lead generation. It offers real-time, personalized interactions with visitors through AI-driven chatbots and live chat.

## The Bug

While testing a site that uses ZoomInfo Chat, we audited the post-message event handler code and noticed a straightforward DOM XSS vulnerability. However, exploiting it seemed impossible at first.

Unlike the common case where developers forget to validate incoming messages altogether (as we discussed in our [TikTok vulnerability blog post](https://www.imperva.com/blog/imperva-red-team-discovers-vulnerability-in-tiktok-that-can-reveal-user-activity-and-information/)), ZoomInfo Chat decided to reinvent the way these messages should be authorized. Instead of checking the message origin, they used a randomly generated token to ensure the authenticity of the message. However, we found a workaround and managed to leak the token.

The supply chain risk in this scenario is significant. Many websites embed the vulnerable ZoomInfo Chat widget, leading to a widespread security issue across numerous domains. When a widely-used third-party script has a vulnerability, it becomes a single point of failure that attackers can exploit to compromise multiple websites.

<https://www.imperva.com/blog/wp-content/uploads/sites/9/2024/07/zoominfo-chat-dom-xss.mp4>

### 

### Exploiting The ZoomInfo Chat Widget

The vulnerability discovered can be exploited through a two-step process involving both the leakage of a secret token and the exploitation of a DOM XSS issue. Here’s how it works:

**Step 1: Leaking the Token**

The developers seem to have confused `window.parent` with `window.top`, which is an easy mistake since they often behave similarly. 

Here’s the difference: `window.top` references the topmost window in the hierarchy, while `window.parent` references the direct parent of the current window.

The ZoomInfo Chat script loads the chat user interface using an iframe that points to “https://{user}.widget.insent.ai.” The widget uses `window.top.postMessage` to send information, including a secret token, back to the parent window. This is intended to ensure that only the hosting site can communicate with the Chat widget.

However, if an attacker embeds a site that includes the ZoomInfo Chat widget on their own website, they can intercept this communication and obtain the secret token.

Here’s how the `postMessage` function is used in the ZoomInfo Chat script:

Additionally, the code uses `*` as the intended origin. If the developers specified the intended origin, the token could not be leaked even with the use of `window.top`.

**Step 2: Exploiting the DOM XSS Issue**

Once the attacker has the secret token, they can use it to communicate with the ZoomInfo site. The attacker then exploits a DOM XSS issue related to the handling of the `iframe-resize` event. Here is the vulnerable code snippet:

The code removes any existing element with the ID “insent-style” and then recreates it using style data received from a post message event. However, it does this insecurely by using the `insertAdjacentHTML` method with untrusted and unsanitized input, which can lead to XSS.

## The Misunderstood Blob

Blob URLs are a unique type of URL that allow developers to reference content that the browser has in memory. A Blob URL is composed of a “blob” protocol, followed by the origin of the site and a unique identifier. They typically look something like this:

At first glance, Blob URLs may seem to operate under a separate protocol, giving developers the impression that they are isolated by the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), a security measure that restricts how documents or scripts loaded from one origin can interact with resources from another origin. An origin is defined by the combination of the protocol, hostname, and port number.

However, the “protocol” in Blob URLs is not really considered by the same-origin policy, which makes this a perfect place to make a mistake.

## Introduction

Replicate.com is a platform for sharing and interacting with AI models. Users can browse, upload, and finetune models for specific needs. The platform supports private model hosting and offers scalable deployment with a simple API.

One of my favorite features of Replicate is the playground, which lets users experiment with AI models by uploading files and previewing results.

## The Bug

When a user drags and drops a file as an input to some AI model in the playground, a Blob URL is generated with the uploaded file content and MIME type. If the user clicks the preview of such an image, the Blob URL opens in a new tab. By embedding a script tag within an SVG image, we were able to execute arbitrary JavaScript that runs in the context of Replicate.com as soon as the user clicks the SVG preview.

While other file types like .html also work, using SVG makes successful exploitation much more likely due to the SVG preview. We specifically used an image that closely resembles the Replicate user interface, showing an “error” which prompts the user to click for more information.

<https://www.imperva.com/blog/wp-content/uploads/sites/9/2024/07/replicate-xss.mp4>

### 

### Exploiting Replicate.com

  1. Send a malicious SVG file to the target and ask them to test it on any Replicate model that accepts images as input.
  2. Upon uploading, the user will immediately see a fake error message prompting them to click for more information.
  3. The user clicks the “error” message.
  4. Our XSS payload executes, exfiltrating the user’s account API key.

This isn’t an isolated incident, in our recent post about [two XSS vulnerabilities we found in ChatGPT](https://www.imperva.com/blog/xss-marks-the-spot-digging-up-vulnerabilities-in-chatgpt/), the first issue was the misuse of Blob URLs with attacker-controlled content.

## Post Exploitation Risks

The trade-off between ease of use and security is a significant factor in the design of many web platforms, including Replicate. In an effort to enhance user experience, Replicate makes API keys easily accessible in the user account settings. This convenience allows users to quickly retrieve their keys without having to go through additional steps, unlike other platforms that only show the key once at the time of generation.

However, this ease of access comes at a cost. In the case of Replicate, the straightforward availability of API keys means that a simple XSS vulnerability can have severe consequences. Once an attacker exploits an XSS flaw, they can easily exfiltrate the user’s API key. Since the key is readily available in the dashboard.

The critical issue here is the lack of user awareness. Users have no way of knowing that their key has been compromised until it’s too late. By the time they realize something is wrong, the attacker may have already used the key to perform unauthorized actions, such as accessing private models, manipulating data, or incurring charges on the user’s account.

## Key Takeaways

In conclusion, understanding and mitigating common developer mistakes is crucial to prevent XSS vulnerabilities. Developers should remember to:

**Beware of Blob URL Misconceptions**

Blob URLs may appear to be protected by the same-origin policy, but they are not. Developers need to ensure that user-uploaded content via Blob URLs is thoroughly sanitized and handled with caution to avoid XSS vulnerabilities.

**Don’t Reinvent PostMessage Authorization**

Avoid creating custom authorization protocols for the PostMessage API. Rely on established, well-vetted security standards and libraries instead. Custom protocols are often less secure and more vulnerable to exploitation due to insufficient testing and scrutiny.

**Supply Chain Vulnerabilities and The Post Message API**

Third-party scripts can introduce widespread vulnerabilities. When integrating external scripts, ensure they follow security best practices and regularly review their security posture. As developers, it’s crucial to understand how these scripts change our attack surface, particularly with APIs like PostMessage.

By adhering to these best practices, developers can significantly reduce the risk of XSS attacks and enhance the overall security of their applications.

### Try Imperva for Free

Protect your business for 30 days on Imperva.

[Start Now](https://www.imperva.com/free-trial/)
