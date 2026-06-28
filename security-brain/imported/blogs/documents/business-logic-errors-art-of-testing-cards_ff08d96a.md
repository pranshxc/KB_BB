---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-04_business-logic-errors-art-of-testing-cards.md
original_filename: 2022-05-04_business-logic-errors-art-of-testing-cards.md
title: Business Logic Errors - Art of Testing Cards
category: documents
detected_topics:
- business-logic
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- business-logic
- command-injection
- otp
- rate-limit
language: en
raw_sha256: ff08d96a021a933da1ccb39a19bb2c0670bc9caba184e66bf9ee3066f4619e89
text_sha256: ed83f3506c913d6e1a397bee639d8e3f71d1b64d80a3931302a5c1cc9b98026d
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Errors - Art of Testing Cards

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-04_business-logic-errors-art-of-testing-cards.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `ff08d96a021a933da1ccb39a19bb2c0670bc9caba184e66bf9ee3066f4619e89`
- Text SHA256: `ed83f3506c913d6e1a397bee639d8e3f71d1b64d80a3931302a5c1cc9b98026d`


## Content

---
title: "Business Logic Errors - Art of Testing Cards"
url: "https://shahjerry33.medium.com/business-logic-errors-art-of-testing-cards-4907cfb46a57"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Payment bypass", "Logic flaw"]
publication_date: "2022-05-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2666
scraped_via: "browseros"
---

# Business Logic Errors - Art of Testing Cards

Business Logic Errors - Art of Testing Cards
Jerry Shah (Jerry)
Follow
6 min read
·
May 4, 2022

231

1

Press enter or click to view image in full size

Summary :

Business logic errors will allow you to manipulate the business logic of an application. Sometimes business logic errors can have devastating effects on the applications. Business logic errors are difficult to find because they involve legitimate use of the application’s functionality. This kind of vulnerabilities are a way of using the legitimate processing flow of an application in a way that it results in a negative consequence to the organization.

Description :

I discovered this vulnerability where I was able to use the test card to purchase the premium subscription on the website. I used card number as 4242 4242 4242 4242, date as 10/23 and a random cvv number 333 to purchase the premium and I was successfully able to purchase it.

Many websites now a days has resolved this issue by implementing a check against test cards provided by https://stripe.com/docs/testing#cards but I have figured out a small bypass for those websites who has limit this fix. We can still use the test cards but this technique will be applied to few websites only. Instead of using the random numbers or the cards provided by https://stripe.com/docs/testing#cards, you can pick the test cards from https://www.fakenamegenerator.com/ and can check whether it works or not.

Limited Mitigation Code (Python) :

//Demo Code

print(“***Fake Card Testing***”)
print(“\n”)

//Insufficient Logic

fake_cards=(4242424242424242,4000056655665556,5555555555554444,2223003122003222 ,2223003122003222,5200828282828210,5105105105105100,378282246310005,371449635398431,6011111111111117,3056930009020004,3566002020360505,6200000000000005,4000002500001001)

card=int(input(“Enter Card Number : “))

if card in fake_cards:
print(“Payment Decline due to test card.”)
else:
print(“Payment Successful.”)

Press enter or click to view image in full size
Limited Fix Code

In the above code, a tuple (an array) has been created with some fake card numbers for identification so if the user uses any of this mentioned card numbers the payment will be declined.

Press enter or click to view image in full size
Payment Declined

But what if the card number used is not mentioned in the above created tuple (an array) ?

The user will still be able to use the test card and will be able to process the payments successfully.

Press enter or click to view image in full size
Payment Success

In the above mentioned screenshot I have used a test card number from https://www.fakenamegenerator.com/ to bypass the logic.

The above mentioned mitigation technique is known as blacklisting but it does not seems logical here as there are n number of cards and you cannot blacklist all of them and the same logic goes for whitelisting also. So the concept of blacklisting and whitelisting is not enough in this case, you need to chain it with other mitigation techniques. You also need to integrate the card’s databases with your system to check whether it is a fake card or not.

How I found this vulnerability ?

I went to my dashboard to upgrade my membership from basic to premium
Press enter or click to view image in full size
Membership Basic
Press enter or click to view image in full size
Opening in New Tab
Press enter or click to view image in full size
Upgrade Page

2. I selected the yearly plan

Press enter or click to view image in full size
Yearly Plan

3. I entered the details of a test credit card with billing address

Press enter or click to view image in full size
Test Card
Press enter or click to view image in full size
Test Billing Address

4. Then I clicked on Place Order button and the payment was processed successfully

Press enter or click to view image in full size
Place Order
Press enter or click to view image in full size
Payment Processed Successfully

5. I went to my dashboard to check for the premium membership and it was successfully purchased

Press enter or click to view image in full size
Premium Member

Why this happened ?

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In our opinion,

It happened because the payment gateway was in the test mode in the back-end and not in the production mode, though the website was in production mode.

Staging OR Pre-production OR Test mode :

Whenever the payment gateways are in the test mode they check into there local database (whitelisted) for the cards and as it is in test mode the local database contains test cards, so if the test card you entered is found in the local database it will successfully process the payment.

Production OR Live mode :

Whenever the payment gateways are in the live mode they check into the integrated databases of the respected cards. For example if you entered a test card of visa then the website will check into visa’s database, if the test card you entered is mastercard then the website will check into mastercard’s database because there databases are integrated with the website you are testing.

Press enter or click to view image in full size
Payment Flow - Test Mode vs Live Mode

The problem with the local database in test mode is that, that it does not provide any checks against the test cards that you use and gives you a successful payment while in live mode the check against the test cards is performed and the test card gets rejected.

Generated Error Messages in Live Mode :

Processing Error: Your card number is incorrect.

Processing Error: Your card was declined. Your request was in live mode, but used a known test card

Impact :

This kind of issues can lead to loss in business as the payments are being done successfully without paying any amount of money.

Calculated CVSS :

Vector String - CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:L

Score - 6.5 (Medium)

Mitigation :

There are various ways to mitigate this issue :

Avoid Test Modes in Payment Gateway :

Test modes does not perform security check against the test card and even if it does there are ways to bypass it. (https://www.fakenamegenerator.com/)

2. Implement Rate Limit :

Implementing rate limit mitigates the issue up to some point as it will block the card testing after the decided tries.

For eg.

An attacker uses a test card but it gets detected and he/she uses another test card which also gets detected, now at this point if rate limit is implemented an attacker will not be able to use n numbers of test cards, he/she will be blocked after 3 unsuccessful tries.

3. Update Database (Limited Fix) :

Update the database regularly that contains the test cards to perform checks against those test cards.

4. Token based check (My Opinion) :

Every original card should have its own token to check its authenticity.

For eg.

All the original visa cards should have there token as tok_visa

All the original mastercards should have there token as tok_mstcrd

All the original american express cards should there its token as tok_amex

So if an attacker is trying to use the test card, a back end check should be performed whether the entered card has the token or not and if it does not have the token then it should be rejected.

5. Balance and Payment checks (My Opinion) :

A check should be performed against the payment being done or not and if payment fails another check against card balance should be performed and if it also fails then the card should be rejected.

NOTE : Performing the check against card balance needs the integrated databases with the respected card companies.

Special thanks to Ashutosh Kumar for making me understand the back-end logic of test mode and live mode.

Press enter or click to view image in full size
