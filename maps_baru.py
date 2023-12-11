import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


# Load the CSV file# Load the CSV file
file_path = r'trained model/clustered_shopping_behavior.csv'  # Update with your file path
data = pd.read_csv(file_path)

# Calculate the average of each column
average_purchase_amount = data['Purchase Amount (USD)'].mean()
average_review_rating = data['Review Rating'].mean()
average_previous_purchases = data['Previous Purchases'].mean()
total_customers = data['Customer ID'].nunique()


# Set page configuration
st.set_page_config(page_title='Customer Segmentation Dashboard', layout='wide')

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
                                        'truck'], menu_icon="cast", default_index=0)
    #selected

# Add a selectbox in the sidebar to choose the theme
col1, col2 = st.sidebar.columns(2)
theme = col1.checkbox('Dark mode', key='theme')
funky = col2.checkbox('Funky mode', key='funky')

# Apply the selected theme
if theme:
    st.markdown("""
        <style>
            /* Main content area */
            .main {
                background-color: #0E1117;
                color: #FFFFFF;
            }
            /* Sidebar */
            .sidebar .sidebar-content {
                background-color: #1E2022;
                color: #DDDDDD;
            }
            /* Headers in main content and sidebar */
            .main h1, .main h2, .main h3, .main h4, .main h5, .main h6,
            .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3, .sidebar .sidebar-content h4, .sidebar .sidebar-content h5, .sidebar .sidebar-content h6 {
                color: #E0E0E0;
            }
            /* Text and links in main content and sidebar */
            .main body, .main a, .sidebar .sidebar-content body, .sidebar .sidebar-content a {
                color: #DDDDDD;
            }
            /* Streamlit widgets in main content and sidebar */
            .main .stTextInput, .main .stSelectbox, .main .stDateInput, .main .stTimeInput, .main .stTextArea, .main .stNumberInput, .main .stFileUploader, .main .stButton > button,
            .sidebar .sidebar-content .stTextInput, .sidebar .sidebar-content .stSelectbox, .sidebar .sidebar-content .stDateInput, .sidebar .sidebar-content .stTimeInput, .sidebar .sidebar-content .stTextArea, .sidebar .sidebar-content .stNumberInput, .sidebar .sidebar-content .stFileUploader, .sidebar .sidebar-content .stButton > button {
                background-color: #262730;
                color: #FFFFFF;
            }
            /* Option menu in sidebar */
            .sidebar .sidebar-content .st-bb {
                background-color: #1E2022;
            }
            .sidebar .sidebar-content .st-bb .st-bv {
                color: #DDDDDD;
            }
            /* KPI header in sidebar */
            .sidebar .sidebar-content h1 {
                font-size: 24px;
                color: #E0E0E0;
            }
            /* Plotly chart background */
            .js-plotly-plot .plotly {
                background-color: #0E1117;
            }
            /* Footer */
            footer {
                background-color: #1E2022;
                color: #FFFFFF;
            }
        </style>
    """, unsafe_allow_html=True)
    chart_bg_color = '#0E1117'  # Dark background color
    text_color = '#FFFFFF'      # White text color
    land_color = '#121212'      # Darker land color for contrast
    geo_bg_color = '#0E1117'    # Dark geo background color
else:
    st.markdown("""
        <style>
            .main {
                background-color: #FFFFFF;
                color: #000000;
            }
            .sidebar .sidebar-content {
                background-color: #F0F2F6;
            }
        </style>
    """, unsafe_allow_html=True)
    chart_bg_color = '#FFFFFF'  # Light background color
    text_color = '#000000'      # Black text color
    land_color = 'lightgray'    # Standard light land color
    geo_bg_color = '#E5ECF6'    # Light geo background color


#st.sidebar.markdown("<h1>KPI</h1>", unsafe_allow_html=True)

# Bagian utama

# Menampilkan teks di bagian bawah halaman berdasarkan tombol yang ditekan
if selected == "General":

    # Paragraf yang ingin Anda tambahkan
    additional_paragraph = """
    This Dashboard has been crafted to offer a deeper understanding of customer behavior and Key Performance Indicator (KPI) analysis based on customer data. Unlock the power of this application to pinpoint customer segments, uncover trends, and gain invaluable insights into how customers engage with your business.
    """

    # Buat kotak teks dengan teks yang digabungkan
    st.sidebar.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 5px;'>About the Cluster</div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(
    f"<div style='margin-top: 5px; margin-bottom: 5px; padding-left: 10px; border-left: 2px solid #333;'>{additional_paragraph}</div>",
    unsafe_allow_html=True
    )

    st.markdown("""
    <div class='big-font' style='font-size: 40px; font-weight: bold; text-align: center; margin: 0 0 0;'>Customer Clustering and KPI Dashboard</div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 20px;'>{selected}</div>
    """, unsafe_allow_html=True)

