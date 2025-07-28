import os
import json
import argparse
import time
from round1a.outline_extractor_enhanced import OutlineExtractorEnhanced
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def main():
    parser = argparse.ArgumentParser(description="Adobe India Hackathon Project - Enhanced Version")
    parser.add_argument("--input_dir", type=str, default="/app/input",
                        help="Input directory containing PDF files.")
    parser.add_argument("--output_dir", type=str, default="/app/output",
                        help="Output directory for JSON results.")
    parser.add_argument("--enable_profiling", action="store_true",
                        help="Enable performance profiling.")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs(args.input_dir, exist_ok=True)

    pdf_files = [f for f in os.listdir(args.input_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in {args.input_dir}")
        return

    print(f"Executing Round 1A: Outline Extraction for PDFs in {args.input_dir}")
    extractor = OutlineExtractorEnhanced(enable_profiling=args.enable_profiling)
    print("Using Enhanced Outline Extractor")

    # Process PDFs
    for pdf_file in pdf_files:
        pdf_path = os.path.join(args.input_dir, pdf_file)

        output_filename = os.path.splitext(pdf_file)[0] + ".json"
        output_path = os.path.join(args.output_dir, output_filename)

        print(f"Processing {pdf_file}...")
        start_time = time.time()
        outline = extractor.extract_outline(pdf_path)
        processing_time = time.time() - start_time

        print(f"  Processing time: {processing_time:.2f} seconds")
        print(f"  Detected language: {outline['metadata']['detected_language']}")
        print(f"  Total headings: {outline['metadata']['total_headings']}")

        with open(output_path, "w") as f:
            json.dump(outline, f, indent=4)

        print(f"  Outline saved to {output_path}")


if __name__ == "__main__":
    main()
