---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-31_bug-hunting-journey-of-2021.md
original_filename: 2021-12-31_bug-hunting-journey-of-2021.md
title: Bug Hunting Journey of 2021
category: documents
detected_topics:
- access-control
- xss
- jwt
- api-security
- cloud-security
- sso
tags:
- imported
- documents
- access-control
- xss
- jwt
- api-security
- cloud-security
- sso
language: en
raw_sha256: 2986dd506bf98f1bf8c5fe7271224df0e97439c2f65ca46adb20a83bb1b4c395
text_sha256: 3e6237f69a7baf8c422b5c53987a943cc263061805913c2fcb846e125bdfc3e8
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Hunting Journey of 2021

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-31_bug-hunting-journey-of-2021.md
- Source Type: markdown
- Detected Topics: access-control, xss, jwt, api-security, cloud-security, sso
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `2986dd506bf98f1bf8c5fe7271224df0e97439c2f65ca46adb20a83bb1b4c395`
- Text SHA256: `3e6237f69a7baf8c422b5c53987a943cc263061805913c2fcb846e125bdfc3e8`


## Content

---
title: "Bug Hunting Journey of 2021"
url: "https://infosecwriteups.com/bug-hunting-journey-of-2021-1fa60b28d949"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
bugs: ["Stored XSS", "Open redirect", "Token leak", "CSRF", "Logic flaw", "Information disclosure", "IDOR", "Account takeover"]
bounty: "3,200"
publication_date: "2021-12-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3044
scraped_via: "browseros"
---

# Bug Hunting Journey of 2021

Bug Hunting Journey of 2021
Sudhanshu Rajbhar
Follow
26 min read
·
Dec 31, 2021

897

4

Heyy Everyoneeee,

I hope everyone had a good hacking year, I didn’t shared any writeups this year so I thought I should do one writeup where I will be discussing most of the bugs which I found this year mainly on the Hackerone platform. All bugs were find manually with the help of Burp, Browser and Brain

This will be similar blog like I already did before:

Bug Hunting Journey of 2019
Heyyy Everyoneee,

sudhanshur705.medium.com

This year I stopped using any scripts to find bugs and totally relied upon my manual hacking skills to find bugs. Instead of going after the subdomains I focused on directly going after the main application.

So you can say that instead of going wider I was going deeper into the target this year.

I had to make many changes in my approach as before I was just using scripts and doing hacking from the terminal, now I have to browse the target understand how it works, then try to break it.

I won’t lie I was using Burpsuite cracked version at that time, yup you heard it right the LarryLau one. The first thing I did was to dump the cracked version and just use the Community version.

I realized it now that I really didn’t needed it but I don’t know why I was using it since I started doing bug hunting maybe because whatever video poc/ tutorial I picked up from youtube, etc were also using the cracked version so it stuck in my mind that to be good at bug hunting you need BurpSuite pro.

I decided to dump the cracked version because:

You might already knew about him:

Harsh Jaiswal - Bug bounty participant - HackerOne | LinkedIn
View Harsh Jaiswal's profile on LinkedIn, the world's largest professional community. Harsh has 4 jobs listed on their…

in.linkedin.com

Harsh is super good at finding server side bugs, if you have looked at his video pocs you might noticed that he uses the Burp Community version, this changed my mentality that you don’t need this Pro tools to find bugs you just need to build up the right skills & experience to do it.

There was a tweet from s0md3v (I can’t find :( now), where he told someone that you shouldn’t use the cracked version. Portswigger does so much for the community, Labs (Web Security Academy), research papers, etc all for free so you shouldn’t betray them in this way. Use the Community version it has all the stuffs you need.

Along the way I got free access to these awesome sites for building up my skills:

Won this one from a CTF challenge which @zseano created :)

Become a bug bounty hunter - Learn about web application vulnerabilities and how to find them on…
New or experienced, learn about various vulnerability types on custom made web application challenges based on real bug…

www.bugbountyhunter.com

Thanks to Snyff and Codingo for their generous giveaway.

