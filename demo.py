from TelemeterRC import TelemeterRcDaemon
import netifaces

if __name__ == "__main__":
    app = TelemeterRcDaemon("02c309816887", "02560a817385")
    app.push()
