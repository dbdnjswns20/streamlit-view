import streamlit as st
from PIL import Image

if "page" not in st.session_state:
    st.session_state.page = "upload"  # 초기 페이지는 업로드 페이지로 설정
if "selected_allergy" not in st.session_state:
    st.session_state.selected_allergy = []  # 알레르기 선택 정보를 세션 상태에 저장

# 페이지 전환 함수
def go_to_next_page():
    st.session_state.page = "next"  # 다음 페이지로 전환

# 업로드 페이지
if st.session_state.page == "upload":
    st.write('# Upload Photo')

    # 알레르기 선택 박스
    st.header("Allergy Selection")
    allergies = ["No", "Egg", "Beef", "Pork", "Chicken", "Shrimp", "Crab", "Squid", "Mackerel", "Shellfish", "Peanut", "Walnut", "Pine nut", "Soybean", "Milk", "Peach", "Tomato", "Wheat", "Buckwheat", "Almond", "Hazelnut", "Sulfurous acid", "Acorn"]
    selected_allergy = st.multiselect("Please select the appropriate allergy", allergies)

    if selected_allergy:
        st.write(f"Selected Allergy: {', '.join(selected_allergy)}")
    else:
        st.write("No allergies selected.")

    st.session_state.selected_allergy = selected_allergy

    # 종교 선택 박스
    st.header("Religion Selection")
    religions = ["No", "Christianity", "Buddhism", "Islam", "Hinduism", "Judaism", "Other"]
    selected_religion = st.selectbox("Please select the appropriate religion", religions)

    if selected_religion != "No":
        st.write(f"Selected Religion: {selected_religion}")
    else:
        st.write("No religion selected.")

    # 이미지 업로드 칸 생성
    uploaded_file = st.file_uploader("please upload the picture", type=["jpg", "jpeg", "png"])

    # 업로드된 파일이 있는 경우 표시
    if uploaded_file is not None:
        # PIL을 사용하여 이미지 열기
        image = Image.open(uploaded_file)
        st.image(image, caption="uploaded image", use_column_width=True)
        st.write("Image upload was successful!")

        # 다음 페이지로 넘어가기 위한 버튼 생성
        if st.button("Go to Next Page"):
            go_to_next_page()

