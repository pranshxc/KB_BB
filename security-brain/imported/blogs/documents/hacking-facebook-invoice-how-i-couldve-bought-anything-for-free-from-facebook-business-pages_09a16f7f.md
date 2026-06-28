---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-18_hacking-facebook-invoice-how-i-couldve-bought-anything-for-free-from-facebook-bu.md
original_filename: 2022-07-18_hacking-facebook-invoice-how-i-couldve-bought-anything-for-free-from-facebook-bu.md
title: 'Hacking Facebook Invoice: How I could’ve bought anything for Free from Facebook
  Business Pages'
category: documents
detected_topics:
- mobile-security
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- mobile-security
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: 09a16f7f27c3498f8ee7d66c412c89335bff0d162efca815742a4109ff8fd6cf
text_sha256: 42f6231c2a6aa12fb51664978ced53bec5e4903b143a0ce3db23056182977811
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Facebook Invoice: How I could’ve bought anything for Free from Facebook Business Pages

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-18_hacking-facebook-invoice-how-i-couldve-bought-anything-for-free-from-facebook-bu.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `09a16f7f27c3498f8ee7d66c412c89335bff0d162efca815742a4109ff8fd6cf`
- Text SHA256: `42f6231c2a6aa12fb51664978ced53bec5e4903b143a0ce3db23056182977811`


## Content

---
title: "Hacking Facebook Invoice: How I could’ve bought anything for Free from Facebook Business Pages"
url: "https://infosecwriteups.com/hacking-facebook-invoice-how-i-couldve-bought-anything-for-free-from-facebook-business-pages-42bcfaa73ec4"
authors: ["Samip Aryal (@samiparyal_)"]
programs: ["Meta / Facebook"]
bugs: ["Payment bypass"]
bounty: "250"
publication_date: "2022-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2434
scraped_via: "browseros"
---

# Hacking Facebook Invoice: How I could’ve bought anything for Free from Facebook Business Pages

Hacking Facebook Invoice: How I Could’ve bought anything for Free from Facebook Business Pages | Parameter Tampering
Samip Aryal
Follow
5 min read
·
Jul 19, 2022

359

4

…

Press enter or click to view image in full size

Samip Aryal, Nepal

This writeup is about how i found a way to basically tamper requests from Facebook’s Order Invoice allowing me to pay for any Items without paying the actual amount i.e. how i could register my payment successfully using Facebook’s Order Invoices and basically get any items for free.

Facebook allows Facebook Pages to create and manage orders and payouts using Order Invoices. The invoice contains four different sections to be marked chronologically for the selling page to finally ship/dispatch the order.

Order Invoice Base Format @ Facebook-Messenger for Commerce

Now, each of these sections has its different synced-up page sections in the Orders and Management Tab in the Meta Business Suite too.

Press enter or click to view image in full size
Orders and Payouts management tab @ Meta Business Suite

Business/Commerce pages at Meta(Facebook, Instagram) selling their products through the platform create such invoices to keep track of the order.

Now, Here in this invoice; the buyer can first confirm the order & then, only the seller page has the ability to mark the order as paid or dispatched after the buyer pays for the order. After that, the buyer can complete the trade by marking the order as received if he wants.

So, the buyer only can:

I was interested in Android Testing the Page Messenging section of Android Messenger (also called Messenger for Commerce). Thus, out of curiosity about this payment invoice, I compared a bunch of requests made when marking each of those sections of the invoice. What I noticed was that a different kind of Post request went while confirming the order from the buyer but when marked as received, the Post request was similar to requests sent when marked as paid or dispatched.

Now this made me excited as Post requests when marked as received & marked as paid were almost identical as they contained identical parameters.

Press enter or click to view image in full size
Post Request when marking as received

Only the difference was that the action_identifier contained the parameter mcom_mark_as_received in the first one with status_step=3 but when marking as paid from the seller page’s side, the action_identifier contained the parameter mcom_mark_as_paid with status_step=1

Get Samip Aryal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, having these two separate requests (with different privileges settings for two separate parties i.e. seller page & the buyer) being identical and no apparent or proper actor permission checks into action initially, I was curious; what if being a buyer, I capture a dummy mark_as_received request from some other invoice and replace the target_id with the target order invoice id and the action_identifier to mcom_mark_as_paid. Will I register a payment for the target order invoice on behalf of the page?

But No!

It showed me an error because there was a permission check needed to complete the mcom_mark_as_paid request.

Felt like there were all the proper permission checks for important parameters like mark_as_paid which I was trying to break in. But after some fuzzing, I found another action identifier: mcom_cancel that pushes the order invoice to a canceled state. This endpoint didn’t have any permission barriers and was accessible by both parties: the buyer & the seller page. Also, I found that the canceled state of the order invoice can be reverted back automatically into an active state by firing any of those above post requests. Here, The canceled state seemed to have no relation with actor privilege checks. Now, at this point; I cracked an idea.

What if I forcefully pushed the order invoice to a canceled state by triggering the mcom_cancel action identifier and then firing the modified request with ‘mcom_mark_as_paid’ in the action_identifier just to automatically bring the order invoice to an active state as a buyer?

Will it also mark the order paid subsequently while turning into an active state?

It did happen!

This means that using that method, I could simply replace the target_id from the dummy mark_as_received Post request captured using my own page, with the target order invoice id of any other victim Business Page for which I want the full payment to be registered without me paying the actual amount.

And the best part here is that every action is happening on behalf of the page which means that the details of these actions are being recorded and shown on behalf of the page (for eg: it’ll show that the page itself canceled the request or marked the request as paid). Additionally, all these activities are synced up with Meta Business Suite’s Order and Payouts management section where the order will reach the waiting for dispatch/ship section with the mark that the seller page has already received the payment amount along with all other genuine orders. In most cases, the seller page might ship the orders when seen paid and waiting for dispatch.

So, using this vulnerability; any malicious buyer could simply make orders, manipulate the endpoint requests, register a fake payment on behalf of the page itself, and buy any items for free.

[Timeline]

Reported: May 2022

Triaged: May 2022

Fixed: July 2022

Rewarded: July 19, 2022 { 250$ ?}

Thank you for reading this write-up. If you have any queries/suggestions, I’m available on Facebook/ Instagram.
