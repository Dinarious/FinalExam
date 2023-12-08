def read_file(file_path):
    from_file = []
    with open(file_path, 'r') as file:
        for line in file:
            from_file.append(line.strip())
    return from_file

def filter_results(results, threshold):
    filtered_results = []
    for result in results:
        time, value = result.split(' ')
        hours, minutes = map(int, time.split(':'))
        if float(value) > threshold:
            filtered_results.append(f"{hours:02d}:{minutes:02d}")
    return filtered_results


file_path = "file.txt"
threshold = float(input("Введіть значення ААА: "))
try:
    results = read_file(file_path)
    filtered_results = filter_results(results, threshold)
    if filtered_results:
        print("Часи коли значення перевищує AAA:")
        for result in filtered_results:
            print(result)
    else:
        print("Немає результатів, що перевищують AAA")
except Exception as e:
    print(f"An error occurred: {e}")