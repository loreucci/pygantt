import matplotlib
import matplotlib.pyplot as plt
from pylab import show
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable


def create_gantt(wps):

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
    wpspace = len(wps)
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
