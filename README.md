# 🎯 Great Number Game

A simple number guessing game built with **Flask** and **Python**.  
The app picks a random number between 1–100, and you have **5 attempts** to guess it.

##  How to Play

1. The app picks a secret number between **1 and 100**
2. Enter your guess and click **Submit**
3. You get feedback: **Too Low**, **Too High**, or **Correct!**
4. You have **5 attempts** — use them wisely
5. Click **Play again** to reset and start a new game

---
## 📁 Project Structure

```
project/
│
├── app.py                  # Main Flask app
└── templates/
    └── index.html          # Game UI
```

---

## ⚙️ App Logic

| Route | Method | Description |
|---|---|---|
| `/` | GET | Starts a new game, resets session |
| `/guess` | POST | Handles the user's guess |

### Session Variables

| Variable | Description |
|---|---|
| `secret_number` | The random number (1–100) |
| `attempts` | Number of guesses so far |
| `game_over` | True if won or ran out of attempts |
| `won` | True if the user guessed correctly |

---

