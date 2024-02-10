const readline = require('readline');

// Create interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to await user input
async function awaitKeyPress() {
  return new Promise((resolve) => {
    rl.question('Press any key to continue...', () => {
      resolve();
    });
  });
}
