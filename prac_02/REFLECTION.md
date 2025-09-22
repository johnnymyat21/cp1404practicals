# Reflection – Prac 02

**What did I do well?**  
I set up a clean workflow using Git + GitHub and kept my commits small with clear, imperative messages (e.g., “Add starter file”, “Add password check program”, “Refactor … to use functions”). I also followed the main-first structure and SRP: pure conversion functions in `temperatures.py`, a single `determine_result()` in `score.py`, and separate I/O in `main()`.

**What was tricky or confusing? How did I resolve it?**  
Enabling Git in PyCharm was confusing at first (I couldn’t see the Git options). I fixed it by creating a Git repository in the project, then setting my global `user.name` and `user.email` when PyCharm prompted me. I also learned the difference between **creating a repo from a template** vs. clicking “New” on GitHub—using the CP1404 template gave me the correct folder structure.

**What will I do differently next time?**  
I’ll initialise Git and make my first commit as soon as I create a project, and push earlier so I always have a remote backup. I’ll also plan functions first (names + parameters + return values) before writing any I/O code, to keep SRP and reusability.

**Git & GitHub – what new thing did I learn?**  
- The difference between **Git (local VCS)** and **GitHub (remote hosting)**.  
- How to **commit locally**, then **push** to a public repo.  
- How to **clone** a repo to another machine and continue working with full history.  
- Why we avoid committing IDE files and keep meaningful commit messages.

**How I applied functions and SRP this week**  
- `password_stars.py`: separated getting a valid password and printing stars.  
- `temperatures.py`: used two pure functions for conversions; I/O stayed in `main()`.  
- `score.py` + `score_menu.py`: one reusable `determine_result(score)` function; reused it from the menu program without rewriting logic.

**Any habits I will keep**  
Consistent function docstrings in imperative mood, underscore_lowercase file names, and pushing at the end of each prac session so my work is always accessible.
