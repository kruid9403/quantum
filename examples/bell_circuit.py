from quantum.circuit import Circuit 

circ = Circuit(2,2)
circ.apply_h_gate([0])
circ.apply_cx([(0, 1)])
print(circ.to_qasm())

copy=circ.copy()
copy.measure_all()

print(copy.to_qasm())