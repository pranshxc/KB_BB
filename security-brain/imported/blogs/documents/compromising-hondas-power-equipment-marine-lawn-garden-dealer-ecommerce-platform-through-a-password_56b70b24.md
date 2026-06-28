---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-06_compromising-hondas-power-equipment-marine-lawn-garden-dealer-ecommerce-platform.md
original_filename: 2023-06-06_compromising-hondas-power-equipment-marine-lawn-garden-dealer-ecommerce-platform.md
title: Compromising Honda’s power equipment / marine / lawn & garden dealer eCommerce
  platform through a vulnerable password reset API
category: documents
detected_topics:
- api-security
- access-control
- password-reset
- sso
- command-injection
- path-traversal
tags:
- imported
- documents
- api-security
- access-control
- password-reset
- sso
- command-injection
- path-traversal
language: en
raw_sha256: 56b70b2482a9a8334c93276a9328a463d84812dbf3d97592f112e15a67f50916
text_sha256: 2f29e27b74462ff2fc136a8c9c9b136664759db79081b99f0cece47d0e8a410a
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Compromising Honda’s power equipment / marine / lawn & garden dealer eCommerce platform through a vulnerable password reset API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-06_compromising-hondas-power-equipment-marine-lawn-garden-dealer-ecommerce-platform.md
- Source Type: markdown
- Detected Topics: api-security, access-control, password-reset, sso, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `56b70b2482a9a8334c93276a9328a463d84812dbf3d97592f112e15a67f50916`
- Text SHA256: `2f29e27b74462ff2fc136a8c9c9b136664759db79081b99f0cece47d0e8a410a`


## Content

---
title: "Compromising Honda’s power equipment / marine / lawn & garden dealer eCommerce platform through a vulnerable password reset API"
url: "https://eaton-works.com/2023/06/06/honda-ecommerce-hack/"
final_url: "https://eaton-works.com/2023/06/06/honda-ecommerce-hack/"
authors: ["Eaton Z. (@XeEaton)"]
programs: ["Honda"]
bugs: ["Password reset", "Broken Access Control", "Account takeover"]
publication_date: "2023-06-06"
added_date: "2023-06-06"
source: "pentester.land/writeups.json"
original_index: 1076
---

# Compromising Honda’s power equipment / marine / lawn & garden dealer eCommerce platform through a vulnerable password reset API

![](/assets/images/ew-logo-4circle-48.png?cb=64e21a35) Eaton • Jun 6, 2023

Copy Link Share 

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/96643ae9-93d5-45d0-523d-2bd10c76da00/full)

