---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-12_clickjacking-dom-xss-on-googleorg.md
original_filename: 2019-08-12_clickjacking-dom-xss-on-googleorg.md
title: Clickjacking DOM XSS on Google.org
category: documents
detected_topics:
- xss
- clickjacking
- command-injection
- api-security
tags:
- imported
- documents
- xss
- clickjacking
- command-injection
- api-security
language: en
raw_sha256: 2d0d557ad479650d0053257fa992ca2f7b536c26a83b2a04f4f82cd9efdcc1a5
text_sha256: c48709eed6ed8e1e46d576c28b1616e7e05263cc0c06ef99f02bfc4dfcd81402
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Clickjacking DOM XSS on Google.org

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-12_clickjacking-dom-xss-on-googleorg.md
- Source Type: markdown
- Detected Topics: xss, clickjacking, command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2d0d557ad479650d0053257fa992ca2f7b536c26a83b2a04f4f82cd9efdcc1a5`
- Text SHA256: `c48709eed6ed8e1e46d576c28b1616e7e05263cc0c06ef99f02bfc4dfcd81402`


## Content

---
title: "Clickjacking DOM XSS on Google.org"
page_title: "Clickjacking DOM XSS on Google.org - Web Security Blog"
url: "https://websecblog.com/vulns/clickjacking-xss-on-google-org/"
final_url: "https://websecblog.com/vulns/clickjacking-xss-on-google-org/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["Clickjacking", "DOM XSS"]
publication_date: "2019-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5087
---

# Clickjacking DOM XSS on Google.org

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[August 12, 2019June 10, 2022](https://websecblog.com/vulns/clickjacking-xss-on-google-org/)

One of the lesser-known Google projects is [Google Crisis Map](https://google.org/crisismap).  
It was created _to help people find and use critical emergency information._ [_[source]_](https://support.google.com/crisismaps/)

Although it is still working, it doesn’t seem to be used much anymore.

Since it’s an older project (created in 2012) and not updated often, it’s a great target to look for vulnerabilities.

It’s hosted on the google.org domain, which doesn’t have as big a severity as google.com (for client-side vulnerabilities), but it’s still a domain owned by Google.

## Logging in

If you go to the project’s home page ([google.org/crisismap](https://google.org/crisismap)), you’ll get redirected to the default map “Weather and Events”. This isn’t very interesting for us since the only thing we can do is view the map.

![Google Crisis Map](https://websecblog.com/wp-content/uploads/image-10-1024x510.png)

There is a way to manage and create new maps. It can be accessed if we add `.maps` at the end of the URL: [google.org/crisismap/.maps](https://google.org/crisismap/.maps)

![google.org/crisismap/.maps](https://websecblog.com/wp-content/uploads/image-8.png)

Once you open this page, you’ll need to log in with your Google account to continue. Now you should see a dashboard with a list of maps. There are three default maps for every account.

![](https://websecblog.com/wp-content/uploads/image-11-1024x279.png)

For some reason, if you publish one of these maps on your own domain, everyone will see that in the dashboard under the “Published Map” field.

## Creating a map

If you click on the red “Create Map” button, you’ll most likely see a message that the _gmail.com_ domain can’t be used for creating new maps.

![Not permitted to create maps in gmail.com](https://websecblog.com/wp-content/uploads/image-13.png)

This means we need to log in using an email with our custom domain. We can do this either by logging in with a GSuite account or an email that uses a domain other than gmail.com. After that, we can create a new map.

![Acceptable use dialog](https://websecblog.com/wp-content/uploads/image-19.png)

After clicking the “Continue” button, we’ll get redirected to a page where we can edit the newly created map.

## Finding the XSS

First, we’ll add a new layer to the map.

![Google Map](https://websecblog.com/wp-content/uploads/image-18.png)

A dialog for creating a new layer will pop up.

We’ll enter anything as the “Title”.  
Now if we enter `javascript:alert(document.domain)` into the “Source URL” field, it’ll show an error:

> Invalid URL – please include a protocol (e.g. http:// or https://) 

![](https://websecblog.com/wp-content/uploads/image-20.png)

This means it checks if the URL is valid before it allows you to save the new layer. The deobfuscated JavaScript code that validates the URL looks like this:
  
  
  if (url && !url.toLowerCase().match("^\\s*(http://|https://|docs://|$)")) {
  showError("Invalid URL - please include a protocol (e.g. http:// or https://)");
  }

But this is only validation on the client-side before the actual save request is sent to the backend.

### Modifying the request

We can use a web debugging proxy like [Fiddler](https://appio.link/fiddler) or [Burp Suite](https://appio.link/burp) to modify the request and send the modified version instead.

First, we need to change the “Source URL” to a valid URL, e.g. `https://example.com`.

