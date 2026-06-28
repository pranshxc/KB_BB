---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-06_from-399-to-1650-usd-part-i-simple-vertical-privilege-escalation-by-changing-htt.md
original_filename: 2020-06-06_from-399-to-1650-usd-part-i-simple-vertical-privilege-escalation-by-changing-htt.md
title: From 3,99 to 1,650 USD (Part I) – Simple Vertical Privilege Escalation by Changing
  HTTP Response
category: documents
detected_topics:
- sso
- access-control
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: de246de188fcfe1487b0b61c2ea4c6d075a85df4aebd63553709df8a467463f1
text_sha256: cc42884987982340e7d3940b9cbc28d73787feaa715d3379489235115950e254
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# From 3,99 to 1,650 USD (Part I) – Simple Vertical Privilege Escalation by Changing HTTP Response

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-06_from-399-to-1650-usd-part-i-simple-vertical-privilege-escalation-by-changing-htt.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `de246de188fcfe1487b0b61c2ea4c6d075a85df4aebd63553709df8a467463f1`
- Text SHA256: `cc42884987982340e7d3940b9cbc28d73787feaa715d3379489235115950e254`


## Content

---
title: "From 3,99 to 1,650 USD (Part I) – Simple Vertical Privilege Escalation by Changing HTTP Response"
page_title: "From 3,99 to 1,650 USD (Part I) – Simple Vertical Privilege Escalation by Changing HTTP Response – Just Another Simple Write-Up"
url: "http://www.firstsight.me/2020/06/from-399-to-1650-usd-part-i-simple-vertical-privilege-escalation-by-changing-http-response/"
final_url: "http://firstsight.me/2020/06/from-399-to-1650-usd-part-i-simple-vertical-privilege-escalation-by-changing-http-response/"
authors: ["YoKo Kho (@YokoAcc)"]
bugs: ["Privilege escalation"]
bounty: "1,000"
publication_date: "2020-06-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4522
---

