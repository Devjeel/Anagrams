from flask import Flask, request
from flask_cors import CORS
from anagrams import Anagrams

app = Flask(__name__)
# To Allow Cross-origin request
cors = CORS(app, resources={r"/anagrams": {"origins": "http://localhost:3000"}})

@app.route('/anagrams', methods=["post"])
def find_anagram():
    s1 = request.form.get("s1", "")
    s2 = request.form.get("s2", "")
    return Anagrams(s1, s2).check_anagram()
 
if __name__ == "__main__":
    app.run(debug=True)