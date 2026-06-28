---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-30_account-taken-over-in-style-.md
original_filename: 2020-04-30_account-taken-over-in-style-.md
title: Account taken over in style !!!
category: documents
detected_topics:
- business-logic
- sso
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- business-logic
- sso
- command-injection
- csrf
- api-security
language: en
raw_sha256: 10203a24c37aaf20b8a7284afd487dc3f4ef945202c66d94ac0028f9825b85a5
text_sha256: 56aa41e1ccb255dea0cdd3937a8a9c809a123bd90af160f359f9a0e7724b6130
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Account taken over in style !!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-30_account-taken-over-in-style-.md
- Source Type: markdown
- Detected Topics: business-logic, sso, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `10203a24c37aaf20b8a7284afd487dc3f4ef945202c66d94ac0028f9825b85a5`
- Text SHA256: `56aa41e1ccb255dea0cdd3937a8a9c809a123bd90af160f359f9a0e7724b6130`


## Content

---
title: "Account taken over in style !!!"
url: "https://medium.com/@kishorehariram/account-taken-over-in-style-8a547342a5ad"
authors: ["kishore hariram (@kishorehariram)"]
bugs: ["Logic flaw", "CSRF", "Account takeover"]
publication_date: "2020-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4622
scraped_via: "browseros"
---

# Account taken over in style !!!

Account taken over in style !!!
kishore hariram
Follow
3 min read
·
Apr 30, 2020

201

Hey guys.. Hope everyone is safe against COVID-19. Its been long since I posted any article, I will post some which I found in recent days.

I am much interested in hunting business logic bugs. After couple of weeks of hunting haven’t found any. Got fed up and tired !! Desperately wanted to have a break. Started scrolling news feeds in FB. Found a quote “It seems impossible until you get it done” motivated me to try ahead. I decided to go with the Indian site, I am not going mention the site’s name. Sorry !! Let’s take it as Redacted.com. Made some initial recon. As usual I started looking for business logic bug.

Get kishore hariram’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Accidentally I found CSRF. I was bit excited and made myself calm. I thought of escalating it. I decided to do CSRF on password change. But unfortunately, application was asking for old password.

Press enter or click to view image in full size

After couple of hours, I created one more account and logged inside. Opened the account setting page. Application threw a popup asking me to set new password.

Press enter or click to view image in full size

On seeing the popup I logged inside the previous account which I created earlier to check whether the same popup is thrown or not. Surprisingly it was not.

Logic behind here is “For the first time when user creates an account and logins inside, application requests user to set new password. Once password is set application asks for the old password to change existing password”

Question raised straight away, “What if I use the set new password feature to change the password for the existing users through CSRF”. Fired up my burpsuite and intercepted set new password request. Investigated the request and concluded that there is no CSRF prevention. Quickly generated CSRF POC.

Press enter or click to view image in full size

Yes you are right. I logged into another account and opened the CSRF link.

Press enter or click to view image in full size

Booom..!!! PASSWORD CHANGED SUCCESSFULLY.

Still wanted to confirm. Logged in with the older creds. Threw an error message USERNAME PASSWORD INVALID. Tried the new password. Logged in successfully. Now able to take over anyone’s account.

Lesson Learnt: Never submit a report once you find a vulnerability. Chain it and try escalating the vulnerability which creates an impact to business.

Thank you for spending your time on reading this post :)
