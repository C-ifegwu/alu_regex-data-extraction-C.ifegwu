#!/usr/bin/env python3
"""
===============================================
          REGEX DATA EXTRACTION TOOL
===============================================

This tool uses Regular Expressions to extract multiple types of data from a sample text.
The following data types are extracted:
  -The data indicated in the rubric are extracted 

Usage:
    python regex_extraction.py
"""

import re


def get_sample_text() -> str:
    """
    Return a sample text containing examples of all the data types to be extracted.
    
    Returns:
        str: The sample text.
    """
    return (
        "Hello, my name is John Doe. You can reach me at john.doe@example.com or "
        "jane.smith@company.co.uk. Please visit our website at https://www.example.com "
        "or check out our partner site at http://subdomain.example.org/page.\n\n"
        "For appointments, call (123) 456-7890, 123-456-7890, or 123.456.7890.\n\n"
        "Payment options include credit card numbers such as 1234 5678 9012 3456 "
        "and 1234-5678-9012-3456.\n\n"
        "Meeting times can be scheduled at 14:30 or 2:30 PM.\n\n"
        "Below are some HTML examples: <p>, <div class=\"example\">, and "
        "<img src='image.jpg' alt='description'>.\n\n"
        "Don't forget to follow us on social media: #example, #ThisIsAHashtag.\n\n"
        "Prices: Our product costs $19.99 and our premium package is $1,234.56.\n"
    )


class RegexDataExtractor:
    """
    Encapsulates regex patterns and the extraction logic for various data types.
    """
    
    def __init__(self):
        """
        Initialize the extractor with a dictionary of regex patterns.
        """
        self.regex_patterns = {
            "Email Addresses": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
            "URLs": r'https?://[^\s]+',
            "Phone Numbers": r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b',
            "Credit Card Numbers": r'\b(?:\d{4}[-\s]?){3}\d{4}\b',
            # Matches 24-hour format (e.g., 14:30) or 12-hour format (e.g., 2:30 PM)
            "Time Formats": r'\b(?:(?:[01]\d|2[0-3]):[0-5]\d|(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM|am|pm))\b',
            # Matches any HTML tag
            "HTML Tags": r'<[^>]+>',
            "Hashtags": r'#[A-Za-z0-9_]+',
            # Matches currency amounts like $19.99 or $1,234.56
            "Currency Amounts": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})'
        }

    def extract_data(self, text: str) -> dict:
        """
        Extract data from the input text using the defined regex patterns.
        
        Args:
            text (str): The input text.
        
        Returns:
            dict: A dictionary mapping each data type to its list of matches.
        """
        extraction_results = {}
        for label, pattern in self.regex_patterns.items():
            extraction_results[label] = re.findall(pattern, text)
        return extraction_results

    @staticmethod
    def display_results(results: dict) -> None:
        """
        Display the extraction results in a readable format.
        
        Args:
            results (dict): Dictionary of extracted data.
        """
        print("----- Extraction Results -----\n")
        for data_type, matches in results.items():
            print(f"{data_type}:")
            if matches:
                for match in matches:
                    print(f"  {match}")
            else:
                print("  No matches found")
            print("-" * 40)


def main():
    """
    Main execution routine:
      1. Retrieve sample text.
      2. Extract data using RegexDataExtractor.
      3. Display the extraction results.
    """
    text = get_sample_text()
    extractor = RegexDataExtractor()
    results = extractor.extract_data(text)
    extractor.display_results(results)


if __name__ == "__main__":
    main()