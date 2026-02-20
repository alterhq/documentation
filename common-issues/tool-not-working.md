# Issue: Tool Is Enabled But Not Used

## Symptoms

- Tool is enabled in Tools Manager but assistant does not call it.
- Integration appears connected but no tool output appears.

## Likely Causes

- Selected model has weak tool-use support.
- Prompt does not provide required parameters.
- Shortcut or integration input format is incomplete.

## Resolution

1. Verify the tool is enabled in Tools Manager.
2. Switch to a tool-capable model (recommended: Alter Best, Gemini 2.0 Flash, Claude Sonnet).
3. Ask with explicit parameters and expected output format.
4. For Apple Shortcuts, ensure shortcut accepts the assistant output as input.

## Verify

- Run a simple command with required arguments and confirm tool execution output appears.

## Related Docs

- https://alterhq.com/docs#troubleshooting-integrations
