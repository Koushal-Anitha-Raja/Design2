class MyHashSet:

    def __init__(self): 
        #length of the primary array
        self.length=1000
        #Initializing the primary array which contains pointer to the secondary array or null
        self.primary= [None] * self.length
        
    def hashkey(self,key):
        #the hash f unction for the primary array 
        return key%self.length
    
    def doublehashkey(self,key):
        #if the length changes example(10^5), then primary array will be 10 ^3 and secondary array will be 10 ^2
        return key//self.length 

    def add(self, key: int) -> None:
        #hash index for the primary array
        hash_index=self.hashkey(key)
        #hash index for secondary array
        double_hash_index=self.doublehashkey(key)
        #if the primary key is not empty
        if self.primary[hash_index]==None:
            if hash_index==0:
                #inserting it in the first index
                self.primary[hash_index]= [False] * (self.length+1)
            else:
                #inserting it in the remaining index other than first array
                 self.primary[hash_index]= [False] * self.length
         #assigning the secondary array with true values           
        self.primary[hash_index][double_hash_index]= True         
                
            
        

    def remove(self, key: int) -> None:
       #hash index for the primary array
        hash_index=self.hashkey(key)
        #hash index for secondary array
        double_hashindex=self.doublehashkey(key)
        #check if the secondary array  is created or not 
        if self.primary[hash_index]!=None:
            #delete the element from the secondary index if primary index is present
            self.primary[hash_index][double_hashindex]= False

    def contains(self, key: int) -> bool:
       #hash index for the primary array
        hash_index=self.hashkey(key)
        #hash index for secondary array
        double_hashindex=self.doublehashkey(key)
        #check if the secondary array  is created or not 
        if self.primary[hash_index]!=None:
            #returns the boolean value if the key exists in the hashset or not 
               return self.primary[hash_index][double_hashindex]
            
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)