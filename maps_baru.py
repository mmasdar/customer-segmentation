import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# Set page configuration
st.set_page_config(page_title='Customer Segmentation Dashboard', layout='wide')

# Interactive Button Area
with st.sidebar:
    st.markdown("<div style='padding: 20px;'>tombol pilihan</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button('1')
        st.button('3')
    with col2:
        st.button('2')
        st.button('4')

# Header
st.markdown("""
<div class='big-font' style='font-size: 40px; font-weight: bold; text-align: left; margin: 15px;'>CUSTOMER SEGMENTATION</div>
""", unsafe_allow_html=True)

# Customer count boxes
customer_count_cols = st.columns(4)
box_styles = [
    {"background-color": "#3498db", "color": "white", "font-size": "20px"},
    {"background-color": "#e74c3c", "color": "white", "font-size": "20px"},
    {"background-color": "#f1c40f", "color": "white", "font-size": "20px"},
    {"background-color": "#2ecc71", "color": "white", "font-size": "20px"}
]

customer_info = [
    {"top_text": "Customer A", "bottom_text": "37.3 %"},
    {"top_text": "Customer B", "bottom_text": "40 %"},
    {"top_text": "Customer C", "bottom_text": "11 %"},
    {"top_text": "Customer D", "bottom_text": "3 %"}
]

for i in range(4):
    with customer_count_cols[i]:
        st.markdown(f"<div style='{'; '.join([f'{prop}: {value}' for prop, value in box_styles[i].items()])}; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 20px; margin: 5px; height: 100px;'><div style='font-size: 14px;'>{customer_info[i]['top_text']}</div><div style='font-size: 24px; font-weight: bold; text-align: center;'>{customer_info[i]['bottom_text']}</div></div>", unsafe_allow_html=True)


# Main Content Area
#st.markdown("<h2>Map of Indonesia</h2>", unsafe_allow_html=True)

# Create a map of Indonesia using Plotly Express
fig = px.choropleth(
    locations=["Indonesia"],  # Provide the country name (Indonesia)
    locationmode="country names",
    color=[3],  # Use a dummy value (1) to represent Indonesia
    title="Map of Indonesia",
)

# Customize the map
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="lightgray",
    projection_scale=60,  # Increase scale for a wider map
    lataxis_range=[-20, 20],  # Adjust latitude axis range for a more centered view
    lonaxis_range=[90, 180],  # Adjust longitude axis range for a wider map
)

# Display the map with a specified width
st.plotly_chart(fig, use_container_width=True)


# Footer with three columns
footer_cols = st.columns(3)

# Left Box (Scatter Plot)
with footer_cols[0]:
    st.markdown("<h3>Scatter Plot</h3>", unsafe_allow_html=True)
    # Create a synthetic scatter plot
    random_data = np.random.randn(100, 2)
    scatter_fig = px.scatter(random_data, x=random_data[:, 0], y=random_data[:, 1])
    st.plotly_chart(scatter_fig, use_container_width=True)

# Center Box (Pie Chart)
with footer_cols[1]:
    st.markdown("<h3>Pie Chart</h3>", unsafe_allow_html=True)
    # Create a synthetic pie chart
    labels = ['Category A', 'Category B', 'Category C']
    values = [30, 40, 30]
    pie_fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(pie_fig, use_container_width=True)

# Right Box (Bar Chart)
with footer_cols[2]:
    st.markdown("<h3>Bar Chart</h3>", unsafe_allow_html=True)
    # Create a synthetic bar chart
    bar_fig = px.bar(x=['A', 'B', 'C', 'D', 'E'], y=[10, 8, 12, 6, 9])
    st.plotly_chart(bar_fig, use_container_width=True)