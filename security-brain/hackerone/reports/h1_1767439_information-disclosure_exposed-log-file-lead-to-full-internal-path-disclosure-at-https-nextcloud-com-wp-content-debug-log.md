---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1767439'
original_report_id: '1767439'
title: Exposed Log File Lead to Full Internal path disclosure at [https://nextcloud.com/wp-content/debug.log]
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2022-11-08T20:05:07.478Z'
disclosed_at: '2022-12-15T22:22:38.776Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
asset_identifier: nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Exposed Log File Lead to Full Internal path disclosure at [https://nextcloud.com/wp-content/debug.log]

## Metadata

- HackerOne Report ID: 1767439
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2022-12-15T22:22:38.776Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi team ,
i found wp-content/debug.log endpoint public accessible That lead to full path disclosure 

Steps : 
Open : https://nextcloud.com/wp-content/debug.log

You can See Internal paths disclosed and date is  : 02-Nov-2022 

```
[02-Nov-2022 08:50:36 UTC] PHP Fatal error:  Uncaught Error: Call to undefined method WP_Textdomain_Registry::reset() in █████████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php:139
Stack trace:
#0 ███████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(119): WPML\ST\MO\Hooks\LanguageSwitch->resetTranslationAvailabilityInformation()
#1 ███plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(73): WPML\ST\MO\Hooks\LanguageSwitch->changeMoObjects()
#2 ███plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(48): WPML\ST\MO\Hooks\LanguageSwitch->switchToLocale()
#3 ██████class-wp-hook.php(310): WPML\ST\MO\Hooks\LanguageSwitch->languageHasSwitched()
#4 ██████████class-wp-hook.php(332): WP_Hook->apply_filters()
#5 ██████plugin.php(517): WP_Hook->do_action()
#6 █████████plugins/sitepress-multilingual-cms/sitepress.class.php(1178): do_action()
#7  in █████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php on line 139
[02-Nov-2022 08:50:36 UTC] PHP Fatal error:  Uncaught Error: Call to undefined method WP_Textdomain_Registry::reset() in █████████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php:139
Stack trace:
#0 ████████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(119): WPML\ST\MO\Hooks\LanguageSwitch->resetTranslationAvailabilityInformation()
#1 ██████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(73): WPML\ST\MO\Hooks\LanguageSwitch->changeMoObjects()
#2 ██████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(48): WPML\ST\MO\Hooks\LanguageSwitch->switchToLocale()
#3 ██████████class-wp-hook.php(310): WPML\ST\MO\Hooks\LanguageSwitch->languageHasSwitched()
#4 █████████class-wp-hook.php(332): WP_Hook->apply_filters()
#5 ███████plugin.php(517): WP_Hook->do_action()
#6 ████████plugins/sitepress-multilingual-cms/sitepress.class.php(1178): do_action()
#7  in ███plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php on line 139
[02-Nov-2022 08:50:36 UTC] PHP Fatal error:  Uncaught Error: Call to undefined method WP_Textdomain_Registry::reset() in ██████████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php:139
Stack trace:
#0 ████████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(119): WPML\ST\MO\Hooks\LanguageSwitch->resetTranslationAvailabilityInformation()
#1 ████████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(73): WPML\ST\MO\Hooks\LanguageSwitch->changeMoObjects()
#2 ██████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php(48): WPML\ST\MO\Hooks\LanguageSwitch->switchToLocale()
#3 ████class-wp-hook.php(310): WPML\ST\MO\Hooks\LanguageSwitch->languageHasSwitched()
#4 ████████class-wp-hook.php(332): WP_Hook->apply_filters()
#5 ███████plugin.php(517): WP_Hook->do_action()
#6 ████plugins/sitepress-multilingual-cms/sitepress.class.php(1178): do_action()
#7  in ████████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php on line 139
[02-Nov-2022 08:50:36 UTC] PHP Fatal error:  Uncaught Error: Call to undefined method WP_Textdomain_Registry::reset() in █████plugins/wpml-string-translation/classes/MO/Hooks/LanguageSwitch.php:139
Stack trace:
```

## Impact

Exposed Log file lead to exposed all internal paths

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
