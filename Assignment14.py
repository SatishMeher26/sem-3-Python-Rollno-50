
import logging
import logging.config
import logging.handlers
import os
import tempfile

LOG_DIR = tempfile.mkdtemp(prefix="logdemo_")


# 1. Logging Levels
def demo_levels():
    print("\n1. LOGGING LEVELS")

    log = logging.getLogger("levels")
    log.setLevel(logging.DEBUG)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    log.addHandler(h)

    log.debug("Debug message")
    log.info("Information message")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")

    log.setLevel(logging.WARNING)
    log.info("This message is hidden")


# 2. Formatter
def demo_formatter():
    print("\n2. FORMATTER")

    log = logging.getLogger("format")
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    ))
    log.addHandler(h)
    log.info("Formatted log message")


# 3. Handlers
def demo_handlers():
    print("\n3. HANDLERS")

    log = logging.getLogger("handlers")
    log.setLevel(logging.DEBUG)
    log.propagate = False

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    path = os.path.join(LOG_DIR, "app.log")
    file = logging.FileHandler(path)
    file.setLevel(logging.WARNING)

    log.addHandler(console)
    log.addHandler(file)

    log.debug("Debug message")
    log.info("Console message")
    log.warning("Warning saved in file")
    log.error("Error saved in file")

    for h in log.handlers:
        h.flush()
        h.close()
    log.handlers.clear()


# 4. Rotating File Handler
def demo_rotation():
    print("\n4. ROTATING FILE HANDLER")

    path = os.path.join(LOG_DIR, "rotate.log")

    h = logging.handlers.RotatingFileHandler(
        path, maxBytes=200, backupCount=2
    )

    log = logging.getLogger("rotate")
    log.setLevel(logging.INFO)
    log.addHandler(h)
    log.propagate = False

    for i in range(20):
        log.info("Log entry number %d", i)

    h.close()
    log.removeHandler(h)

    print("Rotating files:", os.listdir(LOG_DIR))


# 5. Logger Hierarchy
def demo_hierarchy():
    print("\n5. LOGGER HIERARCHY")

    parent = logging.getLogger("shop")
    parent.setLevel(logging.INFO)
    parent.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("%(name)s: %(message)s"))
    parent.addHandler(h)

    logging.getLogger("shop.cart").info("Item added")
    logging.getLogger("shop.pay").info("Payment accepted")


# 6. Exception Logging
def demo_exception():
    print("\n6. EXCEPTION LOGGING")

    log = logging.getLogger("errors")
    log.setLevel(logging.ERROR)
    log.propagate = False
    log.addHandler(logging.StreamHandler())

    try:
        10 / 0
    except ZeroDivisionError:
        log.exception("Division failed")


# 7. Logging Filter
class HideSecrets(logging.Filter):
    def filter(self, record):
        return "password" not in record.getMessage().lower()


def demo_filter():
    print("\n7. LOGGING FILTER")

    log = logging.getLogger("secure")
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()
    h.addFilter(HideSecrets())
    log.addHandler(h)

    log.info("User logged in")
    log.info("Password is 1234")
    log.info("Dashboard opened")


# 8. Lazy Formatting and Extra Fields
def demo_extra():
    print("\n8. LAZY FORMATTING")

    log = logging.getLogger("extras")
    log.setLevel(logging.INFO)
    log.propagate = False

    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter(
        "%(levelname)s user=%(user)s %(message)s"
    ))
    log.addHandler(h)

    log.info("Order %d placed, Rs.%.2f",
             42, 1999.5, extra={"user": "Rahul"})


# 9. Dictionary Configuration
def demo_dictconfig():
    print("\n9. DICTCONFIG")

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {"format": "%(levelname)s: %(message)s"}
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "level": "INFO"
            }
        },
        "loggers": {
            "configured": {
                "handlers": ["console"],
                "level": "INFO",
                "propagate": False
            }
        }
    }

    logging.config.dictConfig(config)
    logging.getLogger("configured").info("Configuration successful")


# MAIN PROGRAM
if __name__ == "__main__":
    demo_levels()
    demo_formatter()
    demo_handlers()
    demo_rotation()
    demo_hierarchy()
    demo_exception()
    demo_filter()
    demo_extra()
    demo_dictconfig()

    print("\nAll logging demonstrations completed!")
    print("Log files saved at:", LOG_DIR)