PentesterLab: Learn Web Penetration Testing: The Right Way
For example, we have a dozen challenges on JSON Web Token (JWT) as JWT introduce really interesting vulnerabilities in…

pentesterlab.com

On to the bugs now

It was pretty hard at the beginning as I was dealing with many Informative reports as I was new to this. My reports didn’t demonstrated any impact so all of them were getting closed. But I kept submitting them

During that time I saw some disclosed reports from :

Logitech - Bug Bounty Program | HackerOne
The Logitech Bug Bounty Program enlists the help of the hacker community at HackerOne to make Logitech more secure…

hackerone.com

Automattic - Bug Bounty Program | HackerOne
The Automattic Bug Bounty Program enlists the help of the hacker community at HackerOne to make Automattic more secure…

hackerone.com

So I thought I should give it a try to see if the disclosed bugs are actually fixed or if I can bypass the protection in place.

I spend quite a time in streamlabs.com, it’s in scope for bounty under Logitech bbp:

Streamlabs | #1 free set of tools for live streamers and gamers
The most popular streaming platform for Twitch, YouTube and Facebook. Cloud-based and used by 70% of Twitch. Grow with…

streamlabs.com

At first I was quite hesitant to hunt on them as Streamlab is very popular, but I still I tried

Found a stored xss, which was really easy to find :) , it was kind of self xss as this page can only be viewed from my dashboard. Later I found that we can invite other users to our dashboard so I added that in my report

