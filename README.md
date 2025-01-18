# 🧠 Intelligent Mental Health Chatbot : MentalityAI

A chatbot powered by AI to provide empathetic conversations, mood tracking, and mental health resources. This project was developed to showcase how technology can promote mental well-being.

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
mental_health_app/
├── backend/                     # Django Backend
│   ├── manage.py
│   ├── mental_health_app/       # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── mood_tracking/          # Mood tracking app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   │       └── __init__.py
│   ├── user_management/        # User management app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   └── views.py
│   ├── flask_services/         # Flask app for Azure services
│   │   ├── app.py              # Flask API integrating Azure services
│   │   └── utils/              # Azure integration utilities
│   │       ├── __init__.py
│   │       ├── azure_speech.py
│   │       ├── azure_personalizer.py
│   │       └── azure_qna.py
│   └── requirements.txt        # Python dependencies
├── frontend/                   # React Frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/        # Reusable components
│   │   │   └── MoodForm.js
│   │   ├── pages/             # Pages like Mood Tracker, Chatbot
│   │   │   └── MoodTracker.js
│   │   ├── App.js             # Main React component
│   │   └── index.js           # Entry point
│   └── package.json           # React dependencies
├── docker-compose.yml         # (Optional) Docker setup
├── README.md                  # Project documentation
└── .gitignore
