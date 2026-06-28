---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-25_how-i-hacked-scopely-and-got-.md
original_filename: 2023-06-25_how-i-hacked-scopely-and-got-.md
title: How I Hacked Scopely and Got $$$
category: documents
detected_topics:
- clickjacking
- xss
- command-injection
- otp
- rate-limit
- cors
tags:
- imported
- documents
- clickjacking
- xss
- command-injection
- otp
- rate-limit
- cors
language: en
raw_sha256: d384ed97ce9d31ac6049d2009a85a8f31517bcefc9d164e20212d73d782769f0
text_sha256: 621fd707b73b233204f88d1a7bcd19011e3f16728b6f851479ddafe5aeed4558
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked Scopely and Got $$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-25_how-i-hacked-scopely-and-got-.md
- Source Type: markdown
- Detected Topics: clickjacking, xss, command-injection, otp, rate-limit, cors
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `d384ed97ce9d31ac6049d2009a85a8f31517bcefc9d164e20212d73d782769f0`
- Text SHA256: `621fd707b73b233204f88d1a7bcd19011e3f16728b6f851479ddafe5aeed4558`


## Content

---
title: "How I Hacked Scopely and Got $$$"
url: "https://medium.com/@mydudehello91/how-i-hacked-scopely-and-got-c60772f77d41"
authors: ["Aryan W13DOM (@NeuRosis23)"]
programs: ["Scopely"]
bugs: ["Self-XSS", "Clickjacking", "Account takeover"]
publication_date: "2023-06-25"
added_date: "2023-06-27"
source: "pentester.land/writeups.json"
original_index: 1012
scraped_via: "browseros"
---

# How I Hacked Scopely and Got $$$

How I Hacked Scopely and Got $$$
W13DOM
Follow
4 min read
·
Jun 25, 2023

144

1

Hey, Bug Hunters I Hope You Are Doing Well And Have a Good Day.

WHOAMI?

My Name is Aryan From Kurdistan And Bug Hunter in Hackerone and Integrity, Also a Student 4th Stage In English Department.

Let’s Start:
Press enter or click to view image in full size
Photo by Shahadat Rahman on Unsplash

Chaining Self Xss To Account Takeover:

As Always I Doing Bug Bounty At Night So One night During Read an Articles I saw Write up of this researcher “ https://ph-hitachi.medium.com/how-i-hacked-scopely-using-sign-in-with-google-298a9c166ad “ I Noticed A Lot of things and Something Came to my mind “ You Can Find a Bug In There” so I Decide to Choose the Scopely as A target.

Press enter or click to view image in full size
Scopely Scope

As You Can See It Has a Big Scope That interesting For Hackers to find a New bug, First Of All, I Gathered All Of the Subdomains Using My Own Tool That Contain a lot Of Resources to Collect Subdomains.

Press enter or click to view image in full size
My Tool To Collect Subdomains

As You Know Scopely Is a Public Program and Some of The Researchers Tested and Found a Bug in There So I Need 15 Minutes To Make a Plan How Can I Test it To Find a Bug, So I Decided To Test Just Some Type Of Vulnerability Like ( Analyze Js Files, Csrf, Github Recon, Xss and Open Redirects) So Before Testing The Vulnerabilities I did some interaction and Playing With Functionality and Take Notes To Provide Myself To Tomorrow and Before Leave my Room I Gathered All The Urls From My Crawler.

Press enter or click to view image in full size
Collect URLS

Next Night I Drank Some Energy and Fire Up My Mind😁 Now Time To Real Interaction With Subdomains, I Checked Some Js Files And Analyzed It But Nothing Interesting Same As GitHub Recon😪 , Due To Scopely Haven’t Interesting Functionality In subdomains That is Impossible for CSRF, I Tested Some Forms For CSRF But Have Protection Like Csrf Token and I Tried Some Bypass Way such as “ Remove Tokens, Reused Token, Remove Token and Put Some Texts, Guessable Tokens To Brute Force “ So I am Plenty Disappointed But I Never Give-up, Time To Move To Another Vulnerability But Before it I Notice Strange Things In Redacted.Scopely.com That Have Connection With Medium App and I Intercepted Requests:

Press enter or click to view image in full size
This Is The Response and Source Code

And Have A Lot Of Information About Medium Account When The Users Interact With This Subdomain So I Found “ User id, username, Facebook account if connect with it, access Token of Medium Account “ But I Don’t Know How I Deliver To the User And Control it, Then I Get Some Ideas like Make a file As Clickjacking attack when the user Click My Button then Steal Data to My Server As CORS Attack But Doesn’t Work Cause X-Frame-Options: Same origin. Thus I decided Break Some Time.

Get W13DOM’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After Some Time at 3:15 A.M, I Looked at My notes That Yesterday Wrote During Interactions, I Saw a REDACTED.SCOPELY.COM That a Login Page For Users You Can Create an Account In There but Haven’t Some Functionality That is why Just tried To Bypass Email Creation But Nothing As Always😂 Then I make a bed and slept cause I am exhausted.

Learned Something New:)

The Next Day, I Looked at My Teacher Course Zhenwar in Bug Bounty And In The Xss Section He Exploiting The Email Form With Xss Payload ( This is New For me, IDK That Previous Saw a Similar way:) So I Tried This Way In The Target :

Payload → “hello<form/><!><details/open/ontoggle=alert(‘W13D0M’)>”@gmail.com

After Clicked Continue BOOM The Xss Alerted

Press enter or click to view image in full size

😍 , But You Know It's Just A Self Xss So I Need To Deliver To Victims So I Created A File To Provide a Clickjacking Attack Fortunately ( Oh Finally My Chance Emerged🤣)This Subdomain is Vulnerable To Clickjacking After Spent Some Time I Provided This:

Press enter or click to view image in full size
Poc

Then I Reported To The Company and Triaged And Rewarded Me with $$$.

Conclusion

Before Testing The Program Make A Note And Interaction With All Subdomains That are In Scope Then During Testing Make a Plan I MEAN How You Can Perform Your Skills In There and Test Every Functionality Also Try to Learn Something New From Articles And Google Things and It Can Be Find A Bug Like It, Many Thanks To My Teacher For This Course:)❤️❤

Happy Hacking!!

My Twitter → https://twitter.com/NeuRosis23

My YouTube → https://youtube.com/@AryanGaming12
