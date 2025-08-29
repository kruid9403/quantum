from quantum.circuit.circuit import Circuit

class Element():
    def __init__(self, atomic_number):
        self.atomic_number = atomic_number
        self.spin_orbitals = self._ALL_SPIN_ORBITALS
        self.occupations = self._ATOM_CONFIGS.get(atomic_number, [])
        self.num_qubits = len(self.spin_orbitals)
        self.circuit = Circuit(self.num_qubits, self.num_qubits)
        for so in self.occupations:
            idx = self.spin_orbitals.index(so)
            self.circuit.apply_x_gate([idx])
        self.circuit.measure_all()

    def to_qasm(self):
        # Get the circuit string
        return self.circuit.to_qasm()
    
    def orbital_map(self):
        # Get mapping
        return { i: so for i, so in enumerate(self.spin_orbitals) }
    
    def display(self):
        print(f"Atomic Number: {self.atomic_number}")
        print(f"Spin Orbitals: {self.spin_orbitals}")
        print(f"Occupations: {self.occupations}")
        print(f"Qubit map: {self.orbital_map()}")
        print(f"Circuit: {self.to_qasm()}")
        print(self.circuit)

    def excite_electron(self, from_so_idx, to_so_idx):
        """Excite an electron from one spin orbital to another."""
        if from_so_idx < 0 or from_so_idx >= self.num_qubits:
            raise ValueError("Invalid from_so_idx")
        if to_so_idx < 0 or to_so_idx >= self.num_qubits:
            raise ValueError("Invalid to_so_idx")
        if from_so_idx == to_so_idx:
            raise ValueError("from_so_idx and to_so_idx must be different")

        # Apply a series of gates to excite the electron
        self.circuit.apply_x_gate([from_so_idx])
        self.circuit.apply_x_gate([to_so_idx])

