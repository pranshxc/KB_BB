---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1353244'
original_report_id: '1353244'
title: '[samokat.ru] PHP modules path disclosure due to lack of error handling'
weakness: Information Exposure Through Debug Information
team_handle: mailru
created_at: '2021-09-28T07:52:19.641Z'
disclosed_at: '2021-11-03T15:34:14.124Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: Samokat
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-exposure-through-debug-information
---

# [samokat.ru] PHP modules path disclosure due to lack of error handling

## Metadata

- HackerOne Report ID: 1353244
- Weakness: Information Exposure Through Debug Information
- Program: mailru
- Disclosed At: 2021-11-03T15:34:14.124Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi security team @mailru we found a Information disclosure in php_project in [sub]samokat.ru
On one side of the server [samokat.ru] generates a full stack error trace instead of an HTTP 500 error. The complete error stack trace reveals the full path of the PHP_Configuration module directory on the integration server.

**System Hosts:**
https://quality.samokat.ru/php.ini

**Proof of Vulnerability :**
  * Opened directory is https://quality.samokat.ru/info.php
  * You will see this respond as ``File not found.`` 
  * Repeat url directory and sent request to "Turbo-Intruder"
  * Set as payloads ``/§fuzz§ HTTP/2`` and sent request
  * You can see a directory sensitive in responsive header as ``/php.ini/``

