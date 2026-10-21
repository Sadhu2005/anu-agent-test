# Agent conventions (anu-agent-test)

- Work only on `agent/<goal-id>-*` branches.
- Never commit to `main`. Never force-push. Never merge without human approval.
- Before each push: run applicable test layers (unit, integration, functional, e2e, regression). Skip missing layers with explicit SKIPPED evidence — do not claim pass.
- On test failure: write `.anu/DIAGNOSIS.md`, replan, repair within retry budget, then re-run the failed layer.
- Prefer small, reviewable commits with evidence in the message (`tests: unit=ok …`).
- Do not commit secrets, `.env`, API keys, or model weights.
- Persist progress in `AUTONOMY_PROGRESS.md` (written by ANU) and brain checklist evidence.
