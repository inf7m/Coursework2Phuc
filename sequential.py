
from io_handler import read_file, write_log


def run_sequential(files, keyword):
    """
    Search keyword in files sequentially.
    """
    results = {}
    for file in files:
        text = read_file(file)
        count = text.lower().count(keyword.lower())
        results[file] = count

    write_log(results, log_file="sequential_log.txt")
    return results
