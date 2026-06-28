---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-07_listing-all-registered-email-addresses-on-googles-crisis-map-thanks-to-idor-and-.md
original_filename: 2020-04-07_listing-all-registered-email-addresses-on-googles-crisis-map-thanks-to-idor-and-.md
title: Listing all registered email addresses on Google’s Crisis Map thanks to IDOR
  and incremental IDs
category: documents
detected_topics:
- sso
- idor
- xss
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- sso
- idor
- xss
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: 300f243d7ff5787612fd4e63db068296a5ebf270e8ae77e2aff9d816bb4ca880
text_sha256: c12bef250cdf9250d54313042a3a262f97833c02c74a9e3c28e40c1317e4ce89
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Listing all registered email addresses on Google’s Crisis Map thanks to IDOR and incremental IDs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-07_listing-all-registered-email-addresses-on-googles-crisis-map-thanks-to-idor-and-.md
- Source Type: markdown
- Detected Topics: sso, idor, xss, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `300f243d7ff5787612fd4e63db068296a5ebf270e8ae77e2aff9d816bb4ca880`
- Text SHA256: `c12bef250cdf9250d54313042a3a262f97833c02c74a9e3c28e40c1317e4ce89`


## Content

---
title: "Listing all registered email addresses on Google’s Crisis Map thanks to IDOR and incremental IDs"
page_title: "Listing all registered email addresses on Google’s Crisis Map thanks to IDOR and incremental IDs - Web Security Blog"
url: "https://websecblog.com/vulns/listing-email-addresses-on-google-crisis-map/"
final_url: "https://websecblog.com/vulns/listing-email-addresses-on-google-crisis-map/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2020-04-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4660
---

# Listing all registered email addresses on Google’s Crisis Map thanks to IDOR and incremental IDs

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[April 7, 2020February 16, 2022](https://websecblog.com/vulns/listing-email-addresses-on-google-crisis-map/)

The [last write-up](https://websecblog.com/vulns/clickjacking-xss-on-google-org/) was about a security vulnerability on [Google.org’s Crisis Map](https://websecblog.com/vulns/clickjacking-xss-on-google-org/), and so is this one. 

In short, Google Crisis Map was quite an old project used for creating and sharing custom maps.  
To do that, you need to log in with a Google account first.

![Google Accounts login screen](https://websecblog.com/wp-content/uploads/image-38.png)

Once you’re logged in, you can create new maps, manage existing maps, or manage your domain settings. Last time we created a new map; this time we will go to the domain settings.

![Google Crisis Map Landing Page](https://websecblog.com/wp-content/uploads/image-40.png)

There are multiple different domain settings.

![Domain settings form](https://websecblog.com/wp-content/uploads/image-41.png)

We will be interested in the _Members_ part of the settings. It lists all the email addresses that have some access to your maps. You can invite other people to collaborate with creating and managing the maps.

![List of members and permissions](https://websecblog.com/wp-content/uploads/image-42.png)

Let’s add another email address as a member of the project.

![Form with a new member email address](https://websecblog.com/wp-content/uploads/image-45.png)

Once we click _Save changes_ a POST request is sent to the following URL:  
`https://google.org/crisismap/example.com/.admin`  
with this body:

![Table containing fields for adding a new member](https://websecblog.com/wp-content/uploads/image-50.png)

In the request body, there are two important fields – `new_user` with the email address we want to add, and `new_user.permission`, which sets the permission level of the new user.

After the request is completed, we can see that the page has been updated with the new information.

![List of members with their email addresses](https://websecblog.com/wp-content/uploads/image-51.png)

We’ll take a look at how it looks like in the HTML:

![HTML code of the list of members](https://websecblog.com/wp-content/uploads/image-53.png)

We can see two important things in this part of the code. The email address and a number (`123456`) appearing twice in the `name` fields of the inputs. The number looks particularly interesting because it’s only a few digits long and appears to be associated with the new user’s email address.

Let’s try sending this form one more time and take a look at the request body.

![Table containing fields with information about current members](https://websecblog.com/wp-content/uploads/image-54.png)

It’s quite similar to the last request, except now instead of `new_user` there is a new item `123456.permission` with the permission value.

This suggests that the member’s permissions are referenced not with an email address, but with an ID.

However, when we open the _Members_ page, we can see the members are listed there with their email addresses.

![List of members with their email addresses](https://websecblog.com/wp-content/uploads/image-51.png)

So what would happen if we instead of `123456.permission` send some different ID, for example `123457.permission`?

Turns out we added a user with the ID `123457` as a member to our project. If we open the _Members_ page once again, we can see this user is added to the members list, **including their email address**.

![List of members with their email addresses, containing a different new member](https://websecblog.com/wp-content/uploads/image-55.png)

This means just by changing the ID in the request when saving the project’s members, we are able to get this user’s email address just by knowing their ID.

So how do we get users’ IDs then? It’s easy — the first registered user has the ID `0`, the second user has ID `1`, and so on.

Since the IDs are incremental, we can easily get the email address of **every registered user on Google Crisis Map** just by adding each ID as a member of the project using this form. This is known as [IDOR](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html).

The latest ID was around `32000`, therefore we would be able to get 32 thousand email addresses of all registered users.

* * *

Timeline|  
---|---  
2018-12-12| Vulnerability reported  
2018-12-13| Priority changed to P2  
2018-12-13| Looking into it  
2018-12-13| Priority changed to P1  
2018-12-18| Reward issued  
  
Written by [Thomas Orlita](https://thomasorlita.com/)
