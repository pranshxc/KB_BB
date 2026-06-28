---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-17_dom-based-xss-for-fun-and-profit-bug-bounty-poc.md
original_filename: 2023-01-17_dom-based-xss-for-fun-and-profit-bug-bounty-poc.md
title: DOM-Based XSS for fun and profit $$$! | Bug Bounty POC
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 678b435302636b428a19797c08fe90148900be172cb751961931ed743938fc65
text_sha256: 9d01eb3892ec081a2b62c568429a0f89733e3c273e6f2f06a5b07245dbf854d4
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# DOM-Based XSS for fun and profit $$$! | Bug Bounty POC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-17_dom-based-xss-for-fun-and-profit-bug-bounty-poc.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `678b435302636b428a19797c08fe90148900be172cb751961931ed743938fc65`
- Text SHA256: `9d01eb3892ec081a2b62c568429a0f89733e3c273e6f2f06a5b07245dbf854d4`


## Content

---
title: "DOM-Based XSS for fun and profit $$$! | Bug Bounty POC"
url: "https://medium.com/@haroonhameed_76621/dom-based-xss-for-fun-and-profit-bug-bounty-poc-f4b9554e95d"
authors: ["Haroon Hameed (@HaroonHameed40)", "Hannan Haseeb (@HannanHaseeb11)"]
bugs: ["DOM XSS"]
publication_date: "2023-01-17"
added_date: "2023-01-18"
source: "pentester.land/writeups.json"
original_index: 1663
scraped_via: "browseros"
---

# DOM-Based XSS for fun and profit $$$! | Bug Bounty POC

DOM-Based XSS for fun and profit $$$! | Bug Bounty POC
Haroon Hameed
Follow
3 min read
·
Jan 18, 2023

301

2

Press enter or click to view image in full size

Hey everyone! This is Haroon Hameed and I’m here to share about our recent finding on Synack Red Team about DOM-based XSS. In this blog post, I’m going to discuss the Bug Bounty report of this discovery.

It was a QR-based target on Synack Red Team

Vulnerability Analysis:

Lets begin! Our main focus was on the main domain, which is https://redacted.com, so we won’t do any subdomain enumeration and starting looking for juicy JavaScript files and luckily we found two interesting JavaScript file, where we found the following JavaScript function:

function saveRegion(regionId, forceReload) {//Save selection
  customer_RegionId = regionId;

  $.ajax({
  type: 'POST',
  url: "/Unauthenticated/SaveRegion",
  data: {
  regionId: regionId
  },
  success: function (response) {
  setCookie('RegionId', regionId, 1);
  $('#select-region-modal').modal('hide');
  var url = getParameterByName('url');
  if (url != null && url != '') {
  createCookie('UAPathway', 'Start', 1);
  setTimeout(function () {
  window.open(url, '_self');
  }, 1000);

In the above code when an unauthenticated user click on Save Region it will send Ajax request (An Ajax request is an HTTP request that uses the XMLHttpRequest object to exchange data asynchronously with a web server. This allows for dynamic web page updates without the need for a full page reload.) with POST type on /Unauthenticated/SaveRegion endpoint(s) than this code will save the selected regionId (regionId is a parameter passed to the function) to a cookie, then reloads the page (or redirects to a specified URL). It then sets a cookie for the user’s pathway (UAPathway) with a value of “Start”.

The code above is vulnerable to DOM-Based XSS. If an attacker is able to inject malicious JavaScript into the “url” parameter, the resulting code will be executed on the page. The code uses the “getParameterByNam”e function to retrieve the value of the “url” parameter, which is then used in the “window.open” function.

Source:

function getParameterByName(name, url = window.location.href) {
  name = name.replace(/[\[\]]/g, '\\$&');
  var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
  results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

In this JavaScript code “getParameterByName()” function, which is used to retrieve parameters from the URL, allows the attacker to execute malicious code on the website by manipulating the “url” parameters.

window.open(url, '_self');

The following are some demonstration payloads which can be used to execute JavaScript commands and access DOM elements, such as document.domain and document.cookie:

Get Haroon Hameed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After understanding the JavaScript code you will clearly see that it will take user-supplied input from ‘url’ parameter and executing it in DOM aka sink.

So we used the following JavaScript payload:

javascript:alert(document.domain)

javascript:alert(document.cookie)
Press enter or click to view image in full size
JavaScript Payload Execution

Hence, We submitted the best quality report to Synack’s Quality Rule program on Synack Red Team and was awarded with 3/3 stars and a bounty of $$$.

Voila! “Sometimes, HACKING is Just someone spending more time on something than anyone else might reasonably expect” it’s always good to look into things that seem to be pointless.

Social Links:

Twitter (Haroon Hameed)

LinkedIN (Haroon Hameed)

We are open to work on any private pentesting projects. If you have any such projects, please feel free to DM any of us. Thank you!

If you like this write-up, Share!

Thank you!
