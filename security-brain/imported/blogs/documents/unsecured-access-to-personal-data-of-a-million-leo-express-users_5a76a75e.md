---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-29_unsecured-access-to-personal-data-of-a-million-leo-express-users.md
original_filename: 2019-01-29_unsecured-access-to-personal-data-of-a-million-leo-express-users.md
title: Unsecured access to personal data of a million Leo Express users
category: documents
detected_topics:
- xss
- access-control
- command-injection
- otp
- graphql
- api-security
tags:
- imported
- documents
- xss
- access-control
- command-injection
- otp
- graphql
- api-security
language: en
raw_sha256: 5a76a75ecd1650dc259c167c90335aa6f1a611ea743d55244a0392d7c8d28ebd
text_sha256: c0ad57d2439f35340d83672c46adae2450bb6f375b5d9b6e0651ad0f06474b15
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Unsecured access to personal data of a million Leo Express users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-29_unsecured-access-to-personal-data-of-a-million-leo-express-users.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, otp, graphql, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `5a76a75ecd1650dc259c167c90335aa6f1a611ea743d55244a0392d7c8d28ebd`
- Text SHA256: `c0ad57d2439f35340d83672c46adae2450bb6f375b5d9b6e0651ad0f06474b15`


## Content

---
title: "Unsecured access to personal data of a million Leo Express users"
page_title: "Unsecured access to personal data of a million Leo Express users - Web Security Blog"
url: "https://websecblog.com/vulns/leoexpress-personal-data/"
final_url: "https://websecblog.com/vulns/leoexpress-personal-data/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Leo Express"]
bugs: ["Broken authorization", "XSS"]
publication_date: "2019-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5444
---

# Unsecured access to personal data of a million Leo Express users

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[January 29, 2019February 4, 2023](https://websecblog.com/vulns/leoexpress-personal-data/)

[Read this article in Czech.](https://websecblog.com/vulns/leoexpress-osobni-udaje/)

Leo Express is a Czech company operating train and bus lines in Central Europe. They provide an option of registering an account and joining loyalty programs as well as getting points for each ride.

When I signed up, I noticed that on every page load a GraphQL request is sent to the server, which returns my account information in JSON.  
[GraphQL](https://graphql.org/) is a query language for APIs (a popular alternative to REST) that returns data defined on the client side in a single request.  

Here’s how the content of this POST request looked like:
  
  
  {
  "query":"
  query getActualUserDataQuery($email: String, $token: String, $timestamp: Int, $locale: String) {
  getActualUserData(email: $email, token: $token, timestamp: $timestamp, locale: $locale) {
  token
  user {
  id
  login
  firstName
  lastName
  phone
  address_state
  address_city
  address_street
  address_zip
  facebook_id
  google_id
  sex
  currency
  language
  profile_picture
  clubmember
  credit_bonus
  credit_standard
  smilebus
  distance
  agreements {
  type
  enabled
  __typename
  }
  __typename
  }
  error {
  code
  message
  __typename
  }
  __typename
  }
  }
  ",
  "variables":{
  "email":"info@example.com",
  "token":null,
  "timestamp":0,
  "locale":"cs"
  },
  "operationName":"getActualUserDataQuery"
  }

In the _variables_ object we will be interested in the _email_ and _token_ fields, where my email and an authorization token were filled in. I didn’t expect this request to **still work** even when the token was changed or wasn’t there at all.

I also tried removing cookies from the request headers in case it was being authorized thanks to them. But this wasn’t the case.  
This meant it will return the data for any registered email that was entered.

The response body contained information like name, phone number, full address and other things,  
e.g. a connected facebook/google account.

![JSON response data](https://websecblog.com/wp-content/uploads/2019/01/graph-3.png)

### Part two, XSS and credit cards

Another problem in connection to a reflected [XSS](https://www.openbugbounty.org/reports/644737/) allowed us to get information about saved credit cards of a logged-in user.

Upon order completion, a redirect will be made to the following URL with a message that the tickets were sent to the user’s email address.
  
  
  https://www.leoexpress.com/en/order-confirmation?order=12345&email=info@example.com&state=success

The issue was that the displayed email address was taken from the URL’s _email_ parameter and special characters weren’t escaped before it was inserted to the page. Since the website didn’t have a [Content Security Policy](https://websecblog.com/vulns/google-csp-evaluator/), it meant it was possible to execute arbitrary JavaScript code on the page.

![Reflected XSS](https://websecblog.com/wp-content/uploads/2019/01/xss.png)

Once any logged-in user clicks or is redirected to that URL, we gain practically unlimited access over their account.

If the user has a saved credit card in their profile, we have an access to the information about it. That includes the card type, date when it was added, and most importantly the first 6 and last 4 digits of the credit card number. That’s **10 digits** from the total of 16. That might already be useful for something…

These vulnerabilities were fixed within three months of the initial report, which isn’t ideal, but better than nothing.

Written by [Thomas Orlita](https://thomasorlita.com/)
