import sys

def process_line(line, metrics):
    try:
        parts = line.split()
        ip, date, status, size = parts[0], parts[3][1:], int(parts[8]), int(parts[9])
        metrics['total_size'] += size
        metrics['status_counts'][status] = metrics['status_counts'].get(status, 0) + 1
    except (IndexError, ValueError):
        pass

def print_statistics(metrics):
    print(f"Total file size: {metrics['total_size']}")

    for status_code in sorted(metrics['status_counts']):
        print(f"{status_code}: {metrics['status_counts'][status_code]}")

def main():
    metrics = {'total_size': 0, 'status_counts': {}}
    lines_processed = 0

    try:
        for line in sys.stdin:
            process_line(line.strip(), metrics)
            lines_processed += 1

            if lines_processed % 10 == 0:
                print_statistics(metrics)
                metrics = {'total_size': 0, 'status_counts': {}}

    except KeyboardInterrupt:
        print_statistics(metrics)
        sys.exit(0)

if __name__ == "__main__":
    main()
