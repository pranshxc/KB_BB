---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-23_dom-xss-in-google-vrview-library.md
original_filename: 2018-04-23_dom-xss-in-google-vrview-library.md
title: DOM XSS in Google VRView library
category: documents
detected_topics:
- xss
- mobile-security
- command-injection
- mfa
- automation-abuse
- supply-chain
tags:
- imported
- documents
- xss
- mobile-security
- command-injection
- mfa
- automation-abuse
- supply-chain
language: en
raw_sha256: b5bad748ce1c64666fd7cbc8aca4276e78307cb66b09e9a39c486098299c606d
text_sha256: 3009698e24e5dc1a9a11d53a6b5c6005b32875d0a7306f62a9607164fb8fac84
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# DOM XSS in Google VRView library

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-23_dom-xss-in-google-vrview-library.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, command-injection, mfa, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `b5bad748ce1c64666fd7cbc8aca4276e78307cb66b09e9a39c486098299c606d`
- Text SHA256: `3009698e24e5dc1a9a11d53a6b5c6005b32875d0a7306f62a9607164fb8fac84`


## Content

---
title: "DOM XSS in Google VRView library"
page_title: "IMQ Minded Security Blog: DOM XSS in Google VRView library"
url: "http://blog.mindedsecurity.com/2018/04/dom-based-cross-site-scripting-in.html"
final_url: "https://blog.mindedsecurity.com/2018/04/dom-based-cross-site-scripting-in.html"
authors: ["Federico Fazzi (@federicofazzi)"]
programs: ["Google"]
bugs: ["DOM XSS"]
bounty: "3,133.7"
publication_date: "2018-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5902
---

While testing the **VRView** web application we discovered a **DOM Based Cross-Site Scripting Vulnerability** in the handling of errors through an inappropriate use of the "**innerHTML** " **property**. The use of this property must be combined with the **encoding** of the **data** before it is used for data assignment, and in this case it wasn't used safely.  
  
Since the vulnerability also affects two of the most used **Wordpress vrview plugins** , an attacker could take control of the remote system that uses these plugins through a code analysis, or through automated tools.  
  
Depending on the type of vulnerability and the role of the vulnerable component within the system, it can lead to trivial effects on the complete ownership of the server and the compromise of any data contained in it. The aspect to always keep in mind is that for the execution of the external components the principle of the minimum privilege is almost never applied.  
  
  

###  About VRView

  
Vrview is a library developed by Google for embedding immersive media into traditional websites.  
  
As described on the main website: <https://developers.google.com/vr/concepts/vrview>  
  
_VR view allows you to embed 360 degree VR media into websites on desktop and mobile, and native apps on Android and iOS. This technology is designed to enable developers of traditional apps to enhance the apps with immersive content. For example, VR view makes it easy for a travel app to provide viewers with an underwater scuba diving tour as they plan a vacation or for a home builder to take prospective buyers on a virtual walk-through before the home is built._  
  
  

###  The Vulnerability

  
The vulnerability lies in the management of library errors, in fact, if it is specified through URL parameters: _**url**_ or _**image**_ , a nonexistent resource, the library returns an error including in the error message the resource specified in the request without executing the output encoding .  
  
  
  
As can be seen from the code below, the user input data passed through the GET request parameters is passed to the "innerHTML" property without performing the parameter encoding output. In this way, an attacker can specify an XSS payload instead of the requested resource, the library will interpret the resource as non-existent and respond with an error indicating the XSS payload entered by the attacker, thus generating an arbitrary code execution Javascript.  
  
The following shows the vulnerable code in the VRView library:  
  
**URL:** <https://github.com/googlevr/vrview/blob/master/src/embed/main.js>  
  
/* [...] */  

  
  
  function onSceneError(message) {
  showError('Loader: ' + message);
  }
  
  function onRenderError(message) {
  showError('Render: ' + message);
  }
  
  /* [...] */
  
  function showError(message, opt_title) {
  // Hide loading indicator.
  loadIndicator.hide();
  
  var error = document.querySelector('#error');
  error.classList.add('visible');
  error.querySelector('.message').innerHTML = message;
  
  var **title** = (opt_title !== undefined ? opt_title : 'Error');
  error.querySelector('.title').innerHTML = title;
  }
  
  /* [...] */
  

  
  

###  Proof of Concept

  
The links below shows the vulnerability in real world example, the vulnerability includes other sub/domains that have not been mentioned such as "[storage.googleapis.com](http://storage.googleapis.com/)".  
  
