---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '190373'
original_report_id: '190373'
title: Gratipay uses the random module's cryptographically insecure PRNG.
weakness: Cryptographic Issues - Generic
team_handle: gratipay
created_at: '2016-12-11T15:49:45.330Z'
disclosed_at: '2016-12-12T17:07:22.677Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- cryptographic-issues-generic
---

# Gratipay uses the random module's cryptographically insecure PRNG.

## Metadata

- HackerOne Report ID: 190373
- Weakness: Cryptographic Issues - Generic
- Program: gratipay
- Disclosed At: 2016-12-12T17:07:22.677Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Dear Gratipay bug bounty team,

# Summary
---

Gratipay currently uses the [random](https://docs.python.org/dev/library/random.html) module's pseudo-random number generator which is not a cryptographically secure PRNG as stated in the docs:

> The pseudo-random generators of this module should not be used for security purposes. For security or cryptographic uses, see the secrets module.

The PRNG is implemented in `crypto.py` as follows:

~~~
try:                                # use the system PRNG if possible
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:         # fall back
    import warnings
    warnings.warn('A secure pseudo-random number generator is not available '
                  'on your system. Falling back to Mersenne Twister.')
    using_sysrandom = False
~~~

Link: https://github.com/gratipay/gratipay.com/blob/master/gratipay/security/crypto.py#L17

# Why does this vulnerability exist?
---

A PRNG is an algorithm used to produce random-looking numbers with certain desirable statistical properties. In order for a PRNG to be cryptographically secure it must be resistant to prediction.

The random module uses the [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) by default, which is designed for simulation (Monte-Carlo simulation) and modelling, and is therefore not suitable for cryptographic purposes. Interestingly Gratipay's current fallback from the `random` module is in fact the Mersenne Twister:

~~~
 warnings.warn('A secure pseudo-random number generator is not available '
                  'on your system. Falling back to Mersenne Twister.')
~~~

# How can this be fixed?
---

I recommend using the [secrets](https://docs.python.org/dev/library/secrets.html#secrets.SystemRandom) module's PRNG as follows:

~~~
random = secrets.SystemRandom()
~~~

For more on `Insecure Randomness` please refer to the OWASP page here: https://www.owasp.org/index.php/Insecure_Randomness

Yours sincerely,
Ed

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
