import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
plt.style.use('ggplot')
def generate_hex():
    randoms = list(np.random.rand(6)*16)
    chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    return "#"+''.join([chars[int(i)] for i in randoms])

def scatter_plot(df, x, y, colorby='City', figsize=(7, 28), title='', legend=True, colors=None):
    if colors is None:
        colors = [generate_hex() for _ in np.unique(df[colorby].values)]
    
    nplots = len(np.unique(np.array([str(x) for x in df[colorby].values if str(x) != 'nan'])))
    fig, ax = plt.subplots(1, 1, figsize=(17, 7))
    plt.subplots_adjust(wspace=0.51, hspace=0.5)
    
    for i, cat, color in zip(range(nplots), np.unique(df[colorby].values), colors):
        sample_x = np.array(df.loc[df[colorby] == cat, x].values)
        sample_y = np.array(df.loc[df[colorby] == cat, y].values)
        
#         print([i//ncols, i%ncols])
        
        ax.scatter(sample_x, sample_y, c=color, label=cat)
        ax.set_xticklabels(sample_x, rotation=90)
        
     
    if legend:
        plt.legend(loc='lower center', ncol=8, bbox_to_anchor=(0.5, -0.24))
    """ 
    if title== '':
        plt.title(title)
    """
    plt.show()

def multi_scatter_plot(df, x, y, colorby='City', figsize=(7, 28), title='', legend=True, colors=None):
    if colors is None:
        colors = [generate_hex() for _ in np.unique(df[colorby].values)]
    
    nplots = len(np.unique(np.array([str(x) for x in df[colorby].values if str(x) != 'nan'])))
    
    ncols = 2
    nrows = (nplots//ncols) + 0
    
    print('{} = {}x{}'.format(nplots, nrows, ncols))
    
    fig, ax = plt.subplots(int(np.ceil(nplots/ncols)), ncols, figsize=(7*ncols, 7*nrows))
    plt.subplots_adjust(wspace=0.51, hspace=0.5)
    
    for i, cat, color in zip(range(nplots), np.unique(df[colorby].values), colors):
        sample_x = np.array(df.loc[df[colorby] == cat, x].values)
        sample_y = np.array(df.loc[df[colorby] == cat, y].values)
        
#         print([i//ncols, i%ncols])
        
        ax[i//ncols, i%ncols].scatter(sample_x, sample_y, c=color, label=cat)
        ax[i//ncols, i%ncols].title.set_text(cat)
        ax[i//ncols, i%ncols].set_xticklabels(sample_x, rotation=90)
        
    """   
    if legend:
        plt.legend(loc='lower center', ncol=8, bbox_to_anchor=(0.5, -0.24))
    
    if title== '':
        plt.title(title)
    """
    plt.show()