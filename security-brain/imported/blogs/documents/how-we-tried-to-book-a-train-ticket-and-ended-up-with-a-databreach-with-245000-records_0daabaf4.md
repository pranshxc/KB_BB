---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-19_how-we-tried-to-book-a-train-ticket-and-ended-up-with-a-databreach-with-245000-r.md
original_filename: 2023-06-19_how-we-tried-to-book-a-train-ticket-and-ended-up-with-a-databreach-with-245000-r.md
title: How we tried to book a train ticket and ended up with a databreach with 245,000
  records
category: documents
detected_topics:
- access-control
- password-reset
- api-security
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- access-control
- password-reset
- api-security
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 0daabaf4f6c6eab771ef5b64a8b079945bdf759f2c3fe0a66bd73e113ce6138b
text_sha256: ef8965a915570bdf1a7c6e18b8a1a97de5f502ab5615a288a9fdf89c41e3a4f8
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: true
---

# How we tried to book a train ticket and ended up with a databreach with 245,000 records

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-19_how-we-tried-to-book-a-train-ticket-and-ended-up-with-a-databreach-with-245000-r.md
- Source Type: markdown
- Detected Topics: access-control, password-reset, api-security, command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: True
- Raw SHA256: `0daabaf4f6c6eab771ef5b64a8b079945bdf759f2c3fe0a66bd73e113ce6138b`
- Text SHA256: `ef8965a915570bdf1a7c6e18b8a1a97de5f502ab5615a288a9fdf89c41e3a4f8`


## Content

---
title: "How we tried to book a train ticket and ended up with a databreach with 245,000 records"
page_title: "How we tried to book a train ticket and ended up with a databreach with 245,000 records - zerforschung"
url: "https://zerforschung.org/posts/freundschaftspass-en/"
final_url: "https://zerforschung.org/posts/freundschaftspass-en/"
authors: ["zerforschung (@zerforschung)"]
programs: ["DiscoverEU"]
bugs: ["Subdomain takeover", "Password reset", "Logic flaw", "Broken Access Control"]
publication_date: "2023-06-19"
added_date: "2023-06-21"
source: "pentester.land/writeups.json"
original_index: 1037
---

# How we tried to book a train ticket and ended up with a databreach with 245,000 records

[![A model of a steam locomotive with French and German flags,a Trans-Europ-Express wagon attached. The train is losing tickets](/p/freundschaftspass/fr-de-freundschaftspass-titel-small.jpg)](/p/freundschaftspass/fr-de-freundschaftspass-titel.jpg)

[Dieser Artikel ist auch auf deutsch erschienen](/posts/freundschaftspass-de/)

