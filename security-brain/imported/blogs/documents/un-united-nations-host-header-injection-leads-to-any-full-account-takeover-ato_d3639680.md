---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-13_un-united-nations-host-header-injection-leads-to-any-full-account-takeover-ato.md
original_filename: 2022-08-13_un-united-nations-host-header-injection-leads-to-any-full-account-takeover-ato.md
title: UN United Nations Host Header Injection leads to any Full Account Takeover
  (ATO)
category: documents
detected_topics:
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- command-injection
- password-reset
- otp
language: en
raw_sha256: d36396808ba0be319fe7d0aa3dc82f5b0c03103a918f0f5ba8605d7cdda1c2e6
text_sha256: acd827149f113f6eb14817559648603f67d5e9b57704eb8a9da9c652acf8fc93
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# UN United Nations Host Header Injection leads to any Full Account Takeover (ATO)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-13_un-united-nations-host-header-injection-leads-to-any-full-account-takeover-ato.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `d36396808ba0be319fe7d0aa3dc82f5b0c03103a918f0f5ba8605d7cdda1c2e6`
- Text SHA256: `acd827149f113f6eb14817559648603f67d5e9b57704eb8a9da9c652acf8fc93`


## Content

---
title: "UN United Nations Host Header Injection leads to any Full Account Takeover (ATO)"
url: "https://medium.com/@Bishoo97x/un-united-nations-host-header-injection-leads-to-any-full-account-takeover-ato-795bc9ebc670"
authors: ["Ahmed Hassan"]
programs: ["United Nations"]
bugs: ["Host header injection", "Password reset", "Account takeover"]
publication_date: "2022-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2322
scraped_via: "browseros"
---

# UN United Nations Host Header Injection leads to any Full Account Takeover (ATO)

UN United Nations Host Header Injection leads to any Full Account Takeover (ATO)
Ahmed Hassan (Bishoo97x)
Follow
3 min read
·
Aug 14, 2022

150

1

Hey all. I hope you are all safe and good. I am happy to publish another new Writeup about an Host Header Injection Vulnerability found in UN United Nations Web Application which leads to Full Accout Takeover of any Account or User on this Plattform.

Without wasting time, let us begin immediately.

So after enumerating and finding most possible Subdomains, I focused on one specific Subdomain where i can register a User called for example target.com. I actually registered a Test-User and tried to find some low-hanging fruits Vulnerabilities, but I did not find anything.

After that, I thought about the Password Reset Functionality. Going through many Vulnerabilities, I come through testing an Host Header Injection Vulnerability.

Quick Explanation of the Bug: Host Header Injection Vulnerabilities allows any Attacker to manipulate the Host Header generating the Password Reset link, so the attacker can receive any Token or Link for resetting the Password and therefore take over the whole Account.

And this is exactly what I have tested, and it actually worked.

Press enter or click to view image in full size

So here you can see when I requested a Password Reset I got redirected to the UN Website where the Website generates a Password Reset Link with a Token.

Get Ahmed Hassan (Bishoo97x)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What if we manipulate the Host Header to evil.com for example and see if the Web Application will generate the Reset Link with our controlled Domain?
And actually it did this exactly.

Press enter or click to view image in full size

Here I was able to change the Host Header to evil.com and the Web Application accepted it and generated a Reset Link with this Domain.

Through this Misconfiguration I would be able to put in a Burp Collaborator Link send this Link to any User and receive the Clear text Reset Login Credentials and take over the whole Account of any User on this Plattform.

Any Account could be hacked through this Vulnerability including any Admin Account.

At the End I hope you enjoyed my Write-up and learned something new, if yes please do not forget to subscribe my Medium, give me a like and follow me on all my Social Media Account too :).

My Website for offering different Security Services: https://titaniumcybersolutions.com/

LinkedIn: https://www.linkedin.com/in/ahmed-hassan-79559487/
YouTube: https://www.youtube.com/channel/UCnbL312SHoFczdheav2TRJQ
Medium: https://medium.com/@Bishoo97x
Facebook: https://www.facebook.com/ahmedhamada81

Happy to see you reading my Write-ups and see you soon in my next Write-up.
