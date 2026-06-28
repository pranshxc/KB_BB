---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-13.md
original_filename: 2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-13.md
title: 'Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)'
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
- oauth
- access-control
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
- oauth
- access-control
language: en
raw_sha256: b8733ad3328dd2750c3ffb9db5ab4caf8638d03331ea3727e49d9cb321a5ae0b
text_sha256: 21261952d678890d8be2f4332833d695e730989c1efe8e43950ac2606bff5724
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-15_checkmk-remote-code-execution-by-chaining-multiple-bugs-13.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security, oauth, access-control
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `b8733ad3328dd2750c3ffb9db5ab4caf8638d03331ea3727e49d9cb321a5ae0b`
- Text SHA256: `21261952d678890d8be2f4332833d695e730989c1efe8e43950ac2606bff5724`


## Content

---
title: "Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)"
page_title: "Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3) | Sonar"
url: "https://blog.sonarsource.com/checkmk-rce-chain-1/"
final_url: "https://www.sonarsource.com/blog/checkmk-rce-chain-1/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["Checkmk"]
bugs: ["RCE", "Code injection", "SSRF", "Line Feed injection", "Arbitrary file read", "Authentication bypass", "Security code review"]
publication_date: "2022-11-15"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 1912
---

## TL;DR overview

  * Part one of Sonar's Checkmk vulnerability series identifies the initial attack surface in this widely used IT infrastructure monitoring platform—finding several weaknesses that individually may seem low-risk but are part of a dangerous exploitation chain.
  * The research focuses on how Checkmk's agent and server communication can be abused to stage the conditions for remote code execution, beginning with an authentication bypass in a specific service endpoint.
  * Checkmk is deployed in many enterprises for monitoring servers and network devices; vulnerabilities in the platform can provide attackers with visibility into—and access to—critical infrastructure.
  * Users of Checkmk should apply available patches and review their agent communication security configurations to reduce exploitation risk.

Checkmk is a modern IT infrastructure monitoring solution developed in Python and C++. According to the vendor’s website, more than 2,000 customers rely on Checkmk. Due to its purpose, Checkmk is a central component usually deployed at a privileged position in a company’s network. This makes it a high-profile target for threat actors.

In our effort to help secure the open-source world, we decided to look at the open-source edition of Checkmk, which is based on a Nagios monitoring core and seamlessly integrates NagVis to visualize status data on maps and diagrams. During our research, we identified multiple vulnerabilities in Checkmk and its NagVis integration, which can be chained together by an unauthenticated, remote attacker to fully take over the server running a vulnerable version of Checkmk.

In this first article, in a series of three, we start by getting an overview of all identified vulnerabilities and a basic understanding of the Checkmk architecture. Furthermore, we determine the disastrous impact of chaining the identified vulnerabilities together. We also dive deep into the technical details of the first two vulnerabilities, which pave the way for an unauthenticated attacker to gain remote code execution.

## Impact

We discovered multiple vulnerabilities in Checkmk and its NagVis integration with the following CVSS scores assigned by the vendor:

  * CVSS 9.1: Code Injection in watolib’s auth.php (CVE-2022-46836)
  * CVSS 9.1: Arbitrary File Read in NagVis (CVE-2022-46945)
  * CVSS 6.8: Line Feed Injection in ajax_graph_images.py (CVE-2022-47909)
  * CVSS 5.0: Server-Side Request Forgery in agent-receiver (CVE-2022-48321)

These vulnerabilities can be chained together by an unauthenticated, remote attacker to gain code execution on the server running Checkmk version 2.1.0p10 and lower:

We verified the exploitation for the open-source Raw Edition by leveraging a specific feature of its monitoring core. It is likely that an attacker can use similar techniques to exploit a server running an Enterprise Editions.

All of these issues are fixed with Checkmk version 2.1.0p12. We strongly recommend updating any instance with a version before this release.

## Technical Details

In this section, we start by looking at the basic architecture of Checkmk and its components. Based on this, we outline how the identified vulnerabilities can be chained together by an attacker and deep dive into the technical details of the first two vulnerabilities, which are the beginning of a full chain to gain unauthenticated, remote code execution.

### Background

Checkmk is an IT infrastructure monitoring solution similar to Zabbix or Icinga. The configuration and monitoring of servers, networks, applications, etc., is done via a web interface. This user-facing component is developed in Python and is called Checkmk GUI.

