import streamlit as st
import figs.bmi_fig as bmi_fig 
import data as df


def bmi():
    st.markdown("## BMI")
    st.markdown("---")
    
    st.markdown(f"""
                In this part, we will observe the correlation between BMI and medical cost. 
                First of all, let's check the criterion for dividing each BMI group.
                """)
    st.table(bmi_fig.criterion)
    
    st.markdown("---")
    
    st.markdown(f"""
                The graph below shows the distribution of BMI in total data. 
                Interestingly, it looks like many people are in overweight or obesity group.
                We also check it in numbers! 
                """)
        
    st.pyplot(bmi_fig.bmi_dis_fig)
    st.table(bmi_fig.bmi_ratio)
    
    st.markdown(f"""
                It is natural to think that the obesity group spends more cost than any other group. 
                Let's find out by checking average charges in each group.
                """)
    
    st.plotly_chart(bmi_fig.bmi_group_avg_bar_fig)
    
    st.markdown(f"""
                As we expected, the obesity group actually spends more cost than any other group in average. 
                Additionally, the graph below shows the average charges per each BMI level. 
                We can see that people spend more cost as BMI level increases.
                """)
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(bmi_fig.bmi_low_data_avg_bar_fig)
    with col2:
        st.plotly_chart(bmi_fig.bmi_nor_data_avg_bar_fig)

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(bmi_fig.bmi_over_data_avg_bar_fig)
    with col4:
        st.plotly_chart(bmi_fig.bmi_obe_data_avg_bar_fig)
        
    st.markdown("---")
    
    st.markdown(f"""
                Take a closer look at the obesity group and overweight group. 
                """)
    
    st.pyplot(bmi_fig.bmi_obe_overweight_fig)
        
    
