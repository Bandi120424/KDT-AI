import streamlit as st
import figs.age_fig as age_fig 
import data as df

insurance_data = df.df_insure_data() 


def age():
    st.markdown("## Age")
    st.markdown("---")
    
    st.markdown(f"""
                In this part, we will observe the correlation between age and medical cost. 
                First of all, let's check the minimum & maximum age of a person in this data.
                
                - Minimum age: {insurance_data['age'].min()}
                - Maximum age: {insurance_data['age'].max()}
                """)
    
    col1, col2 = st.columns(2)
    with col1: 
        st.plotly_chart(age_fig.age_distribution_fig)
    with col2:
        st.plotly_chart(age_fig.group_avg_bar_fig)
     
    st.markdown(f""" 
                    It seems that each age group has a similar size except teenagers and people of age over 60 (let's say elder group).   
                    We can see that the elder group has the highest average medical cost (which is quite reasonable).
                    In addition, the average medical cost tends to increase with age. 
                """)
    
    st.markdown("---")

    st.markdown(f""" 
                    According to the statistics in department of labor logo united states department of labor, northeast region has the 
                    highest weekly wage, the second is southwest, the third is southeast and the last is northwest region. 
                    
                    So, it is worthy to check the medical in each region. In this data, we divide the data into 4 region groups: southwest, southeast, 
                    northwest, northeast.  
                """)
    
    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(age_fig.SW_charge_age_fig)
    with col4:
        st.plotly_chart(age_fig.SE_charge_age_fig)    
            
    col5, col6 = st.columns(2)
    with col5:
        st.plotly_chart(age_fig.NW_charge_age_fig)
    with col6:
        st.plotly_chart(age_fig.NE_charge_age_fig)    
        
    st.markdown(f""" 
                    All regions have the same pattern as we saw earlier. It is likely to spend more money on medical services as we are getting older.  
                    Aside from that, we also find that:
                    - the southwest group is the only group that there is no one spending more than 60k dollars (however, elder group in this region seems to spend more cost that other regions)
                    - there are young people (in their 30s) who spend more that 50k dollars in northwest and northeast region
                    - the pattern in southeast region is in linear than other regions 
                """)
    
    col7, col8 = st.columns(2)
    with col7:
        st.plotly_chart(age_fig.SW_charge_age_fig)
    with col8:
        st.plotly_chart(age_fig.SE_charge_age_fig)    
    
    col9, col10 = st.columns(2)   
    with col9:
        st.plotly_chart(age_fig.NW_charge_age_fig)
    with col10:
        st.plotly_chart(age_fig.NE_charge_age_fig)  
    
    st.markdown("---")
    
    st.markdown(f""" 
                    The gender is also an important factor. 
                """)
    
    col11, col12 = st.columns(2)
    with col11:
        st.plotly_chart(age_fig.SW_charge_age_fig_MF)
    with col12:
        st.plotly_chart(age_fig.SE_charge_age_fig_MF)    
    
    col13, col14 = st.columns(2)   
    with col13:
        st.plotly_chart(age_fig.NW_charge_age_fig_MF)
    with col14:
        st.plotly_chart(age_fig.NE_charge_age_fig_MF)  
        
    st.markdown(f""" 
                    It seems that there is no huge difference caused by gender. Let's see the average medical cost in each gender group.  
                """)

    st.markdown("---")
    
    #bar_Chart 
    st.markdown(f""" 
                    Additionally, we can check the number of children of each age group. 
                """)

    col15, col16 = st.columns(2)
    with col15:
        st.plotly_chart(age_fig.SW_charge_age_bar_fig_MF)
    with col16:
        st.plotly_chart(age_fig.SE_charge_age_bar_fig_MF)
            
    col17, col18 = st.columns(2)
    with col17:
        st.plotly_chart(age_fig.NW_charge_age_bar_fig_MF)
    with col18:
        st.plotly_chart(age_fig.NE_charge_age_bar_fig_MF)
        
    st.markdown(f""" 
                    In all regions, people in their 30s or 40s have more children than any other age group. 
                    If we compare north and south, south region has more children in average. 
                    However, the average number of children in all age group and regions is less than two.  
                """)
