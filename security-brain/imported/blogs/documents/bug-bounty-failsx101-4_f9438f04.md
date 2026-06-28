---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-26_bug-bounty-failsx1014.md
original_filename: 2020-08-26_bug-bounty-failsx1014.md
title: Bug Bounty Failsx101[4]
category: documents
detected_topics:
- mfa
- password-reset
- otp
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- mfa
- password-reset
- otp
- xss
- command-injection
- rate-limit
language: en
raw_sha256: f9438f0493fd12eff5e65e5d84f199f42c1162285a13ecbeb5d8c5d36bbe93ec
text_sha256: 8efdcf1ad9f8072a1d8864af9273818c4d2a34d50b80a7f04cc781b6048c1dc1
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty Failsx101[4]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-26_bug-bounty-failsx1014.md
- Source Type: markdown
- Detected Topics: mfa, password-reset, otp, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `f9438f0493fd12eff5e65e5d84f199f42c1162285a13ecbeb5d8c5d36bbe93ec`
- Text SHA256: `8efdcf1ad9f8072a1d8864af9273818c4d2a34d50b80a7f04cc781b6048c1dc1`


## Content

---
title: "Bug Bounty Failsx101[4]"
url: "https://medium.com/@leviwof/bug-bounty-failsx101-4-b601616fbe9f"
authors: ["ArcherL (@realArcherL)"]
bugs: ["2FA / MFA bypass"]
publication_date: "2020-08-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4294
scraped_via: "browseros"
---

# Bug Bounty Failsx101[4]

Bug Bounty Failsx101[4]
AL
Follow
8 min read
·
Aug 26, 2020

7

Sometimes I think I do bug bounties only to fail, so that I can write about them here, but it’s the process I enjoy which brings joy anyway. Lol

2FA Bypass

This breed of bug is widely popular among-st the new generation of bounty hunters. [not so popular among-st triagers though]

So to exploit or get an OTP bypass:

