---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-12_amazon-cognito-misconfiguration-lead-to-account-takeover.md
original_filename: 2022-08-12_amazon-cognito-misconfiguration-lead-to-account-takeover.md
title: Amazon Cognito misconfiguration lead to account takeover
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
- otp
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
- otp
- cloud-security
language: en
raw_sha256: 4d91e60acae1f0aeccd1a09518c3bfa841ceb8773a23278bb6ce1504709baae7
text_sha256: ef32ffdb15ad8ae866c4cce049541132a6fec30d4d59289199bdba11c55728b7
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Amazon Cognito misconfiguration lead to account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-12_amazon-cognito-misconfiguration-lead-to-account-takeover.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset, otp, cloud-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `4d91e60acae1f0aeccd1a09518c3bfa841ceb8773a23278bb6ce1504709baae7`
- Text SHA256: `ef32ffdb15ad8ae866c4cce049541132a6fec30d4d59289199bdba11c55728b7`


## Content

---
title: "Amazon Cognito misconfiguration lead to account takeover"
page_title: "Suspend any registered user’s account via Amazon Cognito misconfiguration | by Hossam Ahmed | Medium"
url: "https://medium.com/@iknowhatodo/amazon-cognito-misconfiguration-lead-to-account-takeover-20694243ca40"
authors: ["Hossam Ahmed (@iknowhatodo0x01)"]
bugs: ["Account takeover"]
publication_date: "2022-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2329
scraped_via: "browseros"
---

# Amazon Cognito misconfiguration lead to account takeover

Suspend any registered user’s account via Amazon Cognito misconfiguration
Hossam Ahmed
Follow
5 min read
·
Aug 12, 2022

112

2

Hello reader,
I hope you are doing well. Today I want to talk about one of my findings. It was a public program and the bug is not fixed yet. So I am not going to include any information about the program here. Let’s call it redirect.com.

So redirect.com uses Amazon Cognito service as provides authentication, and authorization. And uses a userPool to organize its users. In the userPool; there are userPool attributes, these attributes are pieces of information that help the developer to identify individual users, such as name, email address, and phone number. Some attributes are only for reading; they cannot be modified, and some attributes can be modified (The developer can control that).
More information here: https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.htm

Recon

I started with the main domain and I collected the various functions available on the website and wrote them down in notepad++.
I used the different functions on the website one by one. After that, I analyzed the requests and responses in the burpSuite to see how the process of creating an account and the process of logging in and changing email are done, understanding the developer’s mind and the logic.

After analyzing the requests and responses, I noticed the following:

1- During the registration process, a random user_id is automatically generated. If the user completes the registration process; this user_id doesn’t change if the user changed the current email to another one.

Press enter or click to view image in full size
Part of the registration process.

2- Every time I login to my account, I have getting an accessToken, idToken, and refreshToken.
Note that refreshToken is used as a long-live token. So, I can use it to retrieve another accessToken, idToken, and refreshToken again without needing to login to my account by using email and password. And these tokens are linked with the user_id of an account. Those tokens are valid even after I logged out!

Press enter or click to view image in full size
Different tokens are generated after a successful login.

3- I found a hidden endpoint responsible for changing the email without confirming the change by a code that arrives at the current email.

Press enter or click to view image in full size
The request and response for the hidden endpoint responsible for changing the email without confirming the change by a code that arrives at the current email.

4- I can’t change my current email to another email that’s already in use, even if I use the hidden endpoint I found earlier.

Attack scenario

Attacker perspective:

Press enter or click to view image in full size

Now, I decided to use the Amazon Cognito API to change the current email to another one that is already exist (the victim’s email).

Press enter or click to view image in full size
UpdateUserAttributes is an endpoint that is responsible for changing the user attributes by using accessToken.
Press enter or click to view image in full size
Response.

What! It’s works

That means, that UpdateUserAttributes. In particular; the email attribute, it’s not protected from manipulate by the user by using accessToken

But, now my account is unverified!
This means that I cannot login to my account using the unverified email or using my previous email and current password.

Press enter or click to view image in full size
Now, the email marked as unverified.

The question that came to my mind was, what if I could confirm my current email (victim’s email)?

Get Hossam Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The same email address in the victim’s account will become unverified and therefore will not be able to login with the unverified email and his password because his account is now suspended.

The challenge now, is how can I confirm the victim’s email that linked to my account?

I decided to change the current email to another one I owned but not complete the confirmation process to see what will happen.

I went back to the burpSuite to analyze requests and responses but found what wasn’t expected…….! The current email (victim’s email) has been verified. Wow

Press enter or click to view image in full size
The victim’s email has been verified.

Victim’s perspective:
If I try to login to my account using my email (which has become unverified) and current password, the login process didn’t work. And the reason I mentioned earlier.

Now, I decided to reset my password through my email.
After resetting my password, I logged into my account using my current email and new password. But, I noticed that I logged into an account different from mine! How did that happen? And for whom is this account?

First:
This account is for the attacker
Second:
It happened because the victim’s account had been suspended, so when the victim used the password reset feature and used the email that was confirmed by the attacker, at that time; he changed the password related to the email that linked to the attacker’s account, and it’s also linked with user_id belonged to the attacker and not to the victim’s account.

Account is suspended, This means that account cannot use the various features of the site and that include password reset.

Attacker perspective:

I tried to log in but it didn’t work. The reason is that the victim changed the password.

Now, How can I escalate this attack to get back to my account (victim’s account) again?

Escalate the attack to account takeover

Attacker perspective:

I explained earlier that the refreshToken don’t expire in case of logging out, ending the session, changing the password, or changing the email.

Now I can get a new accessToken and idToken using the old refreshToken belongs to the attacker’s account (which has now become the victim’s account.)

How can I do that?

By using the InitiateAuth endpoint with some specific parameters that includes the refreshToken belongs to the attacker’s account (which has now become the victim’s account.) to generate a new idToken and AccessToken.

Press enter or click to view image in full size
{InitiateAuth} request and response

Now, I can use the hidden endpoint to change the victim’s email without entering the confirmation code that arrives at the victim’s email. Or I can track the victim and see changes in his account, which may be about the credit card information.

Finally I got duplicate for “ Change the email without entering a confirmation code”

Press enter or click to view image in full size

I hope you enjoyed reading.

Follow me on Twitter: @iknowhatodo0x01
