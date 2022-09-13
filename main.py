
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/mypage/me', methods=['GET'] )
def me():
    return render_template("me.html")


@app.route('/mypage/contact',methods=['GET'])
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()

