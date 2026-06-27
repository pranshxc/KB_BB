---
title: Security Remediation Patterns
description: Common remediation patterns for security vulnerabilities with code examples and regression testing guidance.
created: 2026-06-26
tags:
  - taxonomy
  - remediation
  - appsec
  - secure-code-review
---

# Security Remediation Patterns

## Authentication & Token Remediation

### Password Reset Token Fix
- Token must be single-use and expire after a short TTL (15-30 min)
- Invalidate all existing tokens when a new one is generated
- Token must be cryptographically random (CSPRNG)
- Send token via out-of-band channel (email)
- Verify old password when requesting reset
- Log all password reset attempts

### JWT Fixes
- Always validate algorithm header against an allowlist
- Set short expiration times (15-60 min)
- Include `aud` (audience) and `iss` (issuer) claims and validate them
- Use a strong signing key managed via secrets manager
- Implement token rotation/refresh with revocation
- Store token allowlist/blocklist in Redis for critical operations

### Session Fix
- Generate new session ID after login
- Invalidate session on logout, password change, email change
- Set secure, httpOnly, SameSite cookie flags
- Implement absolute and idle session timeouts
- Bind session to IP or user-agent for high-security apps

## Authorization Remediation

### IDOR Fix
- Never expose raw database IDs in URLs or APIs
- Always verify ownership before returning data
- Use indirect object references (UUIDs, hashed IDs)
- Implement server-side authorization checks on every endpoint
- Use a centralized authorization layer (e.g., middleware)

### RBAC/ABAC Fix
- Define roles and their permissions explicitly
- Enforce authorization at API gateway or middleware layer
- Validate permissions on every request, not just on page load
- Test all role combinations
- Deny by default, allow explicitly

## Injection Remediation

### SQL Injection Fix
- Use parameterized queries / prepared statements
- Avoid string concatenation for SQL
- Use an ORM with safe query building
- Apply least-privilege DB user permissions
- Enable query logging for audit

### XSS Fix
- Context-aware output encoding
- Content Security Policy (CSP) header
- Sanitize HTML input (allowlist approach, not denylist)
- Set `X-XSS-Protection` header
- Use React/Vue/Angular auto-escaping (with caution)

### SSRF Fix
- Maintain allowlist of permitted outbound destinations
- Validate and sanitize all user-supplied URLs
- Block access to private IP ranges (127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.169.254)
- Use a dedicated network policy / firewall rules
- Use a URL parser library, not regex or string matching

## Business Logic Remediation

### Race Condition Fix
- Use database transactions with appropriate isolation levels
- Implement optimistic locking with version numbers
- Use distributed locks (Redis Redlock) for critical resources
- Apply idempotency keys for state-changing operations
- Implement database-level constraints

### Rate Limiting Fix
- Implement rate limiting per user, per IP, per endpoint
- Use sliding window, not fixed window
- Apply rate limits to authentication endpoints aggressively
- Return proper `Retry-After` headers
- Use a distributed counter (Redis, memcached)

## Detection & Monitoring

- Log all security-relevant events (auth, authz changes, data access)
- Alert on suspicious patterns (multiple failed auth, rapid API calls)
- Monitor for known attack patterns
- Test detection rules regularly
- Document incident response procedures
