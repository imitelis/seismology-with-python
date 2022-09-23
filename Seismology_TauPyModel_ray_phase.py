from obspy.taup import TauPyModel
model = TauPyModel(model="iasp91")
arrivals = model.get_travel_times(source_depth_in_km=55,distance_in_degree=67)
print(arrivals)

arrivals = model.get_travel_times(source_depth_in_km=100,distance_in_degree=45,phase_list=["P", "PSPSPS"])
print(arrivals)

arr = arrivals[0]
arr.ray_param, arr.time, arr.incident_angle

#For calculating the path traveled by a ray
arrivals = model.get_ray_paths(500, 130)
arrival = arrivals[0]
arrival.path.dtype
arrival.path

#For plotting rays
arrivals = model.get_ray_paths(source_depth_in_km=500, distance_in_degree=130, phase_list=["ttbasic"])
ax = arrivals.plot_rays()

#For particular phases
arrivals = model.get_ray_paths(source_depth_in_km=500,distance_in_degree=130,phase_list=["Pdiff", "Sdiff","pPdiff", "sSdiff"])
ax = arrivals.plot_rays()

#Representation in Cartesian coordenate system
arrivals = model.get_ray_paths(source_depth_in_km=500,distance_in_degree=130,phase_list=["ttbasic"])
ax = arrivals.plot_rays(plot_type="cartesian")

#Example 2
import numpy as np
import matplotlib.pyplot as plt
from obspy.taup import TauPyModel

PHASES = [
    # Phase, distance
    ('P', 26),
    ('PP', 60),
    ('PPP', 94),
    ('PPS', 155),
    ('p', 3),
    ('pPcP', 100),
    ('PKIKP', 170),
    ('PKJKP', 194),
    ('S', 65),
    ('SP', 85),
    ('SS', 134.5),
    ('SSS', 204),
    ('p', -10),
    ('pP', -37.5),
    ('s', -3),
    ('sP', -49),
    ('ScS', -44),
    ('SKS', -82),
    ('SKKS', -120),
]

model = TauPyModel(model='iasp91')
fig, ax = plt.subplots(subplot_kw=dict(polar=True))

#Plot all pre-determined phases
for phase, distance in PHASES:
    arrivals = model.get_ray_paths(700, distance, phase_list=[phase])
    ax = arrivals.plot_rays(plot_type='spherical',legend=False, label_arrivals=True,plot_all=True,show=False, ax=ax)

#Annotate regions
ax.text(0, 0, 'Solid\ninner\ncore',horizontalalignment='center',verticalalignment='center',bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
ocr = (model.model.radius_of_planet - (model.model.s_mod.v_mod.iocb_depth + model.model.s_mod.v_mod.cmb_depth) / 2)
ax.text(np.deg2rad(180), ocr, 'Fluid outer core',horizontalalignment='center',bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
mr = model.model.radius_of_planet - model.model.s_mod.v_mod.cmb_depth / 2
ax.text(np.deg2rad(180), mr, 'Solid mantle',horizontalalignment='center',bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
plt.show()


from obspy.taup import plot_travel_times
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(9, 9))
ax = plot_travel_times(source_depth=10, phase_list=["P", "S", "PP"],ax=ax, fig=fig, verbose=True)
