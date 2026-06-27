---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '449680'
original_report_id: '449680'
title: Attacker can claim credentials for private program that has a published external
  program
weakness: Information Disclosure
team_handle: security
created_at: '2018-11-26T04:55:26.638Z'
disclosed_at: '2018-11-29T19:43:59.906Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 31
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Attacker can claim credentials for private program that has a published external program

## Metadata

- HackerOne Report ID: 449680
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2018-11-29T19:43:59.906Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An attacker can obtain credentials for private programs that have a published external program, even when the attacker doesn't have access to the private program. Here is the regression spec to proof the security vulnerability:

```diff
diff --git a/spec/integration/graphql/mutations/claim_credential_mutation_spec.rb b/spec/integration/graphql/mutations/claim_credential_mutation_spec.rb
index 45745b0ce5..a81439bfe9 100644
--- a/spec/integration/graphql/mutations/claim_credential_mutation_spec.rb
+++ b/spec/integration/graphql/mutations/claim_credential_mutation_spec.rb
@@ -46,6 +46,20 @@ describe Mutations::ClaimCredentialMutation do
   context 'with authenticated user' do
     let(:current_user) { create :user }

+    context 'external program' do
+      let!(:external_program) { create :external_program, team: team }
+
+      context 'that runs a private program' do
+        let(:team) { create :team, :soft_launched }
+
+        context 'user does not have access to private program' do
+          it 'does not claim the credential' do
+            expect { subject }.not_to change { credential.reload.user }
+          end
+        end
+      end
+    end
+
     it { expect { subject }.to change { credential.reload.user }.from(nil).to(current_user) }

     it 'checks if it should send a low-credential-count notification' do
```

## Impact

An attacker can drain the pool of credentials and obtain new credentials, even when they don't have access to the program. This may leak sensitive information.

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
