from quantum.circuit.circuit import Circuit 
from quantum.simulator.simulator import Simulator

circ = Circuit(2,2)
# circ.apply_ry([(0, (200))])
# circ.apply_rx([(1, (300))])
# circ.apply_rz([(0, (300))])

circ.apply_x_gate([0])
circ.apply_cx([(0, 1)])
circ.apply_x_gate([0])

copy=circ.copy()
copy.measure_all()

print(copy.to_qasm())

sim = Simulator(copy.to_qasm(), shots=4096)
result = sim.run(print_results=True)