In order to retrieve additional information from the monitored systems, it is possible to deploy a monitoring agent on these systems. The component responsible for registering agents and receiving data from these agents is called the agent-receiver.

The following picture outlines the basic architecture of Checkmk:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/ae791816-c5a1-4c21-9755-c1936717d1b5/body-56ba7506-82d9-4b1f-98ea-dd5aff445ab0_checkmk-architecture.png)

Checkmk exposes two ports on the external network interface by default:

  * TCP port 80: actual web interface
  * TCP port 8000: agent-receiver

The first component of the web interface is an Apache web server running on TCP port 80, which serves as a reverse proxy. It is possible to run multiple Checkmk instances on a single host. These instances are called monitoring sites or simply sites. For each site, a dedicated, internal Apache server is spawned. The purpose of the outer reverse proxy is to map requests for a specific site to the corresponding internal Apache server dedicated to the requested site. In the picture above, the site `monitoring` is mapped to the Apache server running on TCP port 5000. From the outside, this Apache server can only be reached via the reverse proxy because it only listens on localhost.

The site-dedicated Apache server forwards requests to either the actual Checkmk GUI, a Python WSGI application, or via FCGI to a PHP wrapper in order to integrate the NagVis PHP component.

The heart of Checkmk is the monitoring core, which is responsible for initiating checks, collecting data, detecting state changes, and providing information to the GUI. While the Checkmk Enterprise Editions have their own monitoring core, the open-source Raw Edition uses a Nagios monitoring core. To retrieve data from it, the core provides an interface called Livestatus, which is implemented as a C++ Nagios broker module called `livestatus.o`. This interface uses a proprietary protocol called Livestatus Query Language (LQL), which is similar to both HTTP and SQL. For example, a query to retrieve the name and IP address of all monitored hosts, which are in `DOWN` (`1`) or `UNREACH` (`2`) state, looks like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/370c1d0d-b6b5-4081-93d3-3926b2bcdff0/body-c8c4d41f-6c49-4f93-b107-4581c88947b5_checkmk-lql01.png)

The response may look like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/918bfc87-0ea1-4e2d-9a08-09762001f068/body-2bdbf195-1413-46f6-ae01-fae0a3e84331_checkmk-lql02.png)

More advanced queries can be built by using additional headers. Whenever the GUI needs some data from the core, it sends an LQL query to it, and the core responds with the requested data.

The second component directly reachable via the external interface is the `agent-receiver`. The agent-receiver is a FastAPI web server listening on TCP port 8000, which provides different routes for registering agents and collecting data from these agents.

With this basic understanding of Checkmk’s components, let’s see how an unauthenticated attacker would be able to chain the identified code vulnerabilities together in order to gain remote code execution.

### Exploitation Chain

Some of the identified vulnerabilities have limited practical impact on their own. However, a malicious attacker can chain them together to achieve remote code execution.

The following picture summarizes what abilities the exploitation of an individual vulnerability yields and how an attacker can build on this ability to leverage the following vulnerability to further increase control, which finally results in unauthenticated, remote code execution:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/513dbea0-f520-4135-9136-fdd6f4284af6/body-fee129ee-2bd1-496a-9e34-2cbabbf0e3b2_checkmk-chain-all.png)

The exploitation chain starts with a Server-Side Request Forgery in the agent-receiver (1), which can be leveraged by an attacker to access an endpoint only reachable from localhost. This endpoint is vulnerable to a Line Feed Injection (2). This gives an attacker the ability to forge arbitrary LQL queries, which are used by the Checkmk GUI to retrieve data from the monitoring core. An attacker can take advantage of this ability to delete arbitrary files, which can further be leveraged to bypass the authentication mechanism in the NagVis component.

Once an attacker has gained access to the NagVis component, an authenticated Arbitrary File Read vulnerability (3) in NagVis can be leveraged to read a special Checkmk configuration file called `automation.secret`. With access to the contents of this file, an attacker can gain access to the Checkmk GUI in the context of the automation user. This access can further be turned into remote code execution by exploiting a Code Injection vulnerability (4) in a Checkmk GUI subcomponent called `watolib`, which generates a file named `auth.php` required for the NagVis integration. 

