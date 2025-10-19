# base_calculator.py
"Yeh file Calculator project ki Parent Class (buniyadi dhaancha) hai. Is mein Calculator Class shamil hai jo saare arithmetic operations, input validation, aur memory management (self.memory) ko handle karti hai. Yeh Class Inheritance ke liye tayyar hai."
 Base Class Added: Calculator class includes core arithmetic logic, input validation, and memory management (self.memory).📄 README.md.🧱 Base Class: base_calculator.pyCategoryContentRoleYeh file Calculator Class ki tareef (definition) karti hai aur Parent Class ke taur par kaam karti hai.Key Features1. Core Arithmetic: Saare buniyadi operations (Addition, Subtraction, Division). 2. Robust Input: Methods jaise get_float() aur get_float_list() ke zariye zaroori input validation aur error handling. 3. Memory (self.memory): Calculator ki yaad-daasht ko manage karta hai, taake doosri classes isko istemal kar saken.OOP ConceptEncapsulation: Is Class ke andar data (self.memory) aur us data par kaam karne waale functions (methods) ko aik saath band (encapsulate) kiya gaya hai.Project Name	Scientific Calculator Module (scientific_calculator.py)
Role in OOP	Child Class (Inheritance): Yeh file Calculator Class (Parent) se virasat (inherit) leti hai. Iska maqsad yeh hai ke hum core functionality ko dobara likhe baghair (without rewriting) naye features shamil kar sakein.
Key Features	Scientific Operations: Sine (sin), Log (Base 10), aur future mein aanay waale complex functions.
Technical Highlight	super().__init__() ka istemal karke Parent Class ki memory (self.memory) ko initializ kiya gaya hai. Yeh Inheritance ka saboot hai.
Section,Detail
Project Name,Scientific Calculator Module (scientific_calculator.py)
Role in OOP,Child Class (Inheritance): Yeh file Calculator Class (Parent) se virasat leti hai. Iska maqsad hai core functionality ko dobara likhe baghair naye features shamil karna.
Key Features,"Scientific Operations: Sine (sin), Log (Base 10)."
Section,Detail
Project Name,Base Calculator Module (base_calculator.py)
Role in OOP,Parent Class (Foundation): Yeh file Calculator Class ki tareef karti hai.
Key Features,"Core Arithmetic, Robust Input (get_float), aur Memory Management (self.memory) shamil hain."
Step,Instruction
Files Required,base_calculator.py aur scientific_calculator.py dono files ek hi folder mein honi chahiyein.
How to Run,Terminal mein sirf Child Class file ko run karein: python scientific_calculator.py
