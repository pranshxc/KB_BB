---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-12_500-getclass.md
original_filename: 2019-12-12_500-getclass.md
title: $500 getClass
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 7a18e1be4ab7c8fcc7c168953920497afd5cdf4569e9b162efc1fcae54273905
text_sha256: 222216e6233c7c6b4493a254ebf3dedbf20e25c472992dde04430975a5a04b37
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# $500 getClass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-12_500-getclass.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7a18e1be4ab7c8fcc7c168953920497afd5cdf4569e9b162efc1fcae54273905`
- Text SHA256: `222216e6233c7c6b4493a254ebf3dedbf20e25c472992dde04430975a5a04b37`


## Content

---
title: "$500 getClass"
url: "https://www.ezequiel.tech/p/500-getclass.html"
final_url: "https://www.ezequiel.tech/p/500-getclass.html"
authors: ["Ezequiel Pereira (@epereiralopez)"]
programs: ["Google"]
bugs: ["Sandbox bypass"]
bounty: "500"
publication_date: "2019-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4893
---

###  $500 getClass 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[Google Apps Script](https://www.google.com/script/start/) is a nice service that allows to automate tasks and add features in some Google services.

In order to achieve this, it uses [Rhino](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino), which runs on Java.  

I found that on Google Apps Scripts, several objects that are enumerations had the "getClass" method publicly accessible, for instance:

`Utilities.Charset.getClass()`

  

That line would return a Java [Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html) object, and allowed me to call any of its methods, therefore I could get some information.

  
There was a catch though, Google Apps Scripts implements a white-list of which Java objects can be accessed, most of the objects returned by interesting getClass methods were not in that white-list, so I could not exploit almost anything.  

But I kept trying, and I discovered a nice little thing, any method returning an array was allowed to proceed. And even though I could not open the contents of the array (Therefore, not even list them), I found a workaround.

Every array was converted to a JavaScript array, and for some reason using the method _shift_ on one will return the corresponding object wrapped around a white-listed class.

I could not do much with that wrapper, if I even attempted to see its methods (with a for-each loop) the execution of the script would fail, the only thing I could do was sending it to _Logger.log_ so I could see a representation of the object as a String.  

This was enough to find a few interesting things about the inner workings of Google (Like finding a class called "com.google.apps.maestro.server.beans.memegen.api.MemegenService"), which seems related to the internal [Google Meme Generator](https://www.buzzfeed.com/reyhan/inside-googles-internal-meme-generator) (Located in [memegen.googleplex.com](http://memegen.googleplex.com/)).  

_**Timeline (UTC-3)**_

_2016-08-15, 10:52 PM_ \- **Initial report**

_2016-08-16, 09:22 AM_ \- **Report triaged**  
 _2016-08-17, 10:22 AM_ \- **Bug filed**  
 _2016-08-23, 12:35 PM_ \- **Reward of $500 issued - My first Google VRP reward** :)  
_2016-08-26, 01:24 PM_ \- **Bug fixed and verified**

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/6070397520912981280?pa=1348958821749656904&hl=en&saa=85391&origin=https://www.ezequiel.tech&skin=emporio)
