from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.start()


def schedule_task(trigger_id, schedule):
    # Add logic to parse schedule and add jobs
    scheduler.add_job(
        func=lambda: execute_trigger(trigger_id),
        trigger="interval",  # Example: can be modified
        minutes=int(schedule),
    )


def execute_trigger(trigger_id):
    print(f"Executing Trigger ID: {trigger_id}")
