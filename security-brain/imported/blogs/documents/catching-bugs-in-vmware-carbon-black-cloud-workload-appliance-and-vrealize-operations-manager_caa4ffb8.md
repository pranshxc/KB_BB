---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-25_catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-opera.md
original_filename: 2022-02-25_catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-opera.md
title: 'Catching bugs in VMware: Carbon Black Cloud Workload Appliance and vRealize
  Operations Manager'
category: documents
detected_topics:
- access-control
- ssrf
- command-injection
- supply-chain
- sso
- jwt
tags:
- imported
- documents
- access-control
- ssrf
- command-injection
- supply-chain
- sso
- jwt
language: en
raw_sha256: caa4ffb83ad9b9cdf5363702011c3cd69561bc1941d640129bf45bdf0ada25a9
text_sha256: f3ada0f4b5b58aebf01fc08ccede34545c061aa727d042744571ba0b033b8cb5
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Catching bugs in VMware: Carbon Black Cloud Workload Appliance and vRealize Operations Manager

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-25_catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-opera.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, command-injection, supply-chain, sso, jwt
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `caa4ffb83ad9b9cdf5363702011c3cd69561bc1941d640129bf45bdf0ada25a9`
- Text SHA256: `f3ada0f4b5b58aebf01fc08ccede34545c061aa727d042744571ba0b033b8cb5`


## Content

---
title: "Catching bugs in VMware: Carbon Black Cloud Workload Appliance and vRealize Operations Manager"
page_title: "Catching bugs in VMware: Carbon Black Cloud Workload Appliance and vRealize Operations Manager – PT SWARM"
url: "https://swarm.ptsecurity.com/catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-operations-manager/"
final_url: "https://swarm.ptsecurity.com/catching-bugs-in-vmware-carbon-black-cloud-workload-appliance-and-vrealize-operations-manager/"
authors: ["Egor Dimitrenko (@elk0kc)"]
programs: ["VMware"]
bugs: ["Authentication bypass", "RCE", "SSRF", "Path traversal"]
publication_date: "2022-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2868
---

# Catching bugs in VMware: Carbon Black Cloud Workload Appliance and vRealize Operations Manager

Written by [Egor Dimitrenko](https://swarm.ptsecurity.com/author/egor-dimitrenko/ "Posts by Egor Dimitrenko") on February 25, 2022

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/Pre_2.png)

## Author

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/Egor_Dimitrenko-1-150x150.png)

[Egor Dimitrenko](https://swarm.ptsecurity.com/author/egor-dimitrenko/ "Posts by Egor Dimitrenko")

Penetration Tester 

[elk0kc](https://twitter.com/elk0kc "Visit Egor Dimitrenko’s Twitter")

Last year we found a lot of exciting vulnerabilities in VMware products. The vendor was notified and they have since been patched. This is the second part of our research. This article covers an Authentication Bypass in VMware Carbon Black Cloud Workload Appliance (CVE-2021-21978) and an exploit chain in VMware vRealize Operations (CVE-2021-21975, CVE-2021-22023, CVE-2021-21983) which led to Remote Code Execution.

## VMware Carbon Black Cloud Workload Appliance

Our story begins with a vulnerability in the VMware Carbon Black Cloud Workload Appliance, where we managed to bypass the authentication mechanism and gain access to the administrative console.

The appliance is hosted on-premise and is the link between an organization’s infrastructure and VMware Carbon Black Cloud, which is endpoint protection platform.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_1.png)Carbon Black Cloud Workload Components

By checking the ports available on 0.0.0.0 using the netstat command, we found a web-application on port 443.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_2.png)Output of `netstat` command ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_3.png)Application login page

The front-end server was an Envoy proxy server. Upon looking into its configuration file, we determined that further requests are proxied to tomcat-based microservices.

Excerpt from config `/opt/vmware/cwp/appliance-gateway/conf/cwp-appliance-gateway.yaml`:
  
  
  node:
  cluster: cwp_appliance
  id: cwp-appliance-v1-2020
  static_resources:
  clusters:
  -	
  connect_timeout: 5s
  hosts:
  -
  socket_address:
  address: "127.0.0.1"
  port_value: 3030
  lb_policy: round_robin
  name: service_vsw
  type: LOGICAL_DNS
  -
  connect_timeout: 5s
  hosts:
  -
  socket_address:
  address: "127.0.0.1"
  port_value: 3020
  lb_policy: round_robin
  name: service_apw
  type: LOGICAL_DNS
  -
  connect_timeout: 5s
  hosts:
  -
  socket_address:
  address: "127.0.0.1"
  port_value: 3010
  lb_policy: round_robin
  name: service_acs
  type: LOGICAL_DNS
  

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_4.png)Discovery of Java services utilizing `netstat` command

