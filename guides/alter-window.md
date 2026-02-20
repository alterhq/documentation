## The Alter Window


### General Concept

Alter provides two main interfaces for interacting with AI:

1. **The Hub**: The main window interface with tabs, sidebar, and comprehensive workspace management (see [Hub section](#The Hub---the-centralized-workspace) below)
2. **Quick Panel**: The lightweight floating panel accessible from the notch or hotkey

Both interfaces share core functionality but serve different use cases:
- **Hub**: Best for extended conversations, workspace management, and multi-tasking
- **Quick Panel**: Perfect for quick queries and voice commands

### Hub Interface

Thr Hub is divided into three main sections:

1. **Sidebar**: Navigation for conversations, workspaces, transcripts, and more
2. **Main Content Area**: Tabbed interface showing active conversations, workspaces, or other content
3. **Input Area**: Prompt box and context management

You can navigate within The Hub using a mouse or keyboard shortcuts (see the [Shortcuts](#shortcuts) section).

### Quick Panel Interface

The quick panel (accessible from the notch) is divided into three main sections:

1. **Context**
2. **Prompt**
3. **Additional Selection**

You can navigate within the quick panel using a mouse or the following keyboard keys:
- `←`, `↑`, `→ `, `↓`  to navigate between objects.
- `Enter` to select an object.

> See the **Prompt Box** section for details on manipulating it using keyboard keys.


### The Context Section

The **Context** section displays elements sent to Alter for reference.

You can send multiple context elements to Alter and mix different types, including:
- Files
    - Any files supported
    -  Emails
- Text selection
- Audio Transcripts
- Youtube transcripts
- Folders
- Workspaces
- Applications
- Web pages

You can use the following key strokes to manipulate your context selection in The Hub: 
- `←`, `↑`, `→`, `↓`: navigate between contexts
- `Space Bar`: add/remove selected context(s)
- `Cmd+K`: remove all contexts from the active conversation

#### Using your clipboard

You can paste the content of your clipboard `Cmd+v` to automatically add it to Alter's context.


### The Prompt Box

The **Prompt Box** is where the magic happens.  
Start typing your prompt or an Alter Action title to send it to your LLM model.


- Use `Enter` to prompt with your actif model.  
- Use `Cmd+Enter` to prompt using a web search (via Gemini web).
- Use `Shift+Enter` to do a line break.

> To invoke an Alter Action, type any character in its title.  

Prompt Box shortcuts:
- `@`: Add elements to the context.  
- `#`: Show your history of Alter Conversation.
- `>`: Show your history of meeting transcriptions.
- `/`: List and choose your model.
- `?`: Show the help menu.

#### Help menu


![Help me menu](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/5c14ac40-d9bd-4912-bf57-85f853ad441d/image.png?t=1741473617)


### Conversation Windows

#### Resizing Conversation Windows

You can now fully customize the size of your conversation windows to fit your workflow:

- **Width Adjustment**: Drag the edges of the conversation window horizontally to make it wider or narrower
- **Height Adjustment**: Drag the edges vertically to make the window taller or shorter
- **Flexible Layout**: Resize to fit alongside other applications for multitasking
- **Persistent Settings**: Your preferred window size is remembered for future conversations

This feature is particularly useful when:
- Working with side-by-side applications
- Reviewing long conversations or documents
- Sharing your screen during presentations
- Using Alter on different display configurations

#### Continuous Speech-to-Prompt

You can continue interacting with your last active conversation window using only your voice:

1. **Hold your voice hotkey** (default: Fn key) or mic button
2. **Speak your prompt** naturally
3. **Release** to send to your existing conversation
4. **Keep conversing** - each voice prompt adds to the same conversation thread

This creates a seamless hands-free experience where you can have extended voice-only conversations without touching your keyboard or mouse.


### The Hub - The Centralized Workspace

The Hub is Alter's main window interface that provides a comprehensive workspace for managing conversations, workspaces, transcripts, and more. It features a modern tab-based interface with a sidebar for easy navigation.

#### Key Features

- **Tabbed Interface**: Manage multiple conversations, workspaces, transcripts, and calendar events in separate tabs
- **Sidebar Navigation**: Quick access to conversations, workspaces, transcripts, and scheduled jobs
- **Drag and Drop**: Drop files, folders, or text directly onto The Hub to add them as context
- **Inspector Panel**: View and manage conversation details, context, and settings
- **Workspace Management**: Create, edit, and manage workspaces directly from The Hub

#### Opening The Hub

You can open The Hub by:
- Using your Alter Hub shortcut (default: `Shift+CMD+H`)
- Selecting "Open The Hub" from the menu bar
- Opening a conversation link from a floating conversation

#### Keyboard Shortcuts

The Hub supports powerful keyboard shortcuts for efficient navigation:

- **`Cmd+B`**: Toggle sidebar visibility
- **`Cmd+W`**: Close the active tab
- **`Cmd+Option+→`**: Switch to the next tab
- **`Cmd+Option+←`**: Switch to the previous tab
- **`Cmd+K`**: Clear all contexts from the active conversation
- **`Cmd+Backspace`**: Delete the active conversation

#### Tab Types

The Hub supports different types of tabs:

- **Conversations**: Chat sessions with AI models
- **Workspaces**: Collections of files, folders, and apps for context
- **Transcripts**: Meeting transcriptions and recordings
- **Calendar Events**: Scheduled meetings and events
- **Scheduled Jobs**: Automated tasks and workflows

#### Managing Contexts in The Hub

- **Add Context**: Drag and drop files, folders, or text onto The Hub, or use the `@` shortcut in the prompt box
- **Select Context**: Use arrow keys (`←`, `↑`, `→`, `↓`) to navigate between contexts
- **Clear All**: Press `Cmd+K` to remove all contexts

#### Inspector Panel

The Inspector panel provides detailed information and controls:

- **Conversation Details**: View conversation metadata, export options, and sharing links
- **Context Management**: See all contexts in the current conversation
- **Workspace Information**: View workspace statistics, files, and settings

Toggle the Inspector panel using the sidebar icon in the toolbar or by clicking the inspector button.

### Conversation History

#### Managing Your Chat History

Access your conversation history by typing `#` in the prompt box or using the history feature in The Hub's sidebar.

![History with tags](https://alterhq.com/assets-doc/images/other/history-tags.webp)

**Rename Conversations**

You can rename a conversation by right-clicking an entry in the list. A contextual menu will appear, choose `Rename`

Tip: you can add tags like `#personal` to categorize chats and search quickly for all conversations matching one or more tags within the promptbox. 

For example, typing the text below in the box, will search for `#personal` and `#food`:

```
# #personal #food
```

**Export Conversations**

You can now export entire conversations as markdown files for reuse with other tools or for documentation purposes. Just like `Rename` invoke the contextual menu by right-cliking a line:

1. **Select Conversation**: Find the conversation you want to export
2. **Right-Click**: Right-click on the conversation
3. **Export**: Select the "Export" option
4. **Save**: Choose where to save your markdown file
