## Alter Settings


The Alter settings window provides comprehensive control over the application's functionality, appearance, and integration capabilities. 

### Accessing Alter Settings

When the Alter window is visible


1. Use the keyboard shortcut when the Alter window is open:  `cmd+,`

or 

2. click on the 3 dots on the main window /

![Alter Settings entry](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/34087cbe-ebfe-44d9-ad98-e3f66d372373/Settings_three_dots.png?t=1740498938)

When the Alter widow is not visible 

Access it via the menu bar

![Alter Settings Menu Bar](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/edb04338-d416-42b0-a0d0-fa17bc288c1d/image.png?t=1740499174)

Here's a detailed breakdown of each section

### Defaults

![Alter Settings Defaults](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/12283a80-42d2-4b7e-a3f6-bb98c09af825/Alter_Settings_Default.png?t=1740500278)

Quick access settings:

- Open notch keybinding (default: `Alt+Space`)
- Selection Button toggle for quick access when selecting text

LLM settings:
- Max Tokens: Set maximum text generation length (default: 2,048)
- Temperature: Adjust from deterministic to creative (default: 0.70)

### Dictation 

![Dictation Settings](https://alterhq.com/assets-doc/images/settings/dictation.webp)


#### Shortcut

**Global Keybinding**
Set a custom keyboard shortcut to trigger Alter's voice features. If left empty, the Fn key will be used by default.

**Behavior:**
- **Hold** - Activates speak-to-command mode
- **One tap** - Starts dictation mode

**Record Shortcut**
Click "Record Shortcut" to capture your preferred key combination.

#### File Management

**Transcripts Directory**
Access your saved transcriptions and recordings through Finder. Click "Open in Finder" to navigate directly to where Alter stores your voice data.

#### Language

**Dictation Language**
Set the primary language for voice recognition and transcription. When set to "Automatic", Alter will attempt to detect the language being spoken.

**Note:** All voice features will use this language setting for processing transcriptions, including meetings.

#### Automation

**Auto Record Meetings**
When enabled, Alter automatically starts recording when it detects you're in a meeting.

**Meeting Threshold**
Define how long a recording must be (in seconds) before Alter considers it a meeting rather than a quick voice note. Default is 120 seconds (2 minutes).

**Keep Dictation in Pasteboard**
When enabled, dictated text is automatically copied to your clipboard/pasteboard, making it easy to paste into any application.

#### Dictionary

**Custom Word Recognition**
Add words that you want Alter to better recognize during transcription. This is particularly useful for:
- Technical terms specific to your industry
- Company names and product names
- Proper nouns that might be misunderstood
- Acronyms and abbreviations

**Format:** Enter words separated by commas in the text field.

#### Processor

**Speech Processing Engine**
Choose how Alter processes your voice input:

1. **Cloud** - Uses cloud-based processing for highest accuracy
2. **Local (Apple)** - Uses Apple's on-device speech recognition
3. **Local (Whisper)** - Uses OpenAI's Whisper model locally for privacy
4. **Whisper Pro** - Advanced local processing with 10-second transcripts for meetings

---

*These settings help you customize Alter's voice recognition and automation features to match your workflow and preferences.*

### Profile 

![Alter Settings Profile](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/cecd74bb-f332-4c17-a8e1-f71cb35cabff/Alter_Settings_Profile.png?t=1740500288)

Profile is a simple way to tell Alter who you are and how you want to work together. Context matters - when Alter knows more about you, it can skip the fluff and provide more helpful, targeted responses.

**My Profile:**
Use this personalization section to:
- **Tell Alter about yourself**: Share your role, expertise, and background
- **Share what you're working on**: Describe your current projects and goals  
- **Set your preferred communication style**: Specify how you like to receive information
- **Add explainers for tools**: Detail how you want some tools to be used and provide technical references if needed (pairs of names and ids for example)

**Why Profile Matters:**
When Alter knows you're a developer who prefers concise technical answers, or a writer who wants creative brainstorming, it can adapt its responses accordingly. This personalization helps Alter understand your context and provide more relevant assistance.

Here's a simple example:

```
My name is Samuel ROY, I'm the CEO of Alter, an AI assistant that understands your Mac. It's the first AI assistant living in the macOS notch.  I bring vision and manage product development, I can code and do marketing tasks. I like my AI to output content in a genuine, friendly and direct tone. Humor and Internet culture is appreciated. 

When you use tools, you might need the following informations:
<DISCORD>
Guild ID: XXXXXXX
General channel: general
Private team channel: XXXXX
</DISCORD>

<GITHUB>
Alter app repo: XXXXX
Alter server: XXX
Alter website (alterhq.com): XXXX
</GITHUB>

```


- Generation Language: Select preferred language for outputs
Note: Language selection affects generation only, not application interface

### Appearance 

![Alter Settings Appearance](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/6e65f7b5-25c2-47c8-845e-89bf718b1abc/Alter_Settings_Appareance.png?t=1740500298)


Theme options:
- System (follows system settings)
- Light mode
- Dark mode
Panel customization:
Default Panel Position (e.g., top center)

Menu Font size (default: 16)
Message Font size (default: 16)

Display notch toggle

### Billing 

![Alter Settings Billing](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/edd5417c-3ed3-4246-bac5-1001a9bc2b3b/Alter_Settings_Billing.png?t=1740500310)

### Permissions 

![Alter Settings Permissions](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/8cb8d416-48c5-491d-a551-3d894ae6e339/Alter_Settings_Permissions.png?t=1740500332)


- **Launch at Login**: Toggle switch to control whether Alter starts automatically when the system boots up

#### Required Permissions

Alter will work at best when those permissions are enable

- Accessibility permissions
   - Purpose: Used to get selected text system-wide and to paste text anywhere
   - Status: OK
   - Action button: "Check Accessibility"

- SystemEvents permissions
   - Purpose: Used to interact with other applications
   - Status: OK
   - Action button: "Check SystemEvents"

- Screen Recording permissions
   - Purpose: Used to capture screen content
   - Status: OK
   - Action button: "Check Screen Recording"

- Microphone permissions
   - Purpose: Used to record audio input
   - Status: OK
   - Action button: "Check Microphone"

#### Disable analytics

We rely on analytics to improve Alter. However you are free to disable it if you prefer it

- **Disable Analytics**: Toggle switch to control analytics collection


### External API keys

This is where you want to set up your API keys if you are using your own providers, for example, OpenAI, OpenRouter, or your local models. 

![Alter Settings API keys ](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/04aeef75-fa11-463d-849c-dce8925060c2/Alter_Settings_API_keys.png?t=1740500354)

Partners integration:
- Straico support
- Custom provider options



![Alter Settings API keys on](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/4a22f3fb-ad9e-4f50-8184-1e5cc5238118/Alter_Settings_API_key_custom_provider_on.png?t=1740500360)

Provider configuration:
- Enable/disable custom providers

Provider selection (e.g., LM Studio)

List of providers:
- LM Studio
- Mistral
- Ollama
- OpenAI
- Open Router
- Custom (any OpenAI compatible endpoind)

![Alter Settings API keys choice error](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/63a88122-9032-460b-a2b8-24c4ae5b7ba4/image.png?t=17404994540)



![Alter Settings API keys choice right](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/a3cb944c-7379-49a6-9349-c829bcda071b/image.png?t=1740499713)

![Alter Settings API keys on](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/4a22f3fb-ad9e-4f50-8184-1e5cc5238118/Alter_Settings_API_key_custom_provider_on.png?t=1740500360)

### Router

Alter can be used as a gateway to provide its cloud models to other tools in the same manner than OpenRouter. 

![Alter Settings Router](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/bcb31c63-4c7b-492f-a057-b5ddf7a1d87d/Alter_Settings_Router.png?t=1740500161)

---
