import json
from datetime import datetime
import os

class HistoryManager:
    """Manage prediction history"""

    def __init__(self):
        self.history_file = os.path.join(
            os.path.dirname(__file__),
            '..',
            'data',
            'history.json'
        )
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)

    def add_prediction(self, patient_data, prediction_result, username=None):
        """Add a prediction to history"""
        history = self.load_history()

        entry = {
            'timestamp': datetime.now().isoformat(),
            'date': datetime.now().strftime("%B %d, %Y"),
            'time': datetime.now().strftime("%I:%M %p"),
            'username': username or 'guest',
            'prediction': prediction_result['prediction'],
            'risk_level': prediction_result['risk_level'],
            'confidence': round(prediction_result['confidence'], 1),
            'age': patient_data.get('age'),
            'gender': patient_data.get('gender'),
            'sleep_duration': patient_data.get('sleep_duration'),
            'stress_level': patient_data.get('stress_level', 0)
        }

        history.append(entry)
        self._save_history(history)
        return entry

    def load_history(self):
        """Load prediction history"""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except ValueError:
                return []
        return []

    def load_user_history(self, username):
        """Load history filtered by username"""
        all_history = self.load_history()
        return [h for h in all_history if h.get('username') == username]

    def _save_history(self, history):
        """Save history to file"""
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=2)

    def clear_history(self, username=None):
        """Clear all or user-specific history"""
        if username:
            history = self.load_history()
            remaining = [h for h in history if h.get('username') != username]
            self._save_history(remaining)
        else:
            self._save_history([])

    def get_latest(self, n=10, username=None):
        """Get latest n predictions globally or per user"""
        if username:
            history = self.load_user_history(username)
        else:
            history = self.load_history()
        return history[-n:][::-1]  # Return reversed (newest first)

