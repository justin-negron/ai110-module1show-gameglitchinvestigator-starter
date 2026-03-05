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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

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
