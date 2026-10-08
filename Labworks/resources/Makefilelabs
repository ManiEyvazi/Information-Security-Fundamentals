# Makefile for converting lab.md to PDF and HTML

# Source file
SRC = lab.md

# Output files
PDF  = lab.pdf
HTML = lab.html

# Pandoc options for PDF - Changed font to a more reliable option
PDF_OPTIONS = --pdf-engine=xelatex \
              -V mainfont="Times New Roman" \
              -V lang=ru \
              --resource-path=. \
              --resource-path=media

# Default target: build both PDF and HTML
all: $(PDF) $(HTML)

# Rule to create PDF
$(PDF): $(SRC)
	pandoc "$(SRC)" -o "$(PDF)" $(PDF_OPTIONS)

# Rule to create HTML
$(HTML): $(SRC)
	pandoc "$(SRC)" -o "$(HTML)" --standalone --metadata lang=ru

# Clean up generated files (Windows-friendly)
clean:
	-del /Q "$(PDF)" "$(HTML)" 2>NUL

# Optional: rebuild everything
rebuild: clean all

# Phony targets (targets that are not actual files)
.PHONY: all clean rebuild