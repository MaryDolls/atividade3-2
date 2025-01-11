from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/fazer_pedido', methods=['GET', 'POST'])
def fazer_pedido():
    if request.method == 'POST':
        try:
            massa = request.form.get('massa', '')
            molho = request.form.get('molho', '')
            ingrediente1 = request.form.get('ingrediente1', '')
            ingrediente2 = request.form.get('ingrediente2', '')
            ingrediente3 = request.form.get('ingrediente3', '')
            ingrediente4 = request.form.get('ingrediente4', '')
            borda = request.form.get('borda', '')
            endereco = request.form.get('endereco', '')

            return render_template('confirmacao.html', 
                                   massa=massa, molho=molho, 
                                   ingrediente1=ingrediente1, ingrediente2=ingrediente2, 
                                   ingrediente3=ingrediente3, ingrediente4=ingrediente4, 
                                   borda=borda, endereco=endereco)
        except Exception as e:
            return render_template('error.html', error_message=str(e)), 500

    return render_template('fazer_pedido.html')

@app.route('/confirmacao')
def confirmacao():
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    try:
        app.run(debug=False)
    except SystemExit as e:
        print(f"SystemExit encountered: {e}")
        raise