class Stopwatch {
  constructor() {
    this.startTime = null;
    this.totalTime = 0;
  }

  start() {
    if (!this.startTime) {
      this.startTime = new Date();
    } else {
      console.log("Stopwatch is already running.");
    }
  }

  stop() {
    if (this.startTime) {
      let stopTime = new Date();
      let elapsedTime = stopTime - this.startTime;
      this.totalTime += elapsedTime;
      this.startTime = null;
      console.log("Elapsed time: " + elapsedTime + " milliseconds");
    } else {
      console.log("Stopwatch is not running.");
    }
  }

  reset() {
    this.startTime = null;
    this.totalTime = 0;
    console.log("Stopwatch reset.");
  }

  getTotalTime() {
    return this.totalTime;
  }
}

module.exports = Stopwatch;