**News coverage:**

  * [The Record](https://therecord.media/honda-power-equipment-marine-web-platform-vulnerability)
  * [Bleeping Computer](https://www.bleepingcomputer.com/news/security/honda-api-flaws-exposed-customer-data-dealer-panels-internal-docs/)
  * [SecurityWeek](https://www.securityweek.com/vulnerabilities-in-honda-ecommerce-platform-exposed-customer-dealer-data/)
  * [The Hacker News](https://thehackernews.com/2023/06/password-reset-hack-exposed-in-hondas-e.html)

## **Key Points / Summary**

  * I compromised Honda’s power equipment / marine / lawn & garden dealer eCommerce platform by exploiting a password reset API that let me easily reset the password of any account.
  * Broken/missing access controls made it possible to access **all** data on the platform, even when logged in as a test account.
  * Full admin-level access achieved with access to: 
  * 21,393 customer orders across all dealers from August 2016 to March 2023 – this includes customer name, address, phone number, and items ordered.
  * 1,570 dealer websites (1,091 of those are active). It was possible to modify any of these sites.
  * 3,588 dealer users/accounts (includes first & last name, email address). It was possible to change the password of any of these users.
  * 1,090 dealer emails (includes first & last name).
  * 11,034 customer emails (includes first & last name).
  * Potentially: Stripe, PayPal, and Authorize.net private keys for dealers who provided them.
  * Internal financial reports.
  * **Important:** This hack did not impact Honda’s automobile business. Only the power equipment / marine / lawn & garden business. Honda vehicle owners should not be concerned – only those who purchased other Honda products online.

After successfully breaching Toyota’s systems a [few](https://eaton-works.com/2023/02/06/toyota-gspims-hack/) [times](https://eaton-works.com/2023/03/06/toyota-c360-hack/) late last year, I wanted to try my hand with a fresh automaker target. A question many have asked me lately is, “Why Toyota?” The answer is, my family has driven Toyota vehicles for as long as I remember, so when thinking of an automaker, Toyota was one of the first names that came to mind. Today’s writeup is about Honda. Why Honda? A good friend of mine’s family loves Honda vehicles, so I thought if I found an interesting vulnerability, it would make for a fun conversation topic.

When you think of Honda, you probably think of their cars like the Civic and Accord, but they also sell generators, lawn mowers, snow blowers, outboards, propellers, and more. Much like the cars, these power equipment / marine / lawn & garden products are sold through dealers. Since at least 2016, Honda has maintained an eCommerce platform called Honda Dealer Sites that allows dealers to easily create a website/storefront to sell Honda products.

## **Honda Dealer Sites**

If you are the owner of a hardware store or marina and want to sell Honda products, you will find yourself looking into Honda Dealer Sites. The platform features a website builder to help you establish your web presence and also takes care of product ordering and fulfillment. A short video overview of the platform is here:

This is a closed-registration platform and requires a Honda dealer number to establish an account. You used to be able to view more information about the platform on [hondadealersites.com](http://hondadealersites.com/), but Honda took it down as part of vulnerability remediation and it currently redirects to the power equipment information site. It might return in the future.

Here are 2 real examples of the platform in action:

  1. Ace Hardware is a well-known hardware store chain. Here is a store in Atlanta that sells Honda products: <https://www.batesace.com/>. At the time of writing, there is a “Honda Store” link in the header that points to their Honda-hosted dealer site: <https://batesace.powerdealer.honda.com/>.
  2. Here’s an example of a marine dealer site for The Washington Marina in DC: <https://washingtonmarina.powerdealer.honda.com/>

There are almost 1,600 of those sites – around 1,100 of those are active. Just Google [“powerdealer.honda.com”](https://www.google.com/search?q=%22powerdealer.honda.com%22) to find them.

Customers can view and order products on these dealer sites and have them shipped or reserved for in-store pickup. The Honda eCommerce platform handles all this so dealers don’t have to hire a developer to design their own in-house ordering/payment flow.

## **The Admin Dashboard**

As an owner of a Honda dealer site, you are provided an admin dashboard: <https://admin.pedealer.honda.com/>. It is an [Angular](https://angular.io/) single-page-application. You log in to this dashboard using your username and password and then you can create/edit your website, view customers/orders, etc. The login page is rather generic, but the title of the web page, Honda Dealer Website Admin, made me consider it priority target.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/3b678ac7-4a87-4bc5-0323-bdf145eac300/full)

There is no option to create an account, nor is there any API in the JavaScript code to do so. With that out of the picture, I investigated the possibility of taking over an existing account. With that, there are 2 unique challenges:

  1. Finding a valid email actually registered in the system.
  2. Gaining access to the account.

## **The Vulnerability**

My analysis of the admin dashboard did not reveal any obvious login or password related vulnerabilities. To reset the password, you fill out the reset password form on the “Forgot Password?” page and it would send those same fields to the API, which would trigger a password reset email to be sent.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/65465a50-5d54-4b2c-beae-b8e62a62bd00/full)

This wouldn’t actually reset the password until you followed the instructions in the email, so this seemed like a dead end.

I redirected my focus to other Honda sites. I came across a different site named PETE (Power Equipment Tech Express). My analysis of this website revealed a very similar JavaScript codebase. I concluded PETE was part of the same eCommerce site network, and that an account that worked on this site might also work on the main admin dashboard.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/b235a2ca-0943-47a5-f784-a8bdd7587900/full)

The password reset mechanism on the PETE site appeared to work the same way and required the same information to trigger a password reset email, but there was one thing different – it had an API to actually reset the password.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/bf64ee36-3192-4437-c137-e97186c7ac00/full)

This API does not exist on the admin dashboard site, and you would only notice it by digging into PETE’s JavaScript code. It’s possible it was an older API that was not removed from this particular site. The problem with this API was that it allowed you to reset an account’s password by just knowing the username/email. You did not have to provide the current password or even a token from a password reset email. If you knew an account’s email, you could theoretically reset its password and log in to it.

To test this theory, I had to find a valid email. A concern I had was that I could cause real disruption to a real dealer by locking them out of their account, so I had to consider further action carefully. The breakthrough came in the form of a YouTube video published just a month prior. I found a link to it in the admin dashboard’s JavaScript code:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/b6a2f8a1-fd6d-4272-5626-89a57c606600/full)

It was a webinar explaining the platform to dealers. Importantly, it revealed a login email address. Even better, it was a test/sample account, so I could reset it without causing a disruption to real dealers.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/f3c592ee-8462-46f4-ac38-f488069d3100/full)_This video was deleted from YouTube by Honda as part of vulnerability remediation._

The last step was to set up an HTTP request to the resetpassword API and test if it really worked. It did work and the password was successfully reset!

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/a424d8e9-0ce5-4104-7fd4-ceee6f7f1400/full)_See that Password field in the response? I don’t know why they were returning it or how it’s encoded. Decoding that as base64 does**not** yield the password. If you can figure it out, let me know in the comments! AOtE/+yvAWdxllZ42ASjyz8/s1HcYCyk+/b5kUc88gVVPX94T5ye+BbFaD6befJrJQ==_

## **Accessing all platform data**

With the test account’s password reset I could log into the account, and this is what I saw:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c634edd1-bd4e-46fb-aa2d-a2e1e1c5d600/full)

