---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116764'
original_report_id: '116764'
title: vk.com/login.php
weakness: SQL Injection
team_handle: vkcom
created_at: '2016-02-16T18:48:49.137Z'
disclosed_at: '2016-12-29T19:40:37.591Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- sql-injection
---

# vk.com/login.php

## Metadata

- HackerOne Report ID: 116764
- Weakness: SQL Injection
- Program: vkcom
- Disclosed At: 2016-12-29T19:40:37.591Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Выполнив 3 простейших шага, и  Вы столкнётесь с отказом сервера что-либо делать. 

Шаг 1: Перейти по адресу vk.com/login.php 
Шаг 2: Ввести в поле "логин" символы ( 00 или 000 или 0000,  и так до 17 нулей), пароль указать любой. 
Шаг 3: Нажать логин и сервер будет сильно недоволен. 

Спасибо,  и исправьте свой Drupal )))

By vk.com/black.hat.hacker ( Николай Пиколаев)

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
