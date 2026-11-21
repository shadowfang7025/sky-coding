def filter_by_state(incoming_bank_data: list[dict], incoming_state: str = 'EXECUTED') -> list[dict]:
    outcoming_ids = []
    for item in incoming_bank_data:
        if item['state'] == incoming_state:
            outcoming_ids.append(item)
    return outcoming_ids