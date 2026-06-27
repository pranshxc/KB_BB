---
title: "OAuth 2.0 Redirect URI Validation Bypass"
date: 2024-06-15
author: security-researcher
tags:
  - oauth
  - authentication
  - sso
---

# OAuth 2.0 Redirect URI Validation Bypass

## Overview

When implementing OAuth 2.0, one of the most critical security checks is redirect URI validation. If the redirect_uri parameter is not strictly validated, an attacker can steal authorization codes and gain account access.

## Common Bypass Techniques

1. **Open redirect on whitelisted domain**: If the callback URL is `/oauth/callback` and has an open redirect, an attacker can chain it.

2. **Subdirectory bypass**: `https://app.com/callback/attacker.com` — some validators only check the domain prefix.

3. **Parameter injection**: `https://app.com/callback?redirect=attacker.com` — if the app forwards to the `redirect` parameter.

## Prevention

- Use exact string matching for redirect URIs
- Do not allow wildcards in redirect URI patterns
- Implement PKCE (Proof Key for Code Exchange)
- Use the `state` parameter to prevent CSRF

## References

- RFC 6749 Section 3.1.2
- RFC 7636 (PKCE)
