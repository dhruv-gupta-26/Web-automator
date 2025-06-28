import sys
import webbrowser

# Define URL sets
URLS = {
    "work": [
        "https://www.google.com",
        "https://www.leetcode.com"
    ],
    "personal": [
        "https://www.youtube.com",
        "https://mubi.com/en/in",
        "https://www.reddit.com"
    ],
    "research": [
        "https://arxiv.org",
        "https://scholar.google.com"
    ]
}

def open_webpages(urls):
    print("Opening the following websites:")
    for url in urls:
        print(f"- {url}")
        webbrowser.open_new_tab(url)

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in URLS:
        print("Usage: python script.py <set_name>\n")
        print("Available sets:")
        for set_name in URLS:
            print(f"- {set_name}")
        sys.exit(1)

    selected_set = sys.argv[1]
    open_webpages(URLS[selected_set])
