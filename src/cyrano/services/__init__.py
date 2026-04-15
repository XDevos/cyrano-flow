"""
Services = use-cases of the application.

A service orchestrates:
- data loading (io)
- data processing (analysis)
- and returns structured results

It should NOT:
- print (CLI responsibility)
- read user input
- depend on UI (CLI or GUI)

Examples (future):
- inspect a file
- compare two files
- analyze a plate

This layer helps share logic between:
- CLI
- GUI (Streamlit)
"""
