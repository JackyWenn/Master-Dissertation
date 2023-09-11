import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import random

def random_position_on_edge(G):
    edge = random.choice(list(G.edges(data=True)))
    start_node = G.nodes[edge[0]]
    end_node = G.nodes[edge[1]]

    random_position = random.random()
    x = start_node['x'] + random_position * (end_node['x'] - start_node['x'])
    y = start_node['y'] + random_position * (end_node['y'] - start_node['y'])

    return (x, y), edge


def spoofed_position_nearby(position, distance_meters=200):
    # Convert distance from meters to degrees approximately
    distance_degrees = distance_meters / 111000
    spoofed_x = position[0] + random.uniform(-distance_degrees, distance_degrees)
    spoofed_y = position[1] + random.uniform(-distance_degrees, distance_degrees)
    return (spoofed_x, spoofed_y)


def compute_route_length(G, route):
    length = 0
    for u, v in zip(route[:-1], route[1:]):
        if u in G and v in G[u]:
            length += G[u][v][0]['length']
    return length


def plot_roads_with_car_and_destination(ax, G):
    car_pos, car_edge = random_position_on_edge(G)
    car_nearest_node = ox.distance.nearest_nodes(G, X=car_pos[0], Y=car_pos[1])

    destination_pos, destination_edge = random_position_on_edge(G)
    destination_nearest_node = ox.distance.nearest_nodes(G, X=destination_pos[0], Y=destination_pos[1])

    # Generate a spoofed position near the car
    spoofed_pos = spoofed_position_nearby(car_pos)
    spoofed_nearest_node = ox.distance.nearest_nodes(G, X=spoofed_pos[0], Y=spoofed_pos[1])

    # Ensure there's a path from the car to the destination and from the spoofed position to the destination
    car_route = nx.shortest_path(G, car_nearest_node, destination_nearest_node)
    spoofed_route = nx.shortest_path(G, spoofed_nearest_node, destination_nearest_node)

    # Compute the lengths of the routes
    car_route_length = compute_route_length(G, car_route)
    spoofed_route_length = compute_route_length(G, spoofed_route)

    # Compute the overlapping length
    overlapping_route = [node for node in car_route if node in spoofed_route]
    overlapping_route_length = compute_route_length(G, overlapping_route)

    # Print  information
    print(f"Start Point (Car): {car_pos}")
    print(f"End Point (Destination): {destination_pos}")
    print(f"Spoofed Point: {spoofed_pos}")
    print(f"Length of Basic Route: {car_route_length} meters")
    print(f"Length of Spoofed Route: {spoofed_route_length} meters")
    print(f"Length of Overlapping Route: {overlapping_route_length} meters")
    print(f"Percentage of Overlapping Route in Basic Route: {overlapping_route_length / car_route_length * 100:.2f}%")

    # Clear the previous plot
    ax.clear()

    # Plot the roads
    ox.plot_graph(G, ax=ax, show=False, close=False, node_size=0)

    # Plot the routes
    ox.plot_graph_route(G, car_route, ax=ax, show=False, close=False, route_linewidth=4, route_color='green',
                        route_zorder=1)
    ox.plot_graph_route(G, spoofed_route, ax=ax, show=False, close=False, route_linewidth=4, route_color='lightcoral',
                        route_zorder=2)

    # Draw the path from the car's exact position to its nearest node and from the destination's exact position to its nearest node
    ax.plot([car_pos[0], G.nodes[car_nearest_node]['x']], [car_pos[1], G.nodes[car_nearest_node]['y']], color='green',
            linewidth=4, zorder=1)
    ax.plot([destination_pos[0], G.nodes[destination_nearest_node]['x']],
            [destination_pos[1], G.nodes[destination_nearest_node]['y']], color='green', linewidth=4, zorder=1)

    ax.scatter(*car_pos, color='red', s=100, zorder=3, label='Car (Red Point)')
    ax.scatter(*destination_pos, color='blue', s=100, zorder=3, label='Destination (Blue Point)')
    ax.scatter(*spoofed_pos, color='pink', s=100, zorder=3, label='Spoofed Position (Pink Point)')

    # Add legend to the plot
    ax.legend(loc='upper right')


def refresh(event, ax, G):
    plot_roads_with_car_and_destination(ax, G)
    plt.draw()


def main():
    location_point = (51.5246, -0.1340)  # UCL coordinates
    G = ox.graph_from_point(location_point, dist=1000, network_type='drive')

    fig, ax = plt.subplots(figsize=(20, 15))

    plot_roads_with_car_and_destination(ax, G)

    # Add a refresh button
    ax_refresh = plt.axes([0.8, 0.025, 0.1, 0.04])
    btn_refresh = plt.Button(ax_refresh, 'Refresh')
    btn_refresh.on_clicked(lambda event: refresh(event, ax, G))

    # Set the window size
    manager = plt.get_current_fig_manager()
    manager.resize(2000, 1500)

    plt.show()


main()