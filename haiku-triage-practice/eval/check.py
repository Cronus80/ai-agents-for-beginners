#!/usr/bin/env python3
"""Validate and score a routing output.

Usage: check.py <output.json> [messages.jsonl] [answer_key.json]
Checks: every message appears exactly once, category is allowed, quote is a
verbatim substring of the source body. Then scores vs. the answer key.
"""
import json
import sys
from collections import Counter

ALLOWED = {
    "billing_question", "refund_request", "technical_issue", "account_access",
    "account_change", "shipping_order", "feature_request",
    "complaint_escalation", "security_fraud", "spam_or_unclear",
}

out_path = sys.argv[1]
msg_path = sys.argv[2] if len(sys.argv) > 2 else "data/messages.jsonl"
key_path = sys.argv[3] if len(sys.argv) > 3 else "eval/answer_key.json"

msgs = {}
for line in open(msg_path):
    if line.strip():
        m = json.loads(line)
        msgs[m["id"]] = m
key = json.load(open(key_path))
rows = json.load(open(out_path))

problems = []
counts = Counter(r.get("id") for r in rows)
for mid in msgs:
    if counts[mid] == 0:
        problems.append(f"{mid}: missing")
    elif counts[mid] > 1:
        problems.append(f"{mid}: duplicated x{counts[mid]}")
for mid in counts:
    if mid not in msgs:
        problems.append(f"{mid}: unknown id")

cat_ok = flag_ok = 0
missed_flags, false_flags, cat_errors = [], [], []
for r in rows:
    mid = r.get("id")
    if mid not in msgs:
        continue
    if r.get("category") not in ALLOWED:
        problems.append(f"{mid}: invalid category {r.get('category')!r}")
    q = r.get("quote", "")
    if not q or q not in msgs[mid]["body"]:
        problems.append(f"{mid}: quote not verbatim in source")
    k = key[mid]
    if r.get("category") == k["category"]:
        cat_ok += 1
    else:
        cat_errors.append(f"{mid}: got {r.get('category')} expected {k['category']}")
    if bool(r.get("needs_human")) == k["needs_human"]:
        flag_ok += 1
    elif k["needs_human"]:
        missed_flags.append(mid)  # dangerous: should have gone to a person
    else:
        false_flags.append(mid)   # wasteful: unnecessary review

n = len(msgs)
print(f"Structural problems: {len(problems)}")
for p in problems:
    print("  -", p)
print(f"Category accuracy:   {cat_ok}/{n}")
for e in cat_errors:
    print("  -", e)
print(f"Flag accuracy:       {flag_ok}/{n}")
print(f"Missed human review (high severity): {missed_flags or 'none'}")
print(f"Unneeded human review (low severity): {false_flags or 'none'}")
