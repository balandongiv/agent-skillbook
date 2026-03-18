# Gemini Gem Setup Guide: Good Function Design

This guide walks you through creating a Gemini Gem for this skill.

**Note:** Gemini Gems must be created manually through the Gemini web UI. This repository cannot auto-register Gems.

---

## Prerequisites

- A Google account with access to [gemini.google.com](https://gemini.google.com)
- The `GEM_INSTRUCTIONS.md` file from this directory

---

## Step-by-step setup

### Step 1: Open Gemini

Go to [gemini.google.com](https://gemini.google.com) and sign in.

### Step 2: Navigate to Gems

In the left sidebar, click **Gems**.

### Step 3: Create a new Gem

Click the **New gem** button or the "+" icon.

### Step 4: Name your Gem

Enter the name: **Good Function Design**

### Step 5: Add instructions

Open `GEM_INSTRUCTIONS.md` from this directory. Copy the full content (after the HTML comment lines) and paste it into the instructions field.

### Step 6: Save

Click **Save** to create the Gem.
### Step 7: Test your Gem

Open your new Gem and try a few of the test prompts from `skills/good-function-design/TESTS.md` to verify it is working correctly.


---

## Using the Gem

1. Go to [gemini.google.com](https://gemini.google.com)
2. Click **Gems** in the sidebar
3. Select **Good Function Design**
4. Start your conversation

**Remember:** Select the Gem before asking your question. Gemini requires manual Gem selection — it does not auto-route based on message content.

---

## Updating the Gem

When this skill is updated:

1. Regenerate: `python tools/render_gemini_gem.py skills/good-function-design`
2. Open the updated `GEM_INSTRUCTIONS.md`
3. Edit your Gem in the Gemini UI and replace the instructions
4. Click **Save**
