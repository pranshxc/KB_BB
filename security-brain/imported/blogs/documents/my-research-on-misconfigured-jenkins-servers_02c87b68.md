---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-18_my-research-on-misconfigured-jenkins-servers.md
original_filename: 2018-01-18_my-research-on-misconfigured-jenkins-servers.md
title: My Research on Misconfigured Jenkins Servers
category: documents
detected_topics:
- jwt
- automation-abuse
- cloud-security
- oauth
- sso
- saml
tags:
- imported
- documents
- jwt
- automation-abuse
- cloud-security
- oauth
- sso
- saml
language: en
raw_sha256: 02c87b68be9da155604d28a8e60219347ba6589015c6b791ffa81164071b22a9
text_sha256: d509a03d647aedd0aa0463e15b80ff39f1d4c35682a0977bf930c8bc93a0dd47
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# My Research on Misconfigured Jenkins Servers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-18_my-research-on-misconfigured-jenkins-servers.md
- Source Type: markdown
- Detected Topics: jwt, automation-abuse, cloud-security, oauth, sso, saml
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `02c87b68be9da155604d28a8e60219347ba6589015c6b791ffa81164071b22a9`
- Text SHA256: `d509a03d647aedd0aa0463e15b80ff39f1d4c35682a0977bf930c8bc93a0dd47`


## Content

---
title: "My Research on Misconfigured Jenkins Servers"
page_title: "My Research on Misconfigured Jenkins Servers – Mikail's Blog"
url: "https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/"
final_url: "https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/"
authors: ["Mikail Tunç (@emtunc)"]
programs: ["Google", "Tesco", "Pearson", "News Uk"]
bugs: ["Information disclosure", "Missing authentication", "Exposed Jenkins instance"]
publication_date: "2018-01-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6006
---

Categories 

