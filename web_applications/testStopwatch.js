const Stopwatch = require("./utils/Stopwatch"); // Import the Stopwatch class

// Create a new instance of Stopwatch
const stopwatch = new Stopwatch();

// Start the stopwatch
stopwatch.start();

// Simulate some time passing (e.g., 3 seconds)
setTimeout(() => {
  // Stop the stopwatch after 3 seconds
  stopwatch.stop();

  // Get the total time spent
  const elapsedTime = stopwatch.getTotalTime();
  console.log("Total time spent: " + elapsedTime + " milliseconds");
}, 3000);
