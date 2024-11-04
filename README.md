# Phishing_Detector

```markdown

## Overview

This tool is designed to analyze URLs for potential phishing threats by scraping various SEO metrics and checking the safety of the website. It utilizes requests and BeautifulSoup to gather information about the webpage and determines whether the site is safe to use based on SSL certificates and phishing indicators.

## Features

- Scrapes SEO metrics such as:
  - Title
  - Meta Description
  - Meta Keywords
  - Backlinks Count
  - Internal Links Count
  - External Links Count
  - Images Count
  - Headings Count
  - Paragraphs Count
- Checks for the validity of the URL.
- Verifies the presence of SSL certificates.
- Determines if the website is potentially phishing based on SEO metrics.

## Installation

To use this tool, ensure you have Python installed along with the necessary libraries. You can install the required packages using pip:
```
```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script.
2. Run the script using Python.

```bash
python phishing_detection.py
```

3. Enter the URL you want to test when prompted.

### Example Usage

```plaintext
Enter URL to be tested: https://etherscan.org
URL is valid.
Error scraping SEO metrics: 'NoneType' object has no attribute 'text'
https://etherscan.org is not identified as a phishing website.
It appears safe to use.
```

## Error Handling

If the tool encounters issues while scraping SEO metrics, it will display an error message indicating the problem. In the example provided, an error occurred due to a missing title tag in the HTML content.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to submit a pull request.

## Acknowledgements

- [Requests](https://docs.python-requests.org/en/master/) - For making HTTP requests easier.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - For parsing HTML and XML documents.
```
