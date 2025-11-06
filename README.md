#  Build Your Own AI-Powered YouTube Summarizer

Welcome! 👋  
In this tutorial, you’ll learn how to build your own **YouTube video summarizer** using Google’s **Gemini AI model**.  
By the end, you’ll have a working web app that takes a YouTube link and instantly generates a summary of the video content.

---

##  What You’ll Build

You’ll create a Flask web application that:
1. Accepts a YouTube URL from the user.
2. Sends it to a backend built with Python.
3. Uses Google’s **Gemini API** to analyze and summarize the video.
4. Displays the summarized text neatly on a webpage.

This project is great if you want to learn how to integrate **GenAI models** into real-world web apps!


##  Step 1: Set Up Google Cloud

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


##  Step 2: Install Required Tools

Make sure you have these installed locally:

- **Python 3.9+**
- **Google Cloud SDK (gcloud)**
- **Flask**
- **Google GenAI SDK**

Then install dependencies:

pip install flask google-genai


 ## Step 3: Project Structure

Create a new folder called youtube_summarizer and inside it, set up these files:
```
youtube_summarizer/
│
├── app.py
├── templates/
│   └── index.html
└── requirements.txt
```

Your requirements.txt should look like this:
```
flask
google-genai
```

## Step 4: Backend Code (app.py)

This Python code runs your web server and connects to the Gemini API.
```
from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)
client = genai.Client()

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        video_url = request.form['youtube_url']
        prompt = f"Summarize the content of this YouTube video: {video_url}"
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        summary = response.text
    return render_template('index.html', summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
```

## Step 5: Frontend Code (templates/index.html)

This is the simple webpage users interact with.
```
<!DOCTYPE html>
<html>
  <head>
    <title>YouTube Summarizer</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 40px; }
      input { width: 60%; padding: 10px; }
      button { padding: 10px 14px; margin-left: 8px; }
      .summary { margin-top: 20px; padding: 15px; background: #f5f5f5; border-radius: 10px; }
    </style>
  </head>
  <body>
    <h2>🎥 YouTube Video Summarizer</h2>
    <form method="post">
      <input type="text" name="youtube_url" placeholder="Paste YouTube link here" required />
      <button type="submit">Summarize</button>
    </form>
    {% if summary %}
      <div class="summary">
        <h3>🧠 Video Summary:</h3>
        <p>{{ summary }}</p>
      </div>
    {% endif %}
  </body>
</html>
```
##  Step 6: Run the App Locally

To test it on your own computer:
```
python app.py
```

Then open your browser and go to:
```
http://127.0.0.1:5000/
```

Paste any YouTube link, click Summarize, and you’ll see Gemini generate a smart summary!

## Step 7: Deploy to Google Cloud Run

To make your app public and shareable:

Authenticate with your Google account:
```
gcloud auth login
```

Set your current project:
```
gcloud config set project <your-project-id>
```

Deploy the app:
```
gcloud run deploy youtube-summarizer \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

Once the deployment finishes, Google Cloud will give you a public URL to access your summarizer.

## Step 8: Customization Ideas

You can improve your summarizer with:

-> A better UI using Tailwind CSS or Material UI.

-> Custom prompts to generate “key moments,” “topic timelines,” or “sentiment analysis.”

-> Integration with your own subtitle or action-detection model (like Whisper) to enhance summaries.

-> Adding an upload option for local video files.

## Step 9: Clean Up Resources

When you’re done testing, remember to avoid unnecessary cloud charges:
```
gcloud run services delete youtube-summarizer
```
📘 Final Thoughts

That’s it!
You’ve built a working AI-powered YouTube summarizer using Google’s Gemini model and deployed it with Flask + Cloud Run.

🧑‍💻 Author

Created by Atharv Raje — for educational purposes and to help developers learn how to integrate Google’s Gemini models into web apps.

If you want to explore this concept in greater depth, check out the official Google Codelab that inspired this tutorial:
👉 Build a Gemini-Powered YouTube Summarizer (Official Guide): https://codelabs.developers.google.com/devsite/codelabs/build-youtube-summarizer#1