elif selected == "Spending Behavior":
    additional_paragraph = """
    Identify customer segments based on their spending habits.This can help identify high spenders, bargain hunters, and occasional shoppers. Tailored marketing strategies can be developed for each group, such as exclusive offers for high spenders or targeted discounts for bargain hunters.
    """
    st.sidebar.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 5px;'>About the Cluster</div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(
    f"<div style='margin-top: 5px; margin-bottom: 5px; padding-left: 10px; border-left: 2px solid #333;'>{additional_paragraph}</div>",
    unsafe_allow_html=True
    )

    st.markdown("""
    <div class='big-font' style='font-size: 40px; font-weight: bold; text-align: center; margin: 0 0 0;'>Customer Clustering and KPI Dashboard</div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 20px;'>{selected}</div>
    """, unsafe_allow_html=True)

elif selected == "Product Preference":
    additional_paragraph = """
    Group customers based on the types of products they purchase.  Understanding product preferences can assist in inventory management, personalized marketing, and product development. Identify customer segments based on their spending habits.This can help identify high spenders, bargain hunters, and occasional shoppers. Tailored marketing strategies can be developed for each group, such as exclusive offers for high spenders or targeted discounts for bargain hunters.
    """
    st.sidebar.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 5px;'>About the Cluster</div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(
    f"<div style='margin-top: 5px; margin-bottom: 5px; padding-left: 10px; border-left: 2px solid #333;'>{additional_paragraph}</div>",
    unsafe_allow_html=True
    )

    st.markdown("""
    <div class='big-font' style='font-size: 40px; font-weight: bold; text-align: center; margin: 0 0 0;'>Customer Clustering and KPI Dashboard</div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 20px;'>{selected}</div>
    """, unsafe_allow_html=True)

elif selected == "Loyalty and Engagement":
    additional_paragraph = """
    Segment customers based on their loyalty and engagement with the brand. Identify loyal customers who can be targeted for loyalty programs and new customers who might need engagement strategies to increase their loyalty.
    """
    st.sidebar.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 5px;'>About the Cluster</div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(
    f"<div style='margin-top: 5px; margin-bottom: 5px; padding-left: 10px; border-left: 2px solid #333;'>{additional_paragraph}</div>",
    unsafe_allow_html=True
    )

    st.markdown("""
    <div class='big-font' style='font-size: 40px; font-weight: bold; text-align: center; margin: 0 0 0;'>Customer Clustering and KPI Dashboard</div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 20px;'>{selected}</div>
    """, unsafe_allow_html=True)

elif selected == "Demographic":
    additional_paragraph = """
    Understand customer segments based on demographic data. Tailor marketing campaigns and product offerings to suit the needs and preferences of different demographic groups.
    """
    st.sidebar.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 5px;'>About the Cluster</div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(
    f"<div style='margin-top: 5px; margin-bottom: 5px; padding-left: 10px; border-left: 2px solid #333;'>{additional_paragraph}</div>",
    unsafe_allow_html=True
    )

    st.markdown("""
    <div class='big-font' style='font-size: 40px; font-weight: bold; text-align: center; margin: 0 0 0;'>Customer Clustering and KPI Dashboard</div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 20px;'>{selected}</div>
    """, unsafe_allow_html=True)

