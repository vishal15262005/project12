from flask import Flask, request, render_template, jsonify
import tensorflow as tf
import numpy as np
import os
import base64
from io import BytesIO
from PIL import Image, ImageDraw
from tensorflow.keras.preprocessing import image
from chatbox import get_chat_response  # Import chatbot logic

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("model/cow_skin_model.h5")

# Ensure upload folder exists
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Define class labels
class_labels = ["Lumpy", "Normal"]

# Precaution lists
lsd_precautions = [
    "Isolate infected cattle immediately.",
    "Provide clean and nutritious food.",
    "Regularly disinfect the cattle shed.",
    "Avoid sharing equipment between infected and healthy animals.",
    "Consult a veterinarian for vaccination and treatment."
]

healthy_precautions = [
    "Provide a balanced diet rich in nutrients.",
    "Ensure clean and fresh drinking water is always available.",
    "Regularly clean and disinfect the cattle shed.",
    "Schedule routine veterinary check-ups and vaccinations.",
    "Monitor cattle behavior and isolate sick animals immediately."
]

# Function to predict disease
def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    confidence = float(np.max(predictions) * 100)  # Convert to float

    predicted_class = int(predictions[0][0] > 0.5)
    result = class_labels[predicted_class]

    return result, confidence

# Function to draw a bounding box (Dummy Example)
def draw_bounding_box(image_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size
    x1, y1, x2, y2 = width // 4, height // 4, 3 * width // 4, 3 * height // 4
    draw.rectangle([x1, y1, x2, y2], outline="red", width=5)

    boxed_image_path = os.path.join(UPLOAD_FOLDER, "detected_" + os.path.basename(image_path))
    img.save(boxed_image_path)
    return boxed_image_path

# Homepage Route
@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file:
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)

                result, confidence = predict_disease(filepath)

                if result == "Normal":
                    message = "✅ No Lumpy Skin Disease detected. Keep following good cattle management practices!"
                    result_display = "✅ Healthy - No Disease Detected"
                    precautions = healthy_precautions
                else:
                    message = "⚠ Lumpy Skin Disease detected! Take immediate precautions."
                    result_display = "⚠ Lumpy Skin Disease Detected!"
                    precautions = lsd_precautions
                    filepath = draw_bounding_box(filepath)

                return render_template(
                    "index.html",
                    file_path=filepath,
                    result_display=result_display,
                    confidence=confidence,
                    message=message,
                    precautions=precautions,
                )
    return render_template("index.html")

# Capture Image Route
@app.route("/capture", methods=["POST"])
def capture_image():
    try:
        data = request.json["image"]
        img_data = base64.b64decode(data.split(",")[1])
        img = Image.open(BytesIO(img_data))
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], "captured_image.jpg")
        img.save(filepath)

        result, confidence = predict_disease(filepath)

        if result == "Normal":
            message = "✅ No Lumpy Skin Disease detected. Maintain hygiene and routine check-ups!"
            result_display = "✅ Healthy - No Disease Detected"
            precautions = healthy_precautions
        else:
            message = "⚠ Lumpy Skin Disease detected! Take immediate action."
            result_display = "⚠ Lumpy Skin Disease Detected!"
            precautions = lsd_precautions
            filepath = draw_bounding_box(filepath)

        return jsonify({
            "file_path": filepath,
            "result_display": result_display,
            "confidence": confidence,
            "message": message,
            "precautions": precautions,
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Chatbot Route
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip().lower()
    reply = get_chat_response(user_message)
    return jsonify({"reply": reply})
@app.route("/veterinary")
def veterinary():
    return render_template("veterinary.html")  #

# Insurance Information Route
@app.route("/insurance", methods=["GET"])
def get_insurance():
    insurance_data = [
        {"provider": "ABC Insurance", "coverage": "Theft, Illness, Accident", "premium": "₹2000/year"},
        {"provider": "XYZ Livestock", "coverage": "Natural Disasters, Death", "premium": "₹2500/year"},
    ]
    return jsonify(insurance_data)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict_growth", methods=["POST"])
# Growth Prediction Route
@app.route("/predict_growth", methods=["POST"])
# Growth Prediction Route
@app.route("/predict_growth", methods=["POST"])
@app.route("/predict_growth", methods=["POST"])
@app.route("/predict_growth", methods=["POST"])
# Growth Prediction Route
@app.route("/predict_growth", methods=["POST"])
@app.route("/predict_growth", methods=["POST"])
@app.route("/predict_growth", methods=["POST"])
def predict_growth():
    try:
        data = request.json
        age = int(data["age"])
        weight = float(data["weight"])
        milking = data["milking"]

        # Example Growth Prediction Logic
        future_weight = weight + (age * 0.5)  # Dummy formula (modify as needed)

        # Growth Status Condition
        if age > 24:
            growth_prediction = "🐄 Your cattle is fully grown. Maintain its health!"
        else:
            growth_prediction = f"📈 Expected weight after 6 months: {future_weight + 12:.2f} kg"

        # Productivity Suggestions
        if milking == "yes":
            suggestions = [
                "🥛 **Best Nutrition for Increased Milk Yield:**",
                "• Provide high-protein feed like alfalfa and soybean meal.",
                "• Ensure adequate calcium and mineral supplements.",
                "• Maintain proper hydration and avoid stress.",
                "• Regular milking schedules improve milk quality and quantity.",
                "• Consult a veterinarian for optimal dietary planning."
            ]
        else:
            suggestions = [
                "🌱 **Best Feeding Habits for Growth:**",
                "• Feed young cattle with a balanced fiber and protein-rich diet.",
                "• Ensure access to clean drinking water and mineral blocks.",
                "• Regular deworming and vitamin supplements boost growth.",
                "• Provide ample grazing time for natural nutrient intake.",
                "• Monitor weight gain and adjust feed accordingly."
            ]

        return jsonify({
            "prediction": growth_prediction,
            "weight_estimate": f"📈 Estimated weight after 6 months: **{future_weight:.2f} kg**",
            "suggestions": suggestions  # Returning as a list for structured display
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template
import sqlite3
import webbrowser

app = Flask(__name__)

# Temporary storage for vet requests (Use DB in production)
vet_requests = []

# 🏡 Home Route (Renders Index Page)
@app.route('/')
def home():
    return render_template('index.html')

# 📌 Route: Get Vet Requests
@app.route('/vet-requests', methods=['GET'])
def get_requests():
    return jsonify(vet_requests)

# 📌 Route: Submit Vet Request
@app.route('/vet-request', methods=['POST'])
def submit_request():
    data = request.json

    # Validate input
    if not all(key in data for key in ["farmer_name", "date", "time", "reason", "vet_number"]):
        return jsonify({"error": "Missing data"}), 400

    vet_requests.append(data)

    # Generate WhatsApp message URL
    message = (
        f"Hello Doctor,\n"
        f"👤 Farmer: {data['farmer_name']}\n"
        f"📅 Date: {data['date']}\n"
        f"⏰ Time: {data['time']}\n"
        f"📝 Reason: {data['reason']}"
    )
    
    # Format for WhatsApp URL encoding
    wa_link = f"https://wa.me/{data['vet_number']}?text={message.replace(' ', '%20')}"
    
    # Open WhatsApp automatically (optional)
    webbrowser.open(wa_link)

    return jsonify({"message": "Vet consultation request sent via WhatsApp!"})

# ✅ Run the App
if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
