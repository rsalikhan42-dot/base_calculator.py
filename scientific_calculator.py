# scientific_calculator.py file

import math
# --- WIRASAT KA AHAM HISS A---
# Base Class (Parent) ko import kiya gaya.
from base_calculator import Calculator 

class ScientificCalculator(Calculator):
    """
    Yeh Class Calculator se Wirasat leti hai aur Scientific functions shamil karti hai.
    """

    def __init__(self):
        # Parent (Calculator) class ka __init__ call kiya gaya.
        # Isse self.memory = 0.0 set ho jayega.
        super().__init__() 
        print("✅ Scientific Calculator Ready! (Naye functions shamil hain)")
# --- Naye Scientific Operations ---
    def sine_calc(self):
        a = self.get_float("Enter angle in degrees (or 'M'): ")
        if a is None: return
        
        # Pehle degrees ko radians mein badalna zaroori hai
        res = math.sin(math.radians(a))
        self.update_result(res)

    def log_base10(self):
        a = self.get_float("Enter number for log (or 'M'): ")
        if a is None: return
        if a <= 0:
            print("⚠ Error! Log sirf positive numbers ka nikalta hai.")
            return
        
        res = math.log10(a)
        self.update_result(res)

    def run_scientific_menu(self):
        """
        Naya menu jismein base aur scientific dono operations hain.
        """
while True:
            # Memory aur pause ke liye self.memory aur self.pause() ka istemal kiya gaya hai,
            # kyunki yeh dono Base Class se inherit hue hain.
            print("\n-----------------------------")
            print("   SCIENTIFIC PY CALCULATOR")
            print(f"     MEMORY (M): {self.memory:.2f}") 
            print("-----------------------------")
            
            # Base Class ke menu ko naye tareeqay se dikhana
            print("1. Addition (+)")
            # ... Saare purane options (2 se 13) yahan khud likhne honge ...
            print("14. Clear Memory (C)") 
            
            # Naye scientific options
            print("15. Sine (sin)")
            print("16. Log (base 10)")
            print("0. Exit")
            
            choice = input("Choose an option: ").strip().lower()

            if choice in ("15", "sin", "sine"):
                self.sine_calc()
            elif choice in ("16", "log", "log10"):
                self.log_base10()
            
            # Ab agar user purana option (masalan 1) chunta hai
            elif choice in ("1", "+", "addition"):
                # Seedha Base Class ka method call ho jayega!
                self.addition() 
            # (Aap baqi 2 se 13 options bhi isi tarah shamil kar sakte hain)
            
            elif choice in ("0", "exit"):
                break
            else:
                print("⚠ Invalid choice!")
                
            self.pause()


if __name__ == "__main__":
    # Ab hum ScientificCalculator ka object bana rahe hain
    my_scientific_calculator = ScientificCalculator() 
    # Aur naya menu chala rahe hain
    my_scientific_calculator.run_scientific_menu()
