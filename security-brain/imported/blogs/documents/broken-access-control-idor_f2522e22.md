---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-25_broken-access-control-idor.md
original_filename: 2022-03-25_broken-access-control-idor.md
title: Broken Access Control - IDOR
category: documents
detected_topics:
- access-control
- idor
- command-injection
- sso
- file-upload
- api-security
tags:
- imported
- documents
- access-control
- idor
- command-injection
- sso
- file-upload
- api-security
language: en
raw_sha256: f2522e220e67c7edb1ce632658b96539d76ba91edb2cb6dbef0bdd13b9e7d8ee
text_sha256: f44178095b40b5faa5fbcbaf8086d93433397a47c2a337c2b7b8c7a60d05ae45
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Access Control - IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-25_broken-access-control-idor.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection, sso, file-upload, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `f2522e220e67c7edb1ce632658b96539d76ba91edb2cb6dbef0bdd13b9e7d8ee`
- Text SHA256: `f44178095b40b5faa5fbcbaf8086d93433397a47c2a337c2b7b8c7a60d05ae45`


## Content

---
title: "Broken Access Control - IDOR"
page_title: "Broken Access Control - IDOR — Machevalia"
url: "https://machevalia.blog/blog/broken-access-control-idor"
final_url: "https://machevalia.blog/blog/broken-access-control-idor"
authors: ["Nick Berrie (@machevalia)"]
bugs: ["IDOR"]
bounty: "104"
publication_date: "2022-03-25"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 2782
---

# Broken Access Control - IDOR

[Bug Bounty](/blog/category/Bug+Bounty)[Write Ups](/blog/category/Write+Ups)

Mar 25

Written By [](/blog?author=63a1076f081fe62c6e3ae37b)

## IDOR in Research Site Allows Attackers to Run Experiments on Private Data Files

### What is an IDOR?

From[ Portswigger](https://portswigger.net/web-security/access-control/idor) \- "Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly. The term IDOR was popularized by its appearance in the OWASP 2007 Top Ten. However, it is just one example of many access control implementation mistakes that can lead to [access controls](https://portswigger.net/web-security/access-control) being circumvented. IDOR vulnerabilities are most commonly associated with horizontal privilege escalation, but they can also arise in relation to vertical privilege escalation."

### How do I hunt IDORs?

IDORs are one of the most common vulnerabilities I find although the impact of those vulnerabilities can be negligible to the extent of them being considered "informational" often times. The two methods I use to find IDORs are as follows:

**Manually** \- When I am surfing a target I look for parameters where the value doesn't look like it is randomly generated, thus it directly references an object within the database. For example, 
  
  
  https://insecure-website.com/customer_account?customer_number=132355

In this URL, we see that the _customer_number_ parameter's value appears to be direct reference to our id number, "132355". If we can change this number to another user's _customer_number_ id and see their data then we have an access control violation via an insecure direct object reference. Often times I find examples of this with no security consequence and you probably do to, for instance product IDs are often referenced this way. 

**Automatically with BurpBounty Pro** \- I also use BurpBounty Pro which will find parameters that appear to be IDORs. This can be extremely help for reviewing an application after spidering it or in the case that you may have missed an important IDOR while doing your manual surfing. You can get BurpBounty pro here- https://burpbounty.net/ NOTE: I am not affiliated or sponsored in any way by BurpBounty pro, its just a good tool.

### This IDOR

For this particular IDOR, I was looking at a research laboratory where users could register, upload their own research data, and then utilize the laboratory's program to parse their data and obtain the results for free. Originally, I was shooting for a file-upload bypass to execute arbitrary code but the application rewrote any file uploaded to a .txt file which was good. With that determined, I found some valid test data online by looking up examples data files related to this laboratory's research. I uploaded those vulnerabilities and realized there was an IDOR in the page I was on. 

Example: If I uploaded new test data, I would see the file loaded from a URL like this:
  
  
  /file?id=10001

If I reloaded my page where my test data was displayed and captured it with a proxy, like BurpSuite, I could change the file id parameter and load other user's test data into my page. Unfortunately, I couldn't open the files or download them to see the data so it was pretty useless. 

Next, I moved to actually working with the data. I had my two pieces of valid test data loaded up in the system so I started a job for them. This is where I noticed the second IDOR. When I set up the job the server would use a POST request to tell the application which files to use. I could modify the POST request to use other user's test data and successfully run a job. So while I couldn't see their data files directly, I could run tests on other user's data which was considered an access control violation by the organization.

Example: I could capture the POST request and modify the file parameter values to that of other users:
  
  
  POST /jobs?file1=10002&file2=10003

### Vulnerability Remediation and Payout

My recommendation to the organization was as follows (Veracode's IDOR remediation guidance):

To fix an Insecure Direct Object Reference, you have two options. The first is to add an authorization check before displaying any information that might be useful to an attacker. For example:
  
  
  method = RequestMethod.GET,  produces = MediaType.APPLICATION_JSON_VALUE) @Timed+@PreAuthorize("hasRole('ADMIN') OR hasRole('RecordOwner')")  public ResponseEntity<Record> get(@PathVariable Long id) {  log.debug("REST request to get record" {}", id);

This approach is preferred, since as long as your authorization system is effective, an unauthorized user can't access data through this path, which makes things very difficult for attackers.

There are many different authorization mechanisms, so beware of just using this example verbatim. Make sure you understand the authentication and authorization capabilities your application is using, and follow those patterns.

Unfortunately, there are times when information needs to be available to anonymous users, but you still don't want attackers to easily enumerate the data. In this case, you can create a level of  _indirection_ by creating a map connecting unpredictable values to the real, predictable IDs. A good way to do this is to use `java.util.UUID.randomUUID()` to generate Universally Unique IDs that can be mapped to your more-predictable keys. Your code might then look something like:
  
  
  -@RequestMapping(value = "/records/{id}"),+import java.util.UUID;+...++@RequestMapping(value = "/records/{safe_id}"),  method = RequestMethod.GET,  produces = MediaType.APPLICATION_JSON_VALUE) @Timed+@PreAuthorize("hasRole('ADMIN') OR hasRole('RecordOwner')") -public ResponseEntity<Record> get(@PathVariable Long id) {+public ResponseEntity<Record> get(@PathVariable UUID safe_id) {+  id = getRealIDforUUID(safe_id);  log.debug("REST request to get record" {}", id); ...

With this in place, your URLs would look something like:
  
  
  http://example.org/#/records/946933e0-fab5-419b-8910-cc3d0367d95b

and the `getRealIDforUUID` method accepts `946933e0-fab5-419b-8910-cc3d0367d95b` as its parameter, and retrieves the real id (`921106108`) from a key-value store, database, etc.. Because there are so many UUID possibilities, and random UUIDs aren't predictable, an attacker would have a nearly impossible task to attempt to enumerate these records.

Unfortunately for me, someone had found an IDOR in a different location on this host using the same parameters so I got paid out a reduced rate as a secondary finding. However, I'm always glad to scoop up some cash for a finding. In total, I made $104 for this vulnerability which isn't bad for a few minutes of work.

If you like reading about big paying vulns, stay tuned. I have two remote code executions (RCE) in the hopper now. They should be out next weekend. 

[ ](/blog?author=63a1076f081fe62c6e3ae37b)
