# 🔬 DermaScan AI — Intelligent Skin Disease Detection & Tele-Dermatology Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Django-5.2+-green?logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/TensorFlow-2.16+-orange?logo=tensorflow&logoColor=white" alt="TensorFlow" />
  <img src="https://img.shields.io/badge/Google%20Gemini-AI%20Chatbot-8E75B2?logo=google&logoColor=white" alt="Google Gemini" />
  <img src="https://img.shields.io/badge/Database-MySQL-00758F?logo=mysql&logoColor=white" alt="MySQL" />
  <img src="https://img.shields.io/badge/Payments-Razorpay-0C2340?logo=razorpay&logoColor=white" alt="Razorpay" />
  <img src="https://img.shields.io/badge/Status-Active%20Development-success" alt="Status" />
</p>

---

## 🌟 Overview

**DermaScan AI** is an advanced, full-stack healthcare web application that bridges state-of-the-art computer vision with certified clinical care. It empowers patients with early detection of dermatological conditions using deep convolutional neural networks and an interactive AI skin assistant powered by Google Gemini.

When medical attention is warranted, DermaScan AI seamlessly connects patients with verified dermatologists for online appointments, encrypted tele-consultation chat with media sharing, and secure Razorpay payment processing.

---

## ✨ Key Features

### 🧠 1. AI-Driven Skin Disease Classification
- **Deep Learning Model**: Utilizes a fine-tuned **MobileNetV2** transfer learning model (`skin_cnn_mobilenetv2.h5`).
- **Instant Diagnosis**: Preprocesses skin lesion uploads in real time and classifies conditions (e.g., Bacterial Cellulitis, Impetigo, Athlete’s Foot, Nail Fungus).
- **Confidence Scores & History**: Generates probability percentages and preserves historical analysis records for medical reference.

### 💬 2. Google Gemini Dermatology Assistant
- **Context-Aware Medical Bot**: Integrated with the Google Gemini API to answer patient inquiries regarding symptoms, skin care regimens, and potential causes.
- **Conversational Memory**: Stores previous interactions to deliver continuous, personalized advice.

### 🩺 3. Telemedicine & Doctor Consultation
- **Verified Doctors**: Admin credential verification workflow (Medical Registration No. & State Medical Council checks).
- **Dynamic Scheduling**: Doctors set up custom consultation dates, time intervals, fees, and max patient capacities.
- **Token-Based Appointments**: Automated token generation upon booking confirmation.
- **Interactive Doctor-Patient Chat**: Real-time two-way messaging with support for image attachments for lesion reviews.

### 💳 4. Secure Payment Integration
- Built-in **Razorpay** checkout pipeline with server-side signature verification.
- Instant digital receipts and payment status tracking.

### 👥 5. Role-Based Access Control (RBAC)
- **Admin**: Review & verify doctor credentials, review platform analytics, resolve patient/doctor grievances, monitor feedbacks.
- **Doctor**: Manage appointment slots, conduct tele-consults, review paid patient histories, inspect patient reviews and ratings.
- **Patient**: Perform AI skin diagnostics, consult Gemini chatbot, browse verified specialists, book appointments, track bookings, rate consultations.

---

## 🛠️ Technology Stack

| Domain | Technology |
|---|---|
| **Backend Framework** | [Django](https://www.djangoproject.com/) (Python 3.12) |
| **Deep Learning** | [TensorFlow](https://www.tensorflow.org/), Keras, MobileNetV2, NumPy, Pillow |
| **Generative AI** | [Google Generative AI](https://ai.google.dev/) (Gemini API) |
| **Database** | [MySQL](https://www.mysql.com/) with `mysqlclient` |
| **Payment Gateway** | [Razorpay](https://razorpay.com/) Python SDK |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap, Responsive Glassmorphic UI |
| **Authentication & Security** | Django Auth, Role Groups, CSRF Protection, Anti-Cache Middleware |

---

## 📂 Repository Structure

```text
DermaScan-AI/
├── app/
│   ├── migrations/                # Database migration history
│   ├── context_processors.py      # Dynamic notification & stats processors
│   ├── middleware.py              # Custom security & cache management
│   ├── models.py                  # User, Doctor, Booking, Chat, Prediction schemas
│   ├── skin_cnn_mobilenetv2.h5    # Pretrained MobileNetV2 Deep Learning weights
│   ├── skintest.py                # Standalone prediction & preprocessing script
│   ├── skintrain.py               # Transfer learning & model training pipeline
│   ├── urls.py                    # App-level routing
│   └── views.py                   # Business logic (AI diagnosis, chat, payments, RBAC)
├── project/
│   ├── asgi.py                    # ASGI server configuration
│   ├── settings.py                # Global Django configurations & API integrations
│   ├── urls.py                    # Root URL dispatcher
│   └── wsgi.py                    # WSGI server configuration
├── static/                        # CSS, custom JavaScript, logos, icons, assets
├── templates/                     # Modular Django HTML templates
├── media/                         # User uploads (chat images, patient scan records)
├── .env.example                   # Environment configuration template
├── manage.py                      # Django CLI management utility
├── requirements.txt               # Project Python package dependencies
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started

Follow these steps to set up and run DermaScan AI locally on your workstation.

### 1. Prerequisites
Ensure you have the following installed on your machine:
- **Python**: Version `3.10` to `3.12` installed ([Download Python](https://www.python.org/downloads/))
- **MySQL Server**: Running on port `3306` ([Download MySQL](https://dev.mysql.com/downloads/installer/))
- **Git**: Installed ([Download Git](https://git-scm.com/downloads))

---

### 2. Clone the Repository
```bash
git clone https://github.com/nitinkalarikkal-lab/DermaScan-AI.git
cd DermaScan-AI
```

---

### 3. Create & Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies
Install all required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### 5. Configure the Database
1. Open your MySQL client and create a new database named `project`:
```sql
CREATE DATABASE project CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Confirm or update database credentials in `project/settings.py` (or through environment variables):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'project',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 6. Apply Migrations & Create Superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

### 7. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:
```text
http://127.0.0.1:8000/
```

---

## ⚙️ Environment Configuration

For security best practices, keep sensitive credentials out of version control by configuring your `.env` file (see `.env.example`):

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django unique secret key |
| `DEBUG` | Set `True` for development, `False` for production |
| `DB_NAME` | MySQL database name |
| `DB_USER` | MySQL database user |
| `DB_PASSWORD` | MySQL database password |
| `RAZORPAY_KEY_ID` | Razorpay public test/live key |
| `RAZORPAY_KEY_SECRET` | Razorpay secret test/live key |
| `GEMINI_API_KEY` | Google Gemini API key for chatbot queries |

---

## 🔬 Model Training & Inference

- **Training**: Execute `app/skintrain.py` to train or fine-tune the model with custom image sets:
  ```bash
  python app/skintrain.py
  ```
- **CLI Testing**: Test prediction on any test image directly in terminal:
  ```bash
  python app/skintrain.py
  ```

---

## ⚠️ Medical Disclaimer

> **IMPORTANT:** DermaScan AI is developed for educational, experimental, and preliminary screening assistance. The AI classification and chatbot outputs do **not** constitute official clinical diagnoses or a replacement for direct medical consultations by a certified healthcare professional. Always consult a licensed dermatologist for any concerning dermatological conditions.

---

## 📄 License & Attribution

Developed with ❤️ by [Nitin Kalarikkal](https://github.com/nitinkalarikkal-lab).  
Contributions and suggestions are warmly welcomed! Feel free to open an issue or submit a pull request.
