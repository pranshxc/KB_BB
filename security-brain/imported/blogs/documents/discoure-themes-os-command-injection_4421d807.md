---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-18_discoure-themes-os-command-injection.md
original_filename: 2021-04-18_discoure-themes-os-command-injection.md
title: Discoure themes OS Command Injection
category: documents
detected_topics:
- command-injection
- webhooks
tags:
- imported
- documents
- command-injection
- webhooks
language: en
raw_sha256: 4421d807e64ac1694305b55c5dbe87caf39477ac355d229125c9302da5f1b158
text_sha256: 12fea26845756832eac03f754dd65b3b379e725b4c9761fe05c608964007a340
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Discoure themes OS Command Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-18_discoure-themes-os-command-injection.md
- Source Type: markdown
- Detected Topics: command-injection, webhooks
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `4421d807e64ac1694305b55c5dbe87caf39477ac355d229125c9302da5f1b158`
- Text SHA256: `12fea26845756832eac03f754dd65b3b379e725b4c9761fe05c608964007a340`


## Content

---
title: "Discoure themes OS Command Injection"
page_title: "Discourse themes OS Command Injection :: 0day.click"
url: "https://0day.click/recipe/2021-04-18-discourse-themes/"
final_url: "https://0day.click/recipe/2021-04-18-discourse-themes/"
authors: ["joernchen (@joernchen)"]
programs: ["Discourse"]
bugs: ["RCE", "OS command injection"]
publication_date: "2021-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3733
---

#  [Discourse themes OS Command Injection](https://0day.click/recipe/2021-04-18-discourse-themes/)

2021-04-18

[Discourse](https://www.discourse.org/) offers the possibility to install themes from remote Git repositories. Before [this commit](https://github.com/discourse/discourse/commit/94301854938a0b36dd64666fb7a7c8406544a781) it was possible to inject OS commands via a maliciously crafted theme which is pulled via Git.

The root cause for the issue lay in the parsing of the [`.discourse-compatibility` file](https://meta.discourse.org/t/introducing-discourse-compatibility-pinned-plugin-theme-versions-for-older-discourse-versions/156971) which is a yaml file containing a mapping of the target discourse version and a git version to be checked out for that specific discourse version.

The version information is passed to

`lib/theme_store/git_importer.rb`:
  
  
  def import!
  if @private_key
  import_private!
  else
  import_public!
  end
  if version = Discourse.find_compatible_git_resource(@temp_folder)
  Discourse::Utils.execute_command(chdir: @temp_folder) do |runner|
  return runner.exec("git cat-file -e #{version} || git fetch --depth 1 $(git rev-parse --symbolic-full-name @{upstream} | awk -F '/' '{print $3}') #{version}; git reset --hard #{version}")
  end
  end
  end
  

Here we can inject shell commands into the `version` variable simply by providing a `.discourse-compatibility` file in the git repo containing:
  
  
  2.6.4: master`id>/tmp/haxx`
  

On a discourse installation running version `2.6.4` this will write the current user id to `/tmp/haxx` when importing or updating the theme, as the [`find_compatible_git_resource`](https://github.com/discourse/discourse/blob/0afcf9e12ee2bf770ba32ec486a13a48169d36d7/lib/version.rb#L33-L67) method did not further sanitize the `.discourse-compatibility` entries.

The issue has been reported to discourse on April 11th 2021 via their [bug bounty program](https://hackerone.com/discourse) and was resolved three days later.

* * *

[ < [Discourse SNS webhook RCE] ](https://0day.click/recipe/discourse-sns-rce/) :: [ [Mosaic "0day"] > ](https://0day.click/recipe/m0s41c/)
