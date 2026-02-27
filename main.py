
import time
from config import KEYWORD, DATA_FOLDER, NUM_WORKERS
from sequential import run_sequential
from parallel import run_parallel
from io_handler import get_all_files


def main():
    print("=== Parallel File Search Program ===")

    # Get files
    files = get_all_files(DATA_FOLDER)
    print(f"Total files found: {len(files)}")
    if len(files) == 0:
        print("No files found. Please generate dataset first.")
        return

    # Sequential part/ calling the sequential program
    print("\nRunning Sequential Version...")
    start = time.perf_counter()
    run_sequential(files, KEYWORD)
    end = time.perf_counter()
    seq_time = end - start
    print(f"Sequential Time: {seq_time:.4f} seconds")

    # Parallel part/ calling the parallel program
    print(f"\nRunning Parallel Version with {NUM_WORKERS} workers...")
    start = time.perf_counter()
    run_parallel(files, KEYWORD, NUM_WORKERS)
    end = time.perf_counter()
    par_time = end - start
    print(f"Parallel Time: {par_time:.4f} seconds")

    # Calculate the Speedup
    if par_time > 0:
        speedup = seq_time / par_time
        print(f"\nSpeedup: {speedup:.2f}x")

    print("\nProgram finished.")


if __name__ == "__main__":
    main()
