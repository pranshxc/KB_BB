---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-12-18_flickr-xss-stored-dom-xss.md
original_filename: 2013-12-18_flickr-xss-stored-dom-xss.md
title: Flickr XSS (Stored / DOM XSS)
category: documents
detected_topics:
- xss
- command-injection
- cors
- api-security
tags:
- imported
- documents
- xss
- command-injection
- cors
- api-security
language: en
raw_sha256: afd6a052e7937f7ff8c4b1d29604d538437397ab3143e7d267d17ef7b93b2406
text_sha256: de7941887f36f95c20da370f3bdfa40183060c85b1e5c590c756f1d284f1737b
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# Flickr XSS (Stored / DOM XSS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-12-18_flickr-xss-stored-dom-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `afd6a052e7937f7ff8c4b1d29604d538437397ab3143e7d267d17ef7b93b2406`
- Text SHA256: `de7941887f36f95c20da370f3bdfa40183060c85b1e5c590c756f1d284f1737b`


## Content

---
title: "Flickr XSS (Stored / DOM XSS)"
page_title: "maustin.net  | Flickr XSS (Stored / DOM XSS)"
url: "https://maustin.net/articles/2013-12/flickr_xss"
final_url: "https://maustin.net/articles/2013-12/flickr_xss"
authors: ["Matt Austin (@mattaustin)"]
programs: ["Flickr"]
bugs: ["XSS"]
publication_date: "2013-12-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6384
---

The mobile version of the flicker site accept input from the user controlled data and includes it in the HTML output without proper encoding. This is similar to the bug posted at: [Abusing CORS for an XSS on Flickr](http://blog.fin1te.net/post/69821278473/abusing-cors-for-an-xss-on-flickr) which is actaully really similar to a bug I found on facebook mobile a few years ago: [Facebook XSS via CORS](/2010/07/06/facebook_html5.html)

### POC:

  1. First uploaded an image with the following meta data as a title:  

  2. Get the API (on the mobile domain) url for this video: http://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key=***REDACTED*** 
  3. Normally this would not be an issue for 2 reasons. 
  * This is not directly an XSS because the Content Type is set to text/javascript
  * It is on a different domain that exploitable site. However the API URL can be changed to www (or none) subdomain or to the mobile domain “m.flickr.com”
  4. The http://m.flickr.com/#/ site validates that the rest of the URL is a relative path but because the API can be change to the mobile domain we can send relative path to the unescaped HTML that we added as our video title.

### Final POC (one URL):

http://m.flickr.com/#/services/rest/?method=flickr.photos.getInfo&api_key=***REDACTED***

### Timeline:

  * 12/18/2013 Submitted (auto reply e-mail)
  * 01/21/2013 After 30+ days of no reply Tweet to @YahooSecurity
  * 03/11/2014 Resolved 90 days later Payment from HackerOne

Overall a poor experinace with Yahoo on this issue. The only comunication I recieved other than an automated reply was 3 months later saying it was resolved and only after I reached out via twitter. 90 Days to resolve an XSS that could lead to account take over / private data seems a bit long to me.
