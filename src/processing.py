def filter_by_state(incoming_bank_data: list[dict], incoming_state: str = 'EXECUTED') -> list[dict]:
    outcoming_ids = []
    for item in incoming_bank_data:
        if item['state'] == incoming_state:
            outcoming_ids.append(item)
    return outcoming_ids


def sort_by_date(incoming_bank_data: list[dict], sorting_parameter: str = 'True') -> list[dict]:
    sorted_ids = sorted(incoming_bank_data, key=lambda item: item["date"], reverse=bool(sorting_parameter))
    return sorted_ids
