from flask import Flask, render_template, request
from detector import check_image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    reason = None

    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", result="No file selected")

        file = request.files["image"]
        if file.filename == "":
            return render_template("index.html", result="No file selected")

        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)

        result, reason = check_image(path)

    return render_template("index.html", result=result, reason=reason)

if __name__ == "__main__":
    app.run(debug=True)