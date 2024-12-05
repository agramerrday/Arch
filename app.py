import streamlit as st
import random

def init_papers():
    """Initialize the game state with 16 papers."""
    if 'papers' not in st.session_state:
        st.session_state.papers = [
            {'revealed': False, 'result': None} for _ in range(16)
        ]

def reset_game():
    """Reset the game to its initial state."""
    st.session_state.papers = [
        {'revealed': False, 'result': None} for _ in range(16)
    ]

def main():
    st.set_page_config(
        page_title="靠北建築術科考試模擬",
        page_icon="👷",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for consistent sizing and cross-platform compatibility
    st.markdown("""
    <style>
    /* Reset Streamlit default styles */
    .stApp {
        background-color: #1a1a1a !important;
        color: white !important;
        font-family: 'Courier New', monospace, sans-serif !important;
    }
    
    /* Consistent title styling */
    h1 {
        color: #e74c3c !important;
        text-align: center !important;
        margin-bottom: 20px !important;
    }
    
    /* Paper grid layout */
    .paper-grid {
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 10px !important;
        max-width: 600px !important;
        margin: 0 auto !important;
    }
    
    /* Consistent paper container */
    .paper-container {
        height: 100px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        padding: 0 !important;
    }
    
    /* Paper button styling */
    .stButton > button {
        background-color: #4d4d4d !important;
        color: white !important;
        border: 2px solid #666 !important;
        border-radius: 10px !important;
        height: 100px !important;
        width: 100% !important;
        font-family: 'Courier New', monospace, sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: none !important;
    }
    
    .stButton > button:hover {
        background-color: #5d5d5d !important;
        transform: scale(1.05) !important;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.2) !important;
    }
    
    /* Revealed paper styles */
    .revealed-paper {
        background-color: #4d4d4d !important;
        color: white !important;
        border: 2px solid #666 !important;
        border-radius: 10px !important;
        height: 100px !important;
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        font-family: 'Courier New', monospace, sans-serif !important;
    }
    
    .pass-paper {
        background-color: #4caf50 !important;
        border: 2px solid #45a049 !important;
    }
    
    .fail-paper {
        background-color: #e74c3c !important;
        border: 2px solid #c0392b !important;
    }
    
    /* Responsive text sizing */
    @media (max-width: 600px) {
        .paper-container, .stButton > button, .revealed-paper {
            height: 80px !important;
            font-size: 0.8rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize game
    init_papers()

    # Title and description
    st.markdown("<h1>靠北建築術科考試模擬</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ccc;'>點擊爛爛的試卷，看看你有沒有辦法當上建築師！👷</p>", unsafe_allow_html=True)

    # Create a container for the grid
    grid_container = st.container()
    
    with grid_container:
        # Use custom grid layout
        st.markdown('<div class="paper-grid">', unsafe_allow_html=True)
        
        # Columns for grid layout
        cols = st.columns(4)
        
        # Track if game is won
        game_won = False

        # Render papers
        for row in range(4):
            for col in range(4):
                paper_index = row * 4 + col
                with cols[col]:
                    # Wrap content in a consistent container
                    st.markdown('<div class="paper-container">', unsafe_allow_html=True)
                    
                    # Check if paper is already revealed
                    if st.session_state.papers[paper_index]['revealed']:
                        # Show revealed paper
                        result = st.session_state.papers[paper_index]['result']
                        if result:
                            st.markdown(f'<div class="revealed-paper pass-paper">太扯！過了！</div>', unsafe_allow_html=True)
                            game_won = True
                        else:
                            st.markdown(f'<div class="revealed-paper fail-paper">不及格，爛爆！</div>', unsafe_allow_html=True)
                    else:
                        # Clickable paper
                        if st.button(f"試卷 {paper_index + 1}", key=f"paper_{paper_index}"):
                            # Determine result (10% chance of passing)
                            result = random.random() < 0.1
                            
                            # Update paper state
                            st.session_state.papers[paper_index]['revealed'] = True
                            st.session_state.papers[paper_index]['result'] = result
                            
                            # Rerun to update display
                            st.experimental_rerun()
                    
                    # Close paper container
                    st.markdown('</div>', unsafe_allow_html=True)

        # Close grid container
        st.markdown('</div>', unsafe_allow_html=True)

    # Display result
    if any(paper['revealed'] for paper in st.session_state.papers):
        last_revealed_paper = next(
            paper for paper in reversed(st.session_state.papers) if paper['revealed']
        )
        
        if last_revealed_paper['result']:
            st.success("🎉 恭喜！你的運氣比實力還好！🎉")
        else:
            st.error("💔 哈哈，還是好好念書吧！💔")

    # Reset button
    if st.button("重新開始"):
        reset_game()

if __name__ == "__main__":
    main()