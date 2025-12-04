from datetime import date
from typing import List, Dict, Any
from app.cafe import Cafe


def go_to_cafe(friends: List[Dict[str, Any]], cafe: Cafe) -> str:
    """Return decision for a group of friends about going to the cafe."""
    for friend in friends:
        vaccine = friend.get("vaccine")

        if vaccine is None:
            return "All friends should be vaccinated"

        if vaccine["expiration_date"] < date.today():
            return "All friends should be vaccinated"

    no_mask_count = sum(
        1 for friend in friends if not friend.get("wearing_a_mask")
    )

    if no_mask_count == 0:
        return f"Friends can go to {cafe.name}"

    return f"Friends should buy {no_mask_count} masks"
