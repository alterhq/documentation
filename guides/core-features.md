## Core Features


### Interacting with Your Apps

#### Appsense - Understanding Your Mac

Unlike traditional screen capture methods, AppSense reads actual data directly from macOS applications, allowing Alter to access information beyond what's visible on your screen.

##### Current Application

Alter will automatically suggest using the active window as context.  
Click **Current Application** below the prompt.
Or press `↓` and `Enter`.

### Follow mode

Follow Mode is a core feature of Alter that enables real-time synchronization of data from your active applications, documents, and files during chat sessions.

#### How It Works

Follow Mode continuously monitors the state of applications and files you're working with, providing Alter with comprehensive context about your current workflow at each turn of your conversation. 

This allows you to work or browse pages and have a conversation always in sync with what you're doing.

A great example is working on a landing page copy: While you make changes and have Alter as your Marketing Coach, Alter sees the changes you made without the need for you to explain what you did.

#### Using Follow Mode

1. Add the applications or documents you wish to include to the context list
2. Start your chat session - Alter will automatically track the state of the selected applications
3. Ask questions, even if that content isn't currently visible on screen
4. Interact with the selected apps or updates the documents
5. Keep chatting, Alter knows what you changed.

### Interacting with Files and Folders

You can add files to Alter as context.

##### Drag-and-Drop Support

Drag and drop files or folders onto The Hub or Alter's notch, or use **Right Click > Add to Alter**.


##### Supported File Types

1. **Document Files**: `.xlsx`, `.docx`, `.pdf`, `.txt`, `.md`, `.org`, `.rtf`.  
2. **Image Files**: `.jpg`, `.png`, `.heic`, `.gif`, `.tiff`, `.svg`.  
3. **Web Content**: `.html`, URLs, dragged text.  
4. **Email Content**: `.eml`, Apple Mail messages.  
5. **Audio Files**: `.mp3`, `.wav`, `.m4a`, `.aac`, `.flac`.  
6. **Code Files**: Common programming languages, configuration, shell scripts.  
7. **Special Handling**: Directory drops, OCR for images and PDFs, text encoding detection.

> When dropping an image file, use a model with vision capability.  

 


##### Video: How to Chat with Files and Folders from Finder

Quick talk about starting conversations with files and folders from the Finder

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/eHZAT-D712Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

### Automatic Transcription

When adding audio or video files, Alter automatically transcribes them for you.

<div class="embed-container" style="margin-bottom: 10px">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/D7y5yuufdUo?si=xeuKKAZ1qCfsl-F6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**Automatic Transcription Features:**
- **Instant Processing**: Audio and video files are transcribed automatically when dragged into Alter
- **Parallel Transcription**: Drop multiple files simultaneously for batch processing
- **Both Audio and Video**: Works with audio files (`.mp3`, `.wav`, `.m4a`, `.aac`, `.flac`) and video files
- **Interactive Content**: Once transcribed, you can ask questions about the content (e.g., "What did Steve say in his speech?")

**How to Use:**
1. Drag and drop your audio or video file(s) onto The Hub or Alter's notch icon
2. Transcription begins automatically - no manual action required
3. View the transcription by clicking on the file in your context
4. Start asking questions about the content immediately

> **Smart Detection**: Audio files dropped into Alter are automatically treated as meeting content, enabling speaker identification and meeting-specific features.

### Workspaces

Workspaces are a powerful feature in Alter that allow you to save, organize, and automatically refresh collections of folders, files, and apps for efficient AI-assisted workflows. Think of workspaces as intelligent folders that maintain context across your chat sessions.

#### How Workspaces Work

Workspaces create an indexed map of your selected resources, enabling Alter to:

- Retrieve only the most relevant files for your queries
- Deliver faster, more accurate responses
- Reduce processing costs
- Handle large folders and codebases efficiently

Workspaces automatically convert files to searchable formats:
- **PDFs**: Converted to markdown with page markers for easy navigation
- **DOCX**: Converted to markdown format
- **XLSX**: Converted to markdown/CSV format
- **Images**: OCR processing extracts text from images
- **Directories**: All files within directories are processed recursively

Audio & videos files are not supported by workspaces yet. Transcribe first by dropping the files into Alter.

All converted files are cached locally for fast access.

#### Editing Files in Workspaces

Workspaces support powerful file editing capabilities through three tools:

**Single Edit**
- Edit or create individual files within your workspace using natural language commands
- Alter can modify code, update documentation, refactor functions, and make targeted changes
- Create new files from scratch or modify existing ones
- Changes are applied directly to your workspace files

**Multi Edit**
- Edit or create multiple files simultaneously across your workspace
- Perfect for refactoring, updating imports, or making consistent changes across a codebase
- Create new files and modify existing ones in a single operation
- Apply changes to related files efficiently

**Bash Tool**
- Execute bash commands within your workspace for advanced file operations
- Run scripts, perform batch operations, and automate complex workflows
- Integrates seamlessly with workspace file management

**Security & Sandboxing**
All editing operations are sandboxed using Seatbelt policies with additional security checks to ensure:
- Safe execution of file modifications
- Protection against unauthorized access
- Controlled file system operations
- Isolation from system-critical areas

> **Note**: Editing capabilities respect file permissions and workspace boundaries. Only files within your workspace can be modified.

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/FlROt-rkg4M?si=BwVnZ6-9FptPRbss" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Creating a Workspace

You can create workspaces from the Hub:

