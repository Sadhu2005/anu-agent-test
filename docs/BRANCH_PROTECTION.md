# Branch protection checklist (anu-agent-test)

Apply in GitHub → Settings → Branches → `main`:

- [ ] Require a pull request before merging
- [ ] Require status checks to pass (`ci` / test job)
- [ ] Restrict force pushes
- [ ] Restrict deletions
- [ ] Do **not** allow ANU (or bots) to push directly to `main`

ANU only pushes `agent/*`. Humans merge PRs.
