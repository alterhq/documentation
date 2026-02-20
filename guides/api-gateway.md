## API Gateway


Alter provides an OpenAI-compatible endpoint that allows you to use Alter's models and credits in other AI applications. This feature opens up a world of possibilities by letting you access Alter's powerful model collection through any tool that supports OpenAI endpoints.

### Overview

The Alter API gateway is a centralized billing solution that eliminates the need to manage multiple API keys and billing accounts across different AI providers. Instead of having your billing details scattered across many providers, you can enjoy having Alter as your single entry point for AI model access.

### Supported Features

- **OpenAI-compliant endpoint** supporting chat completions and model listing
- **Centralized billing** through your Alter account
- **Access to all Alter models** from external applications
- **Seamless integration** with existing OpenAI-compatible tools

### Popular Use Cases

The Alter API can be used with popular and specialized projects including:

- **[SillyTavern](https://sillytavern.app/)** - Roleplaying chat app
- **[NovelCrafter](https://www.novelcrafter.com/)** - Book writing application
- **Custom projects** - Develop your own applications using Alter as your LLM provider

### Getting Started

1. **Open Preferences**: Navigate to Alter's settings
3. **Access Router Tab**: Go to the API section in preferences
4. **Create API Key**: Generate your unique API key
5. **Copy Endpoint**: Copy the provided endpoint URL and paste it into your desired application. Some apps may require to add `/v1` to our base endpoint.


```
https://alterhq.com/api
```


### Model Naming Convention

When using the Alter API, model names follow this format:
```
<Provider>#<Model-name>
```

#### Examples:
- `OpenAI#gpt-4o-mini`
- `OpenAI#gpt-4o`
- `Claude#Claude-3-5-Sonnet-20240620`
- `Gemini#gemini-1.5-pro`
- `Mistral#mistral-large-latest`

### Configuration

#### API Key Management
- Generate and manage your API keys through **Settings > Router**
- Keep your API keys secure and never share them publicly
- Rotate keys regularly for security best practices

#### Endpoint Configuration
The Alter API endpoint can be configured in any OpenAI-compatible application by:
1. Setting the base URL to the Alter API endpoint
2. Using your generated API key for authentication
3. Selecting models using the Provider#Model-name format

#### Usage Limits

The API gateway has the following usage limitations:

- **Daily Limit**: 200 requests per day under fair use
- **Throttling**: After exceeding the daily limit, requests are throttled to 1 request per 10 minutes
- **Budget Top-up**: You can "top up" your budget if you need consistent access to premium models beyond the fair use limits

### Troubleshooting

#### Common Issues

**Models Not Listed**
If your application doesn't automatically list available models, manually specify the model using the Provider#Model-name format.

**Authentication Errors**
- Verify your API key is correctly entered
- Ensure you're using the correct endpoint URL: try `https://alterhq.com/api` or `https://alterhq.com/api/v1`
- Check that your Alter account is active and in good standing

**Connection Issues**
- Check if the application supports OpenAI-compatible endpoints
- Ensure you're using the latest version of Alter

> **Note**: The Alter API gateway is available to all Alter users and provides the same powerful model access you enjoy within the Alter application, extended to your favorite third-party tools.
