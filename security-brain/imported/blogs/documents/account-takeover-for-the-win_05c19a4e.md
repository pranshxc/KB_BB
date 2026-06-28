---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-24_account-takeover-for-the-win-.md
original_filename: 2020-08-24_account-takeover-for-the-win-.md
title: Account Takeover For The Win 🏆
category: documents
detected_topics:
- password-reset
- ssrf
- command-injection
- mfa
- otp
- api-security
tags:
- imported
- documents
- password-reset
- ssrf
- command-injection
- mfa
- otp
- api-security
language: en
raw_sha256: 05c19a4e95c0c68fa62e23aaa92ef75048b723c4ee90146bb8e64486f878f6a1
text_sha256: 4ceda8df258b54e44cce1f9cc4c119ae15c54ec2f931b8b2aec42a127f0e93e7
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover For The Win 🏆

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-24_account-takeover-for-the-win-.md
- Source Type: markdown
- Detected Topics: password-reset, ssrf, command-injection, mfa, otp, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `05c19a4e95c0c68fa62e23aaa92ef75048b723c4ee90146bb8e64486f878f6a1`
- Text SHA256: `4ceda8df258b54e44cce1f9cc4c119ae15c54ec2f931b8b2aec42a127f0e93e7`


## Content

---
title: "Account Takeover For The Win 🏆"
url: "https://medium.com/@ricardoiramar/account-takeover-for-the-win-e320ce83cdd9"
authors: ["Ricardo Iramar dos Santos (@ricardo_iramar)"]
bugs: ["Account takeover", "Broken authentication", "Password reset"]
bounty: "2,225"
publication_date: "2020-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4297
scraped_via: "browseros"
---

# Account Takeover For The Win 🏆

Account Takeover For The Win 🏆
Ricardo Iramar dos Santos
Follow
10 min read
·
Aug 24, 2020

157

2

TL;DR: This is about how I got Account Takeover (ATO) vulnerabilities on two big e-commerce companies and a bypass after the first fix for one of the issues with a nice exfiltration technique. These two companies have private bug bounty programs so I’m not allowed to reveal their names. 🤐

Press enter or click to view image in full size
Introduction

Every time that I need to do a penetration test in a web application I always start by understanding the business behind in order to find the feature with the biggest impact. Most of the time authentication related feature is my choice which some times lead to an ATO.

I think the ATO is underestimate by the developers when coding and even more by the testers when performing their penetration tests. I’m saying that because most of ATO that I found was actually a logical flaw which didn’t really require much technical skills. Basically it was just thinking a little bit out of the box. 📦

Out Of Scope

Let’s start from the worst part where I got a really simple ATO but the program decided to mark as out of scope.

I found this ATO in a private bug bounty program so I’m not allowed to reveal any information regarding the company so let’s call this company as Ecom Fake.

Everything started when I found a subdomain takeover under the webstore.ecomfake.de. There was a CNAME pointing webstore.ecomfake.de to internal.notreallyimportant.de and the root domain notreallyimportant.de was available to buy.

Press enter or click to view image in full size
Press enter or click to view image in full size

This is a common mistake where DNS administrators publish internal names on their external DNS which is supposed to be valid only in the internal network.

I don’t like to report only the subdomain takeover vulnerability since it could have a lot different impact and in this program they made clear subdomain takeover as out of scope. Because of that I decided to do a quick check on the application to use the subdomain takeover in a chain for another vulnerability with a nice impact.

In less than five minutes I was able to find out their cookies domain attribute were too permissive which means any logged user on www.ecomfake.de (main application) would send their cookies to the subddomain webstore.ecomfake.de under my control if the user access it.

Press enter or click to view image in full size

I didn’t create a PoC but it was quite easy for an attacker include some links under www.ecomfake.de or any other subdomain under ecomfake.de and get the session cookie from all the users who access the page with the malicious links.

The program initially closed my report with the following statement.

Thanks for finding the subdomain takeover, unfortunately, it is out of scope for this project. I will close this ticket as resolved so you don’t lose a point.

I replied back with the following comment.

The subdomain takeover is in the chain but it’s not the vulnerability that I’m reporting here.
I’m reporting the massive account takeover vulnerability which is possible only because of the cookie domain attribute is too permissive.

