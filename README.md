# 📝 Cover Letter Generator

A web-based **Cover Letter Generator** built using **Flask and Jinja2** that allows users to create professional cover letters by entering their personal and job-related details. The generated cover letter can be downloaded as a PDF.

## 🚀 Live Demo

🔗 **Deployment Link:** https://cover-letter-generator-zb8i.onrender.com/

---

## ✨ Features

- Generate personalized cover letters dynamically
- User-friendly input form
- Dynamic content rendering using Jinja2 templates
- Convert generated cover letters into PDF format
- Download cover letter instantly
- Responsive UI using HTML, CSS, and Bootstrap
- Deployed using Render

---

## 🛠️ Tech Stack

**Frontend**
- HTML5
- CSS3
- Bootstrap

**Backend**
- Python
- Flask
- Jinja2

**PDF Generation**
- xhtml2pdf

**Deployment**
- Render

---

## 📂 Project Structure

```text
Cover-Letter-Generator/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── templates/                 # HTML template files
│   ├── index.html             # User input form
│   └── letter.html            # Cover letter template
│
├── static/                    # Static files
│   ├── style.css              # Styling file
│   └── logo.png               # Website logo
│
└── venv/                      # Virtual environment (not uploaded)
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Cover-Letter-Generator.git
```

### 2. Navigate to the project directory

```bash
cd Cover-Letter-Generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

---

## 🔄 How It Works

1. User enters details such as:
   - Name
   - Email
   - Job role
   - Company name
   - Skills
   - Experience
   - Additional information

2. Flask receives the form data.

3. Jinja2 dynamically inserts user details into the cover letter template.

4. The generated HTML content is converted into a PDF using xhtml2pdf.

5. User downloads the final cover letter.

---

## 📦 Requirements

Main dependencies used:

```text
Flask
Jinja2
xhtml2pdf
gunicorn
```

---

## 🌱 Future Improvements

- Add multiple professional templates
- Add AI-powered cover letter suggestions
- Add user authentication
- Save previous generated letters
- Export cover letters as DOCX
- Improve UI/UX

---
