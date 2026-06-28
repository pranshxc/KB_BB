---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-25_hacking-moodle-apps-via-external-functions.md
original_filename: 2024-07-25_hacking-moodle-apps-via-external-functions.md
title: Hacking Moodle Apps Via External Functions
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- csrf
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- csrf
- api-security
- mobile-security
language: en
raw_sha256: d2ac1907e94b4c52b6e8c5faa5200973b11e518ef610f003de581d56a3caedd6
text_sha256: cdb51dfaddff69e59fed950c872d4db84779a993768654baa8de9ea694fc0f4f
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Moodle Apps Via External Functions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-25_hacking-moodle-apps-via-external-functions.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, csrf, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `d2ac1907e94b4c52b6e8c5faa5200973b11e518ef610f003de581d56a3caedd6`
- Text SHA256: `cdb51dfaddff69e59fed950c872d4db84779a993768654baa8de9ea694fc0f4f`


## Content

---
title: "Hacking Moodle Apps Via External Functions"
url: "https://medium.com/@dub-flow/hacking-moodle-apps-via-external-functions-1fc88a6d697c"
authors: ["Florian Walter"]
bugs: ["Broken Access Control", "Security code review"]
publication_date: "2024-07-25"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 136
scraped_via: "browseros"
---

# Hacking Moodle Apps Via External Functions

Hacking Moodle Apps Via External Functions
Florian Walter
Follow
8 min read
·
Jul 24, 2024

83

So say you’re trying to hack an app that uses Moodle. You start by googling something like “hacking moodle” or “moodle common misconfigurations” and… you don’t really find anything besides a few CVEs on Exploit-DB and a rather short page on HackTricks.

But how can that be? Moodle is quite well-known, right? I can’t speak for everyone but I remember using Moodle for some courses during my time at uni. So how can it be that there is virtually nothing out there on how to hack Moodle?

Well, I don’t know the answer.

But recently, I did quite a long Pentest against a Moodle app, and I want to share with you what I found to be an interesting attack vector against apps running on Moodle: External Functions.

Press enter or click to view image in full size
What are “External Functions”?

While pentesting a Moodle app, you will realize that there is one endpoint that is seemingly called all the time: POST /lib/ajax/service.php. This endpoint in essence accepts 4 parameters:

The sesskey (used for CSRF protection)
The methodname (the name of the function to call)
The args (the arguments to pass to the called function)
The info parameter, which always seems to have the same value as methodname. I always omitted it because the requests worked fine without it, and I didn’t understand its purpose

These functions allow us to perform pretty much any kind of CRUD operation, such as: Querying users, deleting courses, updating curriculums, etc.

