---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-20_how-i-found-an-ssrf-in-yahoo-guesthouse-recon-wins.md
original_filename: 2017-10-20_how-i-found-an-ssrf-in-yahoo-guesthouse-recon-wins.md
title: How i found an SSRF in Yahoo! Guesthouse (Recon Wins)
category: documents
detected_topics:
- sso
- saml
- ssrf
- command-injection
- mfa
- supply-chain
tags:
- imported
- documents
- sso
- saml
- ssrf
- command-injection
- mfa
- supply-chain
language: en
raw_sha256: 7ef189564c687e50fa998b3bcc85d2be0e045c326a839160e42668dda192a6de
text_sha256: a6c14056432f71d4e422bbf6f54cd5254aa898a2ccd55070d4bfaff1d3702b5e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How i found an SSRF in Yahoo! Guesthouse (Recon Wins)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-20_how-i-found-an-ssrf-in-yahoo-guesthouse-recon-wins.md
- Source Type: markdown
- Detected Topics: sso, saml, ssrf, command-injection, mfa, supply-chain
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `7ef189564c687e50fa998b3bcc85d2be0e045c326a839160e42668dda192a6de`
- Text SHA256: `a6c14056432f71d4e422bbf6f54cd5254aa898a2ccd55070d4bfaff1d3702b5e`


## Content

---
title: "How i found an SSRF in Yahoo! Guesthouse (Recon Wins)"
url: "https://medium.com/@th3g3nt3l/how-i-found-an-ssrf-in-yahoo-guesthouse-recon-wins-8722672e41d4"
authors: ["Th3G3nt3lman (@Th3G3nt3lman)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["SSRF"]
publication_date: "2017-10-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6070
scraped_via: "browseros"
---

# How i found an SSRF in Yahoo! Guesthouse (Recon Wins)

How i found an SSRF in Yahoo! Guesthouse (Recon Wins)
Th3G3nt3lman
Follow
4 min read
·
Oct 20, 2017

1.95K

18

Hi Guys,

As i said before sharing is caring, here i am describing one of my findings that was closed 2 weeks ago in yahoo Guesthouse https://gh.bouncer.login.yahoo.com/ and i am describing in details, how recon helped me finding a vulnerable endpoint where i achieved the SSRF.

As mentioned publicly Yahoo! Guesthouse is a set of administration tools used by Yahoo! on a daily basis. They allow Yahoo! administrators to control all aspects of the Yahoo! network, from mail and hosting accounts to server settings and hosting management. Certain parts of the system, such as error reporting tools, are also available to Yahoo!’s customer services team.

If you hunt a lot in yahoo you will notice that when you try to open some subdomains in browser you will be redirected to yahoo gueshose login page where you should enter a username and a password related to yahoo employees and then you will be redirected to the subdomain you are trying to reach as per the below :

Press enter or click to view image in full size
Yahoo Guesthouse login page

I remember that i did scan that before, tried alot to search for vulenrable endpoints, hidden folders/files and couldn't achieve anything out of it, and obviously i don't have credentials to login,but working on another subdomain helped me finding the vulnerable endpoint in that target.

Recon :

so during my normal recon for yahoo i found that target https://alpha.keyserver.yahoo.com/ when you open it you will get not found response as per the below :

Ok, challenge accepted :)

so doing dirsearch took time in that target and result was great, i found a SAML endpoint https://alpha.keyserver.yahoo.com/saml that redirected me to the Yahoo Guesthouse login page i mentioned, but new thing appeared :D, it says after successful login you will be redirected to to a SAML endpoint, the endpoint was new to me in yahoo Guesthouse as per the below :

See the redirected to path

