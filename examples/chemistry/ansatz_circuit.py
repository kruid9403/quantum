from quantum.chemistry.ansatz_circuit import AnsatzCircuit
from quantum.simulator.simulator import Simulator
import numpy as np

ansatz = AnsatzCircuit(num_qubits=2, kind="h2")

circ = ansatz.build(params=[np.pi / 3])

print(circ)

circ.measure_all()

sim = Simulator(circ.to_qasm(), shots=4096)
result = sim.run(print_results=True)