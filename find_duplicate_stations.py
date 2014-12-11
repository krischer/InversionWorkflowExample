import collections
import obspy
import glob


stations = collections.defaultdict(set)

data = glob.glob("SAC/*.SAC")

for filename in data:
    st = obspy.read(filename)
    for tr in st:
        stations[(tr.stats.network, tr.stats.station)].add(
            tr.stats.location)

print("Found %i stations" % len(stations))

for key, value in stations.items():
    if len(value) != 1:
        print("ls SAC/*%s* >> blub" % key[1])
