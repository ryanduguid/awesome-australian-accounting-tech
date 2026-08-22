# Awesome Australian Accounting Tech

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

- **[Ozzit](https://github.com/ryanduguid/Ozzit)** - 130 native Excel `LAMBDA` functions for dynamic-array financial models. Derivative of Craig Hatmaker's Financial Starter Pack; this repo adds Australian GST/FY helpers. See ATTRIBUTION.md. Not an individual-tax engine.
- **[RaymondChambers](https://github.com/ryanduguid/RaymondChambers)** *(ATO Benchmark Compare)* - Local, offline CLI tool for comparing business profit and loss figures against ATO Small Business Benchmark ranges, showing exact calculations and account mapping audit trails.

---

## Compliance, Payroll & Tax Tools

- **[CharlesHenryWickens](https://github.com/ryanduguid/CharlesHenryWickens)** *(payday-super-checker)* - Experimental CLI evaluation tool for validating Australian payday-super contribution timelines, statutory due dates (7 business days), holiday calendars, and estimating SG charge exposure.
- **[TheExchequerTally](https://github.com/ryanduguid/TheExchequerTally)** - Deterministic Base Rate Entity tests under s 23AA of the *Income Tax Rates Act 1986*, Division 203 franking benchmark-rule checks, and corporate distribution statements.
- **[SolomonsSword](https://github.com/ryanduguid/SolomonsSword)** - Review tooling for trust distributions, including reimbursement-agreement risk indicators under s 100A and foreign-trust receipt calculations under s 99B of the *Income Tax Assessment Act 1936*.
- **[Tax Radar AU](https://github.com/ryanduguid/tax-radar-au)** - Queues potential updates to Australian tax legislation and regulatory sources for human review, with provenance tracking and strict synthetic-data test baselines.
- **[RussellMathews](https://github.com/ryanduguid/RussellMathews)** *(monthly-close-control-plane)* - Review-first controls for monthly and annual trial balance exports, producing deterministic review packs with source hashes and exception surfacing; it does not lock periods.

---

## AI Agents & LLM Practitioner Guides

- **[JohnKenley](https://github.com/ryanduguid/JohnKenley)** *(aus-accounting-mcp)* - Unified Model Context Protocol (MCP) server for Australian computational accounting, exposing ATO small-business benchmarks, Payday Super statutory deadline review, and synthetic SBR fixtures to Claude Desktop, Claude Code, Cursor, and Antigravity. Division 7A is refused by design until a reviewed engine exists.
- **[MaryAddisonHamilton](https://github.com/ryanduguid/MaryAddisonHamilton)** *(Australian Accounting Skills for Claude Code)* - 9 Claude Code agent skills for Australian public practice accounting workflows: BAS preparation, FBT return compilation, Division 7A loan registers, Single Touch Payroll (STP) finalisation, and year-end workpapers.
- **[Hardhat Ledger](https://github.com/ryanduguid/hardhat-ledger)** - Claude Code skills tailored for Australian construction and mining subcontractors: progress claim schedules, retention ledgers, WIP calculations, Coal LSL, and contractor payroll tax provisions.
- **[DrDebits](https://github.com/ryanduguid/DrDebits)** - Versioned, primary-source-linked ethical instructions and system prompts for LLM-assisted Australian accounting and BAS work.
- **[ElizabethAnneAlexander](https://github.com/ryanduguid/ElizabethAnneAlexander)** - Fixed-policy, zero-network safety boundary designed for AI-assisted trial balance review using synthetic test data.
- **[OpenAccountants](https://github.com/openaccountants/openaccountants)** - Open-source tax guides for AI coding agents with human-in-the-loop review.

---

## General Ledger & API Connectors

- **[JohnSpenceOgilvy](https://github.com/ryanduguid/JohnSpenceOgilvy)** *(Xero Trial Balance Export)* - Exports balanced Xero trial balances to validated CSV for Power BI, pandas, and Excel. Features rotation-safe OAuth 2.0 refresh handling and Windows DPAPI token encryption.
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

- **[SirArthurFadden](https://github.com/ryanduguid/SirArthurFadden)** - Pipeline for building a provenance-rich local retrieval corpus from in-force Commonwealth tax legislation.
- **[Federal Register of Legislation](https://www.legislation.gov.au/)** - Official whole-of-government website for Commonwealth legislation. Key primary acts include:
  - *Income Tax Assessment Act 1997* (ITAA 1997)
  - *Income Tax Assessment Act 1936* (ITAA 1936)
  - *A New Tax System (Goods and Services Tax) Act 1999* (GST Act)
  - *Superannuation Guarantee (Administration) Act 1992* (SGAA 1992)
  - *Fringe Benefits Tax Assessment Act 1986* (FBTAA 1986)
- **[ATO Legal Database](https://www.ato.gov.au/law/)** - Primary repository of ATO public rulings (TR/GSTR), practical compliance guidelines (PCG), Law Companion Rulings (LCR), and taxation determinations (TD).

---

## Spreadsheets, Power Query & M

- **[SirAlexanderFitzgerald](https://github.com/ryanduguid/SirAlexanderFitzgerald)** - Power Query (M) scripts and VBA automation utilities for Australian accounting practice workpapers and ledger transformations.
- **[Microsoft Excel Labs - Advanced Formula Environment](https://github.com/microsoft/excel-labs)** - Official Microsoft add-in for authoring, testing, and managing Excel `LAMBDA` formulas and namespaces.

---

## Contributing

Contributions and suggestions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) and submit a pull request.