To celebrate Franco-German friendship, German Transport Minister Wissing and his French counterpart Beaune came up with something special: [30,000 free Interrail tickets](https://bmdv.bund.de/SharedDocs/EN/PressRelease/2023/052-wissing-franco-german-friendship-pass-available.html) per country for travel in Germany and France for young adults between 18 and 27. Codename: “Passe France Allemagne”

However, many things went wrong when the Interrail passes were distributed. In the following, we want to take you on a journey through the stages of the not-so-well-implemented ticket and show you how you could still get a pass after registration ended.

And while we’re on the tracks, we’ll also have a look at a security breach in a similar project at the EU level. Implemented by the same agency - which left the data of about 245,000 registrations almost unprotected on the web.

Please stand clear of the doors – we’re departing! 🚄🚃🚃🚃🚃

# Station 1: The town of DDoSing

On June 12 at 10am, the registration for the “Passe France Allemagne” opened - and the servers were immediately overloaded.

The rush could have been expected, as the tickets were distributed on a “first come, first served” basis. Anyone who wanted a chance to get one of the coveted tickets had to be quick. As a result, tens of thousands of users in Germany and France tried to get their hands on the pass at 10 a.m. on the dot.

Of course, setting up a system that can handle such a rush is not trivial. But it is possible! Organizers of concerts by popular bands and artists, for example, are familiar with similar situations - and can usually cope with them.

Something like this has to be well thought out, prepared and tested. If they had done that properly, they would have realized: Damn, we can’t handle so many people - and (hopefully) would have thought of another solution.

After all, there are alternatives to the “first come, first served” principle: Instead of putting everything on a moment’s notice, you can spread the sale over several points in time. This not only spreads out the rush - it also allows people to attend who don’t have time on a Monday at 10 a.m., for example because they’re at school, in training or at university.

In such a system, you can also give interested people a few days to register and then distribute the passes at random amongst all who registered.

Because one thing is for certain: Overloaded servers are not a sign of the success of a campaign, but a sign of failure in planning.

## Station 2: Password-Reset-City

While we were still angry about this failure, we got a hint by mail: This wasn’t the only part of the platform that wasn’t properly thought out and tested.

How did this show? The lucky few who were able to secure a pass had to provide an email address and come up with a password. With that combination, they could then log into the site to check for the status of their “Passe France Allemagne”.

It’s easy to forget or mistype a password - especially when things need to happen quickly. Fortunately, the “Forgot Password?” function was invented for such situations. And as usual, you receive an e-mail from the “Passe France Allemagne” with a link to reset your password. What is unusual, however, is that this link leads to an error page:

[![Screenshot of a 404 error page: 'deutschebahn-sncf-form.vercel.app might be available. Click here to learn how to assign it to a project'](/p/freundschaftspass/vercel-404.png)](/p/freundschaftspass/vercel-404.png)

If we take a closer look at the error page, we see that it links to a Vercel project that is not registered. Vercel is a cloud provider where you can host your own web applications. These applications are then available under `<project name>.vercel.app`. However, if no project is registered with the corresponding name, as is the case here, basically anyone can hijack the address.

Such an hijacked application address could then for example be used for targeted phishing. Fortunately, it was an honest person who found the mistake, registered the application themself and told the responsible organisations and us. Thus, the link to the “Forgot Password?” function only leads to a harmless test page. This page still does not belong to the organizers of the “Passe France Allemagne”, but at least to a friendly person and not to criminals.

## Station 3: Free-tickets-for-all-avenue

This brings us to the next stop on our journey: The ordering process.

Since only 30,000 passes were supposed to be given out, the ordering system has to pay close attention to that. As soon as the 30,001st person tries to register, the system would have to show an error and no longer allow registration. But that was not the case here: Instead, once the first 30,000 people started filling out the booking form, the form was simply removed from the page. The website now displays a notice stating that all passes have been allocated.

But just because you _started_ the form, doesn’t mean you already finished it. So a backdoor was built in: Anyone who had already started an order process but not completed it received an e-mail with a special link. This link could then be used to complete the order process.

There was just only one tiny problem: You could generate these codes yourself with a simple command - even if you didn’t start the order process in time.

The video shows a new code being generated on the left side of the screen. This code is then copied into the browser on the right, where the order form for the “Passe France Allemagne” then opens. The form is filled out and at the end you see a confirmation that the registration was successful.

A few hours later, our new Interrail pass arrived by e-mail.

So the whole thing is kind of like having a treasure in your house - and hanging a sign on the front door saying “All the gold has already been distributed”. But everyone can find the key to the back door.

If you want to know exactly when everything happened, you can find a timeline at the end of the article. 

## Detour via Reporting

[![The model train with the French and German flags detours, as there is a construction site with excavators in front of it.](/p/freundschaftspass/zug-baustelle-umleitung-small.jpg)](/p/freundschaftspass/zug-baustelle-umleitung.jpg)

Of course, we wanted to quickly report the problems to the appropriate parties so they could be fixed. Unfortunately, this turned out to be more difficult than expected: a security contact was nowhere to be found.1

In the end we contacted all places that seemed like they could change something: The advertising agency that’s named in the imprint of the “Passe France Allemagne”. The IT security team of the german railway (Deutsche Bahn). The contact address from the imprint of the german page of the “Passe France Allemagne”. The contact address of the german Ministry of Transportation. And finally, the german federal computer emergency response team (CERT-Bund). We sent a description of the issue to all these and asked for confirmation of receipt and next steps.

Unfortunately, we did not receive an answer at first. Howevery one day later, the extra access was no longer available. Instead, the backdoor page also showed a notice that all passes were already taken.

Figuratively speaking, the back door was also provided with a notice: “Unfortunately, all gold bars have already been distributed.”

## Station 4: Where the wild APIs live.

But noone checked if the door were actually locked. As it turns out: By sending api request directly to the order backend, we could keep generating passes.

Only a few minutes later, the pass arrived by email:

[![Screenshot of interrail pass confirmation with code to redeem the pass in app](/p/freundschaftspass/pass-email.png)](/p/freundschaftspass/pass-email.png)

## Station 5: “Unfortunately, we came to an unscheduled stop…”

At this point we didn’t know what to do anymore.

So we put our heads together and tried to find a solution. We knew that all people in charge were just pointing at the press office of Eurail (i.e. the company behind all Interrail passes, which was probably charged with issuing these passes as well) - and Eurail claimed there was no loophole. So we sent our description to the press office again.

Thereupon - and after insistent requests through other channels - we finally got an answer. Eurail thanked us for pointing out the issue, told us that they had fixed the issue and were now looking for the falsely issued passports.

How Eurail fixed the issue

The backend for the order page was build with Supabase. The API part for this is implemented using [PostgREST](https://github.com/PostgREST/postgrest).

Conveniently, PostgREST provides [automatic API documentation](https://fixmgvbxfmvoowptgiti.supabase.co/rest/v1/?apikey=***REDACTED*** So we can easily track what they really changed.

And this change was actually relatively small:

All api endpoints of the order process now have a new parameter `secret_key`. If you don’t specify this parameter, you can’t call the functions at all.
  
  
  {
  "code": "PGRST202",
  "details": "Searched for the function public.step_eligibility with parameters accepted_conditions, accepted_privacy, birth_date, last_step_completed, residence_country, user_session_code or with a single unnamed json/jsonb parameter, but no matches were found in the schema cache.",
  "hint": "Perhaps you meant to call the function public.step_eligibility(accepted_conditions, accepted_privacy, birth_date, last_step_completed, residence_country, secret_key, user_session_code)",
  "message": "Could not find the function public.step_eligibility(accepted_conditions, accepted_privacy, birth_date, last_step_completed, residence_country, user_session_code) in the schema cache"
  }
  

If you specify an incorrect `secret_key`, you will get an error message:
  
  
  {
  "code": "P0001",
  "details": null,
  "hint": null,
  "message": "Not allowed"
  }
  

We could not try what happens if you sent a request with the correct `secret_key` \- because we (fortunately) do not know it.

So now both the front door and the back door were finally locked.

Just to emphasize that again: Publishing an API doc is not a security breach! On the contrary, it should actually be good practice to do so. Because a software does not become more secure by the fact that nobody knows exactly how it works.

Your front door doesn’t become more secure by painting it in exactly the same color as your house wall, so it’s not so easy to spot. It may look funny and confuse you at first - but the door will be more secure if you lock it.

So _lock_ it, don’t hide it! 🤝

## Station 6: “Data leak of 245,000 records today from track 2 - directly opposite.”

[![Two model trains are parked on the platform, shredded paper falling out of the open doors from the train on the opposite side.](/p/freundschaftspass/databreach-aus-zug-small.jpg)](/p/freundschaftspass/databreach-aus-zug.jpg)

But these doors to more passes weren’t the only ones we found unlocked. We also took a look at the neighboring projects and found another offer similar to the “Passe France Allemange”: [DiscoverEU](https://youth.europa.eu/discovereu_en).

This program emerged back in 2018 as a result of the [#FreeInterrail campaign](https://en.wikipedia.org/wiki/Interrail#DiscoverEU). 18-year-olds can sign up to win a free Interrail pass and travel Europe.

While the “Passe France Allemagne” was dreamed up by the German and French governments, DiscoverEU was the created by the European Commission. However, both offers have one crucial thing in common: This project was implemented by the same agencies - MCI together with [Caracal](https://www.caracal.agency/en/projects/discover-eu).

Information about DiscoverEU is available at `start-discover.eu`. But we didn’t spend much time looking around. Because through the [Certificate Transparency Logs](https://crt.sh/?q=start-discover.eu) we quickly discovered the domain `dashboard.start-discover.eu`. The domain sounds exciting - but we are only greeted with a login screen.

On a technical level, the site is built similarly to the “Passe France Allemagne” - and thus we already knew the API to create an account. On the off chance we created an account – and to our surprise we were able to successfully log in with it. With great concern for the work that now followed, we noticed:

245,971 registrations for DiscoverEU were retrievable on the dashboard. The following data was displayed:

  * Name of the person
  * E-mail address
  * Country of origin
  * State of their registration
  * Type of ticket
  * Interrail order number

[![Screenshot of the dashboard: you can see a table with the columns 'A. Code', 'G.Code', 'E-mail', 'First name', 'Last name', 'Status', 'Special type', 'Type', 'County'](/p/freundschaftspass/dashboard.png)](/p/freundschaftspass/dashboard.png)

All of this personal data was virtually open on the Internet and could be retrieved with little effort or prior knowledge.

Technical details

The steps necessary to exploit the vulnerability were:

  1. Create an account using the following `curl` command. `[EMAIL]` and `[PASSWORD]` would need to be replaced with an email address and password=***REDACTED*** --request POST \
  --url https://zaymuaqytesywmkspxqk.supabase.co/auth/v1/signup \
  --header 'Content-Type: application/json' \
  --header 'apikey=***REDACTED*** \
  --data '{
  "email": "[EMAIL]",
  "password": "[PASSWORD]"
  }'
  

  2. After a few moments, a confirmation email will arrive. Click on the link contained in it:

[![Screenshot of the Confirmation Email: 'Follow this link to confirm your user.'](/p/freundschaftspass/confirmation.png)](/p/freundschaftspass/confirmation.png)
  3. Log in with the newly created account on `https://dashboard.start-discover.eu`.

  4. You can see all registrations.

## Another stop in reporting

[![The model train's mail car, in the open door an oversized paper with the inscription ZER-Report](/p/freundschaftspass/report-per-postwaggon-small.jpg)](/p/freundschaftspass/report-per-postwaggon.jpg)

Completely shocked by this databreach, we again unpacked our digital stationery and reported very quickly: To the agency, the contact address of Start-Discover.eu, the CERT-EU and the office of the European Commission responsible for DiscoverEU. Fortunately, we already knew the right contact person in the press office of Eurail, who then quickly passed the whole thing on to the responsible people.

They reacted quickly and after less than an hour the vulnerabilty was closed - they simply deactivated the registration of new account. They also informed us that that an external security test would now be carried out and the necessary steps defined in the GDPR would be taken.

## Last Stop: Conclusion

The “Passe France Allemagne” and DiscoverEU are actually great ideas: Free train tickets for young people to get to know their neighboring countries. But instead of simply enabling as many people as possible to enjoy a nice summer vacation and make new acquaintances, this unfortunately once again resulted in a digital disaster.

The “Passe France Allemagne” is also a good example of the power imbalances created by bad digital solutions: Those who have enough technical knowledge still get a passport even if all of them are actually already taken. Everyone else goes away empty-handed or even loses their accounts.

Such half-baked solutions would already be insufficient to sell a few concert tickets. But if a federal ministry gives away train tickets, special attention has to be paid that everything is well tested.

It gets even worse when we can not only create new passports, but even retrieve more than 245,000 records from the DiscoverEU program. We say times and times again: **If a website is mature enough to process data, it must also be mature enough to keep it to itself.**  
It’s staggering that such careless work was done here - and that this is apparently just accepted.

We can only hope that we really were the first to discover this vulnerability - and that the data has not already been taken away by less benevolent actors.

## Timeline

All times are CEST.

  * 2023-06-12 10:00 – Start of sale.
  * 2023-06-12 – Unregistered Vercel application is found and reported.
  * 2023-06-13 23:00 – We find the backdoor.
  * 2023-06-14 01:15 – Report to DB-CSIRT, MCI, contact named in the imprint, BMDV, CERT-Bund
  * 2023-06-14 22:00 – Our test addresses receive interrail passes
  * 2023-06-15 00:00 – We send the report to Eurail as well
  * 2023-06-15 10:00 – We notice that the backdoor is also replaced by the “sold out”-notice
  * 2023-06-15 13:00-14:00 – We can verify that passes are still registerable via API
  * 2023-06-15 17:30 – Reply from Eurail that the loopholes have been closed
  * 2023-06-16 13:00 – We discover the databreach at Start-Discover.eu
  * 2023-06-16 15:30 – We report the databreach
  * 2023-06-16 18:50 – MCI replies to us, thanks for the report, at 16:20 the vulnerability had been closed

## 🤝

We shared our findings with Eva Wolfangel for ZEIT Online. You can find her article [here](https://www.zeit.de/digital/datenschutz/2023-06/freundschaftspass-frankreich-website-hacker) (in German).

Originally we wanted to publish our findings on Friday, 16th of june 2023. But because we discovered the databreach at DiscoverEU, reported them and waited until everything was secured, we postponed the publication.

Documenting, reporting and publishing such issues takes nerves and time - which we would also much rather spend looking out the train window. We do all this on a voluntary basis and in our spare time.

If you want to support us, you can find possibilities here: <https://zerforschung.org/unterstuetzen/>

* * *

  1. We recommend that _every_ company publishes a security contact and, if necessary, further information on reporting security vulnerabilities on _all_ websites. The easiest way to do this is via a [security.txt](https://securitytxt.org). This would help (not only) us to be able to report such issues without detours to the right places in companies. ↩︎

<https://zerforschung.org/posts/freundschaftspass-en/>

2023-06-19

* * *

  * [#lang_en](https://zerforschung.org/tags/lang_en)
  * [#databreach](https://zerforschung.org/tags/databreach)
  * [#security](https://zerforschung.org/tags/security)
  * [#trains](https://zerforschung.org/tags/trains)
