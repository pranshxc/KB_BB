---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '292797'
original_report_id: '292797'
title: ActionController::Parameters .each returns an unsafe hash
team_handle: rails
created_at: '2017-11-24T15:05:52.002Z'
disclosed_at: '2020-05-18T20:15:57.565Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# ActionController::Parameters .each returns an unsafe hash

## Metadata

- HackerOne Report ID: 292797
- Weakness: 
- Program: rails
- Disclosed At: 2020-05-18T20:15:57.565Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Rails 5.1.4

The goal of `ActionController::Parameters`'s `permit` method (strong parameters) is to prevent accidental trust in the parameters sent by the client. We can therefore not simply create a hash of all the parameters in the params without permitting them first. When we really want to do this there is the method `to_unsafe_h`, indicating the importance of controlling when an unsafe hash is returned. However, when we use `.each` on our parameters object, an unsafe hash is returned that includes all the keys and their values in a new hash:

```ruby
params = ActionController::Parameters.new(city: 'Nijmegen', country: 'Netherlands', language: 'Dutch')

params.to_h

# ActionController::UnfilteredParameters: unable to convert unpermitted parameters to hash
# from ...lib/ruby/gems/2.4.0/gems/actionpack-5.1.4/lib/action_controller/metal/strong_parameters.rb:265:in `to_h'

params.permit(:city)
=> <ActionController::Parameters {"city"=>"Nijmegen"} permitted: true>

params.permit(:city).to_h
=> {"city"=>"Nijmegen"}

params.to_unsafe_h
=> {"city"=>"Nijmegen", "country"=>"Netherlands", "language"=>"Dutch"}

params.each {}
=> {"city"=>"Nijmegen", "country"=>"Netherlands", "language"=>"Dutch"}
```

This behaviour is extra strange when contraste with how `select` works:

```ruby
params.select { true }
=> <ActionController::Parameters {"city"=>"Nijmegen", "country"=>"Netherlands", "language"=>"Dutch"} permitted: false>
```

Here you can see that select returns an instance of `ActionController::Parameters` that has `permitted: false`

## Impact

An attacker could find out about the accidental use of each in working with parameters in a controller and use this knowledge to send additional (more than provided in a form) parameters along and in this way circumvent authorisation checks.

```ruby
# controller:

def update
  # Attacker has included the parameter: `{ is_admin: true }`
  User.update(clean_up_params)
end

def clean_up_params
  
   params.each { |k, v|  SomeModel.check(v) if k == :name }
end
```

The example (admittedly simplified) above shows a possible scenario where a developer builds a method to do something with each param in a seperate method after which he might expect his parameters to adhere to normal working `permitted: true/false`. Slightly unexpected behaviour that could cause security issues.

Biggest threat would seem to be to opensource projects where attackers can survey the project's code.

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
