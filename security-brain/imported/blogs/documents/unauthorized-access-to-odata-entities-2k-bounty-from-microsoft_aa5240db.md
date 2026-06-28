---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-10_unauthorized-access-to-odata-entities-2k-bounty-from-microsoft.md
original_filename: 2021-01-10_unauthorized-access-to-odata-entities-2k-bounty-from-microsoft.md
title: Unauthorized Access to OData Entities + $2K Bounty From Microsoft
category: documents
detected_topics:
- idor
- access-control
- command-injection
- cors
- information-disclosure
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- cors
- information-disclosure
- api-security
language: en
raw_sha256: aa5240db6f36519d342b88fa8163f8d6948d0a565678af074af9c62d98f1992a
text_sha256: f040b758f4b7247b3dbec331fd085fd76bb7b1db074aa4ac7b41d970634150d5
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthorized Access to OData Entities + $2K Bounty From Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-10_unauthorized-access-to-odata-entities-2k-bounty-from-microsoft.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, cors, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `aa5240db6f36519d342b88fa8163f8d6948d0a565678af074af9c62d98f1992a`
- Text SHA256: `f040b758f4b7247b3dbec331fd085fd76bb7b1db074aa4ac7b41d970634150d5`


## Content

---
title: "Unauthorized Access to OData Entities + $2K Bounty From Microsoft"
url: "https://medium.com/bugbountywriteup/unauthorized-access-to-odata-entities-2k-bounty-from-microsoft-e070b2ef88c2"
authors: ["Borna Nematzadeh (@LogicalHunter)"]
programs: ["Microsoft"]
bugs: ["Broken authorization", "Information disclosure"]
bounty: "2,000"
publication_date: "2021-01-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4011
scraped_via: "browseros"
---

# Unauthorized Access to OData Entities + $2K Bounty From Microsoft

Unauthorized Access to OData Entities + $2K Bounty From Microsoft
Borna Nematzadeh
Follow
7 min read
·
Jan 10, 2021

364

1

Hi, this post is about one of the vulnerabilities I found from Microsoft.

As you know, Office365 has various services. One service that drew my attention was Microsoft Forms. It’s an online survey creator, part of Office 365. You can create your form and share it with other users. This service uses OData for interacting with data. But what is OData?

OData Basics

The OData Protocol is an application-level protocol for interacting with data via RESTful interfaces. It supports the description of data models, editing and querying of data according to those models. [docs.microsoft.com]

OData uses the SQL idea. By saying that I don’t mind what type of client (such as .NET, Java) sent me a request or what the site’s data source is, I receive the request from the client, based on the type of work that client wants, I perform CRUD operations on the data and return the result to the client.

Press enter or click to view image in full size
https://www.progress.com/blogs/what-is-odata-rest-easy-with-our-quick-guide

For simplicity, I explain some concepts of this protocol and do some equivalences. The OData metadata is a data model of the system(consider it as information_schema in relational databases). For each metadata, we have entities(similar to tables in relational databases) and properties (similar to columns) as well as the relationship between different entity types. Each entity type has an entity key that is similar to the key in relational databases. Suppose we have an entity type called Customers, which includes three properties. This entity type has the following records:

In the above example, ID is an entity key. The request below returns an individual record of type Customers by the given ID “2”:

customerApi/Customers(2)

The above request returns the customer information with ID=2. Similar to SQL, we can use query options for querying data. OData supports various kinds of query options for querying data. We can use the $select query option to request a limited set of properties for each entity. The following query is an example, which would fetch the email from the Customers entity for a customer with the ID 2:

customerApi/Customers(2)?$select=email

In SQL, The above example is as follows:

SELECT email FROM Customers WHERE ID=2;

The concepts I have explained so far are enough to understand the continuation of this write-up. Apart from $select, you can use different query options. You can choose the output of data using the $format, whether it is JSON or XML. For further details and getting familiar with other query options, I suggest you this link, which is the main reference for OData.

