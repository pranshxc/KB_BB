---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-19_xss-using-dynamically-generated-js-file.md
original_filename: 2017-07-19_xss-using-dynamically-generated-js-file.md
title: Xss using dynamically generated js file
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
raw_sha256: 426efe450094be00232e48e48df59fc644f9e99488ce3ff24f1e5ad7832222d8
text_sha256: 58daabeb2ed264da7c83d4ff61c89d6acc36cad18c3a3df3091509b54eb3b973
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Xss using dynamically generated js file

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-19_xss-using-dynamically-generated-js-file.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `426efe450094be00232e48e48df59fc644f9e99488ce3ff24f1e5ad7832222d8`
- Text SHA256: `58daabeb2ed264da7c83d4ff61c89d6acc36cad18c3a3df3091509b54eb3b973`


## Content

---
title: "Xss using dynamically generated js file"
url: "https://medium.com/@arbazhussain/xss-using-dynamically-generated-js-file-a7a10d05ff08"
authors: ["Arbaz Hussain (@ArbazKiraak)"]
bugs: ["XSS"]
bounty: "150"
publication_date: "2017-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6150
scraped_via: "browseros"
---

# Xss using dynamically generated js file

Xss using dynamically generated js file
Arbaz Hussain
Follow
2 min read
·
Jul 19, 2017

178

Severity : High

Complexity: Medium

Weakness: Disclosing JS endpoint & not sanitizing User Input

— — — — — — — — — — — — — — — — — — — — — — — — — — — —

Discovery :

While checking Burp Proxy Request’s I came across following JavaScript file.

https://www.site.com/mvcs/kt/tags/pclntny.js

I started brute-forcing for any parameter for JS endpoint and found ?cb=
Which Take’s the user input and append it to getScript Calling Function Since the Content type is text/plain. So we Need to Find a Way to Render our Input .

https://www.site.com/mvcs/kt/tags/pclntny.js?cb=xxxxxxxxx

Press enter or click to view image in full size
We know that JS file’s doesn’t care about SOP & can be access by making cross domain request’s , Luckily there was no X-Content-Sniffing Header aswell .

Now the Task was to Find Where , https://www.site.com/mvcs/kt/tags/pclntny.js js file is being rendered in HTML/Javascript under https://www.site.com/

I Used Burp Proxy Search Filter option to look for that endpoint .
Press enter or click to view image in full size

Found that it is used in https://www.site.com/user/public/apps/tags?val=pcltny.js

<script type="text/javascript" src="/mvcs/kt/tags/pclntny.js" />.
.
.
.
.
  var Doc = uri.queryKey['cb'];

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

Get Arbaz Hussain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Exploitation :

Simple POC :
<html>
<body>
<script src="https://www.site.com/mvcs/kt/tags/pclntny.js?cb=xxxx')<PAYLOAD-HERE>;">
...
window.open(https://www.site.com/user/public/apps/tags?val=pcltny.js, '_blank').focus();
</script>
</body>
</html>

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — -

Able to Bypass their Cross domain Policy by injecting AJAX Request’s

Tools: https://github.com/maK-/parameth For checking Parameter’s .

Reference :

https://www.hurricanelabs.com/blog/new-xssi-vector-untold-merits-of-nosniff
https://www.scip.ch/en/?labs.20160414
http://google-gruyere.appspot.com/part3#3__cross_site_script_inclusion
Nice and Little Bounty!
