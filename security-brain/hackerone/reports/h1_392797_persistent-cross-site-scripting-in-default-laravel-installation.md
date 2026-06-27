---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '392797'
original_report_id: '392797'
title: Persistent Cross-Site Scripting in default Laravel installation
team_handle: laravel
created_at: '2018-03-07T16:40:04.000Z'
disclosed_at: '2018-08-10T15:57:55.973Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 58
tags:
- hackerone
---

# Persistent Cross-Site Scripting in default Laravel installation

## Metadata

- HackerOne Report ID: 392797
- Weakness: 
- Program: laravel
- Disclosed At: 2018-08-10T15:57:55.973Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Persistent XSS in default Laravel Installation

I have been using the [Laravel](https://laravel.com/) framework for quite a while now and discovered something odd.

When following the installation instructions for the latest Laravel version **(5.6.8 at the time of writing)** you will be up and running in a matter of minutes.

Even better: With a single command such as `php artisan make:auth` from the CLI, Laravel will scaffold basic login and registration views and routes.

This is a very convenient function and saves developers a lot of time. But what if there is some resource included that might be vulnerable? 

# POC

Vulnerability: Persistent Cross-site Scripting.

## Installation

Following the instruction from the [Laravel Docs](https://laravel.com/docs/5.6) we can quickly create a new project with basic authentication.

You can use the Laravel installer: `laravel new project` (where project is the directory that is going to be used for your new project.)

This requires you to global require the laravel installer first: `composer global require "laravel/installer"`

The other option is the "old" way with Composer: `composer create-project --prefer-dist laravel/laravel project`

After running one of the above commands your project will be created and you can start developing a new application. Pretty neat.

I am using the the `Vagrant/Homestead` [box](https://laravel.com/docs/5.6/homestead) for local development.
If you haven't tried it and you are developing PHP applications I recommend checking this out!

{F331053}

## User registration and authentication

We now have a fresh Laravel project. Let's start with building the user registration and authentication functionality: `php artisan make:auth`

This will create a view, some controllers and database migrations.

When this is done all you have to do is `php artisan migrate` and you are ready to go.

{F331052}

## The vulnerability

So, the setup is ready. Time to show the proof of concept

Since we used the `php artisan make:auth` command we now have a login and registration function.

{F331055}

Let's create a user:

{F331054}

The vulnerability lies within the username field: using `{{ alert(document.domain) }}`  , Laravel transforms this to `<script>alert(document.domain)</script>` due to Vue.js frontend.
This is the default frontend framework that Laravel uses.

After checking the `app.js` file in /project/resources/assets/js/ we can see that Laravel indeed uses Vue.js as default frontend framework:

``` javascript

/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries. It is a great starting point when
 * building robust, powerful web applications using Vue and Laravel.
 */

require('./bootstrap');

window.Vue = require('vue');

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

Vue.component('example-component', require('./components/ExampleComponent.vue'));

const app = new Vue({
    el: '#app'
});

```

This is where the vulnerability hides, as Vue sees curly brackets and turns it into `<script>` tags. Also, the `v-pre` tags were not present in the default front end code, combined with the curly brackets this led to the persistent cross-site scripting vulnerability.

After authenticating with a registered user that has the payload set as name:

{F331056}

I disclosed this issue to the creator of Laravel through email, later on via Twitter and a blogpost . The issue was fixed with the release of patch **(5.6.9)** within 15 minutes.

Thanks for reading, more posts @ https://x1m.nl

[x1m](https://twitter.com/x1m_martijn)

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
