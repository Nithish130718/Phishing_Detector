
# A python code implementation to detect if a given website url is of a phishing site or not and if the site is safe to use or not.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Function to scrape SEO metrics from a URL
def scrape_seo_metrics(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad response status

        soup = BeautifulSoup(response.text, "html.parser")

        # Scrape title tag
        title_tag = soup.find("title").text.strip()

        # Scrape meta description tag
        meta_description = soup.find("meta", attrs={"name": "description"})
        meta_description = (
            meta_description["content"].strip() if meta_description else None
        )

        # Scrape meta keywords tag
        meta_keywords = soup.find("meta", attrs={"name": "keywords"})
        meta_keywords = (
            meta_keywords["content"].strip().split(",") if meta_keywords else []
        )

        # Scrape number of backlinks (hypothetical)
        backlinks_count = len(soup.select(".backlink"))

        # Scrape number of internal links
        internal_links_count = len(soup.find_all("a", href=True))

        # Scrape number of external links
        external_links_count = len(
            soup.find_all("a", href=lambda href: href and "http" in href)
        )

        # Scrape number of images
        images_count = len(soup.find_all("img"))

        # Scrape number of headings (h1, h2, h3, etc.)
        headings_count = len(soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]))

        # Scrape number of paragraphs
        paragraphs_count = len(soup.find_all("p"))

        return {
            "title": title_tag,
            "meta_description": meta_description,
            "meta_keywords": meta_keywords,
            "backlinks_count": backlinks_count,
            "internal_links_count": internal_links_count,
            "external_links_count": external_links_count,
            "images_count": images_count,
            "headings_count": headings_count,
            "paragraphs_count": paragraphs_count,
        }
    except Exception as e:
        print(f"Error scraping SEO metrics: {e}")
        return None


# Function to determine if a website is phishing based on SEO metrics
def is_phishing(url):
    seo_metrics = scrape_seo_metrics(url)
    if not seo_metrics:
        return False  # Unable to scrape metrics, cannot determine phishing status

    if seo_metrics.get("backlinks_count", 0) < 10:
        return True  # Consider as phishing based on low backlinks count

    if seo_metrics.get("external_links_count", 0) > 20:
        return True  # Potential phishing site with many external links

    return False  # Default to not phishing if no conditions are met


def validate_url(url):
    try:
        parsed_url = urlparse(url)
        return parsed_url.scheme in ("http", "https")
    except:
        return False


def check_ssl_certificate(url):
    try:
        response = requests.get(url)
        return response.url.startswith("https")
    except Exception as e:
        print("Error:", e)
        return False


def is_safe_to_use(url):
    return check_ssl_certificate(url) and validate_url(url)


# Example usage
if __name__ == "__main__":
    url = input("Enter URL to be tested: ")
    
    if validate_url(url):
        print("URL is valid.")
    else:
        print("URL is not valid.")
    
    if is_phishing(url):
        print(f"{url} is identified as a phishing website.")
    else:
        print(f"{url} is not identified as a phishing website.")
    
    if is_safe_to_use(url):
        print("It appears safe to use.")
    else:
        print("Exercise caution when using this website.")
