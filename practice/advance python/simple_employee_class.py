class Employee:
    """A simple class to represent an Employee."""
    
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        
    def display(self):
        """Display employee details."""
        print(f"Employee Name: {self.name}, Salary: ₹{self.salary}")

if __name__ == "__main__":
    e1 = Employee("Rahul", 50000)
    e1.display()
    
    e2 = Employee("Priya", 65000)
    e2.display()
