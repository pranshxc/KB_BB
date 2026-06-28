---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-30_ato-without-any-interaction-aws-cognito-misconfiguration.md
original_filename: 2022-04-30_ato-without-any-interaction-aws-cognito-misconfiguration.md
title: ATO without any interaction [aws cognito misconfiguration]
category: documents
detected_topics:
- otp
- rate-limit
- cloud-security
- oauth
- sso
- access-control
tags:
- imported
- documents
- otp
- rate-limit
- cloud-security
- oauth
- sso
- access-control
language: en
raw_sha256: cd73b838691d3f84cefbbf2a9f007eb83fb37d7e6bb2224e69bb671ca2ccd08a
text_sha256: ef62f6b90de9819e90af8104ebd63593e54b58444a39eb6171ed61a2fb7f5db4
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# ATO without any interaction [aws cognito misconfiguration]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-30_ato-without-any-interaction-aws-cognito-misconfiguration.md
- Source Type: markdown
- Detected Topics: otp, rate-limit, cloud-security, oauth, sso, access-control
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `cd73b838691d3f84cefbbf2a9f007eb83fb37d7e6bb2224e69bb671ca2ccd08a`
- Text SHA256: `ef62f6b90de9819e90af8104ebd63593e54b58444a39eb6171ed61a2fb7f5db4`


## Content

---
title: "ATO without any interaction [aws cognito misconfiguration]"
page_title: "Account takeover without any interaction [aws cognito misconfiguration] | by Shreyas koli | Medium"
url: "https://shreyaskoli.medium.com/ato-without-any-interaction-aws-cognito-misconfiguration-d690f4b3da11"
authors: ["Shreyaskoli (@SPY8OY)"]
programs: ["GitHub"]
bugs: ["Account takeover", "Lack of rate limiting"]
bounty: "550"
publication_date: "2022-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2673
scraped_via: "browseros"
---

# ATO without any interaction [aws cognito misconfiguration]

Account takeover without any interaction [aws cognito misconfiguration]
Shreyas koli
Follow
6 min read
·
Apr 30, 2022

315

4

Hello friends,

This is Shreyas koli from Maharashtra, India. It’s my first article. In this article I will share my recent finding in which I was able to chain aws cognito misconfiguration to account takeover. there might be tones of mistakes .So please ignore my mistakes and lets get started.

One day my friend @manthan suggested me one program. So I decided to give it try. let’s call this target as target.com. Okay so target.com is a website which provides online application from which you can manage your devices which are connected in LAN. like any server , raspberry pi etc. This website was using AWS cognito for login.

About AWS cognito :

Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple.

AWS cognito flow

Above Fig shows AWS cognito flow. And following is description of each request:

In the first step your app user signs in through a user pool and receives user pool tokens after a successful authentication.
Next, your app exchanges the user pool tokens for AWS credentials through an identity pool.
Finally, your app user can then use those AWS credentials to access other AWS services such as Amazon S3 or DynamoDB.

I hope you understood about AWS cognito flow. for more information you can refer AWS cognito documentation .

Now lets get back to our target . By using email & password or Oauth we can login to this site. and both were using AWS cognito for Authorizing access token. When user provide valid login credentials or use Oauth then it was issuing access token (As temporary credential to fetch data or modify data on server). using following command we can get user data with the help of access token.

$ aws cognito-idp get-user --region us-west-2 --access-token <token>

After doing some further testing I found that token issued by providing EMAIL, PASSWORD and through OAUTH are totally different . I mean referred Usernames were different . Following is result of get-user using access token issued by providing EMAIL, PASSWORD. Just remember the username of this access token.

$ aws cognito-idp get-user --region us-west-2 --access-token <token>
{
  "Username": "3b84472e-5b44-4d9e-bbea-a49592b8e162",
  "UserAttributes": [
  {
  "Name": "sub",
  "Value": "3b84472e-5b44-4d9e-bbea-a49592b8e162"
  },
  {
  "Name": "email_verified",
  "Value": "true"
  },
  {
  "Name": "email",
  "Value": "shreyaskoli165@gmail.com"
  }
  ]
}

Following is result of get-user using access token issued by Oauth .

