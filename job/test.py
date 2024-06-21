import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

title_font=FontProperties(family='YouYuan',size=18)
mpl.rcParams['axes.unicode_minus']=False
def draw_macd(df_raw, dif, dea,
              red_bar, green_bar,
              canvas_w=1000, canvas_h=480,
              xtick_period=20,
              title=u'MACD'):
    dpi=72
    figsize=canvas_w/72,canvas_h/72
    plt.figure(figsize=figsize)

    p_dif=plt.plot(dif.index,dif.values)
    p_dea=plt.plot(dea.index,dea.values)
    plt.bar(red_bar.index, red_bar.values, color='#d62728')
    plt.bar(green_bar.index, green_bar.values, color='#889966')
    major_index=df_raw.index[df_raw.index%xtick_period==0]
    major_xtics=df_raw['date'][df_raw.index%xtick_period==0]
    plt.xticks(major_index,major_xtics)
    plt.legend((p_dif[0],p_dea[0]),[u'DIF',u'DEA'])
    plt.title(title,fontproperties=title_font)

    plt.show()
if __name__ == '__main__':
    draw_macd([
        {
            'x':[1,2,3,4],
            'y':[1,2,3,1],
            'label':'macd',
         },{
            'x':[1,2,3,4],
            'y':[5,6,6,6,],
         }])