from flask import Flask, render_template, request
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import text_cleaner
import os

app = Flask(__name__)

# Initialize Portfolio objects
portfolio = Portfolio()

@app.route('/', methods=['GET', 'POST'])
def index():
    email = None
    error = None

    if request.method == 'POST':
        url_input = request.form.get('url_input')
        temperature = float(request.form.get('temperature_input'))

        try:
            chain = Chain(temperature=temperature)
            loader = WebBaseLoader([url_input])
            data = text_cleaner(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = chain.extract_jobs(data)
            
            emails = []
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = chain.write_mail(job, links)
                emails.append(email)

            email = '\n\n'.join(emails)
        except Exception as e:
            error = str(e)
    
    return render_template('index.html', email=email, error=error)

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(debug=True, port=port)
