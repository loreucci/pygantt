import pygantt

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
mywps = [wp1, wp2, wp3, wp4, wp5, wp6, wp7]

pygantt.create_gantt(mywps)
pygantt.show()
