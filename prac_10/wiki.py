"""
CP1404/CP5632 Practical
Wikipedia API & Python Library
"""

import wikipedia


def main():
    """Interact with Wikipedia API to get page information."""
    print("Wikipedia Search")
    
    # Continue prompting for page titles until blank input
    title = input("Enter page title: ")
    while title:
        try:
            # Try to get the page with the given title
            page = wikipedia.page(title, auto_suggest=False)
            # If successful, print the page's title, summary, and URL
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle case where title is too ambiguous
            print("We need a more specific title. Try one of the following, or a new search:")
            print("(BeautifulSoup warning) ")
            print(e.options[:5] + ["..."])  # Print first 5 options to avoid excessive output
        except wikipedia.exceptions.PageError:
            # Handle case where the page doesn't exist
            print(f'Page id "{title}" does not match any pages. Try another id!')
        
        # Prompt for the next title
        print()
        title = input("Enter page title: ")
    
    print("Thank you.")


if __name__ == "__main__":
    main()
