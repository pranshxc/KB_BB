---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-14_3k-bug-bounty-twitters-oauth-mistakes.md
original_filename: 2018-12-14_3k-bug-bounty-twitters-oauth-mistakes.md
title: $3k Bug Bounty - Twitter's OAuth Mistakes
category: documents
detected_topics:
- api-security
- oauth
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- api-security
- oauth
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: cfa8918eb0aee32dba74c7863687a00dae7d1d497e1ae5508860660e652aab28
text_sha256: da6c84fcd7c24a8f225022f73414f34b666852c9c34bf00ecaca2bcab76901ec
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# $3k Bug Bounty - Twitter's OAuth Mistakes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-14_3k-bug-bounty-twitters-oauth-mistakes.md
- Source Type: markdown
- Detected Topics: api-security, oauth, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `cfa8918eb0aee32dba74c7863687a00dae7d1d497e1ae5508860660e652aab28`
- Text SHA256: `da6c84fcd7c24a8f225022f73414f34b666852c9c34bf00ecaca2bcab76901ec`


## Content

---
title: "$3k Bug Bounty - Twitter's OAuth Mistakes"
page_title: "$3k Bug Bounty – Twitter’s OAuth Mistakes – Terence Eden’s Blog"
url: "https://shkspr.mobi/blog/2018/12/twitter-bug-bounty/"
final_url: "https://shkspr.mobi/blog/2018/12/twitter-bug-bounty/"
authors: ["Terence Eden (@edent)"]
programs: ["Twitter"]
bugs: ["OAuth"]
bounty: "2,940"
publication_date: "2018-12-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5524
---

![2018-12-14](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Calendar%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20d%3D%22M512%20455c0%2032-25%2057-57%2057H57c-32%200-57-25-57-57V128c0-31%2025-57%2057-57h398c32%200%2057%2026%2057%2057z%22%20fill%3D%22%23e0e7ec%22%2F%3E%3Cpath%20d%3D%22M484%200h-47c2%204%204%209%204%2014a28%2028%200%201%201-53-14H124c3%204%204%209%204%2014A28%2028%200%201%201%2075%200H28C13%200%200%2013%200%2028v157h512V28c0-15-13-28-28-28z%22%20fill%3D%22%23dd2f45%22%2F%3E%3Cg%20fill%3D%22%23f3aab9%22%3E%3Ccircle%20cx%3D%22470%22%20cy%3D%22142%22%20r%3D%2214%22%2F%3E%3Ccircle%20cx%3D%22470%22%20cy%3D%22100%22%20r%3D%2214%22%2F%3E%3Ccircle%20cx%3D%22427%22%20cy%3D%22142%22%20r%3D%2214%22%2F%3E%3Ccircle%20cx%3D%22427%22%20cy%3D%22100%22%20r%3D%2214%22%2F%3E%3Ccircle%20cx%3D%22384%22%20cy%3D%22142%22%20r%3D%2214%22%2F%3E%3Ccircle%20cx%3D%22384%22%20cy%3D%22100%22%20r%3D%2214%22%2F%3E%3C%2Fg%3E%3Ctext%20id%3D%22year%22%20y%3D%22164%22%20fill%3D%22%23fff%22%20font-family%3D%22monospace%22%20font-size%3D%22140px%22%20x%3D%2216%22%3E2018%3C%2Ftext%3E%3Ctext%20id%3D%22day%22%20x%3D%22256%22%20y%3D%22400%22%20fill%3D%22%23000%22%20font-family%3D%22monospace%22%20style%3D%22text-anchor%3A%20middle%22%20font-size%3D%22256px%22%3E14%3C%2Ftext%3E%3Ctext%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill%3D%22%23000%22%20font-family%3D%22monospace%22%20id%3D%22ord%22%20x%3D%22390%22%20y%3D%22280%22%20font-size%3D%2296px%22%3Eth%3C%2Ftext%3E%3Ctext%20id%3D%22month%22%20x%3D%22256%22%20y%3D%22480%22%20fill%3D%22%23000%22%20font-family%3D%22monospace%22%20style%3D%22text-anchor%3A%20middle%22%20font-size%3D%2290px%22%3EDecember%3C%2Ftext%3E%3C%2Fsvg%3E)

#  [$3k Bug Bounty - Twitter's OAuth Mistakes](https://shkspr.mobi/blog/2018/12/twitter-bug-bounty/)

