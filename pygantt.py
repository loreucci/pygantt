import matplotlib
import matplotlib.pyplot as plt
from pylab import show
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable


def create_gantt(wps, **config):

    # plot config
    width = config.get('barwidth', 0.9)
    markersize = config.get('markersize', 50)
    wp_offset = 1 - config.get('id_first_wp', 1)
    show_delivmile = config.get('show_delivmile', True)
    collapse_wp = config.get('collapse_wp', False)
    fontsize = config.get('fontsize', 10.0)

    # pyplot params
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    plt.rcParams['font.size'] = fontsize

    # find number of displayed lines
    disp = 0
    for wp in wps:
        if collapse_wp:
            disp += 1
        else:
            disp += len(wp['tasks'])
        disp += 1 if show_delivmile else 0
    disp -= 1

    # axis range
    max_month = 0  # to be computed

    # plot
    fig, ax = plt.subplots()
    ticks = []
    labels = []
    wpspace = len(wps)
    for i, wp in enumerate(wps):
        wpspace_size = 0.5 * wpspace

        if collapse_wp:
            # WP only
            wp_start = min([task[1] for task in wp['tasks']])
            wp_end = max([task[2] for task in wp['tasks']])
            ticks.append(disp+wpspace_size)
            labels.append('WP' + str(i+1-wp_offset))
            ax.broken_barh([(wp_start-1, wp_end-wp_start+1)], (disp-width/2.0+wpspace_size, width), facecolors=wp['color'])
            if wp_end > max_month:
                max_month = wp_end + 1
            disp -= 1
        else:
            # tasks
            for task in wp['tasks']:
                ticks.append(disp+wpspace_size)
                labels.append(task[0])
                ax.broken_barh([(task[1]-1, task[2]-task[1]+1)], (disp-width/2.0+wpspace_size, width), facecolors=wp['color'])
                if task[2] > max_month:
                    max_month = task[2] + 1
                disp -= 1
        # deliverables and milestones
        if show_delivmile:
            ticks.append(disp+wpspace_size)
            labels.append('WP' + str(i+1-wp_offset) + ' Deliverables and Milestones')
            ax.scatter(wp['deliverables'], [disp+width/4.0+wpspace_size] * len(wp['deliverables']), s=markersize, color=wp['color'], marker="^")
            if len(wp['milestones']) > 0:
                ax.scatter(wp['milestones'], [disp-width/4.0+wpspace_size] * len(wp['milestones']), s=markersize, color=wp['color'], marker="d")
            disp -= 1
        wpspace -= 1
    ax.set_yticks(ticks)
    ax.set_yticklabels(labels)
    ax.set_xticks(range(0, max_month+1, 6))
    ax.set_xticklabels(['M'+str(x) for x in range(0, max_month+1, 6)])
    ax.set_axisbelow(True)
    ax.grid(True, axis='x')
    make_axes_area_auto_adjustable(ax)
