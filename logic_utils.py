def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50  # FIX: Refactored logic into logic_utils.py using Claude Agent mode. I found this by manually playing the game and noticing the sidebar range didn't match what the UI showed. Normal and Hard ranges were swapped — Hard (1-50) was easier than Normal (1-100).
    if difficulty == "Hard":
        return 1, 100  # FIX: Refactored logic into logic_utils.py using Claude Agent mode. Swapped so Hard is now the wider range, making it actually harder.
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "Correct!"

    try:
        if guess > secret:
            return "Too High", "Go LOWER!"  # FIX: Refactored logic into logic_utils.py using Claude Agent mode. I caught this by playing the game — when I guessed too high it said "Go HIGHER!" which made no sense. Swapped the hint messages so they point the right direction.
        else:
            return "Too Low", "Go HIGHER!"  # FIX: Refactored logic into logic_utils.py using Claude Agent mode. Same swap — too low now correctly says "Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "Correct!"
        if g > secret:
            return "Too High", "Go HIGHER!"
        return "Too Low", "Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number  # FIX: Refactored logic into logic_utils.py using Claude Agent mode. Claude's deep analysis found that the original formula used (attempt_number + 1), which over-penalized the player by 10 points on every win. I logged this as bug #9 in reflection.md.
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5  # FIX: Refactored logic into logic_utils.py using Claude Agent mode. The original code had an inconsistent even/odd penalty — it added +5 on even attempts and -5 on odd. Claude's pytest caught this and we made it a consistent -5 deduction.

    if outcome == "Too Low":
        return current_score - 5

    return current_score
