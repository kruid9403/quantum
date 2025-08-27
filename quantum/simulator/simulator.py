from qiskit import QuantumCircuit
from qiskit_aer import Aer

class Simulator:
    def __init__(self, circuit, backend='qasm_simulator', shots=1024):
        self.shots = shots
        self.circuit = QuantumCircuit.from_qasm_str(circuit)
        self.backend = Aer.get_backend(backend)

    def run(self, print_results=False):
        job = self.backend.run(self.circuit, shots=self.shots)
        result = job.result()
        counts = result.get_counts(self.circuit)
        
        if print_results:
            print("Simulation Results:", counts)
        
        return counts
        