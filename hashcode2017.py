#################data reading and manipulating######################################

def matrix_grid(data):
    M=[]
    for l in data:
        L=[]
        for k in l:
            if k=="#":
                L.append(-1)
            else if k==".":
                L.append(1)
            else:
                L.append(0)
        M.append(L)
    return(M)

#################### intermediatefunctions ###########################################  
def max_grid(H,W,R):
    L=[int(H/R),int(W/R)]
    return max(L)

def surface1():

def surface2(M,cell):
    M1=deep.copy(M)
    S=0
    for i in range(ceil(cell[0]-R/2),ceil(cell[0]+R/2)+1):
        for j in range(ceil(cell[1]-R/2),cell[1]):
            if M1[i][j]==-1:
                for k in range(ceil(cell[1]-R/2),j):
                    M1[i][k]=-1
        for j in range(cell[1]+1,ceil(cell[1]+R/2)+1):
            if M1[i][j]==-1:
                for k in range(j,ceil(cell[1]+R/2)+1):
                    M1[i][k]=-1
            
                
    
    
    





####################determining the cells and the routers################################  
        
def cells(M,H,W,R,init):
    c=max_grid(H,W,R)
    L=[init]
    for i in range(c-1):
        s=0
        j=0
        for k in neighbours(L[i]):
            if surface1(L[i],k)>s:
                s=surface1(L[i],k)
                j=k
        L.append(j)
    return L

def routers(M,H,W,R,S_tot,init):
    cellules=cells(M,H,W,R,init)
    for i in range(len(cellules)):
        cellules[i]=(surface2(cellules[i]),cellules[i])
    cellules.sort()
    cellules.reverse()
    S=surface2(cellules[0])
    rout=[cellules[0]]
    i=0
    while(S<S_tot):
        if(cellules[i+1] not wall):
            S=S+surface1(cellules[i],cellules[i+1])
            i=i+1
            rout.append(cellules[i])
    return rout
        
            
        
