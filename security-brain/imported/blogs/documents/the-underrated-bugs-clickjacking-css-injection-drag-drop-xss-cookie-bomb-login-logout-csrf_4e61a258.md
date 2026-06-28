---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-10_the-underrated-bugs-clickjacking-css-injection-drag-drop-xss-cookie-bomb-loginlo.md
original_filename: 2022-05-10_the-underrated-bugs-clickjacking-css-injection-drag-drop-xss-cookie-bomb-loginlo.md
title: The Underrated Bugs, Clickjacking, CSS Injection, Drag-Drop XSS, Cookie Bomb,
  Login+Logout CSRF…
category: documents
detected_topics:
- oauth
- password-reset
- csrf
- access-control
- xss
- command-injection
tags:
- imported
- documents
- oauth
- password-reset
- csrf
- access-control
- xss
- command-injection
language: en
raw_sha256: 4e61a258bb007330f2d759a3d01601d956ec62852558f03a086f7a3885506a68
text_sha256: 39144dc66b514c87b97de972253ebd5513f1d21d2c40aa1a00436c155f973ea9
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# The Underrated Bugs, Clickjacking, CSS Injection, Drag-Drop XSS, Cookie Bomb, Login+Logout CSRF…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-10_the-underrated-bugs-clickjacking-css-injection-drag-drop-xss-cookie-bomb-loginlo.md
- Source Type: markdown
- Detected Topics: oauth, password-reset, csrf, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `4e61a258bb007330f2d759a3d01601d956ec62852558f03a086f7a3885506a68`
- Text SHA256: `39144dc66b514c87b97de972253ebd5513f1d21d2c40aa1a00436c155f973ea9`


## Content

---
title: "The Underrated Bugs, Clickjacking, CSS Injection, Drag-Drop XSS, Cookie Bomb, Login+Logout CSRF…"
url: "https://medium.com/@renwa/the-underrated-bugs-clickjacking-css-injection-drag-drop-xss-cookie-bomb-login-logout-csrf-84307a98fffa"
authors: ["Renwa (@RenwaX23)"]
bugs: ["CSS injection", "Clickjacking", "Account takeover", "XSS", "Cookie bomb", "Self-XSS", "CSRF"]
bounty: "3,850"
publication_date: "2022-05-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2649
scraped_via: "browseros"
---

# The Underrated Bugs, Clickjacking, CSS Injection, Drag-Drop XSS, Cookie Bomb, Login+Logout CSRF…

The Underrated Bugs, Clickjacking, CSS Injection, Drag-Drop XSS, Cookie Bomb, Login+Logout CSRF…
Renwa
Follow
8 min read
·
May 10, 2022

555

2

Press enter or click to view image in full size
credit: WebSec Academy

During my bug bounty journey, I found a lot of bugs but I don’t have much time to write about them, In this blog, I share 3 of my reports which describe the less known tricks and bug chains for bigger impact.

1.CSS Injection + Clickjacking to Account Takeover

This app has custom communities with different subdomains, any user can create a community and a different subdomain will be assigned to him with all the app functionalities. Let’s call our site test.app1.com

In the app, admins can edit their community theme colors, background image, and fonts which will be applied to all pages including the user settings page

The style is applied to the page using an external CSS file with <link href=...>

Press enter or click to view image in full size

While playing with the inputs I found out quotes ' are not escaped meaning we can get out of the font value and have CSS injection on our community. With this payload Rubik’;}*{color:red;}; everything on all pages will be changed to red color, In first I thought of CSS injection to leak CSRF tokens but the tokens will be changed every page refresh and the recursive leak wouldn’t work since our injection is not at the start of the CSS file, Let’s look at other things

Like I said every community includes a settings page to allow users to change their settings which affects all other communities, one of the settings is the ability to change email. The process is simple one input to change your email, a hidden input contains the CSRF token, and a Change Email button.

The email change request is sending a POST request to /changeEmail which is the same as the GET request form, playing with the inputs I noticed if you send an attacker-controlled email without sending the CSRF token in the request the email will be inside the input but we get an error. This is used for cases when the user is on the email change request for too long and sends a CSRF token that might be expired or for any reason, the browser doesn’t send the token then the email stays inside the input another click will change it.

Now let’s make a form to send our controlled email

Press enter or click to view image in full size

This will automatically submit the form with our controlled email address, our email will be inside the app change email settings the user needs to click on the Change Email button for the changes to happen, This is not reliable and no one will fall for it we need to find a better way to make the victim clicks on that button. Let’s go back to our CSS we can use that to change the style and trick the victim as we want. First, we will hide everything from the page but only the change button then using :before CSS selector we change the text of the submit button, and our final payload would be:

Press enter or click to view image in full size

Let’s compare the normal change email settings page with our changed page

Press enter or click to view image in full size

Now the victim clicks on the text his email will be changed to our controlled email then using the password reset we take over his account, bounty: $1,150

