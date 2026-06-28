---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-11_we-hacked-github-for-a-month-heres-what-we-found.md
original_filename: 2023-02-11_we-hacked-github-for-a-month-heres-what-we-found.md
title: 'We Hacked GitHub for a Month: Here’s What We Found'
category: documents
detected_topics:
- mfa
- sso
- access-control
- password-reset
- otp
- business-logic
tags:
- imported
- documents
- mfa
- sso
- access-control
- password-reset
- otp
- business-logic
language: en
raw_sha256: 3a51f812c56bac474087ac6cc0e2dd91c587cf9004299333ff60dd0b5ca403e9
text_sha256: c8ab63ff6ba5fcc38dd1a876f62c53ed60664ad6b3d30f061df9a23c6c9ad56c
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# We Hacked GitHub for a Month: Here’s What We Found

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-11_we-hacked-github-for-a-month-heres-what-we-found.md
- Source Type: markdown
- Detected Topics: mfa, sso, access-control, password-reset, otp, business-logic
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `3a51f812c56bac474087ac6cc0e2dd91c587cf9004299333ff60dd0b5ca403e9`
- Text SHA256: `c8ab63ff6ba5fcc38dd1a876f62c53ed60664ad6b3d30f061df9a23c6c9ad56c`


## Content

---
title: "We Hacked GitHub for a Month: Here’s What We Found"
page_title: "We Hacked GitHub for a Month : Here’s What We Found – CyberXplore – Blog"
url: "https://blog.cyberxplore.com/we-hacked-github-for-a-month-heres-what-we-found/"
final_url: "https://blog.cyberxplore.com/we-hacked-github-for-a-month-heres-what-we-found/"
authors: ["Shivam Kumar Singh (@MrRajputHacker)", "Vansh Devgan (@Th3Pr0xyB0y)"]
programs: ["GitHub"]
bugs: ["Pre-account takeover", "Broken Access Control", "Email verification bypass", "Logic flaw"]
bounty: "10,000"
publication_date: "2023-02-11"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1546
---