[Tech](https://emtunc.org/blog/category/tech/)

# My Research on Misconfigured Jenkins Servers

  * Post author  By [Mikail](https://emtunc.org/blog/author/e-mikail-t/)
  * Post date  [January 18, 2018](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/)
  * [26 Comments on My Research on Misconfigured Jenkins Servers](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comments)

Late last year I decided to see how many misconfigured CI/CD (continuous integration and deployment) installations I could find on the internet. I decided to focus my research on one of the most popular CI/CD applications – [Jenkins](https://en.wikipedia.org/wiki/Jenkins_\(software\)). This article isn’t an attack on Jenkins in any way shape or form – any piece of software and/or hardware can be configured incorrectly… it just so happens to be that CI/CD servers often host some very sensitive configurations – some of which I will come on to in a bit.

### What is Jenkins?

Jenkins is a continuous integration/deployment web application built in Java. It is designed to run ‘something’ (usually tests to ensure the new code _works_ and doesn’t break production) every time a developer commits code to a repository (Github being the most common) then  _delivering_ that tested/working code to an environment such as a production AWS account.

Given the nature of the beast, Jenkins typically requires credentials to the code repository **and** access to an environment in which to deploy the code to – in my research this was mainly AWS and Azure, in that order.

Given its position in the workflow, Jenkins is a **very** attractive target for attackers.

### How did you find misconfigured Jenkins boxes?

I used my good friend [Shodan](https://www.shodan.io) to do the heavy lifting for me. I used a few search queries to narrow down Jenkins servers in regions and hosting providers I was personally interested in looking at.

### What did you do?

As of this post there are approximately 25,000 Jenkins hosts exposed on the internet. I looked at about half of them and that alone took several weeks of my time – most of which was spent manually validating issues as well as reporting said issues to organisations where possible.

I ran a few searches on Shodan and downloaded the reports in .csv format. I created a list of URLs to crawl – specifically I was interested in Jenkins instances which required no authentication, instances with the self-registration link present and lastly, instances that had a SSO/SAML integration.

If I found that self-registration was enabled, I would register a test account on the instance and see if I was granted any permissions.

If SSO functionality/plugins were present then I would attempt to log-in to the application using a test account (i.e., a test Github/Bitbucket account).

If I gained access to a Jenkins instance (either by default or by registering/logging in with a test account) then I immediately attempted to find out which organisation it belonged to by checking the ‘system’ and ‘credentials’ pages.

**I want to make it absolutely clear that I did not exploit any vulnerabilities to gain access to Jenkins servers – I simply walked through the front door which was visible to the world, then told the owners to close said front door.**

### What issues did you find?

  * I will confidently say that between 10-20% of Jenkins servers I looked at were misconfigured. Misconfigured in this context means any one of the following: 
  * Wide open to the internet with either guest or administrative permissions by default – guest can be just as catastrophic and damaging as having admin rights
  * The web application was behind a log-in prompt but allowed ‘self-registration’ which granted guest or admin rights
  * The web application was behind a SAML/OAuth log-in linked to Github or Bitbucket but was misconfigured to allow **any** Github/Bitbucket account to log-in to Jenkins rather than being locked down to the organisation’s user pool
  * Almost all of the misconfigured instances also leaked one or more of the following sensitive information: 
  * Credentials to private source repositories – this includes usernames, passwords and private keys
  * Credentials to deployment environments – this was typically in the form of usernames, passwords, private keys and AWS access/secret tokens stored in plain text
  * Job log files which did not obscure private/sensitive information – it was not uncommon for me to find credentials, tokens and other sensitive information in completed job logs.

### What kind of servers did you find? What responses did you receive?

In no particular order I will list a small number of incidents I reported as well as responses received:

  * London’s government funded transport body  _Transport for London_ had a Jenkins instance which exposed credentials to internally hosted private repositories. After messaging a number of contacts on LinkedIn, I finally got through to someone. I got a ‘thanks’ from them.
  * Sainsbury’s and Tesco (two of the UK’s largest supermarkets) had misconfigured Jenkins servers. Sainsbury’s was particularly bad – they had exposed sensitive financial reports, service account credentials, Excel spreadsheets with hundreds of usernames and passwords, JWS signing keys, e-mail account credentials and much more. Of all misconfigured instances I found this was probably the worst. They valued this security disclosure with a £20 in-store voucher.
  * Google had exposed sensitive tokens on their Jenkins instance. I reported the issue via their bug bounty programme where it was quickly triaged and fixed.
  * A company who manufacturers toys for children had an exposed instance which granted administrator privileges and exposed sensitive tokens and credentials. The person I dealt with was awesome and offered to send some toys for my kids 🙂
  * Clearscore is a service used by millions of people in the UK. It allows customers to request free copies of their credit scores, reports and much more. As you probably already know – these guys hold a **lot** of sensitive data about customers so you’d think security would be a  _top_ priority (just like it was for Equifax, right guys?).  
I found an open Jenkins server that exposed artifacts, logs, credentials, tokens and more.  
After hunting around for a security contact on their website (hint: there were none) I messaged a number of employees on LinkedIn. None replied. As a last resort (the only reason I persisted is because of the sensitivity of the data they hold on unsuspecting individuals using their ‘free’ service) I e-mailed a few generic e-mail addresses and finally got a response from someone who didn’t even work in the security team. I got a ‘thanks’ from them.
  * Pearson is the largest education company and the largest book publisher in the world. They have no responsible disclosure process. Again I had to hunt for a contact on LinkedIn. Fortunately I found one. **However,** Pearson were the only company out of hundreds I contacted to respond in a negative way. It was implied that I was unprofessional for asking if they had a bug bounty programme.  
I had found two Jenkins instances which exposed SSH private keys, credentials and tokens. The last interaction I had from Pearson was on the 20th September (after I had disclosed the issues). I was supposed to hear back from them but they went quiet after my disclosure.
  * News UK is a large newspaper publisher in the UK. It’s ironic that for an organisation whose sole purpose is to have their voices heard by millions of people around the country, it is impossible to have your voice heard in order to report a serious incident. Again, no security e-mails or responsible disclosure process.  
I reached out to a number of contacts on LinkedIn – one of which accepted my request but didn’t bother actually replying to my message!  
News UK are leaking private tokens and credentials to both their WordPress instance and their AWS accounts.Of all the examples given above, News UK were the only ones to completely ignore my requests and e-mails. Unfortunately, sometimes naming and shaming organisations is the only way you can get them to notice and pay attention to security (or lack thereof). 

**Update:** The day after this article was published, someone from NewsUK got in contact with me to let me know they were going to look into and fix the issues discovered.

### Conclusion

It’s 2018 and most organisations don’t have the most basic of responsible disclosure processes in place. Surprisingly (or not) big names fall foul of this problem too.  
I ended up sending e-mails to generic security@, support@ and press@ addresses as well as attempting to track down security contacts on LinkedIn; even then most didn’t bother replying.

If you work in InfoSec or are responsible for the security of your infrastructure, now’s a good time to methodically crawl through your infrastructure to ensure you’re not unknowingly exposing sensitive interfaces to the internet. It only takes one misconfigured instance to destroy your business.

Whilst you’re at it, create a quick security page on your company website with one or two contact methods so that security researchers can contact you easily; a security researcher shouldn’t have to jump through the hoops I had to just to report a security incident.

Bug Bounties programmes can also work really well so consider starting a private programme for your business if it’s appropriate for what you do.

Here are some examples of organisations doing it right:

[Tesla Motors](https://www.tesla.com/en_GB/about/security)

[Google](https://www.google.co.uk/about/appsecurity/reward-program/)

[LastPass](https://lastpass.com/support_security.php)

[Bugcrowd – list of public bug bounty programmes](https://bugcrowd.com/programs)

### Share this:

  * [ Email a link to a friend (Opens in new window) Email ](/cdn-cgi/l/email-protection#79460a0c1b131c1a0d445c4c3b2a11180b1c1d5c4b4929160a0d5c4c3d5c4b4934005c4b492b1c0a1c180b1a115c4b4916175c4b4934100a1a16171f101e0c0b1c1d5c4b49331c171210170a5c4b492a1c0b0f1c0b0a5f5a494a41421b161d0044110d0d090a5c4a385c4b3f5c4b3f1c140d0c171a57160b1e5c4b3f1b15161e5c4b3f49485c4b3f4b4948415c4b3f0b1c0a1c180b1a115414100a1a16171f101e0c0b1c1d54131c171210170a540a1c0b0f1c0b0a5c4b3f5f5a494a41420a11180b1c441c14181015)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/?share=linkedin)
  * [ Share on X (Opens in new window) X ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/?share=twitter)
  * [ Share on WhatsApp (Opens in new window) WhatsApp ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/?share=jetpack-whatsapp)
  * [ Share on Reddit (Opens in new window) Reddit ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/?share=reddit)
  * [ Share on Telegram (Opens in new window) Telegram ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/?share=telegram)
  * [ Share on Facebook (Opens in new window) Facebook ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/?share=facebook)
  * [ Print (Opens in new window) Print ](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#print?share=print)
  * 

  * Tags  [jenkins](https://emtunc.org/blog/tag/jenkins/)

* * *

[ ← JWT Refresh Token Manipulation ](https://emtunc.org/blog/11/2017/jwt-refresh-token-manipulation/) [ → Creating a Secure Environment for your Cryptocurrency Hardware Wallet ](https://emtunc.org/blog/01/2018/creating-secure-environment-cryptocurrency-hardware-wallet/)

* * *

##  26 replies on “My Research on Misconfigured Jenkins Servers” 

[Misconfigured Jenkins Servers Leak Sensitive Data – TechBabblersays:](http://www.techbabbler.com/2018/01/19/misconfigured-jenkins-servers-leak-sensitive-data/)

[January 19, 2018 at 10:24 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5304)

[…] “I want to make it absolutely clear that I did not exploit any vulnerabilities to gain access to Jenkins servers – I simply walked through the front door which was visible to the world, then told the owners to close said front door,” the researcher noted in a blog post. […]

[Misconfigured Jenkins Servers Leak Sensitive Data | Digitpolsays:](https://digitpol.info/2018/01/19/misconfigured-jenkins-servers-leak-sensitive-data/)

[January 20, 2018 at 4:44 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5305)

[…] “I want to make it absolutely clear that I did not exploit any vulnerabilities to gain access to Jenkins servers – I simply walked through the front door which was visible to the world, then told the owners to close said front door,” the researcher noted in a blog post. […]

[Misconfigured Jenkins Servers Leak Sensitive Data – Tech News Headlinesays:](http://technewsheadline.com/misconfigured-jenkins-servers-leak-sensitive-data/)

[January 21, 2018 at 5:47 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5306)

[…] “I want to make it absolutely clear that I did not exploit any vulnerabilities to gain access to Jenkins servers – I simply walked through the front door which was visible to the world, then told the owners to close said front door,” the researcher noted in a blog post. […]

[Researchers found misconfigured Jenkins servers leaking sensitive dataSecurity Affairssays:](http://securityaffairs.co/wordpress/68028/hacking/misconfigured-jenkins-servers.html)

[January 21, 2018 at 9:16 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5307)

[…] ” wrote the expert in a blog post. […]

[因配置错误，25000个Jenkins服务器泄漏了大量敏感数据 – 安百科技says:](https://vul.anbai.com/82453.html)

[January 24, 2018 at 12:21 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5309)

[…] 最近，安全专家MikailTunç对Jenkins服务器的安全性进行了分析，发现Jenkins服务器的配置错误会泄漏大量敏感数据。不过，MikailTunç澄清说，他并没有利用任何漏洞来攻击Jenkins服务器，仅仅用于研究。 […]

[Misconfigured Jenkins Servers Leak Sensitive Data – Rassegna Stampasays:](http://rassegna.lbit-solution.it/misconfigured-jenkins-servers-leak-sensitive-data/)

[January 26, 2018 at 2:14 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5310)

[…] “I want to make it absolutely clear that I did not exploit any vulnerabilities to gain access to Jenkins servers – I simply walked through the front door which was visible to the world, then told the owners to close said front door,” the researcher noted in a blog post. […]

[![](https://secure.gravatar.com/avatar/c7735ea04a5efeea52593c67b8f23046ebe5b28b76fc7432d7ed26c403fb1949?s=120&d=monsterid&r=g)Alfiesays:](https://the-infosec.com)

[January 26, 2018 at 9:52 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5311)

Good insights! I did similar research a while back >> <https://the-infosec.com/2017/06/22/from-shodan-to-remote-code-execution-1-hacking-jenkins/>

[Hacker Group Makes $3 Million by Installing Monero Miners on Jenkins Servers – Newssays:](https://news.bullwall.com/hacker-group-makes-3-million-by-installing-monero-miners-on-jenkins-servers/)

[February 17, 2018 at 11:13 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5313)

[…] of Jenkins servers available online. In mid-January, security researcher Mikail Tunç published research highlighting that there were over 25,000 Jenkins servers left exposed to Internet connections at […]

[Hacker Group Makes $3 Million by Installing Monero Miners on Jenkins Servers - Cryptinfosays:](http://cryptinfo.net/hacker-group-makes-3-million-by-installing-monero-miners-on-jenkins-servers/)

[February 17, 2018 at 11:36 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5314)

[…] of Jenkins servers available online. In mid-January, security researcher Mikail Tunç published research highlighting that there were over 25,000 Jenkins servers left exposed to Internet connections at […]

[Hacker Group Makes $3 Million by Installing Monero Miners on Jenkins Servers | #VentureCanvas | Amrank Real Estatesays:](https://amrank.info/2018/02/17/hacker-group-makes-3-million-by-installing-monero-miners-on-jenkins-servers-venturecanvas/)

[February 17, 2018 at 11:57 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5315)

[…] of Jenkins servers available online. In mid-January, security researcher Mikail Tunç published research highlighting that there were over 25,000 Jenkins servers left exposed to Internet connections at […]

[BrokenPlanet - The post apocalypse is heresays:](https://brokenpla.net/blog/hacker-group-makes-3-million-by-installing-monero-miners-on-jenkins-servers/)

[February 18, 2018 at 1:04 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5316)

[…] of Jenkins servers available online. In mid-January, security researcher Mikail Tunç published research highlighting that there were over 25,000 Jenkins servers left exposed to Internet connections at […]

[Hackers target Jenkins servers for cryptocurrency – Top Coins Newssays:](https://topcoinsnews.com/hackers-target-jenkins-servers-for-cryptocurrency/)

[February 19, 2018 at 6:40 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5317)

[…] This isn’t the first time either that Jenkins servers have been exploited for malicious use. In January, security researcher Mikail Tunc found 25,000 Jenkins servers that were exposed to hackers. […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more - IT AND USsays:](http://itandus.com/2018/02/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 1:24 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5318)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more – Technology NEWSsays:](https://whiteeyes.design/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 1:32 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5319)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more - Blockalertssays:](http://www.blockalerts.com/all/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 2:03 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5320)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more | Coin Crypto Ramasays:](http://coincryptorama.com/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 2:11 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5321)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more | WavesWorldsays:](http://wavesworld.io/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 3:02 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5322)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more – Top Coins Newssays:](https://topcoinsnews.com/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 3:16 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5323)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[BrokenPlanet - The post apocalypse is heresays:](https://brokenpla.net/blog/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 6:24 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5324)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Заражение серверов Jenkins скрытым майнером принесло злоумышленникам более 3 млн долларов | Coin-Insider.rusays:](http://coin-insider.ru/zarazhenie-serverov-jenkins-skrytym-majnerom-prineslo-zloumyshlennikam-bolee-3-mln-dollarov)

[February 20, 2018 at 9:41 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5325)

[…] на машинах под управлением Windows. А согласно статистике, собранной независимым экспертом Михаилом Тучем (Mikail […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more – CryptoRushNews – Cryptocurrency and ICO News 2018says:](http://cryptorushnews.com/2018/02/20/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 10:19 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5326)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more | Make moneysays:](http://startupnet.biz/2018/02/20/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 1:04 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5327)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more | japan daily sunsays:](http://japandailysun.com/2018/02/20/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 20, 2018 at 1:10 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5328)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more – Crypto News indexsays:](http://cryptonewsindex.com/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 21, 2018 at 2:59 AM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5329)

[…] source automation servers. In January, independent researcher Mikail Tunç estimated that as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more – Go For The Winsays:](https://goftw.net/2018/02/21/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[February 21, 2018 at 4:07 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5330)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

[Cryptocurrency-mining criminals that netted $3 million gear up for more – Rassegna Stampasays:](https://rassegna.lbit-solution.it/cryptocurrency-mining-criminals-that-netted-3-million-gear-up-for-more/)

[March 7, 2018 at 4:04 PM](https://emtunc.org/blog/01/2018/research-misconfigured-jenkins-servers/#comment-5332)

[…] automation servers. In January, independent researcher Mikail Tunç estimated that as many as many as 20 percent of Jenkins servers are misconfigured in ways that make serious hacks possible. The compromises cause slower performance and potential […]

* * *

Comments are closed.
