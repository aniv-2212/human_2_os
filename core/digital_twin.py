import json
from typing import Dict, List, Any

class DigitalTwin:
    def __init__(self, name: str):
        self.name = name
        self.traits = {
            "skills": {},
            "interests": [],
            "goals": []
        }
        self.biometrics = {
            "stress_level": 0.0,
            "energy_level": 1.0,
            "focus_metric": 0.0
        }
        # Memory & Adaptive Personality
        self.interaction_log = []
        self.personality_matrix = {
            "adaptability": 0.1,  # Grows with interaction
            "empathy": 0.1,       # Grows with positive sentiment
            "formality": 1.0,     # Decreases as rapport builds
            "symbiosis_index": 0.0 # Overall connection strength
        }

    def log_interaction(self, user_input: str, system_response: str, sentiment_score: float):
        """Records an interaction and evolves the personality."""
        self.interaction_log.append({
            "user": user_input,
            "system": system_response,
            "sentiment": sentiment_score
        })
        
        # Evolve Personality based on interaction
        self.personality_matrix["symbiosis_index"] = min(1.0, self.personality_matrix["symbiosis_index"] + 0.05)
        self.personality_matrix["adaptability"] = min(1.0, self.personality_matrix["adaptability"] + 0.02)
        
        # Adjust formality: More interactions = Less formal
        if len(self.interaction_log) > 5:
            self.personality_matrix["formality"] = max(0.2, self.personality_matrix["formality"] - 0.05)

    def update_skills(self, skills: Dict[str, float]):
        """
        Update the skill matrix. 
        Skills are rated from 0.0 to 1.0 (Dominance).
        Example: {"Neural Architecture": 0.85, "Systems Thinking": 0.92}
        """
        self.traits["skills"].update(skills)

    def set_interests(self, interests: List[str]):
        self.traits["interests"] = interests

    def set_goals(self, goals: List[str]):
        self.traits["goals"] = goals

    def update_biometrics(self, stress: float, energy: float, focus: float):
        self.biometrics = {
            "stress_level": stress,
            "energy_level": energy,
            "focus_metric": focus
        }

    def get_digital_signal(self) -> Dict[str, Any]:
        """
        Converts human traits into AI-readable signals.
        Returns a structured dictionary representing the Digital Twin Profile.
        """
        return {
            "identity_id": f"dt_{self.name.lower().replace(' ', '_')}",
            "neural_architecture": self.traits["skills"],
            "core_drivers": self.traits["interests"],
            "target_vectors": self.traits["goals"],
            "current_state": self.biometrics,
            "interaction_log": self.interaction_log,
            "personality_matrix": self.personality_matrix
        }

    def get_skill_matrix(self) -> Dict[str, float]:
        """
        Returns the Skill Dominance visualization data.
        """
        return self.traits["skills"]

    def to_dict(self) -> Dict[str, Any]:
        """Serialize state for session storage."""
        return {
            "name": self.name,
            "traits": self.traits,
            "biometrics": self.biometrics,
            "interaction_log": self.interaction_log,
            "personality_matrix": self.personality_matrix
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DigitalTwin':
        """Reconstruct object from session storage."""
        if not data:
            return None
        twin = cls(data["name"])
        twin.traits = data["traits"]
        twin.biometrics = data["biometrics"]
        twin.interaction_log = data.get("interaction_log", [])
        twin.personality_matrix = data.get("personality_matrix", {
            "adaptability": 0.1,
            "empathy": 0.1,
            "formality": 1.0,
            "symbiosis_index": 0.0
        })
        return twin
