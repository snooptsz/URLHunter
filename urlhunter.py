from googlesearch import search

def find_files(query):
    """
    Searches for files online using Google Search.

    Args:
        query: The search terms for finding files.

    Returns:
        A list of URLs containing potentially relevant files of any type.
    """
    # We don't specify any file type in the search term
    search_term = query
    results = search(search_term)  # Removed num_results argument
    return results

def main():
    """
    Prompts the user for a search query and displays results.
    """
    query = input("Enter your search query: ")
    try:
        file_links = find_files(query)
        if file_links:
            print("Found files:")
            for link in file_links:
                print(link)
        else:
            print("No files found for your query.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
