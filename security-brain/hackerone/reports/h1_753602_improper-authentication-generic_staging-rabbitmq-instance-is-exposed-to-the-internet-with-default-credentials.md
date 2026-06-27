---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '753602'
original_report_id: '753602'
title: Staging Rabbitmq instance is exposed to the internet with default credentials
weakness: Improper Authentication - Generic
team_handle: unikrn
created_at: '2019-12-07T11:46:41.492Z'
disclosed_at: '2019-12-09T06:46:47.374Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 101
asset_identifier: unikrn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Staging Rabbitmq instance is exposed to the internet with default credentials

## Metadata

- HackerOne Report ID: 753602
- Weakness: Improper Authentication - Generic
- Program: unikrn
- Disclosed At: 2019-12-09T06:46:47.374Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:** 
RabbitMQ is an open-source message-broker software (sometimes called message-oriented middleware) that originally implemented the Advanced Message Queuing Protocol (AMQP) and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol (STOMP), Message Queuing Telemetry Transport (MQTT), and other protocols.

The instance of the rabbitmq of unikrn is exposed to the internet with the default credentials guest:guest which has an administrative access.

## Steps To Reproduce:
1. Visit ███████
2. Enter user as guest & password as guest.
3. Boom!! You are inside the management console of the rabbitmq of unikrn.

P.S I checked that the ssl certificates belong to domain *.dev.unikrn.space which proves that the instance belongs to unikrn and maybe used for production or development.

##Mitigation
Don't expose the rabbitmq console on the internet & remove the default credentials.

## Supporting Material/References:
Here is a screenshot of the list of queue
███

## Impact

The impact is critical as the attacker can get hell lot of details by dumping the queues as the queues are having confidential details like sso details & api details for different assets. Also the default credential has the administrative access which can help the attacker to add a new queue, modify or delete an existing queue etc.

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
