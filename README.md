# 📄 SummarAI

**SummarAI** is an AI-powered PDF summarization application built with Python. It extracts text from PDF documents and uses a Large Language Model (LLM) to generate concise, structured summaries that help users understand lengthy documents more efficiently.

The project began as a terminal-based application using Ollama and Gemma and is evolving into a web-based document summarization tool using Flask and the Google Gemini API.

> **Current focus:** Structured PDF summarization and a foundation for an intelligent document assistant.

## ✨ Features

- 📄 **PDF Text Extraction** — Extracts text from text-based PDF documents using PyPDF.
- 🤖 **AI-Powered Summarization** — Uses an LLM to generate concise summaries.
- 🧩 **Chunk-Based Processing** — Splits lengthy extracted text into smaller chunks for summarization.
- 📝 **Structured Summaries** — Aims to organize summaries into readable sections with headings and key points.
- 🌐 **Web Interface** — Flask-based interface for interacting with the application.
- ⚠️ **Input Validation** — Handles supported file formats and common input errors.
- 🔐 **Environment-Based Configuration** — Uses environment variables to configure API credentials.
- 🛠️ **Modular Architecture** — Separates PDF processing, summarization, and application logic.

*Note: Features listed here describe the intended/current development direction; verify each feature against the latest implementation before release.*

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Flask | Web application framework |
| PyPDF | PDF text extraction |
| Google Gemini API | Cloud-based AI summarization |
| python-dotenv | Loading environment variables |
| HTML/CSS | Web interface |
| Git and GitHub | Version control and collaboration |
| Python virtual environment | Dependency isolation |

The project originally used **Ollama and Gemma** for local inference. The current development direction is to use the Google Gemini API, reducing the need to run a local LLM.

## 🏗️ How It Works

```text
        User uploads a PDF
                |
                v
        Validate the file
                |
                v
       Extract text using PyPDF
                |
                v
       Split text into chunks
                |
                v
      Send chunks to the LLM
                |
                v
      Generate chunk summaries
                |
                v
       Combine and structure
          the summaries
                |
                v
       Display the final summary
```

## 📁 Project Structure

The structure below represents the main application components. Adjust it to match the files currently present in the repository.

```text
SummarAI/
│
├── main.py                 # Flask application and routes
├── pdf_handler.py          # PDF text extraction and processing
├── summarizer.py           # AI summarization logic
├── templates/
│   └── index.html          # Web interface template
├── static/                 # CSS and other static assets
├── input/                  # Input PDFs, if used locally
├── extracted_text/         # Extracted text, if stored locally
├── output/                 # Generated outputs, if stored locally
├── .env                    # API configuration (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Before running SummarAI, ensure you have:

- Python 3 installed.
- Git installed.
- An active internet connection for Gemini API requests.
- A Google Gemini API key.

### 1. Clone the repository

```bash
git clone https://github.com/bens-max/SummarAI.git
cd SummarAI
```

### 2. Create a virtual environment

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

You can obtain an API key through [Google AI Studio](https://aistudio.google.com/).

**Security reminder:** Never commit your `.env` file or expose your API key in source code, screenshots, logs, or public repositories.

Ensure `.env` is listed in `.gitignore`.

### 5. Run the application

If `main.py` is the Flask application's entry point:

```bash
python main.py
```

Open the local address printed by Flask in your browser. For a typical local development configuration, this may be:

```text
http://127.0.0.1:5000
```

Follow the application's interface to upload a supported PDF and generate a summary.

## 📑 Supported Documents

### Currently targeted

- Text-based PDF documents.
- Single-document summarization.

### Not currently included in the core workflow

- Scanned PDFs requiring OCR.
- Word documents (`.docx`).
- PowerPoint presentations (`.pptx`).
- Image-based document extraction.
- Batch processing of multiple documents.

Support for these formats and capabilities may be added in future versions.

## 🔮 Roadmap

SummarAI is being developed toward a more capable document assistant.

- [x] Initial terminal-based PDF summarizer.
- [x] PDF text extraction using PyPDF.
- [x] Initial AI integration with Ollama and Gemma.
- [ ] Complete and validate Gemini API integration.
- [ ] Improve summary consistency and structure.
- [ ] Refine heading and key-point extraction.
- [ ] Improve handling of long documents and chunk boundaries.
- [ ] Add document continuity detection using previously generated summaries.
- [ ] Compare new document summaries with previously processed documents.
- [ ] Generate questions from uploaded documents.
- [ ] Add chapter-wise summaries.
- [ ] Support OCR for scanned PDFs.
- [ ] Add summary export options.
- [ ] Add multi-file processing.
- [ ] Introduce a REST API.
- [ ] Improve automated testing and error handling.

*Roadmap checkboxes should be updated to reflect the features that are actually completed and tested.*

## 🔐 Security and Privacy

- API credentials should be stored in environment variables.
- The `.env` file should be excluded from version control.
- Uploaded documents and generated outputs should be handled carefully.
- API-based summarization sends document text to the configured AI provider. Avoid uploading confidential documents unless the provider's data-handling terms and your requirements permit it.
- Production deployments should use appropriate upload validation, file-size limits, and secure configuration.

## 🤝 Contributing

Contributions, bug reports, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them.
4. Submit a pull request describing your improvements.

## 📜 License

This project is intended to be distributed under the MIT License. See the repository's `LICENSE` file for the applicable license terms.

## 👨‍💻 Author

**Benson Cherian Suresh**

Third-Year Computer Science and Engineering Student

**Project:** SummarAI

- GitHub: [@bens-max](https://github.com/bens-max)
- Repository: [SummarAI](https://github.com/bens-max/SummarAI)

---

*SummarAI — Making lengthy documents easier to understand, one summary at a time.*
