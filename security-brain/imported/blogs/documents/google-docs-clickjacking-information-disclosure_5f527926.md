---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-05-13_google-docs-clickjacking-information-disclosure.md
original_filename: 2014-05-13_google-docs-clickjacking-information-disclosure.md
title: Google Docs 'ClickJacking' (Information Disclosure)
category: documents
detected_topics:
- clickjacking
- command-injection
- information-disclosure
tags:
- imported
- documents
- clickjacking
- command-injection
- information-disclosure
language: en
raw_sha256: 5f5279264a7b7fa158af75f7a01054c121e57ce42bcadc57bb50200add74dbda
text_sha256: 8c65b8b7057ce705ab24b09e1412dbcf2daa7626df69cd4a8c5f10c019714ab0
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Google Docs 'ClickJacking' (Information Disclosure)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-05-13_google-docs-clickjacking-information-disclosure.md
- Source Type: markdown
- Detected Topics: clickjacking, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `5f5279264a7b7fa158af75f7a01054c121e57ce42bcadc57bb50200add74dbda`
- Text SHA256: `8c65b8b7057ce705ab24b09e1412dbcf2daa7626df69cd4a8c5f10c019714ab0`


## Content

---
title: "Google Docs 'ClickJacking' (Information Disclosure)"
page_title: "maustin.net  | Google Docs 'ClickJacking' (Information Disclosure)"
url: "https://maustin.net/google_docs"
final_url: "https://maustin.net/google_docs"
authors: ["Matt Austin (@mattaustin)"]
programs: ["Google"]
bugs: ["Clickjacking"]
publication_date: "2014-05-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6372
---

**tl;dr** : Google documents leak full name and e-mail address via ClickJacking the “request permissions” dialog in a private doc.

### Details:

![Details](/img/image03-1024x581.png)

  1. Victim visits the evil site.
  2. The evil server uses the google docs API to creates a unique document for the visitor. 
  * The document is named with the unique session id of the victim.
  * The document is set to private.
  3. A URL to the new document is returned to the server.
  4. An iframe is created with the following page from google: 
  * ![google_perms](/img/image02.png)
  * This page is cropped to only have the “request access button”.
  * Style is used to make the iframe 100% transparent and always on top of the page. Javascript is used to make the cropped request access button follow the mouse around the page.The resulting “Click Jack” or UI Redressing would look like:
  * ![click_jack_goog](/img/image01.png)
  5. When the user clicks anywhere on the evil page they are actually clicking on the “request access” button. of the google doc.
  6. Once the user clicks on the link the page starts polling with ajax for an update from the server.
  7. Google sends an e-mail, on behalf of the user including full name and e-mail, to the creator of the document ([[email protected]](/cdn-cgi/l/email-protection)) to request access.
  8. The evil server is running an IMAP client listening for document requests to [[email protected]](/cdn-cgi/l/email-protection).
  9. The IMAP client receives the request from the google doc that is named after the value of the session key. The evil server can now tie the user session (from the document requesting title) to the “from: ” name and address in the request. The polling request from step 6 will be updated with the identity of the current user.

### Success!!!

![click_jack_success](/img/image00.png)
