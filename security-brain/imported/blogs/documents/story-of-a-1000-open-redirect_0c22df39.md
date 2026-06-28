---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-01_story-of-a-1000-open-redirect.md
original_filename: 2024-07-01_story-of-a-1000-open-redirect.md
title: Story of a 1000$ Open Redirect
category: documents
detected_topics:
- ssrf
- xss
- csrf
- oauth
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- csrf
- oauth
- command-injection
language: en
raw_sha256: 0c22df394a1f84478918f20138b1e9953ff0ee0e638e9cafcedfdffdec9fa49e
text_sha256: 3ac29c5a0299066f8bc767aef2fb60b4ed72b81cab23212b89d92af4203e6495
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a 1000$ Open Redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-01_story-of-a-1000-open-redirect.md
- Source Type: markdown
- Detected Topics: ssrf, xss, csrf, oauth, command-injection
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `0c22df394a1f84478918f20138b1e9953ff0ee0e638e9cafcedfdffdec9fa49e`
- Text SHA256: `3ac29c5a0299066f8bc767aef2fb60b4ed72b81cab23212b89d92af4203e6495`


## Content

---
title: "Story of a 1000$ Open Redirect"
url: "https://infosecwriteups.com/story-of-a-1000-open-redirect-1405fb8a0e7a"
authors: ["Debangshu Kundu (@debangshu_kundu)"]
bugs: ["Open redirect"]
bounty: "1,000"
publication_date: "2024-07-01"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 210
scraped_via: "browseros"
---

# Story of a 1000$ Open Redirect

Story of a 1000$ Open Redirect
Debangshu Kundu
Follow
3 min read
·
Jul 1, 2024

525

1

Hi all! Long time indeed ☺

Today I’ll talk about an Open Redirect that got us paid 1k$.

Nothing too complicated about the finding, just the right program ;)

Was invited to this SAAS program with great payouts for P3s and P4s too!

Press enter or click to view image in full size
Reward Range for the program

But firstly…

Why Open Redirects?

Open redirects enable an attacker to manipulate a user by redirecting them to a malicious site. A GET-based open redirect was identified which can impact users' ability to trust legitimate web pages. An attacker can send a phishing email that contains a link with a legitimate business name in the URL and the user will be redirected from the legitimate web server to any external domain. Users are less likely to notice subsequent redirects to different domains when an authentic URL with a valid SSL certificate can be used within the phishing link.

This type of attack is also a precursor for more serious vulnerabilities such as Cross-Site Scripting (XSS), Server-Side Request Forgery (SSRF), Cross-Site Request Forgery (CSRF), or successful phishing attempts where an attacker can harvest users' credentials or gain users' OAuth access by relaying them through an Open Redirection, to a server they control (and can see the inbound requests from).

The Vulnerability
Press enter or click to view image in full size

For confidentiality purposes, I can’t use specific folder names or client information, but I’ll try my best to explain!

Consider this :-

domain.com/abc/xyz/zyc/html/redirect.html

This accepts a `url=` parameter in Base64 encoded form.

Upon browsing to `redirect.html` we find this code :-

Press enter or click to view image in full size
Code of redirect.html

It first waits for an event to happen. Then, it retrieves the input url from the `url=` parameter and base64decodes it.

Get Debangshu Kundu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, it checks the input URL against a specified allowlist of certain domains, google.com, abc.com, etc. and if it matches the allowlist, it waits for 3 seconds (3000 mills) and redirects the user to the allowe domain. If not, it does nothing.

Here comes the fault :-

The regex is checking if the URL contains any of the listed domains. While this approach is straightforward, it can indeed lead to potential issues, including open redirects, because:

Partial Matches:

- The regex will match any URL that contains the specified domains as a substring. For instance, `malicious.com/google.com` or `phishing-abc.com` will also match.
- This partial matching can be exploited by attackers to craft malicious URLs that still pass the check.

And that’s exactly what we did!

We came up with the following payload :-

https://domain.com/abc/xyz/zyc/html/redirect.html?url=<BASE64>https://evil.com#foobar</BASE64>

Resulting in :-

https://domain.com/abc/xyz/zyc/html/redirect.html?url=aHR0cHM6Ly9ldmlsLmNvbSNmb29iYXI=

The faulty regex allowed us to pass #foobar in the URL fragment, hence, bypassing the checks and arming us with a sweet open redirect ;)

There were multiple bypasses for the protection applied by the developers, stated below, but not limited to :-

target.evil.com

evil.com?param=target

evil.com/target

This is because the script only matches the domain (target) name in the redirection, we can place it anywhere. They do not validate the TLDs, only the ‘target’, not even ‘target.com’.

Also, earning as a sweet bounty in the process!

Press enter or click to view image in full size

This bug was in collaboration with 
Aditya Sharma

(He was the mastermind, I just wrote the blog xD)

Follow us at :- https://x.com/Assass1nmarcos & https://x.com/ThisIsDK999
