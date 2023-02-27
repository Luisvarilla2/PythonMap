import folium
m = folium.Map(location=[-34.60661, -58.43558], tiles="Stamen Toner", zoom_start=12)

folium.Circle(
    radius=18,
    location=[-34.60957, -58.43376],
    popup="The Waterfront",
    color="crimson",
    fill=False,
).add_to(m)
m.save("folium.html")