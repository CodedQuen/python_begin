class ExpressionTree(BinaryTree):

    def __init__(self. word):
        super(ExpressionTree, self).__init__(word)

    def parsPostfix(input):
        stack = StackAsLinkedList()

        for line in input.readlines():
            for word in line.split():
                if word == "+" or word == "-"\
                        or word =="*" or word == "/":
                    result = ExpressionTree(word)
                    result.attachRight(stack.pop())
                    result.attachLeft(stack.pop())
                    stack.push(result)
                else:
                    stack.push(ExpressionTree(word))
        return stack.pop()
    parsePostfix = staticmethod(parsePostfix)
