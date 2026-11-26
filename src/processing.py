def filter_by_state(incoming_bank_data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрует банковские ID, в зависимости от указанного статуса"""
    filtered_operations = []
    for item in incoming_bank_data:
        if item['state'] == state:
            filtered_operations.append(item)
    return filtered_operations


def sort_by_date(incoming_bank_data: list[dict], reverse_by_date: bool = True) -> list[dict]:
    """Функция сортирует банковские ID в зависимости от даты и параметра сортировки"""
    sorted_operations = sorted(incoming_bank_data, key=lambda item: item["date"], reverse=reverse_by_date)
    return sorted_operations
