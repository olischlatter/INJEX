
from stl import mesh
import numpy as np


## Example 1:
## Array of vertex positions and array of vertex indexes defining faces
## Colors are specified per-face


# Using an existing stl file:
STLMesh = mesh.Mesh.from_file('fox.stl')

# Or creating a new mesh (make sure not to overwrite the `mesh` import by
# naming it `mesh`):
#VERTICE_COUNT = 100
#data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
#STLMesh = mesh.Mesh(data, remove_empty_areas=False)

# The mesh normals (calculated automatically)
STLMesh.normals
# The mesh vectors
STLMesh.v0, STLMesh.v1, STLMesh.v2
# Accessing individual points (concatenation of v0, v1 and v2 in triplets)
#assert (STLMesh.points[0][0:3] == STLMesh.v0[0]).all()
#assert (STLMesh.points[0][3:6] == STLMesh.v1[0]).all()
#assert (STLMesh.points[0][6:9] == STLMesh.v2[0]).all()
#assert (STLMesh.points[1][0:3] == STLMesh.v0[1]).all()

#colors = np.ones((STLMesh.vectors.shape[0],3, 4))


nrOfVerts = len(STLMesh.vectors)

Points = []
Edges = []
Triangles = []

findNeighbours = []

#print(nrOfVerts)


for iVerts in range(0,nrOfVerts):

    #print(iVerts)    
    
    p1 = STLMesh.vectors[iVerts][0].tolist()
    p2 = STLMesh.vectors[iVerts][1].tolist()
    p3 = STLMesh.vectors[iVerts][2].tolist()
    
    nrOfPoints = len(Points)
    found1,found2,found3 = False,False,False;
    
    for iPoints in range(0,nrOfPoints):
        if((Points[iPoints][0]==p1)):
            ind1 = iPoints
            found1 = True
        if((Points[iPoints][0]==p2)):
            ind2 = iPoints
            found2 = True
        if((Points[iPoints][0]==p3)):
            ind3 = iPoints
            found3 = True
        
    if(not found1):
        ind1 = nrOfPoints
        nrOfPoints+=1
        Points.append([p1,[iVerts]])
    else:
        Points[ind1][1].append(iVerts)
    if(not found2):
        ind2 = nrOfPoints
        nrOfPoints+=1
        Points.append([p2,[iVerts]])
    else:
        Points[ind2][1].append(iVerts)
    if(not found3):
        ind3 = nrOfPoints
        Points.append([p3,[iVerts]])
    else:
        Points[ind3][1].append(iVerts)
    
    normVec = STLMesh.normals[iVerts]/np.linalg.norm(STLMesh.normals[iVerts])
    normVec = np.around(normVec,decimals=4).tolist()    
    
    Triangles.append([[ind1,ind2,ind3],normVec,[]])
    
    pointList = np.sort([ind1,ind2,ind3]).tolist()
    
    for iNeighbours in range(0,len(findNeighbours)):
        if(len(set(pointList)&set(findNeighbours[iNeighbours]))==2):
            Triangles[iVerts][2].append(iNeighbours)
            Triangles[iNeighbours][2].append(iVerts)
    
    findNeighbours.append(pointList)
    

