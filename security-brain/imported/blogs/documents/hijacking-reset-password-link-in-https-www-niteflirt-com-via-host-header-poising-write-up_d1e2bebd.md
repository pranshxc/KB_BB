---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-25_hijacking-reset-password-link-in-httpswwwniteflirtcom-via-host-header-poising-wr.md
original_filename: 2021-02-25_hijacking-reset-password-link-in-httpswwwniteflirtcom-via-host-header-poising-wr.md
title: Hijacking Reset Password Link in https://www.niteflirt.com/ via Host Header
  Poising (Write Up)
category: documents
detected_topics:
- command-injection
- password-reset
tags:
- imported
- documents
- command-injection
- password-reset
language: en
raw_sha256: d1e2bebdddd2d725b8a56da36555c02df9fa149857d727463ee63e497e57170f
text_sha256: 58716ecfff579905217dbafd289d56f0054a7133a91655ad33a011841de95716
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking Reset Password Link in https://www.niteflirt.com/ via Host Header Poising (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-25_hijacking-reset-password-link-in-httpswwwniteflirtcom-via-host-header-poising-wr.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `d1e2bebdddd2d725b8a56da36555c02df9fa149857d727463ee63e497e57170f`
- Text SHA256: `58716ecfff579905217dbafd289d56f0054a7133a91655ad33a011841de95716`


## Content

---
title: "Hijacking Reset Password Link in https://www.niteflirt.com/ via Host Header Poising (Write Up)"
page_title: "Evan Ricafort | Blog: Hijacking Reset Password Link in https://www.niteflirt.com/ via Host Header Poisoning (Write Up)"
url: "https://blog.evanricafort.com/2021/02/hijacking-reset-password-link-in.html"
final_url: "https://blog.evanricafort.com/2021/02/hijacking-reset-password-link-in.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Niteflirt"]
bugs: ["Host header injection", "Account takeover", "Password reset"]
bounty: "50"
publication_date: "2021-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3870
---

Howdy!

  

Summer last year while playing with google dorks I found a random external bug bounty program which is an adult website that allow user to interact each other through chat. The app is similar to tinder.

Since they have a bug bounty program, I tried doing a recon with their domain. fired up my recon tools to gather subdomains, directories and etc... 

So while my recon tools are doing their things, I started up testing the login and reset password page after I signed up for an account and found a simple bug on the reset password.

Long story short, I found a Host Header Hijacking/Poising issue in niteflirt.com which allow me to manipulate the host header during the reset password procedure. The issue allow me to change the reset password link after changing the value of the Host.

  

**_\--Proof of Concept--_**

**_  
_**

****

****

**  
_  
_**

Result:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDCvJC1qkjEz5xmYxmzir_PP7YuPP86nWaScqMDFrpwMcKwFZ3lFDf0KJ9Qm_Xs_JQVzTPHSMloTvF9DRXIM7bU2H_jJpv1HRlyNwW8rXhrdYM-o-B0JPPzXfd2gHCAhl3FXZterYm/w640-h197/Screenshot_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDCvJC1qkjEz5xmYxmzir_PP7YuPP86nWaScqMDFrpwMcKwFZ3lFDf0KJ9Qm_Xs_JQVzTPHSMloTvF9DRXIM7bU2H_jJpv1HRlyNwW8rXhrdYM-o-B0JPPzXfd2gHCAhl3FXZterYm/s752/Screenshot_1.png)

  

  

**_\--Timeline--_**

**_  
_**

Title: Vulnerability Issue (Host Header Hijacking)

Reported: Jul 11, 2020, 3:31 AM

Rewarded: Jul 16, 2020, 5:25 AM (**$50**)

  

__

> _Hi Evan,_
> 
> _  
> _
> 
> _Thanks for your submission with a very clear PoC._
> 
> _  
> _
> 
> _  
> _
> 
> _While we do already have some development in the works to address this known issue, we appreciate this demonstration of a new way to exploit this issue and would like to offer you a $50 reward. Would you mind re-confirming that your paypal email is still <redacted>@gmail.com _
> 
>  _  
> _
> 
> _\---_
> 
> _  
> _
> 
> _  
> _
> 
> _Best regards,_
> 
> _  
> _
> 
> _Bug Bounty_

  

Reference of this issue: [https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html](https://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html) (Cheers to James Kettle [@albinowax](https://twitter.com/albinowax))

  

I hope you enjoy this write up. Stay safe and have a great day y'all!

  

_**“Only those who dare to fail greatly can ever achieve greatly.”**_

 _― Robert F. Kennedy_

  

  

 __
