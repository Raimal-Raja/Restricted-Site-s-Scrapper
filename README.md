# Restricted-Site-s-Scrapper

Python browser-assisted Indeed scraping experiment with job extraction, CSV output, and logging.

## Repository guide

### Contents

- [Multi_Country_Job_results.csv](Multi_Country_Job_results.csv)
- [README.md](README.md)
- [Scraper.py](Scraper.py)
- [requirements.txt](requirements.txt)
- [scraper.log](scraper.log)

### Getting started

```bash
git clone https://github.com/Raimal-Raja/Restricted-Site-s-Scrapper.git
cd Restricted-Site-s-Scrapper
```

Create and activate a virtual environment, then install the project dependencies:

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r "requirements.txt"
```

Application entry point:

```bash
python Scraper.py
```

### Configuration and limitations

Live scraping depends on site permissions, browser availability, current page markup, and anti-bot responses. Passing syntax checks does not verify live collection. Browser-handling code does not guarantee access.

### Validation

Reviewed on 2026-10-08. Python syntax checks passed for 1 source files. Syntax validation does not establish runtime correctness or dependency compatibility.

### Contributions

Describe the issue, reproduction steps, environment, and expected behavior when proposing a change. Keep generated environments, credentials, and unnecessary build artifacts out of new commits.

### License

No top-level license file was found during this review.
