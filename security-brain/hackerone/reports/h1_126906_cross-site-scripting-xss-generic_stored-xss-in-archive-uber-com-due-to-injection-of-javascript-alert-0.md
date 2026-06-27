---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126906'
original_report_id: '126906'
title: Stored XSS in archive.uber.com Due to Injection of Javascript:alert(0)
weakness: Cross-site Scripting (XSS) - Generic
team_handle: uber
created_at: '2016-03-30T14:26:17.893Z'
disclosed_at: '2016-05-09T22:31:09.417Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Stored XSS in archive.uber.com Due to Injection of Javascript:alert(0)

## Metadata

- HackerOne Report ID: 126906
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: uber
- Disclosed At: 2016-05-09T22:31:09.417Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

archive.uber.com is vulnerable to an XSS due to injection of Javascript:alert(0) as the ```download_url``` or the ```home_page``` in the ```setup.py``` when generating the ```.tar.gz```. As of [PEP 0470](https://www.python.org/dev/peps/pep-0470/), the ```download_url``` and ```home_page``` parameters are depreciated. 

An example of a setup.py that can exploit this is: 

``` python
from distutils.core import setup

setup(
    name='IgnoreMe_mime',
    version='1.0.2',
    author='David Dworken',
    author_email='david@daviddworken.com',
    packages=['IgnoreMe_mime'],
    home_page='Javascript: alert(0)',
    download_url='Javascript: alert(0)',
    url='http://pypi.python.org/pypi/IgnoreMe_mime/',
    license='LICENSE.txt',
    description='XSS!',
    long_description=open('README.rst').read(),
    scripts=['uberPip/nothing.py'],
)
```

As with #126197, my PoC will be active once you run the mirror process to update archive.uber.com from pypi. Conveniently enough,, it looks like this was historically exploited on pypi, so a PoC (not mine) is already hosted on archive.uber.com here: 

```
http://archive.uber.com/pypi/simple/ignore-me-1.0/
```

In order to see the alert(0) box you have to click on the link titled ```1 home_page```. This will work in all browsers as it is a persistent XSS rather than a reflected one. 

This XSS was inadvertently fixed by [PEP 0470](https://www.python.org/dev/peps/pep-0470/) which removed the ```download_url``` and ```home_page``` parameters. In order to fix this, all you have to do is upgrade the software you use to host the mirror since this was fixed upstream. 

Thanks,
David Dworken

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
