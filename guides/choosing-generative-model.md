## Choosing Your Generative Model


By default, Alter offers a variety of models, listed alphabetically by their hosting company.

You can also use your [API key](#via-your-api-key) or use [your local model](#locally-via-ollama-or-studiolm).

### Choosing your model 

After opening Alter, just type `/` to show available models and select the model you want to use.


#### Chosing a favorite model

Select the star icon next to a model with your mouse to mark the model as your favorite.
![Favoriting a model](https://alterhq.com/assets-doc/images/models/favorite-model.webp)


When using your API key or a local model, these appear at the top under **Custom**.  
All other interactions are routed through Alter Cloud.

### Using Alter Cloud

By default, Alter is set up with `/best` , our internal model router, choosing the best model based on your query.

![Router and model example](https://alterhq.com/assets-doc/images/settings/router.png)


You can change the default model in **Settings > Defaults > Model**.  


#### List of the models via Alter CLoud



  ##### Model with vision
  <details>

| Name | Context size |
| --- | --- |
| gemini-1.5-flash | 1000000 |
| gemini-1.5-pro | 1000000 |
| gemini-2.0-flash-001 | 1000000 |
| claude-3-haiku-20240307 | 200000 |
| claude-3-opus-20240229 | 200000 |
| claude-3-5-sonnet-20240620 | 200000 |
| claude-3-5-sonnet-latest | 200000 |
| claude-3-7-sonnet-latest | 200000 |
| chatgpt-4o-latest | 128000 |
| gpt-4o | 128000 |
| gpt-4o-2024-08-06 | 128000 |
| gpt-4o-mini | 128000 |
| gpt-4-turbo | 128000 |
| pixtral-12b-latest | 128000 |
| pixtral-large-latest | 128000 |
| gpt-3.5-turbo | 4191 |
</details> 

  ##### Model without vision
   <details>

| Name | Context size |
| --- | --- |
| codestral-2501 | 256000 |
| deepseek-ai/DeepSeek-R1 | 163840 |
| deepseek-ai/DeepSeek-V3 | 131072 |
| meta-llama/Llama-3.1-70B-Instruct-Turbo | 131072 |
| meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-128K | 131072 |
| deepseek-r1-distill-llama-70b | 128000 |
| llama-3.1-70b-versatile | 128000 |
| llama-3.1-8b-instant | 128000 |
| llama-3.1-sonar-large-128k-online | 128000 |
| llama-3.1-sonar-small-128k-online | 128000 |
| sonar | 127000 |
| sonar-pro | 200000 |
| qwen3-32b | 131072 |
| mixtral-8x7b-32768 | 32768 |
| meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo | 32768 |
| meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo | 32768 |
| mistral-small-latest | 32768 |
| nvidia/Llama-3.1-Nemotron-70B-Instruct-HF | 32768 |
| Qwen/Qwen2.5-72B-Instruct-Turbo | 32768 |
| Qwen/Qwen2.5-72B-Instruct-Turbo-lora | 32768 |
| Qwen/Qwen2.5-7B-Instruct-Turbo | 32768 |
| mixtral-8x7b-instruct | 16384 |
| mistral-7b-instruct | 16384 |
| llama-3.3-70b | 8192 |
| llama-3.3-70b-specdec | 8192 |
| llama-3.3-70b-versatile | 8192 |
| llama3-70b-8192 | 8192 |
| llama3-8b-8192 | 8192 |
| llama3.1-8b | 8192 |
| meta-llama/Llama-3-70b-chat-hf | 8192 |
| meta-llama/Llama-3-8b-chat-hf | 8192 |
| Gryphe/MythoMax-L2-13b | 4096 |
</details>

### Using Your API Key

![Custom Local](https://alterhq.com/assets-doc/images/models/custom-api-keys.webp)

You can use your own API key to connect directly to your provider's endpoint:  
1. Go to **Settings > API keys > Custom provider**.  
2. Enable Custom Provider
3. Pick your provider in the list

> Once connected, a tick will appear next to **Custom Endpoint**.  

Your provider's models will be listed under the **Custom** section.

> We only support OpenAI compatible endpoints meaning you can't use your Anthropic API keys.

Here's a list of the supported platforms for custom keys, based on the provided image:

1.  Azure
2.  Gemini
3.  LM Studio
4.  Mistral
5.  Ollama
6.  OpenAI
7.  Open Router
8.  Custom (Any OpenAI compatible endpoint)

#### Setting Up an Azure Endpoint in Alter

1.  **Enable Custom Provider:** In Alter's settings, enable the "Custom provider" option.
2.  **Choose Azure:** Select Azure as your provider.
3.  **Enter Complete Chat Completion Endpoint URL:** Provide the full chat completion endpoint URL, including the `api-version` parameter and the model name within the URL.  For example: `https://yourinstance.openai.azure.com/openai/deployments/your-model-name/chat/completions?api-version=2024-02-15-preview`
4.  **Enter API Key:**  Enter your Azure OpenAI API key.

Important Considerations

*   **Complete Endpoint Required:**  Make sure to use the *complete* chat completion endpoint, as Alter extracts the model name from the URL.
*   **Model Name in URL:** The model deployment name *must* be included in the URL path.
*   **API Version:** The URL *must* include the `api-version` parameter.


#### Where to find your API keys

| Provider | URL for generate an API Key | 
| -------- | -------- | 
| Google (Gemini)     | https://aistudio.google.com/app/apikey   | [Link](https://ai.google.dev/api/compatibility)
| Mistral     | https://console.mistral.ai/api-keys/  
| OpenAI     | https://platform.openai.com/api-keys |[Link]




### Locally using Ollama or LM Studio

![Custom Local](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/a3cb944c-7379-49a6-9349-c829bcda071b/image.png?t=1740499713)

To use Alter with local models (via Ollama or LM Studio):  
1. Go to **Settings > API keys > Custom provider**.  
2. Enable Custom Provider
3. Pick Ollama or LM Studio in the list of provider

> Once connected, a tick will appear next to **Custom Endpoint**.  

![image alt](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/4a22f3fb-ad9e-4f50-8184-1e5cc5238118/Alter_Settings_API_key_custom_provider_on.png?t=1740500360)

Your local models will be listed under the **Custom** section.

![Custom model](https://beehiiv-images-production.s3.amazonaws.com/uploads/asset/file/c3a9bef5-ff23-4a35-99b6-aedc7bc38972/Alter_Main_Custom_Models.png?t=1740502675)
