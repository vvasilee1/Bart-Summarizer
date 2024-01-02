from flask import Flask,request,render_template
from summarizer import SummarizerPipeline
app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')

@app.route('/summarize',methods=['POST'])
def summarize():
    if request.method == 'POST':
       input_text = request.form()
       summary = SummarizerPipeline(input_text)
       
       return render_template('index.html',summary=summary,input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)