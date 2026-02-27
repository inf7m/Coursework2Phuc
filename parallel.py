

from io_handler import read_file, write_log
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_file(file, keyword): # Count the occurrences of 'keyword' in a single file
    text = read_file(file)
    count = text.lower().count(keyword.lower())
    return file, count

def run_parallel(files, keyword, num_workers=4):
    results = {}
    with ThreadPoolExecutor(max_workers=num_workers) as executor: #  Create a ThreadPoolExecutor to run file processing concurrently
        futures = [executor.submit(process_file, f, keyword) for f in files] #Submit each file as a separate task to the thread pool
        for future in as_completed(futures):
            file, count = future.result()
            results[file] = count

    write_log(results, log_file="parallel_log.txt")
    return results
