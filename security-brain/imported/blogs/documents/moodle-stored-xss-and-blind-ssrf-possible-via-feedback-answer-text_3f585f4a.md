---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-22_moodle-stored-xss-and-blind-ssrf-possible-via-feedback-answer-text.md
original_filename: 2021-10-22_moodle-stored-xss-and-blind-ssrf-possible-via-feedback-answer-text.md
title: Moodle - Stored XSS and blind SSRF possible via feedback answer text
category: documents
detected_topics:
- xss
- sso
- ssrf
- command-injection
tags:
- imported
- documents
- xss
- sso
- ssrf
- command-injection
language: en
raw_sha256: 3f585f4a2e07f19caef389cacd15ecee22ae86e23132ea0ec05a192fb559b6d9
text_sha256: f30c93a7a8ca386d05303b22c040d8e7014404da68d944074b9e5cbfa3fc091d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Moodle - Stored XSS and blind SSRF possible via feedback answer text

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-22_moodle-stored-xss-and-blind-ssrf-possible-via-feedback-answer-text.md
- Source Type: markdown
- Detected Topics: xss, sso, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `3f585f4a2e07f19caef389cacd15ecee22ae86e23132ea0ec05a192fb559b6d9`
- Text SHA256: `f30c93a7a8ca386d05303b22c040d8e7014404da68d944074b9e5cbfa3fc091d`


## Content

---
title: "Moodle - Stored XSS and blind SSRF possible via feedback answer text"
page_title: "r0 · Moodle - Stored XSS and blind SSRF possible via feedback answer text"
url: "https://r0.haxors.org/posts?id=20"
final_url: "https://r0.xyz/posts/moodle-stored-xss-and-blind-ssrf-possible-via-feedback-answer-text"
authors: ["rekter0 (@rekter0)", "Holme (@holme_sec)"]
programs: ["Moodle"]
bugs: ["Stored XSS", "SSRF"]
publication_date: "2021-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3225
---

Moodle is an opensource learning management system, popular in universities and workplaces largely used to manage courses, activities and learning content, with about 200 million users
  

|  
---|---  
**Versions affected** | 3.10 to 3.10.1, 3.9 to 3.9.4, 3.8 to 3.8.7, 3.5 to 3.5.16  
**CVE identifier** | CVE-2021-20280  
  
## Summary

When managing a course in Moodle, it's possible to add a 'Feedback' activity. This activity-type allows enrolled students to provide feedback to different questions created by the teacher. Some of these question types allow the students to provide text-input as feedback (eg. 'Short text answer'). The input provided has HTML striped before being inserted into the database and is supposedly sanitized in a safe way before being rendered, during this process, and for unkown reasons to me, moodle did html entities decoding leading to a stored XSS vulnerability and Blind SSRF.

## Vulnerability analysis

When a student submits their feedback text answer it is processed with `s()` function before being stored in the database

`/mod/feedback/classes/completion.php`
  
  
  $itemobj = feedback_get_item_class($item->typ);
  $newvalue['value'] = $itemobj->create_value($data->$keyname);
  
  // Update or insert the value in the 'feedback_valuetmp' table.
  if (array_key_exists($item->id, $existingvalues)) {
  $newvalue['id'] = $existingvalues[$item->id];
  $DB->update_record('feedback_valuetmp', $newvalue);
  } else {
  $DB->insert_record('feedback_valuetmp', $newvalue);
  }

feedback_get_item_class loads class processor for that feedback input type

`/mod/feedback/item/textfield/lib.php`
  
  
  public function create_value($value) {
  return s($value);
  }

`create_value()` process input with `s()` function

`/lib/weblib.php`
  
  
  /**
  * Add quotes to HTML characters.
  *
  * Returns $var with HTML characters (like "<", ">", etc.) properly quoted.
  * Related function {@link p()} simply prints the output of this function.
  *
  * @param string $var the string potentially containing HTML characters
  * @return string
  */
  function s($var) {
  
  if ($var === false) {
  return '0';
  }
  
  return preg_replace('/&amp;#(\d+|x[0-9a-f]+);/i', '&#$1;',
  htmlspecialchars($var, ENT_QUOTES | ENT_HTML401 | ENT_SUBSTITUTE));
  }

As in function description, it removes tags and process the input with htmlspecialchars

**Stored XSS**  
When rendering the answer entry, mid of the process, moodle used to do html_entity_decode

`/mod/feedback/classes/response_table.php`
  
  
  public function other_cols($column, $row) {
  if (preg_match('/^val(\d+)$/', $column, $matches)) {
  $items = $this->feedbackstructure->get_items();
  $itemobj = feedback_get_item_class($items[$matches[1]]->typ);
  $printval = $itemobj->get_printval($items[$matches[1]], (object) ['value' => $row->$column]);
  if ($this->is_downloading()) {
  $printval = html_entity_decode($printval, ENT_QUOTES);
  }
  return trim($printval);
  }
  return $row->$column;
  }

So, if a user supplied a payload with hex-encoded values, e.g. '<' instead of '<' it would have remained the same after `s()` have had processed it. this would have gone under the radar of the sanitizer, and moodle would have decoded it during rendering process. The stored XSS could have been leveraged to trigger a blind SSRF.

## Impact

An authenticated attacker with the least privilege (student), could inject html/js with a crafted response to feedback activity leading to a stored XSS and blind SSRF. Successful exploitation of the XSS vulnerability allows the attacker to takeover moodle users including teachers and administrators or perform actions on their behalf. Exploiting the Blind SSRF would have given the attacker the ability to interact with internal server services and possible RCE in some environement setups.

## Timeline

12-01-2021 - Reported  
01-02-2021 - Vendor confirmed  
15-03-2021 - Fixed in new release
