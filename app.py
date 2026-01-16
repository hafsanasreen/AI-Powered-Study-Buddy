import streamlit as st
import requests  # For Ollama API calls
import json
import time
from PyPDF2 import PdfReader

# Ollama setup (local server at http://localhost:11434)
OLLAMA_URL = "http://localhost:11434/api/generate"

class StudyBuddy:
    def __init__(self):
        # No external APIs—using Ollama locally
        pass

    def call_ollama(self, prompt, model="llama2"):
        """Call Ollama local API for text generation."""
        try:
            response = requests.post(OLLAMA_URL, json={"model": model, "prompt": prompt, "stream": False})
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "Failed.")
            else:
                return "Failed."
        except Exception as e:
            return f"Error: {e}"

    def explain_topic(self, topic, context=""):
        prompt = f"Explain {topic} in simple terms: {context}"
        return self.call_ollama(prompt)

    def summarize_notes(self, notes):
        prompt = f"Summarize the following text: {notes}"
        return self.call_ollama(prompt)

    def generate_quiz(self, text, num_questions=3):
        questions = []
        for i in range(num_questions):
            prompt = f"Generate a multiple-choice question with 4 options based on: {text[:200]}... Format: Question? A) Option1 B) Option2 C) Option3 D) Option4 Correct: A"
            response = self.call_ollama(prompt)
            # Simple parsing (improve with regex)
            parts = response.split("Correct:")
            if len(parts) > 1:
                question_part = parts[0].strip()
                correct = parts[1].strip()
                options = [opt.strip() for opt in question_part.split("A)")[1].split("B)")[0].split("C)")[0].split("D)")[0].split() if opt]
                questions.append({"question": question_part, "options": options[:4], "correct": correct})
            else:
                questions.append({"question": "Sample Question?", "options": ["A", "B", "C", "D"], "correct": "A"})
        return questions

    def generate_flashcards(self, text, num_cards=5):
        prompt = f"Extract {num_cards} term-definition pairs from: {self.summarize_notes(text)} Format: Term: Definition"
        response = self.call_ollama(prompt)
        pairs = response.split("Term:")
        flashcards = []
        for pair in pairs[1:]:
            if ":" in pair:
                term, definition = pair.split(":", 1)
                flashcards.append({"term": term.strip(), "definition": definition.strip()})
        return flashcards[:num_cards]

# Initialize app
st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="wide")
st.title("📚 AI-Powered Study Buddy")
st.markdown("Your Personal AI Study Assistant")

buddy = StudyBuddy()

# Sidebar
with st.sidebar:
    st.header("Settings")
    num_items = st.slider("Number of Quiz Questions/Flashcards", 1, 10, 3)
    if st.button("Clear History"):
        st.session_state.history = []

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Explain Topic", "Summarize Notes", "Generate Quiz", "Generate Flashcards", "History"])

with tab1:
    st.header("Explain Topic")
    topic = st.text_input("Topic")
    context = st.text_area("Context")
    if st.button("Explain"):
        with st.spinner("Generating..."):
            explanation = buddy.explain_topic(topic, context)
            if "Failed" not in explanation:
                st.success("Generated!")
                st.write(explanation)
                st.session_state.history.append({"type": "Explanation", "input": topic, "output": explanation})
            else:
                st.error("Failed. Ensure Ollama is running.")

with tab2:
    st.header("Summarize Notes")
    notes_input = st.text_area("Notes", key="notes_input")
    uploaded_file = st.file_uploader("Upload PDF/TXT", type=["pdf", "txt"])
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            reader = PdfReader(uploaded_file)
            notes_input = "".join([page.extract_text() for page in reader.pages])
        else:
            notes_input = uploaded_file.read().decode("utf-8")
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i+1)
            summary = buddy.summarize_notes(notes_input)
            if "Failed" not in summary:
                st.success("Ready!")
                st.write(summary)
                st.download_button("Download", summary, file_name="summary.txt")
                st.session_state.history.append({"type": "Summary", "input": notes_input[:100], "output": summary})
            else:
                st.error("Failed. Ensure Ollama is running.")

with tab3:
    st.header("Generate Quiz")
    quiz_text = st.text_area("Text", key="quiz_text")
    if st.button("Generate Quiz", key="generate_quiz_btn"):
        with st.spinner("Creating..."):
            quiz = buddy.generate_quiz(quiz_text, num_items)
            if quiz:
                st.success("Generated!")
                for i, q in enumerate(quiz):  # Use enumerate for index
                    st.write(f"**{q['question']}**")
                    st.radio("Answer", q["options"], key=f"quiz_radio_{i}")  # Unique key with index
                quiz_json = json.dumps(quiz, indent=2)
                st.download_button("Download", quiz_json, file_name="quiz.json", key="download_quiz")
                st.session_state.history.append({"type": "Quiz", "input": quiz_text[:100], "output": quiz})
            else:
                st.error("Failed.")
with tab4:
    st.header("Generate Flashcards")
    flash_text = st.text_area("Text", key="flash_text")
    if st.button("Generate Flashcards"):
        with st.spinner("Creating..."):
            flashcards = buddy.generate_flashcards(flash_text, num_items)
            if flashcards:
                st.success("Ready!")
                for card in flashcards:
                    with st.expander(f"Term: {card['term']}"):
                        st.write(f"Definition: {card['definition']}")
                flash_json = json.dumps(flashcards, indent=2)
                st.download_button("Download", flash_json, file_name="flashcards.json")
                st.session_state.history.append({"type": "Flashcards", "input": flash_text[:100], "output": flashcards})
            else:
                st.error("Failed.")

with tab5:
    st.header("History")
    if st.session_state.history:
        for item in st.session_state.history:
            st.write(f"**{item['type']}**: {item['input']}... -> {item['output'][:100]}...")
    else:
        st.write("No history.")

# Footer
st.markdown("---")
st.markdown("Get clear explanations, summaries, quizzes, and flashcards instantly.")