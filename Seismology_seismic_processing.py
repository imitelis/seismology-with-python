# Seismic processing: Charge, Spectrogram, Remove instrumental answer
import time
t=time.time()
print("Loading libraries...")
import numpy as np
from obspy import UTCDateTime, Stream, read, read_inventory
secs=time.time()-t
print("Libraries loaded on %d seconds." % (secs))
print()
# Read all forms of wave
st=read('Sismo_Santos_20210701T140741_M4.6.mseed')
# Show traces
print(st)
# Plot it
st.plot()

# Select trace (channel)
st = st.select(channel='BHZ')
tr = st[0]
print()
print(tr)
# Graph spectrogram of trace frequency
tr.spectrogram()
# Remove instrumental answer
inv = read_inventory('BT_010.dataless')
pre_filt = [1/40, 1/30, 40, 45]
tr.remove_response(inventory=inv, pre_filt=pre_filt, output="DISP", water_level=60, plot=True) # Desplazamiento
st2 = tr.remove_response(inventory=inv, pre_filt=pre_filt, output="VEL", water_level=60, plot=True) # Velocidad
st2.plot()

tp1 = UTCDateTime("2021-07-01T14:08:22.640")
tp2 = UTCDateTime("2021-07-01T14:08:29.640")

tt=read('Sismo_Santos_20210701T140741_M4.6.mseed',format='mseed',starttime=tp1,endtime=tp2)
tt.plot()
tps = tt.select(channel='BHZ')
tpr = tt[0]
tpr.remove_response(inventory=inv, pre_filt=pre_filt, output="DISP", water_level=60, plot=True)