From the official Moodle documentation, about external functions (https://moodledev.io/docs/4.5/apis/subsystems/external):

“Moodle has a full-featured Web Service framework, allowing you to use and create web services for use in external systems. The Web Service framework and the External API work closely together providing a number of Endpoints, and self-describing classes to support a wide range of uses.”

There are a ton of these functions already built into Moodle, but there isn’t really any proper documentation on them and how to use them. You can find a list which may or may not be comprehensive here: https://docs.moodle.org/dev/Web_service_API_functions

Press enter or click to view image in full size
A list of some built-in Functions

An example of a built-in method is core_user_search_identity which takes in a query argument and allows searching users.

Press enter or click to view image in full size

For example, the above query finds all users that contain the string “bobby” and we see a user called “Bobby Fischer”.

On top of that, Moodle apps may have custom external functions implemented by the app developers. These are invoked the same way and are obviously very interesting as the odds are higher that custom code is vulnerable than Moodle itself.

Figuring Out How to Invoke an External Function

Now a big problem I found is that it’s really hard to figure out how to use these functions properly because the documentation is very limited. Of course, you can find many examples of external functions used by the pentested app, just by looking through your Burp Proxy history. But what about all the others?

For some functions, you may find information by googling them. However, the most reliable approach for me has been leveraging the Moodle source code.

Easy Example: core_user_search_identity

For example, the way I figured out how to use core_user_search_identity was as follows:

I found this function by scrolling through https://docs.moodle.org/dev/Web_service_API_functions and it sounded interesting as it’s about retrieving user information
Press enter or click to view image in full size
Go to the Moodle source code at https://github.com/moodle/moodle
In the repository, search for the string “core_user_search_identity”
Press enter or click to view image in full size

Since we know from https://docs.moodle.org/dev/Web_service_API_functions that this function is about searching for users, we can already infer how to use this function at this point (the query is used to identify the queried user).

Thus, for simple examples, we may not need to dive deeper through the code than that.

More Complex Example: core_table_get_dynamic_table_content

So let’s check out another function: core_table_get_dynamic_table_content. This function sparked my interest because its description at https://docs.moodle.org/dev/Web_service_API_functions says: “Get the dynamic table content raw html”. So it sounds like a way to extract data from the database (hackers love this!).

So we search for the string core_table_get_dynamic_table_content in the Moodle GitHub repo, and get the following:

Press enter or click to view image in full size

If we look at the first hit (repository.js), we get the following:

Press enter or click to view image in full size

This shows us all the arguments we need to pass to this function. But oh dear, that’s a shitload of parameters… How are we gonna figure out how to use this method appropriately?

Well, let’s check out the 2nd hit of our GitHub search (services.php):

Press enter or click to view image in full size

This shows us the actual class name, what capabilities are required (i.e., what permissions are required to call this external function), and some other information. The most interesting thing here is the classname, which allows us to further search the GitHub repo for more details on how this external function is used.

Get Florian Walter’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So we search through the whole repository again but for core_table\external\dynamic\get.

Press enter or click to view image in full size

We just looked at the first hit. The second hit is what I was looking for in the first place: The unit tests for this function. The developers of you reading this may already know this, but for the rest: Unit- and integration tests are one of the most valuable pieces of documentation there is.

So we read through the test cases in get_test.php, and we find multiple tests of how NOT to use the function, as well as test_table_get_execute, which shows us how to use the function correctly.

Press enter or click to view image in full size

The first part of the function is just creating some dummy data for the test case.

The interesting part comes here:

This shows us exactly what kind of JSON object we need to send to this external function!

If we read through this, it looks like this is a test for getting all participants in a particular course. So how can we send this request to our tested app?

Well, we can just copy the first 2 parameters as it is (because they are hardcoded and seemingly work in a vanilla Modle environment). For the 3rd one, if we look at the previously created dummy data, at the beginning of the test, we use the string user-index-participants- followed by a valid courseId (i.e., the course we want to know the participants of). This means we simply need to append the Id of a course that exists in our app.

What about the next parameter:

$this->get_sort_array([‘firstname’ => SORT_ASC])

Well, we find that the test file contains a function called get_sort_array which shows us that we can pass something like this to the external function: "sortdata": [{"sortby": "firstname", "sortorder": "ASC"}].

So by reviewing the test cases and combining it with the knowledge we already have (i.e., the purpose of the function as well as all arguments that can be passed in), we bit by bit work on creating a valid request, until we have this:

This queries the course participants for courseId => 2 (which exists in my setup).

This returns a massive JSON with "error": false and a "data" property that contains the queried course participants as a formatted HTML table. This gives us a wealth of information such as user names, their userIds, email addresses, roles, etc.

How to Pwn Apps Using External Functions?

Glad you asked! Now the main answer is Broken Access Control (BAC). I presume that many Moodle apps may have some form of BAC that involves external functions. Another exploitation scenario is leveraging custom external functions, which are more likely to be vulnerable to all sorts of attacks, such as injections.

In this section, I will show how I was able to exploit external functions and provide some explanations as well. But please take my explanations with a grain of salt because I’m no Moodle expert and these are just what I think the reasons are.

The main reason why I think that external functions are exploitable is the fact that they add another layer of complexity to Moodle apps. A ton of functionality can seemingly be performed in 2 ways now:

“Directly”, by talking to the corresponding PHP modules. For example, /course contains functionality to manage courses
Via using external functions

To make things worse, it seems that both of these ways use different authorization mechanisms. It seems that the “direct” access is managed by the role that a user is assigned to (such as student, teacher, admin, etc.).

However, for external functions, it looks like “capabilities” are used (see https://docs.moodle.org/19/en/Roles_and_capabilities). Thus, you may find disconnects where a user has a role that allows them to do certain things, but the user’s capabilities may allow them to do other things. This disconnect is what we’re gonna exploit here.

So our exploitation strategy is as follows:

Browse the app and figure out what information your user can view/add/edit/delete
For things the user isn’t allowed to do, try to figure out how to achieve the same thing via external functions
If you’re lucky, the user may have the appropriate capabilities and can perform restricted functions
Real-World Exploitations

Now let’s quickly talk about real-world exploitation scenarios for some inspiration!

View Other Users Data

In my pentest, I found that the developers created their own roles and locked them down dramatically and way beyond the default configurations of Moodle.

As an example, in a vanilla Moodle instance, users can view the profiles of other course participants. However, in my pentest, this wasn’t possible. Now the problem is that we could use an external function to get this data (see the above call of core_table_get_dynamic_table_content), which allows unintended access to other users’ email addresses and names.

The reason this exploitation is possible here is that either no capabilities are required for core_table_get_dynamic_table_content or all users by default have the required capability.

Delete/Update a Curriculum as a Student

Moreover, I realized that the app implemented custom external functions to delete and update a curriculum (which is intended to be used by admins and teachers).

However, we realized that access to these custom functions was misconfigured and also allowed students to delete and update a curriculum.

Final Words

This article introduces a so-far-not-documented way of exploiting hardened Moodle apps and I hope this is useful for other pentesters and bug bounty hunters assessing Moodle-based apps.

If you have any questions on the matter or want to share your own experiences, please feel free to reach out to me on LinkedIn: https://www.linkedin.com/in/florian-ethical-hacker/.

Also, if you like my content, feel free to follow me for more 😃.
