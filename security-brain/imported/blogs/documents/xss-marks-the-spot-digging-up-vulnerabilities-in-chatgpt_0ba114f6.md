---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-19_xss-marks-the-spot-digging-up-vulnerabilities-in-chatgpt.md
original_filename: 2024-02-19_xss-marks-the-spot-digging-up-vulnerabilities-in-chatgpt.md
title: 'XSS Marks the Spot: Digging Up Vulnerabilities in ChatGPT'
category: documents
detected_topics:
- xss
- csrf
- api-security
- sso
- access-control
- command-injection
tags:
- imported
- documents
- xss
- csrf
- api-security
- sso
- access-control
- command-injection
language: en
raw_sha256: 0ba114f64b1a72a046b8e9559a4c05a60012037167ba6066d309f186987fae5e
text_sha256: bfc23b6bd62b534b8911241d3f8716a882c57001f3cdee972b310f4b2c092108
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Marks the Spot: Digging Up Vulnerabilities in ChatGPT

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-19_xss-marks-the-spot-digging-up-vulnerabilities-in-chatgpt.md
- Source Type: markdown
- Detected Topics: xss, csrf, api-security, sso, access-control, command-injection
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `0ba114f64b1a72a046b8e9559a4c05a60012037167ba6066d309f186987fae5e`
- Text SHA256: `bfc23b6bd62b534b8911241d3f8716a882c57001f3cdee972b310f4b2c092108`


## Content

---
title: "XSS Marks the Spot: Digging Up Vulnerabilities in ChatGPT"
page_title: "XSS Marks the Spot: Digging Up Vulnerabilities in ChatGPT | Imperva"
url: "https://www.imperva.com/blog/xss-marks-the-spot-digging-up-vulnerabilities-in-chatgpt/"
final_url: "https://www.imperva.com/blog/xss-marks-the-spot-digging-up-vulnerabilities-in-chatgpt/"
authors: ["Ron Masas (@RonMasas)"]
programs: ["OpenAI (ChatGPT)"]
bugs: ["AI", "LLM", "XSS", "CSP bypass", "Samesite cookie bypass", "Mass assignment"]
publication_date: "2024-02-19"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 420
---

With its widespread use among businesses and individual users, ChatGPT is a prime target for attackers looking to access sensitive information. In this blog post, I’ll walk you through my discovery of two cross-site scripting (XSS) vulnerabilities in ChatGPT and a few other vulnerabilities. When chained together, these could lead to account takeover.

## Digging into ChatGPT

My journey began with examining ChatGPT’s tech stack. The use of NextJS, a popular React framework, initially made me skeptical about finding an XSS vulnerability. However, as I explored its functionalities and client-side code, I noticed something that changed my mind.

## The Initial Discovery

ChatGPT lets users upload files and ask questions about them. When answering, ChatGPT may quote these files and include a clickable citation icon that takes you back to the original file or website for reference.

Figure 1: Vulnerable Code

The code above handles the citation click event. It processes the file’s content into a blob, which is then opened with the `window.open` function. Depending on the file content type, this method could potentially be a security risk.

I tested this by uploading an HTML file with text and JavaScript. ChatGPT processed it and provided a citation. When I clicked on the citation, the HTML content displayed on my screen via a blob URL, but a Content Security Policy (CSP) violation blocked my JavaScript payload.

## Bypassing CSP

Figure 2: ChatGPT CSP Policy

Investigating the CSP policy, I noticed that the nonce value, which is supposed to be dynamic, was static. A nonce is a unique string that lets specific HTML elements bypass CSP restrictions. Typically, this value changes with each request, ensuring only server-approved elements execute. However, here it remained unchanged.

Testing this with another account and a different IP address confirmed the issue. I then uploaded a new HTML file with a script tag that included this nonce attribute. This time, my script was executed successfully upon clicking the citation.

<https://www.imperva.com/blog/wp-content/uploads/sites/9/2024/02/3-chatgpt-xss.mp4>

