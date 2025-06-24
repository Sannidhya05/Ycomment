# 💬 Ycomment – AI-Powered YouTube Comment Generator

**Ycomment** is a Streamlit web app that takes a YouTube video URL and uses the transcript to generate a witty, wholesome, insightful, or sarcastic comment — powered by the Mistral AI language model.

---

## 🚀 Features

- 🎥 Extracts transcripts from YouTube videos
- 🧠 Summarizes the content using Mistral's `mistral-medium` model
- 💬 Generates human-like comments in your selected style
- 🌐 Streamlit frontend for instant interaction
-⚙️ Easy deployment to Railway

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ycomment.git
cd ycomment
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

### 3. Add your Mistral API key

Create a `.env` file **or** set this as an environment variable in Railway or locally:

```
MISTRAL_API_KEY=your_mistral_api_key_here
```

You can get your key at [https://mistral.ai](https://mistral.ai).

---

## 📦 Deployment

### 🚂 Deploy on Railway

1. Go to [https://railway.app](https://railway.app)
2. Click **New Project** → **Deploy from GitHub**
3. Select this repo
4. Add environment variable:
   - `MISTRAL_API_KEY = your_mistral_key_here`
5. Add a `Procfile` if needed:

```
web: streamlit run app.py --server.port $PORT
```

6. Done! You’ll get a public link to your app.

---

## 🧪 Example Use

Paste this YouTube URL into the app:
```
https://www.youtube.com/watch?v=RhdlZgfzdJ8
```

Choose your tone — `witty`, `wholesome`, `funny`, etc. — and click **Generate**. Watch the magic happen ✨

---

## 📁 File Structure

```
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── Procfile             # For Railway deployment
└── README.md            # This file
```

---

## 🙏 Credits

- Powered by [Mistral AI](https://mistral.ai)
- Transcript extraction via [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api)
- UI built with [Streamlit](https://streamlit.io)

---

