---
title: Access Control Vulnerability Patterns
description: Common access control and authorization bypass patterns.
created: 2026-06-26
tags:
  - hackerone
  - access-control
  - authorization
  - summary
---

# Access Control Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Role-Based Escalation
- Regular user can access admin endpoints
- Role parameter in request determines access
- Cookie/session modification escalates privileges

### 2. Function-Level Access Control
- Missing server-side check for admin functions
- API endpoints not protected behind middleware
- Client-side only hiding of admin actions

### 3. Multi-Tenant Access
- Organization boundary not enforced
- org_id parameter changeable in controller
- Shared DB queries without tenant filter

### 4. Indirect Object Access
- Related objects accessible via parent ID manipulation
- Commenting on another user's private post
- Accessing draft content of other users

### 5. Authorization Through Obscurity
- UUID-based URLs assumed secure
- Non-standard header-based authentication
- Security through hidden endpoints

## Defensive Checklist
- [ ] Implement centralized authorization middleware
- [ ] Apply authorization on every endpoint
- [ ] Use role-based or attribute-based access control
- [ ] Enforce tenant isolation at database level
- [ ] Never rely on client-side authorization
- [ ] Audit all API endpoints for authz consistency
- [ ] Test with multiple user roles for each endpoint
