---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '495382'
original_report_id: '495382'
title: No SearchEngine sanatizing can lead to command injection
weakness: Command Injection - Generic
team_handle: notepad-plus-plus
created_at: '2019-02-13T16:43:45.535Z'
disclosed_at: '2019-06-06T00:47:37.060Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 98
tags:
- hackerone
- command-injection-generic
---

# No SearchEngine sanatizing can lead to command injection

## Metadata

- HackerOne Report ID: 495382
- Weakness: Command Injection - Generic
- Program: notepad-plus-plus
- Disclosed At: 2019-06-06T00:47:37.060Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Information:
**Summary:** 
Notepad++ is vulnerable to a command injection vulnerability.

**Debug Info:**
Notepad++ v7.6.3 (32-bit)
Build time : Jan 27 2019 - 17:20:30
Path : C:\Program Files (x86)\Notepad++\notepad++.exe
Admin mode : ON
Local Conf mode : OFF
OS : Windows 10 (64-bit)
Plugins : none

**Description:**

When launching the web browser with the defined `SearchEngine`, the specified URL is directly passed as a command to `ShellExecute`. However since there is no check, one can put commands in that field instead of URLs.

Relevant piece of code in `NppCommands.cpp`:
```
case IDM_EDIT_SEARCHONINTERNET:
		{
			if (_pEditView->execute(SCI_GETSELECTIONS) != 1) // Multi-Selection || Column mode || no selection
				return;

			const NppGUI & nppGui = (NppParameters::getInstance())->getNppGUI();
			generic_string url;
			if (nppGui._searchEngineChoice == nppGui.se_custom)
			{
				if (nppGui._searchEngineCustom.empty())
				{
					url = TEXT("https://www.google.com/search?q=$(CURRENT_WORD)");
				}
				else
				{
					url = nppGui._searchEngineCustom.c_str();
				}
			}
			else if (nppGui._searchEngineChoice == nppGui.se_duckDuckGo)
			{
				url = TEXT("https://duckduckgo.com/?q=$(CURRENT_WORD)");
			}
			else if (nppGui._searchEngineChoice == nppGui.se_google)
			{
				url = TEXT("https://www.google.com/search?q=$(CURRENT_WORD)");
			}
			else if (nppGui._searchEngineChoice == nppGui.se_bing)
			{
				url = TEXT("https://www.bing.com/search?q=$(CURRENT_WORD)");
			}
			else if (nppGui._searchEngineChoice == nppGui.se_yahoo)
			{
				url = TEXT("https://search.yahoo.com/search?q=$(CURRENT_WORD)");
			}

			Command cmd(url.c_str());
			cmd.run(_pPublicInterface->getHSelf());	
		}
``` 

## Steps To Reproduce:

  1. Go to `Settings->Search Engine` in the text box write `cmd /K echo boom`
  2. Click on `Edit->On Selection->Search on Internet`
  3. A command prompt is launched and `echo boom` is executed

## Impact

Arbitrary commands execution.

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
