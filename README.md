# CourseTube AI 🎓

> Paste any YouTube video URL → Get a full structured course with notes, quizzes and assignments.

---

## What is CourseTube AI?

YouTube contains some of the best educational content in the world.  
But watching a video is not the same as actually learning from it.

Studies show:
- People remember **10%** of what they watch
- People remember **70%** of what they practice

**CourseTube AI** transforms a YouTube video into a complete AI-generated learning experience.

Instead of just watching videos, students get:
- Structured learning modules
- Detailed study notes
- MCQ quizzes
- Practical assignments
- AI-reviewed educational content

All automatically generated using a multi-agent AI system built with CrewAI.

---

## What Problem Does It Solve?

| YouTube gives you | CourseTube AI gives you |
|---|---|
| Raw unstructured video | Structured learning modules |
| No notes | Clean detailed study notes |
| No quiz | MCQ quiz after each module |
| No assignments | Practical hands-on assignments |
| No quality review | AI reviewed and corrected content |
| Passive watching | Active learning |

---

## How It Works

```text
You paste a YouTube video URL
        ↓
Agent 1 fetches the transcript from the video
        ↓
Agent 2 extracts video title, channel name and duration
        ↓
Agent 3 divides the transcript into logical learning modules
        ↓
Agent 4 writes detailed study notes for each module
        ↓
Agent 5 creates MCQ quizzes for each module
        ↓
Agent 6 designs practical assignments
        ↓
Agent 7 reviews and improves all generated content
        ↓
You receive a complete structured course
```

---

## Project Architecture

```text
CourseTube AI
├── app.py              → Streamlit web interface
├── crew.py             → Multi-agent CrewAI workflow
├── tools.py            → Custom YouTube and transcription tools
├── memory.py           → SQLite caching system
├── schemas.py          → Pydantic output schemas
├── validation.py       → YouTube URL validation
├── config/
│   ├── agents.yaml     → Agent roles, goals and personalities
│   └── tasks.yaml      → Task descriptions and outputs
└── .env                → API keys
```

---

## The 7 AI Agents

| Agent | Responsibility |
|---|---|
| TranscriptionAgent | Fetches video transcript. Uses Faster-Whisper if captions are unavailable |
| MetadataAgent | Extracts video title, channel name and duration |
| StructureAgent | Converts transcript into structured learning modules |
| NotesAgent | Writes detailed educational study notes |
| QuizAgent | Generates MCQ quizzes with answer keys |
| AssignmentAgent | Creates practical hands-on assignments |
| ReviewAgent | Reviews and corrects all generated educational content |

---

## Tech Stack

| Technology | Purpose |
|---|---|
| CrewAI | Multi-agent orchestration |
| Cerebras GPT-OSS 120B | LLM powering the agents |
| youtube-transcript-api | Fetches YouTube transcripts |
| pytubefix | Extracts YouTube metadata |
| faster-whisper | Local audio transcription fallback |
| yt-dlp | Downloads video audio |
| Streamlit | Web interface |
| SQLite | Local caching |
| Pydantic | Structured output validation |
| LiteLLM | LLM provider integration |

---

## Features

### Structured AI Learning
Transforms YouTube videos into organized educational courses.

### Smart Caching
Generated courses are stored locally using SQLite.  
Reprocessing the same video loads instantly without rerunning agents.

### Faster-Whisper Fallback
If captions are unavailable, the system downloads audio and transcribes it locally using Faster-Whisper.

### URL Validation
Basic YouTube URL validation prevents invalid links before processing.

### Live Agent Logs
Watch every AI agent work step-by-step in real time.

### AI Quality Review
A dedicated ReviewAgent checks:
- incorrect information
- unclear quiz questions
- weak assignments
- missing concepts

before showing content to the user.

---

## Supported URLs

✅ Single YouTube videos

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

✅ Videos that belong to playlists

```text
https://www.youtube.com/watch?v=VIDEO_ID&list=PLAYLIST_ID
```

❌ Full playlist processing is not yet supported

```text
https://www.youtube.com/playlist?list=PLAYLIST_ID
```

---

## Installation

### Step 1 — Clone the Repository

```bash
git clone https://github.com/abhijithj12/CourseTube-AI.git
cd CourseTube-AI
```

---

### Step 2 — Install Dependencies

```bash
uv add crewai crewai-tools youtube-transcript-api pytubefix faster-whisper streamlit pydantic yt-dlp cerebras-cloud-sdk python-dotenv litellm
```

---

### Step 3 — Get a Cerebras API Key

1. Visit:
   https://cloud.cerebras.ai

2. Create an account

3. Generate a new API key

---

### Step 4 — Create `.env`

```env
CEREBRAS_API_KEY=your_api_key_here
```

---

### Step 5 — Run the Application

```bash
uv run streamlit run app.py
```

---

## Example Workflow

Input:

```text
https://www.youtube.com/watch?v=example
```

Output:
- Structured modules
- Detailed notes
- MCQ quizzes
- Practical assignments
- AI-reviewed educational content

---

## Known Limitations

- Code shown visually on screen is not extracted yet
- Very long videos require more processing time
- Poor audio quality can reduce transcription accuracy
- Full playlist-to-course conversion is not yet supported

---

## Future Roadmap

- [ ] Playlist-to-course generation
- [ ] PDF export
- [ ] Progress tracking
- [ ] Gemini Vision integration for extracting code from video frames
- [ ] Multi-language support
- [ ] Vector database memory for semantic retrieval

---

## Why This Project is Different

Most tools summarize YouTube videos.

CourseTube AI goes further by converting videos into:
- structured educational modules
- detailed notes
- quizzes
- assignments
- reviewed learning material

using a coordinated multi-agent AI system.

---

## Project By

**Abhijith J**

GitHub: https://github.com/abhijithj12