I had achieved a basic foothold in the network, but all I was seeing was sample data created for the YouTube video. The next step was to attempt to escalate access to data in other accounts or achieve admin access.

The password reset vulnerability was significant and now I knew that if I found a real dealer email, I could easily gain access to their account. However, that would potentially be disruptive to their business, so I avoided doing that and instead tried to find another less disruptive exploit.

The next breakthrough was shockingly simple. This platform assigns numeric IDs to everything from orders to sites. The IDs were sequential so just adding +1 to the current ID would bring you to the next record. Each dealer site was assigned an ID and that was shown in the browser address bar. I found that by changing that ID, I could access another dealer’s dashboard:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/d213a012-30a9-46ee-314f-9d8a1813f700/full)_Real customer orders for[Honda East](https://www.hondaeastcincy.com/) seen as recent as the week prior!_

Just by incrementing that ID I could gain access to every dealers’ data. The underlying JavaScript code takes that ID and uses it in API calls to fetch data and display it on the page. Thankfully, this discovery rendered the need to reset anymore passwords moot.

I could click into any order and see the details, with some customer information:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/06b01d1a-8037-4f3a-aa65-ca1938f39200/full)

That didn’t show all the customer information, however if you look at the API response, you can find the rest of it:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/52047199-232a-4316-cf1a-fb1a60a34b00/full)

A quick tour showing what else I had access to on the dealer’s dashboard:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/110a83fa-bdc6-42cc-963b-68a6c33c3600/full)_All their customer emails_

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/f03cc62c-27d6-4053-ccba-c76cfcfbf900/full)_Ability to edit their website_

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/040afbaa-5e9c-4f2a-e28e-d637b5bd3a00/full)_Ability to edit products they have for sale_

## **API Keys**

Only after I reported to Honda did I notice it may have been possible to view API keys for dealers who provided them. Dealers can provide their API keys to process customer payments using their desired payment gateway. Supported payment gateways are Stripe, PayPal, and Authorize.net. To get the API keys it is necessary to send a specific API request to get the dealer site information. Since access to the site was blocked to me at this point, I couldn’t check how many dealers had provided API keys, but if they did, they would have been viewable:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/30c4058d-0bae-4e44-586a-5c5aa74a8100/full)

## **The Admin Dashboard**

While this was an admin dashboard for dealers, there were clues in the JavaScript code that pointed to an admin dashboard within the admin dashboard that is used by Honda themselves to control the platform and view data. To trick the site into thinking I am admin, I intercepted the login response and changed “isadmin” to true:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/4e6c56b4-6b6f-40ba-7d6b-92d747f40300/full)

After letting the modified response pass through, I was put into the admin dashboard that gave me an overview of the network. It shows the 3 tiers of Honda Dealer Sites subscriptions, how many dealers are subscribed, and the total amount the network is making in subscription fees per month. Out of respect for Honda, these figures will not be publicly disclosed.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/0ef5252f-34fc-46db-0cf4-9297df9e2000/full)_Note that due to a quirk of the API, the Dealer Sites section only lists sites the test account is assigned, but it’s still possible to access any dealer’s information through the URL trick. I also could have assigned the test account to all dealer sites to get this section fully populated, but that was unnecessary, and I wanted to keep write operations to a minimum._

A quick tour showing what else I had access to on the dealer’s dashboard:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c3b10faf-a4f1-44e6-5495-cd8666ba9800/full)_All customer emails_

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c3b10faf-a4f1-44e6-5495-cd8666ba9800/full)_All dealer emails_

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/2348430b-a9e6-4523-b762-f52a79a79c00/full)_Financial reports_

## **Impact**

There are several ways a threat actor could have exploited Honda’s eCommerce network for their own gain. They could of course leak all the customer and internal data – that would be embarrassing for Honda and frustrating for customers, but that would ensure the exploit is quickly found and fixed. Smart, financially motivated hackers could have used this exploit to illegally profit from the network with little risk of detection.