After this rough overview of the exploitation chain, let’s dive into the technical details of the first two code vulnerabilities:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/cabcbae5-c8fc-4c9d-8b75-a71530f6fea6/body-0be46e6a-d02d-432c-bd7b-65086e8da82e_checkmk-chain-01.png)

### Server-Side Request Forgery in agent-receiver (CVE-2022-48321)

The Checkmk agent-receiver is a FastAPI web server, which is by default exposed on TCP port 8000. Most of the provided endpoints forward requests to the Checkmk REST API, which is part of the Checkmk GUI exposed on TCP port 80.

The endpoint called `/register_with_hostname` expects a POST request with credentials provided via HTTP Basic authentication as well as the two JSON-encoded parameters `uuid` and `host_name` in the body. The endpoint handler itself only verifies that any credentials are provided and that the two parameters are present.

In order to retrieve and validate the host configuration of the host identified by the `host_name` parameter, the function `host_configuration` is called:

**checkmk/agent-receiver/agent-receiver/endpoints.py**

Copy to clipboard
  
  
  @agent_receiver_app.post(
  "/register_with_hostname",
  status_code=HTTP_204_NO_CONTENT,
  )
  async def register_with_hostname(
  *,
  credentials: HTTPBasicCredentials = Depends(security),
  registration_body: RegistrationWithHNBody,
  ) -> Response:
  _validate_registration_request(
  host_configuration(
  credentials,
  registration_body.host_name,
  )
  )

The `host_configuration` function forwards the request to the Checkmk REST API by calling the function `_forward_get`. The user-provided parameter `host_name` is appended to the target URL without any sanitization or encoding:

**checkmk/agent-receiver/agent-receiver/checkmk_rest_api.py**

Copy to clipboard
  
  
  def host_configuration(
  credentials: HTTPBasicCredentials,
  host_name: str,
  ) -> HostConfiguration:
  if (
  response := _forward_get(
  f"objects/host_config_internal/{host_name}",
  credentials,
  )
  ).status_code == HTTPStatus.OK:

This lack of sanitization and encoding leads to a limited Server-Side Request Forgery (SSRF) vulnerability.

At first, the impact of this vulnerability does not seem to be very high because the SSRF is limited to a GET request to the hostname and port of the Checkmk GUI, and an attacker cannot even read the response. However, this gives an attacker the essential ability to exploit a second vulnerability. Let’s have a look at it.

### Line Feed Injection in ajax_graph_images.py (CVE-2022-47909)

The Checkmk GUI only provides a minimal number of unauthenticated endpoints. This greatly reduces the attack surface. One of the unauthenticated endpoints is called `/ajax_graph_images.py`, whose endpoint handler is implemented in the function `ajax_graph_images_for_notifications`. The purpose of this endpoint is to generate an image with performance data for a given host or service.

Although this endpoint can be accessed unauthenticated, access is restricted by only allowing requests, which originate from localhost (`127.0.0.1` or `::1`):

**checkmk/cmk/gui/plugins/metrics/graph_images.py**

Copy to clipboard
  
  
  def ajax_graph_images_for_notifications(
  resolve_combined_single_metric_spec: Callable[
  [CombinedGraphSpec], Sequence[CombinedGraphMetricSpec]
  ],
  ) -> None:
  """Registered as `noauth:ajax_graph_images`."""
  if request.remote_ip not in ["127.0.0.1", "::1"]:
  raise MKUnauthenticatedException(
  _("You are not allowed to access this page (%s).") % request.remote_ip
  )
  
  with SuperUserContext():
  _answer_graph_image_request(resolve_combined_single_metric_spec)

After verifying that the request originates from localhost, the function `_answer_graph_image_request` is called. This function validates that a `host` GET parameter is provided and then calls `get_graph_data_from_livestatus`:

**checkmk/cmk/gui/plugins/metrics/graph_images.py**

Copy to clipboard
  
  
  def _answer_graph_image_request(
  resolve_combined_single_metric_spec: Callable[
  [CombinedGraphSpec], Sequence[CombinedGraphMetricSpec]
  ],
  ) -> None:
  try:
  host_name = request.get_ascii_input_mandatory("host")
  if not host_name:
  raise MKGeneralException(_('Missing mandatory "host" parameter'))
  ...
  try:
  row = get_graph_data_from_livestatus(site, host_name, service_description)

