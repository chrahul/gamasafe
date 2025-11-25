
"""
hedge_engine.py
--------------------
Validates and manages hedge positions for short strangles.

TODO:
- Ensure sufficient gap between hedge & short legs
- Add logic to auto-adjust hedge during high IV
"""

def validate_hedges(short_legs: dict, hedge_legs: dict, config: dict) -> bool:
    """
    Validates if hedge strikes follow rules:
    - Minimum distance
    - Acceptable premium
    """
    # TODO: implement validation logic
    return True
