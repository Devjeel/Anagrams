from flask import Flask, request
from anagrams import Anagrams

app = Flask(__name__)

@app.route('/anagrams')
def find_anagram():
    s1 = request.args.get("s1", "")
    s2 = request.args.get("s2", "")
    if Anagrams(s1, s2).check_anagram():
        return f"{s1} and {s2} are anagrams"
    else:
        return f"{s1} and {s2} are not anagrams"    

if __name__ == "__main__":
    app.run(debug=True)