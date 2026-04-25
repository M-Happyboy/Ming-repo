## ADDED Requirements

### Requirement: Image Upload
The system SHALL allow the user to upload an image file via the Gradio interface.

#### Scenario: Successful upload
- **WHEN** a user uploads a valid image file
- **THEN** the image is displayed in the input component of the UI

### Requirement: Image Analysis
The system SHALL send the uploaded image to the `gemma-4-31b-it` model via the Google AI Studio API to generate a detailed description.

#### Scenario: Successful analysis
- **WHEN** the user triggers the analysis process
- **THEN** the system returns a detailed visual description of the image

### Requirement: Response Length Constraint
The system MUST ensure that the generated image description is between 3 and 5 sentences long.

#### Scenario: Length validation
- **WHEN** the AI returns an analysis
- **THEN** the response contains no fewer than 3 and no more than 5 sentences

### Requirement: Secure API Configuration
The system MUST retrieve the Google AI Studio API key from an environment variable (e.g., via a `.env` file).

#### Scenario: Missing API key
- **WHEN** the `GOOGLE_API_KEY` is not found in the environment
- **THEN** the system displays a clear error message to the user indicating the missing configuration
