
# k-means algorithm for k=2
## Cigarettes dataset
dict = {'PS':(10.12,7), 'G':(10,12), 'M':(10,14), 'LS':(9,14), 'LD':(5,7)}


# Functions
## Function to compute distances using the manhattan equation
def compute_distance(a, b):     # with a and b being the tuple values from the dict
    xdiff = abs(a[0]-b[0])
    ydiff = abs(a[1]-b[1])
    return xdiff + ydiff

## Function to compute mean points
def compute_meanpt(Cluster):
    global dict
    xsum = 0
    ysum = 0
    for key, value in dict.items():
        if key in Cluster:
            xsum += dict[key][0]
            ysum += dict[key][1]
    xavg = xsum / (len(Cluster))
    yavg = ysum / (len(Cluster))
    return (xavg, yavg)


# Chosen initialization point (as tuples/coordinates)
M1 = dict['G']
M2 = dict['LS']
OldM1 = (0,0)       # make sure that these are different than the initialized points
OldM2 = (0,0)


# Main
count=0
while OldM1 != M1 and OldM2 != M2:
    Cluster1=[]
    Cluster2=[]

    # If mean points are part of the data points then add them to the cluster
    for value in dict.values():
        if M1 == value:
            Cluster1 = [key for key, value in dict.items() if value == M1]
        if M2 == value:
            Cluster2 = [key for key, value in dict.items() if value == M2]

    # Compute Clusters
    for key, value in dict.items():
        if value == M1 or value == M2:
            continue
        else:
            Sum1 = compute_distance(M1, dict[key])
            Sum2 = compute_distance(M2, dict[key])

            # Appoint point to the closer cluster
            if Sum1 < Sum2:
                Cluster1.append(key)
            elif Sum2 < Sum1:
                Cluster2.append(key)

    # Compute Mean Points
    OldM1 = M1
    OldM2 = M2
    M1 = compute_meanpt(Cluster1)
    M2 = compute_meanpt(Cluster2)

    count += 1
    print(f"Iteration {count}: C1 = {Cluster1}, C2 = {Cluster2}")


#################################################################################################
## comments
# next step is to try to generalize the algorithm for any k
# and to try different initialization points and try to solve the optimization problem