With access to more than 21k customer orders, highly targeted phishing campaigns could be created to trick customers into providing even more valuable data, or to try and install malware on their devices. Another possibility would have been to check for new Honda orders every day and send phishing emails to customers disguised as “Register your new Honda product” or “You mistyped your credit card number, click here to correct it”.

The most significant issue I can think of is the access to the dealer sites. There are more than 1k active sites that could have been covertly updated to add malicious code such as cryptominers and credit card skimmers. Of course, it’s possible some astute dealers may discover such website changes, but they might chalk it up to themselves being hacked and change their dealer account password. Unfortunately, there is nothing any dealer could have done to protect their store from this attack.

## **Other Sites**

This eCommerce platform is a network of sites. It turns out the API _does_ verify your access to specific sites, but only when logging in. The admin dashboard has a User Management section where you can edit any dealer user and assign their access:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/bd59a9c1-499f-4405-019e-3270796d9100/full)

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/585b537f-88bb-4118-c211-7123a6f3a900/full)

When I logged in to some sites, it would fail and show a message saying I did not have access. Fortunately, I found a simple workaround – intercept the login HTTP response and replace the error response with the success response from the admin dashboard login. The success response contains the access token for the underlying API. Once the login was faked to be successful, the sites could be accessed without any restrictions, further expanding the reach of the access token. Here are a few screenshots of sites I successfully got into. I believe there are many more out there based on the user roles that can be assigned:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/76e12371-18bf-4cf8-1d4a-fbab4dd61600/full)[hondapromosignup.com](https://www.hondapromosignup.com/)

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/6b65bb55-0a4b-4588-f617-16918efde900/full)[oem.engines.honda.com](https://oem.engines.honda.com/)

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/52415004-c64d-4c28-da71-03f643df0f00/full)[pesalesportal.com](https://pesalesportal.com/)

## **Reporting to Honda**

Honda’s official stance regarding security reports is the following:

_“If a researcher believes that they have discovered a vulnerability with our systems, they are invited to contact our customer service office to document their observations at 1-800-999-1009.”_

It’s hard to send images and links over the phone, so I looked for a different way to report the problems.

[Karn Dhingra](https://www.autonews.com/author/karn-dhingra), a reporter for Automotive News who has covered my previous exploits with Toyota, graciously provided me with his PR contact. I wrote up my report and sent it March 16, 2023, at 8 AM EST. Honda responded to me at 1:26 PM and by then the entire network of sites had been closed for maintenance:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/59d5d6fc-4506-4f3a-3375-36b607a02e00/full)

Honda confirmed to me on April 3, 2023, at 7:18 PM EST that they had completed their investigation and had returned all sites to service. Their full statement:

“ _Thank you again for letting us know about the observed issues with the Power Equipment & Marine sites. As you know, Honda quickly isolated access to the sites, and we subsequently updated the sites’ security measures. All of the sites have now returned to service. At this time, Honda is not aware of any use of this vulnerability to access sensitive consumer or dealer information stored on the sites or of any malicious activity._

_We really appreciate receiving your notice about the potential vulnerabilities, which allowed us to take quick action to resolve the issues._ “

I asked about the possibility of a vehicle or cash reward given the severity of the issue, but Honda does not currently have a bug bounty or mechanism to provide a reward. As a result, **no reward was given for this report**. As Karn previously wrote [here](https://www.autonews.com/mobility-report/automakers-risk-cyberattacks-paying-white-hat-hackers-less), automotive companies should increase rewards to security researchers in order to incentivize good-faith reporting like this. Data breaches are only getting bigger and more frequent, and this was another one just waiting to happen.

Despite receiving no reward, I was glad to help stop a major data breach before it happened. Honda’s response was exceptional, and they deserve praise for taking the affected sites offline quickly and applying proper fixes. I hope in the future they establish a bug bounty or at least set up a dedicated security email inbox.

## **Lessons / Takeaways**

If you’re a web application or API developer, there are 3 primary lessons to learn from this:

  1. **Implement password resets correctly.** When resetting a password, the most common method is to send an email to the user containing a URL + token they can go to in order to proceed with the reset ([more information](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)). Also ensure you don’t accidentally introduce a backdoor to this process, like an insecure admin API to reset a user’s password.
  2. **Implement proper access controls.** This was textbook example of [OWASP A01:2021 – Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/). Every token issued by the authentication service could be used to access any API endpoint without restriction, provided you knew where to look / how to query the APIs. You could also access another dealer’s dashboard just by changing the ID in the URL. Make sure all access/login tokens are properly scoped and don’t provide users with access to data they don’t need.
  3. When making a single-page-application in React or Angular, be careful! As you build the application, remember your visitors’ browsers will see all your code, so be mindful what you include in the code. Code comments should not be presumed safe either!
