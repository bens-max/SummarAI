# 📄 SummarAI

SummarAI is a Python-based AI PDF summarizer that extracts text from PDF documents and generates concise summaries using a locally running Large Language Model (LLM) through Ollama and Gemma. The project is designed as the foundation for a future intelligent document assistant.

> **Current Version:** v1.0 (Terminal Application)

---

## ✨ Features

- 📄 Extracts text from PDF files
- 🤖 Generates AI-powered summaries using Ollama + Gemma
- ✅ Detects unsupported file formats
- ✅ Handles missing files gracefully
- ✅ Detects empty PDF files
- ✅ Validates user input
- 💻 Runs completely locally (No cloud API required)

---

## 🛠️ Technologies Used

- Python 3
- PyPDF
- Ollama
- Gemma
- Virtual Environment (venv)

---

## 📁 Project Structure

```
SummarAI/
│
├── main.py
├── pdf_handler.py
├── summarizer.py
├── requirements.txt
├── README.md
├── .gitignore
└── input/
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/SummarAI.git
cd SummarAI
```

### 2. Create a virtual environment

Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Install Ollama

Download and install Ollama from

https://ollama.com/

After installation, pull the Gemma model:

```bash
ollama pull gemma3
```

Verify it is installed:

```bash
ollama list
```

---

## ▶️ Running the Project

Run:

```bash
python main.py
```

Enter the PDF filename when prompted.

Example:

```
Enter the file name:
sample.pdf
```

The application will:

1. Validate the file
2. Extract text
3. Generate an AI summary
4. Display the summary in the terminal

---

## ⚠️ Current Limitations

Version 1.0 supports:

- Text-based PDF files only
- Terminal interface
- Single document summarization

Currently not supported:

- Scanned PDFs
- OCR
- DOCX
- PPTX
- Images
- Batch processing

---

## 🔮 Planned Features

- Web Interface
- OCR support for scanned PDFs
- Question Answering over documents
- Chapter-wise summaries
- Bullet-point summaries
- Heading extraction
- Multi-file support
- Drag & Drop upload
- Export summary
- REST API

---

## 📸 Example Workflow

```
User
   │
   ▼
Enter PDF filename
   │
   ▼
Validate file
   │
   ▼
Extract text using PyPDF
   │
   ▼
Send text to Ollama (Gemma)
   │
   ▼
Receive summary
   │
   ▼
Display summary
```

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Benson Cherian Suresh**

Third Year Computer Science Engineering Student

Project: **SummarAI**
