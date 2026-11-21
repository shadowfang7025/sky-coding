def filter_by_state(incoming_bank_data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция фильтрует банковские ID, в зависимости от указанного статуса"""
    outcoming_ids = []
    for item in incoming_bank_data:
        if item['state'] == state:
            outcoming_ids.append(item)
    return outcoming_ids


def sort_by_date(incoming_bank_data: list[dict], sorting_parameter: str = 'True') -> list[dict]:
    """Функция сортирует банковские ID в зависимости от даты и параметра сортировки"""
    sorted_ids = sorted(incoming_bank_data, key=lambda item: item["date"], reverse=bool(sorting_parameter))
    return sorted_ids
