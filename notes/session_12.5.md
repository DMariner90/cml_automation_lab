# 📘 Session 12.5 – Python Fundamentals Sandbox  
**Date:** Sep 21, 2025  
**Milestone:** 2 – Python for Network Automation  

---

## 📝 What I Learned  
- Reinforced Python fundamentals: `+=`, `if/else`, `for`, `while`, `range()`, `len()`.  
- Learned how to add **inline comments** and always check **expected results**.  
- Built reusable functions to classify devices and model retry behavior.  
- Combined counters, loops, and conditionals into real-world automation logic.  

---

## 💻 Code & Concepts Practiced  
```python
failures = 0                # Counter with +=
if device.startswith("R"):  # String method for classification
while attempt <= 3:          # Retry loops with increment
for vlan in range(10, 16):   # Iteration over VLANs
len(devices)                 # Count devices in a list
def classify_device():       # Function for reusability
🔎 Review / Recap
Counters (+=) → track attempts or events.

Conditionals → branch logic for device types.

Loops → repeat actions until success/failure.

Functions → centralize and reuse code.

The stretch challenge showed how to blend these tools into an automation workflow.

⚡ Troubleshooting
IndentationError → fix by aligning code blocks consistently.

Infinite loop → ensure += 1 inside while loops.

Logic errors → misplaced break can cut loops short.

🧪 Challenge Labs
Count routers with +=.

Simulate SSH retries with a while loop.

Create VLANs with range(10, 16).

✅ All challenges solved with loops, counters, and conditions.

🆕 Stretch Challenge
Task: Simulate SSH attempts for Routers, Switches, and Firewalls.

Routers succeed on attempt 1.

Switches succeed on attempt 2.

Firewalls always fail after 3 attempts.

Key Learning:

Nested loops + functions model real retry logic.

Success/failure counters build a clean summary.

✅ Expected Result: 4 successes, 1 failure.

🧠 Self-Check + ✅ Answers
+= updates counters efficiently.

break exits loops early.

.startswith("R") returns True/False for classification.

range(3) prints 0, 1, 2.

Functions reduce duplication and make logic reusable.

len(["R1","SW1","FW1"]) = 3.

False → range(1, 5) = 1, 2, 3, 4.

📚 Glossary
Counter (+=) → Increment an existing value.

Condition (if/else) → Decide based on truth values.

Loop (for/while) → Repeat until stop condition.

Function (def) → Encapsulate logic for reuse.

💭 Last Thoughts
This was the toughest session so far but also the most rewarding.
The stretch challenge forced me to combine functions, loops, counters, and logic into a realistic automation task.
Confidence is growing: I can now see how these Python fundamentals apply directly to network automation.


