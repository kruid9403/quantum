from quantum.circuit.circuit import Circuit

class AnsatzCircuit:
    def __init__(self, num_qubits, kind="h2"):
        self.num_qubits = num_qubits
        self.kind = kind

    def build(self, params):
        circ = Circuit(self.num_qubits, self.num_qubits)
        if self.kind == "h2":
            if len(params) != 1:
                raise ValueError("H2 ansatz expects a single parameter.")
            theta = params[0]
            circ.apply_ry([(0, theta)])
            circ.apply_cx([(0, 1)])
        elif self.kind == "hardware_efficient":
            # Example: RY on all qubits, full entangling layer
            if len(params) != self.num_qubits:
                raise ValueError("Hardware efficient needs 1 param per qubit.")
            for i, t in enumerate(params):
                circ.apply_ry([(i, t)])
            for i in range(self.num_qubits - 1):
                circ.apply_cx([(i, i + 1)])
        else:
            raise NotImplementedError("Unknown ansatz kind.")
        return circ