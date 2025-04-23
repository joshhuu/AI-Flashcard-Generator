# AI Flashcard Generator

An AI-powered flashcard generator that extracts key facts from provided text or PDF documents and generates question-answer pairs. This project uses the Hugging Face model `valhalla/t5-base-qg-hl` for question generation and provides a user-friendly interface via **Streamlit**.

## Features

- **Text Input**: Paste any content (e.g., paragraphs, articles) to generate flashcards.
- **PDF Upload**: Upload a PDF document, and the app will extract the text to generate flashcards.
- **Manual Keyword Input**: Enter keywords (e.g., key facts) to guide the generation of flashcards.
- **Interactive**: Flashcards are displayed in a clean, easy-to-read format.
  
## Installation

### Create a virtual environment (optional, but recommended)
```bash
python -m venv env
```

### Activate the virtual environment
- On Windows:
  ```bash
  .\env\Scripts\activate
  ```
- On MacOS/Linux:
  ```bash
  source env/bin/activate
  ```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the app

1. Start the Streamlit app by running the following command in your terminal:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. **Choose input method**: Paste text or upload a PDF file.
4. **Enter keywords**: Manually input the keywords you want to generate flashcards for.
5. **Generate flashcards**: Click "Generate Flashcards" to see the results.

### Example Input

#### Text input:
```txt
The sun is the star at the center of the solar system. It is a nearly perfect ball of hot plasma,
heated to incandescence by nuclear fusion reactions in its core. Earth and other celestial bodies revolve around it.
```

#### Keywords:
```txt
sun, nuclear fusion, solar system
```

### Output Example:
**Q:** What is the sun?  
**A:** The sun is the star at the center of the solar system.

---

## Technologies Used
- **Streamlit**: For creating the web app interface.
- **Transformers**: For utilizing the Hugging Face model (`valhalla/t5-base-qg-hl`) for question generation.
- **PyMuPDF (fitz)**: For extracting text from PDF files.
- **Python 3.x**: For the backend logic and AI processing.

## Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.
6. 
Feel free to tweak the content based on your preferences! This README will provide users with everything they need to know about the project, from setup to usage.
