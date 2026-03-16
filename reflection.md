# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game has a settings column on the left side, with difficulty settings and a range and attempts allowed specifications. The right side of the screen contains an optional pop down menu for debug info, and the game itself has a textbar to enter guesses, and three buttons for submitting guesses, resetting, and showing hints.

- List at least two concrete bugs you noticed at the start
  (for example: "the secret number kept changing" or "the hints were backwards").
  The game is incorrect in answering the hints. It told me to go higher than 5 and lower than 10 and when I exhausted all possibilities, it told me that the number was 34! So the hint feature has incorrect logic. On a different round, I guessed 50,70,90 as the hints told me to go higher and once I reached 100 it told me that I still needed to go higher!

  Something else that I noticed was that the game's New game button does not work. In order to properly reset the game, I have to refesh my browser.

  Another thing I noticed is that entering guesses was not always a smooth process. It did not update in history and needed multiple button presses to get it to show up on screen.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used copilot


- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  I told the AI that the hint suggestion was wrong and I gave it a snippet of code from the app.py file which I thought might have a bug in that function. Claude told me that the actual bug was a couple of lines lower in the file, where a logical error was found. It said "Inside the except block, it does string comparison not numeric, and when "9" > "10" is TRUE, the hint feature points me in the wrong direction.


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  The AI suggested for the hinting bug, that there was a logic error in comparing the secret number to the guesser's number. Specifically, a str() function was being used which compared a str to an int, producing wrong results lexicographically. This suggestion was correct, and after reviewing the code and feeling confident the code changes would be correct, I rerun the streamlit command in the terminal and made sure that my guesses would correctly direct me towards the secret based off of the go lower/ go higher hints. 


- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  One test I ran was called: def test_hint_correct_on_win(), which ensures that no message "go lower, go higher" should print once we guess the winning number.


- Did AI help you design or understand any tests? How?
  The AI helped me understand how robust the tests should be. It was interesting that it created two kinds of assertions for a test. Since we know the outcome and its message, the AI suggested testing both, to assert our outcome should be the appropriate "too high/too low" or that our outcome should be "go higher/go lower", and even both for some tests. I think that learning how to test the check_guess function for its robustness in the messages, demonstrated how important it is to consider all parts of the function. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  A line in the file app.py had this line of code "st.session_state.secret = random.randint(1, 100)", which generated a new number if one didn't already exist. Essentially, on every subsequent rerun, the same secret survives since interacting with the app through clicking buttons causes streamlit to rerun the entire app.py script from top to bottom.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  A rerun is streamlit executing the whole script on every user interaction. Imagine a whiteboard, and when we click a button on the game, the whole whiteboard has to be erased and written from scratch. So if the secret number is calculated using random, it will be picking a new number every time. However, st.session_state will keep our values safe, so when the whiteboard is erased, our secret number for example, does not get written away with it.
- What change did you make that finally gave the game a stable secret number?
  I added an if check, that checks if secret is not in st.session_state. This means that if there is a secret saved, there is no need to 'erase the whiteboard' and create a new one, mid game for example.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I really enjoyed the prompting strategy, it challenged me to think about how I should navigate using AI, since it is a powerful tool but I have to be specific about what I want. I also enjoyed analyzing the AI, and using my own judgement to see whether or not the suggestions for code fixes could help or would complicate a bug more.


- What is one thing you would do differently next time you work with AI on a coding task?
  If I was to work with AI on a coding task for a different project, I think I will give it more of my thoughts as to why a problem is happening than having it explain it to me. Doing this in this exercise has helped challenge my own critical thinking skills, and I feel more confident in my programming skills since it challenges me to find it without help.
- In one or two sentences, describe how this project changed the way you think about AI generated code.


  For starters, a big part of this assignment challenged me to not take the AI's code blindly, since we are tasked with using AI as a helper tool and not as a means to solve everything. For example, playing the game gaveaway to bugs immediately, which meant that AI was not needed to direct me into the code fixes.
