from linkedListStack import LinkedListStack

stack = LinkedListStack()

stack.push(11)
stack.push(22)
stack.push(33)
stack.push(44)

stack.print_stack()

# Print the top element
print("\nTop element is ", stack.peek())

# Delete top element
stack.pop()
stack.pop()
stack.print_stack()

print("\nTop element is ", stack.peek())