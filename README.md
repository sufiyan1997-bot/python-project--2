# 🚀 CLI Multitool: Pattern Generator & Range Analyzer

```text
  ██████╗██╗     ██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
 ██╔════╝██║     ██║    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
 ██║     ██║     ██║    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
 ██║     ██║     ██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
 ╚██████╗███████╗██║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
  ╚═════╝╚══════╝╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝
                                >> Python 3.10+ Powered <<
```

A dynamic, interactive **Python CLI (Command Line Interface) application** built for multi-functional execution. This lightweight utility seamlessly bridges geometric matrix rendering (stars and number pyramids) with algorithmic range calculations, performing quick math and parity analytics on user-defined bounds.

---

## ⚡ Core Features

* 🎛️ **Dual-Engine Architecture:** Toggle instantly between structural pattern layouts and statistical range analysis.
* 📐 **Dynamic Pattern Scaling:** Custom row input generation supporting Regular Triangles, Inverted Triangles, and uniform Number Pyramids.
* 📊 **Smart Range Diagnostics:** Live sequential execution displaying exact integer parity (`Even`/`Odd` detection) combined with cumulative arithmetic summaries.
* 🛠️ **Modern Structural Control:** Implemented natively using Python's structural `match-case` logic instead of redundant `if-elif` stacks.

---

## 📊 Application Architecture (Workflow)

```text
               ┌──────────────────────────────┐
               │    🚀 START: main.py Loop     │
               └──────────────┬───────────────┘
                              │
                    [Capture User Choice]
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
 ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
 │ 1. Patterns  │      │ 2. Analysis  │      │   3. Exit    │
 └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
        │                     │                     │
        ├─ Regular Triangle   ├─ Even / Odd Check   └─ [Break & Close]
        ├─ Inverted Triangle  └─ Cumulative Sum
        └─ Number Pyramid
```

---

## 💻 Get Started

### Prerequisites
* Ensure you have **Python 3.10** or higher installed on your system to support the structural pattern matching syntax.

### Installation & Execution
1. Clone or download this project's code script and save it locally as `main.py`.
2. Launch your command prompt, terminal, or preferred shell interface.
3. Run the application using the following command:
```bash
python main.py
```

---

## 🎨 Interface & Live Previews

### 1. Generating a Number Pyramid (Option 1 -> 3)
```text
Select Pattern Type:
1. Regular Triangle
2. Inverted Triangle
3. Number Pyramid
Enter pattern choice: 3
Enter the number of rows for the pattern: 4

Pattern:
1 
2 2 
3 3 3 
4 4 4 4 
```

### 2. Processing a Range Analysis (Option 2)
```text
Enter the start of the range: 10
Enter the end of the range: 12

Number 10 is Even
Number 11 is Odd
Number 12 is Even
Sum of all numbers from 10 to 12 is: 33
```

---

## 🛠️ Code Architecture

* **State Persistence:** Kept active using a foundational `while True` main loop context, avoiding sudden console terminations.
* **Algorithmic Parity Checking:** Utilizes binary-equivalent remainder checking (`num % 2`) to categorize numerical sets efficiently on the fly.
