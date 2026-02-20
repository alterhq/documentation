## Meetings


Alter provides professional-grade meeting transcription with advanced features like speaker identification, searchable transcripts, and 100% offline processing.

### Automatic Meeting Recording

#### Smart Meeting Detection
Alter automatically detects when you join meetings on:
- **Zoom**
- **Google Meet** 
- **Microsoft Teams**
- **Other conferencing platforms**

During online calls, Alter suggests recording via a subtle notification.

When a meeting is detected, Alter displays a notification giving you the option to record or skip.

#### Auto-Record Settings
- **Enable**: Settings > Dictation > Auto Record Meetings
- **Meeting Threshold**: Define minimum recording length (default: 120 seconds)
- **Notification**: Option to skip recording if notification appears
- **Keep Awake During Recording**: Prevent your Mac from sleeping during long meetings (Settings > Voice > Keep Awake)

#### Keep-Awake Functionality

When enabled in **Settings > Voice**, Alter prevents your Mac from going to sleep during meeting recordings:
- **Automatic activation**: Engages when you start recording a meeting
- **Screen stays active**: Ensures uninterrupted recording for long meetings
- **Battery consideration**: Automatically releases when recording ends
- **User preference**: Can be toggled on/off based on your needs

This is particularly useful for:
- Long conference calls or webinars
- Presentations where screen sleep would interrupt the recording

Navigate to Alter's settings and select the "Dictation" tab to find the "Auto Record Meetings" toggle. Once enabled, Alter will automatically detect when you join meetings. When you enter a meeting, Alter will display a notification giving you the option to skip recording. If you do nothing or click the X on the notification, the meeting will be recorded automatically.

![Auto-Record](https://alterhq.com/assets-doc/images/meetings/auto-record.webp)

#### Manual Recording
You can also manually start and stop meeting recordings:
- **Start recording**: Click the mic icon on the notch. It will turn into a red recording button  
- **End recording**: Click the red button to stop

> The mic will animate during transcription

#### Speaker Search & Identification

Alter uses **Pyannote 4 (Community-1)**, the latest state-of-the-art open-source model for speaker diarization, providing industry-leading speaker identification accuracy.

- **Perfect speaker identification** for all meeting participants using cutting-edge AI
- **Search by speaker**: Find specific contributions from any participant
- **Speaker-specific insights**: Track who said what throughout the meeting
- **Filter speakers**: Focus on specific participants for faster identification
- **Manual speaker renaming**: Correct or customize speaker names as needed
- **100% offline processing**: All speaker identification happens locally on your Mac for maximum privacy

#### Fast Transcription with Whisper Pro
- **10-second transcripts**: Complete meeting transcription in just 10 seconds, regardless of meeting length
- **Local processing**: All transcription happens on your device for maximum privacy
- **Cloud regeneration**: Option to regenerate any transcript using cloud processing for enhanced accuracy
- **Perfect for productivity**: Ideal for back-to-back meetings and high-volume meeting days

### Live Captions

Live Captions brings real-time transcription to every app on your Mac. Like YouTube subtitles, but system-wide—watch captions appear instantly during meetings, podcasts, videos, or any audio playing on your computer.

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/TrSX-tNB0yo?si=JbUvbuvO5OXYMvtn" title="Live Captions on macOS" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### How It Works

Live Captions displays transcribed text in real-time as audio plays through any application:
- **Universal compatibility**: Works with Zoom, Google Meet, Teams, Safari, podcasts, streaming services, and any Mac app
- **Real-time display**: Captions appear instantly as words are spoken
- **Automatic language detection**: Recognizes and transcribes multiple languages automatically
- **100% local processing**: All transcription happens on your Mac for complete privacy
- **Customizable display**: Adjust caption appearance and positioning to your preference

#### Using Live Captions

**Toggle On/Off**
- **Keyboard shortcut**: Press `cmd+shift+↓` to show or hide captions
- **Quick access**: Toggle captions anytime during audio playback

**Requirements**
To use Live Captions, you'll need:
1. Navigate to **Settings > Voice**
2. Select **Local Pro** as your voice processor
3. Download the **Parakeet V3** model (recommended for optimal performance)

#### Practical Use Cases

Live Captions is particularly useful for:
- **Meetings and calls**: Follow along with real-time subtitles during video conferences
- **Video content**: Watch YouTube, streaming services, or recorded videos with live transcription
- **Podcasts and audio**: Read along while listening to podcasts or audio content
- **Accessibility**: Essential for deaf and hard-of-hearing users, or in sound-sensitive environments
- **Language learning**: See transcriptions while practicing listening comprehension
- **Note-taking**: Capture key points visually while audio plays

> **Privacy Note**: Live Captions runs entirely on your device using Local Pro processing. No audio is sent to external servers.

### Edit And Search Transcripts

#### Edit Transcript Content
- **Modify transcriptions**: Correct any recognition errors
- **Edit titles**: Rename meeting transcripts for better organization
- **Update summaries**: Customize meeting summaries to highlight key points

#### Advanced Search Capabilities
Search across all your transcripts by:
- **Titles**: Find meetings by name
- **Content**: Search within transcript text
- **Speakers**: Find contributions from specific participants
- **Summaries**: Search meeting summaries and key points

### Timestamps Navigation

#### Enhanced Navigation
- **Timestamp support**: Jump to specific moments in recordings
- **Visual timeline**: Navigate through long recordings efficiently
- **One-click audio navigation**: Click timestamps to hear specific segments

#### Meeting Reports & Analysis
Generate comprehensive meeting reports with:
- **Action items**: Automatically extracted tasks and follow-ups
- **Key decisions**: Important conclusions and agreements
- **Speaker contributions**: Summary of each participant's input

### Video Demonstrations

#### Real-time Meeting Transcripts with Whisper Pro

Learn how to get complete meeting transcripts in just 10 seconds using Whisper Pro:

<div class="embed-container">
    <iframe src="https://www.youtube.com/embed/tuLA4zfA20Y?si=c7wZxQR5tdhutbGS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Speaker Search And Editable Transcripts

Learn about Alter's advanced transcription features with 100% offline processing:

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/WXuiN3QHDJs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Perfect Speaker Identification

See how Alter identifies and tracks different speakers in your meetings:

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/YIMhbVgtGvk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

### Accessing Your Transcripts

#### File Location
All recordings and transcripts are stored locally at:
`~/Library/Application Support/Alter/Transcripts`

You can directly open the folder by going into your Settings > Dictation.

All your transcripts are also available directly in Alter.

#### Transcript Management
- **Open in Finder**: Access transcript files directly
- **Search interface**: Use Alter's built-in search to find transcripts
- **Export options**: Save or share transcripts as needed

#### Recovery Options
In case of unexpected app closure during recording, audio files can often be recovered from:
`/private/var/folders` (search for files named "recording")

> You can find your recordings and your transcripts in `~/Library/Application Support/Alter/Transcripts`

> In the case Alter crashes, there is a fair chance you could find the audio file in the following folder: `/private/var/folders` and search for files called "recording"

### Smart Notifications

#### Meeting Context Awareness
Alter provides intelligent suggestions based on your meeting activity:
- **Start recording prompt** when joining meetings
- **Generate meeting report** when stopping long recordings
- **Action item extraction** for follow-up tasks

#### Productivity Enhancements
- **Meeting summaries**: Automatic generation of key points
- **Action item tracking**: Extract and organize tasks from discussions
- **Follow-up reminders**: Integration with calendar and task management

---
