# LinkedIn Data Scraper and Email Personalization

## Overview

This project utilizes Beautiful Soup and Selenium to scrape LinkedIn data, extracting various details about a person, including their name, headline, about section, top skills, experience, and education. The extracted data is then stored in JSON format for easy visualization and analysis.

For personalized email generation, the project integrates a perplexity AI library, enhancing the ability to create engaging and contextually relevant email content based on the LinkedIn data.

## Features

- **LinkedIn Data Extraction:**
  - Name
  - Headline
  - About
  - Top Skills
  - Experience
  - Education

- **Data Storage:**
  - All extracted data is stored in a structured JSON format.

- **Email Personalization:**
  - Utilizes a perplexity AI library for generating personalized email content.

## Getting Started

### Prerequisites

- Python 3.x
- Beautiful Soup
- Selenium
- [Perplexity AI Library] (link to the library if applicable)

### Install Dependencies

Before running the application, ensure you have the required dependencies installed. Follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/linkedin-scraper.git
   
2. Install dependencies:

   ```bash
   pip install -r requirements.txt

### Configuration
In the utils.py file, provide your LinkedIn email and password. This information is required to fetch the page source from the given URL.

