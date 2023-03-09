import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    """
    Create a plot of the covariance confidence ellipse of *x* and *y*.

    Parameters
    ----------
    x, y : array-like, shape (n, )
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    n_std : float
        The number of standard deviations to determine the ellipse's radiuses.

    **kwargs
        Forwarded to `~matplotlib.patches.Ellipse`

    Returns
    -------
    matplotlib.patches.Ellipse
    """
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    # Using a special case to obtain the eigenvalues of this
    # two-dimensionl dataset.
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2, facecolor=facecolor,linestyle='--', alpha=0.5, **kwargs)

    # Calculating the stdandard deviation of x from
    # the squareroot of the variance and multiplying
    # with the given number of standard deviations.
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    # calculating the stdandard deviation of y ...
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
#plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['font.size'] = 13
dt = pd.read_csv('index.csv')
fig = plt.figure(dpi=300,figsize=(10,6))

colors = ['b','g','r','orange','purple']
labels = ['自然灾害', '基础设施', '公共卫生', '城市交通', '社会治理']

for _i in range(5):
    ration = dt[dt.Type==labels[_i]]['rationality']
    operal = dt[dt.Type==labels[_i]]['operability']

    plt.scatter(x=ration,y=operal, c=colors[_i], alpha = 0.2, s=50)
    confidence_ellipse(ration, operal, fig.axes[0], edgecolor=colors[_i])

plt.legend(labels)

plt.vlines(x=0.75,ymin=0.5,ymax=1.02,colors=['white'])
plt.annotate("", xy=(0.75, 0.5), xytext=(0.75,1.0),arrowprops=dict(arrowstyle="<-", color='grey'))
plt.hlines(y=0.75,xmin=0.5,xmax=1.0,colors=['white'])
plt.annotate("", xy=(0.5, 0.75), xytext=(1.0,0.75),arrowprops=dict(arrowstyle="<-", color='grey'))
plt.text(x = 0.85, y =0.60, s='倡导性指标')
plt.text(x = 0.85, y =0.85, s='强制性指标')
plt.text(x = 0.60, y =0.85, s='引导性指标')
plt.text(x = 0.60, y =0.60, s='非核心指标')

plt.text(x = 0.725, y =1.02, s='合理性高', color = 'grey')
plt.text(x = 0.725, y =0.48, s='合理性低', color = 'grey')
plt.text(x = 0.93, y =0.76, s='可操作性高', color = 'grey')
plt.text(x = 0.50, y =0.76, s='可操作性低', color = 'grey')


for _i in range(dt.shape[0]):
    deltax=0.0
    if _i in [10, 44,15,41,49, 26]:
        deltax=-0.01
    if _i in [11]:
        deltax=0.01
    plt.text(x=dt.rationality[_i]+deltax,y=dt.operability[_i]+0.005,s=dt.No[_i],size=8,color='grey')

fig.savefig('indexmap.jpg')

