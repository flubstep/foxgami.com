from foxgami import red
stories = red.pull_latest('aww')
[s.save() for s in stories]