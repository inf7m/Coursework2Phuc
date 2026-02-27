# Parallel File Search Program

This repository contains a **file search application** implemented in Python, designed to demonstrate the performance differences between **sequential** and **parallel** processing. The program searches for a specified keyword across multiple text files and records the number of occurrences in log files. This project is part of PSB504IT coursework and illustrates parallel computing concepts, Amdahl’s Law, and performance analysis.

---

## Project Structure
parallel-file-search /

 main.py # Run sequential & parallel versions, measure timing, calculate speedup
sequential.py # Single-thread version
── parallel.py # Multi-thread version using ThreadPoolExecutor
── io_handler.py # File I/O: read/write files and list folder contents
── generateDataset.py # CLI script to generate text files for testing
── config.py # Configuration: DATA_FOLDER, KEYWORD, NUM_WORKERS
── data/ # Folder containing generated text files


---

## Requirements

- Python 3.8+  
- No external libraries (uses only Python standard library)  
- Works on Windows, Linux, or macOS  
- Recommended: PyCharm or terminal for execution  

---

## Configuration

Edit `config.py` to adjust:

```python
DATA_FOLDER = "data"       # Folder containing text files
KEYWORD = "error"          # Keyword to search
NUM_WORKERS = 4            # Number of threads for parallel version