$ aws cognito-idp get-user --region us-west-2 --access-token <token>
{
  "Username": "google_107427578229077464095",
  "UserAttributes": [
  {
  "Name": "sub",
  "Value": "0080f3d4-2173-469f-a929-8a67225d446c"
  },
  {
  "Name": "identities",
  "Value": "[{\"userId\":\"107427578229077464095\",\"providerName\":\"Google\",\"providerType\":\"Google\",\"issuer\":null,\"primary\":true,\"dateCreated\":1651166579396}]"
  },
  {
  "Name": "email_verified",
  "Value": "true"
  },
  {
  "Name": "given_name",
  "Value": "Shreyas"
  },
  {
  "Name": "family_name",
  "Value": "Koli"
  },
  {
  "Name": "email",
  "Value": "shreyaskoli165@gmail.com"
  }
  ]
}

Now you can compare that Username of access token issued by EMAIL, PASSWORD and Username of access token issued by Oauth is different. although access tokens belongs to same account . This means that this two tokens are referring different Usernames for modifying account details like name, email etc.

Get Shreyas koli’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After some time I found that Access token issued by Ouath is allowing to change account’s email to email which already exists . Use following command to change email of your account.

$ aws cognito-idp update-user-attributes --region us-west-2 --user-attributes 'Name=email,Value=victimsemail@gmail.com' --access-token [access token]
{
  "CodeDeliveryDetailsList": [
  {
  "Destination": "v***@g***",
  "DeliveryMedium": "EMAIL",
  "AttributeName": "email"
  }
  ]
}

Then I immediately changed my accounts email to victims email using above cmd and refreshed the page and I got following error :(

Error popup

When I refreshed page. Browser was sending following request to get user data i.e its calling get-user. where it was checking email has verified or not . If it’s not verified then it was expiring the session . After showing pop up “Could not get user data, logging you out…” it logs you out . You can see in following request “email_verified” Field is set to false. which shows email is not verified.

Press enter or click to view image in full size
get-user request

After spending some time to bypass this verification I tried response manipulation and some other methods but no luck. It already had been 2 Am . so I decided that I will give it try tomorrow . Next Day after doing some boring lectures while returning from college . I was thinking what can be the bypass for this validation . I thought that if its only client side validation then I will just disable the JS of my browser before fetching get-user using access token OR I will try match and replace in Response body in which I will only replace false to true in every request of get-user. While testing I just changed my accounts email to victims email using above aws cognito command and refreshed page and started monitoring the requests on my burp . I stopped the forwarding request when I got request of get-user with access token . then Disabled JS of my browser (Go to new tab about:config >> search JS >> disable JS) . Now forwarded get-user request . And guess what I was able to login to victims account :) Because there was only client side validation whether the user’s email has verified or not. After getting successful login I was like :)

Steps:

login to your account using Oauth and get Access token through your burp history.
Using following CMD change your email to victims email.
$ aws cognito-idp update-user-attributes --region us-west-2 --user-attributes 'Name=email,Value=victimsemail@gmail.com' --access-token [access token]

3. Refresh your tab and then start forwarding request until you see get-user request with access token . if you see it then wait

4. Now disable the JS of your browser and turn off intercept

You can see we have successfully logged in as victim :)

While testing aws cognito I noticed that when I change email , every time it’s sending otp to new email . According to gmail if we send email to me+[anything]@gmail.com then it will be received by me@gmail.com. we are using this trick to target specific user . now we can just run CMD of change email in for loop to spam any user and here we have no rate limit bug :)

Bash Script:

#!/bin/bash
for i in {1..100}
do
  echo "$i]"
  aws cognito-idp update-user-attributes --region us-west-2 --user-  attributes "Name=email,Value=victimemail+$i@gmail.com" --access-token [token here]
done

After finding this two bug, I immediately reported this bugs to there bug bounty program. then After some days they rewarded me $500 of bounty for ATO . I was expecting that reward will be at least $$$$ digit but they said that this is highest reward. and also I got $50 of bounty for No rate limit bug. Thanks for reading this article. If you want to learn more about aws cognito misconfiguration then check out following resources.

Lets connect :

Twitter : @SPY8OY

Linkedin : Shreyas Koli

Resources:

Flickr Account Takeover
This post gives a deep dive into a critical security flaw that was present in Flickr's login flow. The authentication…

security.lauritz-holtmann.de

Exploiting weak configurations in Amazon Cognito in AWS
This blog post talks all about understanding and exploiting weak configuration in Amazon Cognito.

blog.appsecco.com

Compromising S3 Buckets through Misconfigured AWS Cognito
In a recent engagement, I came across a misconfigured Cognito service that allowed me to compromise S3 buckets through…

curlsandbun.medium.com

Hacking AWS Cognito Misconfigurations
In this blog, Sunil Yadav, our lead trainer for "Advanced Web Hacking" training class, will discuss a case study of AWS…

notsosecure.com
