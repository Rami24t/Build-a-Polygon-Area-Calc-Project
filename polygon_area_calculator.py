class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5

    def get_picture(self):
        output = ''
        if self.width > 50 or self.height > 50:
            output = "Too big for picture."
        else:
            output = ''.join('*'*self.width +'\n' for _ in range(0,self.height))
        return output

    def get_amount_inside(self, other):
        if self.width >= other.width and self.height >= other.height:
            return self.width//other.width * self.height//other.height
        return 0
    
    def __repr__(self):
        params = ', '.join([
            f"{i}={getattr(self, i)}" for i in vars(self)
        ])
        return f'{self.__class__.__name__}({params})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
        
    def __repr__(self):
        return f"{self.__class__.__name__}(side={self.width})"


# Usage examples
if(__name__=='__main__'):
    sq1 = Square(3) # output: 5.656854249492381
    print(str(sq1) + '\n')
    print(sq1.get_picture())
    # output:
    # ***
    # ***
    # ***

    rect = Rectangle(10, 5)
    print(rect.get_area()) # output: 50
    rect.set_height(3)
    print(rect.get_perimeter()) # output: 26
    print(rect) # output: Rectangle(width=10, height=3)
    print(rect.get_picture())
    # output:
    # **********
    # **********
    # **********

    sq2 = Square(9)
    print(sq2.get_area()) # output: 81
    sq2.set_side(4)
    print(sq2.get_diagonal()) # output: 5.656854249492381
    print(sq2) # output: Square(side=4)
    print(sq2.get_picture())
    # output:
    # ****
    # ****
    # ****
    # ****

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq2)) # output: 8
