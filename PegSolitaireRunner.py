import logging

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]


if __name__ == "__main__":
    print("Hello, World!")