**URL:** <https://vr.google.com/earth/vrview/?url=%3Cimg%20src=x%20onerror=alert(document.domain)%3E>

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgv14EpBY5duxMsDCFj2cBIUnOavVSlVJaUmowDXVGVqFC-laBh_8ckhNugUTiPh1b4enQhIWcSEgHxhJlY_CcU4Rxtgjl_5LR4sLVUnAdbQCA73xOzCr48vYPjNg1mv8andIRCkv9Xm5CZL8zNzEwhWnJ-7N7EahGD30G5KwybqpVuLkPfTviolpTdHA/w640-h350/vr-google-com-xss_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgv14EpBY5duxMsDCFj2cBIUnOavVSlVJaUmowDXVGVqFC-laBh_8ckhNugUTiPh1b4enQhIWcSEgHxhJlY_CcU4Rxtgjl_5LR4sLVUnAdbQCA73xOzCr48vYPjNg1mv8andIRCkv9Xm5CZL8zNzEwhWnJ-7N7EahGD30G5KwybqpVuLkPfTviolpTdHA/s640/vr-google-com-xss_1.png)

  

  
  

  

  
  
**URL:** <http://googlevr.github.io/vrview/index.html?image=%3Cimg%20src=x%20onerror=alert(document.domain)%3E>  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIgjq0Or5zVGB1l0v4Di4axODIVJauh8u0Ra8s3ZEvPYEjee77LIcwNV8VU0VO8rbETbet3Fu1YR-Lfb4FtJFDFElu4bNO9M-4GkJc8WHlhBISCPzZYI2LNEwTRmFa9veMUluhO2Zl9plj8QGC3dOAArh0Dl4j487YYj54V-EIB5ad7OgfW-CnQGKy8w/w640-h350/googlevr-github-io-xss_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIgjq0Or5zVGB1l0v4Di4axODIVJauh8u0Ra8s3ZEvPYEjee77LIcwNV8VU0VO8rbETbet3Fu1YR-Lfb4FtJFDFElu4bNO9M-4GkJc8WHlhBISCPzZYI2LNEwTRmFa9veMUluhO2Zl9plj8QGC3dOAArh0Dl4j487YYj54V-EIB5ad7OgfW-CnQGKy8w/s640/googlevr-github-io-xss_2.png)

  

  

  

Please note that the links above contains a patched version of the library.  
  
  

###  Vulnerable Wordpress Plugins

  
Following are the two vulnerable Wordpress plugins found during the vulnerability analysis.  
  
**1) WP-VR-view -**<https://it.wordpress.org/plugins/wp-vr-view/>  
  
_WP-VR-view is a plugin that allows you to display Photo Sphere images and 360 video on wordpress pages, posts, etc._  
_Website visitors will be able to navigate through your panoramas._  
_Smartphone users can use Google cardboard to look through in Virtual reality way._  
  
**Proof of Concept:**  
`http://example.org/wordpress/wp-content/plugins/wp-vr-view/asset/?image=<img%20src=x%20onerror=alert(document.domain)>`  
  
**  
****2) VRView -** <https://it.wordpress.org/plugins/vrview/>  
  
_VRView makes it easy to embedd Googles VRView into your WordPress installation._  
_Embed 360° Videos and VR Videos as Well as panorama photos into your WordPress-Installation._  
  
**Proof of Concept:**  
`http://example.org/wordpress/wp-content/plugins/vrview/vrview/?image=<img%20src=x%20onerror=alert(document.domain)>`  

  
  
Please refer to section **A9** of the **OWASP Top 10** to check if the application makes use of external components, libraries, frameworks and dependencies from modules that are affected by known vulnerabilities:  
  
**A9 - Using Components with Known Vulnerabilities**  
<https://www.owasp.org/index.php/Top_10_2017-A9-Using_Components_with_Known_Vulnerabilities>  
  
  

###  Disclosure Timeline

  

  * **19-01-2017** – Report to Google Security Team;
  * **20-01-2017** – Received a first feedback said that the report was triaged;
  * **20-01-2017** – Received a second feedback said that the vulnerability exists;
  * **14-02-2017** – Reply from Google Security Bot - The panel has decided to issue a reward of $3133,7;
  * **16-03-2018** – The vulnerability was fixed (<https://github.com/googlevr/vrview/pull/308>);
  * **23-04-2018** – Public disclosure.

  

###  Acknowledgement

  
**Google VRP** panel has decided to reward with a high reward as the vulnerability is included not only in sandboxed domains but also [google.com](//google.com/).  
Vulnerability Found and Reported by Federico Fazzi.
