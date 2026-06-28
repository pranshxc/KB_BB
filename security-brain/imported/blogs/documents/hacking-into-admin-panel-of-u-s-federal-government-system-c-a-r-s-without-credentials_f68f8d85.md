---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-07_hacking-into-admin-panel-of-us-federal-government-system-cars-without-credential.md
original_filename: 2021-12-07_hacking-into-admin-panel-of-us-federal-government-system-cars-without-credential.md
title: Hacking into Admin Panel of U.S Federal government system C.A.R.S — without
  credentials.
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: f68f8d85bbdd29a80eb70ea8eaa208275f7570e64487c4b52bd3dc6cb05ef94b
text_sha256: f0aff7b2d4a2b4e8d3954dddb1e7e594a852809a20b72ca0100376d9723b4f69
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking into Admin Panel of U.S Federal government system C.A.R.S — without credentials.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-07_hacking-into-admin-panel-of-us-federal-government-system-cars-without-credential.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `f68f8d85bbdd29a80eb70ea8eaa208275f7570e64487c4b52bd3dc6cb05ef94b`
- Text SHA256: `f0aff7b2d4a2b4e8d3954dddb1e7e594a852809a20b72ca0100376d9723b4f69`


## Content

---
title: "Hacking into Admin Panel of U.S Federal government system C.A.R.S — without credentials."
url: "https://medium.com/@7azimo/hacking-into-admin-panel-of-u-s-federal-government-system-c-a-r-s-without-credentials-9117b865ba58"
authors: ["Hazem Brini (@ImJungsuu)"]
programs: ["U.S. General Services Administration"]
bugs: ["Client-side enforcement of server-side security", "Privilege escalation"]
publication_date: "2021-12-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3109
scraped_via: "browseros"
---

# Hacking into Admin Panel of U.S Federal government system C.A.R.S — without credentials.

Hacking into Admin Panel of U.S Federal government system C.A.R.S — without credentials.
Hazem Brini
Follow
3 min read
·
Dec 7, 2021

76

Hello guys, I hope you’re doing great! This is my first time writing an article about security bugs and I hope you will learn something new in this journey.

Without further ado, let’s dig in.

While I was looking for a program, I came across the U.S General Services Administration program and selected a target : https://cars.fas.gsa.gov/

This is a U.S Federal government system C.A.R.S : Comprehensive accident reporting system designed for personnel to report car accidents in the US.

PS : I have attached below the report in Hackerone which contains a video explaining more the walkthrough of finding the bug.

Walkthrough

I want to mention the only tools I have used are : BurpSuite & Wappalyzer.

As I approach a new target, the first thing to do is reconnaissance.
So I started looking around and navigating through different functionalities and retrieve information about the website, what kind of technologies its using, all the possible endpoints, are there JavaScript files etc…

Hence, I started from the home page which looked like a simple page :

Press enter or click to view image in full size
Home Page

Unfortunately, I couldn’t find much but only presented with an admin panel login.

Press enter or click to view image in full size
Admin Login Panel

So I tried clicking on CARS & MARS button but got nothing, and the select field was empty, nothing to do here. So I said let’s checkout the source code of the page.

To view the source of page : CTRL+U or Right-Click button and View Code Source.
While looking for some interesting functions, I came across a function called loginchk().

function loginChk() { if (document.forms[0].scSelCen.value ==”admin”) { return true; }

Explanation: the function basically checks if the scSelCen value is “admin” and return true.

Get Hazem Brini’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This particular field scSelCen was not displayed on the form , so I fired up developer console : F12
And I modified the value of the property “scSelCen” to “admin” : document.forms[0].scSelCen.value = “admin”

Press enter or click to view image in full size
Developer Console — Adding the value “admin”

Then I clicked on C.A.R.S and got this response :

Press enter or click to view image in full size
Login Response

It says : Invalid login ID/Password, but I got some options to choose ! which was not shown before.
I chose randomly any value “6MAB” and clicked again on C.A.R.S
And voila ! Got logged in into the system.

Press enter or click to view image in full size
Successful Login.

I reported it right away and it got fixed within 1 week.

Takeaway

Always do your reconnaissance and information gathering pretty well on the target.

Reviewing JavaScript code and understanding its functionality is really crucial part of hunting on web application.

Like in our example here, we got access by only reading 1 line of JavaScript code!

— — — — — —

Report : https://hackerone.com/reports/1063298

Thanks for reading this blog, If you find it valuable then give an applaud 👏👏.
Follow me & Share this blog with your friends and other community.
Till then keep learning keep exploring!

Peace ✌!

If you have any question , feel free to dm me.

My social medial accounts -
Twitter — https://twitter.com/imjungsuu
LinkedIn — https://www.linkedin.com/in/hazem-brini/
