---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-09_pwnassistant-controlling-homes-via-a-home-assistant-rce.md
original_filename: 2023-05-09_pwnassistant-controlling-homes-via-a-home-assistant-rce.md
title: PwnAssistant - Controlling /home's Via A Home Assistant RCE
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- sso
- idor
- access-control
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- sso
- idor
- access-control
language: en
raw_sha256: c3a09eb4bd387ba3c0fcd0af5e12763a11974bdcc6040dfa61c62cb012396bf4
text_sha256: a593a0fab9e942aeccdb0bf4e9766164e8f681d08a461271ade5e1fac0737047
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# PwnAssistant - Controlling /home's Via A Home Assistant RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-09_pwnassistant-controlling-homes-via-a-home-assistant-rce.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, sso, idor, access-control
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `c3a09eb4bd387ba3c0fcd0af5e12763a11974bdcc6040dfa61c62cb012396bf4`
- Text SHA256: `a593a0fab9e942aeccdb0bf4e9766164e8f681d08a461271ade5e1fac0737047`


## Content

---
title: "PwnAssistant - Controlling /home's Via A Home Assistant RCE"
page_title: "PwnAssistant - Controlling /home's via a Home Assistant RCE - elttam"
url: "https://www.elttam.com/blog/pwnassistant/"
final_url: "https://www.elttam.com/blog/pwnassistant"
authors: ["elttam (@elttam)"]
programs: ["Home Assistant"]
bugs: ["Authentication bypass", "RCE", "Security code review", "IoT"]
publication_date: "2023-05-09"
added_date: "2023-05-11"
source: "pentester.land/writeups.json"
original_index: 1173
---

