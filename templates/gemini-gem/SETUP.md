# Gemini Gem Setup Guide: Template Skill Name

This guide walks you through creating a Gemini Gem for this skill in the Gemini web interface.

**Note:** Gemini Gems must be created manually. There is no API for automated Gem creation.

---

## Prerequisites

- A Google account with access to [gemini.google.com](https://gemini.google.com)
- The `GEM_INSTRUCTIONS.md` file from this directory

---

## Step-by-step setup

### Step 1: Open Gemini

Go to [gemini.google.com](https://gemini.google.com) and sign in.

### Step 2: Navigate to Gems

In the left sidebar, look for "Gems" and click it. If you don't see it, look for a menu icon or "Explore Gemini" option.

### Step 3: Create a new Gem

Click the "New gem" button or the "+" icon next to "My Gems".

### Step 4: Name your Gem

Enter the name: **Template Skill Name**

### Step 5: Add instructions

Open `GEM_INSTRUCTIONS.md` from this directory. Copy the entire contents (everything after the HTML comments at the top) and paste it into the instructions field in the Gemini UI.

### Step 6: Save

Click "Save" to create the Gem.

### Step 7: Test the Gem

Click on your new Gem to start a conversation. Try one of these test prompts:

- [Test prompt 1]
- [Test prompt 2]

---

## Using the Gem

To use this Gem in future conversations:

1. Go to [gemini.google.com](https://gemini.google.com)
2. Click "Gems" in the sidebar
3. Select "Template Skill Name"
4. Start your conversation

Remember: you must select the Gem **before** asking your question.

---

## Updating the Gem

When the skill is updated in this repository:

1. Regenerate the export: `python tools/render_gemini_gem.py skills/<slug>`
2. Open the updated `GEM_INSTRUCTIONS.md`
3. Go to your Gem in the Gemini UI and click the edit (pencil) icon
4. Replace the instructions with the new content
5. Click "Save"
