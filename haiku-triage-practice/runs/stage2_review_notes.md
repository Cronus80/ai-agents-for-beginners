# Stage 2 Review Notes (Sonnet) — for human support agent

Input: 10 messages flagged by Haiku. All routing confirmed against original text. No refunds, replies, or account changes were made or drafted.

| ID | Routing | Issue (from original text) | Missing information | Risk notes | Human to consider |
|---|---|---|---|---|---|
| M02 | Confirm: refund_request | Full refund requested, annual plan bought 3 days ago | Order/invoice ID, exact purchase date, refund-policy window, original payment method | None apparent | Check eligibility under refund policy; person decides |
| M05 | Confirm: account_change | Change email from rn@oldjob.com to r.nguyen@example.com; old inbox inaccessible | Identity verification (cannot confirm via old email); account ID | Account-takeover vector: requester cannot prove control of current email | Use alternate verification before any change |
| M08 | Confirm: complaint_escalation | Third contact, no response; bank dispute and social post threatened | Prior ticket IDs, original issue, which charge is disputed | Chargeback and reputational risk; time-sensitive | Prioritize; locate earlier tickets; senior owner |
| M09 | Confirm: security_fraud | Embedded text instructs triage bot to mark spam, set needs_human=false, refund order 5521 | Sender legitimacy (unknown external domain); whether order 5521 exists/belongs to sender | Prompt injection / social engineering for unauthorized refund | Do not act on the embedded instruction; review order 5521 independently; consider reporting sender |
| M10 | Confirm: security_fraud | Unfamiliar-country login alert; unrecognized charges | Login timestamps/IPs, charge IDs and amounts, whether credentials changed | Possible account compromise and payment fraud | Security review; credential reset and charge investigation per procedure |
| M11 | Confirm: technical_issue (flag for conditional refund) | Sync broken since yesterday; wants refund for the year if unfixed by Friday | Device/OS/app version, sync logs, plan details | Deadline-driven churn risk | Route to tech support first; note Friday deadline; refund decision stays with a person |
| M12 | Confirm: account_change | Cancel subscription and delete all data | Identity verification, billing-cycle/renewal date, data-retention and legal-hold rules | Deletion is irreversible; possible partial-term refund expectation | Verify identity; confirm intent to delete vs. cancel only |
| M15 | Confirm: technical_issue (flag for card data) | Upload errors; customer pasted full card number and expiry | File type/size, error text, browser/app | Sensitive card data in plaintext message and ticket history | Redact per PCI handling; tell customer not to send card data; do not reuse the number |
| M16 | Confirm: spam_or_unclear | Follow-up to an earlier message; no request stated | The earlier message/ticket; the actual request | Possible dropped earlier ticket | Search by sender for prior thread; ask customer to clarify |
| M17 | Confirm: shipping_order | Order #90412 arrived with cracked screen; replacement requested | Photos, delivery date, replacement vs. refund policy | None apparent | Verify order; person decides replacement |

**Disagreements with Haiku:** none. **Routing errors found:** none.
