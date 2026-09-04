# Australian Accounting Technology Index

```
+----------------------------------------------------------------------+
|                  awesome-australian-accounting-tech                  |
+----------------------------------------------------------------------+
|             Curated open source tools for AU accounting              |
+----------------------------------+-----------------------------------+
| DR  what it gives you            | CR  what it needs                 |
+----------------------------------+-----------------------------------+
| curated AU accounting links      | PR submissions to the list        |
| seven category tool index        | -                                 |
+----------------------------------+-----------------------------------+
```

A curated compendium of open-source libraries, computational accounting engines, ATO datasets, legislation APIs, and AI agent workflows.

> A curated list of open-source tools, computational accounting libraries, official government datasets, statutory APIs, and AI agent skills for Australian public practice, commercial finance, and fintech engineering.

---

## Contents

- [Computational Engines & Financial Modelling](#computational-engines--financial-modelling)
- [Compliance, Payroll & Tax Tools](#compliance-payroll--tax-tools)
- [AI Agents & LLM Practitioner Guides](#ai-agents--llm-practitioner-guides)
- [General Ledger & API Connectors](#general-ledger--api-connectors)
- [Official Data Sources & Statutory APIs](#official-data-sources--statutory-apis)
- [Legislation & Primary Source Repositories](#legislation--primary-source-repositories)
- [Spreadsheets, Power Query & M](#spreadsheets-power-query--m)
- [Contributing](#contributing)

---

## Computational Engines & Financial Modelling

- **[Ozzit](https://github.com/ryanduguid/Ozzit)** - 134 native Excel `LAMBDA` functions for dynamic-array financial models. Derivative of a third-party Excel LAMBDA workbook, published with the original author's written permission; adds Australian GST, financial-year, modelling-depreciation and AASB 16 lease helpers. See ATTRIBUTION.md. Not an individual-tax engine.
- **[ATO Benchmark Compare](https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare)** *(`ato-benchmark-compare`, in the australian-accounting monorepo)* - Local, offline CLI tool for comparing business profit and loss figures against ATO Small Business Benchmark ranges, showing exact calculations and account mapping audit trails.
- **[The WIP Tally](https://github.com/ryanduguid/australian-accounting/tree/main/packages/the-wip-tally)** *(`the-wip-tally`, in the australian-accounting monorepo)* - Deterministic AASB 15 construction WIP schedule from a contract CSV: cost-to-cost progress after para B19 exclusions, constrained variations, per-contract contract assets and liabilities, and profit-fade flags. Review aid, not a determination.

---

## Compliance, Payroll & Tax Tools

- **[Payday Super Checker](https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker)** *(`payday-super-checker`, in the australian-accounting monorepo)* - Experimental CLI evaluation tool for validating Australian payday-super contribution timelines, statutory due dates (7 business days), holiday calendars, and estimating SG charge exposure.
- **[Company tax and franking checks](https://github.com/ryanduguid/australian-accounting/tree/main/packages/the-exchequer-tally)** *(`the-exchequer-tally`, in the australian-accounting monorepo)* - Deterministic Base Rate Entity tests under s 23AA of the *Income Tax Rates Act 1986*, Division 203 franking benchmark-rule checks, and corporate distribution statements.
- **[Trust distribution checks](https://github.com/ryanduguid/australian-accounting/tree/main/packages/solomons-sword)** *(`solomons-sword`, in the australian-accounting monorepo)* - Review tooling for trust distributions, including reimbursement-agreement risk indicators under s 100A and foreign-trust receipt calculations under s 99B of the *Income Tax Assessment Act 1936*.
- **[Division 7A loan review](https://github.com/ryanduguid/australian-accounting/tree/main/packages/div7a-loan-review)** *(`div7a-loan-review`, in the australian-accounting monorepo)* - Reviews private-company loan terms and minimum yearly repayments against source-linked benchmark rates, with fabricated inputs and explicit refusal boundaries.
- **[Monthly Close Controls](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/packages/monthly-close-control-plane)** *(`monthly-close-control-plane`, in the accounting-review-pipeline monorepo)* - Review-first controls for monthly and annual trial balance exports, producing deterministic review packs with source hashes and exception surfacing; it does not lock periods.
- **[Workpaper Review Gate](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/packages/review-ready-gate)** *(`review-ready-gate`, in the accounting-review-pipeline monorepo)* - Deterministic readiness gate that stops incomplete BAS, month-end, and year-end workpaper packs from reaching manager review. It does not approve a file.

---

## AI Agents & LLM Practitioner Guides

- **[Aus Accounting MCP](https://github.com/ryanduguid/australian-accounting/tree/main/apps/aus-accounting-mcp)** *(`aus-accounting-mcp`, in the australian-accounting monorepo)* - Unified Model Context Protocol (MCP) server for Australian computational accounting, exposing ATO small-business benchmarks, Payday Super statutory deadline review, and synthetic SBR fixtures to Claude Desktop, Claude Code, Cursor, and Antigravity. Division 7A review is limited to reviewed s 109N terms and s 109E minimum yearly repayments for one operator-supplied amalgamated loan, delegated to `div7a-loan-review`; it fails closed on unknown facts and refuses s 109R, unpaid present entitlements, distributable surplus and other unsupported matters.
- **[Australian Accounting Skills](https://github.com/ryanduguid/australian-accounting-skills)** *(`australian-accounting-skills`)* - 19 Claude Code and Codex agent skills for Australian public practice and contracting-business workflows: BAS preparation, FBT, Division 7A loan registers, Single Touch Payroll (STP) finalisation, year-end workpapers, progress claims, retention ledgers, WIP review, Coal LSL, fuel tax credits and contractor payroll tax. The construction and mining workflows formerly published as Hardhat Ledger ship here since v0.2.0; the WIP arithmetic lives in [The WIP Tally](https://github.com/ryanduguid/australian-accounting/tree/main/packages/the-wip-tally).
- **[DrDebits](https://github.com/ryanduguid/DrDebits)** - Versioned, primary-source-linked ethical instructions and system prompts for LLM-assisted Australian accounting and BAS work.
- **[Xero Ledger Review Gate](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/packages/elizabeth-anne-alexander)** *(`elizabeth-anne-alexander`, in the accounting-review-pipeline monorepo)* - Fixed-policy, zero-network safety boundary designed for AI-assisted trial balance review using synthetic test data.
- **[OpenAccountants](https://github.com/openaccountants/openaccountants)** - Open-source tax guides for AI coding agents with human-in-the-loop review.

---

## General Ledger & API Connectors

- **[Xero Trial Balance Export](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/packages/xero-trial-balance-export)** *(`xero-trial-balance-export`, in the accounting-review-pipeline monorepo)* - Exports balanced Xero trial balances to validated CSV for Power BI, pandas, and Excel. Features rotation-safe OAuth 2.0 refresh handling and Windows DPAPI token encryption.
- **[tap-xero](https://github.com/Matatika/tap-xero)** - Singer tap for extracting data from the Xero API, built on the Meltano Singer SDK.
- **[xero-python](https://github.com/XeroAPI/xero-python)** - Official Xero OAuth 2.0 Python SDK.
- **[xero-node](https://github.com/XeroAPI/xero-node)** - Official Xero OAuth 2.0 NodeJS / TypeScript SDK.

---

## Official Data Sources & Statutory APIs

- **[data.gov.au - ATO Datasets](https://data.gov.au/data/organization/australian-taxation-office)** - Official open datasets published by the Australian Taxation Office, including small business benchmarks, taxation statistics, and annual corporate tax transparency reports.
- **[Standard Business Reporting (SBR)](https://www.sbr.gov.au/)** - Definitive specification and ebMS3 messaging standards for digital reporting to Australian government agencies (ATO, ASIC, APRA, State Revenue Offices).
- **[SuperStream Technical Standards](https://softwaredevelopers.ato.gov.au/SuperStreamStandard)** - Technical specifications and XBRL taxonomy for digital superannuation contributions and rollovers.
- **[Single Touch Payroll (STP) Phase 2 Employer Guide](https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/in-detail/single-touch-payroll-phase-2-employer-reporting-guidelines)** - Detailed disaggregation of gross requirements for Australian payroll systems.

---

## Legislation & Primary Source Repositories

- **[au-tax-legislation-corpus](https://github.com/ryanduguid/au-tax-legislation-corpus)** - Pipeline for building a provenance-rich local retrieval corpus from in-force Commonwealth tax legislation. Also home to [Tax Radar AU](https://github.com/ryanduguid/au-tax-legislation-corpus/blob/main/RADAR.md), which queues potential updates to Australian tax legislation and regulatory sources for human review with provenance on every entry.
- **[Federal Register of Legislation](https://www.legislation.gov.au/)** - Official whole-of-government website for Commonwealth legislation. Key primary acts include:
  - *Income Tax Assessment Act 1997* (ITAA 1997)
  - *Income Tax Assessment Act 1936* (ITAA 1936)
  - *A New Tax System (Goods and Services Tax) Act 1999* (GST Act)
  - *Superannuation Guarantee (Administration) Act 1992* (SGAA 1992)
  - *Fringe Benefits Tax Assessment Act 1986* (FBTAA 1986)
- **[ATO Legal Database](https://www.ato.gov.au/law/)** - Primary repository of ATO public rulings (TR/GSTR), practical compliance guidelines (PCG), Law Companion Rulings (LCR), and taxation determinations (TD).

---

## Spreadsheets, Power Query & M

- **[Accounting Excel Toolkit](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/adapters/accounting-excel-toolkit)** *(`accounting-excel-toolkit`, in the accounting-review-pipeline monorepo)* - Power Query (M) scripts and VBA automation utilities for Australian accounting practice workpapers and ledger transformations.
- **[Australian Accounting Power BI](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/apps/australian-accounting-power-bi)** *(in the accounting-review-pipeline monorepo)* - Source-controlled Power BI project (PBIP and TMDL) for Australian accounting analytics, consolidation, ATO benchmarks and Payday Super review, built on fabricated data.
- **[Microsoft Excel Labs - Advanced Formula Environment](https://github.com/microsoft/excel-labs)** - Official Microsoft add-in for authoring, testing, and managing Excel `LAMBDA` formulas and namespaces.

---

## Contributing

Contributions and suggestions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) and submit a pull request.
