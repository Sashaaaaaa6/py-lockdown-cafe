from datetime import date
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from app.cafe import Cafe


def go_to_cafe(friends, cafe: Cafe) -> str:
    """Checks if friends can go to the cafe."""

    # 1. Перевірити, що всі вакциновані і вакцина не прострочена
    for friend in friends:
        vaccine = friend.get("vaccine")

        # Немає ключа vaccine → всі повинні бути вакциновані
        if vaccine is None:
            return "All friends should be vaccinated"

        # Є вакцина — перевірка дати
        if vaccine["expiration_date"] < date.today():
            return "All friends should be vaccinated"

    # 2. Порахувати, скільки друзів без масок
    no_mask_count = sum(1 for friend in friends if not friend.get("wearing_a_mask"))

    if no_mask_count == 0:
        return f"Friends can go to {cafe.name}"

    return f"Friends should buy {no_mask_count} masks"
