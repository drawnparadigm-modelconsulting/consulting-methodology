"""
Drawn Paradigm: Strategic Model Logic
Purpose: Standardized framework for initializing business model audits.
"""

class ModelConsultant:
    def __init__(self, client_name):
        self.client = client_name
        self.phases = ["Discovery", "Architecture", "Monitoring"]

    def initialize_audit(self):
        print(f"--- Initializing Drawn Paradigm Framework for {self.client} ---")
        for phase in self.phases:
            print(f"Status: Preparing {phase} phase...")
        print("Framework Ready.")

# Example Initialization
if __name__ == "__main__":
    dp_audit = ModelConsultant("Strategic Partner")
    dp_audit.initialize_audit()


def check_logic_leak(model_data):
    """
    Identifies 'Static Leaks'—hard-coded numbers that should be dynamic.
    Target: Eliminating manual grunt work and hidden variance.
    """
    detected_leaks = []
    
    # We look for float values that aren't 0 or 1 (common indicators of hard-coding)
    for k, v in model_data.items():
        if isinstance(v, float) and v not in [0.0, 1.0]:
            detected_leaks.append(f"LEAK DETECTED: '{k}' is a hard-coded constant ({v}).")
            
    if not detected_leaks:
        return "PASS: Logic is dynamic and auditable."
    
    return detected_leaks

# --- TEST CASE FOR A CLIENT ---
# Imagine a lead sends you their "Logic"
client_logic = {
    "revenue_growth_target": 0.15,  # Leak!
    "operating_expenses": 45000.50, # Leak!
    "dynamic_margin": 12.5          # Leak!
}

print("Drawn Paradigm Diagnostic Report:")
print(check_logic_leak(client_logic))
