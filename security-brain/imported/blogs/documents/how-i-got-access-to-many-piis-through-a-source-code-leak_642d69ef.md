---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-05_how-i-got-access-to-many-piis-through-a-source-code-leak.md
original_filename: 2021-10-05_how-i-got-access-to-many-piis-through-a-source-code-leak.md
title: How I got access to many PIIs through a source code leak
category: documents
detected_topics:
- api-security
- oauth
- jwt
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- api-security
- oauth
- jwt
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 642d69ef7c3aa57791d818877d64f3be831313f5a45e21b863d48b2f179139fe
text_sha256: 0216ef2aa33184bcfd80050291625f43f0de42cf3c5bc88cbfe8beba99bf7eb9
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I got access to many PIIs through a source code leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-05_how-i-got-access-to-many-piis-through-a-source-code-leak.md
- Source Type: markdown
- Detected Topics: api-security, oauth, jwt, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `642d69ef7c3aa57791d818877d64f3be831313f5a45e21b863d48b2f179139fe`
- Text SHA256: `0216ef2aa33184bcfd80050291625f43f0de42cf3c5bc88cbfe8beba99bf7eb9`


## Content

---
title: "How I got access to many PIIs through a source code leak"
page_title: "How I got access to many PIIs through a source code leak – Supras.io"
url: "https://supras.io/how-i-got-access-to-many-piis-through-a-source-code-leak/"
final_url: "https://supras.io/how-i-got-access-to-many-piis-through-a-source-code-leak/"
authors: ["Supras (@LdrTom)"]
bugs: ["Information disclosure"]
publication_date: "2021-10-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3261
---

