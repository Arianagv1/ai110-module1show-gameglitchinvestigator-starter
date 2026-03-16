from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Hint direction tests ---

def test_hint_says_lower_when_guess_is_too_high():
    # Guess is above secret — player should be told to go lower
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_hint_says_higher_when_guess_is_too_low():
    # Guess is below secret — player should be told to go higher
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_hint_direction_single_digit_vs_two_digit():
    # Regression: lexicographic comparison would make "9" > "10" (wrong).
    # Numeric comparison must be used: 9 < 10, so hint should be Go HIGHER.
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_direction_two_digit_vs_three_digit():
    # Regression: lexicographic comparison would make "20" > "100" (wrong).
    # Numeric comparison must be used: 20 < 100, so hint should be Go HIGHER.
    outcome, message = check_guess(20, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_hint_correct_on_win():
    # A winning guess should not produce a directional hint
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert "HIGHER" not in message
    assert "LOWER" not in message
