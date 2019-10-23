import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable

# WP data
wp1 = {'tasks': [
         ('T1.1', 1, 24),
         ('T1.2', 1, 36),
       ],
       'deliverables': [36],
       'milestones': [24],
       'color': 'tab:orange'
}
wp2 = {'tasks': [
         ('T2.1', 1, 24),
         ('T2.2', 13, 36),
       ],
       'deliverables': [36],
       'milestones': [24],
       'color': 'tab:green'
}
wp3 = {'tasks': [
         ('T3.1', 1, 24),
         ('T3.2', 19, 36),
         ('T3.3', 25, 42),
         ('T3.4', 25, 42),
       ],
       'deliverables': [24, 42],
       'milestones': [36],
       'color': 'tab:red'
}
wp4 = {'tasks': [
         ('T4.1', 1, 18),
         ('T4.2', 7, 24),
         ('T4.3', 13, 36),
         ('T4.4', 37, 42),
       ],
       'deliverables': [18, 24, 42],
       'milestones': [36],
       'color': 'tab:blue'
}
wp5 = {'tasks': [
         ('T5.1', 1, 24),
         ('T5.2', 25, 42),
       ],
       'deliverables': [42],
       'milestones': [24],
       'color': 'tab:purple'
}
wp6 = {'tasks': [
         ('T6.1', 43, 48),
         ('T6.2', 49, 60),
         ('T6.3', 49, 60),
         ('T6.4', 55, 60),
       ],
       'deliverables': [48, 60],
       'milestones': [54],
       'color': 'tab:brown'
}
wp7 = {'tasks': [
         ('T7.1', 1, 60),
         ('T7.2', 1, 60),
         ('T7.3', 1, 60),
         ('T7.4', 1, 60),
       ],
       'deliverables': [6],
       'milestones': [],
       'color': 'tab:cyan'
}
wps = [wp1, wp2, wp3, wp4, wp5, wp6, wp7]

# plot config
width = 0.9
plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
markersize = 50

# find number of displayed lines
disp = 0
for wp in wps:
    disp += len(wp['tasks']) + 1
disp -= 1

# plot
fig, ax = plt.subplots()
ticks = []
labels = []
wpspace = len(wp)
for i, wp in enumerate(wps):
    wpspace_size = 0.5 * wpspace
    # tasks
    for task in wp['tasks']:
        ticks.append(disp+wpspace_size)
        labels.append(task[0])
        ax.broken_barh([(task[1]-1, task[2]-task[1]+1)], (disp-width/2.0+wpspace_size, width), facecolors=wp['color'])
        disp -= 1
    # deliverables
    ticks.append(disp+wpspace_size)
    labels.append('WP' + str(i+1) + ' Deliverables and Milestones')
    ax.scatter(wp['deliverables'], [disp+width/4.0+wpspace_size] * len(wp['deliverables']), s=markersize, color=wp['color'], marker="^")
    if len(wp['milestones']) > 0:
        ax.scatter(wp['milestones'], [disp-width/4.0+wpspace_size] * len(wp['milestones']), s=markersize, color=wp['color'], marker="d")
    disp -= 1
    wpspace -= 1
ax.set_yticks(ticks)
ax.set_yticklabels(labels)
ax.set_xticks(range(0, 61, 6))
ax.set_axisbelow(True)
ax.grid(True, axis='x')
make_axes_area_auto_adjustable(ax)
plt.show()