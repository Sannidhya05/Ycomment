import streamlit as st
from openai import OpenAI
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

client = OpenAI(
    api_key=st.secrets.get("MISTRAL_API_KEY", ""),
    base_url="https://api.mistral.ai/v1"
)

def generate_summary(transcript: str, model: str = "mistral-medium") -> str:
    prompt = f"""
create a consice and accurate summary of the following transcript.

Transcript:
{transcript}
"""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )
    return response.choices[0].message.content.strip()

def generate_comment(transcript: str, style: str = "witty", model: str = "mistral-medium") -> str:
    summary = generate_summary(transcript)
    prompt = f"""
You are a viral YouTube commenter known for being {style}.

Write a short but memorable YouTube comment for this video, based on the transcript summary below. 
It should reflect your {style} tone and feel like something that would get lots of likes.

summary of the video:
{summary}

Only return the comment. Do not include explanations or quotes. No hashtags. No quotation marks.
Humanize it as much as possible.
"""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )
    return response.choices[0].message.content.strip()

def get_transcript(video_id: str) -> str:
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript_list])
    except Exception as e:
        st.error(f"❌ Transcript error: {e}")
        return ""

def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)
    if "youtube.com" in parsed_url.netloc:
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query).get("v", [None])[0]
        elif "/embed/" in parsed_url.path:
            return parsed_url.path.split("/embed/")[1]
    elif "youtu.be" in parsed_url.netloc:
        return parsed_url.path.lstrip("/")
    return None

st.set_page_config(page_title="YouTube Comment Generator", page_icon="💬")
st.title("💬 AI YouTube Comment Generator")
st.write("Paste a YouTube URL and get an AI-generated comment in your favorite style.")

url = st.text_input("🔗 YouTube URL")
style = st.selectbox("🧠 Choose a comment style", ["witty", "insightful", "sarcastic", "wholesome", "funny"])
generate = st.button("✨ Generate Comment")

if generate and url:
    video_id = extract_video_id(url)
    if video_id:
        transcript = get_transcript(video_id)
        if transcript:
            with st.spinner("Generating comment..."):
                comment = generate_comment(transcript, style=style)
            st.success("Generated Comment:")
            st.text_area("💬 Comment", comment, height=100)
        else:
            st.error("❌ Couldn't get transcript for this video.")
    else:
        st.error("❌ Invalid YouTube URL.")