[Bug Report](http://firstsight.me/category/bug-report/) / [Web Apps](http://firstsight.me/category/web-apps/) / [Write-Up](http://firstsight.me/category/write-up/)

# From 3,99 to 1,650 USD (Part I) – Simple Vertical Privilege Escalation by Changing HTTP Response

June 6, 2020 

[__]()

A story about how I got several simple bugs (1 P2, 1 P3, and 2 P4s) on a target (that just allow Specific Country Code to Register) by using Premium Phone Number.

**In the name of Allah, the Most Gracious, the Most Merciful.**

* * *

As usual, I will try to release this article with two different approaches, which are:

  * For those who only need the main points of this finding (as usual, InshaAllah it can saves tons of minutes if readers understanding every flow already) – please kindly see the TL;DR section, and
  * For those who need to understand the flow of execution or journey about this finding. InshaAllah, it can tell the readers about some mindsets and hopefully can help people to enrich their insights.

Please kindly enjoy the story.

* * *

### **I. TL;DR**

Here are the simple 7 points about this issue:

  * Target only allow people to register their accounts with certain country code phone numbers.
  * Use applications that can generate virtual phone numbers to receive phone calls or sms. Since I need 2 different accounts with different phone numbers, then I use [2ndline (free to get a number with several conditions)](https://www.2ndline.co/) and [Hushed (should pay to get a number).](https://hushed.com/)
  * Create two accounts on the same entity, namely as an “**administrator** ” and as a “**staff** “.
  * Log in into the application and try searching for common parameters such as “**isAdm** “, “**isAdmin** “, “**isAdministrator** “, or anything like that (“Adm” can be a “Root”).
  * Change the value of “**isAdm** ” parameter from “**false** ” to “**true** ” when logging in with “**staff** ” account. And also change the value of “**Edit** ” parameter from some number to “**1** ” (it will provide ability to edit the available settings/configurations). 
  * Success to escalating the “**staff** ” account to “**administrator** ” privilege.
  * Few weeks later (after some intensive discussion with the program owner because of some problem), Alhamdulillah, finally it was marked as P2 and rewarded with 1,000 USD.

![The Bug was Marked as P2](http://www.firstsight.me/wp-content/uploads/2020/06/image.png)Figure 1 The Bug was Marked as P2

* * *

### **II. THE JOURNEY**

I forget exactly when I received this invitation, but I believe that this program has stay on my “private homepage” for about 1 year. (Please don’t ask the program name, I won’t answer it).

One day, I decided to look at every private program in my dashboard and see the number of “vulnerabilities rewarded”. **Please note** , there are no proof / clear reasons for this, but sometimes, I feel more comfortable with low numbers of “vulnerabilities rewarded”, although in reality there are several conditions that cause this to happen such as:

  * The target is very difficult,
  * There is no user interest yet about this program (range of bounty, ethical objections, etc.),
  * The program invited not many researchers but researchers who were invited had many programs to deal with, or
  * The researchers are still focused on specific program (and yes, sometimes it’s not easy for us to learn targets from the basics again) -> unless you want to focus on certain types of vulnerabilities on specific features. So it is not too difficult to change targets.

The reasons can vary, but as said, sometimes I feel more comfortable with low numbers of rewarded reports although not everyone agree with this. After spending a little time, I finally came to this program (below 100 reports).

* * *

#### **2.1. Registering Our Account**

When testing targets, it’s better to have some account so that we can have a broader view of the target itself (not mandatory, but nice to have). By logging in, we also have the opportunity to see many functions in it that might have a risk to other users or application owners. In short, this situation will make testers have more “playground” to be able to find potential risks in it.

Back to topic. At the first time, I was very happy when I saw a feature that allows us to register an account for free. But the pleasure was delayed immediately when I found the need for a phone number with a certain country code and need us to verify it.

I never imagined, the challenge had begun before I even started testing it. So, here are some things I did to register an account:

  * I tried several bypasses to identify whether I could register with my own phone number, but it did not give good results (read: failed).
  * I also tried using a number of free public SMS receivers, and yes (as you might guess), phone numbers are already in use.
  * And finally, I tried to reset the password by using those public phone numbers, but the target blocked it. I assume, many people try to use it by reset the password.

* * *

#### **2.1.1. The Used of Virtual Phone Number Service**

Almost desperate because I also don’t have colleagues who live there to be asked for help, but Alhamdulillah, finally I remembered a colleague who likes to use WhatsApp numbers from overseas even though he lives in Indonesia. 

From there, I’m trying to find out about the application that might help me do that (can provide us a unique phone number with a specific country code), and am so glad, I found the [2ndline application](https://www.2ndline.co/) (free with several conditions) that can be used to registering my account 1st account, and [Hushed application](https://hushed.com/) (the premium one) to registering my 2nd account.

![Left \(Hushed - Premium\) - Right \(2ndline - Free\)](http://www.firstsight.me/wp-content/uploads/2020/06/image-1-1024x488.png)Figure 2 Left (Hushed – Premium) – Right (2ndline – Free)

**Notes:**

  * I do not intend to promote the application. I only tell what I get from googling and what I use.
  * And let’s skip the registration process for make this part more simpler (because the point that I want to explain is how we can get a virtual phone numbers from overseas).

So, by using both of those applications, I successfully registered 2 accounts on the same entity. One of them was registered as “administrator” and the other one as a “staff”.

One account with 2ndLine App (free to get a virtual phone number with several conditions) and another account with Hushed App (that made me should pay 3,99 USD for one week access). With this limited access, then I should optimizing the test.

* * *

#### **2.2. The Test!**

#### **2.2.1. I have 2 Different Type of Accounts, what should I do?**

Basically, there are few things that can be done when we have access to the application (read: log in). But personally, I like to test the logic thing first. And in this case, a privilege escalation (either horizontal or vertical).

So, now I have 2 different type of accounts, what should I do for looking the privilege escalation issue?

  * Change the user IDs from one account to another (on POST / GET / any HTTP methods);
  * When the application provides POST method and changing the user ID doesn’t work, then try to change the request from GET to POST. This also applies vice versa;
  * Try accessing the protected URL directly from “low-level” account (for example, administrator has <https://target/protect-url>, then try accessing this protected URL in a “low-level” account);
  * Try to see and analyze how sessions are created (whether the created sessions are predictable or not);
  * And many more things that can be tried. I suggest to readers to see [Pentester Land](https://pentester.land/list-of-bug-bounty-writeups.html) portal. They collecting much of amazing resources.

So, did I finally find it? Yes, but In this case, the privilege escalation works by changing few parameters in the HTTP Response.

* * *

#### **2.2.2. Analyzing the HTTP Response**

_What things should we see to execute privilege escalation through Parameter changes in the HTTP Response?_ Well, the basic way to do this is looking at application responses after you log in. If you get some response with common parameter such as: “isAdm”, “isAdmin”, “isAdministrator” or anything like that (“Adm” can be “Root”), then try to change the value from one state to another.

**Please kindly note** , burpsuite (and I’m sure the other similar tools) has a feature to intercepting the server responses. This will give us the ability to change a value before sending it directly to the client.

![Intercept Server Responses Feature on Burpsuite](http://www.firstsight.me/wp-content/uploads/2020/06/image-2-1024x459.png)Figure 3 Intercept Server Responses Feature on Burpsuite

So, on this target, I found “isAdm” parameter (on 3 different endpoints in 1 request) in the HTTP Response which really caught my attention. From here, I directly try to learn the changes that occur to this parameter when I log in with two different types of accounts, which is an “administrator” and a “staff”.

The result is: I found if the value of “isAdm” parameter will be set to “**true** ” when we log in with administrator account, and will be set to “**false** ” when log in with “staff” account.

So, I immediately changed the value of “isAdm” parameter from “false” to “true” (on those 3 different endpoints) when logging in with “staff” account, with the hope that this account would have administrator rights.

Is it works? **So sad, no**.

From this execution, my “staff” account status had changed completely from “staff” to “administrator”. However, this account can’t modify anything that can normally be modified by an administrator account. It’s like we have the highest privilege account that doesn’t have any privileges. Sounds bad to report this – _what’s the impact of having administrator tag that can’t do administrative thing?_

* * *

#### **2.2.3. A Parameter that Give the Right to Make Changes**

Because those account can’t change anything, then there must be something in the application that gives access rights to make changes. From here, I back to analyzing the HTTP Response again and found “Edit” parameter.

Just like previous activity, I tried to compare the values of this “Edit” parameter on “administrator” and “staff” accounts. And finally I see the difference. In administrator account, the value of “Edit” parameter will be set to “**1** “. But in the staff account, the value will be set to “**2** “. So I assume if this parameter is “blocking” my staff account to change the settings/configuration even though it already has an “administrator” tag.

From this assumption, I immediately re-execute the process. If in the previous activity I only changed the value of the “isAdm” parameter, then in this case, I tried to modify both the “isAdm” and “Edit” parameters.

So, here is the flow of the execution that I done:

  * Log in with staff account. On the HTTP response, we found the “isAdm” parameter which has the value “**false** ” and the “Edit” parameter which has set to “**2** “.
  * Change both of values to “**true** ” for “isAdm” parameter, and to “**1** ” for “Edit” parameter.
  * Forward the request and **finally our “staff” account has administrator privileges**.
  * **To ensure this changes really works** , try to log in with another browser with that account, and try changing few settings/configurations that can only be changed by the administrator. If works, then the privilege escalation has been successfully executed.

![](http://www.firstsight.me/wp-content/uploads/2020/06/Flow-of-Execution-1024x301.png)Figure 4 Flow of Execution

After making sure that everything works, then I tried to record the activity from the beginning.

**Please kindly note** , it’s very important to keep a log of your interceptors about the things you do on your recordings. Sometimes, this log is really needed as proof if you really can reproduce the issue with the behavior you stated.

After about 17 days, finally they marked this issue as P2. And the issue was fixed about a month later.

![The Bug was Marked as P2](http://www.firstsight.me/wp-content/uploads/2020/06/image.png)Figure 5 The Bug was Marked as P2

* * *

### **I**I** I. LESSON LEARNED**

In this section, I would like to add a simple recap to make it easier for readers to understand few lessons of this simple journey:

  * Sometimes, we need more effort in hunting bugs. In many cases I see that people also try to buy premium services offered by the target (I don’t do that) to see something that can’t be seen on a normal account. And in my case, I tried to spend around 3.99 USD just to allow me to create another account (because I need another phone number).

In some condition, Alhamdulillah, it gives a good result (they found a bug just like me found it too), but in the other condition, it also didn’t give any good result.

And yes, as I said on my previous article (about “[From Recon to Optimizing RCE Results](http://www.firstsight.me/2020/02/from-recon-to-optimizing-rce-results-simple-story-with-one-of-the-biggest-ict-company-in-the-world/)“), _there is no guarantee we will have a good result from our effort to buy a premium service (direct or indirectly).**But, that’s the point of testing/hunting, right?** This is not “vulnerable by design” competition, this is something we don’t know for sure if we haven’t test it._

If you ask for my advice, I prefer to try to find bugs first on the target to get a bounty. When I get a bounty from that target, then I will use a little of the bounty to buy premium service (directly or indirectly) as long as the price is makes sense to me. 3,99 USD is makes sense on that time.

But if you can get the premium service without paying (for example, the program owner gives it to you), then it will be nice.

  * When the first change doesn’t work (as in my case when I just changed the value of “isAdm” parameter), then try to look for other parameters that might give us the ability to make it work.
  * Always ensure if the changes that we made is really works. The simple way to do it is just try to log in with another browser with the account we modified, and try changing few settings/configurations that can only be changed by the administrator. If works, then the privilege escalation has been successfully executed.
  * Always documenting your activities with detail PoC video (screenshots can be taken from those video). It will help a lot to facilitate the triager / program owner in reproducing the issue. In other situations, it also helps to prove if the bug exists when you try to reproduce in the version that you test. One of Bugcrowd analyst gave a good advice for this:

_“… do a video poc, or take screenshots which proves that the vulnerability exists/existed. Neither the program owner nor the analyst can deny it when you put facts to the table.”_ – Timmy – [taken from one of his public tweet](https://twitter.com/sh_timmy/status/1246854247435689985). 

So, don’t forget to always keep the interceptor activity (log) as proof of successful exploitation (at least until the decision has been made – read: rewarded). And make sure if your interceptor’s time is same as the time that you showed in your PoC video. InshaAllah, when you meet a problem, the Bugcrowd team “will help you to put facts to the table”.

  * If readers are wondering how is my PoC video is, well, my PoC video is like a summary of this report. I put step by step on the notes that (hopefully) can make it easier to reproducing the issue.

![Screenshot of my PoC Video](http://www.firstsight.me/wp-content/uploads/2020/06/image-5-1024x601.png)Figure 6 Screenshot of my PoC Video

Yes, very tiring to make it like that. But believe me, InshaAllah this can save our time to explain the detail of our bug later.

* * *

Well, finally my simple article ends here. See you next time, InshaAllah.

* * *

### **IV. CREDITS**

Every bug hunters and/or researcher who publishes their hard work (in tweets or article or anything) so we get lots of references to do tests on the target.