[0](https://supras.io/how-i-got-access-to-many-piis-through-a-source-code-leak/#respond)

# How I got access to many PIIs through a source code leak

Posted on [5 octobre 2021](https://supras.io/how-i-got-access-to-many-piis-through-a-source-code-leak/ "18 h 41 min") by [Supr4s](https://supras.io/author/supras/ "Afficher tous les articles par Supr4s")

Hi everyone !

My blog has been unpublished for almost a year now, so I needed a new post … Here is an write-up from a recent P1 found and exploited on an external bug bounty program which led to a leak of many PII (Personally Identifiable Information).

Table of Contents

Toggle

  * Recon time
  * Content discovery
  * Analyze time
  * DumpsterDiver
  * EarlyBird
  * Manual analysis
  * Playing with APIs
  * Validity
  * Headcache
  * Collab for win
  * PII’s time
  * To conclude

# Recon time

It all starts with a Slack notification that a new subdomain has popped up.

Browsing on it and thanks to [Wappalyzer](https://addons.mozilla.org/fr/firefox/addon/wappalyzer/), I quickly identify the technologies of the site: PHP, Apache2 and probably MySQL database. A classic web stack !

![](https://supras.io/wp-content/uploads/2021/10/wappalyzer.png)

## Content discovery

With [ffuf](https://github.com/ffuf/ffuf) and my custom wordlists, I decide to do some content discovery looking for juicy files and hidden directories.

ffuf allows via its _-e_ flag to fuzz specific extensions. No need to put them all (asp, aspx, jsp etc) knowing that our application is written in PHP.

> 
>  ffuf -mc all -c -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0" -u "https://crm.mytarget.com/FUZZ" -w ./my/wordlist -D -e js,php,bak,txt,html,zip,sql,old,gz,log,swp,yaml,yml,config,save,rsa,ppk -ac

After a few minutes, I came across a pretty juicy result :

![](https://supras.io/wp-content/uploads/2021/10/ffuf1.png)

Look at the size of the zip … time to download and analyze !

# Analyze time

After unzipping our dev.zip, I find no less than 14000 directory and 65000 files. Just this ! 🥲

Being a lazy sysadmin, it is out of the question to manually search each file for « suspicious » information. Before automating, I need to know what I want to look for :

  * Harcoded credentials
  * API key, token
  * Any other necessary information that could increase the impact

I chose two tools to complete these tasks : DumpsterDiver and EarlyBird.

## DumpsterDiver

![](https://supras.io/wp-content/uploads/2021/10/DumpsterDiver_logo-300x300.png)

[DumpsterDiver](https://github.com/securing/DumpsterDiver) is a fantastic tool written in Python that will allow us to analyze large volumes of data in search of secrets, API keys and other « possible » leaks. It has an incredible number of features and customization possible depending on what you want. In my case, I don’t have time to spend 3 hours on the documentation, it’s bounty fever, so let’s make it simple.

To install it :

> 
>  $ git clone https://github.com/securing/DumpsterDiver.git
>  $ cd DumpsterDiver && pip3 install -r requirements.txt

Time to launch it :

> 
>  $ python3 DumpsterDiver.py -p /my/directory/dev --exclude-files .png .jpeg .jpg >> ./dumpsterdiver-output.txt

And after a few hours of scanning (I cleaned the output) :

> 
>  [...]
>  
>  FOUND HIGH ENTROPY!!!
>  The following string: <API_KEY> has been found in /my/directory/dev/anotherdirectory/class/fixtures.sql
>  
>  FOUND HIGH ENTROPY!!!
>  The following string: <TOKEN> has been found in /my/directory/dev/anotherdirectory/class/fixtures.sql
>  
>  [...]

## EarlyBird

![](https://supras.io/wp-content/uploads/2021/10/GoEarlyBird-logo_sm-300x129.png)

[EarlyBird](https://github.com/americanexpress/earlybird) is an another fantastic tool written in go that deserves to be known. As indicated on their page, «  _EarlyBird is a sensitive data detection tool capable of scanning source code repositories for clear text password violations, PII, outdated cryptography methods, key files and more. It can be used to scan remote git repositories, local files or directories or as a pre-commit step._ »

To install it, nothing could be easier.

> 
>  $ git clone https://github.com/americanexpress/earlybird.git
>  $ cd early bird && ./build.sh && ./install.sh

A binary is then generated in _/usr/local/bin_.

> 
>  $ which go-earlybird
>  /usr/local/bin/go-earlybird

In my case, EarlyBird will be used to detect potentially hardcoded passwords in the source code. I will only load one module for this :

> 
>  $ go-earlybird --path=/my/directory/dev -enable password-secret | tee earlybird-output.txt

![](https://supras.io/wp-content/uploads/2021/10/earlybird.png)

## Manual analysis

While the scans were running, I was able to do a manual analysis of the application to learn more about this web app.

It was also necessary, as soon as the DumpsterDiver and EarlyBird scans were finished, to concatenate the results and sort out any false positives.

After a few more hours of work, here is what I had in my possession :

  * The web application is based on SugarCRM, a customer relationship management software.
  * I have an uploads folder, containing various product photos, customer invoices, delivery notes, shipping notes etc.
  * I have the credentials of the SQL database
  * I have administrator credentials for back-office access
  * I have many API keys, secret, token in my possession (spoiler: we will use them for the rest of the article)

So I have a nice P1 in my possession, but why stop there ?

![](https://media.giphy.com/media/12OTxgtyHG11QI/giphy.gif)

# Playing with APIs

## Validity

By manually analyzing the application, I realized that the SugarCRM and everything around it (stock management, shops, customers, orders etc) is linked to the APIs of Capillary Anywhere Commerce, provided by Capillary Technologies which publishes itself … SugarCRM.

To play with the APIs in question, you need three things :

  * Merchant ID
  * Public key
  * Secret

Following the [official documentation](https://capillary.github.io/ecom-api-document/), you can test the validity of a public key with the following call :

> 
>  $ curl https://www.martjack.com/developerapi/OAuth/Token/<PUBLIC_KEY>

If a JWT is returned, then the key is valid.

## Headcache

My credentials are valid, yay.

But that’s where the problem starts … Apart from the API call seen above, I can’t interact with the APIs despite everything that is [asked](https://capillary.github.io/ecom-api-document/#authentication-merchant-setup-on-admin-portal).

I can’t find any way to authenticate to the server : all I get is a 401 _Unauthorized_.

  * Pass the headers manually with curl
  * Using Postman
  * Analysis of the source code and APIs calls harcoded but my nulity in PHP caught up with me very quickly (No judgments: I can make a phpinfo appear)

![](https://media.giphy.com/media/11tTNkNy1SdXGg/giphy.gif)

## Collab for win

I let a few days go by to see if I had any other ideas while re-re-re-re-reading the APIs documentation.

And … I was still stuck.

Determined not to give up, I needed the help of someone better than me. Knowing his hacking skills, and having already discuss with him some time before on a private H1 program, I contacted [Shubs](https://twitter.com/infosec_au).

After exchanging about my problem, and after some source code analysis, he generated a few hours later a PHP script able to communicate with the Capillary APIs. While I spent several days on it … Collaboration is key, right ? 😏

## PII’s time

Now that we can interact in an authenticated way with the APIs, we can hit them to retrieve confidential information.

No need to list them all, only some are of interest to us.

Retrieve the list of all customers

> 
>  https://www.martjack.com/DeveloperAPI/Customer/<MERCHANT_ID>/All

Detailed information about a specific customer

> 
>  https://www.martjack.com/developerapi/Customer/<MERCHANT_ID>/<CUSTOMER_ID>

We can also :

Get order history

> 
>  https://www.martjack.com/developerapi/Order/History/<MERCHANT_ID>/

Get store informations

> 
>  https://www.martjack.com/developerapi/Store/Information/<MERCHANT_ID>/

Disable user account

> 
>  https://www.martjack.com/developerapi/Customer/DeActivation/<MERCHANT_ID>/<USER_ID>

And many more …

All of this allowed me to prove the impact and recover PIIs, which is what I wanted by playing the APIs

For thoses who are interested, the script used to interact with the APIs can be found [here](https://gist.github.com/infosec-au/2c4c6f6dd57a086931ed55b0aecaa07b). The output is in XML, it must then be parsed ( **grep -oPm1 « (? <=ValueYouWanted>)[^<]+ »** for example)

# To conclude

This was a really cool bug to exploit even though I swore a lot while working on it. Thanks to [Shubs](https://twitter.com/infosec_au) for his collaboration and [Hisxo](https://twitter.com/adrien_jeanneau) for reading the article before publication ! 🙃

If you liked it, don’t hesitate to share!

__[Infosec](https://supras.io/category/infosec/)
