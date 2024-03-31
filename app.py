from flask import Flask, render_template, request
import statistics

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numeros_str = request.form['numeros']
        numeros_list = numeros_str.split(',')
        numeros = [float(num) for num in numeros_list]
        
        media = statistics.mean(numeros)
        mediana = statistics.median(numeros)
        moda = statistics.mode(numeros)
        
        return render_template('resultado.html', media=media, mediana=mediana, moda=moda)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
