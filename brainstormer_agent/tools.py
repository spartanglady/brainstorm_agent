from googlesearch import search
import os

def web_search_tool(query: str) -> str:
    """
    Performs a web search to get real-world context on the topic.
    Returns a string summary of the top 3 search results.
    """
    try:
        results = []
        # Perform search, limit to 3 results
        search_results = search(query, num_results=3, advanced=True)
        
        for i, result in enumerate(search_results):
            results.append(f"Result {i+1}:\nTitle: {result.title}\nDescription: {result.description}\nURL: {result.url}\n")
            
        return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Error performing web search: {str(e)}"

def save_brainstorm_to_file(content: str, filename: str) -> str:
    """
    Saves the final brainstorming session to a local Markdown file.
    Returns a success message with the file path.
    """
    try:
        # Ensure filename ends with .md
        if not filename.endswith('.md'):
            filename += '.md'
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return f"Successfully saved brainstorming session to {os.path.abspath(filename)}"
    except Exception as e:
        return f"Error saving file: {str(e)}"
