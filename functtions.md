Now that we’ve had a chance to study function basics in Python, let’s begin this chapter with a few words of context. When you start using functions in earnest, you’re faced with choices about how to glue components together—for instance, how to decompose a task into purposeful functions (known as cohesion), how your functions should communicate (called coupling), and so on. You also need to take into account concepts such as the size of your functions, because they directly impact code usability. Some of this falls into the category of structured analysis and design, but it applies to Python code as to any other.

Few general guidelines for readers new to function design principles:
- Coupling: use arguments for inputs and return for outputs. Generally, you
should strive to make a function independent of things outside of it. Arguments
and return statements are often the best ways to isolate external dependencies to
a small number of well-known places in your code.
- Coupling: use global variables only when truly necessary. Global variables
(i.e., names in the enclosing module) are usually a poor way for functions to communicate.
They can create dependencies and timing issues that make programs
difficult to debug, change, and reuse.
- Coupling: don’t change mutable arguments unless the caller expects it.
Functions can change parts of passed-in mutable objects, but (as with global variables)
this creates a tight coupling between the caller and callee, which can make
a function too specific and brittle.
- Cohesion: each function should have a single, unified purpose. When designed
well, each of your functions should do one thing—something you can summarize
in a simple declarative sentence. If that sentence is very broad (e.g., “this
function implements my whole program”), or contains lots of conjunctions (e.g.,
“this function gives employee raises and submits a pizza order”), you might want
to think about splitting it into separate and simpler functions. Otherwise, there is
no way to reuse the code behind the steps mixed together in the function.
- Size: each function should be relatively small. This naturally follows from the
preceding goal, but if your functions start spanning multiple pages on your display,
it’s probably time to split them. Especially given that Python code is so concise to
begin with, a long or deeply nested function is often a symptom of design problems.
Keep it simple, and keep it short.
- Coupling: avoid changing variables in another module file directly. We introduced
this concept in Chapter 17, and we’ll revisit it in the next part of the book
when we focus on modules. For reference, though, remember that changing variables
across file boundaries sets up a coupling between modules similar to how
global variables couple functions—the modules become difficult to understand
and reuse. Use accessor functions whenever possible, instead of direct assignment
statements.

