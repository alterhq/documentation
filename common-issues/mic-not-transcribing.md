# Issue: Mic Input Not Transcribing

## Symptoms

- Holding `Fn` or mic button records nothing.
- Dictation starts but text does not appear.

## Likely Causes

- Microphone permission missing.
- Voice processor not configured or model missing.
- Dictation language and spoken language mismatch.

## Resolution

1. Open Settings > Permissions and ensure microphone permission is granted.
2. Go to Settings > Dictation and confirm voice processor selection.
3. If using local processing, download required model files.
4. Set language explicitly instead of automatic detection if accuracy is poor.
5. Test both modes: hold-to-speak and click-to-dictate.

## Verify

- Hold `Fn`, speak a short prompt, and confirm text appears in the prompt box.

## Related Docs

- https://alterhq.com/docs#dictation
- https://alterhq.com/docs#permissions
