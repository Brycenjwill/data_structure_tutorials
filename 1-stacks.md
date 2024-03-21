# Stacks


## Visualizing stacks
Stacks as a data structure are much like physical stacks that you could see in an office. Imagine what you would be able to do with a stack of five papers. You could add papers to the stack, but most likely only by putting them on top of the stack. You could remove papers from the stack, but you would probably do this by removing the top paper from the stack. This is how stacks function in programming.

## Last in, First out.
As mentioned, in programming only the "top" item of a stack can be accessed. What this means is that the last item put into a stack will be the first removed. This means that the first item put into a stack may have to wait a while for all other items to be removed before it can be accessed.

## Where Do We Use Stacks?
The above explination might make you wonder why stacks would ever be useful as a data structure, given the rules on how they can be accessed. One way in which stacks are used in every program you ever write (without you knowing) is in the running function stack. Take a look at this code below:
```
def hello():
    print("Hello, world!")


def main():
    hello()

main()
```
As you see, there are two functions defined, a main() function, as well as a hello() function. When the main function runs, it will call the hello() function. As you know, the code within the hello() function will be run, while the main() function waits for this to be finished. In this case, python will actually keep track of the currently running functions using a "call stack", so that the program will wait until the latest function call finishes before continuing onwards with whatever was happening before.

## Inserting Into a Stack
As mentioned before, you can only add to the top, or "back", of a stack. We use the push(value) function to push a value to the back of a stack.
**Note: We can simulate stacks in python by using the built in list data type.**

Here is some code for adding an item to the end of a stack. . .
```
my_stack = []

my_stack.push(1)
```
Efficiency: Adding to the end of a stack is O(1)
## Removing From a Stack
Once again, we can only remove froma stack by taking the item off the top / the "back" of the stack. In python, we can do this using the pop() function.

Here is some code for removing an item from the end of a stack. . .
```
my_stack = []
my_stack.push(1)
my_stack.pop()
```
Efficiency: Removing from a stack is O(1)


## Other Useful Stack Functions
### size() - Will return the size of a stack - O(1)
### empty() - Will return true if the stack is empty - O(1)


# Problems
Solve these two problems USING STACKS to show that you have learned the data structure.

## Problem 1:

