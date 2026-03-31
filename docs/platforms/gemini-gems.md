# Gemini Gems Platform Guide

This guide explains how to use skills from this repository with Google Gemini Gems.

---

## Important: Gemini Gems require manual setup

Unlike OpenAI Codex and Claude Code — where skill files can be loaded programmatically — **Gemini Gems are created manually through the Gemini web interface.**

This repository does **not** auto-register Gems with Gemini. There is no API for creating Gems programmatically. This is a limitation of the Gemini Gems platform as of 2024.

What this repository provides:
- `exports/gemini/GEM_INSTRUCTIONS.md` — the text you paste into the Gemini Gem UI
- `exports/gemini/SETUP.md` — a step-by-step guide for creating the Gem in the UI

---

## What is a Gemini Gem?

A Gemini Gem is a customized version of Gemini with specific instructions and a persona. You create it through the Gemini web interface at [gemini.google.com](https://gemini.google.com), and then you can access it whenever you need it.

Gems are saved to your Google account. You select a Gem manually before starting a conversation with it.

---

## How to create a Gem from this repository

### Step 1: Get the instructions text

Open the skill's Gemini export:

```
skills/<slug>/exports/gemini/GEM_INSTRUCTIONS.md
```

This file contains the text you will paste into the Gemini Gem UI.

### Step 2: Follow the SETUP.md guide

Open:

```
skills/<slug>/exports/gemini/SETUP.md
```

This file has step-by-step instructions for navigating the Gemini UI and creating the Gem.

### Step 3: Create the Gem

1. Go to [gemini.google.com](https://gemini.google.com)
2. Click on "Gems" in the left sidebar
3. Click "New gem" or the "+" button
4. Give the Gem a name (use the skill's `title` from `skill.yaml`)
5. Paste the contents of `GEM_INSTRUCTIONS.md` into the instructions field
6. Click "Save"

### Step 4: Use the Gem

To use a Gem, click on it in the Gems panel. This starts a new conversation with the Gem's instructions active.

Because Gemini requires **manual selection**, you need to choose the right Gem before asking your question. Unlike OpenAI and Claude, Gemini does not automatically route to a Gem based on your message.

---

## Keeping your Gems up to date

When a skill is updated in this repository:

1. Regenerate the Gemini export:
   ```bash
   python tools/render_gemini_gem.py skills/<slug>
   ```

2. Open `exports/gemini/GEM_INSTRUCTIONS.md` and copy the updated text.

3. Go to your Gem in the Gemini UI, edit it, and replace the instructions with the new text.

There is no automated sync. This is a manual process.

---

## Why manual selection vs auto-matching?

OpenAI and Claude support loading many skill definitions and automatically matching them to user messages. Gemini Gems work differently — you have one active Gem per conversation, and you choose it manually.

This means:
- You cannot have all skills "always on" in Gemini
- You need to know which skill you want before starting a conversation
- The `description` field matters less for routing in Gemini (since you select it manually), but it still helps you remember what each Gem is for

---

## The `manual_selection: true` flag

In `skill.yaml`, the Gemini platform override is:

```yaml
platform_overrides:
  gemini:
    manual_selection: true
```

This flag is used by the renderer to generate Gemini-appropriate instructions that remind the user to select the Gem manually. It also affects the SETUP.md content.