2.Drag and Drop XSS, jQuery .html() and Cookie Bomb to Account Takeover

We have an app to edit photos online, create accounts and add funds to it, Like any modern application it has a feature to drop images to it instead of selecting it from the file explorer window

Let’s take a look at how the application handles dropped file

Press enter or click to view image in full size

When you drop an image I think sometimes it will be in HTML format <a href=url...> or <img src=data:image/png;base64,AAA> I’m not sure about this and I didn’t look into it but let’s just jump to the last lines.

Get Renwa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

$(‘<textarea />’).html(url[1]).text(); This is a jQuery selector with a dangerous .html() function, the value assigned to it is getting it from the dropped image href value. This doesn’t look safe at all because of 2 reasons.

First In browsers you can override dragged images to any arbitrary value, we just need the victim to drag an image on our site, change its value to our controlled string with dataTransfer.setData then redirect to the vulnerable site, In browsers if a user drags an element then redirect to another origin the element will still be attached to his mouse and can be dropped.

<textarea> is not like any other HTML element because if you set its innerHTML to any value it’s just like setting a value to it like an input element, but developers might not know that jQuery .html() is not the same as innerHTML. jQuery will change the structure of the string before setting it to the textarea. Playing with it I grabbed an XSS payload from the XSS cheat sheet and worked like charm.

Press enter or click to view image in full size

Now we have an XSS but there isn’t much impact we can do so I went to look for how we can leverage this to higher severity, The application is app2.com and the login flow is using OAuth from app2-parent.com it’s a simple process, app2.com will redirect to app2-parent.com/oauth/authorize?client_id=aa...&redirect_uri=https://app2.com/auth&response_type=code the parent domain will check if the user is logged in and then will redirect back to app2.com with the token inside the URL. The application didn’t have any state parameter which will allow an attacker to login into the victim's account from any browser if he has the OAuth token code.

Let’s just make a request to the login page and then steal the token from the URL, but there is a problem if the token comes back to app2.com the server will use the token and then invalidate it meaning even if we steal it we can’t use it for login since it will be expired.

But there is always a way and it’s Cookie Bomb all servers have HTTP request header limit they will throw bad request Header too large , Apache header limit is 8KB in the browser we can have many cookies with a large a value each then when the browser sends the request it will throw the error and the request doesn’t get sent to the server, now the attacker can steal the token and login to victim account without any authorization, here is the POC code I used

The drag-drop technique was the same as my Opera RCE bug and here is what the final POC looked like: (bounty: $1,700)

Press enter or click to view image in full size
3.Self XSS, Login Logout CSRF + OAuth to Account Takeover

A blog website called app3.com allows users to share their thoughts online and other people will interact with it, The app is old and it uses an old version of TinyMCE which is vulnerable to XSS.

Grabbed the POC payload and share it on the website but it didn’t work, later I clicked the Edit button, and the XSS alert box popped up, cool and not cool at the same time. The problem is only the author of the blog can edit the post and see the XSS meaning we have Stored Self-XSS.

Press enter or click to view image in full size

Looked around the site for any way how I can leverage this bug it was useless no way other users can be XSSed, later looked at the login flow it was protected by anti-CSRF which we can’t log in our account into victim’s browser.

I noticed the app also has login with Facebook using OAuth without anti-CSRF token but it has a state parameter, tested the flow and removed the state part of it luckily it worked, which means we can log in victim to our account using our social media account, one problem was using the FB token worked only once for every POC try we need to get another token. I found a creative way to make the POC stable to work every time.

From my browser, I grabbed my FB cookies then using my server I sent a curl request to https://www.facebook.com/v11.0/dialog/oauth?client_id=112233&scope=email&response_type=code&redirect_uri=https://app3.com/api/auth/callback/facebook In the response, we get a 301 redirect to app3.com/api/auth/callback/facebook?code=AQBB8bH…..#_=_ Now using this way we can log in the victim to our account every time.

Now we have XSS inside the victim browser but we can’t do anything since the user is logged out from the account, we need to find a way to re-login the victim to his account, and here OAuth comes in handy again. Using the XSS we open a new window pointing to app3.com/account/login?callbackUrl=https://app3.com/account/email_settings then click on the Login with Facebook button, if the user is logged in to his FB account then it will redirect automatically to the app and logged in again without any notice.

Now we have an XSS window which we control and another window in which the victim account is logged in, since both are in the same-origin we can access that window, Using the XSS we will change the FB email of the victim account and then later use forgot password feature we can reset the account password and access his account.

If you’re wondering why I didn’t use the cookie bomb to steal the victim's FB account token, The app was Flask and the cookie limit is much larger than the browsers limit therefore we can’t get an error from the server and steal it, also the token is valid for one time upon server receive it will be useless for us.

Here is the code I used for the POC: (bounty: TBD ~1k$)

Thanks for reading

Renwa
