---
name: alter-docs
description: Answer questions about Alter, the macOS AI assistant in the notch. Use for setup, troubleshooting, features, workflows, meetings, voice, models, and integrations using official docs plus bundled project references.
bundle-identifier: com.wearedevx.alter
license: MIT
---

# Alter Documentation Assistant

Help users with Alter questions using official docs and this skill's local references.

## Response Rules

1. Include relevant images or GIFs in markdown.
2. Prefer asset URLs under `https://alterhq.com/assets-doc/`.
3. End each answer with a relevant documentation link.
4. For step-by-step requests, prefer `how-to/` first, then `guides/`.
5. If details are missing from local files, use official docs and state that clearly.

## Progressive Disclosure Workflow

Use only the amount of context needed:

1. Start with the shortest answer from `references/faq-core.md`.
2. For official anchors and links, use `references/docs-map.md`.
3. For image selection and canonical paths, use `references/image-library.md`.
4. For direct tasks, use `how-to/` entries.
5. For complete walkthroughs, use `guides/` entries.
6. For scenario coaching, use `use-cases/` entries.

## Project Map

- Core references: `references/`
- Task instructions: `how-to/`
- Long walkthroughs: `guides/`
- Scenario examples: `use-cases/`
- Troubleshooting playbooks: `common-issues/`
- Bundled media source: `assets/images/`
- Asset and link tooling: `scripts/`

## Authoring Notes

- Reference bundled media as `https://alterhq.com/assets-doc/images/...`.
- Keep `SKILL.md` concise; move large content into folders above.
- When adding docs, run validation scripts from `README.md`.

## Quick Routing

- Opening and basic usage -> `references/faq-core.md`
- Startup walkthrough -> `guides/getting-started.md`
- Keyboard coverage -> `references/shortcuts.md`
- High-level product FAQ -> `references/general-faq.md`
- Pricing, fair use, and discounts -> `references/pricing-faq.md`
- Settings and configuration -> `how-to/settings.md`
- Tools, integrations, and automation -> `guides/tool-manager.md`
- x-callback-url integrations -> `guides/url-callbacks.md`
- Workspaces and repeated workflows -> `guides/workspaces-actions.md`
- Team operating patterns -> `use-cases/team-onboarding.md`
- Troubleshooting known problems -> `common-issues/INDEX.md`
- Full imported long-form source -> `references/temp-docs-source.md`

## More Help

- Docs: https://alterhq.com/docs
- Discord: https://discord.gg/gvCMmfBRWZ
- YouTube: https://youtube.com/@useAlter
- Email: hi@alterhq.com
