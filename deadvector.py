import yaml
import random
import pathlib
from typing import Dict, List

class GameState:
    def __init__(self):
        self.difficulty = "medium"  # easy/medium/hard
        self.current_event = None

    def load_events(self) -> List[Dict]:
        """Load all YAML event files from events directory"""
        events = []
        events_dir = pathlib.Path("events")
        for event_file in events_dir.glob("*.yml"):
            if event_file.name == "event_template.yml":
                continue
            events.append(yaml.safe_load(event_file.read_text()))
        return events

    def select_random_event(self, events: List[Dict]) -> Dict:
        """Select a random event with weighted probability by severity"""
        weights = {
            "Minor": 0.4,
            "Major": 0.35,
            "Critical": 0.25
        }
        weighted_events = [
            (event, weights.get(event.get("severity", "Minor"), 0.4))
            for event in events
        ]
        return random.choices(
            [e[0] for e in weighted_events],
            weights=[e[1] for e in weighted_events],
            k=1
        )[0]

    def get_success_threshold(self) -> int:
        """Get success threshold based on difficulty"""
        return {
            "easy": 10,  # 55% success chance
            "medium": 12, # 45% success chance
            "hard": 14    # 35% success chance
        }[self.difficulty]

    def resolve_outcome(self, roll: int) -> str:
        """Determine outcome based on roll and difficulty"""
        threshold = self.get_success_threshold()
        if roll >= threshold + 7:
            return "critical_success"
        elif roll >= threshold:
            return "success"
        elif roll >= threshold - 5:
            return "partial_success"
        else:
            return "fail"

def run_test_session(game: GameState, events: List[Dict], num_tests: int = 50):
    """Run automated test session and print statistics"""
    results = {level: {
        "success": 0,
        "critical_success": 0,
        "partial_success": 0,
        "fail": 0
    } for level in ["easy", "medium", "hard"]}
    
    for level in results.keys():
        game.difficulty = level
        print(f"\nTesting {level} difficulty ({num_tests} rolls)...")
        
        for _ in range(num_tests):
            roll = random.randint(1, 20)
            outcome = game.resolve_outcome(roll)
            results[level][outcome] += 1
            
        # Print stats
        total = num_tests
        print(f"Success: {results[level]['success']}/{total} ({results[level]['success']/total:.0%})")
        print(f"Critical Success: {results[level]['critical_success']}/{total} ({results[level]['critical_success']/total:.0%})")
        print(f"Partial Success: {results[level]['partial_success']}/{total} ({results[level]['partial_success']/total:.0%})")
        print(f"Fail: {results[level]['fail']}/{total} ({results[level]['fail']/total:.0%})")

def main():
    print("Dead Vector - Ship Maintenance RPG")
    print("---------------------------------")
    print("Modes:")
    print("1. Normal play")
    print("2. Test mode (run all difficulties)")
    
    game = GameState()
    events = game.load_events()
    
    mode = input("Select mode (1/2): ")
    
    if mode == "2":
        run_test_session(game, events)
        return
        
    # Normal play mode
    difficulty_settings = {
        "easy": {"threshold": 10, "description": "Easy (55% success)"},
        "medium": {"threshold": 12, "description": "Medium (45% success)"},
        "hard": {"threshold": 14, "description": "Hard (35% success)"}
    }
    
    print("\nSelect difficulty:")
    for level, config in difficulty_settings.items():
        print(f"- {level}: {config['description']}")
        
    while True:
        game.difficulty = input("> ").lower()
        if game.difficulty in difficulty_settings:
            break
        print("Invalid choice. Please enter easy, medium, or hard")
    
    # Main game loop
    try:
        while True:
            game.current_event = game.select_random_event(events)
            print(f"\n[{game.current_event['subsystem']}] {game.current_event['ai_opening']}")
            
            input("\nPress Enter to roll...")
            roll = random.randint(1, 20)
            print(f"\nYou rolled: {roll}")
            
            outcome = game.resolve_outcome(roll)
            print(f"\n{game.current_event['narration'][outcome]}")
            print(f"\nOutcome: {outcome.replace('_', ' ').title()}")
            
            if input("\nContinue? (y/n): ").lower() != 'y':
                print("\nEnding game session...")
                break
                
    except KeyboardInterrupt:
        print("\n\nGame session interrupted")

if __name__ == "__main__":
    main()
