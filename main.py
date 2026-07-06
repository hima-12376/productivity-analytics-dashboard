from tracker.tracker import Tracker


def main():

    tracker = Tracker()

    tracker.initialize()

    tracker.start_tracking()


if __name__ == "__main__":
    main()