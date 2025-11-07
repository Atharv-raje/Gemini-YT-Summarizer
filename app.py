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