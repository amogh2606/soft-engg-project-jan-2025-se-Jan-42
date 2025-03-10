from apscheduler.schedulers.background import BackgroundScheduler
from app.ai_agent.faqs import update_faqs
import atexit


scheduler = BackgroundScheduler()

# scheduled job to update FAQs
def start_scheduler():
    scheduler.add_job(update_faqs, 'interval', hours=1, coalesce=True)
    scheduler.start()
    print("Scheduler has started")
    update_faqs()
    atexit.register(scheduler.shutdown)