After studying the `application.yml` configuration file for the service, which is called `service_acs` and runs on port 3010, we found that a role-based access model from the Java Spring framework is implemented.
  
  
  // application.yml
  rbacpolicy:
  role:
  - name: SERVICE_USER
  description: This role gives you access to all administration related work
  default: DENY
  permissions:
  - '*:*'
  
  - name: APPLIANCE_USER
  description: This role gives you access to all administration related work
  default: DENY
  permissions:
  - 'acs:getToken'
  - 'acs:getServiceToken' 
  - 'apw:getApplianceDetails'
  - 'apw:getApplianceSettings'
  - 'apw:getNetworkConf' 
  …

A cursory examination of the role policy raises many questions:

  * What is a service user?
  * Why does it have unlimited capabilities?
  * What does the `getServiceToken` API method do?

We decided to start by exploring the `getServiceToken` API method. Opening the source code, we studied the description of this method. “Generate JWT Token for Service Request” meaning that every time an application needs authentication for an internal API method call, it accesses this API and receives an authorization token.

An excerpt from `TokenGeneratorApi.java`:
  
  
  @ApiOperation(
  value = "Generate JWT Token for Service Request",
  nickname = "getServiceToken",
  notes = "",
  response = AccessTokenDTO.class,
  tags = {"TokenGenerator"}
  )
  @ApiResponses({@ApiResponse(
  code = 200,
  message = "OK",
  response = AccessTokenDTO.class
  …
  @RequestMapping(
  value = {"/api/v1/service-token/{serviceName}"},
  produces = {"application/json"},
  method = {RequestMethod.GET}
  )
  ResponseEntity<AccessTokenDTO> getServiceToken(@ApiParam(value = "name of the service which is requesting token",required = true) @PathVariable("serviceName") String serviceName);
  

Let’s try to get the authorization token by accessing the service that is attached to port 3010 from the internal network.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_5.png)Accessing Java Service API method using cURL

We got a JWT token, which turns out to be for the role of our old friend, the service user.

Decoding of the JWT token payload:
  
  
  {
  "sub": "any-service",
  "iss": "user-service",
  "nbf": 1645303446,
  "exp": 1731703446,
  "policy": {
  "role": "SERVICE_USER",
  "permissions": {
  "*": [
  "*"
  ]
  }
  },
  "refreshable": false,
  "iat": 1645303446
  }
  

The prospect of being able to generate a token for a super-user without authentication looks very tempting. Let’s try to do the same trick, but this time externally, through the Envoy server.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_6.png)Attempt to get service token by accessing Envoy server

We failed, although the other API methods of the Java service were available to us. Let’s see how proxying to internal services is organized and study the mechanisms that are responsible for routing.

When using the Envoy proxy server as a front-end server, the routing table can be generated dynamically using the Route Discovery API. To do this, inside the backend service, use DiscoveryRequest and others entities from the `io.envoyproxy.envoy.api` package to describe the configuration of routes.

An example of creating a `/admin/` router using Envoy API:
  
  
  public String routeDiscovery(final DiscoveryRequest discoveryRequest) {
  ...
  Route admin = Route.newBuilder().setMatch(RouteMatch.newBuilder().setPrefix("/admin/").build()).setRoute(RouteAction.newBuilder().setCluster("admin_cluster").setHostRewrite(this.hostName).build())
  Builder virtualHostOrBuilder = VirtualHost.newBuilder().setName("backend").addDomains("*");
  virtualHostOrBuilder.addRoutes(admin);
  VirtualHost virtualHost = virtualHostOrBuilder.build();
  RouteConfiguration routeConfiguration = RouteConfiguration.newBuilder().setName("route").addVirtualHosts(virtualHost).build();
  DiscoveryResponse discoveryResponse = DiscoveryResponse.newBuilder().setVersionInfo("1").addResources(Any.pack(routeConfiguration)).build();
  TypeRegistry typeRegistry = TypeRegistry.newBuilder().add(DiscoveryResponse.getDescriptor()).add(ClusterLoadAssignment.getDescriptor()).add(RouteConfiguration.getDescriptor()).build();
  String response = null;
  ...
  try {
  response = JsonFormat.printer().usingTypeRegistry(typeRegistry).print(discoveryResponse);
  } catch (InvalidProtocolBufferException err) {
  log.error("Error while serializing response", err);
  }
  
  return response;
  }
  

Let’s consider a specific example from the Java service.

An excerpt from `EnvoyXDSServiceImpl.java`:
  
  
  package com.vmware.cwp.appliance.applianceworker.service.impl;
  
  @Component
  public class EnvoyXDSServiceImpl implements EnvoyXDSService {
  ...
  public String routeDiscovery(final DiscoveryRequest discoveryRequest) {
  ...
  Route service_token_block = Route.newBuilder()
  .setMatch(RouteMatch.newBuilder()
  .setPrefix("/acs/api/v1/service-token").build())
  .setRoute(RouteAction.newBuilder().setCluster("service_vsw")
  .setPrefixRewrite("/no_cloud").build()).build();
  
  ...
  Route acs = Route.newBuilder()
  .setMatch(RouteMatch.newBuilder()
  .setPrefix("/acs/").build())
  .setRoute(RouteAction.newBuilder()
  .setCluster("service_acs")
  .setHostRewrite(applianceIPv4Address).build()).build();
  ...
  

We see that when we encounter the URL `/acs/api/v1/service-token`, the application forwards the request to the stub page, instead of passing the request onto the service for processing. At the same time, any URL prefixed with `/acs/*` will be forwarded to the backend. Our task is to bypass the blacklist and pass the whitelist conditions. A special feature of the Envoy server is required to allow us to do that. We read the documentation and found one interesting point: the Envoy server has disabled normalization by default.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_7.png) Excerpt from Envoy [documentation](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto#envoy-v3-api-field-extensions-filters-network-http-connection-manager-v3-httpconnectionmanager-normalize-path) ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_7_2.png) Excerpt from Envoy [documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/best_practices/edge)

Despite the recommendations of the Envoy developers not to forget to enable this property when working with RBAC filters, the default value often remains unchanged, as it is in this case. Disabled normalization means that URL `/acs/api/v1/service-token/rand` and `/acs/api/v1/%73ervice-token/rand` will be treated by Envoy API as non-identical strings, although after normalization by another server, such as tomcat, the urls will be treated as identical again.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_8.png)

It turns out that if we change at least one character in the API-method name to its URL representation, we can bypass the blacklist without violating the whitelist conditions.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_9.png)

We send a modified request and receive a service token.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_10.png)

