import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Features", ["Smoothing", 'Transform', 'Edges'], 
        icons=['house', 'gear','gear'], menu_icon="cast", default_index=0,
        styles={"nav-link-selected": {"background-color": "#2C3845"}})



st.title("Image processing")


img_file = st.file_uploader("Choose a image file", type=["jpg","jpeg","png"])
if img_file is not None:
    # Convert the file to an opencv image.
    img_file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    image = cv.imdecode(img_file_bytes,1)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    
    '''
    Smoothing sections
    '''
    if selected == "Smoothing":
        Smoothing_selected = option_menu("Smoothing", ["Mean", 'Median', 'Gaussian', "Bilateral"], 
                            menu_icon="cast", default_index=0, orientation="horizontal",
                            styles={ "container": {"padding": "5!important", "background-color": "#f0f2f6"},
                                    "icon": {"color": "orange", "font-size": "15px"}, 
                                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                    "nav-link-selected": {"background-color": "#2C3845"}})
        '''
        Mean smoothing 
        '''
        if Smoothing_selected == "Mean":
            st.write("**Parameters**")
            col1, col2 = st.columns(2)
            with col1:
                value = st.slider("Kernel value", 3, 63,3,2)
                kernel =(value,value)
                st.write("**Kernel:**", kernel)
            with col2:
                b_types = st.selectbox("Border type", ["CONSTANT", "REPLICATE","REFLECT", "TRANSPARENT", "ISOLATED"])
                if b_types == "CONSTANT":
                    bt = 0
                elif b_types == "REPLICATE":
                    bt = 1
                elif b_types == "REFLECT":
                    bt = 2
                elif b_types == "TRANSPARENT":
                    bt = 5
                elif b_types == "ISOLATED":
                    bt = 16
                st.write("**Border type:**",b_types )
            img = cv.blur(image, kernel,borderType = bt)	
            st.write("**Image processed**")
            st.image(img, channels="RGB")
            '''
            btn = st.button("** Download image processed **")
            if btn:
                with open(os.path.join(img_file.name),"wb") as f:
                    f.write((img).getbuffer())
                    st.success("Image Downloaded")
            '''


                
                
