import folium

# start and end nodes should be in the form:
# START = ["START", latitude, longitude]
def draw_map(
    START, END,
    optimal_path, loc_matrix,
    expanded_nodes_U, expanded_routes_U,
    expanded_nodes_A1, expanded_routes_A1,
    expanded_nodes_A2, expanded_routes_A2):
    
    m = folium.Map(
    location=[16, 108],
    tiles='cartodbpositron',
    zoom_start=7,
)

    from folium.plugins import Geocoder
    Geocoder().add_to(m)

    optimal_layer = folium.FeatureGroup(name = "optimal layer by ucs/a*")
    ucs_layer = folium.FeatureGroup(name = "ucs layer")
    a_star_layer1 = folium.FeatureGroup(name = "a* layer with coef = 1")
    a_star_layer2 = folium.FeatureGroup(name = "a* layer with coef = 2")


    newpath = [START]
    for name in optimal_path:
        for city in loc_matrix:
            if city[0] == name:
                coor = city[1].split(',')
                latitude = float(coor[0])
                longitude = float(coor[1].strip())
                newpath.append([name, latitude, longitude])
    
    newpath.append(END)

    for city in newpath:
        if city[0] == 'START':
            pop = 'your starting point'
            col = 'lightgreen'
        elif city[0] == 'ENDS':
            pop = 'your ending point'
            col = 'red'
        else:
            pop = 'in a route'
            col = 'orange'
        folium.Marker(
        location = city[1:],
        popup = pop,
        tooltip = city[0],
        icon = folium.Icon(color = col)
        ).add_to(optimal_layer)
    
    for city in loc_matrix:
        if city[0] not in optimal_path:
            coor = city[1].split(',')
            latitude = float(coor[0])
            longitude = float(coor[1].strip())
            folium.Marker(
                location = [latitude, longitude],
                popup = 'not in any route',
                tooltip = city[0]
            ).add_to(optimal_layer)
        
        if city[0] in expanded_nodes_U:
            coor = city[1].split(',')
            latitude = float(coor[0])
            longitude = float(coor[1].strip())
            if expanded_nodes_U[city[0]] <= 5:
                col = 'lightgreen'
            elif expanded_nodes_U[city[0]] > 5 and expanded_nodes_U[city[0]] <= 10:
                col = 'orange'
            else:
                col = 'red'
            folium.Marker(
                location = [latitude, longitude],
                popup = 'appear {} times'.format(expanded_nodes_U[city[0]]),
                tooltip = city[0],
                icon = folium.Icon(color = col)
            ).add_to(ucs_layer)
        else: 
            coor = city[1].split(',')
            latitude = float(coor[0])
            longitude = float(coor[1].strip())
            folium.Marker(
                location = [latitude, longitude],
                popup = "haven't expanded",
                tooltip = city[0]
            ).add_to(ucs_layer)

        if city[0] in expanded_nodes_A1:
            coor = city[1].split(',')
            latitude = float(coor[0])
            longitude = float(coor[1].strip())
            if expanded_nodes_A1[city[0]] <= 5:
                col = 'lightgreen'
            elif expanded_nodes_A1[city[0]] > 5 and expanded_nodes_A1[city[0]] <= 10:
                col = 'orange'
            else:
                col = 'red'
            folium.Marker(
                location = [latitude, longitude],
                popup = 'appear {} times'.format(expanded_nodes_A1[city[0]]),
                tooltip = city[0],
                icon = folium.Icon(color = col)
            ).add_to(a_star_layer1)
        else: 
            coor = city[1].split(',')
            latitude = float(coor[0])
            longitude = float(coor[1].strip())
            folium.Marker(
                location = [latitude, longitude],
                popup = "haven't expanded",
                tooltip = city[0]
            ).add_to(a_star_layer1)
        
        if city[0] in expanded_nodes_A2:
            coor = city[1].split(',')
            latitude = float(coor[0])
            longitude = float(coor[1].strip())
            if expanded_nodes_A2[city[0]] <= 5:
                col = 'lightgreen'
            elif expanded_nodes_A2[city[0]] > 5 and expanded_nodes_A2[city[0]] <= 10:
                col = 'orange'
            else:
                col = 'red'
            folium.Marker(
                location = [latitude, longitude],
                popup = 'appear {} times'.format(expanded_nodes_A2[city[0]]),
                tooltip = city[0],
                icon = folium.Icon(color = col)
            ).add_to(a_star_layer1)
        else: 
            coor = city[1].split(',')
            latitude = float(coor[0])
            longitude = float(coor[1].strip())
            folium.Marker(
                location = [latitude, longitude],
                popup = "haven't expanded",
                tooltip = city[0]
            ).add_to(a_star_layer2)
        
    lines = []
    for i in newpath:
        lines.append(tuple(i[1:]))
    folium.PolyLine(lines, color = 'red', weight = 5).add_to(optimal_layer)

    for city in expanded_routes_U:
        draw_line(city, ucs_layer, loc_matrix, 'pink')
    
    for city in expanded_routes_A1:
        draw_line(city, a_star_layer1, loc_matrix, 'purple')
    
    for city in expanded_routes_A2:
        draw_line(city, a_star_layer2, loc_matrix, 'blue')
    

    optimal_layer.add_to(m)
    ucs_layer.add_to(m)
    a_star_layer1.add_to(m)
    a_star_layer2.add_to(m)

    folium.LayerControl().add_to(m)
    m.save("output.html")


def draw_line(city, layer, loc_matrix, col):
    path = city.path
    newpath = []
    for name in path:
        for city in loc_matrix:
            if city[0] == name:
                coor = city[1].split(',')
                latitude = float(coor[0])
                longitude = float(coor[1].strip())
                newpath.append([name, latitude, longitude])
    lines = []
    for i in newpath:
        lines.append(tuple(i[1:]))
    folium.PolyLine(lines, color = col, weight = 2).add_to(layer)