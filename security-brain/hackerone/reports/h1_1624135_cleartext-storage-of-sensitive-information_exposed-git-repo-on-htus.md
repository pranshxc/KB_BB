---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1624135'
original_report_id: '1624135'
title: Exposed GIT repo on ██████████[HtUS]
weakness: Cleartext Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2022-07-07T14:17:05.840Z'
disclosed_at: '2023-05-15T15:18:13.716Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 9
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Exposed GIT repo on ██████████[HtUS]

## Metadata

- HackerOne Report ID: 1624135
- Weakness: Cleartext Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2023-05-15T15:18:13.716Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Git metadata directory (.git) was found in this folder. An attacker can extract sensitive information by requesting the hidden metadata directory that version control tool Git creates. The metadata directories are used for development purposes to keep track of development changes to a set of source code before it is committed back to a central repository (and vice-versa). When code is rolled to a live server from a repository, it is supposed to be done as an export rather than as a local working copy, and hence this problem.

███████

```
Some of Repository files/directories:
├── private
│   ├── Gruntfile.js
│   ├── bootstrap.php
│   ├── build.js
│   ├── classes
│   │   ├── Config.php
│   │   ├── Controller.php
│   │   ├── Database.php
│   │   ├── DatabaseResult.php
│   │   ├── DatabaseResultRow.php
│   │   ├── DebugLog.php
│   │   ├── Dictionary.php
│   │   ├── FileUploader.php
│   │   ├── ImageUploader.php
│   │   ├── Importer.php
│   │   ├── Installer.php
│   │   ├── ModelController.php
│   │   ├── Modeler.php
│   │   ├── Palm
│   │   │   ├── Controller.php
│   │   │   ├── ProblemFetcher.php
│   │   │   └── Status.php
│   │   ├── PalmBrowser.php
│   │   ├── Perls
│   │   │   ├── Controller.php
│   │   │   └── UserManager.php
│   │   ├── Request.php
│   │   ├── Router.php
│   │   ├── UploadController.php
│   │   ├── UserLogin.php
│   │   ├── XmlImporter.php
│   │   └── xAPI
│   │       ├── Builder.php
│   │       ├── Controller.php
│   │       └── Logger.php
│   ├── config.json
│   ├── controllers
│   │   ├── Author
│   │   │   ├── Applications.php
│   │   │   ├── Categories.php
│   │   │   ├── DefaultParameters.php
│   │   │   ├── Globals.php
│   │   │   ├── Images.php
│   │   │   ├── Lists.php
│   │   │   ├── Modules.php
│   │   │   ├── ProblemLayouts.php
│   │   │   ├── ProblemTemplates.php
│   │   │   ├── Problems.php
│   │   │   ├── Publish.php
│   │   │   ├── Tags.php
│   │   │   ├── Unpublish.php
│   │   │   ├── UploadImage.php
│   │   │   └── Users.php
│   │   ├── Import
│   │   │   ├── Parse.php
│   │   │   └── Submit.php
│   │   ├── Palm
│   │   │   ├── Browse.php
│   │   │   ├── Load.php
│   │   │   ├── Problem.php
│   │   │   ├── Reset.php
│   │   │   └── Sequence.php
│   │   ├── Perls
│   │   │   ├── ListModules.php
│   │   │   ├── ProbeProblems.php
│   │   │   ├── RequestPalm.php
│   │   │   ├── SampleProblems.php
│   │   │   └── UserStatus.php
│   │   ├── User
│   │   │   ├── ConfirmEmail.php
│   │   │   ├── Consent.php
│   │   │   ├── Login.php
│   │   │   ├── Logout.php
│   │   │   ├── Register.php
│   │   │   ├── ResetPassword.php
│   │   │   ├── Save.php
│   │   │   ├── Touch.php
│   │   │   ├── Unique.php
│   │   │   └── VerifyEmail.php
│   │   └── xAPI
│   │       ├── Categories.php
│   │       ├── Modules.php
│   │       ├── Problems.php
│   │       ├── Statements.php
│   │       └── Users.php
│   ├── install.xml
│   ├── models
│   │   ├── Applications.php
│   │   ├── Categories.php
│   │   ├── FileTags.php
│   │   ├── GlobalParameters.php
│   │   ├── ImageTypes.php
│   │   ├── Images.php
│   │   ├── Lists.php
│   │   ├── Modules.php
│   │   ├── ProblemLayouts.php
│   │   ├── ProblemTemplates.php
│   │   ├── Problems.php
│   │   └── Users.php
│   ├── package.json
│   ├── sql
│   │   ├── application_parameters.sql
│   │   ├── applications.sql
│   │   ├── categories.sql
│   │   ├── category_parameters.sql
│   │   ├── category_prerequisites.sql
│   │   ├── completed_modules.sql
│   │   ├── file_tags.sql
│   │   ├── global_parameters.sql
│   │   ├── image_tag_map.sql
│   │   ├── image_types.sql
│   │   ├── images.sql
│   │   ├── lists.sql
│   │   ├── module_parameters.sql
│   │   ├── modules.sql
│   │   ├── performances.sql
│   │   ├── priorities.sql
│   │   ├── problem_graph.sql
│   │   ├── problem_layouts.sql
│   │   ├── problem_parameters.sql
│   │   ├── problem_templates.sql
│   │   ├── problems.sql
│   │   ├── problems_logged.sql
│   │   ├── retired_categories.sql
│   │   ├── user_authentication.sql
│   │   ├── user_status.sql
│   │   ├── users.sql
│   │   └── xapi_statements.sql
│   └── vendor
│       └── TinCanPHP
│           ├── About.php
│           ├── Activity.php
│           ├── ActivityDefinition.php
│           ├── ActivityProfile.php
│           ├── Agent.php
│           ├── AgentAccount.php
│           ├── AgentProfile.php
│           ├── Attachment.php
│           ├── Context.php
│           ├── ContextActivities.php
│           ├── Document.php
│           ├── Extensions.php
│           ├── Group.php
│           ├── LRSInterface.php
│           ├── LRSResponse.php
│           ├── LanguageMap.php
│           ├── Map.php
│           ├── Object.php
│           ├── RemoteLRS.php
│           ├── Result.php
│           ├── Score.php
│           ├── State.php
│           ├── Statement.php
│           ├── StatementBase.php
│           ├── StatementRef.php
│           ├── StatementTargetInterface.php
│           ├── StatementsResult.php
│           ├── SubStatement.php
│           ├── Util.php
│           ├── Verb.php
│           ├── Version.php
│           └── VersionableInterface.php
```