Attack Scenarios

“One thing I always bear in mind is that I try to get an overview of the system first, and then I start testing each of the components.”

In this target, I first tried to access the OData metadata because I knew the target was using OData, and I’d better get to know the structure of metadata. By sending a request to the following URL, I was able to access the target’s metadata:

http://forms.office.com/formapi/api/$metadata
Press enter or click to view image in full size

The above document, which is an XML, was not interesting to me. So I used the following website to see the connections between different entity types better:

XOData - Visualize and Explore OData Services Online
Explore OData API - OData Metadata Diagram/Documentation and OData Query Builder

pragmatiqa.com

This website is a generic OData API/Service visualizer and explorer. It has a cool feature that you can give the link of OData metadata, and it shows you the connection between different entity types:

Press enter or click to view image in full size

After getting an overview of metadata, I tried to look for entities that could have sensitive information. I found an entity type called forms. This entity had user-generated form’s data as well as the user’s email: ‌

Press enter or click to view image in full size

The email made me think about how I can access other users’ email? IDOR and CORS were not possible here. After testing different attack scenarios, I found a way to access another user’s email. But The problem was that my attack scenario required user interaction(the victim visits the attacker site and more). The user interaction reduced the impact of my attack scenario. After sending my report to MSRC, I only got the Microsoft Hall of Fame.

Unauthorized Access to OData Entities

After I didn’t get any bounty, I tried to look at the target differently. My previous attack scenario required user interaction, So I had to find a way to access the email without any user interaction.
In Microsoft Forms, a user can share a form with others. I tried to test the file-sharing functionality. If User A wants to share a form with User B, the following steps are required:

User A selects a form to share. The server generates a shareable link for User A.
User A sends the generated link from the previous step to User B.
When User B submits the form, the submitted data send to the server. User A can view the submitted data in his/her account.

In the third step, the following request sends:

The above request has the following structure:

formapi/api/<ownerTenantID>/users/<ownerID>/forms(<formID>)/responses

All the parameters ownerTenantID, ownerID, and ‌formID are related to the user who shared the form with us. When we submit the user’s form, we have access to all these parameters, So there is no need to find any of them.

Get Borna Nematzadeh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The scenario which came to my mind was that I had all the necessary parameters from the victim. Why not use the $select query option and get the victim’s email from the server too? To do that, I used the $select query option and sent the following request:

After I sent the above request, I got 404. The server did not allow me to access the createdBy property or the user’s email on forms entity, So I tried to find another way to access the value of the createdBy property, and an idea came to my mind:

“Is there another entity that has a createdBy property? And also has the same entity key (formID) as forms entity?”

The question that may arise is why the entity key should be the same as the forms entity key?

Suppose the entity that we are looking for is called X.

X has the createdBy property, and our point is to access the value of this property because the value of this property is the user’s email. On the other hand, imagine X has an entity key called accountID, which is a random string. To access the email, we have to send the following request:

formapi/api/<ownerTenantID>/users/<ownerID>/X(<accountID>)$select=createdBy

The problem here is the accountID because we don’t know what the accountID of the victim is, But we saw earlier that we have access to formID using the victim’s shared form.

I tried to look for an entity type with the mentioned conditions. After reviewing the relationship between different entity types, I was able to find an entity called runtimeForms that had the createdBy property and even had the same entity key as forms! , which had all the conditions I wanted:

Press enter or click to view image in full size

I used runtimeForms instead of forms then I used the $select query option to access the email. By sending the following request, I finally managed to access the victim’s email:

With this attack scenario, I could access users’ email without any user interaction. Finally, I got a $2k bounty from MSRC ;)

I hope you enjoyed this write-up. Always look for edge cases in your target to find more interesting vulnerabilities! If you liked this write-up, make sure to follow me on Twitter:

Twitter: @LogicalHunter

LinkedIn: https://www.linkedin.com/in/borna-nematzadeh/
