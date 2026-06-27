---
title: IDOR / BOLA Vulnerability Patterns
description: Common Insecure Direct Object Reference and Broken Object Level Authorization patterns.
created: 2026-06-26
tags:
  - hackerone
  - idor
  - bola
  - access-control
  - summary
---

# IDOR / BOLA Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Numeric ID Enumeration
- Sequential numeric IDs used for resources (users, invoices, orders)
- No ownership check before returning data
- Common in REST APIs: `/api/users/123`, `/api/invoices/456`

### 2. UUID Leakage
- UUIDs exposed in client-side code, URLs, or logs
- Authorization check missing even though UUID is "unguessable"
- Security by obscurity is not sufficient

### 3. Multi-Tenant IDOR
- Organization A can access Organization B's data by changing org_id
- Missing tenant isolation in database queries

### 4. IDOR in Membership/Role Changes
- User can change their role or another user's role via direct API calls
- POST /api/org/123/members/456 with modified role parameter

### 5. IDOR via GraphQL
- GraphQL query allows fetching any object by ID
- Missing field-level authorization checks

## Defensive Checklist
- [ ] Always verify resource ownership before access
- [ ] Use indirect references where possible
- [ ] Implement centralized authorization middleware
- [ ] Test with unexpected IDs (negative, zero, others' IDs)
- [ ] Don't rely on UUID obscurity for access control
- [ ] Apply rate limiting to enumeration-prone endpoints