[Skip to main content](/#main)

Important Update Banner

Close Announcement Banner

[](/)

  * [What We Do](/what-we-do)
  * [How We Work](/how-we-work)
  * [RESOURCES](/resources)
  * [About Us](/about-us)

  * [](/contact)

Contact Us

CONTACT US

[](/)

  * [What We Do](/what-we-do)
  * [How We Work](/how-we-work)
  * [RESOURCES](/resources)
  * [About Us](/about-us)

  * [](/contact)

Contact Us

CONTACT US

By

elttam

May 9, 2023

# PwnAssistant - Controlling /home's via a Home Assistant RCE

Auditing the Home Assistant Pre-Auth Attack Surface

web

iot

cve-2023-27482

On This Page

TOC Element

Share:

## Introduction

Recently, a few members in our team decided to look into home automation and the inherent risks that come with having a “smart home”. Although IoT devices and their associated cloud infrastructure may pose a risk on it’s own, we decided to look into the very established and known open-source automation ecosystem known as [Home Assistant](https://www.home-assistant.io).

As the idea of a smart home increases in popularity, so do the inherent risks, and often users are left asking themselves: How secure is this device? Where is my data going? Who else can see my data? Thankfully, software such as Home Assistant exists, with the goal of taking those smart devices offline, or at least away from the vendor managed cloud instances or required additional hardware bridges.

Home Assistant used to be targeted towards the more tech savvy, and those who wanted to tinker and really configure every detail of the devices they wanted to control within the household. However, as popularity increased, the suite of products has become much more user friendly and has built readily available images for all kinds of architectures, devices (Raspberry Pi) and OS’.

Although Home Assistant aims to bring devices offline and return power to the user, many users still aim to access their instances remotely, whether that be through a private VPN tunnel, or perhaps exposure to the internet. Some online research even suggests that there are over [130,000](https://www.shodan.io/search?query=product%3A%22Home+Assistant%22) publicly accessible instances (that we know of).

The potential impacts of a home network compromise can be disastrous. [News](https://www.theverge.com/2023/2/28/23618353/lastpass-security-breach-disclosure-password-vault-encryption-update) surrounding the recent LastPass data breach revealed that attackers were able to compromise a developer account through a targeted attack against a service running on an employee’s personal home network. Given Home Assistant’s role in managing devices on a home network, it’s not unreasonable to imagine how a critical vulnerability in it may lead to a complete takeover of a home and give an attacker the ability to control cameras or listen in on private conversations. Furthermore, Home Assistant’s vast interconnectivity with third-party services means many users store sensitive credentials in plaintext on their Home Assistant machines – a compromise of these could lead to even more severe consequences. As such, security should be at the forefront of mind when developing or using any sort of system of this nature.

So without further ado, come with us on this journey to understanding the Home Assistant architecture, enumerating the attack surface and trawling for pre-authentication vulnerabilities within the code base.

## Architecture

The aim of this section is to give an architectural overview of Home Assistant to provide context about the different components which we’ll discuss in this post. The developers documentation already gives a great [overview](https://developers.home-assistant.io/docs/architecture_index/) so we encourage giving that a read for some extra background.

Home Assistant can be [installed](https://www.home-assistant.io/installation/) in four different ways. These different installation types give users the ability to run Home Assistant according to their requirements and customise how much or how little is automatically managed.

  * The recommended installation method is via the _Home Assistant Operating System (HAOS)_ , which is a fully fledged Linux based operating system that runs the various Home Assistant components in Docker containers. This is intended to be run on devices like a Raspberry Pi, or within a virtual machine.
  * The standalone _Home Assistant Container_ installation method is also recommended and provides a convenient way to run Home Assistant on a machine with Docker. This installation method does not come with the Supervisor component, so it misses out on a few features, namely add-ons.
  * The _Home Assistant Supervised_ installation involves manually installing the Supervisor component on a Linux system which gives the full Home Assistant experience while letting the user manage the operating system themself.
  * Finally, the _Home Assistant Core_ installation method is another manual installation in which the user runs the Home Assistant Core application directly with Python. As with the Home Assistant Container method, this does not come with the Supervisor component.

The three main components of a Home Assistant installation are the Home Assistant Core application, the Supervisor and the Operating System. All installations run at least the Core, while only the Supervised and Operating System installations run the Supervisor component. Since the Operating System component is only included in HAOS installations and because of its harder-to-reach attack surface, it was not an area of significant focus during our research. The other two components however, proved to be quite interesting to look at.

### Home Assistant Core

Home Assistant Core is, as its name suggests, the core of a Home Assistant installation. It is a Python application whose source code can be found in the [home-assistant/core](https://github.com/home-assistant/core) repository where it is very actively developed. The Core is what an end user, IoT device or service interacts with. It even talks to the Supervisor to make it easy for a user to manage things like backups and add-ons from within the web user interface. The core of the Core however is actually quite minimal. Some of the most interesting functionality Home Assistant has to offer is provided through _integrations_.

Integrations are Python modules that enrich the Home Assistant experience by leveraging helper classes made available by the Core to perform all sorts of useful things. These kinds of things can range from simple tasks like [downloading files](https://www.home-assistant.io/integrations/downloader) and [processing video and audio with FFmpeg](https://www.home-assistant.io/integrations/ffmpeg/) to providing an interface for other integrations to expose [HTTP](https://www.home-assistant.io/integrations/http/) endpoints and register [WebSocket](https://www.home-assistant.io/integrations/websocket_api/) commands. Even the [frontend](https://www.home-assistant.io/integrations/frontend/) web user interface is implemented as an integration. There’s also an integration that literally performs [integration](https://www.home-assistant.io/integrations/integration/).

Anyone can [develop](https://developers.home-assistant.io/docs/creating_component_index) and install custom integrations. The Core itself also comes with a bunch of built-in integrations, which can be found in the [`core/homeassistant/components/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components) directory.

### The Supervisor Component

The Supervisor component is a Python program that lives in the [home-assistant/supervisor](https://github.com/home-assistant/supervisor/) repository. Its responsibility is to manage various parts of the Home Assistant installation by doing things like actually running/updating Home Assistant Core, managing backups, managing add-ons and even updating the operating system (when running a HAOS installation).

It exposes a [HTTP API](https://developers.home-assistant.io/docs/api/supervisor/endpoints/) which is how the Core communicates with it. In the default HAOS installation, this service is not exposed on the network, so it is not possible to access this API remotely or even from within the same LAN.

The Home Assistant developers documentation provides some great diagrams to summarise the overall architecture and an example of how different components interact with the Core:

![](https://cdn.prod.website-files.com/6971f0e051b588235e8acf7b/69c28575e262b9a57b2b1554_69b98971b012f7a8f606fecb_architecture-full.svg)

![](https://cdn.prod.website-files.com/6971f0e051b588235e8acf7b/69c28575e262b9a57b2b155d_69b98971b012f7a8f606fed4_architecture-component-interaction.svg)

## Attack Surface Enumeration

Home Assistant is a big application with a lot of moving parts. Although we had spent some time understanding the architecture and how things fit together, we needed to narrow the focus down a bit to a reasonable subset of components and code to manually audit.

Before properly diving deep into testing and auditing, we noted a few things that we considered interesting from a security perspective:

  * There is (somewhat) a concept of privilege separation between user accounts
  * Devices can be automatically discovered and configured by Home Assistant
  * A web application runs on port 8123 and makes extensive use of HTTP APIs and WebSockets

### Privilege Separation

Differing user permissions within an application is always an interesting thing to look into as vulnerabilities which allow a user to elevate their privileges or otherwise do something they shouldn’t be permitted to do can often have severe consequences. Home Assistant has a concept of user levels – the first account created when you set up a Home Assistant instance is the _owner_ , and the owner can create other _administrator_ and _user_ accounts. However, as of Home Assistant 2023.4.6 (the latest version at the time of writing), there is no functional difference between administrator and user accounts. User accounts are unable to view the settings page within the web application user interface, but otherwise has practically the same access as administrator users in API endpoints and as such can trivially escalate privileges to that of an administrator.

This is well documented in both the [user documentation](https://www.home-assistant.io/docs/authentication/#user-accounts) and [developer documentation](https://developers.home-assistant.io/docs/auth_permissions/). Additionally, when creating a new user through the web application user interface, a message is included which makes note of this:

![](https://cdn.prod.website-files.com/6971f0e051b588235e8acf7b/69c28575e262b9a57b2b1559_69b98971b012f7a8f606fed0_add-user-warning.avif)

A [developer blog post](https://developers.home-assistant.io/blog/2019/03/11/user-permissions/) from 2019 highlights the work-in-progress status of the user permission system and how they plan to properly enforce the distinction between users and administrators. What this means for us is that the authenticated attack surface is still an interesting target, even if not immediately useful.

### Local Attack Surface

Part of what makes Home Assistance so convenient is it’s ability to automatically discover and configure devices in your home. This convenience naturally comes with some risks as it exposes services over the LAN – services which could be targeted for lateral movement given an attacker is able gain a foothold in the local network, for example, by compromising a device via the internet. By default, Home Assistant provides a few core integrations which allow other integrations to implement auto-discovery. We found the following to be the most widely used:

  * [Zero-configuration networking (zeroconf)](https://www.home-assistant.io/integrations/zeroconf/)
  * [Simple Service Discovery Protocol (SSDP)](https://www.home-assistant.io/integrations/ssdp/)
  * [DHCP Discovery](https://www.home-assistant.io/integrations/dhcp/)

While these integrations present some interesting attack surface, we noted that a much larger attack surface is likely to be available through the actual device integrations which consume these core integrations to implement auto-discovery. In most cases, it’s relatively easy to enumerate which integrations are using these auto-discovery protocols by grepping for import statements. As an example, to find integrations that support auto-discovery using zeroconf, we can grep for `import zeroconf`:
  
  
  $ grep -r 'import zeroconf' 'homeassistant/components/'
  homeassistant/components/devolo_home_control/config_flow.py:from homeassistant.components import zeroconf
  ...
  homeassistant/components/lutron_caseta/config_flow.py:from homeassistant.components import zeroconf
  

This can help to narrow down the scope to popular devices where an integration may have a vulnerability in the way a potentially attacker-provided payload is used.

We also noted the [Bluetooth](https://www.home-assistant.io/integrations/bluetooth/) and [USB](https://www.home-assistant.io/integrations/usb/) integrations to have some interesting attack surface for an attacker with physical proximity to a Home Assistant installation.

We didn’t end up spending too much time hunting for bugs in the local attack surface exposed via auto-discovery, partly due to the attack surface provided by the web application being just as interesting while also having a higher likelihood of practical exploitability. Furthermore, the web application is still a viable attack surface via the local network anyway – a vulnerability in the web application may allow an attacker with a foothold in the local network to take control over the Home Assistant instance even if it isn’t exposed to the internet. Given our limited time, we hit two birds with one stone by focusing on this for both local and remote attacks, however, we still considered auto-discovery to be an important part of Home Assistant and think it would be a good target for further research.

### Remote Attack Surface

From the perspective of a (unauthenticated) remote attacker, the web application running on port 8123 may be the most accessible target when looking to pwn an internet-exposed Home Assistant instance. As we hinted at in the architecture section, it is possible for integrations to add HTTP endpoints and register WebSocket commands. Since both HTTP endpoints and WebSockets can be reached via the web application, each integration that does this slightly increases the attack surface area.

#### WebSockets

After briefly auditing the component responsible for handling setup and authentication of WebSockets, we found that all communications going through WebSockets require authentication. This meant that there would be no way to send custom commands through the WebSockets API as an unauthenticated user, which largely reduced the pre-auth attack surface. With that said, given the multitude of interesting functionalities provided through WebSocket commands, it could be a fruitful area for future research, especially when privilege separation is properly implemented and more widely used.

#### HTTP

There’s not much you can do through the web user interface without getting past the login form, but after a bit of digging, we found that there are a few intentionally unauthenticated endpoints which perform some interesting behaviour. This is made possible thanks to some configurable behaviour when registering HTTP APIs – in a way, it is possible to opt-out of authentication, which yields pre-auth attack surface! We discuss the HTTP integration in more detail below.

### Finding Interesting Integrations

Although we understood that integrations were a good place to start looking for bugs, with over a thousand integrations available, it wasn’t possible to go through each one manually. Fortunately, there are a few ways to identify interesting and widely-used integrations. For starters, an integration’s home page shows the number of installations (which have opted in to analytics) it’s being used by. The integrations [analytics page](https://analytics.home-assistant.io/integrations/) is even better as it ranks integrations by the number of Home Assistant instances they are installed on. These statistics could be used to quickly choose which integrations to spend more time on. This list isn’t comprehensive however and seems to lack a few built-in integrations.

There is also the concept of the [Integration Quality Scale](https://www.home-assistant.io/docs/quality_scale/) which assigns integrations a score based on its code quality and user experience. The most interesting to look out for are integrations marked as _internal_ , which are part of Home Assistant itself and most likely to be installed on instances by default. These can be filtered by looking through the `manifest.json` files within the [`core/homeassistant/components/`](https://github.com/home-assistant/core/tree/dev/homeassistant/components) subdirectories and filtering appropriately:
  
  
  $ cat homeassistant/components/*/manifest.json | jq 'select(.quality_scale == 'internal') | .name'
  'Air Quality'
  'Alarm Control Panel'
  ...
  'Zero-configuration networking (zeroconf)'
  'Zone'
  

There are around 150 internal quality integrations, including the HTTP integration which we’ve noted to be particularly interesting. The next section discusses this integration in detail.

## Case Study: HTTP Integration

A lot of our focus during this research project was on integrations exposing HTTP endpoints on the Home Assistant web application. The HTTP integration makes this all possible and is a very essential part of the application so we spent some time auditing it as well as some other interesting integrations which make use of it.

We weren’t able to find much documentation about how an integration developer can use the HTTP integration to register HTTP endpoints, so the next section aims to give a basic understanding of that process as it will help us to know what to look out for when auditing. We then take a deeper look at authentication and our process for hunting for bugs.

### How To Use the HTTP Integration as a Consumer

As code, integrations are Python modules which define a `setup` or `async_setup` function in the `__init__.py` file which is called upon initialisation. This function is passed a singleton [`HomeAssistant`](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/core.py#L276) object ([`hass`](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/bootstrap.py#L111)) as an argument which gives the integration access to anything it will need to do its job.

The HTTP integration provides a way for other integrations to easily add HTTP APIs to the server while automatically dealing with things such as authentication and CORS. It does this by defining a [`HomeAssistantHTTP`](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/__init__.py#L283) class which manages the HTTP server for Home Assistant. It gets instantiated and [set to the `hass.http` attribute](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/__init__.py#L214) when the HTTP integration is setup, making it accessible to any other integration. The web server itself is built on top of [aiohttp](https://docs.aiohttp.org/en/stable/web.html).

As an integration developer, exposing a HTTP API for your integration is as simple as writing a view class that inherits the base [`HomeAssistantView`](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/view.py#L35) class and calling the [`hass.http.register_view`](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/__init__.py#L349) method on it. The view class needs to set a few attributes and define some methods to specify what paths and HTTP methods it should handle. The `url` attribute specifies the path on the server that the handlers will be routed to. To specify the handler functions, you define class methods whose names corresponds to the HTTP method (e.g. `get` or `post`). The `requires_auth` attribute, which is set to `True` by default is also configurable to enable or disable the default access token authentication check. This can all be seen in the definition of the [`register`](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/view.py#L91-L114) method, which gets called when `register_view` is called.

As a basic, minimal [example](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/frontend/__init__.py#L329), we can take a look at the `frontend` integration which sets up an unauthenticated HTTP endpoint to return some static data:
  
  
  async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
  '''Set up the serving of the frontend.'''
  [...]
  hass.http.register_view(ManifestJSONView())
  
  [...]
  
  [...]
  
  class ManifestJSONView(HomeAssistantView):
  '''View to return a manifest.json.'''
  
  requires_auth = False
  url = '/manifest.json'
  name = 'manifestjson'
  
  @callback
  def get(self, request: web.Request) -> web.Response:
  '''Return the manifest.json.'''
  return web.Response(
  text=MANIFEST_JSON.json, content_type='application/manifest+json'
  )
  

The key things to take note of are the following:

  * The view class is defined as a subclass of the `HomeAssistantView` class
  * It is passed as an argument to the `hass.http.register_view` method within the integration’s setup method
  * The view class defines the attributes `requires_auth`, `url` and `name`
  * The view class defines the method `get` which contains the code that is run when this endpoint is requested

With this, we have a relatively simple way of identifying HTTP entrypoints.

### Authentication

As a major goal of our research was to find a pre-auth vulnerability, we naturally decided to audit how authentication is handled in the HTTP integration.

When the HomeAssistantHTTP server is [instantiated and initialised](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/__init__.py#L183-L198), the `async_setup_auth` method is [called](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/__init__.py#L340). This method is [defined](https://github.com/home-assistant/core/blob/ca576d45acf44530c1fe932518132f9650ad12ab/homeassistant/components/http/auth.py#L120) in the `homeassistant/components/http/auth.py` file and is responsible for [registering](https://github.com/home-assistant/core/blob/ca576d45acf44530c1fe932518132f9650ad12ab/homeassistant/components/http/auth.py#L238) middleware that will handle the authentication. We can see in the middleware method [`auth_middleware`](https://github.com/home-assistant/core/blob/ca576d45acf44530c1fe932518132f9650ad12ab/homeassistant/components/http/auth.py#L204-L236) itself how a request is authenticated:
  
  
  @middleware
  async def auth_middleware(
  request: Request, handler: Callable[[Request], Awaitable[StreamResponse]]
  ) -> StreamResponse:
  '''Authenticate as middleware.'''
  authenticated = False
  
  if hdrs.AUTHORIZATION in request.headers and await async_validate_auth_header(
  request
  ):
  authenticated = True
  auth_type = 'bearer token'
  
  # We first start with a string check to avoid parsing query params
  # for every request.
  elif (
  request.method == 'GET'
  and SIGN_QUERY_PARAM in request.query_string
  and await async_validate_signed_request(request)
  ):
  authenticated = True
  auth_type = 'signed request'
  
  if authenticated:
  _LOGGER.debug(
  'Authenticated %s for %s using %s',
  request.remote,
  request.path,
  auth_type,
  )
  
  request[KEY_AUTHENTICATED] = authenticated
  return await handler(request)
  

There are two ways to authenticate a request; via a token in the authorisation header, or via a signature in the request query parameters for GET requests. A request is marked as authenticated if the `request['ha_authenticated']` value is `True`. The [`async_validate_auth_header`](https://github.com/home-assistant/core/blob/ca576d45acf44530c1fe932518132f9650ad12ab/homeassistant/components/http/auth.py#L142) method is simple and defers most of the validation logic to the core auth module implemented within the [`homeassistant/auth`](https://github.com/home-assistant/core/tree/dev/homeassistant/auth) directory. We briefly audited this module but did not find any significant bugs.

Note that the auth middleware is responsible for setting the `request['ha_authenticated']` attribute, but for authentication to be enforced, this value needs to be used somewhere. For HTTP views registered through the `hass.http.register_view` method, this is done within the [`request_handler_factory`](https://github.com/home-assistant/core/blob/739963b5ee1a49039eb19a1831bb569dab255fcc/homeassistant/components/http/view.py#L117-L176) function:
  
  
  def request_handler_factory(
  view: HomeAssistantView, handler: Callable
  ) -> Callable[[web.Request], Awaitable[web.StreamResponse]]:
  '''Wrap the handler classes.'''
  assert asyncio.iscoroutinefunction(handler) or is_callback(
  handler
  ), 'Handler should be a coroutine or a callback.'
  
  async def handle(request: web.Request) -> web.StreamResponse:
  '''Handle incoming request.'''
  if request.app[KEY_HASS].is_stopping:
  return web.Response(status=HTTPStatus.SERVICE_UNAVAILABLE)
  
  authenticated = request.get(KEY_AUTHENTICATED, False)
  
  if view.requires_auth and not authenticated:
  raise HTTPUnauthorized()
  
  [...]
  
  return handle
  

If the view’s `requires_auth` attribute is `True` and the `request['ha_authenticated']` is not, then the handler raises an error. The `requires_auth` attribute is [set to `True` by default](https://github.com/home-assistant/core/blob/da05763a5c1d2dc0a3eae532f17087afdbdf183a/homeassistant/components/http/view.py#L41) in the base `HomeAssistantView` class, but can be overwritten to disable automatic authentication checks.

This means that `grep --exclude-dir tests -r 'requires_auth = False'` is an easy and reliable grep for identifying potential pre-auth attack surface.

#### Hunting For Bugs

Although our brief review of the core auth module did not reveal any significant bugs, we did identify a bug in the signed request validation method while looking at the HTTP integration’s auth middleware. The bug would allow an attacker to tamper with a request’s query parameters to reuse a valid signature to authenticate a request under a different set of query parameters. If request signing was used for sensitive endpoints where things like filenames or IDs are used in the query parameters, this could be used to potentially gain unauthorised access to a resource. However, we only found [one usage](https://github.com/search?q=repo%3Ahome-assistant/core%20async_sign_path&type=code) of signed requests being used in the Core integrations, so the impact here was minimal. We reported this to the HA devs and it was promptly [patched](https://github.com/home-assistant/core/pull/90148). We’ve published an advisory for this bug [here](https://github.com/elttam/publications/blob/master/writeups/home-assistant/signed-url-param-tampering-advisory.md).

A large part of our focus was on higher level authentication bugs within consumers of the HTTP integration using the opt-out authentication as a starting point. There weren’t many HTTP views which set the `requires_auth` attribute to `False`, so it was reasonable to look through each one. In most cases, the default authentication check is opted out of because the endpoint is intended to be a static, public resource, or the integration handles authentication in its own way. As a simple example, the Telegram bot integration has a [webhook endpoint](https://github.com/home-assistant/core/blob/74e0341d83125d1b7dd2dca6c0fc1eae66a4bd20/homeassistant/components/telegram_bot/webhooks.py#L104-L134) which disables the default authentication check. It does perform some authentication in its own way though, in this case, based on the requester’s IP address:
  
  
  class PushBotView(HomeAssistantView):
  '''View for handling webhook calls from Telegram.'''
  
  requires_auth = False
  url = TELEGRAM_WEBHOOK_URL
  name = 'telegram_webhooks'
  
  def __init__(self, hass, bot, dispatcher, trusted_networks):
  '''Initialize by storing stuff needed for setting up our webhook endpoint.'''
  self.hass = hass
  self.bot = bot
  self.dispatcher = dispatcher
  self.trusted_networks = trusted_networks
  
  async def post(self, request):
  '''Accept the POST from telegram.'''
  real_ip = ip_address(request.remote)
  if not any(real_ip in net for net in self.trusted_networks):
  _LOGGER.warning('Access denied from %s', real_ip)
  return self.json_message('Access denied', HTTPStatus.UNAUTHORIZED)
  
  try:
  update_data = await request.json()
  except ValueError:
  return self.json_message('Invalid JSON', HTTPStatus.BAD_REQUEST)
  
  update = Update.de_json(update_data, self.bot)
  _LOGGER.debug('Received Update on %s: %s', self.url, update)
  await self.hass.async_add_executor_job(self.dispatcher.process_update, update)
  
  return None
  

The reason why this is interesting is because it means we have some fresh attack surface to look at. Integrations which perform authentication in their own way might do so poorly, which could lead to an authentication bypass…

When looking through said integrations, we noticed one particularly interesting one: the [Home Assistant Supervisor integration](https://www.home-assistant.io/integrations/hassio/). This integration’s purpose is to allow Home Assistant Core (and hence the web application user interface) to interact with the Supervisor. It does this by proxying requests from the user to the Supervisor’s HTTP API. Given the context of the Supervisor’s role within the Home Assistant architecture, we understood this to be a very critical security boundary in which a bug could lead to severe outcomes. Auditing this integration resulted in [CVE-2023-27482](https://github.com/home-assistant/core/security/advisories/GHSA-2j8f-h4mr-qr25), a pre-authentication RCE vulnerability which we will talk about shortly.

### Incorporating Dynamic Testing

Although code review was the primary driver for the unauthenticated bugs mentioned, dynamic testing played an important part in debugging and identifying further areas that may increase the attack surface. Following the [`debugpy`](https://www.home-assistant.io/integrations/debugpy/) documentation, we were able to successfully set breakpoints and follow code in both Core and Supervisor.

When debugging the applications, we then visited the local instance with a HTTP interception proxy and began navigating through the different pages, settings and features. By exploring the application top-to-bottom and interacting with everything we could see, we were then able to sift through the HTTP history to identify interesting API calls, the data being sent through WebSockets and gain a clearer understanding of some of the data structures that may be passing through the code.

Thinking about common web vulnerability classes, we looked for key functionality that is often prone to bugs such as configuration saving, linking external services, uploading files, parsing of files or data (such as XML), and of course database lookups. When an interesting API request was identified, we then identify the code responsible for handling the request.

For example, a POST request to the path `/api/media_source/local_source/upload` can be located in the code base by grepping for `media_source/local_source`:
  
  
  $ grep -ir 'media_source/local_source' --exclude-dir tests/
  core/homeassistant/components/media_source/local_source.py:  url = '/api/media_source/local_source/upload'
  core/homeassistant/components/media_source/local_source.py:  vol.Required('type'): 'media_source/local_source/remove',
  frontend/src/data/media_source.ts:  '/api/media_source/local_source/upload',
  frontend/src/data/media_source.ts:  type: 'media_source/local_source/remove',
  

We can see that the functionality is handled in `core/homeassistant/components/media_source/local_source.py` inside the [`UploadMediaView`](https://github.com/home-assistant/core/blob/ca1a12898cbf4f8218351d1d98c7ac44d34ced8e/homeassistant/components/media_source/local_source.py#L237) function. By setting a breakpoint on the `post` function, we were then able to step through and even re-run some of the method calls with different inputs to see if they may be vulnerable, such as the `MediaSourceItem.from_uri(self.hass, data['media_content_id'], None)` call to determine the parsed `media_content_id` URI. From our time following this approach, we identified a path traversal vulnerability in the `media_source` upload functionality which we’ve published an advisory for [here](https://github.com/elttam/publications/blob/master/writeups/home-assistant/media-source-arbitrary-file-write-advisory.md).

## CVE-2023-27482: Authentication Bypass in Home Assistant

The most significant vulnerability from our time researching Home Assistant was a critical authentication bypass, tracked as [CVE-2023-27482](https://github.com/home-assistant/core/security/advisories/GHSA-2j8f-h4mr-qr25). elttam’s full advisory detailing the vulnerabilities and Proof-of-Concept can be found [here](https://github.com/elttam/publications/blob/master/writeups/home-assistant/supervisor-authentication-bypass-advisory.md).

The finding resided in the Supervisor integration which allowed for a remote unauthenticated attacker to achieve Remote Code Execution (RCE) on the target Home Assistant instance, and consequently, full access to control all smart home devices, stored data and credentials, and also internal access to the home network.

Reporting the initial vulnerability was relatively straight forward. However, the patching process wasn’t overly smooth and could be improved in future for both the remediation workflow and security advisory details to help ensure users are provided adequate information to understand the severity and applicability of a given vulnerability.

Initially, various minor [fixes](https://github.com/home-assistant/core/pull/88921/files) were made to the code base and merged into regular commits between versions, on top of this, the disclosure by Home Assistant was published over a week after two versions had been pushed to the repository with very little information suggesting the commits had anything to do with a security vulnerability. We discovered various workarounds to the mitigations that were put in place which included techniques such as inserting tabs or other special characters into the URL that were ignored by the handler. Home Assistant developers were quick to push out further [fixes](https://github.com/home-assistant/supervisor/commit/2ae2d0e1070067b2b47bdfecfb44eca697b964fd) to the workarounds, however no further updates to the advisory were made and the fixes were once again merged quietly into day-to-day commits and version releases.

A few days before we commenced the blog, we also identified another entry point within the `/api/hassio_ingress` endpoint on the Supervisor integration, although the Home Assistant Core fixes introduced in 2023.3.2 prevented the exploitation of the issue, the universal updates released in the Supervisor code base aimed at protecting older versions of core were not sufficient and exposed the platform once again. It wasn’t until Home Assistant Core version 2023.3.2 and Supervisor [2023.03.3](https://github.com/home-assistant/supervisor/commit/cede47e95c1349831b52ad354cdaf915ce18bca6) that our workarounds were no longer exploitable despite the advisories still referencing versions 2023.3.0 (core) and 2023.03.1 (Supervisor).

Further to this, the Home Assistant [forums](https://community.home-assistant.io/t/disclosure-supervisor-security-vulnerability/544977) and sites such as [ycombinator](https://news.ycombinator.com/item?id=35075961) and [reddit](https://www.reddit.com/r/homeassistant/comments/11lrqbo/disclosure_supervisor_security_vulnerability/) were home to [many [1]](https://community.home-assistant.io/t/disclosure-supervisor-security-vulnerability/544977/33) [comments [2]](https://community.home-assistant.io/t/disclosure-supervisor-security-vulnerability/544977/85) showing that the potential full impact of the vulnerability was not clear. This vulnerability also affected [Home Assistant Cloud](https://www.nabucasa.com), a partner service offered by Nabu Casa, which was not explicitly mentioned in the announcement – [some [1]](https://community.home-assistant.io/t/disclosure-supervisor-security-vulnerability/544977/34) [comments [2]](https://community.home-assistant.io/t/disclosure-supervisor-security-vulnerability/544977/13) indicated that users were unsure if they were affected or not. Fortunately, this did spark some useful [discussions](https://community.home-assistant.io/t/disclosure-supervisor-security-vulnerability/544977/127) regarding assumptions about the (lack of) security provided by random hostnames and even potential risks involved when using the Nabu Casa service.

Ultimately, the vulnerability is exploitable as long as the Home Assistant instance runs the Supervisor component with the Supervisor integration and is reachable via the internet or through local network access – random hostnames or TLS do not provide any form of protection in this case. The simplest way to avoid being at risk from a remote attacker is to not expose the instance to the internet. We encourage users to consider VPN services like [Tailscale](https://tailscale.com/) which make remote access simple and secure.

### Timeline

A timeline of the disclosure process was as follows:

  * **17/02/2023** \- We begin researching the Home Assistant Supervisor Integration and discover the vulnerability
  * **20/02/2023** \- Vulnerability report sent to security@home-assistant.io
  * **27/02/2023** \- Follow up email sent to confirm receipt of report
  * **28/02/2023** \- Confirmation of receipt from Home Assistant
  * **01/03/2023** \- Home Assistant replies detailing plans to release hardening fixes, request a CVE and publish a blog post
  * **01/03/2023** \- CVE-2023-27482 reserved
  * **01/03/2023** \- Home Assistant 2023.3.0 is released, containing [hardening](https://github.com/home-assistant/core/pull/88921/files) in the HTTP integration security filters middleware
  * **08/03/2023** \- Home Assistant Supervisor 2023.03.1 is released, containing [hardening](https://github.com/home-assistant/supervisor/commit/2ae2d0e1070067b2b47bdfecfb44eca697b964fd) in the security middleware
  * **09/03/2023** \- Home Assistant 2023.3.2 is released, containing further fixes in the Supervisor integration
  * **09/03/2023** \- Home Assistant publishes blog post and [advisory](https://github.com/home-assistant/core/security/advisories/GHSA-2j8f-h4mr-qr25)
  * **21/03/2023** \- Bypass affecting Home Assistant Core <=2023.3.1 discovered and reported to vendor
  * **21/03/2023** \- Confirmation of receipt from Home Assistant
  * **22/03/2023** \- Home Assistant Supervisor 2023.03.2 is released, containing [mitigation](https://github.com/home-assistant/supervisor/commit/2ae2d0e1070067b2b47bdfecfb44eca697b964fd) against the bypass
  * **26/03/2023** \- Bypass affecting Home Assistant Core <=2023.3.1 and Supervisor <=2023.03.2 discovered
  * **27/03/2023** \- Bypass reported to vendor
  * **28/03/2023** \- Confirmation of receipt from Home Assistant
  * **29/03/2023** \- Home Assistant Supervisor 2023.03.3 is released, containing [mitigation](https://github.com/home-assistant/supervisor/commit/cede47e95c1349831b52ad354cdaf915ce18bca6) against the bypass
  * **03/05/2023** \- Draft blog post shared with Home Assistant
  * **04/05/2023** \- Feedback on blog post received from Home Assistant
  * **04/05/2023** \- [Advisory](https://github.com/home-assistant/core/security/advisories/GHSA-2j8f-h4mr-qr25) updated to reflect correct versions
  * **10/05/2023** \- Public release of elttam advisories and blog post

## Conclusion

This post covered our team’s journey on hacking away at Home Assistant. We hope that we were able to provide some insights about how we approached finding high severity vulnerabilities in a large project through mostly manual code review guided by an analysis of the attack surface. We were only able to cover so much ground in the time we had and there are a lot of interesting features and attack surfaces we might not have thought about. We would love to see further security research into Home Assistant especially as the project and smart homes in general continue to grow in popularity.

Our advisories for the vulnerabilities we reported to Home Assistant during this research project can be found [here](https://github.com/elttam/publications).

Thanks for reading!

[Exploiting Auth0 Defaults in XSS Attacks](/blog/exploiting-auth0-defaults-in-xss-attacks)

[Jupyter Enterprise Gateway](/blog/jupyter-enterprise-gateway)

[Golang code review notes II](/blog/golang-code-review-notes-ii)

[ORM Leaking More Than You Joined For](/blog/leaking-more-than-you-joined-for)

[Gotchas in Email Parsing - Lessons From Jakarta Mail](/blog/jakarta-mail-primitives)

[New Method to Leverage Unsafe Reflection and Deserialisation to RCE on Rails](/blog/rails-sqlite-gadget-rce)

[A Monocle on Chronicles](/blog/monocle-on-chronicles)

[DUCTF 2024 ESPecially Secure Boot Writeup](/blog/ductf24-especially-secure-boot)

[plORMbing your Prisma ORM with Time-based Attacks](/blog/plorming-your-primsa-orm)

[plORMbing your Django ORM](/blog/plormbing-your-django-orm)

[Keeping up with the Pwnses](/blog/talkback-intro)

[Exploring the STSAFE-A110](/blog/stsafe-a110)

[RE of LR3](/blog/re-of-lr3)

[Abusing Amazon VPC CNI plugin for Kubernetes](/blog/amazon-vpc-cni)

[PwnAssistant - Controlling /home's via a Home Assistant RCE](/blog/pwnassistant)

[Cracking the Odd Case of Randomness in Java](/blog/cracking-randomness-in-java)

[Golang code review notes](/blog/golang-codereview)

[ESP-IDF setup guide](/blog/esp-idf-setup-guide)

[Tuya IoT and EZ Mode Pairing](/blog/ez-mode-pairing)

[Attacks on GCM with Repeated Nonces](/blog/key-recovery-attacks-on-gcm)

[Simple Bugs With Complex Exploits](/blog/simple-bugs-with-complex-exploits)

[Lua SUID Shells](/blog/lua-suid-shells)

[Hacking with Environment Variables](/blog/env)

[Are you winning if you're pinning?](/blog/certpinning)

[Ruby 2.x Universal RCE Deserialization Gadget Chain](/blog/ruby-deserialization)

[Fuze Multi-Card Technology Security Review](/blog/fuzereview)

[Remote LD_PRELOAD Exploitation](/blog/goahead)

[Building Hardened Docker Images from Scratch with Kubler](/blog/kubler)

[Intro to SDR and RF Signal Analysis](/blog/intro-sdr-and-rf-analysis)

[Playing with canaries](/blog/playing-with-canaries)

[EFF secure messaging scorecard review](/blog/a-review-of-the-eff-secure-messaging-scorecard-pt2)

[Vuln research on the WAG54G home router](/blog/vuln-research-on-the-wag54g-home-router)

[A review of the EFF secure messaging scorecard...](/blog/a-review-of-the-eff-secure-messaging-scorecard-pt1)

[Gaining console access to the WAG54G home router](/blog/gaining-console-access-to-the-wag54g-home-router)

[Why I recommend Chrome to family...](/blog/why-i-recommend-chrome)

[hello@elttam.com](mailto:hello@elttam.com)

Key: [87169502a105dcb5](https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7dd2580f50ab3231873fefa887169502a105dcb5)

Suite 343  
3 Albert Coates Ln  
Melbourne, VIC, 3000

[What We Do](/what-we-do)

[Blog](/resources)

[How We Work](/how-we-work)

[About Us](/about-us)

© {{year}} elttam Security Pty Ltd. ABN 54 684 907 702

[](https://bsky.app/profile/elttam.bsky.social)

[](https://x.com/elttam)

[](https://www.linkedin.com/company/elttam/)

[](https://github.com/elttam)

[](/blog/rss.xml)
