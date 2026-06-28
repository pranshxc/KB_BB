---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-30_how-i-hacked-googles-bug-tracking-system-itself-for-15600-in-bounties.md
original_filename: 2017-10-30_how-i-hacked-googles-bug-tracking-system-itself-for-15600-in-bounties.md
title: How I hacked Google’s bug tracking system itself for $15,600 in bounties
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- rate-limit
- business-logic
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- rate-limit
- business-logic
language: en
raw_sha256: b5f86768366c0e26c8c8976600b762a39d75cb528552b41fda0e2733f48db397
text_sha256: 137ae46047f53811f415fae63d539aeec4cdaa7027f032c56de6ce4e5a3361ed
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked Google’s bug tracking system itself for $15,600 in bounties

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-30_how-i-hacked-googles-bug-tracking-system-itself-for-15600-in-bounties.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, rate-limit, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `b5f86768366c0e26c8c8976600b762a39d75cb528552b41fda0e2733f48db397`
- Text SHA256: `137ae46047f53811f415fae63d539aeec4cdaa7027f032c56de6ce4e5a3361ed`


## Content

---
title: "How I hacked Google’s bug tracking system itself for $15,600 in bounties"
url: "https://medium.freecodecamp.org/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5"
final_url: "https://www.freecodecamp.org/news/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5"
authors: ["Alex Birsan (@alxbrsn)"]
programs: ["Google"]
bugs: ["Logic flaw"]
bounty: "15,600"
publication_date: "2017-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6067
---

