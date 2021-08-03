import h5py
import numpy as np

infile=h5py.File("test_mesh/visdump_surface_mesh.h5","r")


dat=infile["0"]["Mesh"]["Nodes"]
x=dat.shape
print (dat.shape)
print (x[0])
Z = np.zeros((x[0],x[1]))

for i,d in enumerate(dat):
    Z[i][0] = d[0]
    Z[i][1] = d[1]
    Z[i][2] = d[2]

#print (Z)

#with open("david_movie3/visdump_surface_star_mesh.h5","r+") as hf:
#    d2=infile["0"]["Mesh"]["Nodes"]
#d2[...]=Z

outfile=h5py.File("david_movie3/visdump_surface_star_mesh.h5","r+")
d2=outfile["41"]["Mesh"]["Nodes"]
d2[...]=Z

infile.close()
outfile.close()