![](https://blog.cyberxplore.com/wp-content/uploads/2025/06/STORY-OF-CVE.png)

# We Hacked GitHub for a Month : Here’s What We Found

June 15, 2025February 10, 2023 by [cyberxplore](https://blog.cyberxplore.com/author/cyberxplore/ "View all posts by cyberxplore")

After a long hiatus, we are back with a new write-up. Although we don’t typically participate in bug bounty programs due to other commitments, we took up the challenge of hacking GitHub for a month and are excited to share our findings. It all started when Shivam Singh (Mr. Rajput Hacker) reached out to me in November and encouraged me to try bug bounty. We decided to focus on npmjs.com, a subsidiary of GitHub. Despite the fact that GitHub is a large corporation and the bug bounty program was public on HackerOne, we felt that it was worth a shot.

## **Focusing on Business Logic**

Mr. Rajput Hacker and I decided to focus solely on business logic bugs in the application. Before we started our search, we made sure to understand the application completely. This involved minimal use of Burp Suite and a focus on understanding the core functionality and processes of the application. Our goal was to find any weaknesses in the business logic that could potentially be exploited. By limiting our toolset and focusing on understanding the application, we aimed to uncover any unique or overlooked vulnerabilities. As npmjs.com was a relatively small application, our understanding and notes took us less than two hours to complete.

## **Vulnerabilities Discovered**

**Id**| **H1 Report Title**| **Target**| **Reported Date** (DD/MM/YY)| **Severity**| **Reward**  
---|---|---|---|---|---  
1| Claiming Deleted Account Username Before 90 Days Can Lead To Multiple Issues| https://github.com/| 11/12/22| Informative| **NA**  
2| Account Sessions Still Active And Binded To Older Username After Changing Username| https://education.github.com/| 11/12/22| Low| **$2000**  
3| Tricking victim org members by name confusion vulnerability in member invite functionality of organization| https://npmjs.com/| 07/12/22| Medium| **Duplicate**  
4| Victim Can Claim Deleted Account Username Leads To Account Takeover Controlling Deleted Account Session| https://npmjs.com/| 02/12/22| Medium| **$4000**  
5| Delete Anyone’s Account On NPMJS By Abusing Support System Misconfiguration| https://npmjs/com/| 11/12/22| Low| **Duplicate ($200)**  
6| Login Verification Bypass On NPMJS.com| https://npmjs.com/| 16/11/22| Medium| **$4000**  
|  Total Reward| | | | **$10000**  
  
Vulnerability Reported To GitHub Security Program

Even though we mentioned about 9 Vulnerabilities being reported we are going to write about 3 of them over here today which are given below :

  1. Login Verification Bypass On npmjs.com
  2. Pre-Account Takeover On npmjs.com 
  3. Access Control Issue On education.github.com

## **Login Verification Bypass ON NPMJS**

### **Description –**

While going through authentication part of npmjs.com and common functionalities such as updating email address and profile update functionalities we found out an weird behavior about an application which caught our eye which was the format of email verification link , password reset link & link sent to update email address . 

The Link was formatted like **https://npmjs.com/verify/{some_random_token_here}** for all the functionalities be it password reset , email verification link or any xyz link on this site for any purpose . Next we observed every time you login into the application it sends an verification code to registered email address and you have to enter that as part of login verification feature (kind of 2FA/MFA code on email ) to successfully log into the account . we have then tried to bypass this functionality and were successful bypassing it as we have completely used an application in last 2 hours we knew each functionality so we were able to relate and got the bypass read below steps to reproduce to see how we did it .

During our examination of the authentication process and common functionalities of npmjs.com, such as updating email addresses and profiles, we discovered a peculiar behavior in the format of email verification links, pasWe Hacked GitHub for a Month : Here’s What We Foundsword reset links, and links sent to update email addresses. These links were formatted as **https://npmjs.com/verify/{random_token}** , and were used for all functionalities, including password reset, email verification, and others.

We also noticed that every time a user logged into the application, a verification code was sent to the registered email address. This verification code was required to complete the login process, acting as a form of two-factor authentication. Second thing we noticed When updating an email address on npmjs, the update process would occur without requiring a password confirmation. An email would be sent to both the old and new email addresses. The email sent to the old address would inform the recipient that if the change was not made by them, they can click a link (https://npmjs.com/verify/{some_random_token_here}) to revert the change and make their old address the current one. The email sent to the new address would contain a link to verify the new email and link it to the account that was just updated.

We encountered a surprising issue while trying to log into an account after updating the email address in the profile page. Despite not having confirmed or clicked on any links in either the old or the new email, the system displayed a message indicating that a verification code had been sent to the new, unverified address. This seemed to suggest that we would not be able to log in. However, upon closer inspection, we discovered an email sent to our old address, asking us to revert the change in order to avoid account lockout. Upon clicking the provided link (**https://npmjs.com/verify/{random_token}**) to revert the email, we were directed to the login page. To our surprise, when we entered our credentials, the system did not ask for the verification code and instead allowed us to log in and revert the email change.

However, upon further investigation, we were able to successfully bypass this functionality. Our deep understanding of the application, gained from spending two hours familiarizing ourselves with its features, allowed us to relate different functionalities and find the bypass. The steps to reproduce the bypass can be found below.

#### **Steps To Reproduce –**

  1. Signup Using [[email protected]](/cdn-cgi/l/email-protection) (username as attacker1)
  2. Login Into attacker1 with login and password (as npmjs login works with only username and password)
  3. Go To Account > Update Email > [[email protected]](/cdn-cgi/l/email-protection)
  4. Check your email [[email protected]](/cdn-cgi/l/email-protection) inbox you will see email from npmjs.com

5.Open Link **`https://www.npmjs.com/verify/{some_random_token_here}` **It Will Redirect To Login > Try Login using Victim Username & Password  
6.You Will Be Redirected To the 404 Page & Logged Into the Account Without Verification Code ! (Even Though The Page Will Show You An Message Which Tells You Are Not Logged Into Right User )  
  
**POC** –

https://youtube.com/watch?v=ox6np-b3nyI%3Ffeature%3Doembed

### **Impact –**

An attacker can exploit a vulnerability in npmjs to bypass the login verification process, which is meant to protect against credential harvesting and leakage attacks. This effectively allows the attacker to gain unauthorized access to the account without going through the intended security checks. This vulnerability is essentially a bypass of the login verification process, which serves as a temporary measure until two-factor authentication is enabled.

### **Our Conclusion –**

In conclusion, while we enjoyed discovering a vulnerability on GitHub, we were disappointed with the bounty reward received. Despite meeting the criteria listed on GitHub’s Hackerone policy page for a critical vulnerability, including bypassing the login process, accessing sensitive user data, and accessing another user’s data, we were classified as medium and received no clear justification from GitHub. Despite attempting to engage with the GitHub team through H1 Meditation, our efforts were in vain. We believe that this situation raises questions about the fairness of GitHub’s reward system and their adherence to their own policies.

#### **Critical Vulnerability Criteria Mentioned on GitHub’s Hackerone Policy Page**

  * arbitrary code/command execution on a server in our production network
  * arbitrary SQL queries on a production database
  * **bypassing the login process, either password or 2FA**
  * access to sensitive production user data or access to internal production systems
  * accessing another user’s data in the GitHub Actions service

![](https://web.archive.org/web/20240421181836im_/https://blog.cyberxplore.com/wp-content/uploads/2023/11/githubpolicy-768x367-1.png)

**GITHUB POLICY SCREENSHOT**

Request for Feedback from GitHub Team:

If a member of the GitHub team has any justification for the classification of the vulnerability, we would appreciate a response on the report or by reaching out to us on our H1 handles @th3pr0xyb0y and @mrrajputhacker2

### **Pre-Account Takeover On npmjs.com**

### **Description –**

After thoroughly reviewing the application, we decided to focus on finding logical bugs. During our observation, we noticed that the authentication process only used a username to log in and that the email address could easily be updated without password verification. This led us to believe that the username was a critical aspect of the npmjs.com backend.

We tested the delete account functionality and explored the following scenarios:

  1. Could we still access the account session if it was logged in from a different browser?  
We found that deleting the account from one browser immediately logs the user out from all other sessions.
  2. Could we register using the same username of a recently deleted account?  
Our testing showed that it was not possible to sign up with an existing or previously deleted username.
  3. Was there a way to change the username or claim a new/deleted username? We discovered one option to claim or change a username in the application – by creating an organization in npmjs account. This allowed us to choose a new username for the organization or convert our account into an organization, essentially changing our username. However, even this option did not allow us to change to a previously deleted username.

Despite hitting dead ends on all three scenarios, we were determined to find a solution and managed to successfully bypass the system with our persistent attitude. We have documented the steps in our report to demonstrate how we were able to create a pre-account takeover.

#### **New Observations In Our Research –**

We had previous knowledge that we could request to delete our account by submitting a support ticket. Therefore, we tested this method and deleted our account. After receiving the confirmation email, we discovered that even though the account was deleted, we were still logged in with our username displayed in the top right corner, but were unable to perform any actions.

We tried claiming the deleted username again by signing up in a different browser, but it was not possible. However, we had found a way to change our username, so we tried claiming it again in another browser. To our surprise, we were successful, and as soon as we claimed the username, the session was transferred to our previous session where we were only seeing a 404 error page. In this way, we were able to take over the account of a person who tried to change their username to a deleted account because we had the cookies and the session was transferred to us.

If the explanation seems confusing, please refer to the steps to reproduce and proof of concept to better understand this vulnerability.

### **Steps to Reproduce –**

  1. Sign up as an attacker using a common username (e.g. commonusername123) using the Google Chrome browser.
  2. Request account deletion from support.
  3. Once the account has been deleted by support, refresh the browser where the account was logged in. You will see that all pages except the profile page will show your username (the link of the page would be [https://npmjs.com/~username](https://web.archive.org/web/20240421181836/https://web.archive.org/web/20230314103203/https://npmjs.com/~username)).
  4. Try visiting [https://www.npmjs.com/settings/commonusername123/profile](https://web.archive.org/web/20240421181836/https://web.archive.org/web/20230314103203/https://www.npmjs.com/settings/commonusername123/profile). You will see a 404 page.
  5. Sign up as a victim using a different username (e.g. victimusername123) using the Firefox browser.
  6. Convert the victim account into an organization. This will make the org username as victimusername123 and will ask you to choose a new username. Choose commonusername123 as the new username for the account.
  7. Refresh the attacker session page [https://npmjs.com/~username](https://web.archive.org/web/20240421181836/https://web.archive.org/web/20230314103203/https://npmjs.com/~username) using the Google Chrome browser.
  8. Try visiting [https://www.npmjs.com/settings/commonusername123/profile](https://web.archive.org/web/20240421181836/https://web.archive.org/web/20230314103203/https://www.npmjs.com/settings/commonusername123/profile). You will now see the victim’s email (e.g. [[email protected]](/cdn-cgi/l/email-protection#9aecf3f9eef3f7dafdf7fbf3f6b4f9f5f7)) and have access to the victim account and the organization it created.

### **POC** –

https://youtube.com/watch?v=5039T3y8yFw%3Ffeature%3Doembed

### **Impact –**

A malicious actor can create multiple accounts with common usernames on npmjs.com, delete them by submitting a support ticket, and retain the cookies. As a result, they have the potential to take over an account if someone else claims those usernames.

### **Our Conclusion –**

In conclusion, while we were excited to uncover a vulnerability on GitHub, we were disappointed with the bounty reward we received. It was a complex but possible account takeover that could have affected a large organization. To clarify the impact, we still had one account with stored cookies and active sessions that have been ongoing for over three months, as the session of a deleted account never expires on npmjs. However, GitHub considered this vulnerability as “medium” and only awarded us a **$4000** bounty.

### **Access Control Issue On education.github.com**

### **Description –**

After being unsatisfied with GitHub’s response to our previous vulnerabilities reported on npmjs and reward, we decided to focus on other GitHub subdomains. We discovered that education.github.com was using GitHub Single Sign-On (SSO) for its login process. Inspired by the bugs we found on npmjs, we experimented with a similar approach using deleted account usernames.

To our surprise, we found that deleting a GitHub account did not result in the session expiring on education.github.com, and every page displayed a 404 error, even when still logged in. In another browser, we attempted to create a new GitHub account with the same deleted username, but as per GitHub’s policy, usernames can’t be claimed for 90 days after being deleted .

However, despite these dead ends, we were able to bypass the issue and gain access control . 

### **Bypassing The Access Control –**

We observed that even though we changed an username in GitHub and refreshed our session of education.github.com the username is same it didn’t changed even though we had changed that in our GitHub profile this happens due to session token is binded to username and SSO refreshes that only when we login again through GitHub so we quickly claimed deleted GitHub account and then claimed old username which was still associated at **https://education.github.com** with that account using new github account in different browser and logged into **https://education.github.com** on new browser now we observed both the account have same username but different email associated with them and are completely functional so if we submit any educational form or trigger any functions it can cause some data integrity damage at both the sides so we did reported this as an issue and it got accepted as an valid issue .

We noticed that even after changing our GitHub username, the session on education.github.com remained unchanged. This was because the session token was tied to the username and the SSO only refreshed it upon logging in through GitHub. To exploit this, we quickly claimed a deleted GitHub account and then claimed the old username, which was still associated with the education.github.com account. We then logged into education.github.com using a different browser with a new GitHub account, and found that both accounts now had the same username but different email addresses and were fully functional.

This meant that if we submitted an educational form or triggered any functions, it could result in data integrity damage on both sides. We promptly reported this as an issue and it was accepted as a valid vulnerability.

### **Steps To Reproduce –**

  1. Log in to your GitHub account
  2. Visit [https://education.github.com/schools](https://web.archive.org/web/20240421181836/https://web.archive.org/web/20230314103203/https://education.github.com/schools)
  3. Change your username in your GitHub account
  4. Refresh the page or visit [https://education.github.com/schools](https://web.archive.org/web/20240421181836/https://web.archive.org/web/20230314103203/https://education.github.com/schools) again and check the username from the profile icon on the right
  5. You will see that the old username is still active on education.github.com
  6. Since the old username is claimable, it appears that an account takeover on education.github.com is possible by claiming it.
  7. If you don’t have a college email, you can’t verify if the actions performed on the old session will affect a new account signed up with the old username.
  8. Log in to education.github.com on a new Chrome window with a newly created account that has the same username as the old session.
  9. You will see that you now have two active sessions with the same username.

### **Impact –**

The impact of this issue should be evaluated by the GitHub team. It has the potential to compromise sensitive information of new users, such as their school or email address and personally identifiable information (PII), if they sign up with the username for which an active session exists. This could result in an account takeover and the leaking of PII.

### **Our Conclusion –**

we were pleased to discover this vulnerability on GitHub, even though it was similar to what we found on npmjs. This time, we were unable to assess the full impact of the issue. Nonetheless, we were satisfied with the bounty reward that was given.

## **Did you learn something from us?**

Help us by sharing this article with your friends, family, and colleagues, and by following us on our social media accounts. You can also subscribe to our mailing list for more informative write-ups about our findings. Show your support by tweeting about this article and sharing it with the community as much as possible.

Check out our new product, Blind XSS Hunter, designed to support the community, only at [https://bxsshunter.com](https://web.archive.org/web/20230314103203/https://bxsshunter.com/).

Get ready for an exciting launch from CyberXplore! We’ve been hard at work for the past two years, perfecting a product that we can’t wait to share with you. Be the first to experience it by staying connected with us or following us on our journey. And for all the latest updates, make sure to subscribe to our newsletter! This is a launch you won’t want to miss!

Categories [Cyber Security](https://blog.cyberxplore.com/category/cyber-security/), [Security Research](https://blog.cyberxplore.com/category/security-research/)

[How We Are Able To Hack Any Company By Sending Message – $20,000 Bounty [CVE-2021–34506]](https://blog.cyberxplore.com/how-we-are-able-to-hack-any-company-by-sending-message-20000-bounty-cve-2021-34506/)
