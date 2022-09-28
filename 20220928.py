import numpy as np
import matplotlib.pyplot as plt
def AND(list1,list2):
    return [list1[i] and list2[i] for i in range(100)]
score = np.random.randint(0, 100, 100)

x = [np.array(['No Pass','Pass']),
     np.array([x for x in range(5,101,5)]),
     np.array([x for x in range(10,101,10)]),
     np.array(['60~79','80~100','0~59'])]
y = [[score[(score<60)].shape[0],score[(score>=60)].shape[0]],
     [score[(AND((x-5)<score,score<=x))].shape[0] for x in range(5,101,5)],
     [score[(AND((x-10)<score,score<=x))].shape[0] for x in range(10,101,10)],
     [score[(AND((60)<=score,score<80))].shape[0],
      score[(AND((80)<=score,score<=100))].shape[0],
      score[(AND(0<=score,score<60))].shape[0]]]
titles = ['Grade Bar Chart Anylsis', 'Grade Plot Chart Anylsis', 'Grade Scatter Chart Anylsis', 'Grade Pie Chart Anylsis']
colors = ['red', 'blue', 'yellow', 'green']
type = ['bar','plot','scatter','pie']
fig, axes = plt.subplots(nrows=2, ncols=2,)
for i in range(4):
    #axes[i // 2, i % 2].set(title=titles[i])
    axes[i // 2, i % 2].set_title(label=titles[i],loc='left',y=0.95)
    if type[i]=='bar':
        axes[i // 2, i % 2].bar(x[i],y[i],color=colors[i],linewidth=i+1)
    elif type[i]=='plot':
        axes[i // 2, i % 2].plot(x[i], y[i], color=colors[i], linewidth=i + 1)
        axes[i // 2, i % 2].set(xticks=[x for x in range(5,101,10)])
    elif type[i]=='scatter':
        axes[i // 2, i % 2].scatter(x[i], y[i], color=colors[i], linewidth=i + 1, marker='^')
    elif type[i]=='pie':
        axes[i // 2, i % 2].pie(y[i],labels=x[i])
#axes[0,0].set(xticks=[60])

plt.show()
