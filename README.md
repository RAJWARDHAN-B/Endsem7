# Endsem7
This repository contains the study material of BE IT sem 7 Endsem 2019 pattern

## Books

The [DL](DL/Books), [Devops](Devops/Books), [ISR](ISR/Books), and
[SPM](SPM/Books) books are organized for the current syllabus's Units 3-6.
Duplicate copies and Units 1-2 material have been removed.

Files marked `Supplement` contain only matching chapters from other syllabus
editions, not complete coverage of the units named. In particular, the DL RNN
supplements support our Unit 3 but retain their source's printed Unit IV numbering.
The older SPM supplements cover activity planning, project monitoring, and staffing
(our Units 3-5); their unrelated Agile Project Management chapters are excluded.
Different publishers' explanations of the same topics are retained.

RESOURCES:

Uni-PYQ: https://drive.google.com/drive/folders/0Bz9C0ysJZ7PnMGZKeWcybUpXWGM?resourcekey=0-S2yaWXvAG7ObM_Gc8LRNTQ
Tech-neo: https://drive.google.com/drive/folders/1a_Y0QmgkL5Q4-NY-QZ8F3utDUMF4KpPw

https://drive.google.com/drive/folders/1bUKh6QLfon6vXaliS1rYTr9sj-OlDWpO

https://drive.google.com/drive/folders/1VhxyLyhSoXMp7eMsqsDSMZ6BA-Vdo62I

https://chatgpt.com/share/6b029ac6-5558-83e8-9a04-9c363dd78520

https://chatgpt.com/share/6b03a9df-7454-83ee-941c-38f47661f3aa

## Converting PDFs to images

Install the Python dependency once:

```sh
python -m pip install pymupdf
```

Convert a PDF into one PNG per page (150 DPI by default):

```sh
python scripts/pdf_to_images.py "DL/PYQ/DL_Endsem_2026_May-Jun.pdf"
```

Images are written to a sibling folder named `<pdf-name>_images`. Use `--dpi`
to change the resolution or `--output-dir` to choose another folder:

```sh
python scripts/pdf_to_images.py input.pdf --dpi 300 --output-dir rendered-pages
```