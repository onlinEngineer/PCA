import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

data=fetch_olivetti_faces()

X=data.images.reshape((data.images.shape[0],data.images.shape[1]*data.images.shape[2]))
print(X)
print(X.shape)

pca=decomposition.PCA()
pca.fit(X)


plt.title("Eigenvalues")
plt.plot(pca.explained_variance_)

plt.show()


fig,ax=plt.subplots(1,1,figsize=(8,8))
ax.imshow(pca.mean_.reshape((64,64)), cmap="gray")
print(pca.mean_)
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Mean Face')
plt.show()

n_components=50
eigenfaces=pca.components_[:n_components]

print(pca.components_[:20])
fig, axes = plt.subplots(5,4,sharex=True,sharey=True,figsize=(8,10))
for i in range(20):
    axes[i%5][i//5].imshow(eigenfaces[i].reshape((64,64)), cmap="gray")


plt.show()


import numpy as np

mean = np.mean(X, axis = 0)
numOfPC = [5, 10, 40, 200]
for i in numOfPC:
    pc = np.dot(pca.transform(X)[:, :i],
                     pca.components_[:i, :])
    pc += mean
    print(f"PCA={i}",pc[0],pc[0].shape)
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(pc[0].reshape((64,64)), cmap=plt.cm.bone)
    ax.set_title(f"PC={i}")

fig3, ax = plt.subplots(figsize=(4, 4))
ax.imshow(X[0].reshape((64,64)), cmap=plt.cm.bone)
ax.set_title("Real Image")
print(f"Real Image", X[0], X[0].shape)
plt.show()


xt= pca.fit_transform(X)

# Creating figure
fig2 = plt.figure(figsize=(10, 7))
ax = plt.axes(projection="3d")

# Creating plot
ax.scatter3D(xt[:,0], xt[:,1], xt[:,2],c=data.target)
plt.title("First 3 Principal Components")
ax.set_xlabel('Principle 0')
ax.set_ylabel('Principle 1')
ax.set_zlabel('Principle 2')
print(f"First Principal Component",xt[:100,0],xt[:,0].shape)
print(f"Second Principal Component",xt[:100,1],xt[:,1].shape)
print(f"Third Principal Component",xt[:100,2],xt[:,2].shape)

# show plot
plt.show()



