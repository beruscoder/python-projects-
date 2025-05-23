class quiz:
    
    def __init__(self):
        self.thisdict = {
            "what is biggest animal": "whale",
            "what is the king of jungle": "lion",
            "what is the mans bestfriend": "dog"
        }
        self.marks = 0
        print("Welcome to the quiz!")
        self.question()

    def question(self):
        for i, j in self.thisdict.items():
            print(i)
            self.answer = input("Enter your answer: ").strip().lower()  # Convert input to lowercase
            if self.answer == j.lower():  # Compare with lowercase dictionary value
                self.marks += 1
        self.percentage = (self.marks / len(self.thisdict)) * 100
        print(f"Percentage: {self.percentage:.2f}%")

quiz()



