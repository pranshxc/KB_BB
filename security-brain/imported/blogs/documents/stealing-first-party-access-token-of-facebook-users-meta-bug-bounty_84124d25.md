---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-30_stealing-first-party-access-token-of-facebook-users-meta-bug-bounty.md
original_filename: 2024-07-30_stealing-first-party-access-token-of-facebook-users-meta-bug-bounty.md
title: 'Stealing First Party Access Token of Facebook Users: Meta Bug Bounty'
category: documents
detected_topics:
- oauth
- access-control
- command-injection
- otp
- automation-abuse
- graphql
tags:
- imported
- documents
- oauth
- access-control
- command-injection
- otp
- automation-abuse
- graphql
language: en
raw_sha256: 84124d25d4dba90e1c7d6136da70f15ab5e91ff1e40b19b4e2d9f6d35ebec951
text_sha256: 305a8411cd7a49b5797d83c5790eeb69f90778cc49a3150a026d592928173e0b
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing First Party Access Token of Facebook Users: Meta Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-30_stealing-first-party-access-token-of-facebook-users-meta-bug-bounty.md
- Source Type: markdown
- Detected Topics: oauth, access-control, command-injection, otp, automation-abuse, graphql
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `84124d25d4dba90e1c7d6136da70f15ab5e91ff1e40b19b4e2d9f6d35ebec951`
- Text SHA256: `305a8411cd7a49b5797d83c5790eeb69f90778cc49a3150a026d592928173e0b`


## Content

---
title: "Stealing First Party Access Token of Facebook Users: Meta Bug Bounty"
url: "https://iamsaugat.medium.com/stealing-first-party-access-token-of-facebook-users-meta-bug-bounty-44b3b2e87d07"
authors: ["Saugat Pokharel (@saugatscript)"]
programs: ["Meta / Facebook"]
bugs: ["OAuth", "Account takeover"]
publication_date: "2024-07-30"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 121
scraped_via: "browseros"
---

# Stealing First Party Access Token of Facebook Users: Meta Bug Bounty

Stealing First Party Access Token of Facebook Users: Meta Bug Bounty
Saugat Pokharel
Follow
6 min read
·
Jul 30, 2024

170

2

Hi, I am Saugat Pokharel from Kathmandu, Nepal. I am going to talk about one of my findings on Facebook. The vulnerability led to the stealing of 1st party access tokens without the knowledge of Facebook users. So, let’s begin.

During BountyCon 2022 event in Singapore, One of the Facebook security engineers advised me to look into business integrity issues. I was particularly interested in it after knowing the scope of the Integrity Safeguard Program.

The Integrity program had scopes like bypassing different business checkpoints and settings. Examples: Using a fake payment method to run ads, generating an arbitrary amount of Ad revenue via fake impressions, creating an arbitrary amount of prepaid balance without using a valid payment method, etc. You can learn more about Meta Integrity safeguard programs here.

I previously knew about how we can increase likes on Facebook using different bots and applications. Some of my friends used to collect a huge number of likes and comments by visiting websites that provide Facebook likes for free. So, I started analysing those sites.

After some minutes of research, I found a site called “Machine-liker”, which has been helping users to increase likes on Facebook posts. The website had a Login with Facebook button (OAuth flow) that looks identical to Facebook 3rd party login flow.

Login with FB button as implemented in that website

After clicking on Login with Facebook, I was redirected to another window where it asked me to allow permission.

I clicked on Allow Permission thinking it was an expected OAuth flow. After that I was redirected to facebook.com/device and the following code was auto-filled. I clicked on the Continue button to see what happened next.

After clicking on continue, it asked me for various sets of permissions ranging from name, and email address to critical permissions like accessing the pages that I manage, posting on behalf of my account, and many more.

I knew that I should not be providing access to this sensitive information. Therefore, I clicked on “Choose what you allow” and unchecked all the permissions except Name and Profile pictures. Finally, the authorisation process was completed.

