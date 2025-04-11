"""
CP1404/CP5632 Practical
Wikipedia API program
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    while True:
        search_phrase = input("Enter page title: ")
        if not search_phrase:
            break

        try:
            page = wikipedia.page(search_phrase, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(search_phrase, sentences=2, auto_suggest=False))
            print(page.url)

        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)

        except PageError:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')

    print("Thank you.")

if __name__ == "__main__":
    main()


