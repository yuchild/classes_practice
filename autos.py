class car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        
    def show(self):
        print(f'Model is: {self.model}')
        print(f'Color is: {self.color}')