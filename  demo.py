"""Quick demo runner for Titan Codyssey."""

from src.codyssey.engine import CodysseyEngine


def main():
    engine = CodysseyEngine(username="shivay")
    
    # Start Python lesson
    lesson_id = "py_hello"
    step = engine.start_lesson(lesson_id)
    print(f"🎯 Started: {engine.lessons[lesson_id].title}")
    
    # Submit all steps
    for s in engine.lessons[lesson_id].steps:
        print(f"\n✏️  {s.title}: {s.starter_code}")
        result = engine.submit_step(lesson_id, s.step_id, s.starter_code)
        print(f"   {'✅' if result['passed'] else '❌'} Output: {result['output']}")
        if result['commit']:
            print(f"   💾 Commit: {result['commit']['hash']}")
    
    # Stats
    stats = engine.get_user_stats()
    print(f"\n{'='*40}")
    print(f"📈 Level {stats['progress']['level']} | XP: {stats['progress']['xp']}")
    print(f"🔥 Streak: {stats['progress']['streak']} | Commits: {stats['progress']['total_commits']}")


if __name__ == "__main__":
    main()
