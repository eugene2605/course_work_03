import json
from datetime import datetime


def get_operations():
    """
    получает информацию из файла operations.json
    :return: список словарей с операциями
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations_json = file.read()
        operations = json.loads(operations_json)
    return operations


def get_filtered_operations(data):
    """
    получает только выполненные ("EXECUTED") операции
    :param data: список словарей с операциями, полученный с помощью функции get_operations
    :return: отфильтрованный список словарей
    """
    operations_filtr = []
    for operation in data:
        if "state" in operation and operation["state"] == "EXECUTED":
            operations_filtr.append(operation)
    return operations_filtr

def get_sorted_operations(data):
    """
    получает отсортированный по дате по убыванию список словарей
    :param data: список словарей с операциями, полученный с помощью функции get_filtered_operations
    :return: отсортированный список словарей
    """
    def key_sorted(x):
        return x['date']
    operations_sort = sorted(data, key=key_sorted, reverse=True)
    return operations_sort[:5]


def get_formatted_operations(data):
    """
    получает список, подготовленный к выводу, согласно задания
    :param data: отсортированный при помощи функции get_sorted_operations список словарей
    :return: список словарей, готовый к выводу
    """
    for operation in data:
        date_old = operation['date']
        date_formatted = datetime.strptime(date_old, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        to_list = operation['to'].split()
        check_to = to_list[0]
        number_to_before = to_list[1]
        number_to = '*' * 16 + number_to_before[-4:]
        if 'from' in operation:
            from_list = operation['from'].split()
            number_from_before = from_list[-1]
            if len(number_from_before) != 16:
                number_from = '*' * 16 + number_from_before[-4:]
                card_or_check = from_list[0]
            else:
                number_from = f'{number_from_before[:4]} {number_from_before[4:6]}** **** {number_from_before[-4:]}'
                card_or_check = ' '.join(from_list[:2]) if len(from_list) == 3 else from_list[0]
            print(f'{date_formatted} {operation["description"]}\n{card_or_check} {number_from}-> {check_to} {number_to}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
        else:
            print(f'{date_formatted} {operation["description"]}\n{check_to} {number_to}\n{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
