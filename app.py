import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

# Configure page
st.set_page_config(
    page_title="Class Scheduling Optimizer",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'data_manager' not in st.session_state:
    st.session_state.data_manager = DataManager()

def main():
    st.title("🎓 AI-Powered Class Scheduling Optimization System")
    st.markdown("### Optimize your institution's class schedules with intelligent algorithms")
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Welcome to the Class Scheduling Optimization System!**
        
        This application helps higher education institutions create optimized timetables by:
        - 📊 Managing complex scheduling constraints
        - 🧠 Using AI-powered optimization algorithms
        - 📈 Maximizing resource utilization
        - ⚡ Minimizing conflicts and overlaps
        - 📋 Generating comprehensive reports
        
        Navigate through the sidebar to:
        1. **Data Input**: Configure your institution's parameters
        2. **Schedule Generation**: Create optimized timetables
        3. **View Schedules**: Visualize generated schedules
        4. **Analytics**: Review optimization metrics and insights
        """)
    
    with col2:
        st.info("""
        **Quick Start:**
        1. Go to Data Input
        2. Configure your parameters
        3. Generate schedules
        4. Review and export results
        """)
    
    # System Status
    st.subheader("📋 System Status")
    
    # Check current data status
    data_status = st.session_state.data_manager.get_status()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if data_status['classrooms'] > 0:
            st.success(f"🏫 {data_status['classrooms']} Classrooms")
        else:
            st.warning("🏫 No Classrooms")
    
    with col2:
        if data_status['subjects'] > 0:
            st.success(f"📖 {data_status['subjects']} Subjects")
        else:
            st.warning("📖 No Subjects")
    
    with col3:
        if data_status['faculty'] > 0:
            st.success(f"👨‍🏫 {data_status['faculty']} Faculty")
        else:
            st.warning("👨‍🏫 No Faculty")
    
    with col4:
        if data_status['batches'] > 0:
            st.success(f"👥 {data_status['batches']} Batches")
        else:
            st.warning("👥 No Batches")
    
    # Recent Activity
    if hasattr(st.session_state, 'recent_schedule'):
        st.subheader("🔄 Recent Activity")
        st.info(f"Last schedule generated: {st.session_state.recent_schedule.get('timestamp', 'Unknown')}")
        
        if st.session_state.recent_schedule.get('conflicts', 0) == 0:
            st.success("✅ No conflicts detected in last generation")
        else:
            st.warning(f"⚠️ {st.session_state.recent_schedule.get('conflicts', 0)} conflicts detected")

if __name__ == "__main__":
    main()
