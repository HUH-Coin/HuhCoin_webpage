import streamlit as st
import base64

# Set page background
def set_background(png_file):
    with open(png_file, "rb") as file:
        bg_image = file.read()
    bg_image_encoded = base64.b64encode(bg_image).decode()
    background_style = f"""
    <style>
        .stApp {{
        background-image: url("data:image/png;base64,{bg_image_encoded}");
        background-size: cover;
        background-position: center;
        font-family: 'Georgia', serif;
    }}
    .center-title {{
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        font-weight: bold;
        color: #2C3E50;
        margin-top: 10px;
        gap: 10px;
    }}
    .center-title img {{
        width: 80px;  /* Adjust logo size */
        height: 80px;
    
    }}
    h1, h2, h3, h4 {{
        color: #2C3E50;
        text-align: left;
    }}
    .card {{
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }}
    .section-title {{
        font-size: 22px;
        font-weight: bold;
        color: #FF5733;
        margin-bottom: 10px;
    }}
    .section-content {{
        font-size: 16px;
        color: #2C3E50;
        line-height: 1.6;
    }}
    .center-title {{
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: black;
        margin-top: 10px;
    }}
    .center-subtitle {{
        text-align: center;
        font-size: 18px;
        color: #2C3E50;
        margin-top: -15px;
        margin-bottom: 20px;
    }}
    .nav-bar {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px 20px;
        border-radius: 10px;
        display: flex;
        justify-content: center;
        gap: 30px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }}
    .nav-item {{
        font-size: 16px;
        font-weight: bold;
        color: #2C3E50;
        cursor: pointer;
    }}
    .nav-item-selected {{
        color: #FF5733;
        border-bottom: 2px solid #FF5733;
    }}
    .stRadio {{
        display: flex;
        justify-content: center;
        gap: 20px;
        font-size: 24px;
        font-weight: bold;
        color: black;
        }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Set background image
set_background("huh-webpage.png")  # Adjust with the correct file path if needed

# Centered Title and Subtitle
st.markdown("""
<div class="center-title">
    <img src="data:image/png;base64,{}" alt="BRICS Logo">
    HUH Coin
</div>
""".format(base64.b64encode(open("huh_logo.png", "rb").read()).decode()), unsafe_allow_html=True)

# Navigation Buttons
selected_section = st.radio("", ["About HUH", "Tokenomics", "Roadmap"], horizontal=True)

# Apply style based on the selected section
nav_items = {
    "About HUH": "nav-item-selected" if selected_section == "About HUH" else "nav-item",
    "Tokenomics": "nav-item-selected" if selected_section == "Tokenomics" else "nav-item",
    "Roadmap": "nav-item-selected" if selected_section == "Roadmap" else "nav-item"
}

# Custom HTML for the Navigation Bar
st.markdown(f"""
<div class="nav-bar">
    <span class="{nav_items['About HUH']}">About HUH</span>
    <span class="{nav_items['Tokenomics']}">Tokenomics</span>
    <span class="{nav_items['Roadmap']}">Roadmap</span>
</div>
""", unsafe_allow_html=True)

# Display the selected section in a card
if selected_section == "About HUH":
    st.markdown("""
    <div class="card">
        <div class="section-title">About HUH</div>
        <div class="section-content">
            About HUH – The Ultimate Cat Meme Coin

Welcome to the world of HUH – the meme coin that’s all about attitude and a hint of mystery! Inspired by the iconic, unimpressed cat face that says “HUH” to the world, this coin is here to add some purr-fectly sassy fun to the crypto scene.

HUH isn't just another token; it’s a community-driven project with a mission to bring together meme lovers, cat enthusiasts, and crypto fans under one playful, paw-some banner. Just like our meme face, HUH is all about questioning the norms and going “HUH” at the status quo. Why follow the rules when you can create your own with HUH?

Why HUH?
Because who doesn’t love a cool cat? This isn’t just a coin – it’s a vibe, a movement, and a community. With HUH, you’re not just investing in crypto; you’re joining a club of like-minded people who get the joke, embrace the meme culture, and know how to have a good time.

So, if you’re ready to join the coolest club in crypto, say HUH? and dive into the world of the internet’s favorite meme cat coin!

Join us on social media, spread the HUH vibes, and let’s take over the crypto world – one purr at a time!
            So come aboard, grab a BRICS or a billion, and let’s show the world that emerging markets and meme coins are the combo we never knew we needed. Because, after all, if it’s got BRICS in the name, it’s gotta be solid, right?
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Tokenomics":
    st.markdown(f"""
    <div class="card">
        <div class="section-title">HUH Coin Tokenomics</div>
        <div class="section-content">
            <strong>Total Initial Supply</strong>: 1 Billion HUH Coins<br><br>
            <strong>Burned Supply</strong>:<br>
            - 90% Burned: 900 Million HUH Coins permanently removed from circulation.<br>
            - Remaining Circulating Supply: 10% HUH Coins.<br><br>
            <strong>Founder’s Allocation</strong>:<br>
            - 10% of Circulating Supply: HUH Coins reserved for the founder.<br><br>
            <strong>Transaction Fees</strong>:<br>
            - 2% Burn: Further reducing the circulating supply over time.<br>
            - 2% Redistribution: Rewarding existing holders.<br>
            - 1% Liquidity Pool: Added to the liquidity pool to help stabilize the price.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected_section == "Roadmap":
    st.markdown(f"""
    <div class="card">
        <div class="section-title">HUH Coin Roadmap</div>
        <div class="section-content">
            <strong>Phase 1: Concept & Community Building</strong><br>
            - Research & Development, Social Media Launch, Website Launch, Initial Airdrop.<br><br>
            <strong>Phase 2: Token Launch & Liquidity Setup</strong><br>
            - Token Creation, Listing on DEX, Establish Liquidity Pool, Community Incentives.<br><br>
            <strong>Phase 3: Marketing & Partnerships</strong><br>
            - Community Contests & Giveaways, Influencer Partnerships, Educational Content, Partnerships.<br><br>
            <strong>Phase 4: Utility Expansion</strong><br>
            - Exclusive Access & Rewards, NFT Integration, Voting & Governance, Charity Initiatives.<br><br>
            <strong>Phase 5: Global Expansion & Sustainability</strong><br>
            - Cross-Chain Expansion, Partnerships with Emerging Markets, Exchange Listings, Sustainability Initiatives.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div style="
    background-color: rgba(255, 255, 255, 0.8); 
    padding: 15px; 
    border-radius: 10px; 
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); 
    max-width: 300px;
    margin: 20px auto;
    text-align: center;
">
    <h3 style="color: #2C3E50; margin-top: 0;">Join the Community</h3>
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 10px;">
        <img src="https://img.icons8.com/color/48/000000/twitter.png" width="24"/>
        <a href="https://x.com/HUH_Coins" target="_blank" style="color: #1DA1F2; text-decoration: none; font-weight: bold;">Follow us on Twitter</a>
    </div>
    <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 10px;">
        <img src="https://img.icons8.com/color/48/000000/telegram-app.png" width="24"/>
        <a href="https://t.me/+-DqDMavr6E1iMzY1" target="_blank" style="color: #0088cc; text-decoration: none; font-weight: bold;">Join our Telegram</a>
    </div>
</div>
""", unsafe_allow_html=True)
