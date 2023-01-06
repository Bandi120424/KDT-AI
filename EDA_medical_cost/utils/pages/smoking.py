import streamlit as st
import figs.smoker_fig as smoker_fig
import data as df

def smoking():
    st.markdown("## Smoking")
    st.markdown("---")
    
    st.markdown(f"""
                In this part, we will observe the correlation between smoking and medical cost. 
                First, the distribution of charges for smokers/non-smokers is as follows.
                """)
    
    st.pyplot(smoker_fig.smoker_hist_fig)
    
    st.markdown(f"""
                We can see that non-smoker group is much bigger than smoker group.
                Moreover, it is expected that smoker group spends more medical cost. 
                """)

    st.pyplot(smoker_fig.smoker_box_fig)
    
    st.markdown(f""" 
                Again, we can say that the smoking group pay more medical bills that the non-smoking group.                 
                """)
    
    st.markdown("---")
    st.markdown(f"""
                 The age is important when we divide smoking/non-smoking group.
                 We can check that in the graph below. 
                """)    

    st.pyplot(smoker_fig.smoker_age_count_fig)
    
    st.markdown(f"""
                Unfortunately, there are teenager smokers but they are few. 
                In current data, the minimum age is 18 so they are 18 years old. 
                On the other hand, there are many smokers in adult group.
                """)
    
    st.markdown(f"""
                Let's compare the cost between two groups: 18 years old smokers and adult smokers of age over 60. 
                """)
    
    st.pyplot(smoker_fig.minor_smoker_box_fig)
    
    st.markdown(f"""
                The 18 years old smokers definitely spend more cost than non-smokers adult group.
                
                The adult smokers often quit smoking when they have a child.
                So it is worthy to see the number of children for smokers and non-smokers.
                """)
    
    st.pyplot(smoker_fig.smoker_child_fig)
        
    st.markdown(f""" 
                We can see that there are fewer people in smoking group with children.
                """)    
    
    st.markdown("---")
    
    st.markdown("From now on, we see the smoking ratio in each region.")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(smoker_fig.SW_sunburst_fig)
    with col2:
        st.plotly_chart(smoker_fig.SE_sunburst_fig)

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(smoker_fig.NW_sunburst_fig)
    with col4:
        st.plotly_chart(smoker_fig.NE_sunburst_fig)
            
    st.markdown(f"""
                We can see that south region has the higher smoking ratio.
                Moreover, the graph below shows that the smokers usually pay the higher medical cost regardless of region. 
                """)
    col5, col6 = st.columns(2)
    with col5:
        st.plotly_chart(smoker_fig.SW_charge_age_fig_SM)
    with col6:
        st.plotly_chart(smoker_fig.SE_charge_age_fig_SM)    

    col7, col8 = st.columns(2)
    with col7:
        st.plotly_chart(smoker_fig.NW_charge_age_fig_SM)
    with col8:
        st.plotly_chart(smoker_fig.NE_charge_age_fig_SM)


    st.markdown(f"""
                Let's focus on the smoker group.
                The following charts show the average charge and BMI for each age and region.
                """)    
    col9, col10 = st.columns(2)
    with col9:
        st.plotly_chart(smoker_fig.SW_charge_age_bar_fig_smo)
    with col10:
        st.plotly_chart(smoker_fig.SE_charge_age_bar_fig_smo)

    col11, col12 = st.columns(2)
    with col11:
        st.plotly_chart(smoker_fig.NW_charge_age_bar_fig_smo)
    with col12:
        st.plotly_chart(smoker_fig.NE_charge_age_bar_fig_smo)
        
