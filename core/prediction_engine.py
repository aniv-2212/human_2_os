from typing import Dict, List, Any
import random

class PredictionEngine:
    def __init__(self):
        pass

    def forecast_horizon(self, skills: Dict[str, float]) -> List[Dict[str, Any]]:
        """
        Horizon Forecasting: Predicts long-term career trajectories.
        """
        trajectories = [
            {
                "path": "Human-AI Interface Design",
                "probability": 0.0,
                "timeframe": "2027-2030"
            },
            {
                "path": "Neural Architecture Systems Lead",
                "probability": 0.0,
                "timeframe": "2028-2032"
            }
        ]

        # Simple logic to adjust probabilities based on skills
        if skills.get("Neural Architecture", 0) > 0.7:
             trajectories[1]["probability"] = 0.89
        else:
             trajectories[1]["probability"] = 0.45

        if skills.get("Systems Thinking", 0) > 0.6:
             trajectories[0]["probability"] = 0.84
        else:
             trajectories[0]["probability"] = 0.30
             
        return trajectories

    def analyze_biometrics(self, biometrics: Dict[str, float]) -> List[Dict[str, str]]:
        """
        Early Warning System: Detects subtle patterns in biometric data.
        """
        warnings = []
        stress = biometrics.get("stress_level", 0)
        energy = biometrics.get("energy_level", 1)

        if stress > 0.7 and energy < 0.4:
            warnings.append({
                "type": "Burnout Risk",
                "severity": "High",
                "message": "Elevated cortisol patterns detected combined with low energy recovery."
            })
        
        if stress < 0.3 and energy > 0.8:
             warnings.append({
                "type": "Optimal Flow",
                "severity": "Positive",
                "message": "Biometrics indicate peak neuroplasticity state."
            })
            
        return warnings
