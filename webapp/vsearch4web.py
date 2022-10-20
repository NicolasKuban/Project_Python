from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)


def log_request(req:'flask_request', res: str) -> None:
    dbconfig = {
        'host': '127.0.0.1',
        'user': 'vsearch',
        'password': 'vsearchpassd',
        'database': 'vsearchlogDB',
    }
    import mysql.connector
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    print("Подключение")
    _SQL = """
        insert into log
        (phrase, letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s)
    """
    print(_SQL)
    print((req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res,
                            ))
    cursor.execute(_SQL, (req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            "Mozilla",
                            res,
                            )
    )
    conn.commit()
    print("Записано")
    cursor.close()
    conn.close()
    # with open('vsearch.log', 'a') as logfile:
    #     print(req.form, req.remote_addr, req.user_agent, res, file=logfile, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template(
                'results.html',
                the_title='Here are your results:',
                the_phrase=phrase,
                the_letters=letters,
                the_results=results

    )

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template(
                'entry.html',
                the_title='Welcome to search4letters on the web'
    )

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return render_template(
                'viewlog.html',
                the_title='View Log',
                the_row_titles= ['request', 'IP', 'browser', 'result'],
                the_data= contents,
    )

if __name__ == "__main__":
    app.run(debug=True)