Done. We now have a service token with super-user privileges, which grants us administrator powers over this software**.**

## VMware vRealize Operations Manager

In the next story we will tell you about the chain of vulnerabilities found in automation software.

### Server-Side Request Forgery

We started by investigating the Operations Manager API , and found a couple of methods available without authentication. These included the API-method `/casa/nodes/thumbprints`, which takes an address as a user parameter. By specifying the address of a remote server under our control as the parameter in HTTP request we receive a GET request from the Operations Manager instance with the URL-path `/casa/node/thumbprint`.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_11.png)Attempting to perform SSRF ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_12.png)GET request in remote server logs

To control the URL-path completely, we can add the “?” symbol to cut off the path normally concatenated to by the application. Let’s send a request with a custom path:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_13.png)Performing SSRF with arbitrary path ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_14.png)GET request in remote server logs

As a result, we were able to make any GET request on behalf of the application, including to internal resources.

Having been able to make a GET request to internal resources, we tried to make a request to some API methods that are available only to an authorized user. So, for example, we got access to the API method for synchronizing passwords between nodes. When calling this method, we get the password hash of the administrator in two different hashing algorithms – sha256 and sha512.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_15.png)Obtaining administrator password hash via replication functionality

It is worth saying that the sha family of algorithms is not recommended for password hashing and can be cracked with high chances of success. And since the administrator in the application corresponds to the system admin user on server, if there is a ssh server in the system with a keyless mode of operation, you can connect to the server and gain access to the command shell. To store sensitive data such as a password, it is best practice to use so-called slow hash functions.

### Credentials Leak

Despite the high probability of gaining shell access at this stage, the above method is not fully guaranteed and so we have continued our research. It is worth noting how, using SSRF, we gain access to API methods that require authentication. We know of several mechanisms that could provide this functionality and, in this case, not the best approach was chosen. The fact is that every time the API is accessed by the application, it adds a basic authentication header to the request. To extract the credentials from the header, we sent an SSRF request to our remote sniffer, which in response outputs the contents of the http request:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_16.png)Extracting credentials with HTTP request sniffer. ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_17.png)`maintenanceAdmin` user credentials

It appears that the application uses the `maintenanceAdmin` user to access the API. Let’s try to use these credentials to access the protected API methods directly, without SSRF.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_18.png)Verifying that account is up and running

Well, now that we have super-user privileges, we’re only one step from taking control of the server. After looking through all the API methods, we found two ways to access the shell.

### RCE (Password Reset)

The first and rough approach involves resetting the password for the administrative user using the `PUT /casa/os/slice/user` API method. This method allows you to change the password for users without additional verification, such as the current password. Since the admin user of the same name exists in the system, it is not hard to connect to the system with its account via SSH.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_19.png)Changing administrator password

If SSH is disabled, simply enable it using one of the API methods.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_20.png)Enabling SSH server ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_21.png)Connecting via ssh to vROps server

### RCE (Path Traversal)

The previous approach involved resetting the administrator password, which can disrupt the customer’s workflow when pentesting. As an alternative approach, we found a way to load a web shell via a path-traversal attack using the `/casa/private/config/slice/ha/certificate` API method. A lightweight JSP-shell uploaded to the web directory of the server will be used as the web shell.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_22.png)Exploiting path-traversal attack

After uploading, we access the shell at https://vROps.host/casa/webshell.jsp, passing the command in the `cmd` parameter.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/img_23.png)Execution of `id` command on the vROps server

## Outro

Thank you for reading this article to the end. We hope you were able to find something useful from our research. Whether you are a developer, a researcher or maybe even the head of PSIRT.

We also would like to highlight that this research resulted in 9 CVEs of varying severities, and each report was handled with the utmost care by the VMware Security Response Center team. We appreciate VMware for such cooperation.

[Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/)
