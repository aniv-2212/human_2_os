from typing import Dict, List, Any
import random

class DecisionSimulator:
    def __init__(self):
        pass

    def simulate_path(self, path_name: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulates a single decision path.
        """
        # Mock simulation logic
        outcome_prob = random.uniform(0.6, 0.95)
        financial_gain = random.randint(50, 200) # Arbitrary units
        intrinsic_score = self.calculate_intrinsic_motivation(path_name)

        return {
            "path": path_name,
            "success_probability": round(outcome_prob, 2),
            "projected_growth": f"+{financial_gain}%",
            "intrinsic_motivation_index": intrinsic_score,
            "outcome_summary": f"Path '{path_name}' leads to high stability but variable fulfillment."
        }

    def compare_paths(self, path_a: str, path_b: str) -> Dict[str, Any]:
        """
        Path Comparison: Simulates and compares two paths.
        """
        result_a = self.simulate_path(path_a, {})
        result_b = self.simulate_path(path_b, {})

        recommendation = path_a if result_a["intrinsic_motivation_index"] > result_b["intrinsic_motivation_index"] else path_b

        return {
            "path_a": result_a,
            "path_b": result_b,
            "recommendation": recommendation,
            "reasoning": f"Recommended {recommendation} based on higher Intrinsic Motivation Index."
        }

    def calculate_intrinsic_motivation(self, path_name: str) -> float:
        """
        Intrinsic Motivation Index: Measures alignment with internal drive.
        """
        # Mock scoring based on keywords
        if "Creative" in path_name or "Design" in path_name:
            return 0.92
        if "Management" in path_name:
            return 0.65
        return 0.75
