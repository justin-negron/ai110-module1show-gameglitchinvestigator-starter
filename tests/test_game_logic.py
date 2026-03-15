import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score


# ── check_guess tests ──

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_gives_lower_hint():
    # Bug #2: hints are swapped — "Go HIGHER!" appears when guess is too high
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"When guess is too high, hint should say LOWER, got: {message}"


def test_guess_too_low_gives_higher_hint():
    # Bug #2: hints are swapped — "Go LOWER!" appears when guess is too low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"When guess is too low, hint should say HIGHER, got: {message}"


def test_check_guess_with_string_secret():
    # Bug #8: even attempts pass secret as string, causing type mismatch
    # check_guess should work correctly with int guess and int secret only
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"
    # Comparing int guess to string secret should not produce correct results
    outcome_str, _ = check_guess(50, "50")
    assert outcome_str == "Win", "check_guess should handle string secret gracefully"


# ── get_range_for_difficulty tests ──

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_hard_range_is_harder_than_normal():
    # Bug #7: Hard returns (1, 50) which is easier than Normal (1, 100)
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, (
        f"Hard range (1-{hard_high}) should be larger than Normal (1-{normal_high})"
    )


# ── parse_guess tests ──

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."


def test_parse_none():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert err == "Enter a guess."


def test_parse_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."


def test_parse_float_string():
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3


# ── update_score tests ──

def test_score_win_first_attempt():
    # Bug #9: formula uses (attempt_number + 1), so attempt 1 gives 100 - 10*2 = 80 instead of 90
    score = update_score(0, "Win", 1)
    assert score == 90, f"Winning on attempt 1 should give 90 points, got {score}"


def test_score_win_second_attempt():
    score = update_score(0, "Win", 2)
    assert score == 80, f"Winning on attempt 2 should give 80 points, got {score}"


def test_score_win_minimum_points():
    # Even at high attempt numbers, minimum win score should be 10
    score = update_score(0, "Win", 20)
    assert score == 10


def test_score_too_low_always_deducts():
    score = update_score(100, "Too Low", 1)
    assert score == 95


def test_score_too_high_consistent():
    # Score penalty for "Too High" should be consistent, not depend on even/odd attempt
    score_odd = update_score(100, "Too High", 1)
    score_even = update_score(100, "Too High", 2)
    assert score_odd == score_even, (
        f"Too High penalty should be consistent: attempt 1 gave {score_odd}, attempt 2 gave {score_even}"
    )
