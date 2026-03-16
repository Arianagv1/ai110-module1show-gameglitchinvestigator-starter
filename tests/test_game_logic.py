from logic_utils import check_guess, parse_guess

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

#Challenge 1: Added tests for edge cases in parse_guess and check_guess, including negative numbers, decimals, and extremely large values.
# These tests ensure that the game logic correctly handles a wide range of user inputs and provides appropriate feedback.
# --- Negative numbers ---

def test_parse_negative_integer():
    # Negative integers are parsed successfully but fall outside 1-100
    ok, value, _ = parse_guess("-5")
    assert ok is True
    assert value == -5

def test_check_negative_guess_is_too_low():
    # A negative guess should always be too low
    outcome, _ = check_guess(-5, 1)
    assert outcome == "Too Low"

def test_parse_negative_decimal():
    # Negative decimals truncate toward zero via int(float(...))
    ok, value, _ = parse_guess("-3.7")
    assert ok is True
    assert value == -3

def test_check_negative_decimal_guess_is_too_low():
    # Truncated negative decimal is still below any valid secret
    outcome, _ = check_guess(-3, 1)
    assert outcome == "Too Low"


# --- Decimal numbers ---

def test_parse_decimal_truncates_not_rounds():
    # 42.9 should truncate to 42, not round to 43
    ok, value, _ = parse_guess("42.9")
    assert ok is True
    assert value == 42

def test_parse_decimal_exact_half():
    ok, value, _ = parse_guess("50.5")
    assert ok is True
    assert value == 50

def test_parse_decimal_just_above_100():
    # 100.1 truncates to 100, which is still in range
    ok, value, _ = parse_guess("100.1")
    assert ok is True
    assert value == 100

def test_parse_decimal_below_one_truncates_to_zero():
    # 0.9 truncates to 0, which is outside the valid 1-100 range
    ok, value, _ = parse_guess("0.9")
    assert ok is True
    assert value == 0

def test_check_zero_from_decimal_truncation_is_too_low():
    outcome, _ = check_guess(0, 1)
    assert outcome == "Too Low"


# --- Extremely large values ---

def test_parse_extremely_large_value():
    ok, value, _ = parse_guess("999999999")
    assert ok is True
    assert value == 999999999

def test_check_extremely_large_guess_is_too_high():
    outcome, _ = check_guess(999999999, 50)
    assert outcome == "Too High"

def test_parse_astronomically_large_value():
    ok, value, _ = parse_guess("10000000000000000000")
    assert ok is True
    assert value == 10000000000000000000

def test_check_astronomically_large_guess_is_too_high():
    outcome, _ = check_guess(10000000000000000000, 100)
    assert outcome == "Too High"

def test_parse_large_decimal():
    # Large decimal truncates correctly
    ok, value, _ = parse_guess("1234567890.99")
    assert ok is True
    assert value == 1234567890
