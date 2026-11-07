def get_mask_card_number(card_number: str) -> str:
    """Функция мвскирует номер банковской карты из 16 цифр"""
    if len(card_number) != 16:
        print("Invalid card number")
    card_number_masked = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return card_number_masked


def get_mask_account(bank_account_number: str) -> str:
    """Функция маскирует номер счёта из >= 4 цифр"""
    if len(bank_account_number) < 4:
        print("Invalid bank_account_number")
    bank_account_number_masked = f"**{bank_account_number[2:]}"
    return bank_account_number_masked
