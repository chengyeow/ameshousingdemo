# Create and design the UI/UX for the portal for house prediction

import numpy as np
import pandas as pd
import pickle
import streamlit as st
# import sklearn
# from sklearn.linear_model import LinearRegression
from sklearn.linear_model import lasso


from PIL import Image
image = Image.open('proprata.jpg')

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)


st.title('ProPrata')
st.write('Your wish is our command')

page = st.sidebar.selectbox(
    'Select the following',
    ('Home', 'Select Home Features')
)

# @st.cache
# def load_data():
#     df = pd.read_csv('data/austen_poe.csv')
#     return df

if page == 'Home':
    st.image(image, caption='ProPrata Team')
    st.subheader('Your one and only property friend.')
    st.write('A well-established AMES company around your neighborhood for the last 10 years.')

if page == 'Select Home Features':
    # header
    st.subheader('Home Qualities to flip or flop')
    st.write('''Enter the desired or current qualities of your home''')

    # get user input
    age = st.slider('Building Age', format='%d', min_value=int(0), max_value=int(100), step=1, value=int(0))
    neigh_qual = st.slider('Neighboorhood Quality Index (Best=4, Good=3, Average=2, Below Average=1)', format='%d', 
                           min_value=int(1), max_value=int(4), step=1, value=int(2))
    local_conditions = st.slider('Local Positive Features (Best=2, Normal=1, Poor=0)', format='%d', min_value=int(0), 
                                 max_value=int(2), step=1, value=int(1))  
    was_remodeled = st.slider('Remodeled Building (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                              value=int(0))    
    overall_qual = st.slider('Overall Building Quality (Very  Excellent=10 <-> Average=5 <-> Very Poor=0)', format='%d', 
                             min_value=int(0), max_value=int(10),step=1, value=int(5))
    single_story = st.slider('Single Story Building (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                             value=int(1))  
    multiple_story = st.slider('Multiple Story Building (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                               value=int(0))         
    exter_qual = st.slider('External Quality (Excellent=5, Good=4, Average=3, Fair=2, Poor=1)', format='%d', min_value=int(1), 
                           max_value=int(5),step=1, value=int(3))
    exterior_1n2 = st.slider('Type of External Building Feature (Very  Excellent=10 <-> Average=5 <-> Very Poor=0)', format='%d', 
                             min_value=int(0), max_value=int(10),step=1, value=int(5))
    bldg_type_duplex = st.slider('Duplex_Building (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                                 value=int(0))
    bldg_type_twnhs = st.slider('Middle-unit Townhouse (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                                value=int(0))
    bldg_type_twnhse = st.slider('End-unit Townhouse (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                                 value=int(0))
    bldg_type_2fmcon = st.slider('Family House (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                                 value=int(0))
    roof_style_hip = st.slider('High Roof Quality (Yes=1, No=0)', format='%d', min_value=int(0), max_value=int(1), step=1, 
                               value=int(0))
    mas_vnr_ord = st.slider('Masonry Vaneer Type (Quality=1, Basic/None=0)', format='%d', min_value=int(0), max_value=int(1), 
                            step=1, value=int(0))
    functional = st.slider('Building Functionality (Typical=8 <-> Salvage only=0)', format='%d', min_value=int(0), 
                           max_value=int(8), step=1, value=int(8))
    lot_frontage = st.slider('Lot Frontage (Linear feet of street connected to property)', format='%d', min_value=int(20), 
                             max_value=int(200), step=10, value=int(100))
    lot_area = st.slider('Lot Size in square feet', format='%d', min_value=int(2000), max_value=int(215000), step=1000, 
                         value=int(100000))
    outside_porch_sf = st.slider('Outside Grill Space sqft', format='%d', min_value=int(0), max_value=int(1400), step=100, 
                                 value=int(700))
    garage_fin_area = st.slider('Garage Area sqft', format='%d', min_value=int(0), max_value=int(4000), step=100, 
                                value=int(1700))
    garage_cars = st.slider('Car Garage', format='%d', min_value=int(0), max_value=int(5), step=1, value=int(1))
    paved_drive = st.slider('Paved Driveway (Paved=2, Partial Pavement=1, Dirt/Gravel=0', format='%d', min_value=int(0), 
                            max_value=int(2), step=1, value=int(2))
    basement_qual = st.slider('Basement Quality (Excellent=5, Good=4, Average=3, Fair=2, Poor=1, No Basement=0)', format='%d', 
                              min_value=int(0), max_value=int(5),step=1, value=int(3))
    bsmtfin_type_sf = st.slider('Finished Basement Sqft', format='%d', min_value=int(0), max_value=int(13000), step=1000, 
                                value=int(8000))
    bsmt_exposure = st.slider('Basement Ceiling Height (Good=4, Average=3, Min=2, No=1, No Basement=0', format='%d', 
                              min_value=int(0), max_value=int(4), step=1, value=int(3))   
    heater_qual = st.slider('Heater Quality (Excellent=5, Good=4, Average=3, Fair=2, Poor=1)', format='%d', min_value=int(1), 
                            max_value=int(5),step=1, value=int(3))
    kitchen_qual = st.slider('Kitchen Quality (Excellent=5, Good=4, Average=3, Fair=2, Poor=1)', format='%d', min_value=int(1), 
                             max_value=int(5),step=1, value=int(3))
    fireplace_qu = st.slider('Fireplace Quality(Excellent=5, Good=4, Average=3, Fair=2, Poor=1, No Fireplace=0)', format='%d', 
                             min_value=int(0), max_value=int(5),step=1, value=int(3))
    all_floors_sf = st.slider('Finished Upstairs sqft', format='%d', min_value=int(300), max_value=int(4400), step=100, 
                              value=int(2200))
    totrms_abvgrd = st.slider('Rooms Upstairs', format='%d', min_value=int(2), max_value=int(14), step=1, value=int(6))
    room_size = st.slider('Size of Rooms sqft', format='%d', min_value=int(120), max_value=int(560), step=10, value=int(280))
    all_baths = st.slider('All bath rooms', format='%d', min_value=int(1), max_value=int(7), step=1, value=int(4))
    gr_liv_area = st.slider('Ground Living Space sqft', format='%d', min_value=int(300), max_value=int(4400), step=100, 
                            value=int(2200))
                
    data = np.array([age, neigh_qual, local_conditions, was_remodeled, overall_qual, single_story, multiple_story,
                     exter_qual, exterior_1n2, bldg_type_duplex, bldg_type_twnhs, bldg_type_twnhse, bldg_type_2fmcon, 
                     roof_style_hip, mas_vnr_ord, functional, lot_frontage, lot_area, outside_porch_sf, 
                     garage_fin_area, garage_cars, paved_drive, basement_qual, bsmtfin_type_sf, bsmt_exposure, 
                     heater_qual, kitchen_qual, fireplace_qu, all_floors_sf, totrms_abvgrd, room_size,
                     all_baths, gr_liv_area]).reshape(1, -1)
    

    st.subheader('Estimating your house price:')

#     with open('./model/model_ames_cy1.p', 'rb') as pickle_in:
#         model = pickle.load(pickle_in)

    pickle_in = open('./model/model_ames_cylr.p', 'rb')
    model = pickle.load(pickle_in)
        
    predicted_price = model.predict(data)[0]
    st.subheader(f'Your home is worth {round(predicted_price, 2)}. Congratulations!')
#    st.subheader('Results:')
#    st.write(f'Your home is worth {round(predicted_price, 2)}. Congratulations!')
    
    
    
    