The website had no proper redirection back to its login page after successful authorisation. So, it was already very weird for me. So, I went back to the website and clicked on verify & login.

And surprisingly it disclosed all of my posts asking where I would like to increase reactions. Most of the posts shown there had privacy “Only Me” and “Friends”.

I was shocked to see how the website was able to access my private image that had privacy “Only Me” and “Friends”? Even though I declined permission to access photos, how was the website able to show up my photos?

I immediately went to Facebook > Settings > Apps & Websites and then tried to remove the app access. But, I didn’t see any recent apps and websites that I have logged into. Also, I got suspicious login attempts alert in my account.

I didn’t understand how that was happening but I became fairly confident that the website should not be accessing my images when I declined permission to access my photos. So, I quickly went to Facebook whitehat and reported the behavior that I faced.

I could have waited a bit and found the actual cause of this issue, but I was rushed because I was getting so many login attempt notifications.

Get Saugat Pokharel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After I reported the issue, I looked into it further and found that the website uses Facebook Login for Devices.

What is Facebook login for devices?

Facebook Login for Devices provides an easy authentication flow where a user can authenticate just by entering a temporary code without entering their username and password. It is normally used to connect our Facebook accounts with smart TVs, cameras, printers, and other devices.

Example: If you have an Android TV, go to your TV and download the application called Facebook Watch. After you download the app, open it and you will get a temporary code on the TV screen as shown in the picture below. Now, go to facebook.com/device and enter the code given on your TV. In this way, your Facebook account will be connected to your TV.

Press enter or click to view image in full size

Another example:

Meta Quest uses login with devices. So, to connect our Meta Quest with our Facebook account, we simply need to go to: facebook.com/device and enter the code as shown in the Meta Quest. Now, the Meta Quest device will be linked to our Meta/Facebook account.

Press enter or click to view image in full size

In this way, Login with Device provides an easier way to connect Facebook accounts with different devices.

Read detail here: https://auth0.com/docs/get-started/authentication-and-authorization-flow/device-authorization-flow

So, what is the bug? And how was the application able to implement login with devices flow on their website?

After doing some research, I came to know that it is possible to implement this login with device flow on any website. For that, we just need the client_token and app_id of any application that has login with devices enabled. Both of these can be obtained easily through specific endpoints or reverse engineering the application.

Then we can automate the login process easily using the two endpoints.

For generating code & user_code: https://graph.facebook.com/v2.6/device/login?access_token=app_id|client_secret&scope={permissions}&method=post

For generating access token: https://graph.facebook.com/v2.6/device/login_status?access_token=app_id|client_secret&method=post&code={code}

The website automated this process using the above listed URLs to steal access tokens from Facebook users. These stolen tokens are first-party access tokens, which are particularly dangerous due to their capabilities. With these tokens, one can perform sensitive actions such as executing GraphQL queries or mutations to change phone numbers or emails, potentially leading to the takeover of Facebook or Instagram accounts. Also, these tokens are long lived token (do not expire on quick time interval/or after logout).

When a website successfully steals first-party access tokens, it can use them to make GraphQL queries to send reactions or make comments. This is what the website “machine-liker” has been doing for years. These sites encourages Facebook users into authorising the login flow on their platform, thereby collecting millions of first-party access tokens. I also discovered several forums where these tokens are traded for money.

The code autofill was removed. Now, clicking on the link will not auto-fill the code on Facebook.com/device. This makes the attack more difficult.
1st Party dialog box is implemented instead of the third party. Now, users are aware completely because it warns that the app is gaining access to Facebook accounts.
Now, users will understand that they are given a lot of permissions by clicking continue

3. The site that was actively stealing user data is no longer active. I am not sure if the site is forced closed by Facebook or if the site owner closed themselves.

4. The advisory was added. A user will now see an advisory saying: “Only use a code from a source that you trust.”

5. A lot of FB 1st party applications no longer support such device logins.

Timeline:

October 25, 2022: Report Sent
October 26, 2022: Report confirmed by Facebook
June 2023: Multiple Bounties Rewarded