October 30, 2017  / [ #Google ](/news/tag/google/)

# How I hacked Google’s bug tracking system itself for $15,600 in bounties

![How I hacked Google’s bug tracking system itself for $15,600 in bounties](https://cdn-media-1.freecodecamp.org/images/1*417vbJu3b_sEe3dOAwkNAg.png)

By Alex Birsan

#### Easy Bugs for Hard Cash

Have you ever heard of the Google Issue Tracker? Probably not, unless you’re a Google employee or a developer who recently reported bugs in Google tools. And neither had I, until I noticed my vulnerability reports were now being handled by opening a new thread there, in addition to the usual email notifications.

So I immediately started trying to break it.

![Image](https://cdn-media-1.freecodecamp.org/images/5zdrwXUDE3LqKOdzz0Y3CCJLHVd0OvkcuBIc)

So what exactly is this website? According to the documentation, the Issue Tracker (internally called Buganizer System) is a tool used in-house at Google to track bugs and feature requests during product development. It is available outside of Google for use by external public and partner users who need to collaborate with Google teams on specific projects.

In other words, when someone has an **issue** with a Google product, it goes in the **issue** tracker. Makes sense, right? We, as external users, only get to see the tip of the iceberg: A small set of pre-approved categories, and issues where someone at Google explicitly added an external account, such as **vulnerability reports**. But how much information lies under the surface?

![Image](https://cdn-media-1.freecodecamp.org/images/CFgfsjB8Gal-3SyKq0vtArRPOVR5xhY659uv)

By observing numerical IDs assigned to the latest public threads, we can easily estimate how much usage this tool gets internally. There are about **2000–3000 issues per hour** being opened during the work hours in Mountain View, and only **0.1%** of them are public. Seems like a data leak in this system would have a pretty big impact. Let’s break it!

### Attempt #1: Getting a Google employee account

One of the first things I noticed upon discovering the issue tracker was the ability to participate in discussions by sending emails to a special address, which looks like this:

**buganizer-system+**_componentID**+** issueID_**@google.com**

(in which _componentID_ is a number representing a category, and _issueID_ is an unique identifier for the thread you are responding to)

This reminded me of a recent finding called [the Ticket Trick](https://medium.freecodecamp.org/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c), which allowed hackers to infiltrate into organizations’ chat systems by leveraging this kind of email system. Considering that this is an **@google.com** email address, I tried signing up to Google’s Slack team using it, and the confirmation page I got to looked very promising:

![Image](https://cdn-media-1.freecodecamp.org/images/b0-gtpqorm6i73pfQofHEim3r9PGNVX9IvUH)

Alas, no email from Slack ever showed up.

The next best thing I could think of was getting a Google account with an **@google.com** main email address, which would hopefully give me some extra privileges on the Buganizer. Registering such an account from outside Google was not supposed to be allowed:

![Image](https://cdn-media-1.freecodecamp.org/images/lGKxtS-uexq7P1jB9294kXADV5wM4a5s9Qgx)

However, I found a method to bypass this filter: If I signed up with any other fake email address, but failed to confirm the account by clicking on a link received by email, I was allowed to change my email address without any limitations. Using this method, I changed the email of a fresh Google account to `**buganizer-system+123123+67111111@google.com**` **.**

Soon after, I received the confirmation email as a message on the corresponding issue page:

![Image](https://cdn-media-1.freecodecamp.org/images/VWzwunVDR9leTK7k9wsKr9VUlpkKs4OfneZT)

Nice! I clicked the confirmation link, logged in on the Issue Tracker, and …

![Image](https://cdn-media-1.freecodecamp.org/images/J22G5zmwFpEkMXCuaM5wn76CFlaWUo9NL3y8)

I got redirected to the corporate login page. And no, my Google account credentials did not work there. Bummer.

Nevertheless, this account gave me a lot of extra benefits in other places across the internet, including the ability to [hitch a ride](https://google.ridecell.com/request) (for free, maybe?), so it was still a security problem that opened a lot of doors for malicious users.

Accepted: **11 hours** | Bounty: **$3,133.7** | Priority: **P1**

### Attempt #2: Getting notified about internal tickets

Another Issue Tracker feature that caught my eye while getting familiar with the UI is the ability to _star_ items. _Starring_ an issue means you’re interested in the problem being discussed and you want to receive email notifications whenever someone adds a comment.

![Image](https://cdn-media-1.freecodecamp.org/images/3bUICO2Mvfct8zR3qtOL4Yh0gzStAVnCUDIS)

The interesting thing I noticed about this functionality was the distinct lack of errors when trying to use it on issues I did not have access to. Access control rules never seemed to be applied on this endpoint, so I logged in to my second account and tried to star a vulnerability report from my main account by replacing the Issue ID in the request. I then saw this message, which means the action had been successful:

> 1 person has starred this issue.

Could it be that easy to spy on open Google vulnerabilities? I quickly posted a comment on the issue to see if I my fictional attacker account would get notified about it.

![Image](https://cdn-media-1.freecodecamp.org/images/vSJk6ii1tRc5cn0ljK4tp1yyzfg3j0BbdHlh)

But again, no email ever showed up.

For some reason that I genuinely can’t remember, I decided to do some further testing on this one. So I got a recent issue ID, and extrapolated a range of a few thousand IDs which should coincide with the latest issues in the database. I then starred them all.

In a matter of minutes, my inbox looked like this:

![Image](https://cdn-media-1.freecodecamp.org/images/w9q-a7CF3poG65EDwuRxBZPtzWUMWOwqDtAA)

My first thought when opening the inbox was “Jackpot!”.

However, upon closer inspection, there was nothing particularly interesting going on in those threads. Apparently, I could only eavesdrop on translation-related conversations, where people would debate the best ways to convey the meaning of a phrase in different languages.

I even considered not reporting this for a few hours, hoping I would find a way to escalate the severity. In the end, I realized that the Google security team would probably be interested in finding possible pivot methods and variants, so I sent out the details.

Accepted: **5 hours** | Bounty: **$5,000** | Priority: **P0**

### Attempt #3: Game over

When you visit the Issue Tracker as an external user, most of its functionality is stripped away, leaving you with extremely limited privileges. If you want to see all the cool stuff Google employees can do, you can look for API endpoints in the JavaScript files. Some of these functions are disabled completely, others are simply hidden in the interface.

When designing this limited version of the system, someone was nice enough to leave in a method for us remove ourselves from the CCs list, in case we lose interest in an issue or don’t want to receive emails about it any more. This could be achieved by sending a POST request like this:
  
  
  POST /action/issues/bulk_edit HTTP/1.1
  
  
  
  {  "issueIds":[  67111111,  67111112  ],  "actions":[  {  "fieldName":"ccs",  "value":"test@example.com",  "actionType":"REMOVE"  }  ]}
  

However, I noticed some oversights here that led to a huge problem:

  1. **Improper access control:** There was no explicit check that the current user actually had access to the issues specified in `issueIds` before attempting to perform the given action.
  2. **Silent failure** : If you provided an email address that was not currently in the CCs list, the endpoint would return a message stating the email had been removed successfully.
  3. **Full issue details in response:** If no errors occurred during the action, another part of the system assumed that the user had proper permissions. Thus, every single detail about the given issue ID would be returned in the HTTP response body.

I could now see details about every issue in the database by replacing `issueIds` in the request above. Bingo!

I only tried viewing a few consecutive IDs, then attacked myself from an unrelated account to confirm the severity of this problem.

Yes, I could see details about vulnerability reports, along with everything else hosted on the Buganizer.

Even worse, I could exfiltrate data about multiple tickets in a single request, so monitoring all the internal activity in real time probably wouldn’t have triggered any rate limiters.

I promptly sent the exploit details to Google, and their security team had the affected endpoint disabled one hour later. Impressive response time!

Accepted: **1 hour** | Bounty: **$7,500** | Priority: **P0**

When I first started hunting for this information leak, I assumed it would be the _Holy Grail_ of Google bugs, because it discloses information about every other bug (for example, HackerOne pays a [minimum of $10,000](https://hackerone.com/security) for something similar).

But after finding it, I quickly realized that the impact would be minimized, because all the dangerous vulnerabilities get neutralized within the hour anyway.

I’m very happy with the extra cash, and looking forward to finding bugs in other Google products.

* * *

If you read this far, thank the author to show them you care. Say Thanks

Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. [Get started](https://www.freecodecamp.org/learn)

ADVERTISEMENT
