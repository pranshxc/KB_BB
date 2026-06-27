---
title: Security Root Causes Taxonomy
description: Common root causes of security vulnerabilities with detection and prevention guidance.
created: 2026-06-26
tags:
  - taxonomy
  - root-causes
  - appsec
  - secure-code-review
---

# Security Root Causes Taxonomy

## Input Validation Failures

| Root Cause | Examples | Detection |
|------------|----------|-----------|
| Missing input sanitization | XSS, SQLi, Command Injection | Code review, SAST |
| Insufficient type checking | Parameter pollution, type confusion | Type validation |
| No boundary validation | Integer overflow, buffer overflow | Fuzzing |
| Trusting user-controlled data | SSRF, path traversal, open redirect | Input tracing |

## Authentication & Authorization Failures

| Root Cause | Examples | Detection |
|------------|----------|-----------|
| Missing access control checks | IDOR, privilege escalation | DAST, manual review |
| Weak session management | Session reuse, no invalidation | Session analysis |
| Token validation gaps | JWT "none" algorithm, missing signature check | Token fuzzing |
| State validation missing | CSRF, OAuth state parameter | Parameter review |

## Cryptographic Failures

| Root Cause | Examples | Detection |
|------------|----------|-----------|
| Weak algorithm usage | MD5, SHA1, RC4 | SAST, crypto audit |
| Secret exposure | Hardcoded keys, tokens in logs | Secrets scanning |
| Randomness predictability | PRNG seed prediction, token prediction | Code review |
| Missing signature validation | SAML signature bypass, JWT alg confusion | Integration testing |

## Configuration & Deployment Failures

| Root Cause | Examples | Detection |
|------------|----------|-----------|
| Debug/verbose mode enabled | Stack traces, debug endpoints | Configuration review |
| Permissive CORS | Origin reflection, wildcard origins | HTTP header review |
| Missing security headers | X-Frame-Options, CSP, HSTS | Header scanning |
| Insecure default configurations | Default credentials, open buckets | Infrastructure audit |

## Business Logic Failures

| Root Cause | Examples | Detection |
|------------|----------|-----------|
| Race conditions | Coupon abuse, balance manipulation | Concurrent testing |
| State machine flaws | Order state jumps, workflow bypass | Manual review |
| Multi-step process gaps | Email change without confirmation | Flow analysis |
| Boundary condition mishandling | Bulk operations, pagination flaws | Fuzzing |

## Secure Design Principles

The following principles help prevent entire classes of vulnerabilities:

1. **Defense in Depth**: Multiple layers of security controls
2. **Least Privilege**: Minimal access rights for each component
3. **Secure by Default**: Safe defaults, opt-in for risky features
4. **Fail Secure**: Fail closed, not open
5. **Separation of Duties**: Multiple approvals for sensitive actions
6. **Complete Mediation**: Every access checked every time
7. **Economy of Mechanism**: Simple, small trusted computing base
8. **Open Design**: Security doesn't depend on secrecy
