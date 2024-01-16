# LinkedIn Data Scraper and Email Personalization

## Overview

This project utilizes Beautiful Soup and Selenium to scrape LinkedIn data, extracting various details about a person, including their name, headline, section, top skills, experience, and education. The extracted data is then stored in JSON format for easy visualization and analysis.

For personalized email generation, the project integrates a perplexity AI library, enhancing the ability to create engaging and contextually relevant email content based on LinkedIn data.

## Features

### LinkedIn Data Extraction:

- Name
- Headline
- About
- Top Skills
- Experience
- Education

### Data Storage:

All extracted data is stored in a structured JSON format.

### Email Personalization:

Utilizes a perplexity AI library for generating personalized email content.

## Getting Started

### Prerequisites

- Python 3.11
- Beautiful Soup
- Selenium
- [Perplexity AI Library](link to the library if applicable)

### Install Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/linkedin-scraper.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

In the `utils.py` file, provide your LinkedIn email and password. This information is required to fetch the page source from the given URL.

## Usage

Run the `main.py` script:

```bash
python main.py
```

The main file is `main.py`. After running this, you will get the email generated, and it will also be saved in a `.txt` file in the same directory.

When prompted, choose whether to scrape the same LinkedIn account or a different one (enter "1" for "Yes" and "0" for "No"). If the account is the same, the code will use the last saved data in the JSON file without fetching the page source again. If the account is different, provide the LinkedIn profile URL when prompted, and the code will fetch the page source and update the JSON file accordingly.
