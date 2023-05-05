def distancias(self):
    N = len(self)
    vl = []
    for i in np.arange(0, N):
        for j in np.arange(i+1, N):
            if(i != j):
                aux = nx.shortest_path(self,i,j)
                vl.append(len(aux)-1)
    return vl