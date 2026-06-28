---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-02_why-you-shouldnt-use-a-password-manager-for-your-linode-account.md
original_filename: 2019-05-02_why-you-shouldnt-use-a-password-manager-for-your-linode-account.md
title: Why You Shouldn't Use a Password Manager For Your Linode Account
category: documents
detected_topics:
- cloud-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- cloud-security
- command-injection
- information-disclosure
language: en
raw_sha256: 892a8b427468a9f03c57a9fe78fbc6d7fc155678de6a014c42ecb49d95741678
text_sha256: 0bf3926133d4fa8a295eddbe45b8c1890c3c11f239f699a05a88b1be4a0572fb
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Why You Shouldn't Use a Password Manager For Your Linode Account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-02_why-you-shouldnt-use-a-password-manager-for-your-linode-account.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `892a8b427468a9f03c57a9fe78fbc6d7fc155678de6a014c42ecb49d95741678`
- Text SHA256: `0bf3926133d4fa8a295eddbe45b8c1890c3c11f239f699a05a88b1be4a0572fb`


## Content

---
title: "Why You Shouldn't Use a Password Manager For Your Linode Account"
page_title: "Why You Shouldn't Use a Password Manager For Your Linode Account – Utku Sen - Blog – computer security, programming"
url: "https://utkusen.com/blog/why-you-shouldnt-use-password-manager-for-linode.html"
final_url: "https://utkusen.com/blog/why-you-shouldnt-use-password-manager-for-linode"
authors: ["Utku Şen (@utkusen)"]
programs: ["Linode"]
bugs: ["Account takeover", "Information disclosure"]
publication_date: "2019-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5273
---

# Why You Shouldn't Use a Password Manager For Your Linode Account

02 May 2019 

**Update** : Linode security team said they reopened the issue.

**Update2** : Linode security team explained me that the initial assessment was done by HackerOne triage team. The issue was closed by them. Now, Linode security team discussing the issue internally.

I was trying to find an anomaly on popular password managers. After a while, I realized that the most popular password managers such as Lastpass, 1password, Dashlane are supporting form autofill on subdomains by default. Which means, when I use a password for example.com, my password manager will also fill app.example.com too. It’s a good feature for user experience. I shouldn’t write my password again and again for different subdomains such as mail.google.com, calendar.google.com etc.

But there is a catch. If a subdomain of google.com is compromised, an attacker can steal user credentials by tricking them to navigate to compromised subdomain. This is another risk factor for subdomain takeover vulnerabilities.

But wait a minute, what if the website provides us a subdomain itself? Like cloud companies who provides a reverse dns for user created servers. I checked my AWS and Azure accounts quickly.

**AWS** : main domain –> amazon.com / reverse dns domain –> amazonaws.com

**Azure** : main domain –> microsoft.com / reverse dns domain –> azure.com

No luck, they are aware of the risks. Digitalocean is not providing reverse dns (boo!), therefore I tried my luck with Linode. I started a server on Linode and checked the details:

![Linode](/blog/assets/linode2.png)

Linode provides us a reverse dns which is a subdomain of the linode.com domain. Because of that, it’s vulnerable to “Stealing Credentials From Password Manager by Abusing Autofill Function via Compromised Subdomain” (I’m open to name suggestions)

## Attack Steps

1) Target uses Lastpass for his/her Linode account:

![Linode](/blog/assets/linode1.png)

2) Attacker starts a server on Linode and creates a page with a login form with the same elements on linode.com
  
  
  <div class="form-control">
  <label for="username">Username</label>
  <div class="input-wrapper" data-qa-username>
  <input autofocus="autofocus" id="username" name="username" required type="text" value="">
  </div>
  </div>
  <div class="form-control">
  <label for="password">Password</label>
  <div class="input-wrapper" data-qa-password>
  <input id="password" name="password" required type="password" value="">
  

3) Attacker also embeds a Javascript code to the page which sends the autofilled data to an external server.
  
  
  I'M TOO LAZY FOR THAT JAVASCRIPT PoC
  

4) Attacker sends his/her crafted URL (blabla.members.linode.com) to the target. Target clicks the link and credentials autofilled by Lastpass, sent to an external server via the malicious javascript.

![Linode](/blog/assets/linode3.png)

## Fix?

Linode security team started to take actions to prevent this issue.