[Bug Bounty](https://shkspr.mobi/blog/tag/bug-bounty/) [hacking](https://shkspr.mobi/blog/tag/hacking/) [oauth](https://shkspr.mobi/blog/tag/oauth/) [security](https://shkspr.mobi/blog/tag/security/) [twitter](https://shkspr.mobi/blog/tag/twitter/) · [4 comments](https://shkspr.mobi/blog/2018/12/twitter-bug-bounty/#comments) · 450 words · Viewed ~16,159 times

* * *

Imagine the scenario. You're trying out some cool new Twitter app. It asks you to sign in via OAuth as per usual. You look through the permissions - _phew_ \- it doesn't want to access your Direct Messages.

![A Twitter login screen. Highlighted is the information that it cannot access your DMs.](https://shkspr.mobi/blog/wp-content/uploads/2018/11/Google-TV-Twitter-DMs-fs8.png)

You authorise it - whereupon it promptly leaks to the world all your sexts, inappropriate jokes, and dank memes. Tragic!

##  What's going on?

Many years ago [the official Twitter API keys were leaked](https://web.archive.org/web/20151112153930/https://gist.github.com/shobotch/5160017). This means that app authors who can't get their app approved by Twitter are still able to access the Twitter API.

For some reason, Twitter's OAuth screen says that these apps do _not_ have access to Direct Messages. But they do!

In short, users could be tricked into allowing access to their DMs.

##  Restrictions

There are some restrictions which Twitter has put in place in the name of good security. The most important of these is restricting callback addresses. After successful login, the apps will _only_ return to a _predefined_ URL. That means you can't take the official Twitter keys and send the user to your app. This is a sensible security decision.

Except... Not every app has a URL. Or supports callbacks. Or is an actual app. Twitter has a secondary authorisation mechanism for such cases. You log in, it provides a PIN, you type the PIN into your app.

![Twitter login screen displaying a security PIN.](https://shkspr.mobi/blog/wp-content/uploads/2018/11/iphone-pin-fs8.png)

It appears that these official PIN apps don't display the correct OAuth information to the user.

##  Fixing it

Will Twitter audit old apps and make sure the permissions are correctly displayed? I hope so!

Ideally, Twitter should have a much more granular permissions model. Allow apps to read DMs, but not send them. Write tweets, but not delete them. Read Tweets, but not follow people.

##  Timeline

  * 2018-11-06 Submitted via [HackerOne](https://hackerone.com/bugs?report_id=434763)
  * 2018-11-06 Provided clarification and PoC. Issue accepted.
  * 2018-11-15 Proposed publication date of 30th November rejected due to US holidays.
  * 2018-11-16 Bug Bounty of $2,940 offered. Filled in the W2 form to say I'm not a US taxpayer.
  * 2018-11-17 [Drank a fair amount of cider](https://untappd.com/user/edent/checkin/676732835). 
  * 2018-11-21 £2,287.05 deposited in my UK bank account. There was also the option of receiving it via PayPal.
  * 2018-12-06 Twitter fixed the issue and [published the bounty payout](https://twitter.com/edent/status/1070810894144339974). They let me know I was clear to publish. 
  * 2018-12-07 I provided clarification that the issue was still present on some API keys.
  * 2018-12-14 Published this report.

* * *

## Share this post on…

  * [ ![Mastodon](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Mastodon%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%20fill%3D%22%23fff%22%3E%3Crect%20width%3D%22512%22%20height%3D%22512%22%20fill%3D%22url%28%23a%29%22%2F%3E%3ClinearGradient%20id%3D%22a%22%20y2%3D%221%22%3E%3Cstop%20offset%3D%220%22%20stop-color%3D%22%236364ff%22%2F%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%23563acc%22%2F%3E%3C%2FlinearGradient%3E%3Cpath%20d%3D%22M317%20381q-124%2028-123-39%2069%2015%20149%202%2067-13%2072-80%203-101-3-116-19-49-72-58-98-10-162%200-56%2010-75%2058-12%2031-3%20147%203%2032%209%2053%2013%2046%2070%2069%2083%2023%20138-9%22%2F%3E%3Cpath%20d%3D%22M360%20293h-36v-93q-1-26-29-23-20%203-20%2034v47h-36v-47q0-31-20-34-30-3-30%2028v88h-36v-91q1-51%2044-60%2033-5%2051%2021l9%2015%209-15q16-26%2051-21%2043%209%2043%2060%22%20fill%3D%22url%28%23a%29%22%2F%3E%3C%2Fsvg%3E) ](https://share.joinmastodon.org/#text=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F)
  * [ ![Facebook](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Facebook%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20fill%3D%22%231877f2%22%20d%3D%22M0%200h512v512H0z%22%2F%3E%3Cpath%20fill%3D%22%23fff%22%20d%3D%22m356%20330%2011-74h-71v-48c0-20%2010-40%2042-40h32v-63s-29-5-57-5c-59%200-97%2035-97%20100v56h-65v74h65v182h80V330h60z%22%2F%3E%3C%2Fsvg%3E) ](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F&t=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes)
  * [ ![LinkedIn](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22LinkedIn%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%20fill%3D%22%23fff%22%3E%3Cpath%20d%3D%22m0%200H512V512H0%22%20fill%3D%22%230077b5%22%2F%3E%3Ccircle%20cx%3D%22142%22%20cy%3D%22138%22%20r%3D%2237%22%2F%3E%3Cpath%20stroke%3D%22%23fff%22%20stroke-width%3D%2266%22%20d%3D%22M244%20194v198M142%20194v198%22%2F%3E%3Cpath%20d%3D%22M276%20282c0-20%2013-40%2036-40%2024%200%2033%2018%2033%2045v105h66V279c0-61-32-89-76-89-34%200-51%2019-59%2032%22%2F%3E%3C%2Fsvg%3E) ](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F)
  * [ ![BlueSky](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Bluesky%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20d%3D%22m0%200H512V512H0%22%20fill%3D%22%231185fe%22%2F%3E%3Cpath%20d%3D%22M159%20126c39%2029%2082%2089%2097%20121%2015-32%2058-92%2097-121%2028-22%2074-38%2074%2014%200%2011-6%2088-9%20101-13%2043-57%2054-97%2048%2069%2011%2087%2050%2049%2089-72%2075-104-18-112-42l-2-5-2%205c-8%2024-40%20117-112%2042-38-39-20-78%2049-89-40%206-84-5-97-48-3-13-9-90-9-101%200-52%2046-36%2074-14z%22%20fill%3D%22%23fff%22%2F%3E%3C%2Fsvg%3E) ](https://bsky.app/intent/compose?text=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes%20https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F)
  * [ ![Threads](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Threads%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20d%3D%22m0%200H512V512H0%22%2F%3E%3Cpath%20stroke%3D%22%23fff%22%20stroke-width%3D%2234.5%22%20d%3D%22m200.7%20200c12.3-18%2033.3-32%2066.3-29s63%2022%2061.2%2086-29.2%2086-67.3%2087.4-61-21.5-61.6-45.8%2015.2-53.7%2079.2-52.6%20110.7%2030.5%20113.7%2084-46%20108.5-133.2%20108-156-50-156.5-179S173%2079%20256%2079s134%2041%20153.2%20111.3%22%2F%3E%3C%2Fsvg%3E) ](https://www.threads.com/intent/post?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F&text=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes)
  * [ ![Reddit](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Reddit%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20d%3D%22m0%200H512V512H0%22%20fill%3D%22%23f40%22%2F%3E%3Cg%20fill%3D%22%23fff%22%3E%3Cellipse%20cx%3D%22256%22%20cy%3D%22307%22%20rx%3D%22166%22%20ry%3D%22117%22%2F%3E%3Ccircle%20cx%3D%22106%22%20cy%3D%22256%22%20r%3D%2242%22%2F%3E%3Ccircle%20cx%3D%22407%22%20cy%3D%22256%22%20r%3D%2242%22%2F%3E%3Ccircle%20cx%3D%22375%22%20cy%3D%22114%22%20r%3D%2232%22%2F%3E%3C%2Fg%3E%3Cg%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%20fill%3D%22none%22%3E%3Cpath%20d%3D%22m256%20196%2023-101%2073%2015%22%20stroke%3D%22%23fff%22%20stroke-width%3D%2216%22%2F%3E%3Cpath%20d%3D%22m191%20359c33%2025%2097%2026%20130%200%22%20stroke%3D%22%23f40%22%20stroke-width%3D%2213%22%2F%3E%3C%2Fg%3E%3Cg%20fill%3D%22%23f40%22%3E%3Ccircle%20cx%3D%22191%22%20cy%3D%22287%22%20r%3D%2231%22%2F%3E%3Ccircle%20cx%3D%22321%22%20cy%3D%22287%22%20r%3D%2231%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E) ](https://www.reddit.com/submit?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F&title=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes)
  * [ ![HackerNews](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Hacker%20News%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20d%3D%22m0%200H512V512H0%22%20fill%3D%22%23f60%22%2F%3E%3Cpath%20fill%3D%22%23fff%22%20d%3D%22m124%2091h51l81%20162%2081-164h51L276%20293v136h-40V293%22%2F%3E%3C%2Fsvg%3E) ](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F&t=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes)
  * [ ![Lobsters](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Lobste.rs%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20d%3D%22m0%200H512V512H0%22%20fill%3D%22%23ac130c%22%2F%3E%3Cpath%20d%3D%22M421.1%20312.9H398.9c0%2012-5.8%2035.2-10.6%2045-8.8%2017.7-26.8%2032.2-48.4%2036.6-20.8%203.8-41.6%203.2-64.9%203.4-32.4-5.8-42.1-23.7-41.2-57.6V157c-.1-18.6-2.4-45.3%2021-51.5%206.3-1.5%2019.6-2.4%2029.8-2.7v-21H114v21c8.9.6%2019.5%201.6%2024.9%203.1%2022%204.8%2022.4%2026.7%2023.9%2047.9V353.6c0%2010.4-1.1%2018.9-2.3%2025.5-2.4%2012-10.9%2019.5-23.9%2022.8-6.3%201.5-14.4%202.4-24.2%202.7v23.5H421Z%22%20fill%3D%22%23fff%22%2F%3E%3C%2Fsvg%3E) ](https://lobste.rs/stories/new?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F&title=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes)
  * [ ![WhatsApp](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22WhatsApp%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Cpath%20d%3D%22m0%200H512V512H0%22%20fill%3D%22%2325d366%22%2F%3E%3Cpath%20fill%3D%22%23fff%22%20d%3D%22m79%20434%2025.7-93.9a181.1%20181.2%200%201170.3%2068.7M122.5%20391l57-15a150.6%20150.6%200%2010-41.8-40.6m93-127c2%205%200%2010-11%2022.2-6%206-4%208%206.6%2023s28%2029%2044%2036.5%2015%207%2021.7-1c15-17%2011-21%2026-14.2l27%2013c8%204%208.4%204%208.5%209s-1.7%2018-7%2023.6-25%2024.8-60%2012-59-23-99-77-1.6-86%203.6-88%207-1.5%2017-1.3q4%200%207%205%22%2F%3E%3C%2Fsvg%3E) ](https://api.whatsapp.com/send/?text=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F)
  * [ ![Telegram](data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20aria-label%3D%22Telegram%22%20role%3D%22img%22%20viewBox%3D%220%200%20512%20512%22%3E%3Crect%20width%3D%22512%22%20height%3D%22512%22%20fill%3D%22%2337aee2%22%2F%3E%3Cpath%20fill%3D%22%23c8daea%22%20d%3D%22M199%20404c-11%200-10-4-13-14l-32-105%20245-144%22%2F%3E%3Cpath%20fill%3D%22%23a9c9dd%22%20d%3D%22M199%20404c7%200%2011-4%2016-8l45-43-56-34%22%2F%3E%3Cpath%20fill%3D%22%23f6fbfe%22%20d%3D%22M204%20319l135%2099c14%209%2026%204%2030-14l55-258c5-22-9-32-24-25L79%20245c-21%208-21%2021-4%2026l83%2026%20190-121c9-5%2017-3%2011%204%22%2F%3E%3C%2Fsvg%3E) ](https://telegram.me/share/url?url=https%3A%2F%2Fshkspr.mobi%2Fblog%2F2018%2F12%2Ftwitter-bug-bounty%2F&text=%243k%20Bug%20Bounty%20-%20Twitter%27s%20OAuth%20Mistakes)
  * ![Share](data:image/svg+xml;charset=utf-8,%3Csvg%20aria-label%3D%22Share%22%20role%3D%22img%22%20version%3D%221.1%22%20viewBox%3D%220%200%20512%20512%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%3Cpath%20d%3D%22m0%200h512v512h-512%22%20fill%3D%22%235d6%22%2F%3E%3Cpath%20d%3D%22m347%20308c-22%200-40%2010-53%2026l-102-57c2-7%204-14%204-22%200-8-2-15-4-22l102-57a66%2066%200%200%200%2053%2026c36%200%2066-30%2066-66%200-37-30-66-66-66-36%200-66%2030-66%2066%200%208%202%2015%204%2022l-102%2057a66%2066%200%200%200-53-26c-36%200-66%2030-66%2066%200%2036%2030%2066%2066%2066%2022%200%2041-10%2053-26l102%2057c-2%207-4%2015-4%2022%200%2036%2030%2066%2066%2066%2036%200%2066-30%2066-66%200-36-30-66-66-66m0-218c25%200%2046%2020%2046%2046%200%2025-20%2046-46%2046-25%200-46-20-46-46%200-25%2021-46%2046-46m-218%20211c-25%200-46-20-46-46%200-25%2020-46%2046-46%2025%200%2046%2020%2046%2046%200%2025-21%2046-46%2046m218%20120c-25%200-46-20-46-46s20-46%2046-46c25%200%2046%2020%2046%2046s-20%2046-46%2046%22%20stroke-width%3D%22.8%22%2F%3E%3C%2Fsvg%3E%20)
