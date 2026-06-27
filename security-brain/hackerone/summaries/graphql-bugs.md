---
title: GraphQL Vulnerability Patterns
description: Common GraphQL API security vulnerabilities and defensive patterns.
created: 2026-06-26
tags:
  - hackerone
  - graphql
  - api
  - summary
---

# GraphQL Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Authorization Bypass
- Missing field-level authorization in resolvers
- Batch query to test authorization for multiple objects
- Introspection-enabled schema abuse to find unsecured fields

### 2. Rate Limiting / DoS
- Deeply nested queries cause resource exhaustion
- Batching attack (requesting many objects in one query)
- Aliased queries bypass query cost analysis

### 3. Injection via GraphQL
- SQL injection through GraphQL arguments
- NoSQL injection through filter arguments
- Command injection through resolver arguments

### 4. Information Disclosure
- Stack traces in error messages
- Field suggestions in error responses
- Introspection enabled in production

## Defensive Checklist
- [ ] Disable introspection in production
- [ ] Implement field-level authorization
- [ ] Set query depth limits
- [ ] Set query complexity/rate limits
- [ ] Implement persistent query allowlist
- [ ] Sanitize all resolver arguments
- [ ] Use generic error messages