Also the config.json file is expsing senstive infomration
```
{
    // ----------------------------------------------------------------------------------
    // Authoring Tools config file
    // This file is in a JSON format, but comments are allowed.  Make sure all values
    // follow correct JSON syntax.
    // ----------------------------------------------------------------------------------

    // URL_BASE
    // The absolute url prefix to the root of the site.  For example, if the root of the
    // site is at "http://localhost/~fred/site/", the value would be "/~fred/site/".
    // The default value is the domain root, or "/".

    "URL_BASE":                 "/",

    // FORCE_SSL
    // Forces all connections and internal redirects to https.

    "FORCE_SSL":                false,

    // DEBUG_DISPLAY
    // Setting this to true will enable the debug log to be displayed and passed back
    // through AJAX responses

    "DEBUG_DISPLAY":            false,

    // DEBUG_EMAIL_ADDRESSES
    // Array of email addresses to send debug log messages to.

    "DEBUG_EMAIL_ADDRESSES":    [],

    // DEBUG_EMAIL_LEVELS
    // Array of debug log levels to trigger debug emails.  Emails are only sent if an
    // item was logged at that level, and if at least one email address (see above) is
    // set.

    "DEBUG_EMAIL_LEVELS":       ["ERROR"],

    // DEBUG_CAPTURE_ERRORS
    // If true, PHP errors (notices, warnings, etc.) will be captured and inserted into
    // the debug log using a custom error handler.  Otherwise, they will be handled
    // according to the PHP configuration settings.  Fatal errors are not captured.

    "DEBUG_CAPTURE_ERRORS":     true,

    // FORCE_UNBUILT_RESOURCES
    // This forces the use of the unbuilt JavaScript and CSS for the site.  Otherwise,
    // the site will use the built files automatically if they are detected in the build
    // directory.

    "FORCE_UNBUILT_RESOURCES":  false,

    // DATABASE_HOST
    // Database host to connect to

    "DATABASE_HOST":            "localhost",

    // DATABASE_USER
    // Name of the database user to connect as

    "DATABASE_USER":            "authoring_tools",

    // DATABASE_PASSWORD
    // Password to connect with

    "DATABASE_PASSWORD":        "████",

    // DATABASE_NAME
    // Name of the Authoring Tools database

    "DATABASE_NAME":            "authoring_tools",

    // INSTALLER_ENABLED
    // Set this to true to enable access to the database installation script located at
    // '/install.php'.  Once the installer has been run and the site is running correctly,
    // reset this back to false to prevent further access.

    "INSTALLER_ENABLED":        false,

    // SYSTEM_EMAIL
    // The originating email address for all system emails (e.g. account validation).
    // Setting this to an appropriate value can help prevent messages from being
    // filtered as spam.

    "SYSTEM_EMAIL":            "no-reply@example.com",

    // BLOCK_SIZE
    // The number of trials per block

    "BLOCK_SIZE":               10,

    // XAPI_LOCAL_STATEMENTS
    // Set this to true to store xAPI statements in the Authoring Tools database.  This
    // will potentially incur a cost in database storage, since many statements may be
    // generated.

    "XAPI_LOCAL_STATEMENTS":    false,

    // XAPI_REMOTE_LRS_ENDPOINT
    // Base URL for remote LRS to send statement data to.  If null, no data is sent.

    "XAPI_REMOTE_LRS_ENDPOINT": null,

    // XAPI_REMOTE_LRS_USER
    // Username for authenticating connection with remote LRS (as specified in
    // XAPI_REMOTE_LRS_ENDPOINT)

    "XAPI_REMOTE_LRS_USER":     "",

    // XAPI_REMOTE_LRS_PASSWORD
    // Password for authenticating connection with remote LRS (as specified in
    // XAPI_REMOTE_LRS_ENDPOINT)

    "XAPI_REMOTE_LRS_PASSWORD":  "",

    // PERLS_SECRET_KEY
    // PERLS access key for embedding modules and authenticating users.  Set this to a
    // string value that the PERLS system must send with the request as the 'key'
    // parameter.  If set to true, access will be allowed without any secret key.  Null
    // or false will disable PERLS access.

    "PERLS_SECRET_KEY":         null,

    // PARAMETER_DEFAULTS
    // Default values for global parameters

    "PARAMETER_DEFAULTS":
    {
        "delay_constant":       2.0,
        "default_weight":       1.0,
        "rt_weight":            0.1,
        "incorrect_penalty":    2.0,
        "rt_divisor":           1000,
        "window":               3,
        "target_accuracy":      1.0,
        "target_rt":            10000,
        "timeout":              30000
    }
}
```

## Impact

These files may expose sensitive information that may help an malicious user to prepare more advanced attacks

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