elif st.session_state.page == "next":
    # 알레르기 유발 성분 리스트와 키워드
    allergen_keywords = {
        "Egg": ["egg"],
        "Beef": ["beef"],
        "Pork": ["pork"],
        "Chicken": ["chicken"],
        "Shrimp": ["shrimp"],
        "Crab": ["crab"],
        "Squid": ["squid"],
        "Mackerel": ["mackerel"],
        "Shellfish": ["clam", "shellfish", "mussel"],
        "Peanut": ["peanut"],
        "Walnut": ["walnut"],
        "Pine nut": ["pine nut"],
        "Soybean": ["soy", "soybean"],
        "Milk": ["milk", "dairy"],
        "Peach": ["peach"],
        "Tomato": ["tomato"],
        "Wheat": ["wheat"],
        "Buckwheat": ["buckwheat"],
        "Almond": ["almond"],
        "Hazelnut": ["hazelnut"],
        "Sulfurous acid": ["sulfurous acid"],
        "Acorn": ["acorn", "acorn jelly"]
    }

    # 메뉴 데이터
    menu_data = {
        "bibimbap": {
            "description": "A mixed rice bowl topped with various vegetables, meat, and an egg, often served with spicy gochujang sauce.",
            "ingredients": ["short-grain Rice", "carrot", "red bell pepper", "zucchini", "English cucumber", "green onion", "lean cut of beef(fillet mignon, flank steak)", "dried bellflower roots(doraji)", "fernbrake(gosari)", "vegetable oil", "salt", "toasted sesame seeds", "garlic", "soy sauce", "honey(or sugar)", "Korean hot pepper paste(gochujang)", "Egg"],
            "youtube_url": "https://youtu.be/6QQ67F8y2b8"
        },
        "bulgogi": {
            "description": "Bulgogi is a Korean dish made from marinated beef grilled on a barbecue.",
            "ingredients": ["Beef(tenderloin, top sirloin, or skirt steak)", "Garlic cloves", "Green onion", "Soy sauce", "Water", "Sugar", "Toasted sesame oil", "Toasted sesame seeds", "Ground black pepper"],
            "youtube_url": "https://youtu.be/3qBjL_HGvco"
        },
        "godeungeo-gui": {
            "description": "Godeungeo-gui is grilled mackerel. This salty mackerel side dish is one of the most common fish dishes in Korea. Mackerel is known as a fish that is a great source of nutrients such as good fat (omega 3 fatty acids), protein, vitamins, and minerals!",
            "ingredients": ["Mackerel", "Salt", "Vegetable oil", "Flour", "Lemon"],
            "youtube_url": "https://youtu.be/ZMYtYwjLQCE"
        },
        "jjamppong": {
            "description": "Jjamppong is a spicy noodle soup full of seafood, meat, and vegetables. It’s made with various ingredients, creating a hearty meal. Developed by Chinese immigrants in Incheon, Korea, and adapted to Korean tastes.",
            "ingredients": ["Dried anchovies", "Dried kelp", "Water", "Green onion", "leek", "Bok choy", "Onion", "Carrot", "Mussels", "Shrimp", "Squid", "Clams", "Beef or Pork or Chicken", "Noodles", "Korean hot pepper flakes(gochugaru)", "Toasted sesame oil", "Garlic", "Ginger", "Vegetable oil", "Fish sauce", "Salt"],
            "youtube_url": "https://youtu.be/7txoB9qnKWs"
        },
        "ramyeon": {
            "description": "Ramyeon is the Korean version of instant Japanese ramen. A package of ramyeon comes with instructions, but adding simple fresh ingredients can enhance the flavor.",
            "ingredients": ["Korean ramyeon", "Water", "Egg", "Green onion"],
            "youtube_url": "https://youtu.be/zCy8X9H3TEs"
        },
        "yangnyeom_chicken": {
            "description": "Spicy Fried Chicken is called yangnyeom chicken in Korean. Yangnyeom means seasoned, and tongdak means a whole chicken. This dish features crispy fried chicken coated in a spicy, sweet sauce.",
            "ingredients": ["Chicken", "Salt", "Ground black pepper", "Potato starch", "Flour", "Baking soda", "Eggs", "Toasted sesame seeds", "Vegetable oil", "Garlic cloves", "Ketchup", "Rice syrup", "Korean hot pepper paste(gochujang)", "White vinegar", "Corn or vegetable oil for frying"],
            "youtube_url": "https://youtu.be/XnLWBoZn710"
        },
        "doenjang_jjigae": {
            "description": "Doenjang-jjigae is a traditional Korean soybean paste stew with tofu, vegetables, and sometimes meat.",
            "ingredients": ["Fermented soybean paste(doenjang)", "Tofu", "Garlic cloves", "Potato", "Onion", "Green onion", "Zucchini", "Korean chili pepper(cheong-gochu)", "Anchovies"],
            "youtube_url": "https://youtu.be/Slj_fM1jQVo"
        },
        "gamjatang": {
            "description": "Gamjatang is a soup made with pork neck bones and vegetables. The soft fatty meat picked from the gaps between the bones is especially tasty, and it makes a satisfying meal paired with rice.",
            "ingredients": ["Pork neck bones(or spine bones)", "Ginger", "Korean fermented bean paste(doenjang)", "Shiitake mushrooms", "Onion", "Red chili pepper", "Napa cabbage", "Medium potatoes", "Soybean sprouts", "Green onion", "Perilla leaves"],
            "youtube_url": "https://youtu.be/dfET5tfvnxw"
        },
        "kimbap": {
            "description": "Kimbap is a seaweed rice roll made with gim (a sheet of dried seaweed) and bap (rice). Various fillings can be used, from beef and vegetables to kimchi and ham.",
            "ingredients": ["Rice", "Seaweed paper(gim)", "Beef(skirt steak or tenderloin, or ground beef)", "Carrot", "Egg", "Yellow pickled radish", "Spinach", "Garlic cloves", "Soy sauce", "Sugar", "Salt", "Toasted sesame oil", "Vegetable oil"],
            "youtube_url": "https://youtu.be/Y-Y9CXGRJPU"
        },
        "jeyuk bokkeum": {
            "description": "jeyuk bokkeum is a spicy stir-fried pork dish with vegetables.",
            "ingredients": ["Pork belly", "Hot chili paste(gochujang)", "Garlic cloves", "Onion", "Soy sauce", "Hot pepper flakes(gochugaru)", "Sugar", "Ground black pepper", "Toasted sesame oil", "Ginger", "Toasted sesame seeds"],
            "youtube_url": "https://youtu.be/3oFCGKmzQX8"
        },
        "jajangmyeon": {
            "description": "Jjajangmyeon is a popular Korean Chinese dish with noodles in savory black bean paste with pork and vegetables.",
            "ingredients": ["Noodles", "Korean Black bean paste(chunjang)", "Pork belly", "Korean radish(or daikon)", "Zucchini", "Potato", "Onion chunks", "Vegetable oil", "Potato starch powder", "Toasted sesame oil", "Cucumber"],
            "youtube_url": "https://youtu.be/F4Cm75Qvk4A"
        },
        "dak_kalguksu": {
            "description": "Dak kalguksu is a Korean noodle soup with hand-cut noodles in a light chicken broth; 'dak' means chicken, and 'kal' means knife, referring to the knife-cut noodles, and ‘guksu’ means noodle soup.",
            "ingredients": ["Chicken", "Noodles", "Broth", "Water", "Garlic cloves", "Onion", "Flour", "Potato starch", "Zucchini", "Vegetable oil", "Salt", "Fish sauce", "Ground black pepper"],
            "youtube_url": "https://youtu.be/5Ceg1QN56p0"
        },
        "kimchi_jjigae": {
            "description": "Kimchi-jjigae is a spicy stew made with fermented kimchi and pork, loved for its warm and hearty taste.",
            "ingredients": ["Kimchi", "Kimchi brine", "Tofu", "Onion", "Pork shoulder(or pork belly)", "Salt", "Sugar", "Korean hot pepper flakes(gochugaru)", "Korean hot pepper paste(gochujang)", "Toasted sesame oil", "Anchovy stock"],
            "youtube_url": "https://youtu.be/rJgb92JWMCE"
        },
        "mandu": {
            "description": "Mandu is Korean-style dumplings filled with meat and vegetables, enjoyed by families across Korea.",
            "ingredients": ["Dumpling wrappers", "Pork belly", "Ginger", "Garlic cloves", "Soy sauce", "Ground black pepper", "Toasted sesame oil", "Zucchini", "Onion", "Salt", "Vegetable oil", "Sweet potato starch noodles(dangmyeon)", "Asian chives(buchu)", "Mung bean sprouts", "Tofu"],
            "youtube_url": "https://youtu.be/zECZXmDmHR0"
        },
        "pajeon": {
            "description": "Pajeon is a savory Korean pancake made with green onions and often seafood.",
            "ingredients": ["Flour", "Water", "Green onions", "Soybean paste", "Sugar", "Vegetable oil", "Seafood (optional)"],
            "youtube_url": "https://youtu.be/RXcsHj1l-Pc"
        },
        "samgyetang": {
            "description": "Samgyetang is ginseng chicken soup with a whole young chicken stuffed with rice, ginseng, garlic, and jujube.",
            "ingredients": ["Chicken(cornish hen)", "Ginseng root", "Garlic cloves", "Jujube", "Green onion", "Salt", "Short grain rice", "Ground black pepper"],
            "youtube_url": "https://youtu.be/JUmFtHqwrnk"
        },
        "samgyeopsal": {
            "description": "Grilled Pork Belly (Samgyeopsal-gui) is a popular Korean BBQ dish enjoyed socially around the table.",
            "ingredients": ["Pork belly", "Salt", "Green onion salad", "Soy sauce", "Toasted sesame seeds", "Hot pepper flakes(gochugaru)", "Doenjang"],
            "youtube_url": "https://youtu.be/23tRGHUX3qM"
        },
        "sundaeguk": {
            "description": "Sundaeguk is a Korean blood sausage soup.",
            "ingredients": ["Sundae (blood sausage)", "Pork broth", "Garlic", "Green onions"],
            "youtube_url": "https://youtu.be/cWo79ow26nU?si=2zlLNGex1EnIr8hL"
        },
        "tteokbokki": {
            "description": "Tteokbokki is a popular Korean street food made with spicy rice cakes. Tteokbokki is chewy rice cakes cooked in a red, spicy broth.",
            "ingredients": ["Rice cakes(tteok)", "Water", "Dried Anchovy", "Dried kelp", "Korean hot pepper paste(gochujang)", "Korean hot pepper flakes(gochugaru)", "Sugar", "Green onion", "Fish cakes", "Boiled egg(optional)"],
            "youtube_url": "https://youtu.be/TA3Uo3a9674"
        },
        "tteokguk": {
            "description": "Tteokguk (rice cake soup) is a delicious, filling soup made of disc-shaped rice cakes in a clear broth. Koreans always eat it on Seollal (Korean New Year’s Day).",
            "ingredients": ["Rice cakes(tteok)", "Water", "Pound beef(flank steak or brisket)", "Beef broth", "Egg", "Green onions", "Garlic cloves", "Vegetable oil", "Fish sauce(or soup soy sauce)", "Toasted sesame oil", "Ground black pepper", "Dried seaweed paper(gim)", "Salt"],
            "youtube_url": "https://youtu.be/plvT0vWBK14"
        },
        "hotteok": {
            "description":  "Hotteok is a flour dough pancake filled with sugar syrup inside. It’s one of the most popular street snacks in Korea.",
            "ingredients": ["Sugar", "Dry yeast", "Salt", "Vegetable oil", "Flour", "Cinnamon powder", "Walnuts"],
            "youtube_url": "https://youtu.be/R_MPEq53QFs"
        },
        "sundubu_jjigae": {
            "description": "Sundubu-jjigae is a spicy, seasoned stew made with a type of silky soft tofu called sundubu. Served hot at the table in its traditional earthenware bowl.",
            "ingredients": ["Korean hot pepper flakes(gochugaru)", "Toasted sesame oil", "Ground black pepper", "Vegetable oil", "Garlic cloves", "Onion", "King oyster mushroom", "Green onion", "Egg", "Anchovy kelp stock", "Fish sauce", "Soft tofr"],
            "youtube_url": "https://youtu.be/BvZ9m3Bikuw"
        },
        "galbi_jjim": {
            "description":  "Galbi-jjim is made with beef short ribs and is often prepared for special occasions.\
            Traditionally it’s a dish for special occasions such as Korean festival days like Chuseok, but you can make it for any occasion or as a weekend dish.",
            "ingredients": ["Shiitake mushrooms", "Soy sauce", "Mirin(mirim)", "Water", "Ground black pepper", "Garlic cloves", "Ginger", "Korean radish", "Carrot", "Beef short ribs"],
            "youtube_url": "https://youtu.be/vtGzj6cUn7Q"
        },
        "japchae": {
            "description": "Japchae is sweet potato starch noodles stir fried with vegetables and meat.\
        Stir frying each ingredient separately seems like a lot of labor, but each one requires a different cooking time and a bit of care, and keeping the color and freshness of each ingredient intact makes for a stunning final presentation.",
            "ingredients": ["Beef(filet mignon or pork shoulder)", "Shiitake mushroom", "Garlic cloves", "Sugar", "Soy sauce", "Toasted sesame oil", "Toasted sesame seeds", "Egg", "Spinach", "Sweet potato starch noodles(dangmyeon)", "Green onion", "Onion", "White mushroom", "Carrot", "Red bell pepper", "Ground black pepper", "Salt", "Vegetable oil"],
            "youtube_url": "https://youtu.be/i1djfV9uigc"
        },
        "ganjang_gejang": {
            "description": "Ganjang Gejang is a traditional Korean dish made by marinating fresh raw crab in a seasoned soy sauce mixture, emphasizing the crab's natural sweetness and soft texture.",
            "ingredients": ["Live blue crabs(or live flower crabs)", "Apple", "Garlic cloves", "Ginger", "Green chili peppers", "Dried red chili peppers", "Kelp", "Soy sauce", "Rice syrup", "Water"],
            "youtube_url": "https://youtu.be/c8euGxGY32I"
        },
        "galchi_jorim": {
            "description": "Galchi Jorim is a Korean braised dish featuring cutlassfish simmered in a spicy, savory sauce with vegetables, creating tender fish with rich flavors.",
            "ingredients":["Beltfish", "Korean radish(or daikon)", "Onion", "Green onion", "Green chili peppers", "Garlic cloves", "Ginger", "Soy sauce", "Korean hot pepper flakes(gochugaru)", "Ground black pepper", "Water"],
            "youtube_url": "https://youtu.be/dTsYsXpJ30Y"
        },
        "golbaengi_somen": {
            "description": "Golbaengi Somen is a Korean dish made with sea snails mixed in a spicy, tangy sauce served with somen noodles, creating a refreshing yet flavorful combination.",
            "ingredients": ["Sea snail", "Onion", "Carrot", "Cucumber", "Perilla leaves", "Green onion", "Cabbage", "Somen noodles", "Korean spicy green chili peppers(cheongyang)", "Korean hot pepper paste(gochujang)", "Sugar", "Vinegar", "Garlic", "Korean hot pepper flackes(gochugaru)", "Sesame oil", "Soy sauce", "Sesame seeds"],
            "youtube_url": "https://www.youtube.com/watch?v=V2Zpybxv-FU"
        },
        "haemul_jjim": {
            "description": "Haemul-jjim is a Korean steamed seafood dish that combines a variety of shellfish, squid, octopus, and sometimes fish with a spicy, savory sauce.\
            The seafood is simmered with vegetables such as bean sprouts, onions, and peppers, absorbing the rich, spicy flavors.\
            Known for its bold taste and vibrant presentation, Haemul-jjim is often served at gatherings and enjoyed as a hearty main dish.",
            "ingredients": ["Squid", "Shrimp", "Mussels", "Clams", "Water", "Fish sauce", "Bean sprouts", "Green onion", "Water parsley", "Onion", "Korean  pepper flackes(gochugaru)", "Sesame sees", "Starch powder", "Soy sauce", "Korean chili paste(gochujang)", "Sugar", "Rice wine(or Mirin)", "Garlic", "Ground black pepper"],
            "youtube_url": "https://www.youtube.com/watch?v=Q2oMHJfbaPM"
        },
        "dakgalbi": {
            "description": "Dak-galbi is a popular Korean dish featuring spicy, marinated chicken stir-fried with vegetables, such as cabbage, sweet potatoes, and onions, often accompanied by rice cakes.\
            Known for its bold, savory-sweet flavor and vibrant red color from gochujang (Korean red chili paste), it’s typically cooked at the table in a large pan, making it a social meal that’s as fun to cook as it is to eat.\
            Dak-galbi is enjoyed both in restaurants and at home, often wrapped in lettuce leaves with ssamjang sauce for an extra burst of flavor.",
            "ingredients": ["Chicken thigh(or drumsticks)", "Soy sauce", "Ground black pepper", "Garlic cloves", "Ginger", "Water", "Korean hot pepper flakes(gochugaru)", "Rice syrup(or corn syrup, or sugar)", "Rice cake"],
            "youtube_url": "https://youtu.be/JWccdweoVQg"
        },
        "jangjorim": {
            "description": "Jangjorim is a savory Korean side dish made by simmering beef, usually brisket or eye of round, in a soy sauce-based broth with garlic, green onions, and spices.\
            The beef is simmered until tender and then shredded into bite-sized pieces, absorbing the flavorful sauce. Often, hard-boiled eggs or quail eggs are added to the broth for extra flavor.\
            Jangjorim is served cold or at room temperature,making it a popular banchan (side dish) that pairs well with rice, adding a rich, salty, and slightly sweet element to meals.",
            "ingredients": ["Beef flank steak(or beef brisket, beef eye round, shank meat, or any beef with a grain)", "Water", "Soy sauce", "Garlic cloves", "Onion", "Green chili peppers"],
            "youtube_url": "https://youtu.be/mz98rHLxtiM"
        },
        "dotorimuk_muchim": {
            "description": "Dotori-muk is a savory jelly made from acorn starch, commonly served as a refreshing, cold salad topped with soy sauce, sesame oil, and vegetables like julienned carrots and green onions.\
            Its nutty flavor and firm texture make it a popular Korean side dish.",
            "ingredients": ["Acorn jelly", "Water", "Kosher salt", "Soy sauce", "Honey(or sugar)", "Garlic cloves", "Green onion", "Korean hot pepper flakes(gochugaru)", "Toasted sesame oil", "Toasted sesame seeds", "Shredded red pepper(silgochu)", "Lettuce", "Onion", "Edible chrysanthemum", "Perilla leaves", "Carrot", "Cucumber", "Red chili pepper", "Green chili pepper"],
            "youtube_url": "https://youtu.be/Bi2iV3tbM7k"
        },
        "jokbal": {
            "description": "Jokbal consists of pig’s trotters braised in a rich soy-based sauce with garlic, ginger, and spices until tender.\
            The flavorful, gelatinous meat is typically served in slices and enjoyed with lettuce wraps, ssamjang, and pickled radish.",
            "ingredients": ["Pig's trotter", "Water", "Korean fermented soybean paste(doenjang)", "Mirin", "Soy sauce", "Brown sugar", "Kosher salt", "Rice syrup", "Ginger", "Onion", "Toasted sesame seeds"],
            "youtube_url": "https://youtu.be/rRQIRcQqb4k"
        },
        "mul_naengmyeon": {
            "description": "Mul-naengmyeon is a chilled noodle soup made with buckwheat or arrowroot noodles served in a tangy, cold beef or radish broth, often topped with cucumber, radish, and a boiled egg. \
            Its refreshing taste makes it a favorite summer dish in Korea.",
            "ingredients": ["Dried naengmyeon noodles", "Liquid or powdered concentratd broth", "Mustard oil", "English cucumber", "Korean pear", "Kosher salt", "Sugar", "White vinegar", "Hard-boiled egg", "Toasted sesame seeds"],
            "youtube_url": "https://youtu.be/QIgLSko7Kmc"
        },
        "bossam": {
            "description": "Bossam is a Korean dish of tender, boiled pork slices served with fresh vegetables, ssamjang, and kimchi. Each slice of pork is wrapped in lettuce or perilla leaves with condiments, making for a rich and flavorful bite.",
            "ingredients": ["brown sugar", "daikon radish", "doenjang", "fermented salted shrimp", "fish sauce", "garlic, ginger", "gochugaru", "Korean radish", "kosher salt", "napa cabbage", "onion", "oysters", "pork", "sugar", "toasted sesame seeds", "vinegar"],
            "youtube_url": "https://youtu.be/t0Ta_ckc9O0"
        },
        "yukhoe": {
            "description": "Yukhoe is a Korean-style beef tartare, typically made from fresh raw beef marinated in sesame oil, soy sauce, garlic, and spices. Often garnished with egg yolk and pear slices, it’s known for its tender, savory-sweet flavor.",
            "ingredients": ["beef", "beef chuck steak", "beef flank", "eggs", "filet minon", "garlic", "green onion", "ground black pepper", "honey", "Korean pear", "pine nuts", "sesame seeds", "soy sauce", "sugar", "toasted sesame oil"],
            "youtube_url": "https://youtu.be/pa-A2plYl7Q"
        },
        "yakgwa": {
            "description": "Yakgwa is a traditional Korean dessert made with wheat flour, sesame oil, and honey, then fried and soaked in a sweet honey-ginger syrup. These golden, flower-shaped cookies are popular during festivals and celebrations.",
            "ingredients": ["all-purpose wheat flour", "cinnamon powder", "cooking oil", "ginger", "ground black pepper", "honey", "kosher salt", "pine nuts", "pumpkin seeds", "rice syrup", "soju", "sugar", "toasted sesame oil"],
            "youtube_url": "https://youtu.be/s41UpqpY-qc"
        },
        "sanjeok": {
            "description": "Sanjeok consists of thinly sliced beef or pork and various vegetables, skewered and grilled or pan-fried. Each ingredient is marinated for a savory taste, and the skewers are commonly served at special occasions and holidays.",
            "ingredients": ["beef", "carrot", "cooking oil", "egg", "flour", "garlic", "green onion", "ground black pepper", "kosher salt", "large green onion", "sirloin steak", "soy sauce", "toasted sesame oil", "toasted sesame seeds", "vegetable oil", "vinegar"],
            "youtube_url": "https://youtu.be/G_QSybo3ND4"
        },
        "bungeo_ppang": {
            "description": "Bungeo-ppang is a fish-shaped pastry filled with sweet red bean paste, traditionally sold as a winter street food in Korea. The crispy outer shell and warm, sweet filling make it a nostalgic favorite.",
            "ingredients": ["baking soda", "brown sugar", "sweet red beans", "flour", "kosher salt", "sugar", "vegetable oil", "water"],
            "youtube_url": "https://youtu.be/UN1yoJQe_KU"
        },
        "beondegi": {
            "description": "Beondegi, or silkworm pupae, is a popular Korean street snack with a unique, savory flavor. Often boiled or steamed and seasoned, it has a chewy texture and is enjoyed for its high protein content.",
            "ingredients": ["steamed silkworm chrysalis", "red pepper", "green onion", "soy sauce", "sesame oil", "garlic cloves", "salt", "water"],
            "youtube_url": "https://www.youtube.com/watch?v=d7YQ4x0XFmE"
        },
        "gyeran_mari": {
            "description": "Gyeran-mari is a Korean-style rolled omelet, typically made with finely chopped vegetables, ham, or seaweed mixed into the egg. The roll is sliced into bite-sized pieces, making it a colorful and flavorful banchan (side dish) that’s popular in lunchboxes.",
            "ingredients":  ["carrot", "egg", "green bell pepper", "ground black pepper", "kosher salt", "onion", "red bell pepper", "vegetable oil"],
            "youtube_url": "https://youtu.be/kN89ewZjOR8"
        }
    }

    # 메뉴 정보 가져오기 함수
    def get_menu_info(food_name):
        if food_name in menu_data:
            food = menu_data[food_name]
            return food["description"], food["ingredients"], food["youtube_url"]
        else:
            return "The menu item does not exist in the data.", [], ""

    # 알레르기 경고 메시지 생성 함수
    def check_allergens(ingredients, selected_allergy):
        detected_allergens = []
        for allergen in selected_allergy:
            # 알러지 키워드가 재료 리스트에 있는지 검사
            if any(keyword in ' '.join(ingredients).lower() for keyword in allergen_keywords.get(allergen, [])):
                detected_allergens.append(allergen)
        if detected_allergens:
            # 빨간색으로 경고 메시지를 표시
            return f"<span style='color:red; font-weight:bold'>Warning: This dish contains allergens: {', '.join(detected_allergens)}. Please check with the staff for details.</span>"
        else:
            return "No allergens detected in this dish based on your inputs."

    # Streamlit
    st.title("Korean Menu Information")
    st.write("Enter a menu item to get its description, ingredients, and a YouTube tutorial.")

    # 메뉴 이름 입력
    food_name = st.text_input("Enter the name of the food (e.g., Bibimbap)").strip().lower()

    if food_name:
        menu_description, menu_ingredients, youtube_url = get_menu_info(food_name)
        
        # 메뉴 정보 출력
        st.subheader("Menu Information")
        st.write("**Description**:", menu_description)
        
        if menu_ingredients:
            st.write("**Ingredients**:", ', '.join(menu_ingredients))
            st.write("[YouTube Tutorial](" + youtube_url + ")")
            # 사용 예시
            warning_message = check_allergens(menu_ingredients, st.session_state.selected_allergy)
            st.markdown(warning_message, unsafe_allow_html=True)
        else:
            st.write("Menu not found. Please try another menu item.")
    
