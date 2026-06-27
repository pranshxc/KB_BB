---
title: Security Testing Methodology
description: Structured methodology for security testing, code review, and vulnerability assessment.
created: 2026-06-26
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
