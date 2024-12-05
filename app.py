import streamlit as st

def main():
    st.set_page_config(
        page_title="靠北建築術科考試模擬",
        page_icon="👷",
        layout="wide"
    )

    # Custom CSS to remove Streamlit's default padding and make iframe full-width
    st.markdown("""
    <style>
    .reportview-container .main .block-container {
        padding-top: 0rem;
        padding-right: 0rem;
        padding-left: 0rem;
        padding-bottom: 0rem;
    }
    iframe {
        width: 100%;
        height: 100vh;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    # HTML content as a standalone game
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>靠北建築術科考試模擬</title>
        <style>
            body {
                font-family: 'Courier New', monospace;
                background-color: #1a1a1a;
                color: #fff;
                text-align: center;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            h1 {
                font-size: 28px;
                margin-top: 20px;
                color: #e74c3c;
                text-shadow: 2px 2px 0px #000;
            }
            p {
                font-size: 16px;
                color: #ccc;
                text-shadow: 1px 1px 0px #000;
            }
            #game-container {
                position: relative;
                width: 100%;
                max-width: 500px;
                height: 500px;
                margin: 20px auto;
                background-color: #333;
                border: 4px solid #e74c3c;
                display: flex;
                justify-content: center;
                align-items: center;
                box-shadow: 0px 0px 15px #e74c3c;
            }
            .table {
                width: 100%;
                height: 100%;
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                grid-template-rows: repeat(4, 1fr);
                gap: 5px;
            }
            .paper {
                perspective: 800px;
            }
            .paper-inner {
                position: relative;
                width: 100%;
                height: 100%;
                background-color: #4d4d4d;
                border-radius: 5px;
                border: 2px solid #666;
                transition: transform 0.6s;
                transform-style: preserve-3d;
                cursor: pointer;
            }
            .paper:hover .paper-inner {
                box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
            }
            .paper-front, .paper-back {
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                border-radius: 5px;
                text-align: center;
                line-height: 85px;
                font-size: 14px;
                font-weight: bold;
                color: #fff;
            }
            .paper-front {
                background-color: #4d4d4d;
            }
            .paper-back {
                transform: rotateY(180deg);
            }
            .pass .paper-back {
                background-color: #4caf50;
                color: #fff;
                text-shadow: 1px 1px 0px #000;
            }
            .fail .paper-back {
                background-color: #e74c3c;
                color: #fff;
                text-shadow: 1px 1px 0px #000;
            }
            #result {
                margin-top: 20px;
                font-size: 18px;
                color: #ccc;
                text-shadow: 1px 1px 0px #000;
            }
            .paper-flip {
                transform: rotateY(180deg);
            }
            #congrats {
                display: none;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background-color: rgba(0, 0, 0, 0.8);
                padding: 20px;
                border: 4px solid #4caf50;
                border-radius: 10px;
                color: #fff;
                font-size: 24px;
                text-align: center;
                z-index: 10;
                animation: fadeIn 0.5s ease;
            }
            #congrats span {
                display: block;
                margin-top: 10px;
                font-size: 18px;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes fadeOut {
                from { opacity: 1; }
                to { opacity: 0; }
            }
            @media (max-width: 600px) {
                #game-container {
                    width: 95%;
                    height: 95vw;
                    max-height: 500px;
                }
            }
        </style>
    </head>
    <body>
        <h1>靠北建築術科考試模擬</h1>
        <p>點擊爛爛的試卷，看看你有沒有辦法當上建築師！👷</p>
        <div id="game-container">
            <div class="table" id="table"></div>
            <div id="congrats">
                🎉 靠北，竟然及格了！🎉
                <span>你這麼幸運，不去買彩券可惜了！🤣</span>
            </div>
        </div>
        <div id="result"></div>

        <script>
            const table = document.getElementById('table');
            const result = document.getElementById('result');
            const congratsBox = document.getElementById('congrats');

            function initPapers() {
                table.innerHTML = '';
                result.innerHTML = '';
                congratsBox.style.display = 'none';

                for (let i = 0; i < 16; i++) {
                    const paper = document.createElement('div');
                    paper.classList.add('paper');

                    const paperInner = document.createElement('div');
                    paperInner.classList.add('paper-inner');

                    const paperFront = document.createElement('div');
                    paperFront.classList.add('paper-front');
                    paperFront.textContent = `試卷 ${i + 1}`;

                    const paperBack = document.createElement('div');
                    paperBack.classList.add('paper-back');

                    paperInner.appendChild(paperFront);
                    paperInner.appendChild(paperBack);
                    paper.appendChild(paperInner);

                    paper.addEventListener('click', () => {
                        const isPass = Math.random() < 0.1;

                        if (isPass) {
                            paper.classList.add('pass');
                            paperBack.textContent = '太扯！過了！';
                            result.innerHTML = `<span style="color: #4caf50; font-weight: bold;">🎉 恭喜！你的運氣比實力還好！🎉</span>`;
                            showCongrats();
                        } else {
                            paper.classList.add('fail');
                            paperBack.textContent = '不及格，爛爆！';
                            result.innerHTML = `<span style="color: #e74c3c; font-weight: bold;">💔 哈哈，還是好好念書吧！💔</span>`;
                        }

                        paperInner.classList.add('paper-flip');

                        setTimeout(() => {
                            paper.classList.remove('pass', 'fail');
                            paperInner.classList.remove('paper-flip');
                            paperBack.textContent = '';
                            result.innerHTML = '';
                        }, 1500);
                    });

                    table.appendChild(paper);
                }
            }

            function showCongrats() {
                congratsBox.style.display = 'block';
                setTimeout(() => {
                    congratsBox.style.animation = 'fadeOut 0.5s ease';
                    setTimeout(() => {
                        congratsBox.style.display = 'none';
                        congratsBox.style.animation = 'fadeIn 0.5s ease';
                    }, 500);
                }, 1500);
            }

            initPapers();
        </script>
    </body>
    </html>
    """

    # Render the HTML in an iframe
    st.components.v1.html(html_content, height=700, scrolling=False)

if __name__ == "__main__":
    main()