---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-01_angularjs-client-side-template-injection-the-orderby-filter.md
original_filename: 2022-09-01_angularjs-client-side-template-injection-the-orderby-filter.md
title: 'AngularJS Client-Side Template Injection: The orderBy Filter.'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 1378b003c34a3c906ce79767f91d109395c490042f910fb1b3c9a9f51bafea76
text_sha256: a59542fa3a926e18ac07ca8ce518c7879ecb2f6c7dd9bbc7bc808f6b820d4475
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# AngularJS Client-Side Template Injection: The orderBy Filter.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-01_angularjs-client-side-template-injection-the-orderby-filter.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `1378b003c34a3c906ce79767f91d109395c490042f910fb1b3c9a9f51bafea76`
- Text SHA256: `a59542fa3a926e18ac07ca8ce518c7879ecb2f6c7dd9bbc7bc808f6b820d4475`


## Content

---
title: "AngularJS Client-Side Template Injection: The orderBy Filter."
url: "https://medium.com/@xJay/angularjs-client-side-template-injection-the-orderby-filter-20002ca2a0e8"
authors: ["Jay"]
bugs: ["CSTI"]
publication_date: "2022-09-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2228
scraped_via: "browseros"
---

# AngularJS Client-Side Template Injection: The orderBy Filter.

AngularJS Client-Side Template Injection: The orderBy Filter.
_
Follow
7 min read
·
Sep 1, 2022

28

1

Intro:

Recently, while reading research on the interesting vulnerabilities that arise from improper use of client-side template frameworks (like AngularJS), I knew I wanted to try this out for myself. When I came across an image bank using Angular on a VDP I’ve been exploring for the past few weeks, I knew it was the perfect opportunity to put the research into practice, and this ended with exciting results.

A few years ago, the release of Angular 1.6 brought many interesting changes to the framework. The most interesting of these changes was the removal of the expression sandbox. It’s important to note that the intention of the Angular sandbox was never a security mechanism. This means that the many sandbox escapes that researchers highlighted weren’t considered vulnerabilities, even though up until version 1.6 their team continued to patch the sandbox. However, this still gave many developers a false sense of security due to incorrectly assuming that the sandbox itself would protect their application against attacks much like the one highlighted in this post. After the removal, many developers who were once relying on the false sense of security that the sandbox provided (which only made attacks such as these slightly more difficult) are now left to realize that their code allowing untrusted input to be executed as Angular expressions was the problem, and not a weak sandbox.

As a final disclaimer, this is a particularly low priority asset. Meaning the impact of this attack in this particular context is negligible. However, I do think that this is a cool example of what can arise from naive use of templating frameworks like Angular, and I’m positive that more applications are susceptible to similar vulnerabilities.

The Vulnerability:

Due to the relatively small application and knowing what I wanted to find, locating the source of the vulnerability happened fairly quickly. It was just a matter of finding user controlled input that would be evaluated as an expression. When walking through the normal flow of the application, I noticed a URL parameter that was presented when clicking on an image category:

https://<URL>/category?sort=random{<arbitrary number>}

Without much thought, I replaced the parameter value with a basic test expression (?sort={{7*7}}) to see if my input was evaluated and reflected somewhere within the page. And through sheer luck, the template expression was executed and stored within an SEO tag like so:

<meta property="og:url" content="https://<URL>/category?sort=49">

Before moving any further, I think it’s a good time to explain scope in AngularJS. The scope is the binding between HTML (view) and JavaScript (controller) and contains application data and objects. For demonstration purposes, let’s assume our current scope object is defined in the code below:

$scope.imagename= "cute-cat-picture.png";
$scope.getimagename= function() {
  return 'The current image is ' + $scope.imagename;
  };

What does this mean for us? Angular expressions are evaluated against the scope object and not against the global object which contains builtin JavaScript functions, this means we can’t evaluate an expression like the below example and pop an alert due to our current scope object not containing the function we need (Unless we define it):

Invalid Template Expression: {{alert(1)}}

But, if we are limited to the resources of the scope object, how can we execute the functions that we need from the global object? It’s actually quite simple, and the answer can be found in the constructor property. The constructor property returns a reference to an Object instances constructor function (the object constructor function that created the object), an example of this can be seen below:

let o = {}
o.constructor === Object // true
let o = new Object
o.constructor === Object // true

However, if we don’t reference any object, the property is executing in the global context (window.constructor). Where window is a function instance, and functions in JavaScript are also objects which means that the constructor is a Function. For example:

constructor === Window; //true
constructor.constructor === Function; //true (Which is the same as)
window.constructor.constructor === Function; //true

Similar to eval(), Function can be used to create a function instance using a string input as the function body. Meaning if the string input was a JavaScript function within the global object, like alert(), the result would be a function that calls alert() when executed.

constructor.constructor('alert(1)')() // Is the same as
Function('alert(1)'); // Which is the same as
function () {
  alert(1);
}

