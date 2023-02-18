from flask import Flask,render_template,request
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add", methods =["GET", "POST"])
def add():
    if request.method=="POST":
        first=request.form.get("text")
        if first=="":
            return "NO INPUT GIVEN"
        else:
            t=first.upper()
            f=open("templates/list.html","r",encoding="utf8")
            content=f.read()
            soup=BeautifulSoup(content,"html.parser")
            new=soup.new_tag("li")
            new.string=t
            soup.ol.append(new)
            savechange=soup.prettify("utf-8")
            with open("templates/list.html","wb") as fr:
                fr.write(savechange)
            return "TASK ADDED TO YOUR TODO LIST  :     "+t
    return render_template("add.html")

@app.route("/view", methods =["GET", "POST"])
def view():
    f = open("templates/list.html", "r", encoding="utf8")
    content=f.read()
    soup = BeautifulSoup(content, 'html.parser')
    if request.method == 'POST':
        search=request.form.get("text")
        ol = soup.find("ol")
        li=ol.find_all('li')
        if search=="":
            return "NO INPUT GIVEN/ GIVE VALID INPUT"
        else:
            for i,l in enumerate(li, 1):
                text=l.get_text()
                t=str(i)+text
                if search in t:
                    li_to_delete = li[int(search) - 1]
                    li_to_delete.extract()
            with open("templates/list.html", "w") as f:
                f.write(str(soup))
    return render_template("list.html")

if __name__=="__main__":
    app.run(debug=True)