The function `get_graph_data_from_livestatus` retrieves performance data for the given host via the Livestatus Query Language (LQL) interface. When inspecting all invoked functions within the call stack, the `_ensure_connected` function caught our attention:

**checkmk/cmk/gui/sites.py**

Copy to clipboard
  
  
  def _ensure_connected(user: Optional[LoggedInUser], force_authuser: Optional[UserId]) -> None:
  ...
  if force_authuser is None:
  request_force_authuser = request.get_str_input("force_authuser")
  force_authuser = UserId(request_force_authuser) if request_force_authuser else None
  ...
  _set_livestatus_auth(user, force_authuser)

Although this is an internal function part of the code responsible for querying the LQL interface, a GET parameter called `force_authuser` is accessed. Further inspecting the call stack reveals that this GET parameter is inserted into the `AuthUser` header of the LQL query without any sanitization:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7825f82a-64fc-4f61-9a7f-a904d193fa41/body-e318ed88-2801-4022-8008-52278c807470_checkmk-call-chain.png)

The `AuthUser` header is used to restrict the response to data that the specified user is allowed to see. However, this is not essential for our considerations. The important aspect is that the above `AuthUser` string contains the value of the GET parameter `force_authuser` and this string is inserted into the final LQL query sent to the monitoring core. Since the GET parameter `force_authuser` is not sanitized, it is also possible to insert line feed characters (`0x0a`) into the LQL query.

Usually, an external attacker cannot reach the vulnerable endpoint `/ajax_graph_images.py` because it is restricted to localhost only. When combined with the SSRF vulnerability in the agent-receiver this assumption is not valid anymore. The SSRF can for example be used to trigger a request with the following GET parameter:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/cb4aa71c-c800-4238-b104-2143a02744a2/body-e60362bc-c948-4f30-a479-13361f2d6f0b_checkmk-lql03.png)

This request results in the following LQL query sent to the core:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/f99c493c-2621-4db0-9f45-9afd1a1c48e0/body-9c478387-d0cc-447c-a268-3b2642531ada_checkmk-lql04.png)

By using a line feed character in the `force_authuser` parameter, additional headers can be injected into the LQL query:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/d986d7f6-c177-48fa-b6e3-2a89da050952/body-ca7068d7-f018-4ce8-a73e-af5d1afbe4f8_checkmk-lql05.png)

The resulting LQL query contains the additional header:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/53cdfe7b-d1cd-4ad7-92e2-9a4b55446755/body-c0bf8765-7219-410b-afe4-acb30c23fda7_checkmk-lql06.png)

The ability to inject a whole new query in order to use other tables or commands would increase the attack surface even more. An attacker could try to add two line feed characters and insert a new query after these:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0990d946-c8e1-437d-b469-c1e7d45a53fd/body-6f87ff83-4563-44d8-a7e7-914755d75e4b_checkmk-lql07.png)

However, the LQL interface terminates the connection by default if two subsequent line feed characters are read, which form the end of a single query. Thus the second query is not evaluated:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/012c2ca4-069e-4d7e-8033-f1196ef32b0e/body-5d27877e-3e24-4941-ae23-0e06e20b52f9_checkmk-lql08.png)

This behavior can be altered by leveraging the `KeepAlive` header. When this header is set to `on`, the connection will be kept alive. This way whole new LQL queries can be injected:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/91965d31-1d7b-4942-955e-d455eacee56b/body-4e5a78ae-76c4-4aae-a4ea-04dc51a0166d_checkmk-lql09.png)

This results in three distinct LQL queries, which are processed separately.

Query 1:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/70a8ca1f-1ae1-493b-96f3-69a81c3c9147/body-02382b7a-8857-4dbb-bdc3-8e0b6798a7b4_checkmk-lql10.png)

Query 2:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/15083dab-a18a-4d20-9463-191a46264108/body-3f34cb05-829c-4e03-9e54-5d39416a999f_checkmk-lql11.png)

Query 3:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/e0e965b2-9cb7-4a20-8321-096be8f6c9c5/body-0e888fc8-99ac-4952-9cb2-946cf15a2e44_checkmk-lql12.png)

The second query can be fully controlled by an attacker.

