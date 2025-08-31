
from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

# Directory to save the uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/deploy', methods=['POST'])
def deploy():
    if 'bot_code' not in request.files or 'requirements' not in request.files:
        return jsonify({"error": "No file part"}), 400

    bot_code = request.files['bot_code']
    requirements_file = request.files['requirements']

    # Save the uploaded files
    bot_code_path = os.path.join(app.config['UPLOAD_FOLDER'], 'bot_code.py')
    requirements_path = os.path.join(app.config['UPLOAD_FOLDER'], 'requirements.txt')

    bot_code.save(bot_code_path)
    requirements_file.save(requirements_path)

    # Install dependencies
    subprocess.run(["pip", "install", "-r", requirements_path])

    # Run the bot code
    subprocess.run(["python", bot_code_path])

    return jsonify({"message": "Bot deployed successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
    