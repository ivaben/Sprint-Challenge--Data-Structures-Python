class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cur = 0
        self.data = []
             
    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.cur]= item
        else:
            self.data.append(item)
        self.cur= (self.cur + 1) % self.capacity
                
    def get(self):
        data_items = []
        # append an element at the end of the buffer if the data_items is None
        [data_items.append(item) for item in self.data if item is not None]
        # Return a list of elements from the oldest to the newest
        return data_items
        
        
        