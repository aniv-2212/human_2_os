from typing import List, Dict, Any
from .digital_twin import DigitalTwin

class InsightEngine:
    def __init__(self):
        pass

    def analyze_architecture(self, digital_twin: DigitalTwin) -> List[Dict[str, Any]]:
        """
        Proactive Growth: Analyzes Neural Architecture to provide suggestions.
        """
        signals = digital_twin.get_digital_signal()
        skills = signals["neural_architecture"]
        goals = signals["target_vectors"]
        
        suggestions = []

        # Simple logic to generate suggestions based on skill gaps or enhancements
        # In a real system, this would use a more complex AI model.
        
        if skills.get("Systems Thinking", 0) > 0.8:
            suggestions.append({
                "suggestion": "Lead a cross-functional architectural review",
                "reasoning": "High dominance in Systems Thinking (80%+) indicates readiness for high-level synthesis roles.",
                "type": "Enhancement"
            })
        
        if "AI Integration" not in skills or skills.get("AI Integration", 0) < 0.5:
            suggestions.append({
                "suggestion": "Deep dive into Human-AI Interface Design",
                "reasoning": "Detected gap in AI Integration relative to projected 2027 trends.",
                "type": "Growth"
            })

        return suggestions

    def get_reasoning_summary(self, suggestion_id: int) -> str:
        """
        Reasoning Summary: Provides detailed reasoning for a specific path.
        (Mock implementation)
        """
        return "Reasoning engine trace: Analyzed current skill vectors against 2030 industry probability map. Confidence: 94%."
