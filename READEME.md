AI-Powered Study Buddy
Overview
AI-Powered Study Buddy is an innovative web application designed to assist students in learning complex topics through AI-driven tools. Built with Streamlit and powered by Ollama (running Llama 2 locally), it provides offline, privacy-focused features like topic explanations, note summarization, quiz generation, and flashcards. This project demonstrates practical AI/ML skills, including local model deployment, NLP, and user-centric app development—ideal for educational and internship portfolios.

Key Highlights:

Free and Offline: No API costs or internet dependency; runs entirely on your device.
Privacy-Focused: All data stays local, ensuring security.
Easy to Use: Simple web interface with multi-tab navigation.
Scalable: Built with modular code for easy extensions.

Features
Explain Topic: Input a topic and optional context to get a simple, AI-generated explanation.
Summarize Notes: Upload or paste text/PDF notes for concise summaries.
Generate Quiz: Create multiple-choice quizzes from provided text.
Flashcards: Extract and display term-definition pairs for quick review.
Session History: Track and review past interactions.
File Upload: Support for PDF and TXT files for note summarization.

Tech Stack
Frontend/UI: Streamlit (Python-based web app framework).
AI/ML: Ollama (local LLM runner), Llama 2 (open-source language model).
Libraries: Requests (for API calls), PyPDF2 (for PDF processing), JSON (for data handling).
Environment: Python 3.11+, Windows/Linux/Mac (with Ollama installed).

Installation and Setup
Follow these steps to set up and run the project locally.

Prerequisites
Python 3.11 or 3.12 (download from python.org).
Ollama installed (download from ollama.ai).
At least 8GB RAM and 10GB free disk space for models.

Step 1: Clone or Download the Repository

Step 2: Install Python Dependencies
pip install streamlit requests PyPDF2

Step 3: Set Up Ollama
Install Ollama from ollama.ai and run the installer.
Pull the Llama 2 model:
ollama pull llama2
Start the Ollama server in a separate terminal:
ollama serve
Keep this running in the background.

Step 4: Run the Application
streamlit run app.py

Open the provided local URL (e.g., http://localhost:8501) in your browser.
The app is now ready to use!

Usage
Launch the App: Run streamlit run app.py and navigate to the local URL.
Navigate Tabs:
Explain Topic: Enter a topic (e.g., "Photosynthesis") and click "Explain" for an AI-generated summary.
Summarize Notes: Paste text or upload a PDF/TXT file, then click "Summarize".
Generate Quiz: Provide text, set the number of questions in the sidebar, and generate quizzes.
Flashcards: Input text to extract term-definition pairs.
History: View past sessions.
Settings: Use the sidebar to adjust quiz/flashcard counts or clear history.
Troubleshooting: If features fail, ensure Ollama is running (ollama serve).

Example Workflow
Upload a PDF of biology notes.
Summarize it for quick review.
Generate a 5-question quiz to test knowledge.
Use flashcards for memorization.
Screenshots/Demo
[Add screenshots here, e.g., app interface, quiz generation]
Demo Video: [Link to YouTube or hosted video showing the app in action]

Project Structure

ai-study-buddy/
├── app.py                 # Main Streamlit application
├── README.md              # This file
├── requirements.txt       # Python dependencies (optional)
└── assets/                # Screenshots or additional files (optional)

Challenges and Solutions
API Reliability: Initially used external APIs (e.g., Hugging Face), but switched to local Ollama for stability and privacy.
Hardware Constraints: Optimized for CPU; added progress bars for user feedback.
Model Quality: Fine-tuned prompts to improve output accuracy.
Future Improvements
Add model selection (e.g., Mistral or Gemma via Ollama).
Implement user feedback ratings for generated content.
Integrate vector databases for advanced retrieval-augmented generation (RAG).
Deploy to Streamlit Cloud or a VPS for remote access.
Contributing
Contributions are welcome! Fork the repo, make changes, and submit a pull request. For major changes, open an issue first.

License
This project is licensed under the MIT License. See LICENSE for details.

Acknowledgments
Ollama for local LLM support.
Streamlit for the web framework.
Llama 2 model from Meta (via Ollama).

