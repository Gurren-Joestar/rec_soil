# define loads
tsTag = 1
id_nload = 1
ti = 0*s
tf = 0.2*s
fr = 50*Hz
period = 1/fr
Fx = 0*N
Fy = 10000*N
ops.timeSeries('Trig', tsTag, ti, tf, period, '-factor', 1.0)
ops.pattern('Plain', 1, tsTag, '-fact', 1.0)
ops.load(id_nload, Fx, Fy)

# constraints nodes
ops.equalDOF(1, 6, *[1, 2])
ops.equalDOF(1, 7, *[1, 2])
ops.equalDOF(1, 300, *[1, 2])
ops.equalDOF(1, 301, *[1, 2])