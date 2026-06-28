---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-07-15_how-i-could-steal-money-from-instagram-google-and-microsoft.md
original_filename: 2016-07-15_how-i-could-steal-money-from-instagram-google-and-microsoft.md
title: How I Could Steal Money from Instagram, Google and Microsoft
category: documents
detected_topics:
- rate-limit
- command-injection
- mfa
- otp
- automation-abuse
- race-condition
tags:
- imported
- documents
- rate-limit
- command-injection
- mfa
- otp
- automation-abuse
- race-condition
language: en
raw_sha256: afb5bfc8fbccedb0691b9b1666dd9160d881bec506788a1e92f28333cc6a106f
text_sha256: 1558a4d1a269577a950bf72b161131bae7761630616e7862eae09ddeba34956d
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I Could Steal Money from Instagram, Google and Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-07-15_how-i-could-steal-money-from-instagram-google-and-microsoft.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, mfa, otp, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `afb5bfc8fbccedb0691b9b1666dd9160d881bec506788a1e92f28333cc6a106f`
- Text SHA256: `1558a4d1a269577a950bf72b161131bae7761630616e7862eae09ddeba34956d`


## Content

---
title: "How I Could Steal Money from Instagram, Google and Microsoft"
page_title: "How I Could Steal Money from Instagram, Google and Microsoft – Arne Swinnen"
url: "https://www.arneswinnen.net/2016/07/how-i-could-steal-money-from-instagram-google-and-microsoft/"
final_url: "https://www.arneswinnen.net/2016/07/how-i-could-steal-money-from-instagram-google-and-microsoft/"
authors: ["Arne Swinnen (@ArneSwinnen)"]
programs: ["Google", "Microsoft", "Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "2,500"
publication_date: "2016-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6281
---

[42](https://www.arneswinnen.net/2016/07/how-i-could-steal-money-from-instagram-google-and-microsoft/#comments)

# How I Could Steal Money from Instagram, Google and Microsoft

Posted on [July 15, 2016](https://www.arneswinnen.net/2016/07/how-i-could-steal-money-from-instagram-google-and-microsoft/ "12:54 am") by [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "View all posts by Arne Swinnen")

**TL;DR:** Instagram ($2000), Google ($0) and Microsoft ($500) were vulnerable to direct money theft via premium phone number calls. They all offer services to supply users with a token via a computer-voiced phone call, but neglected to properly verify whether supplied phone numbers were legitimate, non-premium numbers. This could have allowed a dedicated attacker to steal thousands of EUR/USD/GBP/… . Microsoft was exceptionally vulnerable to mass exploitation by supporting virtually unlimited concurrent calls to one premium number. The vulnerabilities were submitted to the respective Bug Bounty programs and properly resolved.

# Instagram: Link Account to Premium Number

Instagram supports linking a mobile phone number to an account, which allows other users to look them up in Instagram’s global address book. After entering the mobile phone number, Instagram sends a text with the 6-digit token:

[![1](https://www.arneswinnen.net/wp-content/uploads/2016/02/1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/1.png) [![2](https://www.arneswinnen.net/wp-content/uploads/2016/02/2.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/2.png)

However, if one does not enter the code within three minutes on the following screen, Instagram will **call** from California:

[  
](https://www.arneswinnen.net/wp-content/uploads/2016/02/3.png)[![3](https://www.arneswinnen.net/wp-content/uploads/2016/02/3.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/3.png) [![5](https://www.arneswinnen.net/wp-content/uploads/2016/02/5.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/5.png)

<https://www.arneswinnen.net/wp-content/uploads/2016/02/Instagram_Call.mp3>

This call would last around 17 seconds. The underlying request who causes this is the one outlined below in burp repeater:

[![4](https://www.arneswinnen.net/wp-content/uploads/2016/02/4.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/4.png)

The request to https://i.instagram.com/api/v1/accounts/robocall_user/ could only be replayed once every 30 seconds due to rate limiting. However, it was also noticed that Instagram would happily call any number that was supplied to them, such as a premium number of 0.06 GBP/minute in the UK registered via eurocall24.com:

[![6](https://www.arneswinnen.net/wp-content/uploads/2016/02/6.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/6.png) [![7](https://www.arneswinnen.net/wp-content/uploads/2016/02/7.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/7.png)

As a PoC, 60 additional calls were made in an automated fashion with Burp Intruder, each with 30 seconds throttle in between. This concluded the theft of one symbolic pound over the course of 17 minutes:

[![8](https://www.arneswinnen.net/wp-content/uploads/2016/02/8.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/8.png)

One attacker could thus steal 1 GBP per 30 minutes, or 48 GBP/day, 1.440 GBP/month or 17.280/year with one [instagram account, premium number] pair. However, a dedicated attacker could easily setup and manage 100 of these pairs, increasing these numbers by a factor 100: 4.800 GBP/day, 144.000 GBP/month or 1.728.000 GBP/year.

Additionally, it turned out that an attacker would only need one premium number and 100 Instagram accounts. The rate limiting threshold of 1 request / 30 seconds was for accounts only. The premium number could happily be used to link to different Instagram accounts concurrently.

## Facebook’s Remediation

First response of Facebook on the submission:

> This is intentional behavior in our product. We do not consider it a security vulnerability, but we do have controls in place to monitor and mitigate abuse.

Were they actually giving me a free pass to directly steal money from Instagram here?

[![moneycat21](https://www.arneswinnen.net/wp-content/uploads/2016/02/moneycat21.jpg)](https://www.arneswinnen.net/wp-content/uploads/2016/02/moneycat21.jpg)

After some discussions and extrapolating calculations from 1 to 100 accounts, Facebook elaborated:

> Thanks for following up — because these requests are routed through a dedicated service for monitoring and blocking abuse, “intentional behavior” in this case is considered “accepted risk”. Generally speaking, attacks that depend on multiple accounts under attacker control fall under the “spam or social engineering techniques” category of ineligible reports for the whitehat program.

And finally, after some more elaboration from my side (“100 accounts can be easily created manually”):

> Hello again! We’ll be doing some fine-tuning of our rate limits and work on the service used for outbound calls in response to this submission, so this issue will be eligible for a whitehat bounty. You can expect an update from us again when the changes have been made. Thanks!  
>  (…)  
>  We have looked into this issue and believe that the vulnerability has been patched (rate limits adjusted and some additional monitoring in place).

## Timeline

  * 5 September 2015: Initial bug report sent to Facebook
  * 13 November 2015: Initial decline of Facebook (see above), followed by elaboration from my side
  * 21 December 2015: Second decline of Facebook (see above), followed by elaboration from my side
  * 22 December 2015: Acceptance of the bug report
  * 6 January 2016: Vulnerability patched
  * 9 January 2016: Bug bounty of $2000 awarded.
  * 11 January 2016: Confirmation of bounty multiplication by a factor two ($4000) to donate to [Non-Profit Let Us Change Ethiopia](https://www.letuschange.net/en/), which supports street Children in Ethiopia.

I got to keep the acquired 1 GBP.

# Google: Two Factor Authentication via Premium Number

The case of Google was a tad bit more complicated. Google doesn’t call during the mobile phone linking process, but they do have an option to call to communicate a 6-digit 2FA token:

[![1](https://www.arneswinnen.net/wp-content/uploads/2016/02/1-1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/1-1.png)

Entering a premium number here would result in a phone call from Google, but the number would be blocked after a few attempts when no valid token is entered. However luckily, eurocall24.com supported forwarding the call to a SIP server (“Callcentre”) and consuming them with a SIP client (Blink in this case) so I could actually hear the message out loud:

[![2](https://www.arneswinnen.net/wp-content/uploads/2016/02/2-1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/2-1.png)

By linking a premium number to this callcentre and then entering it as 2FA mobile number, we would receive the call in our client and be able to hear & enter the correct 6-digit token to confirm it:

[![3](https://www.arneswinnen.net/wp-content/uploads/2016/02/3-1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/3-1.png) [  
](https://www.arneswinnen.net/wp-content/uploads/2016/02/4-1.png) [![5](https://www.arneswinnen.net/wp-content/uploads/2016/02/5-1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/5-1.png)

<https://www.arneswinnen.net/wp-content/uploads/2016/02/Google_Call.mp3>

[![6](https://www.arneswinnen.net/wp-content/uploads/2016/02/6-1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/6-1.png)

Once passed the registration, it was identified that Google allowed to make 10 phone calls/hour to the mobile phone number by attempting to login. Whether the call was actually received and the login was successful or not did not matter, which surprised me a bit. I was already mentally preparing myself for some SIP Server -> Voice recognition -> Selenium script chaining, but that turned out to be unnecessary.

First, the call destination for the premium number on eurocall24.com was modified to a standard “conference service”, so I wouldn’t be bothered by it anymore. Then, a selenium script to login with username & password to the 2FA-protected account was recorded with the Firefox IDE plugin & exported to a [login.py python script](https://gist.github.com/ArneSwinnen/a5edd4b47ca6a4de38e7). Last but not least, a second [quick & dirty python script loop.py](https://gist.github.com/ArneSwinnen/124aaae3390c444e4763) was designed to execute the former one every 6 minutes and executed. Two hours and 17+1 (enrollment) calls later, the symbolic Euro was mine again.

[![8](https://www.arneswinnen.net/wp-content/uploads/2016/02/8-1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/8-1.png)

[![10](https://www.arneswinnen.net/wp-content/uploads/2016/02/10.png)](https://www.arneswinnen.net/wp-content/uploads/2016/02/10.png)One call lasts for approximately 35 seconds. A quick calculation reveals that an attacker would be able to steal 12 EUR/day = 360 EUR/month = 4.320 EUR/year with one premium number at this rate. However, an attacker could easily manage and maintain around 100 premium numbers and Google accounts linked to them, multiplying the magnitude of the impact with a factor 100 to 1.200 EUR/day = 36.000 EUR/month = 432.000 EUR/year. In the case of Google, actual unique pairs of [Google Account, premium number] were required.

## Google’s remediation

> It looks like we have mitigations in place, and because of how the whole telco industry works, it’s impossible to prevent it completely from happening. The attempt to exfiltrate the money would be stopped after a short time though, as we have the mitigations in place to detect it, so there’s that.
> 
> Because of the above, the panel decided not to reward this report financially (as we said, Google money loss for our process is less important than users security). It qualified for the credit though – you’ll appear in a [Google Hall Of Fame.](https://bughunter.withgoogle.com/profile/e8446887-7b4f-4935-9961-eda983dd341f)

## Timeline

  * 9 February 2016: Initial bug report sent to Google VRP
  * 10 February 2016: Initial response of Google, suggesting I use the vulnerability to break into [please.break.in@gmail.com](mailto:please.break.in@gmail.com)
  * 10 February 2016: Email sent to Google asking for clarification
  * 11 February 2016: Response from Google saying their previous mail was not meant to be sent to me, and they are investigating the issue until further notice.
  * 16 February 2016: Initial decline of Google: “This issue has very little or no security impact, and therefore we believe that it is not in scope for the program”, followed by elaboration of my side
  * 17 February 2016: Response from Google saying that the previous mail was an automated response which shouldn’t have been sent, and they are still investigating the issue. However, adding that “Surprisingly, money is less sensitive/impactful than access to user data. That’s not to say money isn’t important, it’s just that money is easy to recover from than user trust, so while I agree it’s ironic, I think it’s better for our users like this :)”
  * 23 February 2016: Update from Google that the investigation is still ongoing
  * 1 March 2016: Final response of Google (see above).

# Microsoft: Office 365 Trial Registration with Premium Number

During Office 365 Trial Registration, one can submit a phone number to which a call is made by Microsoft. It was found that Microsoft actually called to entered premium numbers, but blocked the number after 7 failed registration attempts via this number:

[![2](https://www.arneswinnen.net/wp-content/uploads/2016/07/2.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/2.png) [![3](https://www.arneswinnen.net/wp-content/uploads/2016/07/3.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/3.png)

[![4](https://www.arneswinnen.net/wp-content/uploads/2016/07/4.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/4.png)

<https://www.arneswinnen.net/wp-content/uploads/2016/07/Microsoft-call.mp3>

However, two different bypasses for this protection mechanism were identified which allowed, many, many more calls to the premium number.

### Prepended zeroes

It was found that by prepending the number with a zero, the number would again be accepted and result in another call to the same underlying premium number. Moreover, this trick could be repeated 18 times, since the normal number prepended with 18 zeroes would still be accepted. Finally, It was found that by replacing a random prepending zero pair with the country code of the premium number’s country ( in this case 48 – Poland), the call would still be made:

[![5](https://www.arneswinnen.net/wp-content/uploads/2016/07/5.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/5.png) [![7](https://www.arneswinnen.net/wp-content/uploads/2016/07/7.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/7.png)

[![9](https://www.arneswinnen.net/wp-content/uploads/2016/07/9.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/9.png)

[![10](https://www.arneswinnen.net/wp-content/uploads/2016/07/10.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/10.png)

The following formula describes the total amount of additional number variations that can be made by exploiting this first block bypass method, where variable n describes the length of the padding in front of the phone number:

[![formula1](https://www.arneswinnen.net/wp-content/uploads/2016/07/formula1.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/formula1.png)

  * For n = 1, there is one option to prepend with “0″
  * For n = 2, there is an option to prepend with “00” or “48”
  * For n = 3, there is an option to prepend with “000”, “480” or “048″
  * …

The total number of variations for one premium number is thus 171+1=172 now.

### Appended random digits

An additional bypass was found by appending the number with maximum 4 random digits (in this screenshot, 1111):

[![11](https://www.arneswinnen.net/wp-content/uploads/2016/07/11.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/11.png)

[![12](https://www.arneswinnen.net/wp-content/uploads/2016/07/12.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/12.png)

The total number of combinations that can be made with four random trailing digits is given by the following formula, where i describes the number of trailing digits:

[![](https://www.arneswinnen.net/wp-content/uploads/2016/07/formula-2-2.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/formula-2-2.png)

  * For i = 0, there is 1 possibility (no appended digits)
  * For i = 1, there are 10 possibilities (0-9)
  * For i = 2, there are 100 possibilities (00-99)
  * For i = 3, there are 1000 possibilities (000-999)
  * For i = 4, there are 10000 possibilities (0000-9999)

Since this trailing number can be appended to any accepted number, the following calculation describes the total amount of calls that Microsoft will make to a single premium number:

(172*11111) * 7 = 13.377.644 calls/premium number

Each call takes approximately 23 seconds, so let’s take 20 to make the calculations easier. The premium number yielded 0,15 EUR/minute:

(13.377.644/3)*0,15 = **668.882 EUR/premium number**

### Concurrent calls

On top of this, Microsoft allowed concurrent calls to the same premium number. Eurocall24.com limits the number of concurrent calls from one source address to one of its premium numbers to 10, so a PoC was performed where 2*10 concurrent calls were made within less than one minute, yielding a little more than 1 EUR profit:

[![16](https://www.arneswinnen.net/wp-content/uploads/2016/07/16.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/16.png)

[![17](https://www.arneswinnen.net/wp-content/uploads/2016/07/17.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/17.png)

[![18](https://www.arneswinnen.net/wp-content/uploads/2016/07/18.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/18.png) [![20a](https://www.arneswinnen.net/wp-content/uploads/2016/07/20a.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/20a.png)

[![21a](https://www.arneswinnen.net/wp-content/uploads/2016/07/21a.png)](https://www.arneswinnen.net/wp-content/uploads/2016/07/21a.png)

In the end, an attacker could thus steal an enormous amount of money in very little time by automating this exploitation approach with multiple premium numbers.

## Microsoft’s remediation

The prepending and appending bypasses for the number blocking mechanism were fixed in two phases (March & July 2016). A $500 minimum bounty reward was my share.

> The reward decisions are made by an adjudication team for the bounty program that is making the award. We aim to grant awards based on their impact to 1) Microsoft customers and then 2) Microsoft itself. Given that there is a 3rd party that performs this service for us, the impact to Microsoft for this weakness was negligible. Even though the bulk of the risk was to a company Microsoft works with, and not Microsoft itself, we still chose to award a bounty.

> This was certainly a vulnerability, and a good one, and thus we’ve chosen to award a five hundred dollar bounty. From a security standpoint we put a premium on protecting our customers specifically, and while this vulnerability was worth awarding and fixing, we did not see a way in which our customer’s data was put at risk. We always want to encourage researchers to spend their time helping us protect the users, but in this case, we certainly want to provide a reward for helping to protect us and our partners.

## Timeline

  * 14 February 2016: Initial bug report sent to Microsoft Security Response Center
  * 15 February 2016: Initial confirmation by Microsoft
  * 11 March 2016: Initial fix communicated by Microsoft
  * 13 March 2016: Response by me that retest indicated that only the prepending bypass was fixed, not the appending bypass
  * 15 March 2016: Confirmation of retest result by Microsoft
  * 3 June 2016: Communication of Bounty value of $500
  * 6 June 2016: Question for elaboration of the Bounty decision with regards to the vulnerability impact
  * 15 July 2016: Elaboration of Microsoft with regards to the Bounty value (see above) and confirmation of the fix deployment

### [Arne Swinnen](https://www.arneswinnen.net/author/swinnenarne/ "All posts by Arne Swinnen")

![](https://secure.gravatar.com/avatar/85c6e3f06dfe5994e9c112f745d801f39266bc0c77c1deadbfed337f3aa5da49?s=70&d=mm&r=g)

[](https://www.twitter.com/ArneSwinnen)[](https://www.linkedin.com/in/arneswinnen)

Belgian. IT Security. Bug Bounty Hunter.
