#!/usr/bin/env python3
"""
Generate security taxonomy Markdown files for the Security Brain.

These files provide general AppSec knowledge for the RAG system,
including bug classes, root causes, testing methodology, remediation patterns,
and curated summaries of common vulnerability patterns.

Usage:
  python generate_security_taxonomies.py
  python generate_security_taxonomies.py --output-dir security-brain/hackerone/taxonomies
  python generate_security_taxonomies.py --summaries-dir security-brain/hackerone/summaries
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("taxonomy-gen")


# ==============================================================================
# TAXONOMIES
# ==============================================================================

BUG_CLASSES = """---
title: Security Bug Classes Taxonomy
description: Comprehensive taxonomy of security vulnerability classes relevant to web applications, APIs, and cloud services.
created: {date}
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
"""

ROOT_CAUSES = """---
title: Security Root Causes Taxonomy
description: Common root causes of security vulnerabilities with detection and prevention guidance.
created: {date}
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
"""

TESTING_METHODOLOGY = """---
title: Security Testing Methodology
description: Structured methodology for security testing, code review, and vulnerability assessment.
created: {date}
tags:
  - taxonomy
  - testing
  - methodology
  - secure-code-review
---

# Security Testing Methodology

## 1. Reconnaissance & Information Gathering

- Map application functionality and features
- Identify authentication/authorization boundaries
- Document data flow and trust boundaries
- Review API documentation and schema
- Identify third-party integrations

## 2. Authorization Testing

