from copy import deepcopy

class Circuit():
    def __init__(self, num_qubits, num_clbits):
        self.num_qubits = num_qubits
        self.num_clbits = num_clbits
        self.instructions = []

    def apply_h_gate(self, qubit_indicies):
        for i in qubit_indicies:
            self.instructions.append(f"h q[{i}];")
        return self # For chaining

    def apply_x_gate(self, qubit_indicies):
        for i in qubit_indicies:
            self.instructions.append(f"x q[{i}];")
        return self

    def apply_cx(self, pairs):
        """Apply CX (CNOT) gate to each control-target pair.
        'pairs' should be a tuple list: [(ctrl1, tgt1), (ctrl2, tgt2), ...]"""
        for ctrl, tgt in pairs:
            self.instructions.append(f"cx q[{ctrl}], q[{tgt}];")
        return self
    
    def set_state(self, idx, state):
        """Set the state (spin) of qubit idx."""
        if state == '0':
            pass  # Already |0>
        elif state == '1':
            self.instructions.append(f"x q[{idx}];")
        elif state == '+':
            self.instructions.append(f"h q[{idx}];")
        elif state == '-':
            self.instructions.append(f"x q[{idx}];")
            self.instructions.append(f"h q[{idx}];")
        else:
            raise ValueError("state must be '0', '1', '+', or '-'")
        return self
    
    def set_amplitude(self, idx, theta, phi):
        self.instructions.append(f"u3({theta}, {phi}, 0) q[{idx}];")
        return self
    
    def copy(self):
        return deepcopy(self)

    def measure(self, qubit_idx, clbit_idx):
        self.instructions.append(f"measure q[{qubit_idx}] -> c[{clbit_idx}];")
        return self

    def measure_all(self):
        for i in range(self.num_qubits):
            self.instructions.append(f"measure q[{i}] -> c[{i}];")
        return self
    
    def to_qasm(self):
        lines = []
        lines.append("OPENQASM 2.0;")
        lines.append("include \"qelib1.inc\";")
        lines.append(f"qreg q[{self.num_qubits}];")
        lines.append(f"creg c[{self.num_clbits}];")
        for instr in self.instructions:
            lines.append(instr)
        return "\n".join(lines)
    
    def to_qasm_file(self, filename):
        quasm_code = self.to_qasm()
        with open(filename, "w") as f:
            f.write(quasm_code)

    def apply_y_gate(self, qubit_indices):
        for i in qubit_indices:
            self.instructions.append(f"y q[{i}];")
        return self

    def apply_z_gate(self, qubit_indices):
        for i in qubit_indices:
            self.instructions.append(f"z q[{i}];")
        return self

    def apply_s_gate(self, qubit_indices):
        for i in qubit_indices:
            self.instructions.append(f"s q[{i}];")
        return self

    def apply_sdg_gate(self, qubit_indices):
        for i in qubit_indices:
            self.instructions.append(f"sdg q[{i}];")
        return self

    def apply_t_gate(self, qubit_indices):
        for i in qubit_indices:
            self.instructions.append(f"t q[{i}];")
        return self

    def apply_tdg_gate(self, qubit_indices):
        for i in qubit_indices:
            self.instructions.append(f"tdg q[{i}];")
        return self

    def apply_rx(self, targets):  # targets: [(idx, theta), ...]
        for idx, theta in targets:
            self.instructions.append(f"rx({theta}) q[{idx}];")
        return self

    def apply_ry(self, targets):  # targets: [(idx, theta), ...]
        for idx, theta in targets:
            self.instructions.append(f"ry({theta}) q[{idx}];")
        return self

    def apply_rz(self, targets):  # targets: [(idx, theta), ...]
        for idx, theta in targets:
            self.instructions.append(f"rz({theta}) q[{idx}];")
        return self
