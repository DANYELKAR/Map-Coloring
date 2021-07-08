import plotly.express as px
from random import choice

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]


# Write your code here

def read_graph(path):

    graph = {}
    last_added = None

    with open(path) as f:
        for line in f.readlines():
            if line.startswith("-"):
                neighbor = line[2:-1]
                graph[last_added].append(neighbor)
            else:
                nodename = line[:-1]
                if nodename not in graph:
                    graph[nodename] = []
                    last_added = nodename
    return graph

def paint_map(graph):
    colormap = {
        "Argentina": "uncolored",
        "Bolivia": "uncolored",
        "Brazil": "uncolored",
        "Chile": "uncolored",
        "Colombia": "uncolored",
        "Ecuador": "uncolored",
        "Falkland Islands": "uncolored",
        "Guyana": "uncolored",
        "Paraguay": "uncolored",
        "Peru": "uncolored",
        "Suriname": "uncolored",
        "Uruguay": "uncolored",
        "Venezuela": "uncolored"}

    waitings = [["Argentina"], ["Falkland Islands"]]
    error = False

    for waiting in waitings:
        visited = []
        while len(waiting) > 0 and not error:
            node = waiting.pop(0)

            avaliable_colors = colors[:]
            for neighbor in graph[node]:
                try:
                    avaliable_colors.remove(colormap[neighbor])
                except ValueError:
                    pass

            if colormap[node] == "uncolored":
                try:
                    colormap[node] = choice(avaliable_colors)
                    visited.append(node)
                except IndexError:
                    error = True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if neighbor not in waiting:
                        waiting.insert(0, neighbor)

    if error:
        return paint_map(graph)

    return colormap


# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":


    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    #plot_choropleth(colormap=colormap_test)

    graph = read_graph("countries.txt")
    colormap = paint_map(graph)
    plot_choropleth(colormap=colormap)