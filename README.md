# Agent Capability Atlas

A decision-grade capability map for engineers moving into **Agent Platform Engineering**, **Agentic AI Engineering**, **Harness engineering**, and adjacent model-system specialties.

**Live site:** https://bing2030.github.io/agent-capability-atlas/

This is a living reference. The HTML is intentionally self-contained and the evidence is reproducible; updates can be made directly in the repository and published through GitHub Pages.

## What is inside

- **Two core tracks** — Agent Platform Engineering and Agentic AI Engineering — plus three adjacent specializations: model serving/inference, post-training/Agentic RL, and product/organizational leadership.
- **18 branches and 75 capability nodes**, each with:
  - what the capability is;
  - a traditional software-engineering anchor;
  - an example acceptance exercise;
  - key technologies;
  - related JD references and primary-source links.
- **Harness lens** — loop/termination, model/prompt contract, tools/skills, context/memory, execution/recovery, and evaluation/telemetry.
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

1. Edit the content and capability data in `index.html`. The capability trees, evidence rows, and source register are defined near the bottom of the file.
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

- Keep the title and metadata in `index.html` current.
- Keep protocol and framework claims tied to primary sources; these facts change quickly.
- Record the source date when adding version-sensitive material.
- Prefer adding a capability node or a source over adding a generic claim.
- Preserve the distinction between Platform responsibilities, Agentic behavior, and adjacent model-system work.

## Repository

https://github.com/Bing2030/agent-capability-atlas
