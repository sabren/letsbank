# sabren/letsbank

> LETSbank — "currency for collaboration": a community-currency
> bank web app from 2003–2004, built on the workshop stack
> (sixthday, strongbox, zebra). Members log in, transfer currency
> to each other with notes, and view balances and histories
> computed on the fly. An alpha-test artifact: its own homepage
> warns the database would be wiped clean on 10/01/2003.
> Repo: https://github.com/sabren/letsbank — 43 files, git history
> in this clone 2003-09-25 → 2004-05-10. **Keep — documented here;
> the archive step is blocked (see below), so no archive was
> attempted.**

## What it is

- **The app (`letsbank/` package):** `Bank.py` (account lookup,
  `balanceFor`/`historyFor` computed from transaction history),
  `Account.py`, `AccountAuth.py`, `Transaction.py`,
  `BankingApp.py` (extends sixthday's `AdminApp`; transfer form
  with messages "transfer successful!", "amount must be positive",
  "invalid amount!", "can't transfer money to yourself"), and
  `ProfileApp.py` (per-user history/balance view, HTML or XML
  output). Balances are calculated on the fly, not stored.
- **The web front end (`letsbank.org/`):** zebra templates (`.zb`)
  and `.app` scripts — `index.html` ("LETSbank! - currency for
  collaboration", username/password login form), `banking.app`
  (auth check, then `BankingApp`), `profile.app`, `signup.app`,
  `main.zb` (transfer form: amount, destination user, note), plus
  `letsbank.css`, logos, and a welcome-mail template.
- **Tests (`letsbank/spec/`):** four small test files (111 lines
  total): `BankTest`, `AccountTest`, `AccountAuthTest`,
  `TransactionTest`.
- **Dependencies:** imported from the workshop stack — `pytypes`
  (`FixedPoint`), `sixthday`, `strongbox`, `zebra` — none of them
  vendored in this repo. The tree also carries a `CVSROOT/`
  directory and `.cvsignore` files, consistent with its CVS-era
  origin; the repo itself does not state its import history.
- **History:** initial checkin 2003-09-25, profiles and template
  refactoring in a 2003-10-07 batch, last commit 2004-05-10
  ("cleanup after strongbox/arlo fixes").

## Archive status — blocked, not attempted

The tickler for this repo said "document and archive", but
archiving sabren repos is currently blocked: the tangentstorm
account has push-only access without admin on sabren repos, and
past archive attempts failed with 403. No archive was attempted
for letsbank, and none should be attempted until Michal archives
it while logged in as sabren or grants tangentstorm admin on
sabren repos.

## Verdict

**Keep (documented) — archive pending his action as sabren.**
The repo is a small, complete, historically interesting app; the
doc above is the record, and the archive decision waits on the
admin-access fix, not on anything in the code.
