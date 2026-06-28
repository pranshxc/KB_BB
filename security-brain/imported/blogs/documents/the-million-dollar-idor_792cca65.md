---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-27_the-million-dollar-idor.md
original_filename: 2022-08-27_the-million-dollar-idor.md
title: The Million Dollar IDOR
category: documents
detected_topics:
- idor
- access-control
- command-injection
- automation-abuse
- race-condition
- graphql
tags:
- imported
- documents
- idor
- access-control
- command-injection
- automation-abuse
- race-condition
- graphql
language: en
raw_sha256: 792cca65e21148fa0fdc18ee4813499c278298743c1c15988eee2be596e74889
text_sha256: 32abd54ae3b6a0306473d6d5a69cc208da7747bab36be9912c24921796389ea2
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# The Million Dollar IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-27_the-million-dollar-idor.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, automation-abuse, race-condition, graphql
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `792cca65e21148fa0fdc18ee4813499c278298743c1c15988eee2be596e74889`
- Text SHA256: `32abd54ae3b6a0306473d6d5a69cc208da7747bab36be9912c24921796389ea2`


## Content

---
title: "The Million Dollar IDOR"
page_title: "The Million Dollar Hack.Hacking A Gift Card Company | Medium"
url: "https://monish-basaniwal.medium.com/the-million-dollar-hack-8163892bfe2f"
authors: ["Monish Basaniwal"]
bugs: ["IDOR", "Race condition", "GraphQL"]
publication_date: "2022-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2253
scraped_via: "browseros"
---

# The Million Dollar IDOR

The Million Dollar IDOR
Monish
Follow
6 min read
·
Aug 27, 2022

50

2

Press enter or click to view image in full size

“With great power comes great responsibility”

Read on to find out how I was able to leverage a simple IDOR + Authorization vulnerability to expose thousands of Visa gift cards on a leading gift card company’s website + Bonus: Found a way to redeem them more than once.

Monetary websites have a high need for the best grade security as they protect valuable assets that shouldn’t easily be accessible to anyone. Very recently we all heard the news of Tremendous, another gift card company which was hacked and a lot of user data and gift cards were stolen :

Press enter or click to view image in full size
The Recon

I stumbled on this site [redacted.com] randomly and was keen to understand the technology they were using and the kind of data that was being passed in the background, very quickly it was clear that the website was making use of a GraphQL-based API where the API requests were in the form of. “queries” requesting exactly the amount of data it needs.

What does this mean to hackers? The endpoint for all API communications in a GraphQL API remains the same usually /graphql and the queries and the methods to run in the body define the kind of operation which has to be performed which is backed by a Schema.

There are a few ways by which you can fetch all the available queries, and mutations and also return the entire schema which includes everything which has been defined, popularly known as the Retrospection Query.

Fetch all available queries

{
  __schema {
  queryType {
  fields {
  name
  }
  }
  }
}

Fetch all available mutations

{
  __schema {
  mutationType {
  fields {
  name
  }
  }
  }
}

Note that Retrospection Queries are sensitive and are usually disabled on serious production graphql servers and by default on the Apollo GraphQL server. But you will find that very often they are still available.

The Hack

The platform made use of very simple queries to retrieve and show all the gift cards owned by a user. Right after login, a query for getUserStipends was made which basically fetched all the cards which belonged to a specific user, listed out the visa card number, the CVV and the expiry for each card and each card had an id which was guessable and incremental like 45,46,47.

query getUserStipends {
  myStipends {
  id
  status
  stipend {
  amount
  canAccrue
  colorHex
  colorHex2
  currency
  currentIntervalStart
  emoji
  endDate
  id
  interval
  logoUrl
  name
  nextIntervalStart
  recurrenceStart
  startDate
  createdAt
  }
  }
}

After clicking on a specific card there was yet another request this time for getUserStipend with the id of the specific card I had clicked on:

