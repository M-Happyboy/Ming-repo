## Why

The user needs a simple yet powerful local interface to perform detailed visual analysis of images using the state-of-the-art `gemma-4-31b-it` model via Google AI Studio.

## What Changes

- Create a Gradio-based web interface for image uploads and result display.
- Implement the Google AI Studio API integration using the `google-generativeai` SDK.
- Configure the model with a specialized system prompt to ensure "detailed analysis" while constraining output to 3-5 sentences.
- Implement secure API key management using a `.env` file and `python-dotenv`.

## Capabilities

### New Capabilities
- `image-analysis`: Ability to upload an image and receive a concise (3-5 sentence) detailed description using a multimodal LLM.

### Modified Capabilities
- None

## Impact

- **Dependencies**: Addition of `gradio`, `google-generativeai`, and `python-dotenv`.
- **Environment**: Requires a `GOOGLE_API_KEY` in a local `.env` file.
