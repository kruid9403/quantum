
class Isotope:
    def __init__(self, atomic_number: int, mass_number: int):
        self.atomic_number = atomic_number    # Z: Number of protons
        self.mass_number = mass_number        # A: Total nucleons
        self.neutron_count = mass_number - atomic_number

    def symbol(self):
        # Lookup from periodic table (can store in element lookup)
        PERIODIC_TABLE = {
            1: ("H",  "Hydrogen"),
            2: ("He", "Helium"),
            3: ("Li", "Lithium"),
            4: ("Be", "Beryllium"),
            5: ("B",  "Boron"),
            6: ("C",  "Carbon"),
            7: ("N",  "Nitrogen"),
            8: ("O",  "Oxygen"),
            9: ("F",  "Fluorine"),
            10: ("Ne", "Neon"),
            11: ("Na", "Sodium"),
            12: ("Mg", "Magnesium"),
            13: ("Al", "Aluminum"),
            14: ("Si", "Silicon"),
            15: ("P",  "Phosphorus"),
            16: ("S",  "Sulfur"),
            17: ("Cl", "Chlorine"),
            18: ("Ar", "Argon"),
            19: ("K",  "Potassium"),
            20: ("Ca", "Calcium"),
            113: ("Nh", "Nihonium"),
            114: ("Fl", "Flerovium"),
            115: ("Mc", "Moscovium"),
            116: ("Lv", "Livermorium"),
            117: ("Ts", "Tennessine"),
            118: ("Og", "Oganesson"),
        }
        return f"{PERIODIC_TABLE.get(self.atomic_number, '?')}-{self.mass_number}"

    def info(self):
        return {
            "symbol": self.symbol(),
            "protons": self.atomic_number,
            "neutrons": self.neutron_count,
            "mass_number": self.mass_number
        }