elif selected == "Payment and Shipping":
    additional_paragraph = """
    Segment customers based on their payment and shipping preferences. This can help in optimizing payment and shipping options to enhance customer satisfaction.
    """
    st.sidebar.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 5px;'>About the Cluster</div>
    """, unsafe_allow_html=True)
    st.sidebar.markdown(
    f"<div style='margin-top: 5px; margin-bottom: 5px; padding-left: 10px; border-left: 2px solid #333;'>{additional_paragraph}</div>",
    unsafe_allow_html=True
    )

    st.markdown("""
    <div class='big-font' style='font-size: 40px; font-weight: bold; text-align: center; margin: 0 0 0;'>Customer Clustering and KPI Dashboard</div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='big-font' style='font-size: 20px; text-align: center; margin: 0 0 20px;'>{selected}</div>
    """, unsafe_allow_html=True)


# Customer count boxes
customer_count_cols = st.columns(4)
box_styles = [
    {"background-color": "#3498db", "color": "white", "font-size": "20px"},
    {"background-color": "#e74c3c", "color": "white", "font-size": "20px"},
    {"background-color": "#f1c40f", "color": "white", "font-size": "20px"},
    {"background-color": "#2ecc71", "color": "white", "font-size": "20px"}
]

# Update customer_info with the calculated averages
customer_info = [
    {"top_text": "Total Customer", "bottom_text": total_customers},
    {"top_text": "Average Purchase Amount", "bottom_text": f"$ {average_purchase_amount:.2f}"},
    {"top_text": "Average Review Rating", "bottom_text": f"{average_review_rating:.2f} / 5"},
    {"top_text": "Retention Rate", "bottom_text": f"{average_previous_purchases:.2f} times"}
]

for i in range(4):
    with customer_count_cols[i]:
        st.markdown(f"<div style='{'; '.join([f'{prop}: {value}' for prop, value in box_styles[i].items()])}; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 10px; margin: 0px; height: 100px;'><div style='font-size: 14px;'>{customer_info[i]['top_text']}</div><div style='font-size: 34px; font-weight: bold; text-align: center;'>{customer_info[i]['bottom_text']}</div></div>", unsafe_allow_html=True)


# Main Content Area
#st.markdown("<h2>Map of Indonesia</h2>", unsafe_allow_html=True)

# For demonstration, let's count the number of entries per location

# Assuming 'data' is your DataFrame
# Calculate total purchase amount for each state

# Mapping of full state names to abbreviations
state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
    'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
    'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

data['State Abbreviation'] = data['Location'].map(state_abbreviations)

# Assuming 'data' is your DataFrame

def general_analysis(data):
    # Calculate total purchase amount for each state
    purchase_amount_by_state = data.groupby('State Abbreviation')['Purchase Amount (USD)'].sum().reset_index()

    # Create a choropleth map
    fig = px.choropleth(
        purchase_amount_by_state,
        locations="State Abbreviation",
        locationmode="USA-states",
        color="Purchase Amount (USD)",
        color_continuous_scale="Viridis" if theme == 'Dark' else "Cividis",
        scope="usa",
        labels={"Purchase Amount (USD)": "Total Purchase Amount"})

    # Calculate the distribution of clusters
    cluster_distribution = data['Category'].value_counts(normalize=True) * 100

    labels = cluster_distribution.index.tolist()
    values = cluster_distribution.values.tolist()

    # Create a pie chart
    fig2 = px.pie(names=labels, values=values)
    return fig, fig2

def spending_behavior_analysis(data):
    # Calculate total purchase amount for each state
    mode_df = data.groupby('State Abbreviation')['Cluster Spending Behavior'].agg(lambda x: x.mode()[0]).reset_index()
    
    # Create a choropleth map
    fig = px.choropleth(
        mode_df,
        locations="State Abbreviation",
        locationmode="USA-states",
        color="Cluster Spending Behavior",
        color_continuous_scale="Viridis",
        scope="usa",
        labels={"Spending Behavior": "Cluster"})

    # Calculate the distribution of clusters
    cluster_distribution = data['Cluster Product Preference'].value_counts(normalize=True) * 100

    labels = cluster_distribution.index.tolist()
    values = cluster_distribution.values.tolist()

    # Create a pie chart
    fig2 = px.pie(names=labels, values=values)
    return fig, fig2


def product_preference_analysis(data):
    # Calculate total purchase amount for each state
    mode_df = data.groupby('State Abbreviation')['Cluster Product Preference'].agg(lambda x: x.mode()[0]).reset_index()
    
    # Create a choropleth map
    fig = px.choropleth(
        mode_df,
        locations="State Abbreviation",
        locationmode="USA-states",
        color="Cluster Product Preference",
        color_continuous_scale="Viridis",
        scope="usa",
        labels={"Spending Behavior": "Cluster"})

    # Calculate the distribution of clusters
    cluster_distribution = data['Cluster Product Preference'].value_counts(normalize=True) * 100

    labels = cluster_distribution.index.tolist()
    values = cluster_distribution.values.tolist()

    # Create a pie chart
    fig2 = px.pie(names=labels, values=values)

    return fig, fig2

def loyalthy_analysis(data):
    # Calculate total purchase amount for each state
    mode_df = data.groupby('State Abbreviation')['Cluster Loyalty and Engagement'].agg(lambda x: x.mode()[0]).reset_index()
    
    # Create a choropleth map
    fig = px.choropleth(
        mode_df,
        locations="State Abbreviation",
        locationmode="USA-states",
        color="Cluster Loyalty and Engagement",
        color_continuous_scale="Viridis",
        scope="usa",
        labels={"Loyalthy and Engagement": "Cluster"})

    # Calculate the distribution of clusters
    cluster_distribution = data['Cluster Loyalty and Engagement'].value_counts(normalize=True) * 100

    labels = cluster_distribution.index.tolist()
    values = cluster_distribution.values.tolist()

    # Create a pie chart
    fig2 = px.pie(names=labels, values=values)

    return fig, fig2

def demographic_analysis(data):
    # Calculate total purchase amount for each state
    mode_df = data.groupby('State Abbreviation')['Cluster Demographic'].agg(lambda x: x.mode()[0]).reset_index()
    
    # Create a choropleth map
    fig = px.choropleth(
        mode_df,
        locations="State Abbreviation",
        locationmode="USA-states",
        color="Cluster Demographic",
        color_continuous_scale="Viridis",
        scope="usa",
        labels={"Demographic": "Cluster"})

    # Calculate the distribution of clusters
    cluster_distribution = data['Cluster Demographic'].value_counts(normalize=True) * 100

    labels = cluster_distribution.index.tolist()
    values = cluster_distribution.values.tolist()

    # Create a pie chart
    fig2 = px.pie(names=labels, values=values)

    return fig, fig2

def payment_analysis(data):
    # Calculate total purchase amount for each state
    mode_df = data.groupby('State Abbreviation')['Cluster Payment and Shipping'].agg(lambda x: x.mode()[0]).reset_index()
    
    # Create a choropleth map
    fig = px.choropleth(
        mode_df,
        locations="State Abbreviation",
        locationmode="USA-states",
        color="Cluster Payment and Shipping",
        color_continuous_scale="Viridis",
        scope="usa",
        labels={"Payment and Shipping": "Cluster"})

    # Calculate the distribution of clusters
    cluster_distribution = data['Cluster Payment and Shipping'].value_counts(normalize=True) * 100

    labels = cluster_distribution.index.tolist()
    values = cluster_distribution.values.tolist()

    # Create a pie chart
    fig2 = px.pie(names=labels, values=values)

    return fig, fig2


# Execute functions based on the selected option
if selected == 'General':
    fig, fig2 = general_analysis(data)
elif selected == 'Spending Behavior':
    fig, fig2 = spending_behavior_analysis(data)
elif selected == 'Product Preference':
    fig, fig2 = product_preference_analysis(data)
elif selected == 'Loyalty and Engagement':
    fig, fig2 = loyalthy_analysis(data)
elif selected == 'Demographic':
    fig, fig2 = demographic_analysis(data)
elif selected == 'Payment and Shipping':
    fig, fig2 = payment_analysis(data)


# Adjust the map's appearance
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="black" if theme == 'Dark' else "grey",
    showland=True,
    landcolor=land_color,
    bgcolor=geo_bg_color
)

# Update layout
fig.update_layout(
    paper_bgcolor=chart_bg_color,
    plot_bgcolor=chart_bg_color,
    font_color=text_color,
    width=800,
    height=600,
    margin={"t": 10, "l": 10, "r": 10},
    showlegend=False
)

# Remove the legend
fig2.update_traces(hole=0)

fig2.update_layout(
    paper_bgcolor=chart_bg_color,
    plot_bgcolor=chart_bg_color,
    font_color=text_color,
    title=" ",  # Empty title for spacing
    margin={"t": 5, "l": 5, "r": 5, "b": 5})


# Create a sidebar column for the pie chart
col1, col2 = st.columns([3, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)

# Footer with three columns
footer_cols = st.columns(3)

# Margin yang ingin diatur
margin = {"t": 10, "b": 10, "l": 10, "r": 10}

# Left Box (Scatter Plot)
with footer_cols[0]:
    st.markdown("<h3>Scatter Plot</h3>", unsafe_allow_html=True)
    # Create a synthetic scatter plot
    random_data = np.random.randn(100, 2)
    scatter_fig = px.scatter(random_data, x=random_data[:, 0], y=random_data[:, 1])
    # Atur margin untuk scatter plot
    scatter_fig.update_layout(margin=margin,
                                paper_bgcolor=chart_bg_color,
                                plot_bgcolor=chart_bg_color,
                                font_color=text_color,)
    st.plotly_chart(scatter_fig, use_container_width=True)

# Center Box (Pie Chart)
with footer_cols[1]:
    st.markdown("<h3>Pie Chart</h3>", unsafe_allow_html=True)
    # Create a synthetic pie chart
    labels = ['Category A', 'Category B', 'Category C']
    values = [30, 40, 30]
    pie_fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    # Atur margin untuk pie chart
    pie_fig.update_layout(margin=margin,
                                paper_bgcolor=chart_bg_color,
                                plot_bgcolor=chart_bg_color,
                                font_color=text_color,)
    st.plotly_chart(pie_fig, use_container_width=True)

# Right Box (Bar Chart)
with footer_cols[2]:
    st.markdown("<h3>Bar Chart</h3>", unsafe_allow_html=True)
    # Create a synthetic bar chart
    bar_fig = px.bar(x=['A', 'B', 'C', 'D', 'E'], y=[10, 8, 12, 6, 9])
    # Atur margin untuk bar chart
    bar_fig.update_layout(margin=margin,
                                paper_bgcolor=chart_bg_color,
                                plot_bgcolor=chart_bg_color,
                                font_color=text_color,)
    st.plotly_chart(bar_fig, use_container_width=True)


