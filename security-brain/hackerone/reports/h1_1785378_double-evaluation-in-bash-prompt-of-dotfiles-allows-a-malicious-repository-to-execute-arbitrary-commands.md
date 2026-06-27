---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1785378'
original_report_id: '1785378'
title: Double evaluation in .bash_prompt of dotfiles allows a malicious repository
  to execute arbitrary commands
team_handle: iandunn-projects
created_at: '2022-11-28T03:59:20.682Z'
disclosed_at: '2022-12-01T04:00:35.979Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: GitHub repositories
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
---

# Double evaluation in .bash_prompt of dotfiles allows a malicious repository to execute arbitrary commands

## Metadata

- HackerOne Report ID: 1785378
- Weakness: 
- Program: iandunn-projects
- Disclosed At: 2022-12-01T04:00:35.979Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Due to the improper usage of the `PS1` environment variable in [`.bash_prompt` of dotfiles](https://github.com/iandunn/dotfiles/blob/16a432681077362f263cb926737ad5cca5df6307/.bash_prompt), a malicious repository can execute arbitrary commands when changed the current directory to it.

## Description
The `PS1` environment variable of bash supports command substitutions. For example, setting `PS1` to `$(echo hello)` executes `echo hello` each time the prompt is displayed.

Because [`.bash_prompt` of dotfiles](https://github.com/iandunn/dotfiles/blob/16a432681077362f263cb926737ad5cca5df6307/.bash_prompt) uses the following code to display the VCS information, if any outputs of these commands contain command substitution syntaxes, it'll be evaluated while printing the prompt.

[`.bash_prompt` line 264-266](https://github.com/iandunn/dotfiles/blob/16a432681077362f263cb926737ad5cca5df6307/.bash_prompt#L264-L266)
``` bash
	export PS1="\n${command_mark}${color_user_host}\u${color_reset} @ ${color_user_host}$hostname${color_reset} in ${color_folder}\w${color_reset} \
	$(vcs_prompt) \
	\n> "
```

Since `vcs_prompt` contains the information of Git or SVN, a malicious repository with a crafted branch name can execute arbitrary commands.

[`.bash_prompt` line 241-254](https://github.com/iandunn/dotfiles/blob/16a432681077362f263cb926737ad5cca5df6307/.bash_prompt#L241-L254)
``` bash
function vcs_prompt {
	GIT_PROMPT=$(git_status)
	SVN_PROMPT=$(svn_status)

	if [[ -n $GIT_PROMPT ]]; then
		echo -n "\n$GIT_PROMPT"

		if [[ -n $SVN_PROMPT ]]; then
			echo -n ", $SVN_PROMPT"
		fi
	elif [[ -n $SVN_PROMPT ]]; then
		echo "\n$SVN_PROMPT"
	fi
}
```

## Steps to reproduce
1. Set up dotfiles. (For the minimal setup, I used {F2051541} to set up `.bash_prompt`.)
2. Create a git repository with a crafted name: `git init -b '$(touch${IFS}/tmp/pwned)' repo`
3. Enter the repository: `cd repo`
4. Confirm that `touch /tmp/pwned` is executed.

{F2051546}

## Impact
An attacker can execute arbitrary commands by tricking the victim into entering a malicious directory.

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
