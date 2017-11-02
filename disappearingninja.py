from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)    
                         
@app.route('/')          
                        
def ninjas():
    return render_template('ninjas.html')   

@app.route('/ninja')
def disappearingNinjas():
    return render_template('disappearingninjas.html')

@app.route('/ninja/<color>')
def ninjaColors(color):
    if color == 'red':
        color = url_for('static', filename='raphael.jpg')
        return render_template('ninjacolor.html', color = color)

    elif color == 'purple':
        color = url_for('static', filename='donatello.jpg')
        return render_template('ninjacolor.html', color = color)

    elif color == 'blue':
        color = url_for('static', filename='leonardo.jpg')
        return render_template('ninjacolor.html', color = color)

    elif color == 'orange':
        color = url_for('static', filename='michelangelo.jpg')
        return render_template('ninjacolor.html', color = color)

    else:
        color = url_for('static', filename='static/notapril.jpg')
        return render_template('ninjacolor.html', color = color)

app.run(debug=True) 