from datetime import datetime
from masks import get_mask_account, get_mask_card_number


def mask_account_card(incoming_data: str) -> str | None:
    space_counter = 0
    for symbol in incoming_data:
        if symbol == " ":
            space_counter += 1
        else:
            continue
    data_numerical_part = ''.join(s for s in incoming_data if s.isdigit())
    if len(data_numerical_part) < 4 or incoming_data == '' or len(data_numerical_part) > 20 or space_counter > 1:
        return "Invalid input"
    elif len(data_numerical_part) == 16:
        return get_mask_card_number(incoming_data)
    elif len(data_numerical_part) == 20:
        return get_mask_account(incoming_data)
    else:
        return "Incorrect card number or bank account number"


def get_date(date_and_time: str) -> str:
    format_template = "%d.%m.%Y"
    date_raw_formatted = datetime.fromisoformat(date_and_time)
    date_formatted = str(date_raw_formatted.strftime(format_template))
    return date_formatted
