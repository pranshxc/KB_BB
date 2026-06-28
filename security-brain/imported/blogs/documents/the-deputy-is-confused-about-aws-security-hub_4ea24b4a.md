---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-03_the-deputy-is-confused-about-aws-security-hub.md
original_filename: 2023-11-03_the-deputy-is-confused-about-aws-security-hub.md
title: The Deputy Is Confused About AWS Security Hub
category: documents
detected_topics:
- cloud-security
- sso
- access-control
- xss
- command-injection
- information-disclosure
tags:
- imported
- documents
- cloud-security
- sso
- access-control
- xss
- command-injection
- information-disclosure
language: en
raw_sha256: 4ea24b4ae4e6dda0e4ec78d6c30a32706eafbb6808198b37e595ea56fa6e8221
text_sha256: 29fa074ded186c6335ac321cd62151b533424d10cda5c864f5735512a2a18cef
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# The Deputy Is Confused About AWS Security Hub

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-03_the-deputy-is-confused-about-aws-security-hub.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, access-control, xss, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `4ea24b4ae4e6dda0e4ec78d6c30a32706eafbb6808198b37e595ea56fa6e8221`
- Text SHA256: `29fa074ded186c6335ac321cd62151b533424d10cda5c864f5735512a2a18cef`


## Content

---
title: "The Deputy Is Confused About AWS Security Hub"
url: "https://blog.plerion.com/the-deputy-is-confused-about-aws-security-hub/"
final_url: "https://www.plerion.com/blog/the-deputy-is-confused-about-aws-security-hub"
authors: ["Daniel Grzelak (@dagrz)"]
programs: ["AWS"]
bugs: ["Confused deputy", "Information disclosure", "Cloud"]
publication_date: "2023-11-03"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 688
---

## The Deputy Is Confused About AWS Security Hub

Update: The AWS Security Hub team got in touch to clarify some of the points below, and get feedback to help customers avoid some of the gotchas herein. The resulting goodness has been sprinkled throughout the post, and we are grateful to AWS for being so proactive about security. <3

