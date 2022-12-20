class Stack:
    def __init__(self):
        self.stack_data = []

    def __str__(self):
        return self.stack_data


    def is_empty(self):
        return bool(self.stack_data)

    def push(self, new_lm):
        self.stack_data.append(new_lm)

    def pop(self):
        return self.stack_data.pop()

    def peek(self):
        return self.stack_data[-1]

    def size(self):
        return len(self.stack_data)



def balance(string: str):
    stack = Stack()
    if len(string) % 2 == 0:
        for i in string:
            if i == "{" or i == "[" or i == "(":
                stack.push(i)
            elif i == "}" and stack.peek() == "{":
                stack.pop()
            elif i == "]" and stack.peek() == "[":
                stack.pop()
            elif i == ")" and stack.peek() == "(":
                stack.pop()
        if not stack.stack_data:
            return "Сбалансированно"

        else:
            return "Несбалансированно"
    else:
        return "Несбалансированно"


print(balance("(((([{}]))))"))
print(balance("[([])((([[[]]])))]{()}"))
print(balance("{{[()]}}"))
print(balance("}{}"))
print(balance("{{[(])]}}"))
print(balance("[[{())}]"))