Press enter or click to view image in full size
Logitech disclosed on HackerOne: Stored XSS in...
Heyy there, I have found a stored xss vulnerability in the following goals setting pages. '''…

hackerone.com

And then I found a csrf vuln which affected most of the endpoints,

Although there was a csrf header in the request it wasn’t validated at all by the server so while testing the application I just removed this header and voila it still worked. But there was one problem, the Content-Type header was properly validated so it must be set to application/json so I couldn’t create a csrf poc as it will trigger a CORS preflight request.

So I went through all the endpoints and found one which accepted text/plain

Logitech disclosed on HackerOne: CSRF in changing users...
Hey there, I have found that the `api/v6/viewer-portal/viewer-settings/donation_settings` endpoint is vulnerable to…

hackerone.com

To create a CSRF poc for JSON request, we need to add an extra padding. In the below screenshot you can see that I have added an extra key,value pair (highlighted part) which will make sure the request body is valid json data

Press enter or click to view image in full size

Read this writeup from Geekboy if you want to know more about this JSON CSRF POC:

Geekboy | Security Researcher
For the Case 1, there is possibility in some cases where server reject the request due to extra padding of data, but…

www.geekboy.ninja

During this time I found one last bug in Logitech , Streamlab offers many features which are available to Prime members only.

All the highlighted endpoints requires Prime subscription.

Press enter or click to view image in full size

While going through different request/response’s , I found this endpoint quite interesting:

https://streamlabs.com/api/v5/user/prime/subscription
Reponse:
{
  "is_active": false,
  "is_pending": false,
  "is_past_due": false,
  "is_canceled": false,
  "is_pro": false,
  "type": "",
  "free_trial_claimed": false,
  "hibernate_claimed": false,
  "free_trial_eligible": false,
  "hibernate_eligible": false,
  "cooldown_eligible": false,
  "cooldown_seconds_past": null
}

Everything is set to false, so I decided to use the Burp’s Match and Replace rule to replace every occurrence of false in the Response body to true

Press enter or click to view image in full size
Burp Match & Replace
Type: Response Body 
Match: false 
Replace: true

I was just curious to see if the application was actually relying upon client side validation only to check whether the user has Prime subscription or not.

To my surprise, it actually worked.

The most interesting part of the Prime subscription is that you get free stuffs like tshirt, mouse,etc

Press enter or click to view image in full size
Before applying the Match & Replace rule

Now look at this screenshot after applying the Match & Replace rule:

Press enter or click to view image in full size

To actually confirm it worked or not, I clicked on the Reedeem button and it asked for an email address:

This is the exact email I received in my inbox:

Press enter or click to view image in full size
Press enter or click to view image in full size

A coupon code to purchase the Logitech Mouse for free

I told them this impact:

By creating 1000 accounts I can claim 1000 gifts , the gift is a logitech gaming mice which cost on average is around $30. So 1000 Logitech gaming mouse costs would be 30*1000 = $30,000 . I can get all of this for free

It could lead to financial loss to the company but they still lowered the severity :(

Logitech disclosed on HackerOne: Manipulating response leads to...
Heyy team, I have a found cool bug which allows me to get access to streamlabs prime features for free. Here is the api…

hackerone.com

I participated in h1-ctf which was going on during the last week of the year, so I was able to get many free invites private programs. I decided to focus on the private programs more as I would have better chance of finding an valid bug there.

As most of the bugs I found were in Private programs , most of the things will be in redacted form.

BUG: XSS leads to Account Takeover

I started with a program which started just few months back , it was completely new there weren’t many submissions and the response time was really appealing so I decided to give it a shot.

After poking around here and there in the site for a while I had now idea about the application working what all features it provides. The application was basically something similar to TryHackme platform.

I looked at the cookie policies:

Press enter or click to view image in full size

You can see the scope of the cookie is set to .example.com

which means that all the subdomains will also have the same cookie as example.com so if I am able to find xss on a subdomain it will allow me to easily steal the victim’s cookies. The interesting part about this application was that all the vulnerable challenges were hosted on the subdomain of example.com

eg. Suppose there was a xss challenge, so it will be hosted on a subdomain xss-challenge.example.com

So I used the xss-challenge.example.com subdomain (which already had a xss vuln ) to demonstrate that it’s possible to steal other user’s session cookies via the xss. I told them to change the scope of the cookies to a single domain only or else use some sandbox domains for hosting the challenges.

This issue was triaged and rewarded as a HIGH severity vuln :)

Moving on to the next program,………..

This program was 2–3 years old and had a large amount of submission rate, the hacker on 1st place had a reputation of 1500+

Looking at the statistics of the program you can confidentially say that the chances of getting a duplicate for a bug are very high as they are taking on average 1 year to fix an issue, I still decided to give this program a try.

BUG: Multiple CSRF

Found a csrf bug which allowed me to change the victim’s login email address this could easily lead to account takeover vulnerability I quickly reported it and as expected it was duplicate.

Then I found many more csrf bugs like changing applicant’s name and many other low severity csrf vulns. I decided not to report them as they might have been already reported (as I already go a duplicate for a high severity csrf vuln ) and didn’t wanted to waste my time on them.

After few days when I didn’t find any other bugs on the same target, I thought fuck it man I will report those low severity csrf bugs and see what happens.

Reported them during the evening and the next morning when I checked my mails there was some activity in those reports, I was like yeah all of them got closed as duplicate I already know but when I opened the mail I found that all of them were triaged and rewarded which I didn’t expected at all.

I had already reported 4–5 of those csrf bugs, so I decided to find more similar ones .It was very easy to identify those vulnerable requests as there was no csrf token in them

In total I was able to find around 10 csrf bugs non-duplicate all got rewarded. I was quite motivated then to hunt on the program more.

BUG: IDOR

I then checked other domains mentioned in the scope , in one application I could see there was parameter company_id in most of the GET Based request only. So I tested them for IDOR vuln, soon enough found one which was disclosing some information related to the victim’s company, I reported this IDOR and it was closed as Duplicate :(

Earlier I specifically mentioned that only GET Based request were having that comapny_id parameter, there was no such parameter in case of POST based requests (like changing profile settings, company settings)

Press enter or click to view image in full size

Although the GET Based IDOR report got duplicate, this one didn’t. It was triaged and rewarded as High Severity.

If you are looking for a collection of IDOR bypasses checkout this site:

IDOR
Checklist - Local Windows Privilege Escalation

book.hacktricks.xyz

BUG: Stored XSS via SVG File upload along with 2 bypasses

Now I am going to tell you about an experience on a program where I felt I was cheated, yup this happens a lot not all programs are good so make sure you choose the right one :)

I found a stored xss bug in this program via file attachments upload , it was basically a Slack type application.

The uploaded files were stored in a s3 bucket eg: xmessenger-attachments.s3.amazonaws.com ,

The same uploaded files could also be accessed from a subdomain of the target attachments.example.com

I uploaded a svg file with the following contents:

The url of the uploaded file was something like this:

Press enter or click to view image in full size

I have a xss on a subdomain of the target, if you’re not short tempered I told something about this in the beginning of the article :)

I checked the cookie scope policy and found the same thing here also .example.com , this time in the cookies there was a jwt token which was used in all the api endpoints and other subdomains for authentication purpose.

Along with that I checked the change password request and found that it didn’t required the current password.

This time I had found something which could easily allow me change victim’s password and takeover their account.

I mentioned this specifically in my report:

We can create a javascript code which will first steal the victim's jwt token , then sends a request to the change password endpoint using the stolen jwt token, which will eventually allows us to takeover the victim's account. If you need a actual POC for this let me know, I am not providing it along the report as it will take time

The program had a great response time so I received a response in a couple of hours after submitting the report and this happened:

Press enter or click to view image in full size

It went back & forth like 2–3 times then I didn’t said anything as they told me every time the same answer that they are already aware of the cookie policy and are doing a large effort to secure them. It was rewarded as a Medium severity which kinda sucks as the impact was much higher than that.

Btw guess what I just checked even after their continuous efforts the cookie’s policy is still same.

After a week or so the issue was fixed.

I just thought of checking the fix at that time and found a bypass which was pretty easy :)

This was the request made to upload the attachment

POST /graphql HTTP/2
Host: x.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Authorization: Bearer Redacted
Content-Type: application/json
Content-Length: 59
{
  "operationName": "uploadFile",
  "variables": {
  "fileType": "image/svg+xml",
  "cId": "1490072"
  },
  "query": "mutation uploadFile($cId: ID!, $fileType: String!) {\n  uploadFile(cId: $cId, fileType: $fileType)\n}\n"
}

After the fix the application didn’t accepted the file if the Content-Type of the file was image/svg+xml , so to bypass it I tried different content-types of file such as image/svg , text/html ,etc and I found that text/xml was allowed, the xss popup again appeared .

The program had Retest enabled but they didn’t asked me to do so in the first report so I filed a new report and submitted it.

They confirmed the bypass I got rewarded with the same amount of bounty again.

Again a new fix was applied and the report was closed as Resolved this time also no Retest was asked.

Fired up my burp to check the fix and now along with image/svg+xml it also doesn’t accepts text/xml . Behind the scenes they probably had a whitelist filter which only accepted few content-type such as text/plain and other common ones.

content-type-research/XSS.md at master · BlackFan/content-type-research
Content-Type Research. Contribute to BlackFan/content-type-research development by creating an account on GitHub.

github.com

Press enter or click to view image in full size

fileType:text/html(xxx , fileType:text/html,xxx ,etc

I tried all of them to see if the application allowed any of them but none of them worked.

Then I came to a conclusion that the application validates the content-type from the extension of the uploaded file for eg: If I upload a file with name test.txt, the fileType parameter value will be text/plain in the upload request. So I uploaded the xss.svg file and changed the fileType parameter value from image/svg+xml (which is not allowed) to image/png (which is allowed) and the file was successfully uploaded

Press enter or click to view image in full size
Url of the uploaded file
HTTP/2 200 OK
Content-Type: image/svg+xml
Content-Length: 416
Date: Mon, 27 Dec 2021 05:14:36 GMT
Last-Modified: Wed, 01 Sep 2021 04:52:51 GMT
Content-Disposition: inline; filename="xss2.svg"
Accept-Ranges: bytes
Server: AmazonS3
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg" width="240px" height="240px">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
  alert(document.cookie);
  </script>
</svg>

Made a new report , they verified the bypass and rewarded me (same amount as the previous ones).

And this time they asked for a retest :)

Press enter or click to view image in full size

I confirmed their fix and found no bypass this time they did a great job this time. But wait the story doesn’t ends here.

Here comes the twist in the story.

Press enter or click to view image in full size

So I checked the bug again and it was reproducible this time which I didn’t believe at all, I told them yeah I just tried reproducing it and found it still there. Sadly I didn’t had any video poc for the Retest so I can’t prove that this wasn’t reproducible before when I checked it.

After a week they pushed out a fix and when I checked it I could see a difference in the upload request:

Press enter or click to view image in full size
POST /graphql HTTP/2
Host: x.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0
Authorization: Bearer Redacted
Content-Type: application/json
Content-Length: 59
{
  "operationName": "uploadFile",
  "variables": {
  "fileType": "image/svg+xml",
  "fileName":"xss2.svg",
  "cId": "1490072"
  },
  "query": "mutation uploadFile($cId: ID!, $fileType: String!) {\n  uploadFile(cId: $cId, fileType: $fileType)\n}\n"
}

A new parameter was added in the body, fileName . Now the application was validating both the file name and the file content-type .

Get Sudhanshu Rajbhar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In the above screenshot you can see that the Retest was rejected, so I told them that I didn’t get the $50 for the retest as it was rejected. This was their reply:

Press enter or click to view image in full size

That was the moment I decided not to hack on their program ever again, btw Hackerone still showed that I had earned $50 for the retest which is kinda funny.

Press enter or click to view image in full size

Always be careful with programs like this , in one of the talks from Frans Rosen he told that when hacking on a new program at first he sends only few low-hanging bug reports , to actually to find if the program is of worth his time or not. He doesn’t want to spend his precious time on a program where they don’t respect the hacker and don’t take security seriously .

BUG: Private note disclosure via api endpoint

The bug which I am going to talk about now was really a very easy one, didn’t have much impact but still relatively easy to find.

It was a program which has been running for 4–5 years so it didn’t hope of finding something like this so easily. The application was a file sharing platform, where users can upload and share files with other users.

There was one feature which allows any user to set a password to their file, if anyone wants to access it they need to provide the password. Along with the file the owner could also send a note , both of them could only be visible to the end user when he provides the right password.

So I took the shared link and opened it in my browser, checked all the requests made after loading that url, the very first request was made to an /api endpoint.

https://example.com/api/file/v1/info?hash=xxxxxxxxxxxxxxxxx

In the response you could see a description field which contains the note which was attached along with the file, this shouldn’t be disclosed in the response.

I was like no way this could have happened, I opened the same url again in the Incognito window and monitor the requests in burp. Found the same response.

Then I decided to report it I had a strong feeling this might have been already reported as it was so obvious you just need to load the url and watch the response , easy bug right?

Well it wasn’t reported by anyone else triaged and rewarded as a LOW severity vuln, even got fixed after few hours of reporting it.

Bug: Disable any user’s acc by just knowing there email address

Be ready now I am going to talk about a very interesting bug which was easy to find but also had so much impact

I got invited to this program quite a long time ago but didn’t find anything interesting during that time, someone disclosed their finding which was about a Full read ssrf bug found on the main scope .I was really amazed by this bug so I decided to spent more time on this program to see what I can find.

When you are hacking on a new program you can set some goals like I am going to do my best to submit at least 1 valid bug on this program, it’s ok even if you don’t find any bugs some targets are hard and have very good security posture. Move on try some different programs like programs with social media sites or B2B application or retails sites or etc , find what suits best for you.

Back to the bug ,…

I kinda love to look for Improper access control , Privilege Escalation bugs to find such bugs you need to dig deeper into the application , understand how different user roles are defined ,what actions can be performed only Admin’s acc,etc

The application which I was testing was an Merchant portal, where the owner can control their retail stores. We could also invite other users to our merchant portal.

So I invited another user by entering the email address, a invitation email was sent to the user’s email address and now the invited user can access the merchant portal and perform actions based upon his Role

The access controls were setup pretty strong I wasn’t able to find any misconfiguration in any endpoint.

Back to the admin acc, I noticed that we can perform some actions such as change the invited user username ,etc

I change the name to something else and then visited the invited user profile , the changes were successfully made. At that moment I realized that when I invited the user, an invitation mail was received which had the Invitation Confirmation Link and I correctly remembered that I didn’t clicked on it.

If you haven’t already figured out, let me tell what’s wrong here. The application doesn’t validates if the invited user has actually confirmed the Invitation request or not . The invited user is directly added to the Merchant portal.

By just knowing some ones email address I could invite them to my Merchant Portal and then can make changes to their username (First name , Last name) without any user interaction at all.

I submitted this as soon as possible , after a few hours I noticed that I completely missed something . I could a lot more than just changing the invited user username. I can enable 2fa on their acc , Disable login

The invited user would never be able to login into his account until I remove him from my Merchant Portal

Exact reply which I sent to them with further details:

Press enter or click to view image in full size

After few days I received the following updates on the report:

Press enter or click to view image in full size

Well that got escalated quickly :)

There was one more scope which I wanted to test but the provided credentials weren’t working, so in the same report I asked them if they could look into this problem. They replied in a few hours with the new pair creds and I was ready to look at another scope now.

It was a completely different application from the Merchant Portal

while looking around what all features it has I noticed a similar looking User Management endpoint which I have already seen in the Merchant Portal

I decided to check for the same bug in this endpoint also and it worked !!!!!!!!!

The only problem was that I can’t perform any other actions rather than changing the victim’s name (First name, Last name) . other options like enable 2fa, disable login weren’t working here.

As it was a very similar issue to what I already reported , I decided to ask the program-manager what should I do file a new report (as it might be possible that both the application shares the same codebase, so only one fix was required).

The program-manager told me to file a new report and then they will verify it.

And then they rewarded for this report also :)

Press enter or click to view image in full size

I really like engaging with this program as they responded very quickly , the program-manager was also very nice.

BUG: CSRF in invite user action

It was a fairly new private program launched 2–3 months ago but had a good number of submissions and seemed very active. This application was also a Merchant Portal just like before.

I spent few time understanding the application, then started playing with the requests. In state changing requests such as (POST,PUT,DELETE) , there were many custom headers used along with X-CSRF-Token header.

Press enter or click to view image in full size

Seeing so many custom headers along with the X-Nonce and X-CSRF-Token anyone wouldn’t be bother looking for CSRF bugs right?

I removed the X-CSRF-Token and forwarded the request, still successful. Then I thought they might be validating other custom headers for sure. One by one I removed the custom headers , but still the request was successful. Wow so they weren’t even validating any of those headers.

Then I needed to confirm one last thing whether the application accepts text/plain as the Content-Type of the request body or not, it worked :)

I created a poc and verified it then submitted the report, again had a doubt it might get duplicate as this was pretty easy to find.

This was a site-wide csrf issue which affected all the endpoints , the most sensitive endpoint was the one which I showed above Invite user action, so I used it as an example in my report to demonstrate the impact of this.

Next day I received a response from the team, I wasn’t expecting such type of response. I was quite amazed seeing their reaction to this report:

Press enter or click to view image in full size

I will explain what the program-manager meant by his 2nd reply, to confirm the csrf bug . I created a csrf.html file and save the csrf poc code there

The below is similar to what you have already seen in the case of Streamlab's csrf poc

Press enter or click to view image in full size

I just opened the csrf.html file in my browser so the url was something like file:///Directory/csrf.html , in Firefox if the request is made from the file URI no Origin header is sent. If you try the same in other browsers such as Chrome you will notice the Origin: null header is sent.

The server accepts the requests without the Origin header

If you have read this writeup which I shared few days ago you might already know , how to deal with the Origin header .

Story of a weird CSRF bug
Heyyy Everyoneeee,

infosecwriteups.com

I used the same trick iframe data uri to create a poc and updated the report with the working poc now.

Soon enough the program-manager validated the report

Press enter or click to view image in full size

I agreed to their reasoning and wasn’t even expecting that much amount so it was really grateful for them. .

BUG: Stealing vitcim’s access_token via open redirect

One thing which every bug hunter should do is to read disclosed reports on the Hackitivity on Hackerone

HackerOne
Edit description

hackerone.com

If you want to take it one step further go ahead and try to reproduce the bug to confirm if it’s actually fixed or not.

Here is a diagram to explain what I am trying to say:

Press enter or click to view image in full size

Here’s an example of the diagram :

A report got disclosed in the Hackitivity

Logitech disclosed on HackerOne: session takeover via open protocol...
Summary: Hi Logitech team, on streamlabs.com the endpoint…

hackerone.comFrF

From the report I got to know about an endpoint:

Press enter or click to view image in full size

The attacker has control over the protocol part of the url, they describe it as open protocol redirection not open redirect as they don’t have full control over the url. just the protocol part.

After the fix the protocol is validated and now it only accepts http & https. I am not sure if the reporter tried escalating the open protocol redirection to xss via javascript: as they had full control over the protocol part xss might be possible there.

Only streamlabs.com subdomain were whitelisted , if I try with any other url such as example.com an error will be thrown. I tried some variations also xstreamlabs.com , streamlabs.co.in ,etc to see if it works or not.

As nothing was working, I just though of searching for this endpoint in the wayback machine to see if I can find any other domain which is also in the whitelist.

GitHub - lc/gau: Fetch known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and…
getallurls (gau) fetches known URLs from AlienVault's Open Threat Exchange, the Wayback Machine, and Common Crawl for…

github.com

https://streamlabs.com/global/identity?r=https://darthvapes.tv https://streamlabs.com/global/identity?r=https://dragynslair.live/ https://streamlabs.com/global/identity?r=https://franmg.net/merch https://streamlabs.com/global/identity?r=https://itzyony2.com https://streamlabs.com/global/identity?r=https://lmgtwitch.com https://streamlabs.com/global/identity?r=https://maitresharinganv1.com https://streamlabs.com/global/identity?r=https://themavshow.tv https://streamlabs.com/global/identity?r=https://veterangamertv.com https://streamlabs.com/global/identity?r=https://www.koopatroop.com https://streamlabs.com/global/identity?r=https://www.lokenplays.com https://streamlabs.com/global/identity?r=https://yagurlbubblezl4d.com

From this I was able to find some more whitelisted domains:

dragynslair.live 
darthvapes.tv 
nixxiom.tv

If an authenticated user visits this url, his access_token will be sent to the dragynslair.live domain: https://streamlabs.com/global/identity?r=https://dragynslair.live/

Press enter or click to view image in full size

The most interesting thing about this particular domain is that it was available for registration

Press enter or click to view image in full size

To prove my claim , I added an entry for dragynslair.live in my /ect/hosts file, this will allow me to confirm it without actually buying the domain

In this screenshot you can see the access_token was sent to my server.

Press enter or click to view image in full size

The access_token could be used in the following endpoints:

/authorize
With the Streamlabs API you can access various aspects of a user's Streamlabs account and even trigger custom alerts…

dev.streamlabs.com

The team just like last time lowered the severity without any explanation, which I already knew was going to happen as per my past experience from this program

Bug: XSS filter bypass

In this program it was clearly mentioned that if you find any waf bypass for eg like for xss they will treat the report as HIGH severity and reward accordingly.

The application had many functionalities so I was able to find an interesting endpoint, where the input was passed to the window.location sink.

The filter was working something like this: If I input javascript:alert() , it will end up like this

I tried uppercase JAVASCRIPT , mix uppercase-lowercase JaVaSCript but same thing happened.

Then I looked up on Portswigger xss cheatsheet to find more ways:

Cross-Site Scripting (XSS) Cheat Sheet - 2021 Edition | Web Security Academy
This cross-site scripting (XSS) cheat sheet contains many vectors that can help you bypass WAFs and filters. You can…

portswigger.net

j&#x61vascript:alert(1)
&#X6A;avascript:alert(1)
javascript&colon;alert(1)
java&Tab;script:alert(1)
java&NewLine;script:alert(1)
javascript&colon;alert&lpar;1&rpar;
.............

Then I started looking for other blogs , and stumble upon payloads which had hex escape sequence in them and this worked on my target I was able to bypass the filter

\x61 represents a

Press enter or click to view image in full size

It was triaged and rewarded as a High Severity vuln.

BUG: STORED XSS

I will be talking about one last bug which had the highest severity and also highest reward I have gotten for a bug so far.

It was a super new program, I could say I was on the group of people who were invited before anyone else.

I already had a very bad experience from another new program I submitted many bugs there such as stored xss, csrf, access control bugs even one bxss which triggered in one of their Admin panel. One by one they started closing the reports as Informative & Duplicate stating that csrf,access control, xss bugs are site-wide so they will be only rewarding the first report which highlighted the problem.

I talked to other people also who were in the same program, all said the same thing site-wide , their reports also got closed as Duplicate because of that. A couple of months have already passed still they didn’t even paid out the reward for any valid bug also.

It was good lesson for me to not engage so much with new programs.

Back to the new private program, because of the past experience I was quite hesitant to hunt on this program but I still tried, the application was similar to Twitch where we can do streaming.

Users profile were public and there we could add any spotify embed code which would then be displayed to other user also.

Press enter or click to view image in full size

In the above screenshot you can see an example of the embed code, btw if you have never heard of Darknet Diaries before you should start listening to this awesome podcast. Trust me you’ll love it :)

Darknet Diaries - True stories from the dark side of the Internet.
A podcast featuring true stories from the dark side of the Internet.

darknetdiaries.com

Press enter or click to view image in full size

The application embedded this iframe code in the user’s profile, I started testing to see if I can take advantage of this functionality and add my own own arbitrary code to it .

I first started with a simple payload <img src=x onerror=alert()> , error returned not a valid Spotify Embed code , then I tried various other tags but it seems only frame was allowed.

So I started playing with the src attribute , if I can change it to src=javascript:alert() I will have an easy xss bug but the same error was received not a valid Spotify Embed code .

I though of using srcdoc attribute but that also didn’t worked

: The Inline Frame element - HTML: HyperText Markup Language | MDN
The HTML element represents a nested browsing context, embedding another HTML page into the current one. Each embedded…

developer.mozilla.org

After some time I thought why not just add an on event handler which will trigger when the src gets load, I added this attribute to the embed code onload=alert()

And it worked !! I could see the xss popup , this xss was in my public profile. So if any other user visits my website the xss wil be triggered.

I quickly submitted this issue and waited for their response. When dealing with such new programs , make sure you don’t waste time report the bug as soon as possible to make sure you don’t get duplicate , I already learned this lesson from some other programs.

There response time was really fast, they rewarded this xss as a HIGH severity vuln.

Press enter or click to view image in full size

I was looking around and notice the application allows user’s to login via Google/Facebook , then I also find the settings from where we could Add/Remove Google/facebook acc ,

so I was thinking using the xss bug I can easily takeover the victim's account as I have seen in some writeups.

I explained this to them and they verified my claim

Press enter or click to view image in full size

In total they rewarded me with $3200 for a Critical

This was the highest reward I have ever gotten for a reward so I was really very happy after this.

This year I started playing CTFs just for the web challenges, you are provided with the source code of the challenge as I am not good with source code reviewing doing this ctf challenges allows me to overcome my weaknesses. Also the challenge authors will often use some obsecure techinuqes which you want to be able to find anywhere else.

So if you want to improve your web hacking skills start playing some ctfs which have high rating points.

You can know about upcoming ctfs from here:

CTFtime.org / All about CTF (Capture The Flag)
Capture The Flag, CTF teams, CTF ratings, CTF archive, CTF writeups

ctftime.org

I know this was a really long read, I hope you didn’t get bored after reading this long writeup and learned one or two things from it.

That’s all, thankyou very much for reading it till the last. Hope you would have enjoyed it.

Goodluck for 2022 :)

Sya Everyoneeee