- Test horizontal privilege escalation (user A → user B's data)
- Test vertical privilege escalation (user → admin)
- Test role-based access controls
- Test object-level authorization (IDOR/BOLA)
- Test function-level authorization
- Test tenant isolation boundaries
- Test API key/scope enforcement

## 3. Authentication Testing

- Test credential strength and password policies
- Test session management (creation, expiration, invalidation)
- Test multi-factor authentication (enrollment, bypass, reset)
- Test OAuth/OIDC flows for known misconfigurations
- Test SAML SSO for signature validation
- Test JWT token handling (alg confusion, expiration, validation)
- Test password reset flow (token expiration, reuse, prediction)
- Test account recovery and email verification

## 4. Input Validation Testing

- Test for injection vulnerabilities (SQLi, NoSQLi, Command Injection)
- Test for XSS (reflected, stored, DOM-based)
- Test for SSRF (internal resources, cloud metadata)
- Test for path traversal (files, directories)
- Test for file upload abuse (type bypass, path traversal, malware)
- Test for XXE and XML parsing issues
- Test for template injection (SSTI)
- Test deserialization (pickle, YAML, Java)

## 5. Session & Token Testing

- Verify session tokens are cryptographically random
- Test session timeout and idle timeout
- Test session invalidation on logout
- Test concurrent session handling
- Test token scope and audience restrictions
- Test API key rotation and revocation

## 6. API & GraphQL Testing

- Test GraphQL introspection is disabled in production
- Test GraphQL query depth limits
- Test GraphQL batching/rate limiting
- Test API versioning and deprecation handling
- Test API key scope enforcement
- Test webhook signature validation
- Test API mass assignment
- Test request smuggling

## 7. Business Logic Testing

- Test workflow state machines
- Test concurrent operations (race conditions)
- Test coupon/discount logic
- Test transaction rollback and reversal
- Test multi-step process flows
- Test boundary values (max/min quantities, pagination)

## 8. Configuration Testing

- Review CORS configuration
- Review security headers (CSP, HSTS, XFO, etc.)
- Review error handling (no stack traces)
- Review logging (no sensitive data)
- Review rate limiting and throttling
- Review file upload restrictions

## 9. Cryptographic Testing

- Verify TLS configuration and certificate validity
- Review encryption at rest for sensitive data
- Review hashing algorithm choices (passwords, tokens)
- Review random number generation (CSPRNG usage)
- Review key management practices

## 10. Regression Testing

- After fixing a vulnerability, verify the fix
- Add automated tests for the specific attack pattern
- Check for similar patterns in other parts of the codebase
- Verify no new issues introduced by the fix
- Document the finding and remediation

## Code Review Checklist Template

```
### Authentication Review
- [ ] Password hashing uses bcrypt/argon2/scrypt
- [ ] Session tokens are CSPRNG-generated
- [ ] Session invalidated on logout/password change
- [ ] MFA enforcement on sensitive actions
- [ ] JWT validation checks algorithm, signature, expiration, audience

### Authorization Review
- [ ] Every endpoint checks authorization
- [ ] IDOR prevented via indirect object references or ownership checks
- [ ] Role-based access enforced server-side
- [ ] API key scopes validated on every request
- [ ] Tenant isolation verified at data layer

### Input Validation Review
- [ ] All user input sanitized for context (HTML, SQL, shell)
- [ ] File upload restricted by type, size, content
- [ ] SSRF protection (allowlist, URL validation, network policy)
- [ ] GraphQL depth/complexity limiting enabled
- [ ] CORS allowlist not wildcard

### Crypto & Secrets Review
- [ ] Encryption keys managed via secrets manager
- [ ] TLS configured correctly (no weak ciphers)
- [ ] Secrets never logged or exposed in errors
- [ ] CSPRNG used for all security tokens
```
"""

REMEDIATION_PATTERNS = """---
title: Security Remediation Patterns
description: Common remediation patterns for security vulnerabilities with code examples and regression testing guidance.
created: {date}
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
"""


# ==============================================================================
# SUMMARIES
# ==============================================================================

SUMMARIES = {
    "password-reset-bugs.md": """---
title: Password Reset Bug Patterns
description: Common vulnerability patterns in password reset functionality, derived from HackerOne disclosed reports.
created: {date}
tags:
  - hackerone
  - password-reset
  - authentication
  - summary
---

# Password Reset Bug Patterns

## Common Vulnerability Patterns

### 1. Token Not Expiring After Email Change
- Token generated for old email but still usable after email is changed
- Root cause: Token not invalidated on profile change
- Remediation: Invalidate all active reset tokens when email changes

### 2. Token Reuse
- Reset token can be used multiple times
- Root cause: Token not invalidated after successful reset
- Remediation: Mark token as used after first successful reset

### 3. Token Prediction
- Sequential or predictable token generation
- Root cause: Weak PRNG or timestamp-based tokens
- Remediation: Use CSPRNG (secrets.token_urlsafe, SecureRandom)

### 4. Token Leakage via Referrer
- Reset link contains token, external resources leak via Referrer header
- Root cause: Missing rel="noreferrer" on external resources
- Remediation: Set `rel="noopener noreferrer"` on all external links

### 5. Host Header Poisoning
- Password reset link uses Host header, attacker poisons it
- Root cause: Trusting Host header for URL generation
- Remediation: Use SERVER_NAME / configured base URL, not Host header

### 6. Password Reset via SMS Manipulation
- SMS-based reset codes guessable or interceptable
- Root cause: Short codes, no rate limiting
- Remediation: Longer codes, rate limiting, multi-channel verification

## Defensive Checklist
- [ ] Token expires after short TTL (15-30 min)
- [ ] Token is single-use
- [ ] Token generated via CSPRNG
- [ ] Existing tokens invalidated on email change
- [ ] Existing tokens invalidated on password change
- [ ] No token leakage in URLs or logs
- [ ] Rate limiting on reset endpoint
- [ ] Confirmation step before password change
"""
,
    "idor-patterns.md": """---
title: IDOR / BOLA Vulnerability Patterns
description: Common Insecure Direct Object Reference and Broken Object Level Authorization patterns.
created: {date}
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
"""
,
    "oauth-bugs.md": """---
title: OAuth Vulnerability Patterns
description: Common OAuth implementation vulnerabilities and misconfigurations.
created: {date}
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
"""
,
    "ssrf-patterns.md": """---
title: SSRF Vulnerability Patterns
description: Common Server-Side Request Forgery vulnerability patterns and defenses.
created: {date}
tags:
  - hackerone
  - ssrf
  - server-side
  - cloud
  - summary
---

# SSRF Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Cloud Metadata Access
- Accessing AWS `http://169.254.169.254/latest/meta-data/`
- Accessing GCP `http://metadata.google.internal/computeMetadata/v1/`
- Accessing Azure `http://169.254.169.254/metadata/instance`

### 2. Internal Network Scanning
- SSRF to internal services (Redis, MySQL, Elasticsearch)
- Port scanning via SSRF
- Protocol smuggling (gopher://, dict://, file://)

### 3. Blind SSRF
- Outbound request to attacker-controlled server
- Timing-based data exfiltration

### 4. DNS Rebinding
- Domain initially resolves to legitimate IP
- After validation, attacker changes DNS to internal IP

### 5. SSRF via File Upload / Image Processing
- Image URL processing leads to SSRF
- PDF generation with external resource inclusion

## Defensive Checklist
- [ ] Block access to private/meta IP ranges
- [ ] Use URL allowlist, not denylist
- [ ] Validate URL scheme (reject file://, gopher://, dict://)
- [ ] Use dedicated HTTP client with restricted capabilities
- [ ] Apply network-level controls (firewall, proxy)
- [ ] Disable DNS rebinding protection on resolver
"""
,
    "graphql-bugs.md": """---
title: GraphQL Vulnerability Patterns
description: Common GraphQL API security vulnerabilities and defensive patterns.
created: {date}
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
"""
,
    "information-disclosure.md": """---
title: Information Disclosure Patterns
description: Common information disclosure vulnerability patterns.
created: {date}
tags:
  - hackerone
  - information-disclosure
  - summary
---

# Information Disclosure Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Debug Endpoints Exposed
- `/debug`, `/api/docs`, `/swagger`, `/actuator/health`
- Verbose error messages with stack traces
- Database error exposure in responses

### 2. Directory Listing
- Directory listing enabled on web servers
- Backup files exposed (.bak, ~, .swp)
- Git folder exposed (.git/config, .git/HEAD)

### 3. Source Code Disclosure
- Minified source maps (.map files)
- Backup files with source code
- IDE configuration files (.idea, .vscode)

### 4. Sensitive Data in Responses
- API responses include internal IDs, email addresses
- PII in logs or error messages
- Token/secret in URL parameters

## Defensive Checklist
- [ ] Disable debug endpoints in production
- [ ] Implement generic error messages
- [ ] Disable directory listing
- [ ] Set proper security headers
- [ ] Audit API responses for sensitive data
- [ ] Scan for exposed files periodically
"""
,
    "file-upload-bugs.md": """---
title: File Upload Vulnerability Patterns
description: Common file upload security vulnerabilities.
created: {date}
tags:
  - hackerone
  - file-upload
  - summary
---

# File Upload Vulnerability Patterns

## Common Vulnerability Patterns

### 1. Content-Type Bypass
- Attacker modifies Content-Type header to bypass validation
- MIME type sniffing by browser leads to XSS

### 2. Path Traversal in Filename
- Filename contains ../ to write outside upload directory
- Archive extraction creates files outside target dir (Zip Slip)

### 3. Unrestricted File Upload
- Executable files uploaded (.php, .jsp, .war)
- SVG upload with embedded scripts (XSS)

### 4. File Size / Resource Abuse
- No file size limit → disk exhaustion
- Multiple large parallel uploads → DoS

### 5. Storage-Based Attacks
- Uploaded files served from same domain → cookie theft
- Direct access to uploaded files without authorization

## Defensive Checklist
- [ ] Validate file content, not just content-type
- [ ] Generate random filenames, preserve extension safely
- [ ] Restrict executable file extensions
- [ ] Set file size limits
- [ ] Serve uploads from separate domain/CDN
- [ ] Scan uploads for malware
- [ ] Use anti-virus / sandbox for suspicious files
"""
,
    "access-control-bugs.md": """---
title: Access Control Vulnerability Patterns
description: Common access control and authorization bypass patterns.
created: {date}
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
"""
}


def write_file(filepath: Path, content: str):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    log.info(f"  Created: {filepath.name}")


def write_taxonomy(filepath: Path, template: str, date: str):
    content = template.format(date=date)
    write_file(filepath, content)


def write_summary(filepath: Path, template: str, date: str):
    content = template.format(date=date)
    write_file(filepath, content)


def main():
    parser = argparse.ArgumentParser(description="Generate security taxonomy Markdown files.")
    parser.add_argument(
        "--taxonomies-dir",
        default="security-brain/hackerone/taxonomies",
        help="Taxonomy output directory (default: security-brain/hackerone/taxonomies)",
    )
    parser.add_argument(
        "--summaries-dir",
        default="security-brain/hackerone/summaries",
        help="Summary output directory (default: security-brain/hackerone/summaries)",
    )
    args = parser.parse_args()

    taxonomies_dir = Path(args.taxonomies_dir)
    summaries_dir = Path(args.summaries_dir)

    today = datetime.utcnow().strftime("%Y-%m-%d")

    log.info("=" * 50)
    log.info("Security Taxonomy Generator")
    log.info("=" * 50)
    log.info(f"Taxonomies: {taxonomies_dir.resolve()}")
    log.info(f"Summaries:  {summaries_dir.resolve()}")
    log.info("")

    # Write taxonomy files
    log.info("Writing taxonomy files...")
    taxonomy_files = {
        "bug-classes.md": BUG_CLASSES,
        "root-causes.md": ROOT_CAUSES,
        "testing-methodology.md": TESTING_METHODOLOGY,
        "remediation-patterns.md": REMEDIATION_PATTERNS,
    }
    for name, template in taxonomy_files.items():
        write_taxonomy(taxonomies_dir / name, template, today)

    # Write summary files
    log.info("Writing summary files...")
    for name, template in SUMMARIES.items():
        write_summary(summaries_dir / name, template, today)

    log.info(f"\nDone! Created {len(taxonomy_files)} taxonomies and {len(SUMMARIES)} summaries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
