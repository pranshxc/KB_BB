---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-12_stealing-user-information-via-xss-via-parameter-pollution.md
original_filename: 2021-01-12_stealing-user-information-via-xss-via-parameter-pollution.md
title: Stealing User Information Via XSS Via Parameter Pollution
category: documents
detected_topics:
- xss
- command-injection
- graphql
tags:
- imported
- documents
- xss
- command-injection
- graphql
language: en
raw_sha256: 80f4f402be022e448fbe4cd4d127b02bee8fb60cd6efe949560960b09a335933
text_sha256: da917b43d0d65219394316b8a1422c3f2a3d5ec1d1d8fecca37e2016d9599029
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing User Information Via XSS Via Parameter Pollution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-12_stealing-user-information-via-xss-via-parameter-pollution.md
- Source Type: markdown
- Detected Topics: xss, command-injection, graphql
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `80f4f402be022e448fbe4cd4d127b02bee8fb60cd6efe949560960b09a335933`
- Text SHA256: `da917b43d0d65219394316b8a1422c3f2a3d5ec1d1d8fecca37e2016d9599029`


## Content

---
title: "Stealing User Information Via XSS Via Parameter Pollution"
page_title: "How I Earned $1250 x2 With A Simple XSS | Level Up Coding"
url: "https://levelup.gitconnected.com/stealing-user-information-via-xss-via-parameter-pollution-7d99b3379e7d"
authors: ["Hamza Avvan (@hamzaavvan)"]
bugs: ["Open redirect", "XSS"]
bounty: "1,250"
publication_date: "2021-01-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4004
scraped_via: "browseros"
---

# Stealing User Information Via XSS Via Parameter Pollution

Member-only story

Steal User Information - Chaining XSS & Http Parameter Pollution
Hamza Avvan
Follow
4 min read
·
Jan 12, 2021

429

3

In my recent article find out how I was able to discover a P1 in A Unique Tale Of P1: Exposed GraphQL Leads to Mass User Account Takeovers using source code review skills.

So, I was wandering and suddenly this tweet popped up in my news feed.

Press enter or click to view image in full size
@zseano motivational tweet 😁 brought tears in my eyes

Then, I decided to give myself a new start as it’s 2021 🎉. I logged in to my bugcrowd account and picked a suitable target (on which I’ve found bugs in the past) according to my skills.

I started with source code review, reviewed their bunch of javascript files and eventually found two endpoints that seem to be vulnerable to Open Redirect + XSS as the developers allowed the application to redirect user after performing certain action rather than the server, like this:

function get_param(param) {
  var params = {};
  var url = window.location.href;
  var start = url.indexOf('?');
  start = start < 0 ? url.length : start + 1;
  var end = url.indexOf('#');
  end = end < 0 ? url.length : end;
  var parameters = url.slice(start,end).split('&');
for ( var i = 0; i < parameters.length; i++) {
  var parameter = parameters[i].split('=');
  params[parameter[0]] = parameter[1];
  }
  return params[param];
}

// redirect from application
window.location.href = get_param("continue_url");
