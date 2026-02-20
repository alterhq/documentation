# Issue: Custom Provider Models Not Showing Under Custom

## Symptoms

- API key is entered but no models appear in `/` selector under **Custom**.
- Provider connection does not show as active.

## Likely Causes

- Custom provider toggle is off.
- Endpoint format is invalid (common with Azure).
- API key or API version is incorrect.

## Resolution

1. Open Settings > API keys > Custom provider.
2. Enable Custom Provider and select your provider.
3. Re-enter API key and verify endpoint format.
4. For Azure, use full chat completions URL including deployment and `api-version`.
5. Reopen model selector with `/` and check **Custom** section.

## Verify

- One or more provider models appear under **Custom** in the model picker.

## Related Docs

- https://alterhq.com/docs#using-your-api-key
- https://alterhq.com/docs#external-api-keys
