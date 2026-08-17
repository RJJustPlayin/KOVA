# KOVA

KOVA is a personal AI operating system designed to feel like an Alexa-style assistant on a computer and phone, with OpenAI reasoning, web knowledge, memory, tools, computer control, music, reminders, and smart-home/Alexa integrations.

## Current milestone

This repository contains the **KOVA Core** foundation:

- OpenAI-powered conversation
- System personality/instructions
- Persistent local conversation memory
- Safe tool architecture
- Environment-based secrets
- CLI interface
- Clean extension points for web search, voice, computer control, Alexa, phone, and automation

## Quick start

1. Install Python 3.11+.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and add your OpenAI API key.
5. Run:

```bash
python main.py
```

## Important

Never commit `.env`, API keys, passwords, Alexa credentials, or other secrets. KOVA uses environment variables for credentials.

## Roadmap

1. KOVA Core
2. Voice input/output and wake word
3. Long-term memory
4. Web search / current knowledge
5. Tool system
6. Computer control
7. Music and media
8. Calendar/reminders
9. Alexa/smart-home integration
10. Mobile app
11. Coding agent with sandboxed execution
12. Proactive automation