There was a long discussion which doesn’t worth to put here and in the end they fixed the subdomain takeover and close as resolved but not eligible for a bounty.

To avoid the same issue with other bug hunters I’ve suggested them to make the policy clear by including a text saying that any issue combined with subdomain takeover would be invalidated but they didn’t update the policy.

Regarding the permissive domain cookie issue they’ve informed me this is a “known generic issue” and they won’t fix it. 🤷‍♂️

Trying Again

I was really upset with their decision but I decided to try again the ATO by checking now their main application under www.ecomfake.com. Actually the authentication mechanism was exactly the same for all their stores around the globe.

It took some time but I found an security issue which I’ve already seen in other applications before. The “Forgot your password?” feature had a logical flaw allowing an attacker to takeover an user account. There were only two requirements for an successful attack:

The attacker needs to know the victim email and name.
The victim needs to be tricked to validated his own OTP.

The step by step process wasn’t so intuitive so I sent a video and also described the steps below.

Set any proxy tool like Burp in your browser.
Access https://www.ecomfake.com and perform the “Forgot your password?” using the victim email.
When the application ask for the OTP copy he latest URL the browser address bar.
Send an e-mail to the victim with the URL from the previous step. A real attacker would create a phishing email like “We detect a malicious activity in your account. Please reset your password clicking here.”
Keep refreshing the page multiple times from step 3 until get a different response. As soon as the victim provide the OTP code you will be actually loading the next step.
Provide the victim name and after that the new password before the victim. Note this can be easily automated with a python script in order to change the password before the victim since you can detect when the user has already provided the OTP by checking the response.
Login into the victim account with the new password.

On step 5 even if the user resend the OTP it’d work anyway. The key was trick the user to load the URL from step 3 and provide the OTP to reset his own password.

For the second time but now directly from Hackerone triagger I got the bad news below.

I believe the best course of action for this report is for you to self-close this report.

He also included some text explaining why I should self-close the report. One of them was this one below.

The policy page explicitly states that this report is out-of-scope as it requires social engineering/phishing a user to exploit.

I almost closed my report because it seems every time that I open a report the Hackerone triagger has the goal to disqualify it. Even though I tried to argument with the comment below.

The problem here is not the phishing attack but the security issue in how the forgot password feature was designed.
From my perspective the forgot password feature should never allow be started from one browser and get part of it process in a different browser session. My suggestion for the solution in this case is when the user access the site for the very first time he should get an anonymous session and any ID for any process must be tied to this session which would prevent this attack.
Even that take look the instructions from Ecom Fake regarding phishing attacks. In the video and text they are asking to the user o check if the domain is a real domain from Ecom Fake and in this attack it is from Ecom Fake. Why an user shouldn’t trust in a real URL from Ecom Fake? Actually it should trust and that’s why the security issue is on the “Forgot your password?” feature in this case.

In the end the Ecom Fake defined this ATO was a low severity issue and gave me the charity of US$125.

Get Ricardo Iramar dos Santos’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I’ve decided not working with this bug bounty program anymore. It just doesn’t worth the stress. 🙅‍♂️

Winner Winner Chicken Dinner!

After a few weeks the disaster described above I found a similar ATO in another company. This is another private bug bounty so let’s call this e-commerce company as Exemplo.

In this case the account recover feature through Google had a logical flaw allowing an attacker to start the process and by a phishing attack force the user to perform the required steps to finish the ATO attack. Let’s take a look in the attack step by step that I’ve sent to the bug bounty program.

1 . Let’s use the email victim@gmail.com as an example. Set up a browser with a proxy tool like Burp and access https://www.exemplo.com.br.

2 . Start the recover account process by providing the email victim@gmail.com.

3 . In the next screen enable Burp interception and click on account recover feature link.

4 . On Burp forward the first POST request and stop on the GET request to https://xpto.exemplo.com.br/authentication?id=%7Bid%7D&mail=victim%40gmail.com&redirect_url=%7Bredirect_url%7D.

Press enter or click to view image in full size

