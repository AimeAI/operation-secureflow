# ⚙️ Installation Guide

This guide will help you set up **Operation SecureFlow** on a local machine or a secure development server.

## Prerequisites
*   **Python 3.8 or higher** installed.
*   **pip** (Python Package Installer).
*   Git (optional, for version control).

## Step-by-Step Setup

### 1. Clone the Repository
If you have the files locally, skip this. If using git:
```bash
git clone https://github.com/your-org/operation-secureflow.git
cd operation-secureflow
```

### 2. Create a Virtual Environment (Recommended)

Isolate the project dependencies to avoid conflicts.

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Libraries

Install the required Python packages listed in requirements.txt.

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Launch the Streamlit server.

```bash
streamlit run secureflow_demo.py
```

The application should automatically open in your default web browser at http://localhost:8501.

---

## Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'streamlit'`
**Solution:** Make sure you've activated your virtual environment and run `pip install -r requirements.txt`

**Issue:** Port 8501 is already in use
**Solution:** Run with a different port: `streamlit run secureflow_demo.py --server.port 8502`
