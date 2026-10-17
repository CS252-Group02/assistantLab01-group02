# AuraJournal — AI Service Interface

**Status:** Proposed interface (documentation only)  
**Component:** `ai-service`  
**Scope:** Future AI integration; no LLM or media API calls are implemented in this issue.

## 1. Purpose

AuraJournal is a personal journaling space. Its AI companion should help users feel heard and create a comfortable environment for writing—not act as a therapist, make diagnoses, or give unsolicited, specific life advice.

This document defines the **contract** between the application backend and a future AI service. The implementation and choice of AI providers are intentionally left open.

The AI service may support three optional features:

1. **Supportive reflection:** Short, neutral, empathetic acknowledgments that do not judge or prescribe solutions.
2. **Visual ambience:** A description/prompt for a calming journal background based on the user's selected mood or preferences.
3. **Audio ambience:** An optional mood/style recommendation for background music or sounds while journaling.

Generating an image, fetching audio, and playing music belong to separate application/media components; this interface only returns recommendations or generation instructions.

## 2. Proposed Function Signature

```python
async def create_journal_companion(
    request: JournalAIRequest,
) -> JournalAIResponse:
    """Return optional supportive text and ambience suggestions."""
```

The names and types below are a proposed contract, **not implemented Python classes**. The team may later expose the same contract through an HTTP endpoint instead of a Python function.

## 3. Inputs — `JournalAIRequest`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `entry_text` | `str \| null` | No | Current journal text, shared with AI only with the user's consent. |
| `mood` | `str \| null` | No | Mood explicitly selected by the user (e.g., `calm`, `sad`, `stressed`, `happy`, `reflective`). |
| `features` | `list[str]` | Yes | Any of `reflection`, `background`, `audio`. May be empty. |
| `preferences` | `object` | No | Optional preferences, such as visual theme, music style, or reduced stimulation. |
| `allow_text_processing` | `bool` | Yes | Explicit permission to use `entry_text` for AI processing. Defaults to `false` at the UI level. |

**Input rules**

- `entry_text` is optional because users may want ambience without sharing journal content.
- If `allow_text_processing` is `false`, the AI service **must ignore** `entry_text` and must not forward it to any model/provider.
- If no mood or usable text is provided, choose a neutral ambience rather than claiming to know how the user feels.
- Invalid feature names or unsupported field types should produce `INVALID_INPUT`.
- The service should process only the data needed for the features the user selected.

Example request:

```json
{
  "entry_text": "I feel a little overwhelmed today.",
  "mood": "reflective",
  "features": ["reflection", "background", "audio"],
  "preferences": {"visual_theme": "night sky", "audio_style": "instrumental"},
  "allow_text_processing": true
}
```

## 4. Outputs — `JournalAIResponse`

| Field | Type | Description |
| --- | --- | --- |
| `status` | `str` | One of `ok`, `fallback`, `error`. |
| `supportive_message` | `str \| null` | Optional brief response; `null` when reflection was not requested. |
| `background_prompt` | `str \| null` | Optional prompt/description for a future background-image generator. This is **not** an image URL. |
| `audio_mood` | `str \| null` | Optional ambience tag (e.g., `soft_piano`, `rain`, `ambient`, `silence`). This is **not** an audio file. |
| `error_code` | `str \| null` | Machine-readable error if a request fails or uses fallback. |

Only requested features should return non-null content. Media components decide how to map prompts and tags to available images, tracks, or soundscapes.

Example response:

```json
{
  "status": "ok",
  "supportive_message": "That sounds like a lot to carry today. You can take your time putting it into words.",
  "background_prompt": "A quiet night sky with soft blue tones and gentle stars; minimal distractions.",
  "audio_mood": "soft_piano",
  "error_code": null
}
```

## 5. Errors

| Code | Meaning | Expected handling |
| --- | --- | --- |
| `INVALID_INPUT` | Unsupported features or malformed input. | Return `status: error`; ask the caller to correct the request. |
| `SERVICE_UNAVAILABLE` | AI/model provider cannot be reached. | Use deterministic fallback when possible. |
| `TIMEOUT` | AI generation exceeds the configured time limit. | Use deterministic fallback when possible. |
| `INVALID_RESPONSE` | AI output does not match the response contract. | Discard invalid content and use fallback. |
| `CONTENT_UNSAFE` | Generated content violates the service's safety requirements. | Do not display unsafe content; return a safe fallback. |

Error details must not expose journal text, credentials, or provider internals.

## 6. Fallback Behavior

AuraJournal must remain usable when AI is disabled or unavailable.

- **Reflection:** Return a short, prewritten, nonjudgmental message (e.g., "Take your time. This space is yours to write in.").
- **Background:** Use a default, locally available calming background instead of relying on image generation.
- **Audio:** Use `silence` or a user-selected local ambience preset; never auto-play unexpected audio.
- **No requested features:** Return `status: ok` with optional fields set to `null`; no AI call is needed.
- **Invalid inputs:** Return an error, not a fabricated successful response.

Fallback responses should preserve the same output fields so the UI/backend can handle them consistently.

## 7. Safety, Privacy, and User Control

- **User autonomy:** Reflection is optional. Keep replies brief and supportive; avoid unsolicited instructions, forced positivity, diagnoses, or claiming to know the user's feelings.
- **Sensitive situations:** Do not respond to indications of immediate danger with generic cheerfulness. Use an appropriate supportive safety response encouraging real-world help; the AI companion is not an emergency service.
- **Privacy:** Journal text is private. Do not log raw entries, include them in error messages, or send them to external AI providers without explicit consent. Whether the app stores an entry is handled separately by the journal backend.
- **Transparency:** Make it clear when a message or suggestion is AI-generated. Do not imply that the AI is a human companion or a licensed professional.
- **Control:** Users may disable AI, override mood or ambience suggestions, change backgrounds, and manually start/stop audio. Never infer a clinical condition from journal content.

## 8. Scope and Acceptance Criteria

**In scope for this issue:** Document the function signature, inputs, outputs, errors, fallback behavior, and basic privacy/safety rules.

**Out of scope:** Implementing an LLM integration, generating images, streaming music, storing journal entries, or selecting specific third-party providers.

This document is ready for review when:

- [ ] The backend and UI developers can understand the proposed request/response contract.
- [ ] Every output and error has a defined meaning.
- [ ] Fallback behavior is defined for AI unavailability.
- [ ] No live LLM/media calls or secrets are introduced.
- [ ] The team has reviewed and agreed on the proposed interface.
