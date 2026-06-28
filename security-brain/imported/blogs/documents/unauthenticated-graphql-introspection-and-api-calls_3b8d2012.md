---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-26_unauthenticated-graphql-introspection-and-api-calls.md
original_filename: 2023-02-26_unauthenticated-graphql-introspection-and-api-calls.md
title: Unauthenticated GraphQL Introspection and API calls
category: documents
detected_topics:
- graphql
- command-injection
- otp
- api-security
tags:
- imported
- documents
- graphql
- command-injection
- otp
- api-security
language: en
raw_sha256: 3b8d2012749ded1e4097f244f4678ff2c7b896bbd3f125c66e8be131766af689
text_sha256: 8a88c2f22e7c9d61100e41f7683b513ffebce20a3b6de4d0e0e925e353cc9f7f
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated GraphQL Introspection and API calls

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-26_unauthenticated-graphql-introspection-and-api-calls.md
- Source Type: markdown
- Detected Topics: graphql, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `3b8d2012749ded1e4097f244f4678ff2c7b896bbd3f125c66e8be131766af689`
- Text SHA256: `8a88c2f22e7c9d61100e41f7683b513ffebce20a3b6de4d0e0e925e353cc9f7f`


## Content

---
title: "Unauthenticated GraphQL Introspection and API calls"
url: "https://medium.com/@osamaavvan/unauthenticated-graphql-introspection-and-api-calls-92f1d9d86bcf"
authors: ["Osama Avvan (@osamaavvan)"]
bugs: ["GraphQL", "Missing authentication"]
publication_date: "2023-02-26"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1471
scraped_via: "browseros"
---

# Unauthenticated GraphQL Introspection and API calls

Top highlight

Unauthenticated GraphQL Introspection and API calls
Osama Avvan
Follow
4 min read
·
Feb 26, 2023

261

5

Assalam u Alikum Everyone, it’s been a while since my last writeup. So here I am with another interesting finding.

Press enter or click to view image in full size

GraphQL Introspection is a feature of the GraphQL specification that allows clients to query information about a GraphQL API’s schema. This can be useful for various purposes, such as generating documentation, building GraphQL clients, and performing validations.

Unauthenticated GraphQL Introspection refers to the ability of anyone, including unauthenticated users, to access the GraphQL Introspection functionality without any restrictions. This means that anyone can query the API’s schema and retrieve all its types, fields, and relationships.

So while hunting on a Bugcrowd Public Program there was a subdomain that doesn’t have any login or signup page or anything interesting so after fuzzing I came across a Graphql endpoint that was allowing Unauthenticated GraphQL Introspection and I was able to make API calls to all the Graphql queries being unauthenticated. To test for the Introspection we will send a POST request with a query.

{"query": "query IntrospectionQuery{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}"}
Press enter or click to view image in full size
Graphql Schema in the HTTP Response

Now copy the whole JSON in the response which is the schema and save it in a file with the .json extension. Now we will use the Burp InQL Scanner Extension, In your Burp Suite click on the InQL scanner tab and click on Load and load the .json file

Press enter or click to view image in full size
Loading the schema file

After the schema is loaded it will create a nice-looking directory structure separating Queries and Mutations.

GraphQL queries are used to fetch data, and they typically take the form of a JSON-like object with a set of fields that define the data to be returned. For example, a query might request a user’s name, email address, and profile picture.

Get Osama Avvan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

GraphQL mutations, on the other hand, are used to modify data on the server. They allow clients to specify the exact changes they want to make, and they can be used to create, update, or delete data. Mutations are similar to queries in structure, but they are typically used to change data on the server rather than retrieve it.

Press enter or click to view image in full size
Graphql isEmailAvailable Query in the query folder

Now we will use the isEmailAvailable query to see which email is taken meaning if the user has an account or not. Select the isEmailAvailable.query and click on the Raw Tab on the top.

Press enter or click to view image in full size
Raw Query which will be used in a POST request

The “code*” in the query indicates that it is expecting a string datatype, which is obvious, Now copy the Raw query and send a POST request at the /graphql endpoint with the JSON query.

Press enter or click to view image in full size
POST request with isEmailAvailable query with my email

As I have already created an account with my email so in the Response we can see it says “is_email_available: false” which means the email is already taken.

Now let’s move to the Mutations, as we now know we can use the mutation query to create/modify data on the server, so now we will be using the createCustomer.query to create an account, copy the RAW query and fill the values according to their fields as we know the “code*” will be replaced with the string values but the gender: field is without quotes so it means that it will be an integer value.

Press enter or click to view image in full size
Graphql createCustomer mutation in the mutation folder

Sending the POST request with fields filled with their respective data.

Press enter or click to view image in full size

The account was created and an access token was returned in the HTTP Response.

Now after creating the account, there was no login page on that subdomain, but after some analysis, it was found that there was another subdomain which was a service portal of the company where these credentials were working and I got access to that portal. That portal had the same Graphql Queries that I had access to before but without any authentication.

Thank you for reading.
