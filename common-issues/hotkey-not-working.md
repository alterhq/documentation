# Issue: Quick Access Hotkey Not Working

## Symptoms

- Pressing `Alt+Space` does not open Alter.
- Voice hotkey may still work but quick menu does not.

## Likely Causes

- Hotkey changed in settings.
- Another app is using the same shortcut.
- Alter window state or permissions are blocking global capture.

## Resolution

1. Open Settings with `Cmd+,` while Alter is visible.
2. Go to Defaults and confirm the **Open notch keybinding**.
3. Test a different key combo that is not used by other apps.
4. Check **Settings > General > Quick Access** for the Alter Quick Menu shortcut.
5. Retry after closing other launcher apps that capture global shortcuts.

## Verify

- Press your configured quick access shortcut and confirm Alter opens from any app.

## Related Docs

- https://alterhq.com/docs#hotkey-alter-quick-menu
- https://alterhq.com/docs#defaults
