from obspy import UTCDateTime
from obspy.clients.fdsn import Client

t1 = UTCDateTime("2010-09-3T16:30:00.000")
t2 = UTCDateTime("2010-09-3T17:00:00.000")
fdsn_client = Client('IRIS')
# Fetch waveform from IRIS FDSN web service into a ObsPy stream object
# and automatically attach correct response
st = fdsn_client.get_waveforms(network='NZ', station='BFZ', location='10',
                               channel='HHZ', starttime=t1, endtime=t2,
                               attach_response=True)
#
# define a filter band to prevent amplifying noise during the deconvolution
pre_filt = (0.005, 0.006, 30.0, 35.0)
st.remove_response(output='DISP', pre_filt=pre_filt)
#st.remove_response(pre_filt='')

from obspy import read, read_inventory 
st = read("/path/to/IU_ULN_00_LH1_2015-07-18T02.mseed") 
tr = st[0] 
inv = read_inventory("/path/to/IU_ULN_00_LH1.xml") 
pre_filt = [0.001, 0.005, 45, 50] 
tr.remove_response(inventory=inv, pre_filt=pre_filt, output="DISP", water_level=60, plot=True)
