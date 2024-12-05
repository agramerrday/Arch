import streamlit as st
import random

def main():
    st.set_page_config(page_title="建築師考試術科考試模擬", page_icon="🏛️")

    # Custom CSS for styling
    st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
        color: #fff;
    }
    h1 {
        color: #4caf50 !important;
        text-shadow: 2px 2px 0px #000;
        text-align: center;
    }
    .paper {
        background-color: #4d4d4d;
        border: 2px solid #666;
        border-radius: 5px;
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: all 0.2s ease;
        color: #fff;
        text-shadow: 1px 1px 0px #000;
    }
    .paper:hover {
        background-color: #5d5d5d;
        transform: scale(1.05);
    }
    .pass {
        background-color: #4caf50 !important;
        border-color: #2e7d32 !important;
    }
    .fail {
        background-color: #e74c3c !important;
        border-color: #c0392b !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and instructions
    st.markdown("<h1>建築師考試術科考試模擬</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ccc;'>點擊任一試卷來查看你是否通過術科考試！</p>", unsafe_allow_html=True)

    # Initialize session state for papers if not already exists
    if 'papers' not in st.session_state:
        st.session_state.papers = [{'text': f'試卷 {i+1}', 'passed': None} for i in range(16)]
        st.session_state.result = ''

    # Create a grid of papers
    cols = st.columns(4)
    for row in range(4):
        for col in range(4):
            idx = row * 4 + col
            paper = st.session_state.papers[idx]
            
            with cols[col]:
                # Determine button style and text based on paper state
                if paper['passed'] is None:
                    button_style = 'paper'
                    button_text = paper['text']
                elif paper['passed']:
                    button_style = 'paper pass'
                    button_text = '通過'
                else:
                    button_style = 'paper fail'
                    button_text = '未通過'
                
                # Create button with custom styling
                button = st.button(
                    button_text, 
                    key=f'paper_{idx}', 
                    disabled=paper['passed'] is not None,
                    use_container_width=True,
                    type='secondary'
                )
                
                # Handle button click
                if button and paper['passed'] is None:
                    # 10% chance of passing
                    is_pass = random.random() < 0.1
                    st.session_state.papers[idx]['passed'] = is_pass
                    
                    # Set result message
                    if is_pass:
                        st.session_state.result = '恭喜！你通過了術科考試！🎉'
                    else:
                        st.session_state.result = '很遺憾，你未通過術科考試。'
    
    # Display result
    if st.session_state.result:
        st.markdown(f"<div style='text-align: center; margin-top: 20px; color: {'#4caf50' if '恭喜' in st.session_state.result else '#e74c3c'}; font-weight: bold;'>{st.session_state.result}</div>", unsafe_allow_html=True)
    
    # Reset button
    if st.button('重新開始'):
        st.session_state.papers = [{'text': f'試卷 {i+1}', 'passed': None} for i in range(16)]
        st.session_state.result = ''
        st.experimental_rerun()

if __name__ == "__main__":
    main()