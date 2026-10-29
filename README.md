# Agent Capability Atlas

A decision-grade capability map for engineers moving into **Agent Platform Engineering**, **Agentic AI Engineering**, **Harness engineering**, and adjacent model-system specialties.

**Live site:** https://bing2030.github.io/agent-capability-atlas/

This is a living reference. The HTML is intentionally self-contained and the evidence is reproducible; updates can be made directly in the repository and published through GitHub Pages.

## How it is organised

One capability graph, six views. The graph is the source of truth; every other view is a projection or cross-referenced operating view. Branch codes (A1, B6, C2 …) stay stable wherever you read them, while capability IDs (A1-1, B6-4 …) identify individual leaves.

| View | Answers | Key |
|---|---|---|
| Layers | Where in the runtime does this capability sit, who owns it | L0–L8 |
| Domain forest | Which domain does it belong to, what sits below it | domain → branch → capability → practice → technology |
| Lifecycle | Which stage needs it, what is the exit condition | frame → build → evaluate → release → operate → learn → govern |
| Control plane | Is it data plane or control plane, what primitive is it | plane + platform primitive |
| Autonomy level | How much supervision and governance is required | R0–R4 |
| Role | How deep should someone in this role go | A / B / C × P1–P4 |

Harness is both a cross-cutting lens (03·7) and a first-class branch. The lens explains how a task is organised into deliverable behaviour; the branch **B9 · Harness engineering** (in its own cross-cutting band D10) holds the capabilities for engineering the harness itself — boundary and component contracts, feedforward/feedback controls, making the harness an experiment variable, loop engineering, and bounded self-evolution. Splitting them this way avoids duplicating execution, tooling, context and evaluation capabilities that already exist in A1–A7 and B3.

**Why not two trees.** The original Platform / Agentic split mixed three different axes on one level: job role, system responsibility, and professional maturity ("adjacent" implies secondary). It also split co-owned work — tool contracts (A3) and tool semantics (B5) — into different trees. Capability domains are now the spine; A/B/C survive as a role projection with explicit depth levels. The reasoning and the frameworks that informed it (CNCF platform engineering, NIST AI RMF, ISO/IEC 42001, AWS AgentOps, SFIA, NICE, Anthropic) are documented in section 03·5 of the site.

**Stable capabilities, volatile technology.** The time horizons shown in the atlas are maintenance-planning heuristics, not measured industry half-lives. Technologies are kept in a separate register with a type and an editorial review-priority status (S0 relatively stable / S1 evolving / S2 structurally volatile), so replacing a tool does not invalidate the capability tree.

## What is inside

- **9 capability domains + 2 cross-cutting bands**, 19 branches, 80 capability nodes, 92 registered technologies.
- **Each capability node** carries: what it is, a traditional software-engineering anchor, an example acceptance exercise, key technologies, JD references or an explicit `SRC` marker when the node is derived from primary literature rather than the JD corpus, and primary-source links.
- **Domain forest and coverage matrix** — every branch mapped to its domain and to the target depth (P1–P4) for Platform, Agentic, and Adjacent roles.
- **Operating views** — lifecycle stages with exit conditions, data/control/management plane responsibilities, and autonomy levels R0–R4.
- **Harness lens and branch** — 03·7 covers loop/termination, model/prompt contract, tools/skills, context/memory, execution/recovery, evaluation/telemetry; B9 adds the engineering discipline around the harness itself.
- **Technology register** — 92 entries filterable by type, each tied to a concrete capability ID and through it to a branch and domain.
- **JD evidence** — visibility counts across 25 target roles, with a 22-role core sensitivity view and explicit `BROAD` / `LITERAL` labels.
- **Migration matrix** — 15 traditional SWE capabilities mapped to their Agent-era counterparts with a fidelity rating.
- **Interview signal table** — JD language translated into likely interview questions and the evidence to prepare.
- **Primary-source register** — specifications, official documentation, official engineering posts, and benchmark sources.

## Repository layout

| Path | Purpose |
|---|---|
| `index.html` | Self-contained GitHub Pages site and interactive capability map |
| `assets/agent-capability-atlas.pdf` | Print/offline edition |
| `jd-capability-evidence.py` | Reproducible JD visibility analysis |
| `data/` | Reserved for published evidence snapshots and future dataset artifacts |
| `.nojekyll` | Ensures GitHub Pages serves the static site directly |
| `README.md` | Project overview and maintenance guide |

## Updating the map

1. Edit the content and capability data in `index.html`. The data lives near the bottom of the file:
   - `TREES` — branches and capability nodes;
   - `DOMAINS` — the canonical domain spine (every branch must appear exactly once);
   - `COVER` — target depth per branch per role;
   - `TECH` — the technology register; its third field must be a valid capability ID such as `A3-2`;
   - `SOURCES` — primary sources referenced by key.
2. If the JD corpus changes, rerun the analysis:

```bash
python3 jd-capability-evidence.py /path/to/jd-library.md --pretty
```

3. Update the counts in `EVIDENCE` and the corpus SHA-256 shown in the page.
4. If you change the PDF, replace `assets/agent-capability-atlas.pdf`.
5. Commit and push to `main`:

```bash
git add .
git commit -m "Update capability map"
git push origin main
```

GitHub Pages is configured to deploy from the repository root on the `main` branch, so a push is enough; there is no build step.

## Evidence boundary

The chart measures **JD visibility**, not mandatory-requirement frequency, market share, or salary impact. It is based on a targeted 25-role sample, not a random market census. Broad regex families are labeled separately from literal terms. Example acceptance criteria are learning and portfolio exercises; production release gates must be calibrated to task risk, sample size, and business SLOs.

The JD corpus itself is not included in this repository. The analysis script, source file hash, and aggregate evidence are retained so the method can be audited and rerun when the corpus is available.

## Maintaining the site

- **Add capability before technology.** A new tool goes into `TECH`. Only change `TREES` when a technology alters what the capability *is* — for example, a genuinely new isolation primitive.
- **Every branch needs exactly one domain.** The forest and the coverage matrix are generated from `DOMAINS`; a missing or duplicated branch breaks both.
- **Keep capability IDs stable.** `A3-2` means branch A3, capability 2. Do not renumber existing capabilities when inserting content; append new IDs or explicitly migrate every register reference.
- **Validate every technology mapping.** Every `TECH` row must point to an existing capability ID, not merely a branch. Its domain is derived through that capability.
- **Declare where a node comes from.** If a capability is derived from primary literature or engineering practice rather than the JD corpus, set its JD field to `—`. The renderer shows `SRC` in the tree and "来源驱动" in the reference line, so no reader mistakes it for a JD citation.
- **Depth, not ownership, expresses importance.** If a field matters to a role, raise its level in `COVER` rather than giving it its own tree.
- Keep protocol and framework claims tied to primary sources; these facts change quickly.
- Record the source date when adding version-sensitive material.
- If a source cannot be fetched by a script but loads in a browser (ISO, SFIA), say so rather than implying it was automatically verified.
- Preserve the distinction between capability (stable) and technology (replaceable).

## Repository

https://github.com/Bing2030/agent-capability-atlas
