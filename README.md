# Bubble Sort Algorithm with Linked List Implementation

This project was developed as part of a programming assignment to understand and implement the **Bubble Sort** algorithm on both Python's built-in list data structure and a custom **Linked List**. The project focuses not only on sorting logic but also on how data structures behave differently when implementing the same algorithm.

---

## Project Purpose

The main goal of this project is to:
- Implement **Bubble Sort** in a modular and testable structure
- Understand the difference between **data swapping** and **node swapping** in linked lists
- Apply sorting without converting the Linked List into a Python list (i.e., no to_list or from_list)
- Gain experience in **unit testing** and **CI automation** with GitHub Actions

---


### Python List Sorting
The `bubble_sort()` function detects if the input is a standard Python list. It then applies the classic Bubble Sort algorithm by comparing adjacent elements and swapping them if needed.

### Linked List Sorting (Direct Node Swapping)
If the input is an instance of `LinkedList`, the algorithm performs Bubble Sort **by actually swapping the nodes**, not just the data. This is done through a custom method called `swap_nodes(prev, curr)` which updates `.next` pointers directly.

This approach:
- Keeps the linked structure intact
- Avoids converting the list to a Python list
- Demonstrates a deeper understanding of pointer manipulation in linked data structures

---

## How It Works

The project contains two main modules:
- `ds.py`: Contains the `Node` and `LinkedList` classes. The `LinkedList` includes:
  - `append(data)`: Adds new node
  - `__iter__()`: Makes the list iterable
  - `swap_nodes(prev, curr)`: Swaps two nodes by updating links

- `sorting_algorithms.py`: Contains the `bubble_sort()` function that handles both Python list and LinkedList inputs appropriately.

---

## Unit Testing

Unit tests were written using Python's `unittest` framework and are located in the `tests/` folder. The tests cover:
- Sorting a Python list with multiple values
- Sorting a `LinkedList` with multiple nodes
- Single-item and empty list scenarios for both data structures

To run the tests locally:

```bash
python -m unittest discover tests

##Using AI 

While doing the project, I asked CHATGPT questions for help in the parts of the assignment that I could not understand. I had problems with the functioning of the assignment. During this process, I asked questions focused on understanding the logic and solving the functioning. I asked various questions such as how linked lists work, what __iter__() does, how unit tests are structured and how GitHub Actions work automatically. In the problems and confusions I experienced, I asked different questions to teach me every detail of the assignment, explain it and help me find the solution myself, and teach me the solution when I could not find it. I used CHATGPT to help me understand the logic of the code and to teach me the parts I did not understand. The only purpose of using AI was to understand and learn the code. I used it from beginning to end for this purpose.

