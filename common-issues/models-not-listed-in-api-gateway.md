# Issue: Models Not Listed In API Gateway Client

## Symptoms

- External app connects to Alter API but model list is empty.
- Requests fail unless model is manually typed.

## Likely Causes

- Client does not fully support model listing endpoint.
- Model name format is not set to `Provider#Model-name`.

## Resolution

1. Set base URL to `https://alterhq.com/api` or `https://alterhq.com/api/v1`.
2. Enter your generated Router API key.
3. Manually set a model in `Provider#Model-name` format.
4. Retry request in chat completions mode.

## Verify

- A completion request succeeds with a manual model id like `OpenAI#gpt-4o-mini`.

## Related Docs

- https://alterhq.com/docs#overview
