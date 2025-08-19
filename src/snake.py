from .element import Element
from collections import deque
from .direction import Directions

class Snake:
    def __init__(self,head: Element) -> None:
        self.deque = deque()
        self.deque.appendleft(head)
        self.direction = Directions.RIGHT
    
    def set_direction(self,new_direction: Directions) -> None:
        if len(self.deque) == 1 or new_direction.value%2 != self.direction.value %2:
            self.direction = new_direction

    def enqueue(self,head:Element) -> None:
        self.deque.appendleft(head)

    def dequeue(self) -> None:
        self.deque.pop()
        
    def get_new_head(self) -> Element:
        head = self.deque[0]
        if self.direction == Directions.UP:
            return Element(head.x,head.y+1)
        elif self.direction == Directions.RIGHT:
            return Element(head.x+1,head.y)
        elif self.direction == Directions.LEFT:
            return Element(head.x-1,head.y)
        else:
            return Element(head.x,head.y-1)
        
    def is_contains(self,e:Element) -> bool:
        try:
            self.deque.index(e)
            return True
        except ValueError:
            return False
        
        
                