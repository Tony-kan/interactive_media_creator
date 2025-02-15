# Interactive Media Creator

Interactive Media Creator is an AI-driven storytelling app that lets you create a full multimedia experience—from generating comic-style images based on your descriptions to crafting and narrating engaging stories. It combines the power of image generation, text-to-speech, and advanced language models to bring your creative ideas to life.

---

## Overview

This application provides a seamless workflow for creating dynamic, interactive stories:

- **Image Generation:** Use the DALL·E API to transform your text descriptions into detailed comic-style images.
- **Story Creation:** Optionally, utilize GPT-4 Turbo to analyze the generated images and craft a unique narrative.
- **Text-to-Speech:** Convert the written story into spoken words with Clarifai's text-to-speech API, making your content accessible to a broader audience.

---

## Tech Stack

- **Python:** Core programming language for the app.
- **Streamlit:** Framework for building the interactive user interface.
- **Clarifai API:** For text-to-speech conversion.
- **OpenAI API (DALL·E & GPT-4 Turbo):** For image generation and story crafting.
- **PIL (Pillow):** For image processing and manipulation.
- **dotenv:** To manage environment variables securely.

---

## Features

- **Dynamic Image Generation:** Transform textual descriptions into vivid images using DALL·E.
- **Automated Storytelling:** Leverage GPT-4 Turbo to create narratives based on the generated images.
- **Voice Narration:** Convert text stories into natural-sounding audio via Clarifai’s text-to-speech API.
- **User-Friendly Interface:** A clean and intuitive UI built with Streamlit, allowing users to interact easily with all functionalities.
- **Accessibility:** Enhances content accessibility, particularly for visually impaired users, by providing audio narration.

---

## Get Started

### Prerequisites

- **Python 3.7 or later**
- **Accounts with:**
  - [Clarifai](https://www.clarifai.com/)
  - [OpenAI](https://openai.com/)

### Setting Up the Virtual Environment and Installing Packages

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Tony-kan/interactive-media-creator.git
   cd interactive-media-creator

   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv

   ```

3. **Activate the Virtual Environment:**

   ```bash
    source venv/bin/activate

   ```

4. **Install the Required Packages:**

   ```bash
   pip install -r requirements.txt

   ```

5. **Setting Up Environment Variables:**

   1. **Create a `.env` File:**  
      In the project root directory, create a new file named `.env`.

   2. **Add Your API Keys:**  
      Open the `.env` file in your favorite text editor and add your keys in the following format:

   ```env
   CLARIFAI_PAT=Your_Clarifai_Personal_Access_Token
   OPEN_AI=Your_OpenAI_API_Key

   ```
