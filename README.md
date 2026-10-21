# anu-agent-test

Engineering **lab target** for [Anu-AI-Agent](https://github.com/Sadhu2005/Anu-AI-Agent).

ANU (the agent) clones this repo, plans work from an operator goal, implements on `agent/*` branches, runs the test matrix (unit → integration → functional → e2e → regression), diagnoses failures, commits, and pushes each verified step. Humans merge to `main` — ANU never force-pushes or auto-merges.

## Operator assign (from Pi / ANU)

```text
Goal: <what to build>
Repo: https://github.com/Sadhu2005/anu-agent-test
Criteria: <acceptance checklist>
```

```bash
python3 /srv/anu/bin/anu-project-assign-v0.1.py \
  --db /srv/anu/brain/anu-brain.db \
  assign \
  --project-key anu-agent-test \
  --github Sadhu2005/anu-agent-test \
  --goal "…" \
  --criteria "…" \
  --autonomous \
  --expand
```

## Local checks

```bash
python -m unittest discover -s tests -q
```

## Branch policy

| Branch | Who |
|--------|-----|
| `main` | Stable baseline (protected) |
| `agent/*` | ANU work branches only |
| `feature/*` | Human experiments |