Welcome to some extremely niche AWS security content. If you are the kind of crazy that we are at Plerion, and you’ve decided to build a product that integrates with [AWS Security Hub](https://aws.amazon.com/security-hub/), this blog post is for the you. We made a mistake in our implementation, fixed it, and now you can too!

Security teams have a lot of security tools, too many tools. Luckily in 2019 our friends at AWS saved us from the agony of a thousand dashboards by creating a single dashboard to rule them all, at least for security issues related to AWS infrastructure.
  
  
  aws securityhub enable-import-findings-for-product --product-arn arn:aws:securityhub:us-east-1::product/plerion/cloud-security-platform

It’s pretty snazzy actually.

  * Step 1: Find a commercial tool you love that finds badness in AWS stuff. (Aside: Security Hub supports non-commercial tools that aren’t listed as providers too, they just use a slightly different model)
  * Step 2: You fight your CFO for budget, and they eventually agree to end the lease on your current office so you can buy license of the tool.
  * Step 3: You log into to your AWS account and click “Accept findings” on the integration associated with the tool you’ve chose.

![accept-findings](https://cdn.prod.website-files.com/663cfee0a192fe7e5bd05ee8/66a09c770f40c8024b5537eb_accept-findings-1-qhzot8eh1n6p9dhxra1hflo8q24vm19g40vt6ht4uy.webp)

  * Step 4: Findings start rolling into your unified single-pain-of-glass one-stop-shop Security Hub hub. All that’s left is letting the sense of accomplishment wash over you like a cool Summer breeze.

I told you it was snazzy! You’ll know better than to doubt me next time.

### Not so fast

If you’re on the other end of this pipe, building a scanner and generating highly valuable signal that is desperate to make its way to a dashboard, things are a little bit more complicated.

The customer has provided their consent for you to send them the goodies. But how how do you know where to send those goodies? Well naturally you ask:

Hello valued customer [Name], we have the best security issues to send to your Security Hub hub. Where is it?

**Hottest Regards, Important Product Person**[**Tweet**](https://twitter.com/intent/tweet?text=Hello+valued+customer+%5BName%5D%2C+we+have+the+best+security+issues+to+send+to+your+Security+Hub+hub.+Where+is+it%3F+%E2%80%94+Hottest+Regards%2C+Important+Product+Person&url=https%3A%2F%2Fblog.plerion.com%2Fthe-deputy-is-confused-about-aws-security-hub%2F)

They respond by giving you their AWS account ID (which is actually unnecessary because typically findings should just go to the account they relate to) and you smoosh it into your security scanning machine. It purrs like a kitten, generating goodies. Like clockwork (usually 2-5 minutes later) the goodies end up on the customer’s dashboard. Everyone erupts in euphoric cheer as another happy customer has solved their cloud security problems. 

But what if the customer went on a bender the night before, and instead of giving you their current account ID, they accidentally give you their old employer’s account ID that they diligently memorized during a battle to the death with CloudFormation? If their old employer hasn’t clicked “accept findings” then not much happens.

If their old employer has clicked “accept findings” at any point, this results in what the big dogs in cybersecurity intelligentsia call a ‘[confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem)‘.

![sequence-diagram](https://cdn.prod.website-files.com/663cfee0a192fe7e5bd05ee8/66a09c77aa53bbbd1f9a4e0b_sequence-diagram-1.webp)

Many customers have authorized your platform to send them findings but the platform hasn’t validated ownership of the accounts where the findings are being sent. So whether intentionally or maliciously, the one customer’s findings are being sent to another customer.

Note: For the moons to align in this way, the user controlled account ID has to end up in the call to BatchImportFindings.

The security implications of this aren’t earth shattering but they do exist. An attacker could sign up to your scanning service and use it to pollute someone else’s Security Hub hub. Security folk have enough false positives and irrelevant noise to deal with already, without having to deal with intentionally irrelevant and misleading data.

The more important implication is the loss of trust a security product would face if it were the cause of such cross-tenant data pollution. It’s just not a good look. The sheriff would not be happy with this deputy. Luckily, as part of the integration process with the Security Hub team, correct generation and sending of findings to the right accounts is reviewed before go live. However, life happens, code and people change over time, and it is important to note that if code changes happen past the initial integration, this problem can occur.

### What else can go wrong?

Turns out there’s more niche minutiae to think about. Who knew?

Let’s say a customer is a big nerd like me and likes to do things through the cli instead of the web console. Instead of navigating through a visual list of products and clicking “accept findings”, they could do something like:
  
  
  aws securityhub enable-import-findings-for-product --product-arn arn:aws:securityhub:us-east-1::product/plerion/cloud-security-platform

But how would they know what product ARN to provide to the command? Well they would first have to run:
  
  
  aws securityhub describe-products

Which would return a big ol’ json blob that looks something like this:
  
  
  {
  "Products": [
  ...
  {
  "ProductArn": "arn:aws:securityhub:us-east-1:123456789012:product/plerion/cloud-security-platform",
  "ProductName": "Cloud Security Platform",
  "CompanyName": "Plerion",
  "Description": "Plerion is a Cloud Security Platform with a unique threat-led, risk-driven approach offering customer preventative, detective, and corrective action across their workloads. Plerion's integration with Security Hub allows customers to centralize and act upon their security findings in one place.",
  "Categories": [
  "Cloud Security Posture Management (CSPM)",
  "Asset Management",
  "Threat Modeling"
  ],
  "IntegrationTypes": [
  "SEND_FINDINGS_TO_SECURITY_HUB"
  ],
  "MarketplaceUrl": "https://aws.amazon.com/marketplace/seller-profile?id=464b7833-edb8-43ee-b083-d8a298b7ba08",
  "ActivationUrl": "https://au.app.plerion.com/resource-center/platform-documentation/integrations/outbound/securityHub",
  "ProductSubscriptionResourcePolicy": "{...}"
  },
  <more products here>
  ...
  ]
  }

This is a call anyone with an AWS account needs to be able to make. What is returned is essentially public. So now your ProductArn is public and if it includes your AWS account ID (it stopped being included in 2019), that too is public.

That’s not all, in order to scope which Account IDs can act on your product’s behalf to send findings, and which account IDs can enable your product, AWS kindly produces the IAM policy used to enforce this scoping inside the ProductSubscriptionResourcePolicy parameter.

Unescaping the parameter produces JSON that looks something like this:
  
  
  {
  "Version": "2012-10-17",
  "Statement": [
  {
  "Effect": "Allow",
  "Principal": {
  "AWS": "123456789012"
  },
  "Action": [
  "securityhub:BatchImportFindings"
  ],
  "Resource": "arn:aws:securityhub:us-east-1:123456789012:product-subscription/plerion/cloud-security-platform",
  "Condition": {
  "StringEquals": {
  "securityhub:TargetAccount": "123456789012"
  }
  }
  },
  <more statements here>
  ...
  ]
  }

Now not only is your one main account ID being leaked but a whole bunch of other account IDs you probably use for development and testing of the integration. Again, the world is not ending but it’s not ideal. AWS is looking into ways it can prevent this or at minimum make the implications clear in documentation.

If you like one liners, here is how you get the account IDs of all of your favourite AWS security products:
  
  
  aws securityhub describe-products | jq '.Products[] | {CompanyName: .CompanyName, ProductName: .ProductName, AccountId: (.ProductArn + " " + .ProductSubscriptionResourcePolicy) | scan("\\d{12}")}'

The awesome [fwd:cloudsec](https://fwdcloudsec.org/) team maintains an open source list of known AWS account IDs and their owners [here](https://github.com/fwdcloudsec/known_aws_accounts).

### Are we done here?

Mostly but there are just a couple of other quirks that may some implication in even more niche scenarios.

  1. Imagine that a customer stops using your fancy security product. They stop paying you and get their office back, so you deactivate their account. No one is happy about the breakup but at least you don’t have to see each other any more. However, if you are the jealous or clingy kind of product developer you can still send that former customer findings to their Security Hub hub. Why? Because they gave you permission and haven’t taken it back. Of course, they can remove permission at any time. AWS is updating documentation to make sure partners also include off-boarding guidance for their customers.
  2. In order to create a finding in SecurityHub, you make a call like aws securityhub batch-import-findings, which accepts a JSON blob the size of a 90s enterprise XML document. Eventually the values contained in that blob end up being displayed in web console dashboard. Two of those fields (SourceURL and Resources[].Id ) sometimes end up becoming links, and if they are controlled by a bad person, could end up being links to bad stuff. No one wants to get rick rolled from their AWS web console! AWS is moving quickly to add validation so this won’t be a concern for long.

![source-url-arbtirary-clickable-masked.png](https://cdn.prod.website-files.com/663cfee0a192fe7e5bd05ee8/66a09c77ae44b458c4f5acce_source-url-arbtirary-clickable-masked-1.png-1.webp)

### Story time was nice, but what do I need to do?

Congratulations on making it this far. You are amongst the 0.00000001% of the earth’s population who is either building an AWS SecurityHub integration or likes cloud security content so much you couldn’t help yourself. As a reward, here are the practical steps you can take to protect yourself against the oddities described above.

  * Include a validation step when asking customers which account to send Security Hub findings to. Ideally you’ve validated ownership of accounts already, so you can pop those in a list to choose from. This will prevent the deputy (your product) from getting confused. Alternatively this step is totally unnecessary if findings are only ever delivered to the account they are found in AWS reference architecture.
  * When generating the findings and sending them to Security Hub, include some standard authorization logic to ensure data never goes to the wrong tenant. There are a number of ways to approach this but they are typically language dependant. Making this a part of your product’s security model will help generalize the protection to prevent similar issues in other places.
  * Consider not using your existing AWS accounts for the sending and receiving findings. Instead create special purpose accounts for SecurityHub integrations. That way you will never leak your important AWS account IDs, and not expose yourself to unwanted reconnaissance from annoying hackers.
  * Update your customer off-boarding process to include customers un-accepting notifications from your SecurityHub product integration. This will ensure that findings never end up back in a former customer’s dashboard unexpectedly.
  * Ensure that users cant influence what is put in the SourceURL and Resource.Id fields of findings. These should be system generated only to prevent them being abused to craft malicious links in the AWS web console.

### If you enjoyed this blogue…

You might also enjoy our no-longer-vulnerable-to-any-of-this-nonsense Plerion Cloud Protection Platform, which integrates securely with SecurityHub.

‍