- Open The Hub and navigate to the Workspaces section in the sidebar
- Click the "+" button in the workspace picker to create a new workspace
- Add files and folders using the "Add Files" button in the workspace view

#### Managing Workspaces in the Hub

Workspaces are primarily managed through The Hub's dedicated workspace view:

**Viewing Workspace Details:**
- Click on a workspace in the sidebar to open it in a tab
- View workspace statistics: file count, token estimate, and total size
- See all files and folders included in the workspace

**Editing Workspaces:**
- **Rename**: Double-click the workspace name or use the menu to rename
- **Add Files**: Click "Add Files" to browse and add new files or folders
- **Remove Files**: Click the "×" button on any file to remove it from the workspace
- **Edit Description**: Click the edit icon to add or modify the workspace description
- **Generate Description**: Use the AI sparkle icon to automatically generate a description

**Workspace Actions:**
- **Reindex**: Click "Reindex" to reprocess all files and rebuild the search index
- **Open in Finder**: Click "Open in Finder" to view the workspace directory
- **Delete**: Use the menu to delete a workspace (this action cannot be undone)

#### Workspace Storage

Workspaces are stored locally at:
```
~/Library/Application Support/Alter/Workspaces/
```

Each workspace has its own directory containing:
- Workspace definition file (`.alterworkspace`)
- Files and folders
- Cache directory with converted files (PDFs, DOCX, images, etc.)


#### Video: How to Use Workspaces?

We talk about Workspaces, a feature where you can talk with thousand of folders, files and apps. Here's a video showcasing an Obsidian vault.


<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/HZr7mr-WS3A?si=6dsX2vvQRZ83LtTW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


### Interacting with a YouTube video

When visiting a YouTube video page:  
- Alter will notify you with an option to summarize the video.  
- The video's transcript will be added to your context window, even if you ignore the notification 

> This works only if the Youtube video has a transcribe available

#### Video: How to Chat with YouTube Videos

Quick video showing how to start a chat with a Youtube video using push-to-command or the notch.

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/LkZEH4wqI14" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>



### Alter Actions - Workflows

#### General Principle

Alter Actions are advanced prompts configured with triggers and instructions.  
Default actions are organized in folders.

#### Create Your Actions

You can create actions via:  
- **Action Editor**: Accessible from the menu bar.  
- **Prompt Box**: Invoke "Create > Alter Action" and specify your requirements.

> Built-in actions cannot be edited but can be duplicated.

#### Bespoke Model Selection

You can now assign specific AI models to individual Alter Actions, giving you precise control over which model handles each workflow.

##### Why Use Bespoke Models?

**Privacy-First Workflows**: Use local models for sensitive tasks while keeping cloud models for general queries.

**Specialized Performance**: Assign fast, tool-optimized models like Qwen3 for automation tasks while using creative models for writing.

**Cost Optimization**: Use lightweight local models for simple tasks and reserve powerful cloud models for complex operations.

##### How to Set Up Bespoke Models

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/KqnwL6qEtAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

1. **Open Action Editor**: Click the three dots in the Alter window and select "Action Editor"
2. **Select Your Action**: Choose the Alter Action you want to customize
3. **Access Advanced Settings**: In the action details, find the "Advanced" section
4. **Choose Model**: Select the specific model you want this action to use
5. **Save Changes**: The action will now always use your chosen model

##### Use Cases

**Local Privacy Actions**: Create actions that always use local models for sensitive data processing, even when your default is a cloud model.

**Tool-Optimized Actions**: Assign Qwen3 or other tool-friendly models to actions that interact with your calendar, send messages, or automate workflows.

**Creative vs. Analytical**: Use different models for creative writing tasks versus data analysis or code generation.

**Fallback Strategy**: You can still choose "Best" routing to let Alter automatically select the optimal model for each action.

#### Action-Level Tool Customization

Choose exactly which tools each Alter Action can use, giving you surgical precision over your workflows. This powerful feature allows you to define tools per action for faster execution, better accuracy, and context-aware automation.

##### Why Customize Tools Per Action?

**Faster Execution**: Limit tools to only what's needed, reducing decision overhead and speeding up action completion.

**Better Accuracy**: Prevent the AI from choosing irrelevant tools by restricting available options to only those that make sense for the specific action.

**Context-Aware Automation**: Create specialized workflows where certain actions only have access to specific integrations (e.g., a "Quick Note" action that only uses Notes, while "Project Update" only uses GitHub and Slack).

**Cost Optimization**: Reduce token usage by limiting the tool context sent with each request.

##### How to Customize Tools for Actions

1. **Open Action Editor**: Click the three dots in the Alter window and select "Action Editor"
2. **Select Your Action**: Choose the Alter Action you want to customize
3. **Access Tool Settings**: In the action details, find the "Tools" section under "Advanced"
4. **Choose Specific Tools**: 
   - Select individual tools from your enabled integrations
   - Or disable all tools for actions that don't need them
5. **Save Changes**: Your action will now only use the selected tools

##### Managing Tool Sets

You can create different tool configurations for different purposes:
- **Minimal**: One or two specific tools for laser-focused actions
- **Grouped**: Related tools for specific workflows (all communication tools, all productivity tools, etc.)
- **Full Access**: All tools enabled for general-purpose actions
- **No Tools**: Perfect for creative or analytical tasks that don't need external integrations

> **Pro Tip**: Start with all tools disabled for new actions, then add only what you need. This ensures optimal performance and prevents unexpected tool usage.
