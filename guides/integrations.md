## Integrations


Alter connects seamlessly with your Mac applications and external services to enhance your productivity. All local integrations are completely **FREE** and work offline, keeping your data private and secure.

### Local Tools

Alter provides 17+ powerful local tools for free that integrate directly with your Mac applications. Unlike other AI chatbots, Alter actually controls your Mac through natural language commands.


#### How to Use Local Tools

1. **Availability For FREE**: All local tools are available to everyone for free
2. **Tools Manager**: Open Alter menu and click on `Tools Manager`
3. **Enable one or more tools**: In the `Local Tools` section, search and enable the tools you're looking for, like Apple Calendar or Apple Maps.
4. **Natural Commands**: Simply ask Alter to perform actions with your apps
   - "Send a message to John saying I'm running late"
   - "Add a meeting to my calendar for tomorrow at 2 PM"
   - "Show me my unread emails"
   - "Find the contact for Sarah"

5. **Privacy First**: All local tools work offline and keep your data on your Mac

> **Note**: You can toggle all tools on/off using the global toggle in the tool window (Settings > Tools).

#### Video Demonstration

Learn about the 17 powerful automation features including Messages, Calendar, Maps, and Contacts:

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/qL9iiHihYOU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Core Mac Applications List

1.  **Productivity & Organization**
    *   Notes: access and manage your notes
    *   Reminders: manage your reminders
    *   Calendar: create, edit, remove and list events
    *   Finder: list and open apps
2.  **System & Automation**
    *   Alter: use Quick Actions as tools, copy to clipboard and other expert use cases.
    *   System Settings: send a system notification
    *   Shortcuts: call your Apple Shortcuts using the last AI reply as entry
    *   Script Editor: run an Apple Script
3.  **Web & Navigation**
    *   Maps: search for places and addresses, get directions and points of interest
    *   Safari: web search powered by DuckDuckGo
4.  **Communication**
    *   Contacts: Manage and search your contacts
    *   Mail: Draft emails
    *   Messages: Send messages

### Connect with 2000+ Services

Alter can also connect with over 2000 external applications and services like Linear, Notion or Google services (Gmail, Calendar) for advanced automation workflows.

> **Availability**: Early preview for Yearly and Lifetime users


#### Video: Connect Alter with WhatsApp & thousands of Apple Shortcuts

See how to connect Alter with Apple Shortcuts, webhooks, WhatsApp, Make, N8N, Relay, and Zapier:

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/ltYMIKf6nV8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

#### Popular integrations:

- **Notion**
- **OpenAI**
- **Anthropic**
- **Google Sheet**
- **Telegram**
- **Google Drive**
- **Google Calendar**
- **Slack**
- **Salesforce**
- **HubSpot**
- **Zoho CRM**
- **GitHub**
- **YouTube**
- **And 2000+ more applications**

### Automation Workflows

#### Webhooks
- Set up webhook integrations for custom workflows
- Connect Alter with any webhook-compatible service
- Trigger external actions from Alter conversations

#### Apple Shortcuts Integration
- Connect with thousands of Apple Shortcuts
- Trigger Shortcuts from Alter using natural language
- Automate complex Mac workflows through Shortcuts

#### Quick Actions
Create custom actions that work with your integrations:
- **Insert Quick Action**: Automatically place AI replies into active apps
- **Webhook Actions**: Send data to external services
- **Apple Script Integration**: Run custom AppleScripts
- **Form Builder**: Create interactive forms with variables

**Auto-Insert AI Replies & Custom Forms**

See the Insert Quick Action and Form Builder features in action:

<div class="embed-container">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/m2i7PC7n9JE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

### x-callback-url Integration

Alter supports the [x-callback-url](https://x-callback-url.com/) protocol, allowing you to automate workflows and integrate Alter with hundreds of Mac apps that support custom URL schemes.

#### What is x-callback-url?

x-callback-url is a standard for inter-app communication on Apple platforms. It lets apps trigger actions in each other using special URLs, optionally passing data and returning to the original app when done. This enables powerful automations and integrations between Alter and your favorite tools.

#### How to Use x-callback-url with Alter

**1. Triggering Alter Actions from Other Apps**
- In the Alter Action Editor, select an action and find the "URL Callback" section under "General".
- Copy the provided `alter://` URL scheme for that action.
- Use this URL in any app that supports launching URLs (Shortcuts, Notes, browser, etc.) to trigger the Alter action directly.


**Example:**
(Click to try) 
[alter://action/ask-web?input=What+is+Alter+MacOS](alter://action/ask-web?input=What+is+Alter+MacOS)
```
alter://action/ask-web?input=What+is+Alter+MacOS
```
This URL if paste to a new browser tab or clicked as a link will open Alter and runs the "Ask Web" action with your input.


**2. Triggering Other Apps from Alter**
- Create a clickable link in Alter using the target app's URL scheme (e.g., `bear://`, `things://`, etc.).
- Clicking the link in Alter will launch the other app and perform the specified action.

**Example:**
```
bear://x-callback-url/create?title=Demo%20Note
```
This creates a new note in Bear titled "Demo Note".

#### Practical Use Cases
- Launch an Alter action from a calendar event, note, or automation app.
- Create links in Alter that open notes, tasks, or documents in other apps.

#### Supported Apps
Many popular apps support x-callback-url, including Bear, Things, Drafts, OmniFocus, 1Writer, Agenda, and more. For a comprehensive list and links to documentation, see the [Alter Callback URLs Guide](/blog/alter-callback-urls-guide).

#### Troubleshooting
- Double-check the URL scheme and parameters for the target app.
- Encode special characters in URLs.
- Make sure the app supports the action you want to trigger.

> For more detailed examples and troubleshooting, see the [full guide](/blog/alter-callback-urls-guide).


### Setting Up Integrations

#### Accessing Integration Settings
1. Open Alter (your global shortcut or with your mouse)
2. Open the menu (three dots on the right)
2. Navigate to the **Tools Manager** entry
3. Enable/disable specific integrations as needed

#### Privacy & Security
- **Local Tools**: All data stays on your Mac - completely offline
- **External Integrations**: Make sure to enable only the tools you need from each integrations
- **No Background Monitoring**: Alter only accesses data when you request it

### Troubleshooting Integrations

#### Common Issues
1. **Tool Not Working**: Check what parameters are required and do not hesitate to create custom prompts or add explainers to your profile to ground your tools usage.
2. **Assistant not picking up the tools**: Make sure the model you choose supports tools. We recommend "Alter - best", Gemini 2.0 flash,  Gemini 2.0-flash-lite, and Claude 4 Sonnet.
3. **Apple Shortcuts**: Ensure shortcuts are properly configured to take the last assistant message as an argument

#### Getting Help
- Ask Alter to explain how a tool is used once the tool is enabled.
- Join us on Discord to get help by the team and the community.

> **Pro Tip**: Start with local tools to get familiar with Alter's integration capabilities before setting up external services.
