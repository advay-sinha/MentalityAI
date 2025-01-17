# 🧠 Intelligent Mental Health Chatbot

A chatbot powered by AI to provide empathetic conversations, mood tracking, and mental health resources. This project was developed during a 3-day hackathon to showcase how technology can promote mental well-being.

---

## 🚀 Features
- **Empathetic Chatbot**: Uses AI to provide supportive and empathetic responses.
- **Mood Tracking**: Allows users to log their emotions and visualize mood trends.
- **Resource Recommendations**: Offers curated mental health resources based on user input.
- **Crisis Detection**: Identifies signs of distress and suggests professional help.

---

## 🛠️ Tech Stack
### **Frontend**
- React.js
- Material-UI / Tailwind CSS
- Chart.js (for visualizations)

### **Backend**
- Flask / Django
- GPT-4 (via OpenAI API) or Hugging Face Transformers
- MongoDB / Firebase (for database)

---

## 📂 Project Structure
frontend/
  src/
    components/ # Reusable React components
    pages/ # Pages like Chatbot, Mood Tracker
    App.js # Main app file
    index.js # Entry point
  public/
backend/
├── app.py                # Main backend server
├── utils/
│   ├── azure_speech.py   # Helper for Azure Speech Service
│   ├── azure_personalizer.py  # Helper for Azure Personalizer
│   ├── azure_qna.py      # Helper for Azure Language Question Answering
├── requirements.txt      # Python dependencies