**Request**
```
GET /§Fuzz§ HTTP/2
Host: quality.samokat.ru
Upgrade-Insecure-Requests: 1
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Connection: close
```
**Responsive Vulnerable**
```javascript
HTTP/2 500 Internal Server Error
Date: Tue, 28 Sep 2021 07:49:15 GMT
Content-Type: text/html; charset=UTF-8
Cache-Control: no-cache, private
Cf-Cache-Status: DYNAMIC
Expect-Ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
Cf-Ray: 695b5fbd09a84a1d-SIN


#	CALLED CODE	DOCUMENT	LINE
44	Doctrine\DBAL\Driver\PDOConnection->__construct(…)	~/vendor/laravel/framework/src/Illuminate/Database/Connectors/Connector.php	64
43	Illuminate\Database\Connectors\Connector->createPdoConnection(…)	~/vendor/laravel/framework/src/Illuminate/Database/Connectors/Connector.php	97
42	Illuminate\Database\Connectors\Connector->tryAgainIfCausedByLostConnection(…)	~/vendor/laravel/framework/src/Illuminate/Database/Connectors/Connector.php	47
41	Illuminate\Database\Connectors\Connector->createConnection(…)	~/vendor/laravel/framework/src/Illuminate/Database/Connectors/PostgresConnector.php	33
40	Illuminate\Database\Connectors\PostgresConnector->connect(…)	~/vendor/october/rain/src/Database/Connectors/ConnectionFactory.php	29
39	October\Rain\Database\Connectors\ConnectionFactory->October\Rain\Database\Connectors\{closure}()		
38	call_user_func(…)	~/vendor/laravel/framework/src/Illuminate/Database/Connection.php	915
37	Illuminate\Database\Connection->getPdo()	~/vendor/laravel/framework/src/Illuminate/Database/DatabaseManager.php	248
36	Illuminate\Database\DatabaseManager->refreshPdoConnections(…)	~/vendor/laravel/framework/src/Illuminate/Database/DatabaseManager.php	234
35	Illuminate\Database\DatabaseManager->reconnect(…)	~/vendor/laravel/framework/src/Illuminate/Database/DatabaseManager.php	168
34	Illuminate\Database\DatabaseManager->Illuminate\Database\{closure}(…)		
33	call_user_func(…)	~/vendor/laravel/framework/src/Illuminate/Database/Connection.php	753
32	Illuminate\Database\Connection->reconnect()	~/vendor/laravel/framework/src/Illuminate/Database/Connection.php	767
31	Illuminate\Database\Connection->reconnectIfMissingConnection()	~/vendor/laravel/framework/src/Illuminate/Database/Connection.php	616
30	Illuminate\Database\Connection->run(…)	~/vendor/laravel/framework/src/Illuminate/Database/Connection.php	333
29	Illuminate\Database\Connection->select(…)	~/vendor/laravel/framework/src/Illuminate/Database/Query/Builder.php	1719
28	Illuminate\Database\Query\Builder->runSelect()	~/vendor/laravel/framework/src/Illuminate/Database/Query/Builder.php	1704
27	Illuminate\Database\Query\Builder->get(…)	~/vendor/october/rain/src/Database/QueryBuilder.php	217
26	October\Rain\Database\QueryBuilder->October\Rain\Database\{closure}()	~/vendor/laravel/framework/src/Illuminate/Cache/Repository.php	323
25	Illuminate\Cache\Repository->remember(…)	~/vendor/laravel/framework/src/Illuminate/Cache/CacheManager.php	304
24	Illuminate\Cache\CacheManager->__call(…)	~/vendor/october/rain/src/Database/QueryBuilder.php	158
23	October\Rain\Database\QueryBuilder->getCached(…)	~/vendor/october/rain/src/Database/QueryBuilder.php	121
22	October\Rain\Database\QueryBuilder->getDuplicateCached(…)	~/vendor/october/rain/src/Database/QueryBuilder.php	92
21	October\Rain\Database\QueryBuilder->get(…)	~/vendor/laravel/framework/src/Illuminate/Database/Eloquent/Builder.php	481
20	Illuminate\Database\Eloquent\Builder->getModels(…)	~/vendor/laravel/framework/src/Illuminate/Database/Eloquent/Builder.php	465
19	Illuminate\Database\Eloquent\Builder->get(…)	~/vendor/laravel/framework/src/Illuminate/Database/Concerns/BuildsQueries.php	77
18	Illuminate\Database\Eloquent\Builder->first()	~/modules/system/behaviors/SettingsModel.php	114
17	System\Behaviors\SettingsModel->getSettingsRecord()	~/modules/system/behaviors/SettingsModel.php	76
16	System\Behaviors\SettingsModel->instance()	~/modules/system/behaviors/SettingsModel.php	135
15	System\Behaviors\SettingsModel->get(…)		
14	call_user_func_array(…)	~/vendor/october/rain/src/Extension/ExtendableTrait.php	414
13	October\Rain\Database\Model->extendableCall(…)	~/vendor/october/rain/src/Database/Model.php	647
12	October\Rain\Database\Model->__call(…)	~/vendor/laravel/framework/src/Illuminate/Database/Eloquent/Model.php	1489
11	Illuminate\Database\Eloquent\Model::__callStatic(…)	~/modules/system/models/EventLog.php	37
10	System\Models\EventLog::useLogging()	~/modules/system/ServiceProvider.php	286
9	System\ServiceProvider->System\{closure}(…)		
8	call_user_func_array(…)	~/vendor/october/rain/src/Events/Dispatcher.php	233
7	October\Rain\Events\Dispatcher->dispatch(…)	~/vendor/laravel/framework/src/Illuminate/Log/Writer.php	295
6	Illuminate\Log\Writer->fireLogEvent(…)	~/vendor/laravel/framework/src/Illuminate/Log/Writer.php	201
5	Illuminate\Log\Writer->writeLog(…)	~/vendor/laravel/framework/src/Illuminate/Log/Writer.php	114
4	Illuminate\Log\Writer->error(…)	~/vendor/laravel/framework/src/Illuminate/Support/Facades/Facade.php	221
3	Illuminate\Support\Facades\Facade::__callStatic(…)	~/vendor/october/rain/src/Foundation/Exception/Handler.php	66
2	October\Rain\Foundation\Exception\Handler->report(…)	~/vendor/laravel/framework/src/Illuminate/Foundation/Bootstrap/HandleExceptions.php	81
1	Illuminate\Foundation\Bootstrap\HandleExceptions->handleException(…)		
```
**Proof On Concept:**
F1463843
F1463837

## Impact

Sensitive Information disclosure PHP_Project manager in samokat.ru

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
