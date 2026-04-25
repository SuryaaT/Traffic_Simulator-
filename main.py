from traffic_sim.simulation import Simulation
from traffic_sim.junction import Junction
from traffic_sim.road import Road
from traffic_sim.source import Source
from traffic_sim.sink import Sink
from traffic_sim.router import Router
from traffic_sim.visualization import animate

sim = Simulation()

# junctions
j1 = Junction("J1")
j2 = Junction("J2")
j3 = Junction("J3")
j4 = Junction("J4")

sim.junctions = [j1, j2, j3, j4]

# roads (NO SHORTCUT NOW)
r1 = Road("R1", j1, j2)
r2 = Road("R2", j2, j3)
r4 = Road("R4", j3, j4)

sim.roads = [r1, r2, r4]

# connections
j1.add_outgoing(r1)

j2.add_incoming(r1)
j2.add_outgoing(r2)

j3.add_incoming(r2)
j3.add_outgoing(r4)

j4.add_incoming(r4)

# graph (UPDATED)
graph = {
    j1: [r1],
    j2: [r2],
    j3: [r4],
    j4: []
}

router = Router(graph)

# source & sinks
source = Source(j1, rate=0.5, destinations=[j3, j4], router=router)

sink1 = Sink(j3)
sink2 = Sink(j4)

sim.sources = [source]
sim.sinks = [sink1, sink2]

# positions
pos = {
    j1: (0, 2),
    j2: (2, 3),
    j3: (4, 2),
    j4: (6, 1)
}

animate(sim, pos)