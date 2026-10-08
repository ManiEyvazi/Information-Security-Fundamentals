# Makefile for converting lab.md to PDF and HTML

# Source file
SRC = лаб.md

# Output files
PDF = лаб.pdf
HTML = лаб.html

# Pandoc options for PDF
PDF_OPTIONS = --pdf-engine=xelatex -V mainfont="Arial"

# Default target: build both PDF and HTML
all: $(PDF) $(HTML)

# Rule to create PDF
$(PDF): $(SRC)
	pandoc "$(SRC)" -o "$(PDF)" $(PDF_OPTIONS)

# Rule to create HTML
$(HTML): $(SRC)
	pandoc "$(SRC)" -o "$(HTML)"

# Clean up generated files
clean:
	rm -f $(PDF) $(HTML)

# Phony targets (targets that are not actual files)
.PHONY: all clean

# Optional: rebuild everything
rebuild: clean all