---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-11_zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-.md
original_filename: 2022-02-11_zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-.md
title: '''Zero-Days'' Without Incident - Compromising Angular via Expired npm Publisher
  Email Domains'
category: documents
detected_topics:
- supply-chain
- xss
- cloud-security
- command-injection
- password-reset
- automation-abuse
tags:
- imported
- documents
- supply-chain
- xss
- cloud-security
- command-injection
- password-reset
- automation-abuse
language: en
raw_sha256: 17ed05b954390dea7f7940e01682d10b387247f0134411f3d195b238077ce6e9
text_sha256: 29bdafe817e461cbaa93492a34747cc6a3474fac3245a453425320821d9b6d84
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# 'Zero-Days' Without Incident - Compromising Angular via Expired npm Publisher Email Domains

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-11_zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-.md
- Source Type: markdown
- Detected Topics: supply-chain, xss, cloud-security, command-injection, password-reset, automation-abuse
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `17ed05b954390dea7f7940e01682d10b387247f0134411f3d195b238077ce6e9`
- Text SHA256: `29bdafe817e461cbaa93492a34747cc6a3474fac3245a453425320821d9b6d84`


## Content

---
title: "'Zero-Days' Without Incident - Compromising Angular via Expired npm Publisher Email Domains"
page_title: "'Zero-Days' Without Incident - Compromising Angular via Expired npm Publisher Email Domains – The Hacker Blog"
url: "https://thehackerblog.com/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/"
final_url: "https://thehackerblog.com/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/"
authors: ["Matthew Bryant (@IAmMandatory)"]
programs: ["GitHub"]
bugs: ["Supply chain attack"]
publication_date: "2022-02-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2913
---

# "Zero-Days" Without Incident - Compromising Angular via Expired npm Publisher Email Domains

**NOTE:** _If you’re just looking for the high level points, see the “The TL;DR Summary & High-Level Points” section of this post._

Recently I took an interest in the [npm registry](https://www.npmjs.com/) due to it’s critical role in the security of managing packages for all of JavaScript and Node. After registering an account and creating an example package, I began looking through various web endpoints to understand what sort of system I was dealing with.

While browsing various popular packages, I noticed one fairly unique thing to the registry: email addresses for all users are public. For example, requesting my own [profile page](https://www.npmjs.com/~mandatory) returned my email address:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image14.png)

_HTTP response including my npm account email._

Spam concerns aside, this is an interesting choice for a registry as it publicly discloses the email addresses for maintainers of all npm packages. An attacker could use this to enumerate the emails of all maintainers for an npm package and utilize them in a targeted spear phishing campaign, for example. In any case, these sorts of phishing attacks are well-known and not of particular interest for research. However, there may be more novel ideas to consider…

## Custom Email Domains & Developer Culture

Upon viewing more packages and maintainers, another pattern began to emerge: emails at developer-owned domains. As many developers will tell you, having an email at your own domain is peak nerd street cred. I hate to admit it, but when someone gives me their email and I notice it has a custom domain, I subconsciously think “this person may know a thing or two about computers”.

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image3.gif)

_Average nerd reaction to receiving another nerd’s email with a custom domain._

Of course, these custom emails are not just used for social communication. They are used for all of the various accounts that developers utilize. As you may have guessed, one of those online accounts could very well be a developer’s account on the npm registry.

This raises a point that I don’t think many developers consider. By registering and using a custom domain as their main email address, they implicitly give that domain [and their TLD](https://thehackerblog.com/the-io-error-taking-control-of-all-io-domains-with-a-targeted-registration/) complete control over most of their online accounts. While not universally true, often if you have control of someone’s email account you can get access to their online accounts by simply initiating and completing the password reset process for each site. Again, the npm registry is no exception to this. If you have control of someone’s email you can reset the npm account’s password and take over the account.

## Ticking Towards Vulnerable, Domain Expiration

Domains for the most part are not free, and require continually paying a fee to keep them under your control. Over a long enough time period this can prove problematic, because often these domains can end up expiring and becoming available for registration by other people. I’ve written about vulnerabilities caused by this [as far back as 2015](https://bishopfox.com/blog/noscript-bypass-advisory), and overtime I’ve only seen more and more potential for attacks utilizing this issue.

I was curious if any of the maintainers of popular npm packages had emails which were hosted on expired domain names. From past experience, if you have a somewhat probable event and you cast a wide-enough net, it reasons that you’re likely to get results. With this in mind, I wrote a custom script to scrape the maintainers for the top 1,000 npm packages and the dependencies they depend upon. For each package I pulled the full list of developer emails, extracted the email base domains, and checked if these domains returned a [status (`RCODE`)](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6) other than [`NOERROR`](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6). The idea being that if the domains returned a non-standard error code when queried, they might be expired or exploitably-misconfigured.

## Results, Registrations, and Resets

The results met expectations: lots of [`NXDOMAIN`](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6) (domain not found) and other DNS errors in the domains extracted from maintainer emails. Many of these domains were for smaller packages without many weekly installs, but a few were from packages that were quite popular.

For example, the package [`ajv-formats`](https://www.npmjs.com/package/ajv-formats) has a maintainer [`additiveamateur`](https://www.npmjs.com/~additiveamateur) with an email address of `carlo[@]machina[dot]bio`. The package is quite popular, with ~5 million installs a week on npm at the time of this writing:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image12.png)

_Weekly package downloads of[`ajv-formats`](https://www.npmjs.com/package/ajv-formats) as of Feb 6, 2022._

This domain name returned an `NXDOMAIN` error and was available for registration. In order to confirm that it was actually possible to take over the [`ajv-formats`](https://www.npmjs.com/package/ajv-formats) package with this expired domain, I proceeded to register it:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image11.png)

_Registration confirmation of`machina.bio`_

Once the domain was registered, I configured the domain’s DNS to route email from `carlo[@]machina[dot]bio` to my personal email inbox. With emails routing for this address, I then initiated the password-reset process for the [`additiveamateur`](https://www.npmjs.com/~additiveamateur) npm user:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image8.png)

_Recover password prompt on the npm registry website._

However, I encountered an unexpected error upon submitting the request:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image17.png)

_Error message upon submitting the password reset request._

Checking the raw HTTP response provided some clarity on the potential problem:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image6.png)

_Raw HTTP response detailing error from password reset._

This type of thing is exactly why doing end-to-end confirmation for theoretical vulnerabilities is so important. To quote Benjamin Brewster: [_“In theory there is no difference between theory and practice. In practice there is.”_](https://quoteinvestigator.com/2018/04/14/theory/).

What caused this account to be flagged in this way? Was there some npm security check created to lock all accounts with emails at expired domains? That would be an impressive level of defense-in-depth, but perhaps there is a more simple explanation at play.

## Contacting Support

I wanted to see if contacting support was actually a real barrier to exploitation of these accounts. In order to do this, I submitted a support ticket intentionally written to be as basic as possible:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image13.png)

_Intentionally basic support ticket submission to test the “contact support” roadblock._

I didn’t want to bias the test by using any persuasive language or social engineering, so I kept the ticket message plain. I simply noted that I’m getting an error when resetting the password for the account and I’d like it to be unblocked. If support required further verification to do this, or if there was some other hurdle, then the plan was to conclude the research there.

However, after three days of waiting, I received the following response from npm support:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image10.png)

_Response from support confirming that the ability to reset passwords has been re-enabled._

Support confirmed that they had re-enabled the ability to reset passwords for the account. Their response seemed to indicate that the account was flagged due to previous issues sending emails, which would be expected with the domain having expired.

Perhaps a much more simple explanation for the restriction was that they had issues delivering to the email address on file previously, and as a result email-sending features were disable for the account. This would make sense, as [bouncing emails can hurt your email sender reputation](https://docs.aws.amazon.com/ses/latest/dg/send-email-concepts-deliverability.html#send-email-concepts-deliverability-bounce) and get your emails marked as spam.

In any case, the support roadblock was not an actual preventative measure in this case.

## Taking Over the `additiveamateur` Account

I then again attempted to reset the password for the `additiveamateur` account. This time I was greeted with a confirmation that the reset had succeeded and that a reset link was sent to the email address for the account:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image5.png)

_Confirmation prompt that the password reset was successful._

Sure enough, I received an email with a link to reset the account password for the account in my inbox:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image7.png)

_Password reset email received for the account._

The next steps were about what you’d expect, I set a new password and was then able to successfully log in as the `additiveamateur` account:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image1.png)

_Screenshot of options once logged in to the`additiveamateur` account._

As expected, the account had full access to the [`ajv-formats`](https://www.npmjs.com/package/ajv-formats) package:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image9.png)

_Settings page for[`ajv-formats`](https://www.npmjs.com/package/ajv-formats), demonstrating admin access to the package. Screenshot dated January 15th, 2022._

At this point, I was satisfied that the impact was proven and I ceased testing on the issue. I didn’t push any updates to the package because I believed the risk of affecting developers far out-weighed the benefit of proving the entire attack chain. Clearly this was possible, so I believed that taking this extra step would be unnecessary (and potentially reckless).

However, there was something that was still bothering me: _why was this package being installed so frequently_? The package seemed useful of course, but ~5 million installs a week (and rising) is a huge amount. This was not adding up, so I did a bit more digging. I reported the issue responsibly to the vendor but it was marked as Informative, see the disclosure timeline for more details.

## Through the Fire & Flames of Dependency Hell

The npm registry website has a nice feature which allows you to see the packages that depend on a given npm package. Using this, I took a look at [the packages which would install `ajv-formats` as a dependency when they were installed](https://www.npmjs.com/browse/depended/ajv-formats):

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image15.png)

_A few of the packages which install the package as a dependency._

The package was a dependency of both [`@angular-devkit/core`](https://www.npmjs.com/package/@angular-devkit/core) and [`schema-utils`](https://www.npmjs.com/package/schema-utils). What happens when we go one level deeper and find the dependencies of these packages?

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image2.png)

_Packages with a dependency on`*@angular-devkit/core`_.*

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image16.png)

_Packages with a dependency on[`schema-utils`](https://www.npmjs.com/browse/depended/schema-utils)._

Shockingly, the [`ajv-formats`](https://www.npmjs.com/package/ajv-formats) package was a transitive dependency for both the Angular CLI and for `webpack`! A quick sanity check confirmed that when I installed the Angular CLI, I was also installing the [`ajv-formats`](https://www.npmjs.com/package/ajv-formats) package:

![alt text](https://docpusher.s3.amazonaws.com/images/fece4fff8be683f3787a6f14d791d467/image4.gif)

_Installing the Angular CLI and confirming that the[`ajv-formats`](https://www.npmjs.com/package/ajv-formats) package is also installed._

For those not as familiar with Angular, [the Angular CLI is essentially required for building and deploying Angular apps](https://angular.io/guide/deployment) (unless you’re using a third-party builder).

This result seemed to clearly confirm the real-world impact of this vulnerability, had it been exploited by an actual malicious attacker. Notably there were a few other popular packages which were exploitable in this same fashion (registration of developer email domains), but in the spirit of keeping this writeup succinct I’ve decided not to include them in this post.

**NOTE:** As of the time of this writing, the [`webpack`](https://www.npmjs.com/package/webpack) package is pinned to [`schema-utils`](https://www.npmjs.com/package/schema-utils) version [3.1.1](https://www.npmjs.com/package/schema-utils/v/3.1.1) which does _not_ include [`ajv-formats`](https://www.npmjs.com/package/ajv-formats). As such, it would not be transitively installed until [`webpack`](https://www.npmjs.com/package/webpack) updated the version of [`schema-utils`](https://www.npmjs.com/package/schema-utils) that it depends upon. This would be a natural requirement in all cases of backdoored npm packages, and a more nuanced perspective is included below.

## Is There Any Backstop? The Nuance of Exploiting Users of Transitively-Dependent Packages

This research raises a number of interesting questions around npm dependencies, and just how serious the impact the compromise of a transitive dependency is. For example, if you have a package which has a dependency on another package and that sub-package is compromised, is the main package compromised as well?

As with most things in software, the answer is nuanced.

### What You Cannot Do In the npm Registry

To introduce the more interesting pieces of dependency security, a few key points need to be mentioned about how packages work in npm. Specifically it’s important to note that:

  * [You cannot “overwrite” an already-published version of a package](https://docs.npmjs.com/unpublishing-packages-from-the-registry#when-to-unpublish). If you’ve published a `[[email protected]](/cdn-cgi/l/email-protection)` version, for example, you can’t suddenly push a backdoored package to that same exact version. Notably [this was not always the case](https://blog.npmjs.org/post/141577284765/kik-left-pad-and-npm.html).

  * [You can only unpublish a package version if it’s less than 72 hours old and no other packages depend on it.](https://docs.npmjs.com/unpublishing-packages-from-the-registry) (So no, you can’t get clever and delete a version only to republish a backdoored version.)

This removes the most immediate path for compromising downstream packages, leaving us with the obvious alternative of pushing a new and backdoored version instead. Updating package dependencies is a regular part of package maintenance after all, and it happens regularly across the npm ecosystem.

### Pinning Dependencies With `package-lock.json` & the Dependency Security Catch-22

Those familiar with the world of dependency security will also be familiar with the catch-22 of “pinning your dependencies”. In the case of npm, this usually means to have a [`package-lock.json`](https://docs.npmjs.com/cli/v8/configuring-npm/package-lock-json#description) file which specifies the entire dependency tree for your project. With this file sitting in your root project folder, `npm install` commands will now always install all of your dependency versions as they were when you ran `npm install` to generate the file. Rogue packages updates are no longer your concern since you’re not updating! Problem solved, _right_?

However, this leaves another potentially more serious problem: vulnerable libraries are no longer being updated. If you’re pinning all your dependencies (and their dependencies), then you’ll never receive bug fixes and critical patches. In the [wake of the log4j vulnerability](https://www.lunasec.io/docs/blog/log4j-zero-day), this is clearly not an ideal route to take. Like most things in security, it’s a risk tradeoff decision. You weigh the pros and cons of each and proceed accordingly.

### Marking a Package as “Vulnerable” to Push Downstream Packages to Update to Your Malicious Version

What if an attacker were to intentionally flag their compromised package as “vulnerable”? Where would that leave dependent packages? Authors of packages which depend on the attacker’s package now have to make a decision on the exact catch-22 we mentioned before. If they _don’t update_ their dependencies, they risk putting all those who utilize their package at risk of being “vulnerable”. However, if they _do update_ their dependencies, they risk a whole slew of new code being incorporated into their package.

### Can’t We Just Review _Everything_ Before We Update?

That raises another question, _can’t maintainers and developers just review all of the new code in each dependency before including the updated versions?_

The most obvious rebuttal to this idea is probably self-evident: _it’s a ton of work_. We’re talking about going over diffs for the dependencies themselves, their dependencies, and so on. Doing so with any serious level of rigor is a large time-consuming effort. A vast majority of full time software developers aren’t reviewing every change in their dependencies, let alone volunteers who maintain packages in their own personal time. Asking these volunteers to do this daunting task seems unrealistic, to say the very least.

The problem only becomes more murky when you factor in the ability to specify [version ranges in your package.json](https://docs.npmjs.com/cli/v8/configuring-npm/package-json#dependencies). If you have a dependency that allows for flexibility in its dependencies (e.g: `>=package_name`) then a developer could later publish an update to a new version, and they would be included in fresh installs. This means that you could review all of your dependencies, find nothing malicious, and then be seamlessly backdoored later.

### Some Homework and Some Thoughts

For those interested in doing a bit of learning and research themselves, take a stab at looking at the process for updating dependencies in Angular. In my opinion Google actually does a fairly good job of it (all things considered). Here’s an example pull request to get you started: <https://github.com/angular/angular/pull/45013>

If not Angular, pick any popular package that you use in your JavaScript development. When you research the process, ask yourself some of these questions:

  * _“Would this process catch a rogue dependency update which is malicious?”_

  * _“Would it catch a malicious update to a dependency-of-a-depency?”_

  * _“Does it prevent dependencies that specify a version range instead of a specific singular version?”_

  * _“Are packages being regularly updated to ensure vulnerabilities are being regularly patched?”_

This is not a quiz and there are no gotchas or simple answers, this is meant to have you seriously think about the problems being faced in dependency security. The real world is filled with nuance and hard problems and software development is no exception!

## Wait, What About the Expired Email Domains Problem?

Clearly dependency security is a complex issue, so let’s focus on the more simple issue here: expired domains in account emails. In this case, there are a few important pieces to consider:

  * Custom domains are a common part of developer culture, and they are unlikely to go away. They carry a real risk of being exploitable when these domains expire, and developers should give serious consideration of this problem when using them for their important accounts.

  * During this research the npm accounts weren’t the only accounts which were suddenly hijackable upon registering the expired domains. Accounts on all sorts of important websites such as Github, Slack, etc were also in jeopardy. Any website which uses emailed password resets as a single-factor for account access has this problem.

  * Sites may want to proactively disable accounts when their email domains expire or become non-routable. They will also likely need to have an alternative path to reset the account’s password that strongly verifies the person is the owner of the account when this happens and the original account owner needs to get access to their account again.

In the npm case, I reported the problem to them (the Github security team) via HackerOne which they require for vulnerability reports. They closed the report as “Informative” and noted that “ _This is something we’ve been tracking internally and have mitigations in place for_ ”. Whether or not they implemented any new changes is unclear. See the disclosure timeline below, or [this archive of the HackerOne report for more info](https://imgur.com/a/7TQs3vx). I would probably advise npm users to proceed with the assumption that this is still a problem that could be exploited.

## The TL;DR Summary & High-Level Points

  * Developers for highly-installed npm packages had their npm accounts registered to email addresses at expired domains.

  * Registering these expired domain names allowed for the takeover of important npm packages such as [`ajv-formats`](https://www.npmjs.com/package/ajv-formats) which currently has ~5 million installs a week.

  * The [`ajv-formats`](https://www.npmjs.com/package/ajv-formats) package is a dependency of [`@angular-devkit/core`](https://www.npmjs.com/package/@angular-devkit/core), Angular’s core utility library. [`@angular-devkit/core`](https://www.npmjs.com/package/@angular-devkit/core) is a dependency of [`@angular/cli`](https://www.npmjs.com/package/@angular/cli), which is the tooling [used to compile Angular apps](https://angular.io/start/start-deployment#prerequisites).

  * Dependency security is a complex problem with risk tradeoffs that should be weighed carefully.

  * Developers using custom domains for their email address should seriously consider the risks they are taking on by using the email for their online accounts. If this domain expires or is hijacked, where does that leave them?

  * It’s unclear if npm has changed anything as a result of my report to them and npm users should likely assume that this issue could still be exploited in the future.

## Disclosure Timeline

### `ajv-formats`/`machino.bio` Domain Disclosure

  * _Jan 10, 2022_ : Reached out to the owner of `machina.bio` domain via LinkedIn to disclose the issue.

  * _Jan 15, 2022_ : Realized I had missed a reply to the LinkedIn reachout with the developer’s email. Sent details of disclosure to the email address provided.

  * _Jan 21, 2022_ : Received a response to `machina.bio` domain disclosure email.

  * _Jan 22, 2022_ : Followed up with credentials for npm account and `machina.bio` domain transfer code to complete handover.

### npm Registry (Github Security Team) Disclosure

  * _Jan 17, 2022_ : Submitted HackerOne bug to Github’s bug bounty program, due to [npm’s site](https://www.npmjs.com/support) requesting bugs be submitted via this avenue. [Report ID #1452186](https://hackerone.com/reports/1452186).

  * _Jan 25, 2022_ : Github security team closes the bug as invalid _“Because this attack vector included submitting a support request to re-enable password resets for a disabled account, this is considered social engineering and is therefore ineligible for a reward under the Bug Bounty program.”_. They also considered the issue mitigated _“​​This is something we’ve been tracking internally and have mitigations in place for.”_

  * _Jan 25, 2022_ : Requested public disclosure due to the bug being apparently mitigated and because the report was closed as Informative.

  * _Feb 2, 2022_ : Github denies disclosure request due to bug being closed as Informational. However, they state that publishing a write up is completely fine. You can see the full HackerOne report as an image here: <https://imgur.com/a/7TQs3vx>

—

_Special thanks to[Michael Xu (@michaelxproxy)](https://twitter.com/michaelxproxy) for consulting with me on this topic. His feedback was essential for the sections on the nuances of package-pinning._

Matthew Bryant (mandatory)

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=/zero-days-without-incident-compromising-angular-via-expired-npm-publisher-email-domains-7kZplW4x/ "Share on Google Plus")

[About the Author](https://thehackerblog.com)

### Matthew Bryant (mandatory)

![Matthew Bryant \(mandatory\)](/images/avatar.jpg)

Security researcher who needs to sleep more. Opinions expressed are solely my own and do not express the views or opinions of my employer.

  * [__](https://github.com/mandatoryprogrammer)
  * [__](https://www.linkedin.com/in/matthew-bryant-a9403289/)

[Follow @mandatoryprogrammer](https://github.com/mandatoryprogrammer)  
[Follow @IAmMandatory](https://twitter.com/IAmMandatory)

[Read More](/video-download-uxss-exploit-detailed/)

### [Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass (~15.5 Million Affected)](/video-download-uxss-exploit-detailed/ "Video Downloader and Video Downloader Plus Chrome Extension Hijack Exploit - UXSS via CSP Bypass \(~15.5 Million Affected\)")

Note: This post is going to be a bit different from the previous Chrome extension vulnerability writeups. I’m going to actually walk thro...… [Continue reading](/video-download-uxss-exploit-detailed/)

#### [Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions](/kicking-the-rims-a-guide-for-securely-writing-and-auditing-chrome-extensions/ "Kicking the Rims – A Guide for Securely Writing and Auditing Chrome Extensions")

Published on June 12, 2018

#### [Steam, Fire, and Paste – A Story of UXSS via DOM-XSS & Clickjacking in Steam Inventory Helper](/steam-fire-and-paste-a-story-of-uxss-via-dom-xss-clickjacking-in-steam-inventory-helper/ "Steam, Fire, and Paste – A Story of UXSS via DOM-XSS & Clickjacking in Steam Inventory Helper")

Published on June 07, 2018
