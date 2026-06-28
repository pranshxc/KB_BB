---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-08_vulnerabilities-in-online-payment-systems.md
original_filename: 2022-10-08_vulnerabilities-in-online-payment-systems.md
title: Vulnerabilities in Online Payment Systems
category: documents
detected_topics:
- sso
- command-injection
- business-logic
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- business-logic
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 456ee6754b26925b4fa1c677ea8ee69c47c3ad815b5cfb1d3ae88bac47e978c1
text_sha256: 6e88771f2dc17a3a93b1ad0fa63f08e766f17affef2ef19cbc6823b6d2a212f3
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities in Online Payment Systems

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-08_vulnerabilities-in-online-payment-systems.md
- Source Type: markdown
- Detected Topics: sso, command-injection, business-logic, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `456ee6754b26925b4fa1c677ea8ee69c47c3ad815b5cfb1d3ae88bac47e978c1`
- Text SHA256: `6e88771f2dc17a3a93b1ad0fa63f08e766f17affef2ef19cbc6823b6d2a212f3`


## Content

---
title: "Vulnerabilities in Online Payment Systems"
url: "https://medium.com/@claudio_moranb/vulnerabilities-in-online-payment-systems-edd2d3c06905"
authors: ["Claudio Moran"]
bugs: ["Payment bypass", "Payment tampering", "Logic flaw"]
publication_date: "2022-10-08"
added_date: "2022-10-08"
source: "pentester.land/writeups.json"
original_index: 2071
scraped_via: "browseros"
---

# Vulnerabilities in Online Payment Systems

Vulnerabilities in Online Payment Systems
Claudio Moran
Follow
6 min read
·
Oct 8, 2022

307

1

Press enter or click to view image in full size
Photo by Pankaj Patel on Unsplash

Years ago I was involved in security research and I was a consultant for some tech companies in my country. During that time I found many things but one that was very common was payment systems with implementation issues. If you are into the bug bounty world or if you own a site and want to improve its security, then this article is for you.

Backstory

I’ve always been interested in computer security. I learned how to use some tools including Burpsuite and some plugins in my browser. I know some code including Python and know quite a bit of cryptography. But I also know that is not enough.

There are many tools to find security issues. These are available also for developers so known vulnerabilities are hard to find. You also compete with other Pentesters and white hat hackers looking for a bounty so if there is something out there you have to be quicker than them. You also need to be lucky, to find a pot of gold.

When it comes to Payment systems; libraries, and SDKs are supported by the Payment Service provider, this means that if someone reports a vulnerability it will quickly get resolved and they will inform all of their users about it.

Then, Where Do you need to look?

This applies not only to Payments but probably to other implementations and the answer is: Where you know it is probably an in-house solution. This means it was built only for that website by an internal team.

Where to look

How the last recommendation applies to Payment systems?
Well, if the implementation is done using one single payment provider then developers usually follow the documentation or implement the SDK. The issue comes when a site needs a multi-channel Payment system, this means they had to implement their own system to process the approvals.

When I say multi-channel I mean they have more than one payment provider and it usually looks like this:

Another target is also pages that are present in many countries.
Why is that? If the same page is in more than one country they probably have the same back-end services for all of them providing a micro front-end for each location but also they probably have an API developed in-house to work as a switch to call local payment providers. Even the credit card switch won’t be the same for all countries.

Get Claudio Moran’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As you see in this case the vulnerabilities you may find are because of flaws in the logic or checkups and not the common back-doors found in libraries.

Vulnerabilities

Before we move forward there are a few things to know regarding websites where you can buy things.
If you are on a website that sells computers, even if you find a way to bypass the payment system, there are several other steps in the process. They may have a 2–3 Day Delivery timeline where they wait for the clearance of payments giving them time to catch all the fake transactions. If they don’t, they still may have an address that they delivered or they may have a signature so these types of sites may have technical issues but that doesn’t mean the whole transaction system is vulnerable depending on the steps required for delivery.
What makes a site vulnerable to an attacker is when they deliver the goods immediately: Concert tickets, Coupons, Gift cards, Computer games, or any type of DLC.

Price Change

The most common thing to look for is to change the checkout price before paying for the item. Note that sometimes is in several places and it is a matter of finding which one could impact the result. Sometimes in one request, as there might be several before you reach the actual payment provider, you may find it more than once in one single request, but that doesn’t mean all of them have to be changed, maybe one goes to the payment provider and the other ones don’t have to be change because they go back to the inventory system.

Buy fractions

Sometimes changing the amount of the item into a fraction (0.1 Computers for example instead of 1 Computer), which will impact the price as well, will lead the inventory system to check out for 1 whole item because is not able to sell a fraction of the product.

Press enter or click to view image in full size
Failure is a success

Another common thing to try is to change the payment failure page with the successful one. Usually, when the payment method is called, you see in the payloads the successful redirect URL and the one for failure, you may switch that and see what happens. You may also try to catch that when you cancel a payment and the browser redirects you back to the page, change the URL for a successful one using the proxy in Burpsuite. This works sometimes because the payload for a success page is the same as the one for a failure.

Payment conversion issue

This happens in pages that are using the same back-end to serve many countries.

Let’s say this page is in the US and Argentina and they share the same URL to access but you have to select the country. 300 Dollars is a lot of money but 300 Argentinian pesos are about 2 dollars.

First, you need to select your 300-dollar item from the US site and then checkout. At that time when you select the payment method you may see something like this in the source code:

Press enter or click to view image in full size

We can see the value for that option is “us_payment_method”. If we know the value of payments used in Argentina, then it is a matter of replacing it:

Press enter or click to view image in full size

When the site takes you to pay it will redirect you to an Argentinian payment provider. The problem is when they receive the number 300 they understand it as their local currency and they don’t think it is dollars, neither they try to convert that amount. That makes it vulnerable. The payment then can go on, it is a real payment, and when the site receives that back understands everything is fine and completes the transaction.

Look for free items
Press enter or click to view image in full size

Have you ever been to a page that gives free items? Sometimes you can add to your cart a courtesy item, maybe it is a free ticket for a concert, or maybe they created a free item to turn your package into a gift instead, or sometimes you see is a free computer game to download. If this happens check the code. You may find there is a special tag to turn this item into courtesy and changing a regular item into a freebie works.

I hope you like my article, and I hope it helps develop safer payment systems by doing the proper checks.
