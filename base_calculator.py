# Advanced Mix-Language Calculator (Version 3.0: Object-Oriented)

import math

class Calculator:
    """
    Yeh class Calculator ki saari functionality aur data (memory) ko handle karti hai.
    """

    def __init__(self):
        """
        __init__ method Class ke shuru hone par chalta hai aur data ko set karta hai.
        """
        # Memory ko Class ka hissa (instance variable) bana diya gaya hai.
        self.memory = 0.0 
        print("✅ Calculator Ready! / Calculator taiyar hai!")
  # --- Input Validation and Utility Methods ---

    def get_float(self, prompt):
        """
        Ek number input leta hai, validation karta hai, aur 'M' ke liye memory check karta hai.
        """
        while True:
            try:
                val = input(prompt).strip()
                if val.lower() in ("exit", "quit"):
                    return None
                
                # 'M' ke liye self.memory ka istemal
                if val.lower() == 'm':
                    print(f" (Memory: {self.memory}) ", end="")
                    return self.memory
                
                return float(val)
            except ValueError:
                print("⚠ Invalid number! Bara-e-meharbani sirf number dein. (Please enter a valid number or 'M' for Memory)")

    def get_positive_int(self, prompt):
        """
        Ek non-negative integer input leta hai.
        """
        # (Purana logic, Class ke andar)
        while True:
            try:
                val = input(prompt).strip()
                if val.lower() in ("exit", "quit"):
                    return None
                n = int(val)
                if n < 0:
                    print("⚠ Ghalat! Negative number nahi chalega. (Enter a non-negative integer.)")
                    continue
                return n
            except ValueError:
                print("⚠ Invalid input! Bara-e-meharbani integer dein. (Please enter an integer)")
   def get_float_list(self, prompt):
        """
        Space-separated numbers leta hai aur unhe float list mein convert karta hai.
        """
        print(prompt)
        s = input("Numbers: ").strip()
        if not s:
            print("⚠ No numbers entered.")
            return None
        try:
            nums = [float(x) for x in s.split()]
            return nums
        except ValueError:
            print("⚠ Invalid number in input. Please enter numbers only.")
            return None

    def pause(self):
        """
        Screen rokne ka method.
        """
        input("\nPress Enter to continue... / Agay barhne ke liye Enter dabain...")

    def update_result(self, res):
        """
        self.memory ko update karta hai.
        """
        # self.memory Class ke data ko access karta hai.
        self.memory = res
        print(f"Result: {res}  →  Jawab: {res}")
        print(f"✅ Result saved to Memory (M). / Jawab Yaad-daasht (M) mein save ho gaya.")
   # --- Operation Methods ---

    def addition(self):
        a = self.get_float("Enter first number (or 'M'): ")
        if a is None: return
        b = self.get_float("Enter second number (or 'M'): ")
        if b is None: return
        res = a + b
        self.update_result(res)

    def subtraction(self):
        a = self.get_float("Enter first number (or 'M'): ")
        if a is None: return
        b = self.get_float("Enter second number (or 'M'): ")
        if b is None: return
        res = a - b
        self.update_result(res)
    
    # (Baqi sare operations (multiplication, division, square, power_xy, etc.) isi tarah badlenge: 
    # self.get_float() aur self.update_result() ka istemal karte hue.)

    def multiplication(self):
        a = self.get_float("Enter first number (or 'M'): ")
        if a is None: return
        b = self.get_float("Enter second number (or 'M'): ")
        if b is None: return
        res = a * b
        self.update_result(res)

    def division(self):
        a = self.get_float("Enter dividend (first number or 'M'): ")
        if a is None: return
        b = self.get_float("Enter divisor (second number or 'M'): ")
        if b is None: return
        if b == 0:
            print("⚠ Error! Division by zero is not allowed. / Zero se taqseem mumkin nahi.")
            return
        res = a / b
        self.update_result(res)

    def square(self):
        a = self.get_float("Enter number to square (or 'M'): ")
        if a is None: return
        res = a ** 2
        self.update_result(res)
        
    def power_xy(self):
        a = self.get_float("Enter base (X or 'M'): ")
        if a is None: return
        b = self.get_float("Enter exponent (Y or 'M'): ")
        if b is None: return
        try:
            res = a ** b
            self.update_result(res)
        except OverflowError:
            print("⚠ Result is too large. / Jawab bohat bara hai.")

    def percentage(self):
        value = self.get_float("Enter the value (or 'M'): ")
        if value is None: return
        percent = self.get_float("Enter percentage (% or 'M'): ")
        if percent is None: return
        res = (value * percent) / 100.0
        self.update_result(res)

    def table_1_to_10(self):
        n = self.get_float("Enter number for table (1 to 10 or 'M'): ")
        if n is None: return
        try:
            n_int = int(n)
        except:
            n_int = n
        print(f"\nTable of {n_int}: / {n_int} ka table:")
        for i in range(1, 11):
            print(f"{n_int} x {i} = {n_int * i}")
        print() 
   def square_root(self):
        a = self.get_float("Enter number for square root (or 'M'): ")
        if a is None: return
        if a < 0:
            print("⚠ Cannot compute square root of negative number. / Manfi number ka sqrt nahi nikal sakte.")
            return
        res = math.sqrt(a)
        self.update_result(res)

    def factorial_calc(self):
        n = self.get_positive_int("Enter a non-negative integer for factorial: ") 
        if n is None: return
        try:
            res = math.factorial(n)
            self.update_result(res)
        except (ValueError, OverflowError):
            print("⚠ Error computing factorial (value may be too large).")

    def absolute_value(self):
        a = self.get_float("Enter number to get absolute value (or 'M'): ")
        if a is None: return
        res = abs(a)
        self.update_result(res)

    def maximum_minimum(self):
        nums = self.get_float_list("Enter numbers separated by space (e.g., 5 3 9 1):")
        if nums is None: return
        
        mx = max(nums)
        mn = min(nums)
        print(f"Maximum: {mx}  →  Zyada: {mx}")
        print(f"Minimum: {mn}  →  Kam: {mn}")
        self.update_result(mx) 

    def average_list(self):
        nums = self.get_float_list("Enter numbers separated by space (e.g., 2 3 4):")
        if nums is None: return

        avg = sum(nums) / len(nums)
        self.update_result(avg)
        
    def run_menu(self):
        """
        Menu dikhane aur user ki pasand par operation chalane ka method.
        """
        while True:
            print("\n-----------------------------")
            print("     ADVANCED PY CALCULATOR")
            # Memory ko Class ke data se dikhana
            print(f"     MEMORY (M): {self.memory:.2f}") 
            print("-----------------------------")
            print("1. Addition (+)        → جمع")
            print("2. Subtraction (-)     → تفریق")
            print("3. Multiplication (*)  → ضرب")
            print("4. Division (/)        → تقسیم")
            print("5. Square (X²)         → مربع")
            print("6. Power (X^Y)         → طاقت")
            print("7. Percentage (%)      → فیصد")
            print("8. Table (1 to 10)     → جدول")
            print("9. Square Root (sqrt)  → جذر")
            print("10. Factorial (fact)   → فیکٹوریل")
            print("11. Absolute (abs)     → مطلق")
            print("12. Max / Min (list)   → زیادہ/کم")
            print("13. Average (list)     → اوسط")
            print("14. Clear Memory (C)   → یادداشت صاف") 
            print("0. Exit                → باہر نکلیں")
            choice = input("Choose an option: ").strip().lower()

            # ... choices mein self.method() call karna ...
            if choice in ("1", "+", "addition"):
                self.addition()
            elif choice in ("2", "-", "subtraction"):
                self.subtraction()
            elif choice in ("3", "*", "multiplication"):
                self.multiplication()
            elif choice in ("4", "/", "division"):
                self.division()
            elif choice in ("5", "square", "x^2", "x²"):
                self.square()
            elif choice in ("6", "power", "x^y"):
                self.power_xy()
            elif choice in ("7", "percentage", "perc", "%"):
                self.percentage()
            elif choice in ("8", "table"):
                self.table_1_to_10()
            elif choice in ("9", "sqrt", "square root"):
                self.square_root()
            elif choice in ("10", "fact", "factorial"):
                self.factorial_calc()
            elif choice in ("11", "abs", "absolute"):
                self.absolute_value()
            elif choice in ("12", "maxmin", "max / min", "max", "min"):
                self.maximum_minimum()
            elif choice in ("13", "avg", "average"):
                self.average_list()
            elif choice in ("14", "c", "clear"):
                self.memory = 0.0 # Class data ko seedha badalna
                print("✅ Memory cleared! / Yaad-daasht saaf ho gayi.")
            elif choice in ("0", "exit", "quit"):
                confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
                if confirm == "y":
                    print("Exiting... Goodbye! / Khuda hafiz!")
                    break
                else:
                    print("Cancelled. Returning to menu. / Wapis menu par ja rahe hain.")
            else:
                print("⚠ Invalid choice! Ghalat option diya hai. / Please try again.")

            self.pause()

if __name__ == "__main__":
    # Naya: Pehle Calculator ka object banana
    my_calculator = Calculator() 
    # Naya: Phir us object ka method call karna
    my_calculator.run_menu()






