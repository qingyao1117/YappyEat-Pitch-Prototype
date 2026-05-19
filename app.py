import streamlit as st
import requests

# 1. PAGE INITIALIZATION & PALETTE INJECTION
st.set_page_config(page_title="YappyEat", page_icon="🌸", layout="centered")

# Custom CSS to match the pastel, rounded UI theme from your Figma screens
st.markdown("""
    <style>
    /* Main Layout Aesthetics */
    .stApp {
        background-color: #FFF9F6;
    }
    h1, h2, h3 {
        color: #3E2723 !important;
        font-family: 'Sofia Pro', 'Inter', sans-serif;
    }
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 8px 20px;
        color: #795548;
        border: 1px solid #FFE0D3;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FF8A80 !important;
        color: white !important;
        font-weight: bold;
    }
    /* Card Container Styling */
    .recipe-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 24px;
        box-shadow: 0px 8px 16px rgba(255, 138, 128, 0.05);
        border: 1px solid #FFF0EB;
        margin-bottom: 15px;
    }
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: bold;
        margin-right: 5px;
    }
    .badge-top { background-color: #FFF9C4; color: #F57F17; }
    .badge-easy { background-color: #E8F5E9; color: #2E7D32; }
    </style>
""", unsafe_allow_html=True)

# Top Bar Header Profile Mock
st.markdown("""
    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;'>
        <div>
            <p style='color: #8D6E63; margin: 0;'>Good morning! 🌸</p>
            <h1 style='margin: 0; font-size: 28px;'>What's cooking, Mia?</h1>
        </div>
        <div style='text-align: right;'>
            <span style='background-color: #FFEBEE; color: #C62828; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;'>⚠️ 2 Allergies Saved</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 2. NAVIGATION BOTTOM-BAR CORRESPONDENCE VIA TABS
tab_home, tab_cook, tab_occasions, tab_community, tab_shop, tab_me = st.tabs([
    "🏠 Home", "🔍 Cook (Scan)", "✨ Occasions", "👥 Community", "🛍️ Shop", "👤 Me"
])

# ============================================================
# TAB 1: HOME PAGE
# ============================================================
with tab_home:
    st.markdown("### ✨ AI Picks For You")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class='recipe-card'>
                <span class='badge badge-top'>⭐ Top Match</span>
                <h4>Egg Fried Rice</h4>
                <p style='color: #757575; font-size: 14px;'>🤖 AI Optimized Matching</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Egg Fried Rice Recipe", key="home_r1"):
            st.info("💡 Tip: Navigate to the 'Cook' tab to simulate your real-time cloud calculations!")
            
    with col2:
        st.markdown("""
            <div class='recipe-card'>
                <span class='badge badge-easy'>🌿 Easy</span>
                <h4>Pasta Primavera</h4>
                <p style='color: #757575; font-size: 14px;'>🤖 AI Recommended</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🔥 Trending Now")
    st.markdown("""
        <div class='recipe-card'>
            <strong>🥑 Avocado Toast Supreme</strong><br>
            <span style='color: #757575; font-size: 13px;'>⏱️ 12 min | 🔥 380 kcal | ⭐ 4.9 Rating</span>
        </div>
        <div class='recipe-card'>
            <strong>🥞 Fluffy Pancakes</strong><br>
            <span style='color: #757575; font-size: 13px;'>⏱️ 20 min | 🔥 480 kcal | ⭐ 4.9 Rating</span>
        </div>
    """, unsafe_allow_html=True)

# ============================================================
# TAB 2: COOK / AI INGREDIENT SCANNER (Feature A)
# ============================================================
with tab_cook:
    st.markdown("### 🧺 Your Kitchen Pantry")
    st.write("Simulate scanning or selecting left-over fresh produce to compute recipes via Gemini.")
    
    # Mirroring the inventory list tokens directly from your image
    st.markdown("**Active Scanned Ingredients Matrix:**")
    st.markdown("""
        <span style='background: #FFEBEE; color: #D32F2F; padding: 6px 14px; border-radius: 20px; margin-right: 5px; font-weight: 500;'>Eggs ❌</span>
        <span style='background: #FFF3E0; color: #F57C00; padding: 6px 14px; border-radius: 20px; margin-right: 5px; font-weight: 500;'>Avocado ❌</span>
        <span style='background: #E8F5E9; color: #388E3C; padding: 6px 14px; border-radius: 20px; margin-right: 5px; font-weight: 500;'>Tomato ❌</span>
        <span style='background: #F3E5F5; color: #7B1FA2; padding: 6px 14px; border-radius: 20px; margin-right: 5px; font-weight: 500;'>Cheese ❌</span>
    """, unsafe_allow_html=True)
    st.write("")
    
    # Simulates camera ingestion array selection
    quick_add_items = st.multiselect(
        "Simulate adding more items detected by your camera hardware module:",
        ["Broccoli", "Carrot", "Ginger", "Pasta", "Chicken", "Onion", "Garlic", "Rice"],
        default=["Broccoli", "Carrot"]
    )
    
    # Combined target string payload calculation
    base_ingredients = ["Eggs", "Avocado", "Tomato", "Cheese"]
    final_query_list = base_ingredients + quick_add_items
    
    st.write("---")
    if st.button("🚀 Formulate AI Recipe Matches (Run Live Backend)", type="primary"):
        with st.spinner("Executing structural vector mapping inside your cloud gateway..."):
            try:
                # Triggers data fetch from your running Uvicorn server context
                backend_url = "http://127.0.0.1:8000/api/v1/recipes/match"
                payload = {"detected_ingredients": final_query_list, "user_id": "Mia_Johnson_5"}
                
                response = requests.post(backend_url, json=payload)
                if response.status_code == 200:
                    api_data = response.json()
                    st.success("✨ Optimal Cooking Blueprint Found!")
                    
                    # Renders macro metric indicators directly from your UI screen layout styling
                    c1, c2, c3, c4 = st.columns(4)
                    c1.metric("Calories", "380 kcal")
                    c2.metric("Protein", "18g")
                    c3.metric("Carbs", "32g")
                    c4.metric("Fat", "22g")
                    
                    st.markdown("### 📖 Step-by-Step Culinary Instructions")
                    st.markdown(api_data["data"])
                else:
                    st.error("Model mapping failed. Verify error configuration.")
            except Exception as e:
                st.error(f"Cannot reach your running server instance. Ensure your black Uvicorn window is up! {e}")

# ============================================================
# TAB 3: OCCASION PLANNER (Feature B)
# ============================================================
with tab_occasions:
    st.markdown("### 📅 AI Occasion & Dining Router")
    st.write("Select the target event atmosphere directly mapped out on your layout proposal tabs.")
    
    selected_vibe = st.radio(
        "Choose Atmosphere Context:",
        ["Birthday", "Picnic", "Dinner Party", "Date Night", "Family Gathering"],
        horizontal=True
    )
    
    if st.button("Generate Event Gastronomy Concepts"):
        with st.spinner("Drafting curated theme menu options..."):
            try:
                backend_url = "http://127.0.0.1:8000/api/v1/recipes/occasion-planner"
                payload = {"vibe": selected_vibe, "dietary_restrictions": ["Halal", "Almond Allergy"]}
                
                response = requests.post(backend_url, json=payload)
                if response.status_code == 200:
                    st.success(f"Curated '{selected_vibe}' Recipe Ideas Generated Successfully!")
                    st.markdown(response.json()["data"])
            except Exception as e:
                st.error(f"Connection failed: {e}")

# ============================================================
# TAB 4: COMMUNITY BOARD (Feature C)
# ============================================================
with tab_community:
    st.markdown("### 👥 Community Feed")
    st.markdown("""
        <div class='recipe-card'>
            <strong>👤 Sophia Chen</strong> <span style='color: #BDBDBD;'>• @sophiaeats • 2h ago</span><br><br>
            <p>Made these fluffy pancakes from leftover berries and oat milk 🥞 honestly better than the café version!!</p>
            <span style='color: #FF8A80;'>❤️ 247 Likes | 💬 31 Comments</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("✍️ Share Your Leftover Creation")
    dish = st.text_input("What did you cook?", "Zero-Waste Veggie Soup")
    caption = st.text_area("Write a caption:", "Saved some celery and carrots from going bad!")
    
    if st.button("Publish to YappyEat Feed"):
        try:
            backend_url = "http://127.0.0.1:8000/api/v1/community/share"
            payload = {
                "user_id": "Mia123", "username": "miaeats", 
                "dish_name": dish, "caption": caption, "image_url": "mock_url"
            }
            res = requests.post(backend_url, json=payload)
            if res.status_code == 200:
                st.success(res.json()["message"])
        except Exception as e:
            st.error(f"Link broken: {e}")

# ============================================================
# TAB 5: MARKETPLACE (Feature D)
# ============================================================
with tab_shop:
    st.markdown("### 🛍️ Neighbor Food Market")
    st.write("Purchase homemade surplus products created by micro-cooks right around your campus neighborhood.")
    
    market_tab = st.radio("Filter Listings By:", ["All", "Pastries", "Meals", "Healthy", "Desserts"], horizontal=True)
    
    try:
        backend_url = f"http://127.0.0.1:8000/api/v1/marketplace/items?category={market_tab}"
        response = requests.get(backend_url)
        if response.status_code == 200:
            items = response.json()["items"]
            
            for item in items:
                st.markdown(f"""
                    <div class='recipe-card'>
                        <div style='display: flex; justify-content: space-between;'>
                            <h4>🍳 {item['name']}</h4>
                            <span style='color: #E91E63; font-weight: bold; font-size: 18px;'>RM {item['price']:.2f}</span>
                        </div>
                        <p style='margin: 0; color: #757575;'>🧑‍🍳 Cook: {item['seller']} | Tag: <code>{item['category']}</code></p>
                    </div>
                """, unsafe_allow_html=True)
                st.button("Add to Cart", key=f"shop_{item['id']}")
    except Exception as e:
        st.error(f"Failed to extract mock database rows: {e}")

# ============================================================
# TAB 6: USER PROFILE
# ============================================================
with tab_me:
    st.markdown("### 👤 User Profile Dashboard")
    
    # Injects the badge gamification layout variables directly from your final image asset
    st.markdown("""
        <div class='recipe-card' style='text-align: center; background: linear-gradient(135deg, #FF9E80 0%, #FF8A80 100%); color: white;'>
            <h2 style='color: white !important;'>Mia Johnson</h2>
            <p style='margin: 0;'>🥇 Level 5 Chef | 🌾 Sustainable Eco-Cook</p>
        </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Recipes", "48")
    c2.metric("Posts", "23")
    c3.metric("Followers", "1.2k")
    c4.metric("Following", "89")
    
    st.markdown("#### 🏅 Earned Gamification Badges")
    st.markdown("""
        - 🏅 **First Recipe:** Awarded for completing initial system integration.
        - 🔥 **7-Day Streak:** Maintained household resource tracking for a week straight.
        - 🌱 **Eco Cook Badge:** Reduced waste tracking metrics by over 15% this month!
    """)
