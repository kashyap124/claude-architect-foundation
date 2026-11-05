# Claude Architect Foundation

A personal study journal and knowledge base for preparing for the **Claude Architect Foundation** certification from Anthropic.

This repo tracks my learning: notes, hands-on labs, practice questions, and a running log of progress, so everything is in one place for revision before the exam.

> **Status:** 🟡 Just started
> **Target exam date:** _TBD_
> **Started:** 2026-11-05

---

## Table of Contents

- [Goals](#goals)
- [Exam Overview](#exam-overview)
- [Study Plan](#study-plan)
- [Progress Tracker](#progress-tracker)
- [Repository Structure](#repository-structure)
- [Core Topics](#core-topics)
- [Resources](#resources)
- [Journal](#journal)
- [How I Use This Repo](#how-i-use-this-repo)

---

## Goals

- Build a solid understanding of how to design, build, and operate solutions on Claude.
- Get hands-on with the Claude API, tool use, agents, and MCP, not just read about them.
- Keep concise, revisable notes that I can skim in the final week before the exam.
- Pass the certification exam.

## Exam Overview

Fill this in from the official exam guide and keep it updated, since the exam may change.

| Item | Details |
| --- | --- |
| Certification | Claude Architect Foundation |
| Provider | Anthropic |
| Format | _TBD_ |
| Duration | _TBD_ |
| Passing score | _TBD_ |
| Registration link | _TBD_ |
| Official exam guide | _TBD_ |

## Study Plan

| Phase | Focus | Target dates | Status |
| --- | --- | --- | --- |
| 1. Foundations | Models, prompting basics, API fundamentals | _TBD_ | ⬜ |
| 2. Building | Tool use, structured outputs, agents, MCP | _TBD_ | ⬜ |
| 3. Production | Evaluation, safety, cost/latency, observability | _TBD_ | ⬜ |
| 4. Revision | Practice questions, weak-area review, mock exam | _TBD_ | ⬜ |

## Progress Tracker

Legend: ⬜ not started · 🟨 in progress · ✅ done

| Topic | Notes | Hands-on lab | Practice Qs | Status |
| --- | --- | --- | --- | --- |
| Models and capabilities | | | | ⬜ |
| Prompt engineering | | | | ⬜ |
| Messages API and SDKs | | | | ⬜ |
| Tool use / function calling | | | | ⬜ |
| Structured outputs | | | | ⬜ |
| Agents and agentic workflows | | | | ⬜ |
| Model Context Protocol (MCP) | | | | ⬜ |
| Prompt caching and context management | | | | ⬜ |
| RAG and retrieval patterns | | | | ⬜ |
| Evaluation and testing | | | | ⬜ |
| Safety, guardrails, responsible use | | | | ⬜ |
| Cost, latency, and scaling | | | | ⬜ |
| Architecture and design patterns | | | | ⬜ |

_Adjust this list to match the official exam domains once confirmed._

## Repository Structure

Planned layout (folders get created as I fill them):

```
claude-architect-foundation/
├── README.md            # This file: overview, plan, tracker
├── notes/               # One markdown file per topic
├── labs/                # Hands-on code and experiments
├── practice/            # Practice questions, mock exams, answers
├── journal/             # Dated daily/weekly study log entries
└── resources/           # Links, cheat sheets, diagrams
```

## Core Topics

Short summaries live in [notes/](notes/). Key questions I want to be able to answer for each topic:

- **Models:** How do I pick between model tiers for capability, cost, and latency?
- **Prompting:** What makes a prompt reliable? How do system prompts, examples, and structure help?
- **Tool use:** How does the tool-use loop work, and how do I handle errors and parallel calls?
- **Agents:** When should I use a workflow vs. an autonomous agent? How do I keep agents safe and bounded?
- **MCP:** What problem does it solve, and how do servers, clients, and tools fit together?
- **Context and caching:** How do I manage long contexts, and when does prompt caching pay off?
- **Evaluation:** How do I measure quality and catch regressions?
- **Safety:** What guardrails, permissions, and human-in-the-loop checks does a production system need?

## Resources

Add links as I find them.

- Anthropic documentation: <https://docs.anthropic.com>
- Anthropic courses and cookbook: _add links_
- Anthropic engineering blog (e.g. building effective agents): _add links_
- Model Context Protocol: <https://modelcontextprotocol.io>
- Official certification page and exam guide: _add link_

## Journal

Newest first. Each entry: date, what I studied, what I built, what is still unclear.

| Date | Summary | Link |
| --- | --- | --- |
| 2026-11-05 | Created the repo and set up the README structure. | |

## How I Use This Repo

1. Study a topic and write a short note in `notes/`.
2. Build something small in `labs/` to make it concrete.
3. Test myself with questions in `practice/`.
4. Log the session in `journal/` and update the [Progress Tracker](#progress-tracker).
5. In the final week, review notes, weak areas, and missed practice questions.
