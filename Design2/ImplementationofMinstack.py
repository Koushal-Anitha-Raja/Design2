class MinStack:

    def __init__(self):
        #Initializing the  first stack 
        self.stack=[]
        #Initializing the "Minstack" stack
        self.minstack=[]
        
    def push(self, val: int) -> None:
        #appending all the values to the primary stack 
        self.stack.append (val)
        #if the minstack is empty then follow further more
        if len(self.minstack)==0:
            self.minstack.append(val)
            #if the new entering value is lesser than the older minimum value in stack then further go through the process
        else:    
            if self.minstack[-1]>val:
            #if it is lesser then append the value to the top of minstack
                self.minstack.append(val)
            else:
                #otherwise append the older top value of minstack
                self.minstack.append(self.minstack[-1])
                
                
    def pop(self) -> None:
        #remove the top off the element from stack 
        self.stack.pop()
        #remove the top of element from minstack
        self.minstack.pop()
        

    def top(self) -> int:
        #remove the top element of the stack (ie) removing the first element from the stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        #removing the top element from the minstack (ie) remove the least element 
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()