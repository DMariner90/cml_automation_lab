# 📘 Session 12 – While Loops & Counters  
**Date:** Sep 20, 2025  
**Milestone:** 2 – Python for Network Automation  

---

## 📝 What I Learned  
- How `while` loops work by repeating actions until a condition is false.  
- The role of **counters** (`+=`) inside loops to avoid infinite loops.  
- How to combine loops and conditionals to model login retries.  
- The importance of cleanup after loops (resetting counters or breaking out).  

---

## 💻 Code & Concepts Practiced  
```python
attempt = 1
max_attempts = 3

while attempt <= max_attempts:     # Loop runs while condition is True
    print(f"Attempt {attempt}: SSH failed")
    attempt += 1                   # Increment to avoid infinite loop
python
Copy code
# Example with conditional success
attempt = 1
while attempt <= 3:
    if attempt == 2:               # Success condition
        print(f"Attempt {attempt}: SSH success")
        break                      # Exit loop early
    else:
        print(f"Attempt {attempt}: SSH failed")
    attempt += 1
🔎 Review / Recap
while loops run until the condition is no longer true.

Counters (+=) prevent infinite loops by changing the condition.

break lets you exit a loop early when a success condition is met.

Loops are a natural fit for retry logic (SSH logins, API retries).

⚡ Troubleshooting
Infinite loop → forgot to increment the counter.

Loop ends too soon → incorrect condition in while.

break misplaced → can skip logic unexpectedly.

🧪 Challenge Labs
Simulate 3 failed SSH attempts with a while loop.

Add logic: success on attempt 2, break early.

✅ Both labs showed how while + counters + conditionals combine.

🧠 Self-Check + ✅ Answers
What happens if you forget attempt += 1 in a while loop?
→ Infinite loop.

What does break do inside a loop?
→ Exits the loop immediately.

How many times does this loop run?

python
Copy code
x = 0
while x < 5:
    x += 1
→ 5 times.

📚 Glossary
while loop → Executes as long as condition is True.

counter → A variable that increments inside the loop.

break → Exits the loop before the condition becomes False.

💭 Last Thoughts
This session focused on while loops and counters, which are essential for retries and monitoring tasks in network automation.
It was a good step-up from if/else and for loops, showing how to add control and safety to repeated tasks.