With this ability, an attacker has literally made it to the core of Checkmk. Within the next article of this series, we will explore the LQL interface as a new attack surface and see how some minor differences in a developer’s implementation can prevent or enable an attacker to bypass authentication mechanisms.

### Patch

Checkmk patched the [limited SSRF](https://checkmk.com/werk/14385) in the agent-receiver in version 2.1.0p12 ([commit](https://github.com/tribe29/checkmk/commit/2a384409a17c33422964f9d61327aaf49da069e7)). According to our recommendations, the endpoint handler for `/register_with_hostname` now URL-encodes the `host_name` parameter before inserting it into the URL:

**checkmk/agent-receiver/agent-receiver/checkmk_rest_api.py**

Copy to clipboard
  
  
  from urllib.parse import quote
  ...
  
  def _url_encode_hostname(host_name: str) -> str:
  ...
  return quote(host_name, safe="")  # '/' is not "safe" here
  ...
  
  def host_configuration(...):
  ...
  response := _forward_get(
  f"objects/host_config_internal/{_url_encode_hostname(
  host_name)}", ...)
  ...

This prevents an attacker from accessing other endpoints than the intended one when the request is forwarded to the Checkmk REST API.

The [Line Feed Injection vulnerability](https://checkmk.com/werk/14384) was also patched with version 2.1.0p12 ([commit](https://github.com/tribe29/checkmk/commit/2e8cf315be262df7a749c55f205ff21f895a84db)) by validating the value provided for the `AuthUser` header:

**checkmk/livestatus/api/python/livestatus.py**

Copy to clipboard
  
  
  # Pattern for allowed UserId values
  validate_user_id_regex = re.compile(r"^[\w_][-\w.@_]*$")
  ...
  # Set user to be used in certain authorization domain
  def set_auth_user(self, domain: str, user: UserId) -> None:
  # Prevent setting AuthUser to values that would be rejected later. See Werk 14384.
  # Empty value is allowed and used to delete from auth_users dict.
  if user and validate_user_id_regex.match(user) is None:
  raise ValueError("Invalid user ID")

Also, an additional check for injected line feed characters was introduced:

**checkmk/livestatus/api/python/livestatus.py**

Copy to clipboard
  
  
  def build_query(self, query_obj: Query, add_headers: str) -> str:
  # Prevent injection of further livestatus commands inside AuthUser header.
  if "\n" in self.auth_header[:-1]:
  raise MKLivestatusQueryError("Refusing to build query with invalid AuthUser header.")

These patches effectively prevent an attacker from injecting line feed characters in the `force_authuser` parameter.

## Timeline

**Date**| **Action**  
---|---  
2022-08-22| We report all issues to Checkmk.  
2022-08-23| Vendor confirms all issues.  
2022-09-15| Vendor releases patched version 2.1.0p12.  
  
## Summary

In this first article in a series of three, we briefly introduced the Checkmk architecture and outlined the vulnerabilities we identified including the serious impact of chaining these together. We also did a technical deep dive into the first two vulnerabilities, which enable an external attacker to send arbitrary LQL queries to the monitoring core.

The root cause of most vulnerabilities is the lack of sanitization of user-controlled data. This is also true for both of the vulnerabilities we looked at. The Line Feed Injection vulnerability is somehow hard to spot because the user-controlled data is accessed by a function deep down in the call stack and not directly in the endpoint handler. This is generally a bad pattern and should be prevented.

In the next article in this series, we will have a more detailed look at the LQL interface and derive the impact of an attacker’s ability to forge arbitrary queries. We will also look at Checkmk’s NagVis integration and how the aforementioned ability can be leveraged to bypass the authentication of NagVis due to some specific implementation details.

Finally, we would like to thank the Checkmk team very much for quickly responding to our report, handling each issue with absolute transparency, and providing a comprehensive patch for all reported vulnerabilities.

## Related Blog Posts

  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (2/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-2/)
  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (3/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-3/)
  * [Zabbix - A Case Study of Unsafe Session Storage](https://www.sonarsource.com/blog/zabbix-case-study-of-unsafe-session-storage/)
  * [Path Traversal Vulnerabilities in Icinga Web](https://www.sonarsource.com/blog/path-traversal-vulnerabilities-in-icinga-web/)
