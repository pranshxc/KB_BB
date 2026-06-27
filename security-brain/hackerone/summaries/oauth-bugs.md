---
title: OAuth Vulnerability Patterns
description: Common OAuth implementation vulnerabilities and misconfigurations.
created: 2026-06-26
tags:
  - hackerone
  - oauth
  - sso
  - authentication
  - summary
---

# OAuth Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Redirect URI Validation Bypass
- Open redirect on callback URI allows token theft
- Router-based bypass: /callback/valid/../attacker.com
- Path traversal: /callback/valid?attacker.com
- Subdomain takeover on allowed redirect domains

### 2. CSRF on OAuth Flow
- Missing `state` parameter allows CSRF attack
- Attacker initiates auth and links their account to victim's session

### 3. Authorization Code Interception
- Code exchanged over insecure channel (missing PKCE)
- Native apps without PKCE vulnerable to custom scheme interception

### 4. Token Scope Escalation
- User can escalate scope by modifying token request
- Implicit grant abuse to request additional scopes

### 5. OpenID Connect ID Token Issues
- Missing `nonce` parameter allows token replay
- Claims not verified against expected values
- `azp` (authorized party) claim not validated

## Defensive Checklist
- [ ] Validate redirect_uri against allowlist (exact match)
- [ ] Implement PKCE for all OAuth flows
- [ ] Use `state` parameter to prevent CSRF
- [ ] Validate scope boundaries server-side
- [ ] Use `nonce` in OIDC flows
- [ ] Implement refresh token rotation
- [ ] Validate all token claims (iss, aud, exp)
