# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:08:19 2023

@author: Rishikesh Sreehari
"""

import plotly.graph_objects as go

# Define data
source_data = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14]
target_data = [7, 8, 8, 9, 10, 11, 11, 12, 13, 13, 14, 14, 7, 15, 16, 15]
value_data = [120, 80, 40, 150, 30, 50, 120, 180, 50, 60, 40, 60, 100, 70, 80, 70]

# Create the Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=[
            "Primary Energy", "Coal", "Oil", "Natural Gas", "Renewable",
            "Electricity", "Industrial", "Residential", "Commercial",
            "Transportation", "Refinery", "Agriculture", "Power Plants",
            "Losses", "Exports", "Non-Energy Use"
        ],
    ),
    link=dict(
        source=source_data,
        target=target_data,
        value=value_data
    )
))

# Set the title
fig.update_layout(title_text="Primary Energy Flow - India (Dummy data!)")

# Display the Sankey diagram
fig.show()

# Display the Sankey diagram
fig.show()



fig.write_html("path\sankey_diagram.html")

