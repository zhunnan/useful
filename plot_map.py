import scipy.io
import matplotlib.pyplot as plt

path = '/home/wan/Matlab/'
path2 = '/home/wan/2021-4/SG_PR/'
sequese = '00'
data = scipy.io.loadmat(path+sequese+'.mat')
gnd = data['groundtruth']
data2 = scipy.io.loadmat(path2+sequese+'pred_db.mat')
col = data2['foo']
plt.scatter(gnd[:,0],gnd[:,1],s=2,c=col[0],cmap=plt.get_cmap('rainbow'))
plt.colorbar()
plt.show()
