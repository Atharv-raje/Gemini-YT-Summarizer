# 🎬 Build Your Own AI-Powered YouTube Summarizer

Welcome! 👋  
In this tutorial, you’ll learn how to build your own **YouTube video summarizer** using Google’s **Gemini AI model**.  
By the end, you’ll have a working web app that takes a YouTube link and instantly generates a summary of the video content.

---

## 🧠 What You’ll Build

You’ll create a Flask web application that:
1. Accepts a YouTube URL from the user.
2. Sends it to a backend built with Python.
3. Uses Google’s **Gemini API** to analyze and summarize the video.
4. Displays the summarized text neatly on a webpage.

This project is great if you want to learn how to integrate **GenAI models** into real-world web apps!

---

## 🧩 Step 1: Set Up Google Cloud

Before we code, we need a Google Cloud project.

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Click **“New Project”** and give it a name (for example, `youtube-summarizer`).
3. Enable **billing** (Gemini API requires it).
4. Enable the following APIs:
   - Vertex AI API  
   - Cloud Run API  
   - Cloud Build API  
   - Cloud Resource Manager API  

These APIs allow your app to use Gemini and deploy to the cloud.

---

## ⚙️ Step 2: Install Required Tools

Make sure you have these installed locally:

- **Python 3.9+**
- **Google Cloud SDK (gcloud)**
- **Flask**
- **Google GenAI SDK**

Then install dependencies:
```bash
pip install flask google-genai


step 3: Project Structure

Create a new folder called youtube_summarizer and inside it, set up these files:

youtube_summarizer/
│
├── app.py
├── templates/
│   └── index.html
└── requirements.txt
