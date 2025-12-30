from typing import Dict, Any, Tuple
import random
from .digital_twin import DigitalTwin

class NeuralInterface:
    def __init__(self):
        self.positive_keywords = ["happy", "good", "great", "excited", "love", "thanks", "amazing", "progress"]
        self.negative_keywords = ["sad", "bad", "tired", "stressed", "angry", "fail", "stuck", "boring"]
        
    def process_input(self, user_input: str, twin: DigitalTwin) -> str:
        """
        Processes user input, updates the twin's state, and generates an adaptive response.
        """
        sentiment_score = self._analyze_sentiment(user_input)
        
        # Update Biometrics based on sentiment
        self._adjust_biometrics(twin, sentiment_score, user_input)
        
        # Generate Response
        response = self._generate_response(user_input, twin, sentiment_score)
        
        # Log Interaction
        twin.log_interaction(user_input, response, sentiment_score)
        
        return response

    def _analyze_sentiment(self, text: str) -> float:
        """Simple heuristic sentiment analysis (-1.0 to 1.0)."""
        text = text.lower()
        score = 0.0
        for word in self.positive_keywords:
            if word in text: score += 0.2
        for word in self.negative_keywords:
            if word in text: score -= 0.2
        return max(-1.0, min(1.0, score))

    def _adjust_biometrics(self, twin: DigitalTwin, sentiment: float, text: str):
        """Updates stress/energy based on conversation context."""
        current_stress = twin.biometrics["stress_level"]
        current_energy = twin.biometrics["energy_level"]
        
        if sentiment < -0.2:
            # Negative sentiment increases stress, lowers energy
            twin.update_biometrics(
                stress=min(1.0, current_stress + 0.1),
                energy=max(0.0, current_energy - 0.1),
                focus=twin.biometrics["focus_metric"]
            )
        elif sentiment > 0.2:
            # Positive sentiment reduces stress, boosts energy
            twin.update_biometrics(
                stress=max(0.0, current_stress - 0.1),
                energy=min(1.0, current_energy + 0.1),
                focus=twin.biometrics["focus_metric"]
            )

    def _generate_response(self, user_input: str, twin: DigitalTwin, sentiment: float) -> str:
        """Generates a response based on personality matrix."""
        p_matrix = twin.personality_matrix
        formality = p_matrix["formality"]
        symbiosis = p_matrix["symbiosis_index"]
        
        # 1. Check for specific queries first
        if "status" in user_input.lower():
            if formality > 0.7:
                return f"System Status: Nominal. Stress Level at {int(twin.biometrics['stress_level']*100)}%. Neural synchronization active."
            else:
                return f"You're doing okay. Stress is at {int(twin.biometrics['stress_level']*100)}%, but we can manage it."

        # 2. Adaptive Response Generation
        if formality > 0.8:
            # High Formality (Robotic, Precise)
            if sentiment < 0:
                return f"Negative variance detected. Re-calibrating biometric baselines. Recommended action: Cognitive break."
            else:
                return f"Input received. Data integrated into neural profile. Optimization vectors updated."
        
        elif formality > 0.4:
            # Medium Formality (Professional Assistant)
            if sentiment < 0:
                return f"I'm sensing some resistance in your inputs. I've adjusted your stress metrics. Perhaps we should review your goals?"
            else:
                return f"That sounds positive. I've updated your profile to reflect this momentum. Let's keep going."
        
        else:
            # Low Formality (Symbiotic Partner)
            if sentiment < 0:
                return f"I feel that. I've logged the stress spike, but hey—we've got this. Take a breath, and let's look at the long game."
            else:
                return f"Love the energy! This is exactly what helps the prediction engine grow. You're on a roll."