We’ll click the “OK” button and click “Save” to send the save request. Then we’ll modify the request. This is what the request looks like:
  
  
  POST https://google.org/crisismap/.api/maps/1234
  
  
  {
  "id": "1234",
  "title": "Untitled map",
  "base_map_type": "GOOGLE_ROADMAP",
  "layers": [{
  "id": "1",
  "title": "Test layer",
  "visibility": "DEFAULT_ON",
  "type": "KML",
  "source": {
  "kml": {
  "url": "https://example.com"
  }
  }
  }]
  }
  

We’ll replace `https://example.com` with `javascript:alert(document.domain)` and send this modified request.

## Testing the XSS

The request is now sent and saved, so we’ll reload the page.

Open “Layers” and click on “Download KML”.

![Google Crisis Map - Download KML](https://websecblog.com/wp-content/uploads/image-22.png)

After we click on the download link, the XSS is fired and the alert box pops up with the domain name!

![XSS alert popup](https://websecblog.com/wp-content/uploads/image-21.png)

### How to fix this

Why did this happen? The URL validation happened only on the frontend and not in the backend. That means this could be fixed by validating the URL in the backend as well.

But this is not the way Google decided to fix it. Instead of checking the URL when saving it in the backend, the URL is now validated before displaying in the DOM.

So if the URL isn’t valid, it won’t be used as the link. It’ll use a meaningless value like `about:invalid` instead.
  
  
  <a href="about:invalid#zClosurez">Download KML</a>

## The impact

Okay, so we have a link that points to a `javascript:` URI containing the payload. The link is on a page to manage the map. And you must log in and have permission to access the page.

Clearly, this is self-XSS since only we are able to get this XSS executed.

Now how do we get from self-XSS to a real XSS?

### Increasing the severity

Every map we create can be published to be viewed by the public. If you’re logged in via an email with the domain `example.com`, you can publish the map to the URL `https://google.org/crisismap/example.com/test`.

![List of maps with a Publish button clicked on the first map](https://websecblog.com/wp-content/uploads/image-24.png)

Anyone can open this URL and view the map we’ve created. To get the XSS working, the user would have to open or be navigated to this page, open the “Layers” view and then click the “Download KML” link.

This means it’d no longer be self-XSS, but it’s still too many steps the user would have to make for this XSS to be useful.

## Clickjacking

If we take a look at the response HTTP headers, we can see that google.org doesn’t send the `X-Frame-Options` header.

![Response headers from google.org ](https://websecblog.com/wp-content/uploads/image-35.png)Response headers from google.org 

![Response headers from google.com](https://websecblog.com/wp-content/uploads/image-33.png)Response headers from google.com

> The `X-Frame-Options` HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a `<frame>`, `**< iframe>**`, `<embed>` or `<object>`. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
> 
> — [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)

The (intentional) lack of this HTTP header on google.org means we can embed the published map into an `iframe` on our own website.
  
  
  <iframe src="https://google.org/crisismap/example.com/test"></iframe>

This is how it’ll look like. In order to fire the XSS the user now doesn’t have to even leave our website. But they’d still need to click on two places in the `iframe` (“ _Layers_ ” > “ _Download KML_ “).

![Google Crisis Map in an iframe](https://websecblog.com/wp-content/uploads/image-37.png)

The `iframe` is loaded on our website – that means we can use CSS and JavaScript to manipulate it.

The first thing that came to my mind was to put black DIVs around the point where we want the user to click. Then detect a click and move the DIV to the second point.

This worked well but it still requires the user to click on two different locations.

![Google.org clickjacking demonstration](https://websecblog.com/wp-content/uploads/google_org_vuln_gif.gif)

But a more efficient solution would be to position the `iframe` absolutely with CSS so the user doesn’t have to move the cursor at all.

Below ~~is~~ _was_ a live demo. _Unfortunately, Google Crisis Map has been discontinued so the live demo won’t work anymore. You can see how it looked like in the video_.

It scales the `iframe` 50× and moves it to the position we want the user to click. First to the “Layers” tab. After a click, it moves over the link with the payload.

It was possible to execute the XSS by clicking two times somewhere in the `iframe`. We could even overlay the iframe with an opaque div with `pointer-events` disabled, so the user would have no idea they are clicking in the iframe.

_For the sake of the sample and the fact that this vulnerability is already fixed, the link goes to_` _https://_`_and not_` _javascript:_`_URI._

## Conclusions

There are several things to be taken from here.

  1. Never trust user input. Always check (on the backend) if it’s valid before saving it. Make sure to properly sanitize it depending on the context it will be in.
  2. Don’t allow other domains to embed your website in an `iframe` by correctly setting the `[X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)` header.
  3. When looking for vulnerabilities, try to find the highest possible severity of the vulnerability.  
For example, if you find an XSS, try making it into an account takeover by finding incorrectly configured cookies or endpoints. 
  4. Don’t be afraid to look for older projects that still fit into the scope of the Bug Bounty program.

* * *

Timeline|  
---|---  
2018-12-09| Vulnerability reported  
2018-12-10| Priority changed to P1  
2018-12-10| Looking into it  
2018-12-10| Nice catch  
2018-12-11| Reward issued  
  
Written by [Thomas Orlita](https://thomasorlita.com/)
