---
title: Password Reset Bug Patterns
description: Common vulnerability patterns in password reset functionality, derived from HackerOne disclosed reports.
created: 2026-06-26
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
