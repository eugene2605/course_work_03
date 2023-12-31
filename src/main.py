from src.utils import get_operations, get_filtered_operations, get_sorted_operations, get_formatted_operations

operations = get_operations()

operations_filtr = get_filtered_operations(operations)

operations_sort = get_sorted_operations(operations_filtr)

operations_format = get_formatted_operations(operations_sort)
for operation in operations_format:
    print(operation)
