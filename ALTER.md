# ALTER.md

Rules for AI agents contributing to this repository.

## 1) First Principles

- Follow progressive disclosure.
- Keep `SKILL.md` short and routing-focused.
- Put detailed content in `references/`, `how-to/`, `guides/`, `use-cases/`, and `common-issues/`.
- Do not invent product facts. If unsure, mark as needing verification.

## 2) Content Placement

- `references/`: stable canonical information and FAQs.
- `how-to/`: short task instructions.
- `guides/`: full walkthroughs.
- `use-cases/`: scenario playbooks.
- `common-issues/`: symptoms, causes, fixes, verification.

When adding a new file, update the relevant `INDEX.md`.

## 3) Assets And Links

- Bundle media under `assets/images/...`.
- In docs, reference media with `https://alterhq.com/assets-doc/...`.
- Keep `assets/manifest.csv` updated for downloaded media.

Before finishing, run:

- `python3 scripts/check_links.py`
- `python3 scripts/check_assets.py`

Optional stricter checks:

- `python3 scripts/check_links.py --check-external-media`
- `python3 scripts/check_assets.py --fail-on-orphans`

## 4) Writing Quality

- AI-assisted content is welcome, but must be fact-checked.
- Avoid low-signal filler or repetitive "AI slop".
- Keep answers digestible and useful for the community.
- External resources (social posts, YouTube, personal blogs) are allowed when clearly relevant.

## 5) Templates And Naming

- Use folder templates prefixed with `_`, for example `_TEMPLATE.md`.
- Keep filenames descriptive and kebab-case.

## 6) Commits

Use [Conventional Commits](https://www.conventionalcommits.org/).

Examples:

- `docs(guides): add callback integration examples`
- `fix(common-issues): clarify device-limit troubleshooting`
- `chore(assets): add callback screenshot to manifest`