query getUserStipend($id: Int!) {
  stipendUser(id: $id) {
  activeUserAddressId
  id
  personalCardEnabled
  status
  isTestCard
  redemptionType
  endDate
  endDateExtension
  stipend {
  amount
  canAccrue
  colorHex
  colorHex2
  company {
  id
  allowParticipantBillingAddress
  allowParticipantPersonalCC
  }
  currency
  currentIntervalStart
  emoji
  endDate
  id
  interval
  logoUrl
  name
  nextIntervalStart
  recurrenceStart
  startDate
  createdAt
  address {
  city
  country
  id
  line1
  line2
  phone_number
  postal_code
  state
  }
  merchantCategory {
  categoryId
  categoryName
  merchantId
  merchantName
  url
  logoUrl
  networkId
  }
  }
  userAddresses {
  city
  country
  id
  line1
  line2
  phone_number
  postal_code
  state
  }
  card {
  stripeCardId
  currentBalance
  accruedBalance
  number
  cvc
  expiry
  status
  donated
  categories {
  displayTitle
  title
  }
  cardholder {
  name
  address {
  city
  country
  line1
  line2
  postal_code
  state
  }
  }
  }
  reimbursement {
  history {
  status
  occurredAt
  }
  amount
  targetCurrency
  totalFee
  wiseQuoteId
  wiseRecipientId
  wiseTransferId
  }
  }
}

{
  "id": 100000
}

This query, in turn, returned more in-depth data about the specific card, the amount which was available the currency and so on, the first thing that came to my mind was to change the id parameter to something else as it was very easily guessable.

Get Monish’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Changing the id parameter caused the query to execute successfully and it returned the entire card details of some other user! Just to be sure I tried the same request with another id and every time it returned a new visa gift card which did not belong to me. I now had access to 1000s of valid visa gift cards with varying values and unhinged access to all of them, all with a simple IDOR which resulted in exposing extremely confidential details valued in millions.

I immediately took to the platform’s helpline and reported the vulnerability and within hours this was fixed and acknowledged by the company’s co-founder:

Press enter or click to view image in full size
The Bonus Hack

This was not it, the platform offered another very interesting feature where if you have been issued a gift card in some other currency, you can get it cashed out in the currency of your choice, in this case, they offered direct conversions between USD and INR where the money would be paid directly to an UPI id instantly.

There existed a very interesting vulnerability in the redemption form known as Race Condition.Quoting from Google:

A race condition is an undesirable situation that occurs when a device or system attempts to perform two or more operations at the same time, but because of the nature of the device or system, the operations must be done in the proper sequence to be done correctly.

In simpler words, if you simultaneously ask the server to process 2 or more similar requests which lead to very similar results it may either behave unexpectedly or result in double outputs.

When a redemption process was initiated the platform used to generate a quotationID with the converted amount of the card in the requested currency and then proceeded to ask for more details like the UPI Id to be paid. Once redeem was clicked a request was sent using the quotationID to mark it paid and after which the card would no longer be useful. I intercepted the redemption request and duplicated it a couple of times and sent them all at once, it resulted in the converted amount being credited multiple times to my bank account!

Imagine it like a group of slingshots tied to a single lever, when the lever is pulled all the requests are sent simultaneously to the server, and before the server can mark the quotation id as “used” the server has placed multiple redemption requests which in turn sends multiple reimbursements to the user. Its explained a little better in the following figure :

Press enter or click to view image in full size

So now not only did I have unlimited visa gift cards, but I also had a way to redeem them into my local currency multiple times/card! How could something like this be avoided?

1) Queries leading to actions: On modules where critical systems are involved do not talk to the Database on a multi-query basis. Instead of asking about the gift card in one query and then issuing a second query to change its status, perform both in one query: ‘If not paid set to paid and payout’.

2) DB Acid Properties: Depends on what kind of database you are using, Databases have a very interesting take on ACID properties where most scalable databases place a temporary “lock” on the part of data you are accessing through one request so until one operation is completely done that part of the data is not accessible by other queries.

This report lead to another bounty + a security contract with the company :)

Closing notes and conclusions

1)Do not hesitate to change id parameters to various values especially if they are not unique like a UUID and are incremental like in this case.

2) Always check for race conditions, any action which may lead to a critical action must be double-checked to be race-condition safe. These are more common in single-use assets like vouchers, coupons etc.