## Challenges and Limitations

Exploiting this vulnerability is not straightforward. It requires the user to upload a harmful file and engage in a way that prompts ChatGPT to quote from this file. Then, the user needs to click the citation to trigger the XSS.

I looked into ChatGPT’s feature for sharing conversations as a possible way to make this exploit shareable. The plan was to share a conversation link with the target and get them to click a citation, which would trigger the XSS.

This approach didn’t work as expected. Files uploaded in a ChatGPT conversation are accessible only to the account that uploaded them. Attempts to access these files from another account resulted in a 404 error.

Figure 3: Download file failure

## New Approach with Knowledge Files

[GPTs](https://openai.com/blog/introducing-gpts), introduced by OpenAI, come with knowledge files. These files function through an API quite similar to the one used for user-uploaded files but with a notable addition—a “gizmo_id” parameter. Through my exploration, I discovered that when a GPT is set to public, it enables any account to access and download these knowledge files, as long as they have the necessary information – specifically, the GPT ID and the associated file ID.

I’ve considered this a Broken Function Level Authorization bug since it allows any ChatGPT user to download public GPT knowledge files.

Figure 4: GPTs Files API

This led to a new possibility for exploitation. If I can make the shared conversation request a public file instead of the original uploaded file, it could make the XSS vulnerability exploitable.

I’ve focused on the _“/backend-api/conversation”_ endpoint for starting ChatGPT conversations. Below is how the request body looks:

Figure 5: Conversation Request Body

I noticed this structure was similar to the assistant’s metadata I saw in the “pageProps” object of a shared ChatGPT conversation I had previously created.

Figure 6: Assistant message metadata

I saw the citation object inside the assistant message metadata, which included the file ID I had uploaded. This was the same ID used by the vulnerable code I initially discussed to fetch the file contents. At this point, I realized that I could probably make this vulnerability shareable if I could control this metadata.

## Experimenting with Roles and Mass Assignment

I then explored whether and how I could manipulate this metadata. I started by trying to change the role from “user” to “assistant” in the conversation. To my surprise, ChatGPT accepted this change and continued generating responses as if they were from the assistant.

Next, I tried adjusting the metadata to match the citation structure I saw in the “pageProps” object. This method also worked, indicating the presence of a Mass Assignment vulnerability. A Mass Assignment vulnerability arises when an application indiscriminately assigns user-provided data to internal objects or variables. This can happen if the application doesn’t properly filter or limit what data can be assigned. In this context, I could use input data to manipulate aspects of the ChatGPT application — specifically, the citation metadata — in ways that should ordinarily be off-limits to a regular user.

## The Exploit

I crafted a new request to the “/backend-api/conversation” endpoint, impersonating the assistant and injecting a custom citation object. The only change I made was to set the file ID to _“file-Cbn7djQD1W20s3h5JM8NfFs8/download?gizmo_id=g-ghPiYIKcD#”_ forcing ChatGPT client-side to use the GPTs API instead.

This exploit worked as planned. I created and shared a conversation, and when tested with another ChatGPT account, clicking any citation in the conversation downloaded the knowledge file from my public GPT, which triggered the XSS.

<https://www.imperva.com/blog/wp-content/uploads/sites/9/2024/02/shareble_xss_chatgpt.mp4>

I reported this vulnerability to OpenAI. They responded by removing the blob creation and altering the logic to open the download URL directly.

Figure 7: OpenAI’s Patched Code

Post-fix, I examined additional functionalities involving “context_connector,” “metadata,” and “download_url.” However, these components did not present any new vulnerabilities since the conversation metadata cannot directly control those values.

## Another XSS Vulnerability

I then broadened my investigation by examining additional functionalities related to how ChatGPT handles the rendering of citations from websites. This exploration led me to the following code:

Figure 8: Vulnerable Code #2

While examining the code, I noticed that the citation metadata object, referenced as _“em”_ in the code, was directly used to set the “href” attribute of a citation link (i.e., `em.url`). This was a red flag because, as I had already established, I could manipulate the metadata by impersonating the assistant.

## Initial Test and a New Challenge

To test this vulnerability, I set up a new conversation. In this setup, I manipulated the citation metadata, setting its URL value to a JavaScript protocol URL, like “javascript:alert(1)”. However, the exploitation didn’t go as planned. Although I successfully set the anchor tag’s `href` attribute to my JavaScript URL, the tag also contained a `target=”_blank”` attribute. This attribute, as I’ve discussed in a previous blog post, “[Hacking Microsoft and Wix with Keyboard Shortcuts](https://www.imperva.com/blog/hacking-microsoft-and-wix-with-keyboard-shortcuts/),” can only be exploited using keyboard shortcuts.

ChatGPT allows its interface to be embedded in other websites using an `iframe.` This meant the vulnerability could be triggered from an entirely different website.

In my proof of concept, I embedded the shared ChatGPT conversation within an `iframe` and used CSS to position it so that any click would inadvertently trigger the citation link. To make the iframe invisible, I set its opacity to zero. Layered on this invisible iframe, I added the text “Hold ⌘ and click to open me in a new tab.” A user following these instructions would unknowingly execute arbitrary JavaScript on chat.openai.com.

## SameSite Cookies & Storage Partitioning

Another obstacle involved [SameSite cookies](https://web.dev/articles/samesite-cookies-explained) and [storage partitioning](https://developers.google.com/privacy-sandbox/3pcd/storage-partitioning), security measures designed to safeguard privacy and security on the web by limiting how browsers manage cookies and other types of storage across different origins. In our scenario, when a user visited our malicious site that embedded an iframe linking to our ChatGPT shared conversation, these measures would block access to the ChatGPT session cookie and LocalStorage, effectively logging them out of their account within the iframe.

These security features aim to protect against Cross-Site Request Forgery (CSRF) attacks and various forms of side-channel cross-site tracking attacks, such as [Timing Attacks](https://dl.acm.org/doi/10.1145/352600.352606), [XS-Leaks](https://github.com/xsleaks/xsleaks), and [Cross-Origin State Inference (COSI) attacks](https://arxiv.org/pdf/1908.02204.pdf). Notably, the threat model for these measures does not include Cross-Site Scripting (XSS), which is the vulnerability we exploited in this scenario.

By creating a Blob object containing HTML content and generating a URL for it using the URL.createObjectURL method within the chat.openai.com context, I was able to navigate the parent window to this Blob URL. This bypasses the SameSite cookie restrictions and storage partitioning. This was possible because the navigation, initiated from within chat.openai.com, was considered a same-origin request, thus not subject to the typical cross-origin restrictions, **enabling the takeover of any ChatGPT account.**

<https://www.imperva.com/blog/wp-content/uploads/sites/9/2024/02/embeded-chatgpt-exploit.mp4>

Below is our final exploit code:

Figure 9: Final exploit code

## OpenAI’s Fix

After discovering these vulnerabilities, I promptly shared my proof of concept with OpenAI. Their response was impressively quick, fixing the XSS issue within a few hours by adding client-side validation for citation URLs.

Below, you can see that the “eF” method was added and used when rendering the citation links, validating that only the “https,” “mailto,” and “tel” protocols can be used.

Figure 10: OpenAI’s Patched Code #2

## Closing Thoughts

I want to express my gratitude to OpenAI for their collaborative and efficient approach to addressing these vulnerabilities. It’s rewarding to know that our efforts have made ChatGPT more secure for all its users.

Watch for our next blog post, where we’ll delve into The Double Agent attack, a new post-exploitation technique we developed for ChatGPT-like systems.

### Try Imperva for Free

Protect your business for 30 days on Imperva.

[Start Now](https://www.imperva.com/free-trial/)
