from django.shortcuts import render
import joblib
import numpy as np

crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
    
crop_description = {
    1: "Rice is a staple food for a large part of the world's human population, especially in Asia. It grows best in warm climates with high humidity and plenty of water. Rice cultivation requires a lot of water, and it is usually grown in flooded fields called paddies. There is a high demand for rice globally due to its importance as a primary food source.",
    2: "Maize, also known as corn, is one of the most widely grown crops in the world. It is a versatile crop used for food, animal feed, and industrial products. Maize grows well in a variety of climates, from tropical to temperate regions. It requires well-drained soil and plenty of sunlight. Maize production is driven by its demand in various industries, including food processing, livestock feed, and biofuel production.",
    3: "Jute is a long, soft, shiny vegetable fiber that can be spun into coarse, strong threads. It is one of the cheapest natural fibers and is second only to cotton in terms of production quantity. Jute grows best in warm and humid climates with well-drained soil. It is primarily used to make burlap, hessian, and gunny cloth. The demand for jute is driven by its eco-friendly nature and its use in packaging, textiles, and construction industries.",
    4: "Cotton is a soft, fluffy staple fiber that grows in a boll, or protective case, around the seeds of the cotton plants. It is one of the most important commercial crops globally, and it is grown in warm climates with adequate rainfall or irrigation. Cotton cultivation requires well-drained soil and plenty of sunlight. Cotton is used to make a variety of textile products, including clothing, bed sheets, and towels. The demand for cotton is driven by the textile industry's need for raw materials.",
    5: "Coconut is a tropical fruit that grows on the coconut palm tree. It is highly valued for its versatility and nutritional benefits. Coconut palms require warm climates with plenty of sunlight and regular rainfall. Coconuts are used in various forms, including fresh coconut water, coconut milk, coconut oil, and desiccated coconut. The demand for coconut products is driven by their use in cooking, cosmetics, and traditional medicine.",
    6: "Papaya is a tropical fruit with sweet, orange-colored flesh and black seeds. It grows best in warm climates with well-drained soil and plenty of sunlight. Papaya trees are relatively easy to cultivate and can produce fruit within a year of planting. Papayas are rich in vitamins, minerals, and antioxidants, making them a popular choice for healthy eating. The demand for papayas is driven by their nutritional value and delicious taste.",
    7: "Orange is a citrus fruit known for its sweet and tangy flavor. It grows on evergreen trees in subtropical and tropical regions. Oranges require well-drained soil and regular irrigation. They are rich in vitamin C and other nutrients, making them a popular choice for juices, snacks, and desserts. The demand for oranges is driven by their nutritional value and versatility in culinary applications.",
    8: "Apple is a sweet and crunchy fruit that grows on deciduous trees in temperate climates. It requires cold winters and warm summers to thrive. Apples come in various colors, flavors, and textures, depending on the variety. They are rich in fiber, vitamins, and antioxidants, making them a popular choice for healthy snacks and desserts. The demand for apples is driven by their nutritional value and long shelf life.",
    9: "Muskmelon, also known as cantaloupe, is a sweet and juicy fruit with a netted rind and orange flesh. It grows best in warm climates with well-drained soil and plenty of sunlight. Muskmelons are rich in vitamins A and C, as well as potassium and dietary fiber. They are often eaten fresh as a snack or used in fruit salads and desserts. The demand for muskmelons is driven by their refreshing taste and nutritional benefits.",
    10: "Watermelon is a large, juicy fruit with sweet, pink flesh and black seeds. It grows best in warm climates with plenty of sunlight and regular irrigation. Watermelons are rich in vitamins A and C, as well as water content, making them a hydrating and refreshing fruit. They are often eaten fresh as a snack or used in fruit salads, smoothies, and desserts. The demand for watermelons is driven by their delicious taste and high water content.",
    11: "Grapes are small, round fruits that grow in clusters on woody vines. They are cultivated in temperate and tropical regions around the world. Grapes require well-drained soil, plenty of sunlight, and regular pruning to thrive. They come in various colors, including green, red, and purple, and are often eaten fresh as a snack or used to make wine, juice, and jam. The demand for grapes is driven by their versatility and nutritional value.",
    12: "Mango is a tropical fruit known for its sweet and juicy flesh and large seed. It grows best in warm climates with well-drained soil and plenty of sunlight. Mango trees are relatively easy to cultivate and can produce fruit within a few years of planting. Mangoes are rich in vitamins A and C, as well as antioxidants, making them a popular choice for healthy snacks, smoothies, and desserts. The demand for mangoes is driven by their delicious taste and nutritional value.",
    13: "Banana is a long, curved fruit with a thick yellow peel and soft, creamy flesh. It grows on herbaceous plants in tropical and subtropical regions. Bananas require warm climates with plenty of sunlight and regular rainfall. They are rich in potassium, vitamins, and dietary fiber, making them a nutritious and convenient snack. Bananas can be eaten fresh, dried, or used in cooking and baking. The demand for bananas is driven by their availability, affordability, and nutritional value.",
    14: "Pomegranate is a round fruit with a thick, leathery skin and hundreds of edible seeds inside. It grows on deciduous shrubs or small trees in subtropical and temperate regions. Pomegranates require well-drained soil, plenty of sunlight, and regular irrigation. They are rich in antioxidants, vitamins, and minerals, making them a healthy choice for snacks, juices, and salads. The demand for pomegranates is driven by their nutritional value and medicinal properties.",
    15: "Lentil is a small, lens-shaped legume that grows in pods on the lentil plant. It is one of the oldest cultivated crops and is rich in protein, fiber, and essential nutrients. Lentils grow best in cool climates with well-drained soil and regular rainfall. They are a staple food in many cultures and are used in soups, stews, salads, and side dishes. The demand for lentils is driven by their nutritional value, versatility, and affordability.",
    16: "Black gram, also known as black lentil or urad dal, is a small, black seed with a white interior. It is rich in protein, fiber, and essential nutrients. Black gram grows best in warm climates with well-drained soil and regular rainfall. It is a staple food in many Indian dishes and is used to make dal, soups, curries, and snacks. The demand for black gram is driven by its nutritional value, culinary versatility, and cultural significance.",
    17: "Mung bean, also known as green gram or moong dal, is a small, green seed with a yellow interior. It is rich in protein, fiber, vitamins, and minerals. Mung beans grow best in warm climates with well-drained soil and regular rainfall. They are a staple food in many Asian cuisines and are used to make dal, sprouts, curries, and desserts. The demand for mung beans is driven by their nutritional value, versatility, and affordability.",
    18: "Moth bean, also known as matki or moth dal, is a small, brown seed with a creamy interior. It is rich in protein, fiber, vitamins, and minerals. Moth beans grow best in warm climates with well-drained soil and regular rainfall. They are a staple food in many Indian dishes and are used to make dal, curries, soups, and snacks. The demand for moth beans is driven by their nutritional value, culinary versatility, and cultural importance.",
    19: "Pigeon pea, also known as arhar dal or toor dal, is a small, round seed with a beige color and dark spots. It is rich in protein, fiber, vitamins, and minerals. Pigeon peas grow best in warm climates with well-drained soil and regular rainfall. They are a staple food in many cuisines around the world and are used to make dal, curries, soups, and stews. The demand for pigeon peas is driven by their nutritional value, versatility, and affordability.",
    20: "Kidney bean is a large, kidney-shaped legume with a deep red color. It is rich in protein, fiber, vitamins, and minerals. Kidney beans grow best in warm climates with well-drained soil and regular rainfall. They are a staple food in many cuisines and are used to make chili, soups, salads, and side dishes. The demand for kidney beans is driven by their nutritional value, culinary versatility, and popularity as a meat substitute.",
    21: "Chickpea, also known as garbanzo bean or chana dal, is a small, round seed with a beige color and nutty flavor. It is rich in protein, fiber, vitamins, and minerals. Chickpeas grow best in warm climates with well-drained soil and regular rainfall. They are a staple food in many cuisines and are used to make hummus, falafel, curries, salads, and snacks. The demand for chickpeas is driven by their nutritional value, culinary versatility, and popularity as a plant-based protein source.",
    22: "Coffee is a brewed beverage made from roasted coffee beans, which are the seeds of the coffee plant's berries. It is one of the most popular beverages globally and is consumed for its stimulating effects and rich flavor. Coffee plants grow best in tropical climates with well-drained soil and plenty of rainfall. They require careful cultivation and harvesting to produce high-quality beans. The demand for coffee is driven by its widespread popularity and the global coffee culture."
}

def make_prediction(model, N, P, k, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, k, temperature, humidity, ph, rainfall]])
    prediction = model.predict(features)
    return prediction

def predict_view(request):
    model = joblib.load('crop_prediction/random_forest_model.pkl')
    if request.method == 'POST':     
        data = request.POST
        N = data['N']
        P = data['P']
        k = data['k']
        temperature = data['temperature']
        humidity = data['humidity']
        ph = data['ph']
        rainfall = data['rainfall']
        
        prediction = make_prediction(model, N, P, k, temperature, humidity, ph, rainfall)
        crop = crop_dict[prediction[0]]
        description = crop_description[prediction[0]]
        return render(request, 'result.html', {'prediction': crop, 'description': description})
    else:
        return render(request, 'form.html')

