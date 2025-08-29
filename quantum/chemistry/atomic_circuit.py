from quantum.circuit.circuit import Circuit

class AtomicCircuit:
    """Represents a simple atom in second quantization mapped to qubits."""
    # Hard-coded minimal basis occupation map for H→O
    _ATOM_CONFIGS = {
        1: ["1s_alpha"], # H
        2: ["1s_alpha", "1s_beta"], # He
        3: ["1s_alpha", "1s_beta", "2s_alpha"], # Li
        4: ["1s_alpha", "1s_beta", "2s_alpha", "2s_beta"], # Be
        5: ["1s_alpha", "1s_beta", "2s_alpha", "2s_beta", "2p_alpha"], # B
        6: ["1s_alpha", "1s_beta", "2s_alpha", "2s_beta", "2p_alpha", "2p_beta"], # C
        7: ["1s_alpha", "1s_beta", "2s_alpha", "2s_beta", "2p_alpha", "2p_beta", "2p'_alpha"], # N
        8: ["1s_alpha", "1s_beta", "2s_alpha", "2s_beta", "2p_alpha", "2p_beta", "2p'_alpha", "2p'_beta"], # O
        # expand as needed
    }
    # List all possible spin-orbitals in this minimal basis set
    _ALL_SPIN_ORBITALS = []
    so_seen = set()
    for fill in _ATOM_CONFIGS.values():
        for so in fill:
            if so not in so_seen:
                _ALL_SPIN_ORBITALS.append(so)
                so_seen.add(so)

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
        return self.circuit.to_qasm()

    def orbital_map(self):
        """Returns mapping of qubit indexes to spin-orbital labels."""
        return {i: so for i, so in enumerate(self.spin_orbitals)}

    def display(self):
        print("Atomic number:", self.atomic_number)
        print("Spin-Orbitals:", self.spin_orbitals)
        print("Occupied:", self.occupations)
        print("Qubit map:", self.orbital_map())
        print("Circuit QASM:\n", self.to_qasm())