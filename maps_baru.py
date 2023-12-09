import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu



# Set page configuration
st.set_page_config(page_title='Customer Segmentation Dashboard', layout='wide')

#st.sidebar.markdown("<h1>Clustering Analysis</h1>", unsafe_allow_html=True)

# Inisialisasi variabel untuk menyimpan teks yang akan ditampilkan
#selected_button = None

# Sidebar dengan tombol pilihan
#with st.sidebar:
#    st.markdown("<div style='padding: 20px;'>Select Clustering : </div>", unsafe_allow_html=True)
#    if st.button('🌍    Spending Behavior'):
#        selected_button = "Cluster Spending Behavior"
#    if st.button('🌍    Product Preference'):
#        selected_button = "Cluster Product Preference"
#    if st.button('🌍    Loyalty and Engagement'):
#        selected_button = "Cluster Loyalty and Engagement"
#    if st.button('🌍    Demographic'):
#        selected_button = "Cluster Demographic"
#    if st.button('🌍    Payment and Shipping'):
#        selected_button = "Cluster Payment and Shipping"

selected = None

with st.sidebar:
    selected = option_menu("Clustering Analysis", ['General', 
                                        'Spending Behavior', 
                                        'Product Preference',
                                        'Loyalty and Engagement',
                                        'Demographic',
                                        'Payment and Shipping'], 

        icons=['house', 
                'currency-dollar', 
                'basket-fill',
                'arrow-through-heart-fill',
                'globe-americas',
                'truck'], menu_icon="cast", default_index=1)
    #selected

st.sidebar.markdown("<h1>KPI</h1>", unsafe_allow_html=True)

# Menampilkan teks di bagian bawah halaman berdasarkan tombol yang ditekan
if selected:
    st.sidebar.markdown(f"<h3>{selected}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3>{selected}</h3>", unsafe_allow_html=True)

# Bagian utama
st.markdown("""
<div class='big-font' style='font-size: 40px; font-weight: bold; text-align: left; margin: 5px 0 15px;'>CUSTOMER SEGMENTATION</div>
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
        st.markdown(f"<div style='{'; '.join([f'{prop}: {value}' for prop, value in box_styles[i].items()])}; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 10px; margin: 0px; height: 100px;'><div style='font-size: 14px;'>{customer_info[i]['top_text']}</div><div style='font-size: 24px; font-weight: bold; text-align: center;'>{customer_info[i]['bottom_text']}</div></div>", unsafe_allow_html=True)


# Main Content Area
#st.markdown("<h2>Map of Indonesia</h2>", unsafe_allow_html=True)

# Data yang akan digunakan untuk peta Indonesia
data = {
    "Country": ["Indonesia"],
    "Life expectancy": [3],
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)


# Membuat peta Indonesia menggunakan Plotly Express
fig = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Life expectancy",
    color_continuous_scale="Inferno",  # Gunakan skema warna yang sama dengan sebelumnya
    title="Life Expectancy in Indonesia",
)

# Menyesuaikan tampilan peta
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="black",
    showland=True,
    landcolor="lightgray",
    projection_scale= 0.9,  # Sesuaikan dengan skala yang sesuai
    lataxis_range=[-13, 13],  # Rentang latitude sesuai dengan Indonesia
    lonaxis_range=[94, 141]  # Rentang longitude sesuai dengan Indonesia
)

# Mengatur ukuran peta dengan ukuran yang lebih besar
fig.update_layout(
    width=800,  # Sesuaikan ukuran peta sesuai kebutuhan
    height=600   # Sesuaikan ukuran peta sesuai kebutuhan
)



# Create a sidebar column for the pie chart
col1, col2 = st.columns([3, 1])

# Add the pie chart to the sidebar column
with col1:
    st.plotly_chart(fig, use_container_width=True)


# Display the map in the larger column
with col2:
    # Create a synthetic pie chart
    # Create a synthetic pie chart
    labels = ['Category A', 'Category B', 'Category C']
    values = [30, 40, 30]
    fig = px.pie(labels = labels, 
            values = values, 
            title = "Pie Chart Example")

    # Remove the legend
    fig.update_layout(showlegend=False)

    # Display the modified pie chart with a square aspect ratio
    st.plotly_chart(fig, use_container_width=True, height=500)


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