Using this information, crafting what should be a working payload is easy. We simply use constructor.constructor to create a function instance that calls a JavaScript built-in from the global object. Which would make the working payload:

{{constructor.constructor('alert(1)')()}}

However, as shown when the template gets reflected in the SEO tag, single quotes are being sanitized causing a syntax error when the application attempts to evaluate our template expression.

<meta property="og:url" content="https://<url>/page?sort={{constructor.constructor(&apos;alert(1)&apos;)()}}">

This presents a harder problem. The problem being that because we are inside a template and anything we put inside of it is being evaluated against the current scope object, we can’t use one of the JavaScript functions that generate strings like the one we need, String.fromCharCode(). When searching for a way to bypass the filter within an expression, I came across this post which detailed an awesome way to solve this problem, the payload can be seen below:

{{constructor.constructor(valueOf.name.constructor.fromCharCode(97,108,101,114,116,40,49,41,10))()}}

The payload works in essentially the same way as what was used to define a function with the constructor property. First, valueOf.name is used because it returns a string value. Second, the constructor property is used to get the constructor function of valueOf.name:

valueOf.name === "valueOf" // true
valueOf.name.constructor === String // true

Because the constructor of valueOf.name is a String object, all of the functions within the String object are accessible. This payload should pop an alert as it meets the criteria for both using a function we need from the global scope, and bypassing the filter.

Press enter or click to view image in full size

As hoped, the alert pops - many, many times. Using context like the name of the URL parameter and it’s intended functionality, we can conjure up a guess that we are most likely injecting into an orderBy filter. While reading about the orderBy filter, I came across this post that details the dangers of allowing user-defined expressions to be passed into orderBy, and how the sandbox could have protected an application from the attack. For a detailed explanation, I encourage anyone to read their research. However, I will be covering why the alert box appears multiple times as I thought it was interesting and provides context as to why this filter can be dangerous if used naively.

Get _’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The orderBy filter returns an array containing items from a specified collection (array or array-like object to sort), ordered by a comparator function (used to determine the relative order of value pairs) based on the values computed using the expression predicate (a predicate to be used by the comparator to determine the order of elements).

Now, what if the developer wanted to update the sort parameter dynamically? e.g. a user clicks on a table header and the collection is sorted by the specified field. To accomplish this, the developer would define the scope property ‘propertyName’ and use that in the orderBy filter instead of a static string. As a user clicks on the table header, ‘propertyName’ is set to the corresponding value and the table sorts accordingly. For example:

https://<url>/page?sort=imagename
https://<url>/page?sort=imagecategory
https://<url>/page?sort=imagedate

The injection vulnerability arises in the three basic steps that constitute how orderBy sorts a collection:

The unsorted list gets passed through a mapping function which creates a new collection with the original item/calculated value to use for the comparison.
The new list gets sorted in order based on the value calculated for each item in the previous step.
The sorted list is created by recreating the original list based on the sorting order determined in step 2.

The first step is the dangerous portion of this algorithm. When a string is supplied as the predicate for sorting the elements in a collection according to a specific property, orderBy evaluates that predicate as an expression against each element in the collection,the result being used for sorting the elements. The function responsible for the first step can be seen here. However, the interesting snippet of code (seen on line 620 to 621) can be seen below:

if (predicate !== ' ') {
  get = $parse(predicate);

$parse is used to convert Angular expressions into JavaScript functions. In the above, orderBy injects a dependency to the $parse service and calls $parse on the provided predicate to convert the expression into a function. This function is then called on every item in the collection to return the comparison object:

return getPredicateValue(predicate.get(value), index);

When the get-function is invoked on each item in the collection, the code that was compiled when passing the predicate to the $parse service is executed. This is why multiple alert boxes are triggered when submitting the payload, the injected expression is executing on each element in the collection.

As stated before, the impact of this bug was minimal given the nature of the application. However, I did think it was really interesting and the research I did while finding the bug, crafting a working payload, and figuring out the “why” of some of the interesting behavior I noticed opened my eyes to a new attack surface, and a new bug to add to my arsenal. To any one who stuck around this long, I hope it did the same for you.

Resources:

https://www.synopsys.com/blogs/software-security/angularjs-1-6-0-sandbox/
https://code.angularjs.org/1.6.9/docs/api/ng/filter/orderBy#under-the-hood
https://docs.angularjs.org/api/ng/service/$parse
http://ghostlulz.com/angularjs-client-side-template-injection-xss/
https://appsec-labs.com/portal/angular-template-injection-without-quote-characters/
https://portswigger.net/research/xss-without-html-client-side-template-injection-with-angularjs
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor
https://github.com/angular/angular.js/blob/v1.6.9/src/ng/filter/orderBy.js#L592
https://github.com/angular/angular.js/blob/v1.6.9/src/ng/filter/orderBy.js#L609
