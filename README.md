# Bubble Sort with Linked List

In this project, I implemented the **bubble sort algorithm** for both regular Python lists and a custom **linked list** data structure. The process included:

- Creating the `Node` and `LinkedList` classes from scratch
- Writing a bubble sort function that works with both data types
- Designing unit tests to verify the correctness of the implementation
- Setting up a GitHub Actions workflow to automatically test the code on every push

---

## Usage of `__iter__()`

To make the `LinkedList` class iterable, I implemented the `__iter__()` method.  
This allows me to loop through the linked list using a `for` loop or convert it to a list using `list(my_linked_list)`.

It simplifies traversal and testing, making the linked list behave more like a native Python structure.

---

## Difference Between Error and Failure in Unit Testing

While testing:

- An **error** happens when something breaks during the test run (e.g., missing methods, incorrect attributes).
- A **failure** means the test ran, but the expected and actual results didn't match.

> ✅ Failure = Assertion didn't hold  
> ❌ Error = Unexpected crash or exception

---

## GitHub Actions

I used GitHub Actions to automate testing.  
The `.github/workflows/python-tests.yml` file ensures that every commit or pull request triggers automated tests.  
This guarantees the stability and correctness of the codebase over time.

---

## AI Usage Statement

## Using AI

While doing the project, I asked **CHATGPT** questions for help in the parts of the assignment that I could not understand. I had problems with the functioning of the assignment. During this process, I asked questions focused on understanding the logic and solving the functioning. I asked various questions such as how linked lists work, what `__iter__()` does, how unit tests are structured and how GitHub Actions work automatically. In the problems and confusions I experienced, I asked different questions to teach me every detail of the assignment, explain it and help me find the solution myself, and teach me the solution when I could not find it. I used **CHATGPT** to help me understand the logic of the code and to teach me the parts I did not understand. The only purpose of using AI was to understand and learn the code. I used it from beginning to end for this purpose.


---

## Author

**Arife Nur Çakır**  
Computer Engineering – Hacettepe University  
Spring Semester, 2025  

