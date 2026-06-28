---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-21_paypal-idor-via-billing-agreement-token-closed-informative-payment-fraud.md
original_filename: 2022-05-21_paypal-idor-via-billing-agreement-token-closed-informative-payment-fraud.md
title: PayPal IDOR via billing Agreement Token (closed Informative, payment fraud)
category: documents
detected_topics:
- idor
- jwt
- command-injection
- mfa
- otp
- api-security
tags:
- imported
- documents
- idor
- jwt
- command-injection
- mfa
- otp
- api-security
language: en
raw_sha256: 389b324fde2ca202b53129ab97d7f2ffce4d37deea75739e3713a80aa2a28a16
text_sha256: ec2bfdd39611a8e26a106b0d9ba5f4f9bf0bcf5d1fc8813a7eeb6894434bc6e9
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# PayPal IDOR via billing Agreement Token (closed Informative, payment fraud)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-21_paypal-idor-via-billing-agreement-token-closed-informative-payment-fraud.md
- Source Type: markdown
- Detected Topics: idor, jwt, command-injection, mfa, otp, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `389b324fde2ca202b53129ab97d7f2ffce4d37deea75739e3713a80aa2a28a16`
- Text SHA256: `ec2bfdd39611a8e26a106b0d9ba5f4f9bf0bcf5d1fc8813a7eeb6894434bc6e9`


## Content

---
title: "PayPal IDOR via billing Agreement Token (closed Informative, payment fraud)"
url: "https://medium.com/@h4x0r_dz/paypal-idor-via-billing-agreement-token-closed-informative-payment-fraud-3245202fab38"
authors: ["Souhaib Naceri (@h4x0r_dz)"]
programs: ["Paypal"]
bugs: ["IDOR"]
publication_date: "2022-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2622
scraped_via: "browseros"
---

# PayPal IDOR via billing Agreement Token (closed Informative, payment fraud)

Top highlight

PayPal IDOR via billing Agreement Token (closed Informative, payment fraud)
h4x0r_dz
Follow
4 min read
·
May 21, 2022

440

4

Summary:

Hello everyone, in this article I will show you an Insecure direct object references (IDOR) that I found on PayPal 7 months Ago where an attacker can expose PayPal users data: billing address,email, nonce code using billing Agreement Token.

A critical security issue in api.braintreegateway.com where I was able to create a PayPal transaction just by knowing billing Agreement Token of the users. the issue is That, this endpoint api.braintreegateway.com/merchants/<ID>/client_api/v1/payment_methods/paypal_accounts should be authenticated by the merchant. but the user can send post requests to this endpoint. and generate Payment Method Nonces.

I was reading the documents about Payment Method Nonces,

A payment method nonce is a secure, one-time-use reference to payment information. It’s the key element that allows your server to communicate sensitive payment information to Braintree without ever touching the raw data.

source: https://developer.paypal.com/braintree/docs/guides/payment-method-nonces

and I understand that, if I am able to get valid billing Agreement Token of another user I can generate a new Nonces code > make Payment!

proof of concept

I Reproduced this bug In a real merchant that uses Braintree which is grammarly.com. also,

go to https://www.grammarly.com/upgrade and log in with your account
Choose Your Plan, and select Paypal as the payment method, now make an intercept on
click on Paypal checkout, then accept the payment.
when you come to this request, drop it, to cancel the payment (And this way you won’t have to pay anything to Grammarly :’.
POST /api/v1/subscribe HTTP/1.1
Host: subscription.grammarly.com
Connection: close
Content-Length: 135
Cookie: <>
nonce=<nonce>&planId=1005&sessionId=<sessionId>&isTaxable=false&billingCountryCode=US

you can see Grammarly is use Payment Method Nonces and this Nonce can be generated in the unauthenticated endpoint.
back to burp history, and find this endpoint:

https://api.braintreegateway.com/merchants/68r2vzdxyjwst8d7/client_api/v1/payment_methods/paypal_accounts

send it to the repeater.

now to confirm the bug: open the victim Paypal account, repeat the same steps, and copy the billingAgreementTokenfrom victim account.

now change the billingAgreementToken in api.braintreegateway.com/merchants/68r2vzdxyjwst8d7/client_api/v1/payment_methods/paypal_accounts to the victim token.

Get h4x0r_dz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

note: 68r2vzdxyjwst8d7 is Grammarly public client ID .

Press enter or click to view image in full size

in the response, you will find that you are able to generate Nonces codes using billing Agreement Token for the victim. and no specific authentication is needed.

how an attacker can get the billingAgreementToken for other users?

now If you ask, how an attacker can get valid billingAgreementToken ! well there are tons of ways :

## 1. Wayback Machine

you can use these tools :

GitHub - tomnomnom/waybackurls: Fetch all the URLs that the Wayback Machine knows about for a…
Accept line-delimited domains on stdin, fetch known URLs from the Wayback Machine for *.domain and output them on…

github.com

GitHub - lc/gau: Fetch known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and…
getallurls (gau) fetches known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, Common Crawl, and…

github.com

https://web.archive.org/web/*/paypal.com/*

gau tool resultes : commend : gau paypal.com | grep "ba_token"

Press enter or click to view image in full size

and as you can see there are more soo many leaked billingAgreementToken in wayback machine. and this is because the billingAgreementToken is a public token :).

The next step for the attacker is to find the valid merchants that can accept one of these billingAgreementToken for example if one of these tokens is used in Grammarly, the attacker send the post request: https://api.braintreegateway.com/merchants/68r2vzdxyjwst8d7/client_api/v1/payment_methods/paypal_accounts

and in the response he will receive the user Paypal information, although the attacker needs to find the right merchants id and test all the tokens.

and this step is possible 100% , how many companies use Braintree Gateway? 1000 or 99999? The number is very limited :) .

2. google dork.

and because the billingAgreementToken is passed in GET request, you can find some of them on google using this dork , There isn't much :( .

Press enter or click to view image in full size
3. laked in 3rd party

also I found that the billingAgreementToken is leaked to Third-party for example Google Analytics

Press enter or click to view image in full size
the Impact

missing authentication In sansative endpint , an attacker can expose payapl user data : billing Address,email,nonce code using billing Agreement Token.

also this endpoint api.braintreegateway.com/merchants/<ID>/client_api/v1/payment_methods/paypal_accounts used to generate a valid Nonce code, and this code can be used to make a payment to the merchant.

an attacker can make payments from Paypal victim's accounts.

HackerOne triage response :

Press enter or click to view image in full size

for me , I Think this endpoint

https://api.braintreegateway.com/merchants/<ID>/client_api/v1/payment_methods/paypal_accounts

must be authenticated, the only ones who should have access to this endpoint should be the merchants using his API keys because there are so many authentication endpoints on api.braintreegateway.com and this one should be the same.
