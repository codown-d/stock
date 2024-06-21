import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import pandas as pd

def drawing_plt(plt_list):
    num = len(plt_list)
    fig, axes = plt.subplots(num, 1, )
    for i,item in enumerate(plt_list):
        x_axis= item['x']
        y_axis= item['y']
        label =item.get("label", None)
        axes[i].plot(x_axis,y_axis)
        axes[i].set_title(label)
    # 调整布局
    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    drawing_plt([
        {
            'x':[1,2,3,4],
            'y':[1,2,3,1],
            'label':'macd',
         },{
            'x':[1,2,3,4],
            'y':[5,6,6,6,],
         }])