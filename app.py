from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from core.digital_twin import DigitalTwin
from core.insight_engine import InsightEngine
from core.prediction_engine import PredictionEngine
from core.decision_engine import DecisionSimulator
from core.neural_interface import NeuralInterface
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) # Secure session key

# Initialize Core Engines (Stateless)
insight_engine = InsightEngine()
prediction_engine = PredictionEngine()
decision_simulator = DecisionSimulator()
neural_interface = NeuralInterface()

@app.route('/')
def index():
    if 'twin_data' not in session:
        return redirect(url_for('setup'))
    return redirect(url_for('dashboard'))

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        # 1. Capture Identity
        name = request.form.get('name', 'Unknown Subject')
        twin = DigitalTwin(name)
        
        # 2. Capture Neural Architecture (Skills)
        skills = {
            "Neural Architecture": int(request.form.get('skill_neural', 0)) / 100.0,
            "Systems Thinking": int(request.form.get('skill_systems', 0)) / 100.0,
            "AI Integration": int(request.form.get('skill_ai', 0)) / 100.0,
            "Strategic Forecasting": int(request.form.get('skill_strat', 0)) / 100.0
        }
        twin.update_skills(skills)
        
        # 3. Capture Drivers & Vectors
        interests = [i.strip() for i in request.form.get('interests', '').split(',') if i.strip()]
        goals = [g.strip() for g in request.form.get('goals', '').split(',') if g.strip()]
        twin.set_interests(interests)
        twin.set_goals(goals)
        
        # 4. Capture Biometrics
        stress = int(request.form.get('bio_stress', 0)) / 100.0
        energy = int(request.form.get('bio_energy', 0)) / 100.0
        focus = int(request.form.get('bio_focus', 0)) / 100.0
        twin.update_biometrics(stress=stress, energy=energy, focus=focus)
        
        # Save to session (Fixes Concurrency Issue)
        session['twin_data'] = twin.to_dict()
        
        return redirect(url_for('dashboard'))
        
    return render_template('setup.html')

@app.route('/dashboard')
def dashboard():
    twin_data = session.get('twin_data')
    if not twin_data:
        return redirect(url_for('setup'))
    
    # Rehydrate Digital Twin from session
    twin = DigitalTwin.from_dict(twin_data)

    # 1. Digital Twin Data
    digital_signal = twin.get_digital_signal()
    
    # 2. Insights
    suggestions = insight_engine.analyze_architecture(twin)
    
    # 3. Predictions
    forecasts = prediction_engine.forecast_horizon(twin.get_skill_matrix())
    warnings = prediction_engine.analyze_biometrics(digital_signal["current_state"])
    
    # 4. Decision Simulation (Example Scenario)
    simulation = decision_simulator.compare_paths("Creative Director", "Engineering Manager")

    return render_template(
        'dashboard.html',
        twin=digital_signal,
        suggestions=suggestions,
        forecasts=forecasts,
        warnings=warnings,
        simulation=simulation
    )

@app.route('/reset')
def reset():
    session.pop('twin_data', None)
    return redirect(url_for('setup'))

@app.route('/api/simulation/simulate/<path_a>/<path_b>')
def simulate_decision(path_a, path_b):
    result = decision_simulator.compare_paths(path_a, path_b)
    return jsonify(result)

@app.route('/api/chat', methods=['POST'])
def chat():
    if 'twin_data' not in session:
        return jsonify({"error": "No active session"}), 403
    
    data = request.json
    user_input = data.get('message', '')
    
    # Rehydrate Twin
    twin = DigitalTwin.from_dict(session['twin_data'])
    
    # Process with Neural Interface
    response = neural_interface.process_input(user_input, twin)
    
    # Save updated state back to session
    session['twin_data'] = twin.to_dict()
    session.modified = True
    
    return jsonify({
        "response": response,
        "personality_state": twin.personality_matrix
    })

if __name__ == '__main__':
    # Debug=True is dangerous in production, but okay for dev.
    app.run(debug=True, port=5001)
