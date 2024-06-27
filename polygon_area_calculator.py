class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        params = ', '.join([
            f"{i}={getattr(self, i)}" for i in vars(self)
        ])
        return f'{self.__class__.__name__}({params})'

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
        output = ('*'*self.width +'\n' for _ in range(0,self.height))
        return ''.join(output)

    def get_amount_inside(self):
        pass

class Square:
    def __init__(self, width):
        super().__init__()


if(__name__=='__main__'):
    rect1 = Rectangle(9,5)
    print(str(rect1) + '\n')
    print(rect1.get_picture())
