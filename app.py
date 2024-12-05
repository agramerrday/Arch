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
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for styling
    st.markdown("""
    <style>
    .stApp {
        background-color: #1a1a1a;
        color: white;
        font-family: 'Courier New', monospace;
    }
    .title {
        color: #e74c3c;
        text-align: center;
    }
    .paper {
        background-color: #4d4d4d;
        border: 2px solid #666;
        border-radius: 10px;
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .paper:hover {
        transform: scale(1.05);
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }
    .pass {
        background-color: #4caf50;
        color: white;
    }
    .fail {
        background-color: #e74c3c;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Initialize game
    init_papers()

    # Title and description
    st.markdown("<h1 class='title'>靠北建築術科考試模擬</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #ccc;'>點擊爛爛的試卷，看看你有沒有辦法當上建築師！👷</p>", unsafe_allow_html=True)

    # Create a grid of papers
    cols = st.columns(4)
    
    # Track if game is won
    game_won = False

    # Render papers
    for row in range(4):
        for col in range(4):
            paper_index = row * 4 + col
            with cols[col]:
                # Check if paper is already revealed
                if st.session_state.papers[paper_index]['revealed']:
                    # Show revealed paper
                    result = st.session_state.papers[paper_index]['result']
                    if result:
                        st.markdown(f"<div class='paper pass'>太扯！過了！</div>", unsafe_allow_html=True)
                        game_won = True
                    else:
                        st.markdown(f"<div class='paper fail'>不及格，爛爆！</div>", unsafe_allow_html=True)
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