You can brute force it.
You can fake the page response and bypass it (I did it myself, awaiting disclosure and…..so you all know I was closed as N/A :( )
You can send in a blank OTP.
You can smash it, burn it and what not, but there is still another way.

The authentication token is something that validates the legitimacy of the user with the websites. As in, once you have completed the authentication process that is login, you will be identified to the website using a unique, long and random identifier string that is the authentication token. Sites protect it with certain flags such as HttpOnly, Secure, the same-site, etc.

Mostly HttpOnly and Secure cookie flags make life miserable for bug hunters. With “HttpOnly flag (optional) included in the HTTP response header, the cookie can not be accessed via the client side script (XSS)” and “a cookie with a Secure flag set is not sent over an unencrypted, HTTP request” that makes it extremely difficult to extract an auth token which generally resides in the cookies, which brings us to

The Curious Case of 2FA and its love for auth tokens.

5. This is a way where you can bypass OTP with auth token, but only if these conditions are met.

The victim’s account has 2FA enabled.

Attackers know the victim’s login and password, but they don’t have access to OTP or backup codes.

Attackers somehow can disclose HTTP only; Secure auth token from the victim.

Only in this case, the attacker can bypass 2FA leveraging:

victim’s login+password

auth cookie - if attackers have access to auth, it's likely they have/had access to the active session of the victim or there was a way to leak live auth cookie moreover, the attack is being performed in or before the token expires (which is roughly between 10–20 minutes).

Considering the above assumptions lets attack our victim on REDACTED website.

Step I: Enter the user ID, password and OTP for the attacker account. Save the successful response of the correct OTP.

Press enter or click to view image in full size
How the 2FA works on the website.

Step II: Enter the victim ID and password while intercepting the request, copy the mfavalue.

Again after entering the OTP (any arbitrary value) intercept the response and replace it with the saved response from Step I, simultaneously changing the values of mfavaluewith previously copied one and auth with the stolen one.

Press enter or click to view image in full size
- BOOM HACKED!!

BOOM!! you have bypassed the OTP check! give me bounty please! moment. I immediately reported this as bug.

No, I seriously did………

*“bye bye teer… bye bye teer”-BB Ki Vines

Closed as Informative.

PS: Now after the whole fiasco, I am kind of glad that this wasn’t closed as N/A.

Let’s rewind and understand another concept of “how bug bounties work” in context to this report, systematically with the plot twist in the end.

Reporter Vs Triager round I (Bug 1)

I. The assumptions are too heavy.

How did you manage to get the auth cookie, which is so tough to exploit (nearly impossible)? Even if you’ve managed to get it via victim’s PC, it’s out of scope to be able to gain physical access to the account.

my counter: Well, that’s not why I reported this, its an OTP bypass and not auth leakage report. The scenario leading to auth stealing is not what this report deals with.

Get AL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2. If you have auth, you have access to the victim account which already makes it compromised, it doesn’t make any sense to be able to create a new access.

my counter: Isn’t the whole point of having 2FA to prevent a new point of access by the adversary? no matter what means are applied? Also the auth expires in 15 mins, you can change the pass but not regain access with 2FA enabled.

3. Why do you have to go through the trouble to log in to a new PC? The user will eventually receive an OTP notification and, out of suspicion, will change the pass so the whole process of bypassing is absurd.

my counter: (Unique to my case)Yeah, but the fact that I could compromise the account, why wouldn’t I change the password and email as the first thing, knowing that these stuff could put my hack at risk (iss Baat ki koi sense ban rhi hai? mujhe ban rahi thi tabh). [more on this later]

II. Had this been a pen test report, it would have been considered a legitimate (great) bug but as of now it isn’t because of too many presumptions for this exploit to happen, which bug bounties don’t accept.

Both sides have compelling arguments, no matter how much I want to believe this to be a valid report, the odds (tiagers mostly) are against it.

Its not like this attack scenario hasn’t been reported before. The Grammarly report (#665722) employees the exact same methodology and was accepted as a valid bug. But I have been told that the program was running a promotion campaign and its one of the reporter got lucky case!

Should we give up though?

Reporter Vs Triager round II (Bug 2)

Now, you see another thing comes to mind, how about trying to bypass 2FA altogether? hmm.

A strange thing happened, while checking the website out (LOL!) I found out that despite having the 2FA enabled, one will be simply logged in without the need to fill the 2FA, i.e., via forgot password/reset password link.

Assumption here is you have the Email ID with which this account was registered compromised, as in all you need is the reset link, if you have it you can reset the password and you will be directly logged in, and NO 2FA value will be asked.

Bonus, if you place the victim auth cookie here, it will log you into the victim’s account. Note: Unless you know a way to steal the auth token, this is just how web applications work.

Press enter or click to view image in full size
Bypass 2FA with password reset.
Reporter Vs Triager round III (Bug 3)

I presented the triager with another bug, that “The password is reset while the attacker is halfway through the authentication process but has not yet entered the OTP, it would not sort any effect on the partial authentication session. Consequently, the user will be able to log in without the need to insert the new password”

In simple words,

Attacker is mid-way with the login i.e., about to enter the OTP, that is exactly when the password reset is done by victim.
With session still valid, the attacker is able to login into the account with 2FA PIN, without the need to re-authenticate with new password, since the session in which he entered the old password, and now in which he reached the OTP form hasn’t expired.

Assumption here is you have the means to access OTP, but this assumption is needed only in one special case when Bug 1 fails to work properly.

Press enter or click to view image in full size
Attacker waiting patiently.
Press enter or click to view image in full size
User resets the password, attacker bypasses the need to re-enter the password

Now lets combine Bug 1,2 and 3

Press enter or click to view image in full size
The explanation of the whole scenario.

So the only BIG assumption now here is that the Email Id with which the account was registered on <REDACTED> website to be compromised (i,e., all you need is the reset password link), the only required assumption.

After real hard-work and one month of dedication I was able to chain all these bugs and submit the report and finally turn the report to from informative to Critical.

Naah…. It is still being kept closed as informative. **screams in corner

The Ugly Truth: well, lets face it

The possibility of your Gmail/Bing/Yahoo (whatever you used to register account) being compromised is very low in order to get a password reset link(triager’s words not mine) unless you get someway to forge the reset password link.
Secondly, <redacted>.com has nothing to do with your Gmail/Bing/Yahoo account compromise or any other for that matter. To them its important that nothing happens to your account within their own website boundaries.

Then why do we have 2FA, isn’t that’s the whole purpose of it? my question to all triagers and bug bounty programs.

Lastly Is it a valid bug?

Well I leave that up to you!! Vulnerabilities like these have been considered as valid in the past.

EDIT: The root cause of this whole fiasco is nothing but the issues with the auth cookie expiration. But the reason I tried an account login was to maintain and show persistence, you see the auth would have expired in 10–20 mins, but once logged in, you stay in control as long as you want (even when the password is reset, you are logged out but the cookie still remains valid). Also for the bug 3, for this to be working, you should consider the time the auth cookie stays valid, should be at least 24 hours, for such a bug to be considered as valid, with another assumption that somehow the attacker got hold of the 2FA device or like in this case knew how to bypass it.

I hope you found this informative. You can find me on twitter. Happy hunting.
