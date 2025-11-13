from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Read all images inside static/gallery
    images = os.listdir("static/")
    images = [img for img in images if img.lower().endswith(("jpg", "jpeg", "png"))]
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)


