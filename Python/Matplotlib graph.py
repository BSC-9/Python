import matplotlib.pyplot as plt
No=int(input("Enter number of co-ordinates: "))
x,y=[],[]
while(No!=0):
    X=int(input("Enter x: "))
    Y=int(input("Enter y: "))
    x.append(X)
    y.append(Y)
    No=No-1
#matplotlib functions
plt.plot(x,y)  #to plot graph
#Labels X and Y and Title of the graph
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph")
#To display the graph
plt.show()