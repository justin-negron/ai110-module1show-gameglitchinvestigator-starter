# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. When clicking "Submit Guess" without entering a number, we get a UI error that says "Enter a guess." but the "Attempts left" counter still decrements.
2. It seems the UI hints, "Go LOWER!" when I am too low, and "Go HIGHER!" when I am too high, which seems to be backwards logic.
3. When you win, and click "New Game", nothing happens.
4. Similiary, when you lose, and click "New Game", nothing happens.
5. The settings output does not match the Game Glitch Investigator output. 
  a. For Difficulty=Easy, it says Range: 1 to 20, and Attempts allowed: 6, but the Game Glitch UI says "Guess a number between 1 and 100. Attempts left: 5"
  b. For Difficulty=Normal, it says Range: 1 to 100, and Attempts allowed: 8, but the Game Glitch UI says "Guess a number between 1 and 100. Attempts left: 7"
  c. For Difficulty=Hard, it says Range: 1 to 50, and Attempts allowed: 5, but the Game Glitch UI says "Guess a number between 1 and 100. Attempts left: 4
6. As the "Attemps left: " counter decrements, when reaching "1" in any Difficulty, the UI outputs an error saying "Out of attempts!" and displays score.
7. Hard difficulty range (1-50) is easier than Normal (1-100), which does not make sense since a smaller range means fewer possibilities.
8. On even-numbered attempts, the secret number is converted to a string before comparison, causing intermittent hint/win behavior due to type mismatch.
9. The score formula uses `attempt_number + 1` instead of `attempt_number`, penalizing the player an extra 10 points on every win.

---

## 2. How did you use AI as a teammate?

I used Claude Code (Agent mode) as my primary AI tool for this project. I manually played through the game in each difficulty, documented every bug I found in this reflection, and then brought Claude in to help locate each defect in the codebase and collaborate on fixes.

**Correct AI suggestion:** Claude correctly identified that the "New Game" button wasn't resetting `status`, `score`, or `history` in session state — only `attempts` and `secret` were being reset. That's why clicking "New Game" after a win or loss did nothing; the status was still "won" or "lost" so `st.stop()` blocked the UI. I verified this by reading the original code at lines 134-138 of app.py, where only two fields were reset. After Claude added the missing resets, I clicked "New Game" after both winning and losing and confirmed it worked.

**Incorrect/misleading AI suggestion:** When I asked Claude to fix the Hard difficulty range, it initially suggested changing Hard to `(1, 200)` on its own. That wasn't what I wanted — I needed Normal to be 50 and Hard to be 100, essentially swapping the two ranges so the progression made sense (Easy=20, Normal=50, Hard=100). I rejected the edit and clarified what the correct values should be. Claude then applied the fix I described. This taught me that AI suggestions need to be checked against your own understanding of the design, not just accepted.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by running both manual tests in the Streamlit UI and automated tests with pytest. For manual testing, I played through each difficulty, submitted empty guesses, won games, lost games, and clicked "New Game" after each — basically retracing every scenario from my bug list in section 1.

For automated testing, Claude generated 17 pytest cases in `tests/test_game_logic.py` that targeted every bug we identified. When we first ran them against the broken code, 6 tests failed — each one proving a specific defect: the swapped hints, the wrong Hard range, the off-by-one score formula, and the inconsistent "Too High" penalty. After applying fixes to `logic_utils.py`, we re-ran pytest and watched the failures drop to 0. That gave me confidence the logic was solid.

Claude helped design the tests by writing assertions that described the *correct* behavior rather than what the buggy code was doing. For example, `test_guess_too_high_gives_lower_hint` asserts that `"LOWER"` appears in the message when the guess is too high — which failed against the original swapped hints. This approach made the tests serve double duty: they proved the bugs existed before the fix, and confirmed they were gone after.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
