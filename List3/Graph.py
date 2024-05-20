import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = [
    'Dishwasher', 'Water Inlet Valve', 'Heating Element', 'Spray Arms',
    'Drain Pump', 'Detergent Dispenser', 'Control Panel', 'Door Latch',
    'Detergent', 'Rinse Aid', 'Salt', 'Wash Cycle', 'Clean Dishes', 'Unclean Dishes'
]
G.add_nodes_from(nodes)

# Add edges with labels
edges = [
    ('Dishwasher', 'Water Inlet Valve', 'composed of'),
    ('Dishwasher', 'Heating Element', 'composed of'),
    ('Dishwasher', 'Spray Arms', 'composed of'),
    ('Dishwasher', 'Drain Pump', 'composed of'),
    ('Dishwasher', 'Detergent Dispenser', 'composed of'),
    ('Dishwasher', 'Control Panel', 'composed of'),
    ('Dishwasher', 'Door Latch', 'composed of'),
    ('Dishwasher', 'Detergent', 'requires'),
    ('Dishwasher', 'Rinse Aid', 'requires'),
    ('Dishwasher', 'Salt', 'requires'),
    ('Dishwasher', 'Wash Cycle', 'requires'),

    ('Unclean Dishes', 'Dishwasher', 'processed by'),
    ('Dishwasher', 'Clean Dishes', 'produces')
]

for edge in edges:
    G.add_edge(edge[0], edge[1], label=edge[2])

# Define positions manually
scale_factor = 5
pos = {
    'Dishwasher': (0, 0),
    'Water Inlet Valve': (-1*scale_factor, 4*scale_factor),
    'Heating Element': (-1.75*scale_factor, 3.5*scale_factor),
    'Spray Arms': (-2.5*scale_factor, 2.5*scale_factor),
    'Drain Pump': (-3*scale_factor, 1*scale_factor),
    'Detergent Dispenser': (-2.5*scale_factor, -0.5*scale_factor),
    'Control Panel': (-1.75*scale_factor, -1.5*scale_factor),
    'Door Latch': (-1*scale_factor, -2*scale_factor),
    'Detergent': (2*scale_factor, 2.5*scale_factor),
    'Rinse Aid': (2*scale_factor, 1*scale_factor),
    'Salt': (2*scale_factor, -2*scale_factor),
    'Wash Cycle': (2*scale_factor, -0.5*scale_factor),
    'Clean Dishes': (4.5, 3.25*scale_factor),
    'Unclean Dishes': (0, 3.5*scale_factor)
}

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=15000, node_color='black', font_size=10, font_weight='bold', font_color="white")



# Draw edge labels
edge_labels = {(edge[0], edge[1]): edge[2] for edge in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=8, font_weight='bold')

# Show the plot
plt.title('Dishwasher Diagram')
plt.show()
