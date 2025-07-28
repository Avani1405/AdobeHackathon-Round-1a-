 Adobe India Hackathon — Enhanced PDF Outline Extractor
This project extracts a clean outline from messy PDFs — including the title, headings, and basic structure — automatically and accurately.

 What it does
Detects the document’s language

Smartly picks the title (big, bold, top of page)

Finds headings by analyzing font sizes, boldness, and spacing

Builds a clear H1–H4 hierarchy

Outputs everything as JSON

 How it works
1️. Parse the PDF — We use PyMuPDF to get fonts, sizes, and positions.

2. Detect the language — We grab text samples, clean them, and run langdetect.

3. Extract the title — Picks the biggest, boldest, top-most line that’s short enough to be a real title.

4. Find headings — Anything larger than body text (or bold), well-spaced, and meaningful is marked as a heading.

5. Assign levels — Bigger fonts become H1, smaller ones H2, H3, etc.

6. Save results — Title, headings, page numbers, and metadata are saved in a clean JSON file.

 Why it’s better
Handles real, messy PDFs.

Works for multiple languages.

Fast, explainable rules — no heavy models.

Easy to tweak if you need.

 Built for Adobe India Hackathon
We wanted a simple, reliable tool that turns PDFs into structured outlines with minimal fuss.
Drop in a PDF — get a clear JSON back.

