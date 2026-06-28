---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-03-17_near-universal-xss-in-mcafee-web-gateway.md
original_filename: 2017-03-17_near-universal-xss-in-mcafee-web-gateway.md
title: Near universal XSS in McAfee Web Gateway
category: documents
detected_topics:
- xss
- command-injection
- cors
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- cors
- api-security
- supply-chain
language: en
raw_sha256: 5c2a9bf8154138942b6aa5596b1760ce813d907c878db71b60ec09dc54d281ba
text_sha256: 5799148eb5742e39af3f4562820f68002a5f8aa131872d7c7bd01e493e349484
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Near universal XSS in McAfee Web Gateway

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-03-17_near-universal-xss-in-mcafee-web-gateway.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `5c2a9bf8154138942b6aa5596b1760ce813d907c878db71b60ec09dc54d281ba`
- Text SHA256: `5799148eb5742e39af3f4562820f68002a5f8aa131872d7c7bd01e493e349484`


## Content

---
title: "Near universal XSS in McAfee Web Gateway"
url: "https://blog.ettic.ca/near-universal-xss-in-mcafee-web-gateway-cf8dfcbc8fc3"
authors: ["Olivier Arteau"]
programs: ["McAfee"]
bugs: ["XSS"]
publication_date: "2017-03-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6206
scraped_via: "browseros"
---

# Near universal XSS in McAfee Web Gateway

Near universal XSS in McAfee Web Gateway
Olivier Arteau
Follow
4 min read
·
Mar 17, 2017

11

In this blog post, a vulnerability in the McAfee Web Gateway will be presented. The vulnerability was disclosed on September 15th 2016 to McAfee and was fixed on October 12th 2016 with the release of Web Gateway 7.6.2.5. XSS are a common vulnerability in web application, but the one presented here is of a very different nature from the ones we typically see. But first let’s look at how the product works at a high level. McAfee Web Gateway is essentially an enterprise proxy server that will filter the content based on rules. It allows company to control what people can visit when they are within the company network. To properly work, the McAfee Web Gateway also generates a root certificate that can be installed on the devices of the company. This allows the proxy to change the response of HTTPS traffic to something else. The main use case of this traffic alteration is to display custom HTTP error when a domain is blocked or doesn’t exist. When it happens, a page like the one below is returned to the user.

Press enter or click to view image in full size

Image Source : https://kc.mcafee.com/library/MCAFEE/CORPORATE_USER/CORP_TS_AGENT/Webwasher/KB69994_f.png

What initially got me interested about this page was that the entire requested URL was visible in the response. Looking at the HTML of the page, we could see the following HTML.

<!-- Info -->
<table class=”infoTable”>
<tr>
<td class="infoData">
<b>URL : </b><script type="text/javascript">break_line("http://digg.com");</script><br />
</td>
</tr>
</table>
<!-- /Info -->

The break_line JavaScript function had, at the time, the following definition. It essentially inserts a “<wbr />” tag every 20 characters and outputs the content directly in the page.

function break_line(lineToBreak) {
 if (lineToBreak != '') {
  var len = lineToBreak.length;
  var splitStr = '<wbr />';
  for (var i = 0; i < len;) {
  lineToBreak = lineToBreak.substring(0, i) + splitStr + lineToBreak.substring(i);
  i += 20 + splitStr.length;
  len += splitStr.length;
  }
  document.write(lineToBreak);
 }
}

The next question I asked myself was which encoding did it applied to the reflected URL ? With minimal fuzzing, I found that it takes the received URL and does an HTML encoding for the key HTML character (<, > and “). But is it the correct way to encode it ?

To explore this question we first have to look at the context in which it’s reflected. The reflected URL passes in two contexts. The first one being a JavaScript string and then in an HTML context (the break_line function). The correct way to encode content is to apply a context specify encoding for each context that it will be passed to from the last context to the first one. In this case, it means doing an HTML encoding and then a JavaScript encoding (result = javascript_encode(html_encode(data))). If we come back a bit we know that it’s only doing an HTML encoding, which means that the JavaScript encoding is missing.

Get Olivier Arteau’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

One of the interesting things that can be done when one of the context specific encoding is missing is to use alternate character encoding. In HTML “a” can also be written as “&#97;” and in JavaScript “a” can also be written as “\x61” and “\u0061”. Since the HTML encoding won’t encode the “\” character, we can rewrite character that would normally be encoded by the HTML encoding using an alternate JavaScript encoding (“<” changed to “\x3c”). This basically allows us to output any character and bypass the HTML encoding.

But the journey towards a fully functional proof of concept doesn’t stop here. If we remember previously, the JavaScript function break_line inserts a <wbr /> every 20 characters and this will get in the way of a standard XSS payload. So we need a way to write longer payload or bootstrap them. The easiest way that I found to deal with this limitation is to start each 20 characters segment with a */ and end it with a /*. This places the <wbr /> tag in JavaScript comment. This leaves us with 16 characters per segment. One of the solution that I found, was to use this as the first segment

\x3cscript\x3e/*AAAAAAAAAA*/a=String;b=/*AAAAA*/a.fromCharCode(/*A*/

Use this as the last segment.

*/);eval(b);/*AAAAAA*/\x3c/script\x3e

Use the other segments to provide the ASCII value for each character of our JavaScript payload. With this, I was able to make a first functional proof of concept.

http://aaaa.perdu.com/favicon.ico?AAAAAA\x3cscript\x3e/*AAAAAAAAAA*/a=String;b=/*AAAAA*/a.fromCharCode(/*A*/97,108,101,114,/*A*/116,40,119,105,/*A*/110,100,111,119,/**/46,108,111,99,/*AA*/97,116,105,111,/*A*/110,41/*AAAAAAAAAA*/);eval(b);/*AAAAAA*/\x3c/script\x3e

Do note that for longer payload, using an intermediate payload along the lines of eval(unescape(location.hash.substr(1))) and placing the full JavaScript payload after the “#” in the URL is a lot more practical.

So we can now execute any arbitrary JavaScript with our XSS, but for it to be useful we have to understand how to trigger those error pages. The most reliable way to trigger it is by visiting an URL where the domain doesn’t resolve to anything. Most domain name don’t catch all subdomains which means that you can get for most domain an XSS on doesnotexists.maindomain.com. While this doesn’t give you a direct access to other subdomains or the main domain, the browser gives special privilege to subdomain like setting cookies for *.maindomain.com. Also, since any request will be performed from a subdomain of maindomain.com, if the server trust its subdomains for CORS request, it can also lead to data stealing. Another way to trigger the error page for arbitrary domain is when the proxy is flooded and can no longer respond to request. This is in practice hard to obtain reliably, but will allow an XSS to be obtained on any domain. The XSS payload simply has to wait for the flood to end and then make any request with XHR.

There are probably other ways to trigger those error pages, but I don’t know the product well enough and the proof of concept was already interesting enough to warrant a fix.
