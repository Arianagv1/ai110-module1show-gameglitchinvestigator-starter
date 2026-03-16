def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
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


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """

    #FIX: refactored logic into logic_utils.py using Claude to fix a bug where lexicographic comparison was being used instead of 
    #numeric comparison, causing incorrect hints for certain inputs (e.g., "9" vs "10").
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


#Challenge 4: Enhanced the get_temperature_hint function to provide more granular feedback
# based on how close the guess is to the secret number, using a ratio of the distance to the total range. 
# This allows for a wider variety of hints (e.g., "Scorching", "Hot", "Warm", "Lukewarm", "Cool", "Freezing") that give players a better sense of 
# their proximity to the correct answer, making the game more engaging and informative.
def get_temperature_hint(guess: int, secret: int, low: int, high: int) -> str:
    """
    Return a hot/cold emoji hint based on how close the guess is to the secret.

    Proximity is measured as a fraction of the total range.
    """
    distance = abs(guess - secret)
    range_size = high - low or 1
    ratio = distance / range_size

    if ratio < 0.05:
        return "🔥🔥🔥 Scorching! You're basically standing on it!"
    if ratio < 0.15:
        return "🔥🔥 Hot! Keep going!"
    if ratio < 0.25:
        return "🔥 Warm. Almost there."
    if ratio < 0.40:
        return "🌡️ Lukewarm… a bit further to go."
    if ratio < 0.60:
        return "🧊 Cool. Not freezing, but not lukewarm."
    return "❄️❄️ Freezing! Way off!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