So doing view source to the page i was able to see the full endpoints which is : https://gh.bouncer.login.yahoo.com/simplesaml/saml2/idp/SSOService.php?SAMLRequest=nFjXkuJI073vpyDYS6JbBgkkYnu%2BkAMECJCQkLmTKXmHSv7p%2F4Aew8zO9r%2B7Vx1deTLrZObJLODP%2F%2FVZOmlBBaMif59ib%2Bh0AnK38KI8eJ9q6vqVmv7vy8uf0M5SvFwxTR3mCrg1ANaTPktzuPqwvE%2BbKl8VNozgKrczAFe1u7ow0mGFv6Grsirqwi3S6ZPP5x42hKCqoyJ%2FdoFR8D4N67pcIUjXdW%2Fd%2FK2oAgRHURRBaaTPUg9GwR%2FTici%2FT5cegTqe573SzsJ7peZL9BUA23ulaYDhPrW0F%2BhiOrl%2Byxy%2FZ37%2BypON8o8CfEbR%2BQDB1VZVz6%2Fn00WdTphvtLkih00Gqguo2sgFmnL4YA5XCGKnZWi%2FJWCAoGpB9TbYYVG8uUW2Iog58kgUFtMJD2Ad5Xb9oPfNNwjfnKLJXVC9pUUQ5T%2BcERhlZQru7o8YOBJ5JXK5nL5SeCvDcjpZF5ULHl18n%2Fp2CsF0IkLYADGHtZ3X71McxZavKPWKkipGrnBqRc7f5jSNzlEKm1t%2Fn6GYe6B%2Fn6LTCVPXVeQ0NfhARHnwK%2BTLy2QymXxoavW4vnoW0z9Vxpd%2FVdA%2Fkef7nimUq6OdAZE%2FF2nkDhMmTYuOq4Bdg%2FdpXTXgUbXMrj%2FndT%2BJvFf%2FAV3VlZ3DCOT1FPn5qq%2FDA7xHE7gir0H%2F30aJK7LSriJ4lwfobbf%2BWtfvt62er%2BBSG0IF%2BP9hAr98CnNX7j00gKuzDWFXVN59ioBbA0%2B9F6Esqvqj9r%2Fl87U6yGfleaogjILVJQpyu24qMBG99%2Bn3%2F7Bf8%2F%2BGBZ6Y%2B8UP408Azs6LPHLtNBofoyaBOiy8CZMGRRXVYfY3CwdDMPS%2BcF5B7766GJH%2F8a3Rv6XwIPgPQ%2F%2B0yypov8LQxv42ugJ8UIHcBRNNEd%2Bnf%2FyjtfdzrJ%2FiPXp2FzH8K%2Bj3wH%2BXEMhbkBYl8F7ht7r8mtsPQfx%2FhL6T4aMAwPq%2FFPh3xf1N6KudNuCLVHcSrrazIFCOurlAuxTwhNIimhe8%2F2D87PHy%2B6S%2Bd%2B1Jsshnmv2rmj7iX8du4AUTm0WZgeqjNA9D76Ag%2FTkOjzKUJP4mRUlyvZ2o%2BdJvFrHI4OBISSYu9Kp6sr2XERyos0OdttZtxwo7fMssS3KxhgRdJhW%2FH%2FryjN2o%2BtJzSeNUxYZWuyAt8nGZ8l7rWu6L44472C8Mut8ruFnqRqni5ZgTokGAdbrbjXw66pdZKaTKFjuDdpHwRmjvoZUfPQuljRdtnDVXbGAa9DyeWd3ZCRHtO7Lf7RskOG4a%2FQDoOKKJRrCWF3YXLReO4HvD2Wi1ZUzK7At%2BdOmU6G9JEHJbhp7HPuLgxKItC4KaASBJBkftTSde81h9KeUNxurIheZ8wjycotCyXuCaNhaR4zG7JbcMh03a7cz%2BclTymJebkciKhTsS3sw%2F5JTYCTecUKOIznBrPhud%2FeKkvsgBx2DRRXQv2lhWXnZp3dhOdMclrTRPl8oFENsyCdaLiDAZdLdRHVNOoy2x3m%2BGUoypl722hsORCYk0QwuTIqlD1eLQ2Q59nni2V2On075VSr1BiGS0lxLfJVej0azlbUnuzjH6UojoGW2afdR1g2ZRrnSuJYrcSgdotVVf3NjqqBOXMFyva9%2FBI99OeKRkWYegSz%2Br0vaFuuGojRS3pKC3Ob6%2BDIfTooluBYZ32S2mNCq3zzPmvBtK0TscelVlMHrRBMCKt6OZGOVLMwPn0h8R9wApvEFughoEveck47gndL3Jig2H4wLuZKL5%2FrPWn%2BT8V73vwfDJ9jZIlObt2v5kfu8Q7v6S%2BZFr1%2BCLJIpCwnMcM48CphNZJhA5IZY7XjZ3%2B8ISw9Y9MrJwYGWmC0y050ZmxwbHK8uYKpNeVUmROkE2%2Bassi0JX8qbel1ZGD06WhpIidgLzsG2FLlU9nWyAYYXORuuFkVE%2B4hQql6ahvaFbUUgbcyD67ch4HzaorpO0ecTT16it0424VlITDxsH71trnjxhJXWd7VpPJ2PL2I2mjsFDfkydjTXautdYutxtQ%2FcoqWZ3UkX88ZeXMf1%2BFgvdiZf672cxS0oy7LiPvDZCt7tqo6BKrLBhME3gWGkv42to61brZmRpqk%2B2UNrr%2BrpwcCq46GR8iAVfYtEPWy%2FpF53MnPmuNg2ldHAiuG6usb0hW2dD50D9gWV6STczGnOyY%2Brmx9DRu8bFr%2Fc9UVo4mVr3nl3EX%2FvEsjLDB4FwZu52ueCCQGAZyScNnwPi3mAS%2B1awR3shp%2B7C5sfIa4KLEC4lpzq1qujlRaTeDGVkvMgoNO6UMXkeooWGbvKhE9ett8CKY2hoB7Rq3bxlzzEfS0lTEmv36g7nTKWILsOyZjO6zsZAaY0jrP1NJnvb5lTW4bbH8Hh2ySTjD5cjDW0wdKlMEr3m%2BYt6f8Os2ZalKOZoisuDB%2FpjKBG935OukHhDQVOyX7Gz4raReJ2mtO2JFXfHxYFpJFpeurmXEPtNhKAhOJlMiVTNyTP5BTKkNcKqekgubok6P6B2wOnqSbSAjBJb1G2HgFzozca6ZGrltzPqFhQCJRZbn%2BJqZx6whEcYsm84hXdGEGKhL%2B25sL3RKMd0AsPYJ46RYRcEwlZiknvvPKGTOYlhugNj7kzREhnTIeRAOLIspW81urN0UtXQLlDwa2MZu9DbXBNRuPdZKa0sjU1DSb%2FqwOMDWWdZxTgyJ0ggw6gZUijfMovhBbO%2BhV4Vc2x1nzEFjVlxk0jiJizMjVqKG1kSN8d%2FqeOLxDIPG9tLO21%2BbZw8xU29T5%2FmfC90pWXqYesM7M7JpEZSqG77YTsIvbVzsns8LPQ2aetErGbpx8LJaOjgHvmE5YXeipz5tTHx6%2BDi69rhyNHS%2B8zF09zJrkkQJEy5Za%2Fs7KxokPndTuIf%2Bhb2g41dm1N2jfy2DYw4Ol1CdgCXDukP%2BgD2JCnKZX4ZUJPYyki2PmOKcE3wECpByt7q8pCs9%2Fu1Chp7JlehWMaX0kPWh0a0jC7a7uHoioKeh1ony9XGinzzbOaKCOzkcIKFY6mxQmJ0GwZiy1pavrs6veb2B%2FcMpYQ%2BHQjBxWUIGeR2kVPdyRfSzoiH09kT93CBdxikF5raIgl69LZ2FKdk0wSqIXutrx8dq8HWtN1ZXVG7LSH6DiPRCmjcthyGWChzrFqM%2FSAuCgq1LU9po9qRQubgjEHV4jprNfN0js3m5G3Dr7c9lFAMD12e9kae1bjtUbmtSVdS62odM%2Fvl4iLCXacj8xkB0ad36ddX428%2Bx%2F31%2Fflh%2B%2Bnl%2Bs2L9%2BXl%2B7ee559VvvxfAAAA%2F%2F8%3D

