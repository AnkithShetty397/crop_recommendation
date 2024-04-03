from django.shortcuts import render
import joblib
import numpy as np

crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

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
        return render(request, 'result.html', {'prediction': crop})
    else:
        return render(request, 'form.html')