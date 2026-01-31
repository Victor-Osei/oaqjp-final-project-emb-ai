# import os
# from flask import Flask, request, jsonify, render_template
# from EmotionDetection.emotion_detection import emotion_detector

# # Define the paths to your nested templates and static folders
# template_dir = os.path.join(os.getcwd(), "oaqjp-final-project-emb-ai", "templates")
# static_dir = os.path.join(os.getcwd(), "oaqjp-final-project-emb-ai", "static")

# # Create Flask app with custom folders
# app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# # Home route: render main page
# @app.route("/")
# def home():
#     return render_template("index.html")

# # Favicon route to avoid 404 logs
# @app.route("/favicon.ico")
# def favicon():
#     return "", 204

# # Route for emotion detection
# @app.route("/emotionDetector", methods=["GET", "POST"])
# def detect_emotion_route():
#     if request.method == "POST":
#         data = request.get_json()
#         statement = data.get("statement", "")
#         if not statement:
#             return jsonify({"error": "No statement provided"}), 400

#         result = emotion_detector(statement)

#         response_text = (
#             f"For the given statement, the system response is "
#             f"'anger': {result['anger']}, "
#             f"'disgust': {result['disgust']}, "
#             f"'fear': {result['fear']}, "
#             f"'joy': {result['joy']}, "
#             f"'sadness': {result['sadness']}. "
#             f"The dominant emotion is {result['dominant_emotion']}."
#         )

#         return jsonify({
#             "result": result,
#             "formatted_response": response_text
#         })

#     # GET request simply renders page
#     return render_template("index.html")


# # Run the app
# if __name__ == "__main__":
#     app.run(host="localhost", port=0, debug=True)




# 
# server.py for handlig error when dominant emotion is nono
# import os
# from flask import Flask, request, jsonify, render_template
# from EmotionDetection.emotion_detection import emotion_detector

# # Nested templates and static folders
# template_dir = os.path.join(os.getcwd(), "oaqjp-final-project-emb-ai", "templates")
# static_dir = os.path.join(os.getcwd(), "oaqjp-final-project-emb-ai", "static")

# app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# # Home route
# @app.route("/")
# def home():
#     return render_template("index.html")

# # Favicon route to avoid 404
# @app.route("/favicon.ico")
# def favicon():
#     return "", 204

# # Emotion detection route
# @app.route("/emotionDetector", methods=["GET", "POST"])
# def detect_emotion_route():
#     if request.method == "POST":
#         data = request.get_json()
#         statement = data.get("statement", "")

#         # Call emotion detector
#         result = emotion_detector(statement)

#         # Handle blank or invalid input
#         if result['dominant_emotion'] is None:
#             response_text = "Invalid text! Please try again!"
#         else:
#             response_text = (
#                 f"For the given statement, the system response is "
#                 f"'anger': {result['anger']}, "
#                 f"'disgust': {result['disgust']}, "
#                 f"'fear': {result['fear']}, "
#                 f"'joy': {result['joy']}, "
#                 f"'sadness': {result['sadness']}. "
#                 f"The dominant emotion is {result['dominant_emotion']}."
#             )

#         # Debug log
#         print(f"Statement submitted: '{statement}'")
#         print(f"Detected emotions: {result}")

#         return jsonify({
#             "result": result,
#             "formatted_response": response_text
#         })

#     # GET request
#     return render_template("index.html")

# # Run the app
# if __name__ == "__main__":
#     app.run(host="localhost", port=0, debug=True)




# Modified for PyLint Compliance
"""
Flask application for emotion detection using Watson API.

Routes:
- "/" : Home page rendering index.html
- "/favicon.ico" : Prevents 404 on favicon requests
- "/emotionDetector" : POST route for detecting emotions from input text

Handles blank inputs and invalid entries gracefully.
"""

import os
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Paths for nested templates and static folders
template_dir = os.path.join(os.getcwd(), "oaqjp-final-project-emb-ai", "templates")
static_dir = os.path.join(os.getcwd(), "oaqjp-final-project-emb-ai", "static")

# Create Flask app
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


@app.route("/")
def home():
    """
    Render the main page (index.html) for the application.
    Returns:
        HTML page for user input.
    """
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    """
    Handle favicon requests to prevent 404 logs.
    Returns:
        Empty response with HTTP 204 (No Content)
    """
    return "", 204


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion_route():
    """
    Handle emotion detection requests.

    POST: Accepts JSON with 'statement' key, calls emotion_detector,
          and returns emotion scores and dominant emotion in JSON.
          Handles blank inputs by returning an error message.

    GET: Renders the main index.html page.

    Returns:
        JSON response with emotion scores or error message (POST)
        or HTML page (GET)
    """
    if request.method == "POST":
        data = request.get_json()
        statement = data.get("statement", "")

        # Call emotion detector
        result = emotion_detector(statement)

        # Handle blank or invalid input
        if result['dominant_emotion'] is None:
            response_text = "Invalid text! Please try again!"
        else:
            response_text = (
                f"For the given statement, the system response is "
                f"'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, "
                f"'joy': {result['joy']}, "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )

        # Debug logs
        print(f"Statement submitted: '{statement}'")
        print(f"Detected emotions: {result}")

        return jsonify({
            "result": result,
            "formatted_response": response_text
        })

    # GET request
    return render_template("index.html")


# Run the app
if __name__ == "__main__":
    app.run(host="localhost", port=0, debug=True)
