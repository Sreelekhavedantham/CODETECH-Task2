import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<action>')
def action(action):
    if action == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
    elif action == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
    return index()

@app.route('/shutdown')
def shutdown():
    GPIO.cleanup()  # Clean up GPIO
    return "Shutting down", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
