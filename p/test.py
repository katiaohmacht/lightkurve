import lightkurve as lk
#%matplotlib inline
tpf = lk.search_targetpixelfile('K2-199', author='K2', campaign=6).download()
tpf.plot()
