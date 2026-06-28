---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-02_noauth-account-takeover-via-microsoft-oauth.md
original_filename: 2023-10-02_noauth-account-takeover-via-microsoft-oauth.md
title: 'nOAuth: Account Takeover via Microsoft Oauth'
category: documents
detected_topics:
- oauth
- command-injection
- cloud-security
tags:
- imported
- documents
- oauth
- command-injection
- cloud-security
language: en
raw_sha256: c6ecc6a656c826d0990aecdf51536bf3379f329ffd8311b22794fb9f77effb1f
text_sha256: 355869aa74691b4546b02fd0152e78196be44677fc2a1ccb3fe0412d4aa682ec
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# nOAuth: Account Takeover via Microsoft Oauth

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-02_noauth-account-takeover-via-microsoft-oauth.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `c6ecc6a656c826d0990aecdf51536bf3379f329ffd8311b22794fb9f77effb1f`
- Text SHA256: `355869aa74691b4546b02fd0152e78196be44677fc2a1ccb3fe0412d4aa682ec`


## Content

---
title: "nOAuth: Account Takeover via Microsoft Oauth"
url: "https://bibek-shah.medium.com/noauth-account-takeover-via-microsoft-oauth-cc653410b886"
authors: ["Bibek Shah"]
bugs: ["OAuth", "Account takeover"]
publication_date: "2023-10-02"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 731
scraped_via: "browseros"
---

# nOAuth: Account Takeover via Microsoft Oauth

nOAuth: Account Takeover via Microsoft Oauth
Bibek Shah
Follow
3 min read
·
Oct 2, 2023

173

4

Hi everyone, I want to share a cool and easy account takeover I recently found. I was able to perform a full account takeover via Sign In with the Microsoft feature. I hope you will learn something new in this one :)

The website had different ways to sign in using email, and Oauth providers like Google, Microsoft and Apple. There was recently a Misconfiguration discovered by Descope in Microsoft which can be found here. So, My target also had the Sign in Microsoft feature therefore I decided to test the nOauth vulnerability.

Prerequisites for attack

To test this vulnerability, the Attacker needs to create a Tenant organization in their Microsoft portal, which is free to create.

Go to your Azure portal and search for Azure Active Directory
Press enter or click to view image in full size

2. Click on Create New Tenant and choose Tenant type Azure Active Directory

Press enter or click to view image in full size

3. Give it some name and click on review and create, after that it will give you a captcha, solve it and it will take roughly a minute to create.

Press enter or click to view image in full size

4. Now you have created a Tenant, Click on Add > User > Create a new user.

Press enter or click to view image in full size

5. Fill details and make sure you remember the password.

Press enter or click to view image in full size

6. Click on the User section from left to show your created user.

Press enter or click to view image in full size

7. Now click on user you created, go to properties section and change email from contacts and click on save. Enter your victim email there, it can be any email.

Press enter or click to view image in full size

Now that all prerequisites required for the attack are completed, you can test sites for nOauth vulnerability.

Get Bibek Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Misconfiguration Takeover Testing Scenario

Victim: Sign up using the victim's email on the website using any sign options and verify the account if required.

Attacker:

Choose to sign in with Microsoft and use the email and password from the account you created above.
Press enter or click to view image in full size

2. Enter the details we created above in the Microsoft account login process and If this website is vulnerable you will get logged into the Victim account.

Simple, yet Critical leading to Account Takeover.

POC:

The company did not allow me to make it public ¯\_(ツ)_/¯. I will make sure to add it if any of them agree.

Why this happens:

Vulnerable sites use claims like email and preferred username which Microsoft warns not to use.

Press enter or click to view image in full size

Thanks for making it to the end. I hope you enjoyed this write-up.

If you have any questions, please DM me on Twitter.
