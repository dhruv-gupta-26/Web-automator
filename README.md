#🧭 Web Automator
A simple Python script to automatically open a curated set of websites based on your context—work or personal.

🔧 What It Does
This script streamlines your workflow by launching predefined groups of websites in your default browser with a single command-line argument.

🧠 Why It’s Useful
Time-saving: Instantly opens all your go-to tabs at once.

Context-aware: Switch between work and personal environments easily.

Lightweight: No dependencies, just Python’s standard library.

Customizable: Easily modify the URLS dictionary to fit your routine.

🚀 How to Use It
Clone the repo:

bash
Copy
Edit
git clone https://github.com/yourusername/web-automator.git
cd web-automator
Run the script with the desired set:

bash
Copy
Edit
python script.py work
or

bash
Copy
Edit
python script.py personal
🛠️ Customization
Want to add your own sets?

Edit the URLS dictionary in script.py:

python
Copy
Edit
URLS = {
    "work": ["https://mail.google.com", "https://github.com"],
    "personal": ["https://reddit.com", "https://spotify.com"],
    "research": ["https://arxiv.org", "https://scholar.google.com"]
}
⚙️ Requirements
Python 3.x

A default web browser configured on your system

💡 Future Ideas (Optional)
Add GUI with Tkinter or PyQt

Support for scheduling (e.g., open at specific times)

Save/load user profiles from a JSON file

Browser-specific support (Chrome, Firefox, etc.)
