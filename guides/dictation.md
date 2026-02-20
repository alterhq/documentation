## Dictation


Alter's dictation capabilities go far beyond simple speech-to-text conversion, offering intelligent voice commands and advanced text transformation features. 

### Voice Triggers

Voice Triggers allow you to activate any Alter Action using speech-to-prompt. Hold your voice hotkey and say a magic word or phrase to instantly trigger your configured actions.

#### How Voice Triggers Work

1. **Set Up Triggers**: In the Action Editor, assign a trigger word or phrase to any Alter Action
2. **Hold to Speak**: Hold your configured hotkey (default: Fn key) or the mic icon
3. **Say the Trigger**: Speak your trigger word or phrase (e.g., "Hey Charlie", "Hey Google")
4. **Release**: Let go of the hotkey - the action fires immediately with the configured settings

#### Practical Examples

- Hold and say **"Hey Charlie"** to start a conversation with your Mental Model expert
- Hold and say **"Hey Google"** to trigger a web search
- Hold and say **"Hey Translate"** to activate your translation action
- Create custom triggers for any of your frequently-used actions

#### Setting Up Voice Triggers

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/Gc9IKXpbSWc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

1. **Open Action Editor**: From the Alter menu, select "Action Editor"
2. **Choose an Action**: Select the action you want to trigger by voice
3. **Add Voice Trigger**: In the action settings, add your trigger word or phrase
4. **Test It Out**: Hold your voice hotkey and say the trigger word to activate the action

#### Best Practices

- **Keep triggers short**: 2-3 words work best for quick recognition
- **Make them unique**: Avoid common phrases you might say in conversation
- **Use clear pronunciation**: Choose words that are easy to say and distinguish
- **Combine with context**: Voice triggers work great with text selections or current app context

> **Note**: Voice triggers use speech-to-prompt (hold to speak), making them perfect for quick voice-activated workflows.

### Modes

#### Speech-to-Prompt (Hold to Speak)
Perfect for quick voice commands and queries:
- **Hold** your configured hotkey (default: Fn key) or mic icon
- Speak your command naturally
- Release to process immediately
- Your text selection or the currently active window is automatically selected for context

#### Dictation Mode (Click to Start/Stop)
Ideal for text input, by default :
- **Click once** on the mic icon to start dictation
- Speak your content
- **Click again** to stop and process
- Perfect for drafting emails, documents, or longer prompts

By default, dictation over 2 minutes is treated as a meeting. If you dictate for longer than that, you can go to Settings > Dictation to change this behavior.


### Voice-Powered Text Transformation

Transform any selected text using voice commands:

1. **Select text anywhere** on your Mac
2. **Hold** the record button (or Fn key)
3. **Speak transformation commands** such as:
   - "Rewrite in friendly tone"
   - "Create counter arguments"
   - "Add my thoughts: [your input]"
   - "Make this more professional"
   - "Translate to Spanish"

This feature works system-wide with any text selection, making it incredibly powerful for editing documents, emails, or any text content.

### Language Settings

#### Automatic Language Detection
When set to "Automatic," Alter detects the language you're speaking and processes it accordingly. Auto-detecting doesn't work with all languages and depends on the underlying engine chosen. Try setting your language if you have accuracy issues or get no results.


#### Custom Word Recognition
Add technical terms, company names, and industry-specific vocabulary to improve recognition accuracy:
- Navigate to **Settings > Dictation > Dictionary**
- Add words separated by commas
- Particularly useful for acronyms, proper nouns, and technical terminology

#### Dictation Replacements

Dictation Replacements allow you to automatically transform words and phrases during dictation and speech-to-prompt. This powerful feature helps you:
- Replace common misspellings or misrecognitions automatically
- Convert abbreviations to full phrases
- Fix frequently mispronounced words
- As a Voice Snippets system

##### How to Set Up Replacements

1. **Open Settings**: Navigate to **Settings > Voice > Replacements**
2. **Add Replacement Rules**: Create pairs of "spoken phrase" → "written text"
3. **Apply Automatically**: Replacements happen at the end of your dictation

##### Practical Examples

- "altair" → "Alter" (fix uncommon words)
- "CTA" → "call-to-action" (expand abbreviations)
- "discord link" → "https://discord.com/xxxx" (replace with a snippet)

##### Use Cases

**Technical Writing**: Replace code-related terms that are often misheard (e.g., "jay son" → "JSON")

**Professional Communication**: Standardize company names, product names, and industry terms

**Personal Shortcuts**: Create voice shortcuts for frequently used phrases or email signatures

> **Note**: Replacements apply to both regular dictation and speech-to-prompt, ensuring consistency across all voice input methods.

### Processing Options

Choose how Alter processes your voice input:

1. **Cloud Processing** - Highest accuracy and fast using cloud-based speech recognition
2. **Local (Apple)** - Uses Apple's on-device speech recognition for privacy
3. **Local (Whisper)** - Uses OpenAI's Whisper model locally for maximum privacy, can be very fast depending on the model chosen
4. **Whisper Pro** - Advanced local processing with 10-second transcripts for meetings of any length

#### Whisper Pro: Real-time Meeting Transcripts

Get complete meeting transcripts in just **10 seconds** regardless of meeting length - whether it's a 5-minute standup or a 3-hour strategy session.

**How to Enable Whisper Pro:**
1. Navigate to **Settings > Dictation**
2. In the **Voice Processor** dropdown, select **"Whisper Pro"**
3. Choose your model (we recommend **Whisper Large V3 626MB** for optimal speed/accuracy balance)
4. Click **Download** and wait for completion


### Configuration

#### Global Voice Hotkey
- **Default**: Fn key
- **Customizable**: Set any key combination in Settings > Dictation > Shortcut
- **Hold behavior**: Speech-to-prompt mode
- **Single tap**: Dictation mode

#### Clipboard Integration
When enabled, dictated text is automatically copied to your clipboard for easy pasting into any application.

---
