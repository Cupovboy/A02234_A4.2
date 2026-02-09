"""
This module calculates descriptive statistics from a text file.
It computes mean, median, mode, standard deviation, and variance.
"""
# pylint: disable=invalid-name
import sys
import time

def compute_statistics(numbers):
    """Computes statistics using basic math."""
    number_len = len(numbers)
    if number_len == 0:
        return None
    # Mean
    total_sum = 0
    for x in numbers:
        total_sum += x
    mean = total_sum / number_len
    # Median
    sorted_nums = sorted(numbers)
    if number_len % 2 == 0:
        median = (sorted_nums[number_len // 2 - 1] + sorted_nums[number_len // 2]) / 2
    else:
        median = sorted_nums[number_len // 2]
    # Mode
    counts = {}
    for x in numbers:
        counts[x] = counts.get(x, 0) + 1
    max_count = 0
    for count in counts.values():
        if count > max_count:
            max_count = max(max_count, count)
    modes = [val for val, count in counts.items() if count == max_count]
    mode = modes[0] if len(modes) == 1 else modes
    # Variance
    sum_sq_diff = 0
    for x in numbers:
        sum_sq_diff += (x - mean) ** 2
    variance = sum_sq_diff / number_len
    # Standard Deviation
    std_dev = variance ** 0.5
    return {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Std Dev": std_dev
    }

def main():
    """
    Main entry point of the script. 
    """
    start_time = time.time()
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        return

    filename = sys.argv[1]
    numbers = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if not word:
                    continue
                try:
                    numbers.append(float(word))
                except ValueError:
                    print(f"Error: Invalid data found and skipped: '{word}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    stats = compute_statistics(numbers)
    end_time = time.time()
    elapsed_time = end_time - start_time

    if stats:
        # Prepare result string
        results = (
            f"--- Statistics for {filename} ---\n"
            f"Mean: {stats['Mean']}\n"
            f"Median: {stats['Median']}\n"
            f"Mode: {stats['Mode']}\n"
            f"Variance: {stats['Variance']}\n"
            f"Standard Deviation: {stats['Std Dev']}\n"
            f"Execution Time: {elapsed_time:.4f} seconds\n"
        )

        # Print to console
        print(results)

        # Write to file
        with open("StatisticsResults.txt", "a", encoding='utf-8') as out_file:
            out_file.write(results + "\n")
    else:
        print("No valid numerical data to process.")

if __name__ == "__main__":
    main()
    