Get Th3G3nt3lman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now for those who don't know, SAMLRequest and SAMLResponse in SAML are base64 encoded XML , So after decoding it and trying to test for XXE and SSRF in the XML request you might get a good bug, but i failed to exploit it , for more information about this technique you can refer to the amazing write up from @seanmeals https://seanmelia.files.wordpress.com/2016/01/out-of-band-xml-external-entity-injection-via-saml-redacted.pdf that worked for me in another private program.

What to do now ?

So even though i could exploit this, even though i also tried to bypass the SSO itself, i couldn't just move on, tried to dig more and more in this , so when i was checking the request in burp i found something special in the GET request for the above endpoint, there was a cookie BouncerSAMLRemoteSessionHost=bouncer12-os.gh.bf2.yahoo.com; as you can see the cookie value is a website/yahoo subdomain so there is a high chance for an SSRF here.

BINGO!!!

Yes i was right, as you can see below i added my VPS ip address with port 4566 in the BouncerSAMLRemoteSessionHost cookie and i had netcat listening in my VPS and received a request from dip2.gq1.yahoo.com (63.25.204.23) port 48633:

Press enter or click to view image in full size

Its also important to mention that if you don't have VPS, Collaborator everywhere in burp can help you testing that thanks to @albinowax as i also confirmed that host is vulnerable to external DNS interactions in the X-Forwarded-For, so i could have just put the same value that burp sends in the cookie and confirm the issue without using a VPS.

tried to read files or escalate this ssrf and couldn't, so i reported to yahoo and got triaged immediately, bounty not received yet but hope it will be good.

Key Points Here :

1- Recon Wins, see where i reached from a “not found” response on a subdomain to a bug in another subdomain.

2- Never give up, put more efforts in what you are doing and read other hunters write-ups as it will help you to find bugs in other places.

3- For those who don't share findings where they can, i will not blame you, its your choice and i respect that but if you can just do it, do it for the community, for the new hackers here, small informations like this will help them to understand HOW to look for bugs and exploit them, we are not doing Black Magic here :)
