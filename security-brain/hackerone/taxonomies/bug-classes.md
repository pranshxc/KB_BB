---
title: Security Bug Classes Taxonomy
description: Comprehensive taxonomy of security vulnerability classes relevant to web applications, APIs, and cloud services.
created: 2026-06-26
tags:
  - taxonomy
  - bug-classes
  - appsec
  - owasp
---

# Security Bug Classes Taxonomy

## Authentication & Session Management

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| Password Reset Bugs | Password reset poisoning, token reuse, link expiration | Account takeover |
| Session Management Bugs | Session fixation, session hijacking, concurrent sessions | Account takeover |
| MFA Bypass | 2FA bypass, OTP bypass, MFA reset | Unauthorized access |
| OAuth Bugs | OAuth misconfiguration, redirect_uri bypass, CSRF on OAuth | Account takeover |
| SAML Bugs | SAML signature bypass, XML signature wrapping, issuer confusion | Authentication bypass |
| JWT Bugs | Algorithm confusion (none, HS256/RS256 mix), key confusion | Authentication bypass |
| Email Verification Bypass | Email confirmation skip, verification link reuse | Account takeover |

## Access Control

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| Broken Access Control | Privilege escalation, horizontal/vertical | Data exposure |
| IDOR / BOLA | Insecure Direct Object Reference, Object ID enumeration | Data access |
| Tenant Isolation Bugs | Multi-tenant bypass, cross-tenant access | Data breach |
| Authorization Bypass via Role Downgrade | Role manipulation, privilege de-escalation | Unauthorized access |
| API Mass Assignment | Auto-binding, property injection | Data manipulation |

## Injection

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| XSS (Cross-Site Scripting) | Reflected, Stored, DOM-based | Session theft, phishing |
| SQL Injection | SQLi, blind SQLi, second-order SQLi | Data exfiltration |
| Command Injection | RCE, OS command injection, argument injection | Remote code execution |
| Path Traversal | Directory traversal, Local File Inclusion (LFI) | File read |
| Template Injection | SSTI (Server-Side Template Injection) | Remote code execution |
| LDAP Injection | LDAP query injection | Authentication bypass |
| NoSQL Injection | MongoDB injection, query operator injection | Data access |

## Server-Side Attacks

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| SSRF | Server-Side Request Forgery, cloud metadata attack | Internal access |
| Web Cache Poisoning | Cache deception, cache poisoning | Content hijacking |
| Request Smuggling | HTTP request smuggling, TE.CL, CL.TE | Request hijacking |
| Race Conditions | TOCTOU, race window, concurrent execution | Data corruption |
| Business Logic Bugs | Logic flaw, business logic bypass | Financial loss, abuse |
| Rate Limit Bypass | Rate limiting bypass, throttling bypass | Brute-force, abuse |

## Client-Side Attacks

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| CORS Misconfiguration | CORS bypass, origin reflection | Cross-origin data read |
| Clickjacking | UI redressing, frame overlay | Unauthorized actions |
| CSRF | Cross-Site Request Forgery, session riding | State-changing actions |

## File & Resource Handling

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| File Upload Bugs | Content-type bypass, unrestricted upload, path traversal | RCE, storage abuse |
| Insecure File Processing | XXE, file parsing, zip slip| RCE, DoS |
| Subdomain Takeover | DNS takeover, CNAME takeover, dead domain | Phishing, credential theft |

## Information Disclosure

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| Information Disclosure | Debug endpoints, stack traces, verbose errors, directory listing | Reconnaissance |
| Open Redirect | URL redirect, parameter injection| Phishing |

## GraphQL Specific

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| GraphQL Authorization Bypass | GraphQL authz bypass, missing field-level checks | Data access |
| GraphQL Introspection | Introspection enabled, schema leak| Reconnaissance |
| GraphQL Batching Attack | Batching, resource exhaustion, N+1 queries| DoS |
| GraphQL Depth Attack | Deeply nested queries| DoS |

## Banking / Fintech Specific

| Class | Common Synonyms | Typical Impact |
|-------|-----------------|----------------|
| Webhook Signature Validation | Webhook replay, missing signature check| Data injection |
| Insecure Direct Object Reference (Financial) | Invoice download, transaction viewing | Financial data leak |
| Coupon/Referral Abuse | Discount manipulation, promo code reuse | Financial loss |
