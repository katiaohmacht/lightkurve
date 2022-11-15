import lightkurve as lk
import matplotlib
matplotlib.use('AGG')
matplotlib.pyplot.savefig('filename') 
tpf = lk.search_targetpixelfile('K2-199', author='K2', campaign=6).download()
tpf.plot();