5 . Copy the URL from the GET described above and replace the redirect_url URL parameter with “https%3a//xpto.exemplo.com/xpto%3fgo%3dhttps%253a//exemple.com.ricardo-iramar.com”. In my case I’m using this open redirect vulnerability pointing to a subdomain under my domain so I’d be able to know when the victim is done with the required steps. This is not really required because it’d work anyway by providing any invalid exemplo.com subdomain. Don’t worry you are going to get in the next steps.

6 . Now it’s time to phishing by sending the URL created in the previous step to the victim with any interesting story.

7 . From another browser open the URL from the fake email above to simulate the victim access and try to recover the account using Google.

8 . If the user has already been logged on Google and previously approved the login on Exemplo this step is not required. If not the victim will need to login on Google.

9 . In this PoC the page will be redirected to https://exemplo.com.ricardo-iramar.com with doesn’t have any application returning 500 HTTP error. A real attack would redirect the user back to https://www.exemplo.com.br and the victim would never know what happened.

10 . If I was doing remote I’d know the user has finished the required steps by checking the access logs on https://exemplo.com.ricardo-iramar.com and after that it’s just a matter to disable the Burp intercept from step 4. Winner winner chicken dinner!

This ATO was almost the same from the previous one but it doesn’t required much user interaction. If the victim was already logged on Google/Gmail by just loading the malicious URL the ATO would work totally transparent.

The Exemplo company was very nice during the process and rewarded me with US$1400. 👍

Winner Winner Chicken Dinner Bypass!

After the fix the Exemplo company asked me to check if the security issue was properly fixed. I’ve checked and reported to them that I was unable to exploit in the same way that I was doing before but I noticed that maybe it could be exploited in a different way and I’d need more time to investigate.

Few weeks later I had some free time to play again with this ATO bypass and noticed they include an extra step to validate the user email provided by the making impossible to exploit using the open redirect that I was using before. Because of this extra step validation now it was required a specific URL ID parameter. Basically if I was able to get the URL ID parameter I’d be able to exploit similar from the last time. The big problem was how to get the URL ID parameter!

After some time checking other services provided by the same Exemplo company I saw an interesting service where I could host my own store under the same root domain. Let’s call this service as MyStore.

The MyStore had some nice features and integrations with “Google Analytics” services which gave me a really nice idea. Let’s check the attack step by step now with a ninja exfiltration technique that I’ve sent to the bug bounty program.

1 . In order to perform this attack first we need to create a fake account under https://www.exemplo.com.br (e.g. attacker@gmail.com).

2 . Now we need to activate the MyStore for the account created in the previous step and enable the Google Analytics feature.

3 . Take the victim email account (e.g. victim@gmail.com), set up a browser with a proxy tool like Burp and access https://www.exemplo.com.br.

4 . Start the recover account process by providing the victim email (e.g. victim@gmail.com) and click on continue button.

5 . In the next screen enable request and response Burp interception and click on forgot password link.

6 . On Burp forward the first POST request and stop on the response which will be a redirection (302 Found). Copy the redirected URL from the Location response header.

Press enter or click to view image in full size

7 . Paste the URL from the previous step in a text file in order to have a copy of it. Change the copied URL by replacing the redirect_url URL parameter with your MyStore URL created from the first steps. Note the entire redirect_url URL parameter could be URL encoded to hide the content from the victim.

8 . Go back to Burp, drop the response and any following requests to stop the account recover process.

9 . Now it’s time to phishing by sending the URL created in the previous step to the victim with any interesting story.

10 . From another browser instance open the URL from the fake email above to simulate the victim access and try to recover the account using Google.

11 . If the user has already been logged on Google and previously approved the login this step is not required. If not the victim will need to login on Google. In the end the victim will be redirected to the MyStore created in the first steps.

12 . As the attacker access your Google Analytics dashboard and go to “Realtime > Overview” on the left panel. Copy the URL parameters under “Top Active Pages” section.

Press enter or click to view image in full size

13 . Now is the real trick. Remember the original URL which we took a copy and pasted in a text file. Take the redirect_url URL parameter, decode it first and append the parameters extracted from Google Analytics.

14 . Load the URL from the previous step under the same browser where you started the recover account process. Winner winner chicken dinner again!

Since it was a bypass and required more user interaction the Exemplo company rewarded me with US$700. 😁

If you have any question or want to share any interesting technique please send an email to ricardo.iramar@gmail.com or contact me on twitter @ricardo_iramar.
