from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            return "VALUE1 passed" # do something
        elif  request.form.get('action2') == 'VALUE2':
            return "VALUE2 passed" # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        start_html = """
<!DOCTYPE html>
<html lang="en">
<head> <!--additional info and links -->
    <link href="main.css" type="text/css" rel="stylesheet"> 
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content = "IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Qaiser's Skull Island!</title>
</head>
<body>
<h1>Skull Island</h1>
"""
button = """
<h3>Our Flask Buttons<h3/>
    <form method="post" action="/">
        <input type="submit" value="VALUE1" name="action1"/>
        <input type="submit" value="VALUE2" name="action2" />
</form>"""
end_html = """
</body>
</html>"""
        return start_html
    
    # return render_template("index.html")
    return start_html

if __name__ == "__main__":
    app.run(debug=True)