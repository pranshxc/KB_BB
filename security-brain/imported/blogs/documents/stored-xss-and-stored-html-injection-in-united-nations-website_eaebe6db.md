---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-08_stored-xss-and-stored-html-injection-in-united-nations-website_2.md
original_filename: 2022-07-08_stored-xss-and-stored-html-injection-in-united-nations-website_2.md
title: stored XSS and stored HTML Injection in United Nations Website
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
raw_sha256: eaebe6dbf14dffe0a6d96256ca9e9c64e06dd3a3062aa1407740752a787b0f32
text_sha256: 966b3c86a5f43dc9dcfb99c83a6b30aed8acfc8acc9f5604efd138dedd2295fd
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# stored XSS and stored HTML Injection in United Nations Website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-08_stored-xss-and-stored-html-injection-in-united-nations-website_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `eaebe6dbf14dffe0a6d96256ca9e9c64e06dd3a3062aa1407740752a787b0f32`
- Text SHA256: `966b3c86a5f43dc9dcfb99c83a6b30aed8acfc8acc9f5604efd138dedd2295fd`


## Content

---
title: "stored XSS and stored HTML Injection in United Nations Website"
url: "https://medium.com/@Bishoo97x/stored-xss-and-stored-html-injection-in-united-nations-website-db87d445e41"
authors: ["Ahmed Hassan"]
programs: ["United Nations"]
bugs: ["XSS", "HTML injection"]
publication_date: "2022-07-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2476
scraped_via: "browseros"
---

# stored XSS and stored HTML Injection in United Nations Website

stored XSS and stored HTML Injection in United Nations Website
Ahmed Hassan (Bishoo97x)
Follow
3 min read
·
Jul 9, 2022

74

1

Hello all i am very happy to publish another Writeup after a long time of missing.

So while hunting on a specific United Nations Subdomain i was able to identify several stored XSS and stored HTML Injection Vulnerabities.

Press enter or click to view image in full size
United Nations (UN)

So lets us go through the Recon and Exploitation Process :)

Press enter or click to view image in full size
Photo by Arget on Unsplash

After getting through the Registration Process i was testing different changing Parameters like Firstname, Lastname. Through submitting a simple XSS Payload <script>alert(‘XSS’)</script> i was surprised that multiple XSS Popups were fired. At the same Time i tested an HTML Injection Vulnerability through putting a simple HTML Code redirecting to the OWASP Site <A HREF=”https://owasp.org">Clickhere </A>.

Press enter or click to view image in full size

After saving and reloading the Webpage i was surprised from the amount of XSS Alert Pop-ups :).

Press enter or click to view image in full size
Cross Site-Scripting Pop-up after saving and refreshing the Website

It was a really good Achievement but after this step i wondered where i can find the HTML Code Input did it run properly ?

So while inspecting the Website in depth i saw that the Output is showing a different Colour and redirecting the User to the owasp.org Homepage.

Get Ahmed Hassan (Bishoo97x)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Maybe it is not clear enough but here you can see the word CL which is in blue and if you hover or click on it you will be redirected to any Website you put in and in this case to owasp.org

HTM Injection redirecting to a any malicious Website

That was a really good Indication for a reflected XSS and HTML Injection but i just moved a step further.

I logged myself out and tried to login again to see if we have a stored XSS and HTML Injection in case all the Payloads run automatically again without any Interaction from the Attacker.

And in fact all the Payloads run automatically and without any Interaction from the Attacker and through this i was able to find multiple stored XSS and HTML Injection Vulnerabilities on a Subdomain of the United Nations.

At the End i submitted these Vulnerabilities to the United Nations Security Team and they already accepted all of them and are working now on the Fix.

Press enter or click to view image in full size
United Nations accepts all the submitted Vulnerabilities and waiting for the Add on their Hall of Fame

Finally i want to thank you for taking time and going through my Writeup just follow me here and on LinkedIn for more Writeups there are a lot more coming hope you enjoyed and see you next time stay safe. :)

LinkedIn Profiel: https://www.linkedin.com/in/ahmed-hassan-79559487/
