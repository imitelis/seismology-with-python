from obspy.clients.fdsn import Client
client = Client("IRIS")

from obspy import UTCDateTime
t = UTCDateTime("2019-07-04T17:33:49.000")


st = client.get_waveforms("IU", "ANMO", "*", "*", t, t + 60 * 60)
st.plot()


st = client.get_waveforms("IU", "ANMO", "*", "BHZ", t, t + 60 * 60)
st.plot()
traza1 = st[0]
traza2 = st[1]
dtraza = traza1.data - traza2.data
plt.show()
#There is instrumental amplifying or difference

ampl1 = abs(traza1.data)
import matplotlib as plt
plt.show(ampl1)
ampl2 = abs(traza2)
ampl2 = abs(traza2.data)
#If there are zeros I cannot take away the quotient for stablishing
#the amplifying resolution

e1 = traza1.integrate()
#The signal isnt corrected instrumentally and shows drift

M_ing = traza2.max()/traza1.max()
